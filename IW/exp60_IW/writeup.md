# Exp60

## Description
```
We are given an IP address and a port to connect to, upon connecting we are asked to solved the following equation:
	X > 1337
	X * 7 + 4 = 1337
```

## Solution

It is pretty obvious that we to do an integer overflow, after some manual testing I used the following dirty C code:

```
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	int x = 610000000;
	int i = 0;
	for (i; i<100000000; i++) {
		if ((x+i)*7 + 4 == 1337) printf("%d", i);
	}
}
```

which gives us the answer: 613566947

## Results
```
Solve the following equations:
X > 1337
X * 7 + 4 = 1337
Enter the solution X: 613566947
You entered: 613566947
613566947 is bigger than 1337
1337 is equal to 1337
Well done!
IW{Y4Y_0verfl0w}
```