# nand2tetris


## Notes on Various Sections

### 6

This was pretty fun to write, the implementation is pretty straight forward. I didn't follow the books recommended approach and actually prefer my way a bit more. I also wrote some basic unit tests since it's not hard to understand the problem space beforehand.

### 7/8

My translator does not follow the recommended approach at all and I think this cost me quite a bit of time, taking this into account for future work...


### 10/11

The compiler also has a nice _eat method that is not required, but super helpful for validating you are actually consuming the expected token. Other than that it's a pretty direct implementation of how the book/videos recommend.

There are a lot of things here that are unpythonic, the code is not perfect by any means and could be refactored to be a lot cleaner. It's left this way primarily because I was trying to focus more on the course material on not so much writing idiomatic python.

### 12

Ended up skipping Screen, Output, and Keyboard classes from project 12 and sourcing them from [here](https://github.com/havivha/Nand2Tetris)

The Memory module passes the test but could use a defrag implementation, it's actually pretty clever imo and I haven't seen another implementation like it.

I really found myself wishing that I was implementation an actual operating system with a basic filesystem, process scheduling, memory management and other things I read about. Instead this felt like the bare minimum required to work with RAM and the rest being a standard library for the hack language.

The rest of the work is my own