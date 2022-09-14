---
description: After you have created a DLL, you can use the functions it defines in an application. The following is a simple console application that uses the myPuts function exported from Myputs.dll (see Creating a Simple Dynamic-Link Library).
ms.assetid: d67000c2-21ca-49c2-86f1-708f33003d1e
title: Using Load-Time Dynamic Linking
ms.topic: article
ms.date: 05/31/2018
---

# Using Load-Time Dynamic Linking

After you have created a DLL, you can use the functions it defines in an application. The following is a simple console application that uses the myPuts function exported from Myputs.dll (see [Creating a Simple Dynamic-Link Library](creating-a-simple-dynamic-link-library.md)).

Because this example calls the DLL function explicitly, the module for the application must be linked with the import library Myputs.lib. For more information about building DLLs, see the documentation included with your development tools.


```C++
#include <windows.h> 

extern "C" int __cdecl myPuts(LPCWSTR);   // a function from a DLL

int main(VOID) 
{ 
    int Ret = 1;

    Ret = myPuts(L"Message sent to the DLL function\n"); 
    return Ret;
}
```



## Related topics

<dl> <dt>

[Load-Time Dynamic Linking](load-time-dynamic-linking.md)
</dt> </dl>

 

 



