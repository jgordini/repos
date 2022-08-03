<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
⊃ b ⍝ First
(⊃⌽∘,)b ⍝ Last
⊣⌿b ⍝ Top Row
⊢⌿b ⍝ Bottom Row
⊣/b ⍝ First Column
⊢/b ⍝ Last Column
(⊂≢⊆)b ⍝ Nested Array?
(⊂≡⊆)b ⍝ Simple Array?
∊b ⍝ Flatten Array 
c∘≡¨d ⍝ Match ie. string equal
(⊃0∘⍴)c ⍝ Fill - convert char to space num to 0
⍪e ⍝ Vector into 1 column matrix
↓b ⍝ Matrix to Row Vector
(↓⍉)b ⍝ Matrix to Column Vector
↓f ⍝ Split (3dim or opt. Axis ex. ↓2 5⍴⍳10)
↑b ⍝ Mix: Remove nesting (num) or  Row Vectors to Matrix
↑a b ⍝ Row Table
⍉↑a b ⍝ Column Table
b,a ⍝ add b to end of vector
b~a ⍝ remove b from a vector
b,[0.5]a ⍝ Lamination with Fractional Axis Specification
⌊0.5+a ⍝ Round
(⊂∘⍋⌷⊢)a ⍝ Sort Ascending
(⊂∘⍒⌷⊢)a ⍝ Sort Descending
≠a ⍝ Unique Mask
∪b ⍝ Return Unique Rows in Matrix or Unique items in Vector - de-dupe
⊢∘≢⌸a ⍝ Unique Count
+/a∘.≡b ⍝ Count Occourences
 ⊂a ⍝ Enclose - Scalarize
 +⍀a ⍝ Scan - Returns an array - Itterates over each [axis]
 +⌿a ⍝ Reduce - Returns the result of Scan [axis]
 2+⌿a ⍝ Pair-wise (Windowed Reduction) sum the first group of 2 then next 2
(⍳a)∘=⍳a ⍝ Identity Matrix
X⊃¨∘⊂Y ⍝ Chipmunk - Selective Picking from Array
X f@(1↑⍨∘-≢)Y ⍝ Apply function f(x) to last cell of Y
a∘.×b ⍝ Vector Outer Product
a∘.,b ⍝ Cartesian product: all pairs of X and Y
(⍳∘≢,⊢)b ⍝ Row Numbers Matrix
a≠a ⍝ Keep structure replace with Zero
10⊥⍣¯1⊢ ⍝ Split a scalar into a vector (⊤ Vector to Scalar)

</body>
</html>