module Utils where

import Text.Read

-- getInput reads from a file path and returns the output as a list of strings 
getInput :: FilePath -> IO [String]
getInput path = do
    contents <- readFile path
    return $ lines contents

inputToInteger :: [String] -> [Maybe Int]
inputToInteger = map readMaybe 

-- reads till a specified character; return portion of string before/after 
readTill :: Char -> String -> (String, String)
readTill c "" = ("", "")
readTill c s = readTill' c s ""
    where 
        readTill' :: Char -> String -> String -> (String, String)
        readTill' c "" readString = (readString, "")
        readTill' c (first: rest) readString 
            | c == first = (readString, rest)
            | otherwise = readTill' c rest (readString ++ [first])