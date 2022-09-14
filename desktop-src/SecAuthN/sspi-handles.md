---
description: Lists the handles used by the SSPI API.
ms.assetid: 94b622d0-7c04-4513-841f-0df9b5d49136
title: SSPI Handles
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Handles

SSPI uses the following handle types and pointer to these handles:

-   **SecHandle** and **PSecHandle**
-   **CredHandle** and **PCredHandle**
-   **CtxtHandle** and **PCtxtHandle**

These handle types and pointers to these handle types are defined as follows.


```C++
typedef struct _SecHandle {
  ULONG_PTR       dwLower;
  ULONG_PTR       dwUpper;
} SecHandle, * PSecHandle;

typedef SecHandle    CredHandle;
typedef PSecHandle   PCredHandle;

typedef SecHandle    CtxtHandle;
typedef PSecHandle   PCtxtHandle;
```



 

 



