---
Description: All of the examples in the Cryptography SDK documentation are assumed to have the following \#include and \#define compiler directives.
ms.assetid: 98f85e7d-e557-4dde-b510-891b37daec87
title: '\#includes and \#defines'
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# \#includes and \#defines

All of the examples in the Cryptography SDK documentation are assumed to have the following **\#include** and **\#define** compiler directives.


```C++
#include <stdio.h>
#include <windows.h>
#include <Wincrypt.h>
#define MY_ENCODING_TYPE  (PKCS_7_ASN_ENCODING | X509_ASN_ENCODING)
```



Additionally, the **\_WIN32\_WINNT** constant must be appropriately defined. For more information about **\_WIN32\_WINNT**, see [Using the Windows Headers](winprog.using_the_windows_headers).

 

 



