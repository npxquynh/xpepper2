### How did it feel to work with such fast, comprehensive tests?
I'm more confident in refactoring, and know that the test will caught errors

### Did you make mistakes while refactoring that were caught by the tests?
I did. I outputted "Advantage for player1" instead of "Advantage player 1"

Also I found that the SetP1Score() in TennisGame2 wasn't covered by test. So I added one for it.

### If you used a tool to record your test runs, review it. Could you have taken smaller steps? Made fewer refactoring mistakes?
I didn't use any tool to record test runs.

I tried to refactor a little bit each time, and focus on one specific problem. Then I run test before commit those small changes.

### Did you ever make any refactoring mistakes and then back out your changes? How did it feel to throw away code?
I did. At that time I made some mistake with "Find and Replace", and it's just easy to revert to the original version and "Find and Replace" again. Afterthat, I commit code much more usual.

### What would you say to your colleague if they had written this code?
First of all, I think they should follow the Python Style Guide, and make all the naming consistent. About the logic of the program, there are many places that it can be simplified to make the code clearer to read and understand.

### What would you say to your boss about the value of this refactoring work? Was there more reason to do it over and above the extra billable hour or so?

