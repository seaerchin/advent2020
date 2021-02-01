module Eight.Eight where

import Utils 
import Text.Parsec hiding (count, parse, uncons, getInput)
import qualified Text.Parsec as Parsec 
import Data.Either ( rights )
import Data.Map ((!))
import qualified Data.Map as M

data Sign = Negative | Positive
data Instruction = NOP | ACC | JMP Sign Int 

driver = do 
    input <- getInput "data.txt"
    let parsed = rights $ map (parse instruction) input 
    print parsed

    return ()

-- acc -> ptr -> ... 
exec :: Int -> Int -> Instruction -> (Int, Int) 
exec x ptr NOP = (x, ptr) 
exec x ptr ACC = (x + 1, ptr) 
exec x ptr (JMP Negative y) = (x, ptr - y)
exec x ptr (JMP Positive y) = (x, ptr + y)

-- we wrap exec in a map 
-- for every ptr value, we will check if it is executed before
-- if yes nvm
-- otherwise, return that value
wrapped :: (Int, Int) -> M.Map Int Bool -> [Instruction] -> Int
wrapped (acc, ptr) m input
    | ptr `M.member` m = acc 
    | otherwise = wrapped (acc', ptr') m' input
        where 
            (acc', ptr') = exec acc ptr curIns 
            curIns = input !! ptr
            m' = M.insert ptr True m

-- an instruction is a series of words then an instruction followed by a sign 
instruction :: Parser (String, String) 
instruction = do 
    instruction <- many1 letter 
    char ' '
    sign <- char '+' <|> char '-'
    nums <- many1 digit
    return (instruction, sign: nums) 