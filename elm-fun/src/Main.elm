module Main exposing (..)
import Html exposing (..)
import Html.Attributes exposing (..)

view model = 
    div [class "jumbo"] 
        [h1 [] [text "Welcome to my page"]]

main =
    view "model"