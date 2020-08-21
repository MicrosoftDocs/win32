---
title: Function Return Values
description: Function return values are similar to \ out\ -only parameters because their data is not provided by the client application.
ms.assetid: 98d8d228-7222-49bf-9f29-7749a7a76d5a
ms.topic: article
ms.date: 05/31/2018
---

# Function Return Values

Function return values are similar to **\[out\]**-only parameters because their data is not provided by the client application. However they are managed differently. Unlike **\[out\]**-only parameters, they are not required to be pointers. The remote procedure can return any valid data type except reference pointers and nonencapsulated unions.

However, using an **\[out\]** parameter instead of a return value for complex data types is recommended. While returning complex data types, the MIDL compiler will generate an /Os mode stub. As a result, all recent error-checking information provided by /robust is lost.

Function return values that are pointer types are allocated by the client stub with a call to [midl\_user\_allocate](/windows/desktop/Midl/midl-user-allocate-1). Accordingly, only the unique or full pointer attribute can be applied to a pointer function-return type.

 

 