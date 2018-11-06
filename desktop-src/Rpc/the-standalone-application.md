---
title: The Standalone Application
description: This standalone application, which consists of a call to a single function, forms the basis of our distributed application.
ms.assetid: 640f5d01-84c8-4fe8-9dae-f4d55cc6f06b
ms.topic: article
ms.date: 05/31/2018
---

# The Standalone Application

This standalone application, which consists of a call to a single function, forms the basis of our distributed application. The function, **HelloProc**, is defined in its own source file so that it can be compiled and linked with either a standalone application or a distributed application.


```C++
/* file hellop.c */
#include <stdio.h>
#include <windows.h>

void HelloProc(char * pszString)
{
    printf("%s\n", pszString);
}
 
/* file: hello.c, a stand-alone application */
#include "hellop.c"

void main(void)
{
    char * pszString = "Hello, World";
    HelloProc(pszString);
}
```



 

 




