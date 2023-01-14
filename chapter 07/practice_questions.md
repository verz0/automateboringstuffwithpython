1. re.compile()

2. If not, backslashes should be escaped

3. matched objects

4. By using group()

5. group 0 : (\d\d\d)-(\d\d\d-\d\d\d\d)
   group 1 : (\d\d\d)
   group 2 : (\d\d\d-\d\d\d\d)

6. by using \ to escape them

7. by using groups in the regex code

8. it signifies "or"

9. non greedy matching and to match one group

10. "+" : matches one or more
    "*" : matches zero or more

11. {3} : matches 3 elements
    {3,5} : matches 3 - 5 elements

12. \d : digit
    \w : word
    \s : space

13. \D : not a digit
    \W : not a word
    \S : not a space

14. .* : greedy matching
    .*? : non greedy matching

15. [0-9] and [a-z]

16. by using re.I

17. . character matches anything while re.DOTALL matches anything including a new line if passed as a second argument

18. X drummers, X pipers, five rings, X hens

19. adds space

20. re.compile(r'^\d{1,3}(,\d{3})*$' )

21. re.compile(r'[A-Z][a-z]*\sWatanabe')

22.  re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)