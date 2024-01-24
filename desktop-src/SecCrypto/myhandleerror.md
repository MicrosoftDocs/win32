---
description: The MyHandleError function is an example of a tool function used to print an error message and exit the calling program.
ms.assetid: 7b28509f-a77f-4b60-90d4-18edaa6d1a2d
title: MyHandleError
ms.topic: article
ms.date: 05/31/2018
---

# MyHandleError

The **MyHandleError** function is an example of a tool function used to print an error message and exit the calling program. The examples for several CryptoAPI functions in [Cryptography Reference](cryptography-reference.md) and the more extended examples in [Using Cryptography](using-cryptography.md) implement this function. Real applications may require more complex error handling capability.


```C++
#include <stdio.h>
#include <tchar.h>
#include <windows.h>

void MyHandleError(LPTSTR psz)
{
    _ftprintf(stderr, TEXT("An error occurred in the program. \n"));
    _ftprintf(stderr, TEXT("%s\n"), psz);
    _ftprintf(stderr, TEXT("Error number %x.\n"), GetLastError());
    _ftprintf(stderr, TEXT("Program terminating. \n"));
    exit(1);
} // End of MyHandleError

```



 

 



