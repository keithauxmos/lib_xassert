// Copyright (c) 2015-2016, XMOS Ltd, All rights reserved
#include <xassert.h>

void f(int x) {
  unreachable();
}

int main() {
  f(0);
  return 0;
}