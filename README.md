
# Eco
Eco is a stack-based esoteric programming language that was made by **Notxnorand** on **March 27 2026**
<br><br>
## Commands
The Eco command list contains the following:<br><br>
* **PUSH X**<br>
Pushes a specified value onto the stack.<br>
* **POP**<br>
Pops the top value off the stack.<br>
* **PRTINT**<br>
Pops the top value off the stack and prints it as an integer.<br>
* **PRTCHR**<br>
Pops the top value off the stack and prints it as its ASCII value.<br>
* **INTIN**<br>
Retrieves an integer from the user and pushes it onto the stack, pushing 0 as a fallback.<br>
* **CHRIN**<br>
Retrieves an ASCII character from the user and pushes it onto the stack, pushing 0 as a fallback.<br>
* **DUP**<br>
Duplicates the top value onto the stack.<br>
* **IF**<br>
Skips the next command if the top value on the stack is 0, doesn't pop.<br>
* **GOTO X**<br>
Jumps to the specified line number, 1-indexed.<br>
* **REV**<br>
Swaps the top 2 values on the stack.<br>
* **FETCH X**<br>
Pops the value relative to the top of the stack and pushes it to the top.<br>
* **ADD**<br>
Pops the top 2 values on the stack, adds them, and pushes the result.<br>
* **SUB**<br>
Pops the top 2 values from the stack, subtracts them, taking the top from the second, and pushes the result.<br>
* **MUL**<br>
Pops the top 2 values on the stack, multiplies them, and pushes the result.<br>
* **DIV**<br>
Pops the top 2 values on the stack, with the top value dividing the second, and pushes the result.<br>
* **EQL**<br>
Pops the top 2 values on the stack, if they are equal, push 1, else push 0.<br>
<br>
Every command requires an operand, or a dummy operand for those without one.<br>
Anything following a `#` (with a preceding space) is ignored. Comments can also be placed directly after an operand.
