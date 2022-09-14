---
title: /msc_ver switch
description: The /msc\_ver switch is used to allow MIDL to generate code that includes optimizations for different versions of Microsoft C/C++ compilers.
ms.assetid: cdcb8f3e-e791-44c2-8bea-e77f94cc1682
keywords:
- /msc_ver switch MIDL
topic_type:
- apiref
api_name:
- /msc_ver
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /msc\_ver switch

The **/msc\_ver** switch is used to allow MIDL to generate code that includes optimizations for different versions of Microsoft C/C++ compilers.

``` syntax
midl /msc_ver version_number
```

## Switch Options

<dl> <dt>

*version\_number* 
</dt> <dd>

Specifies an integer version number of the Microsoft Visual C++ compiler that will be used to compile the client and server stubs of the distributed application. The default version number is 1100, which corresponds to Visual C++ version 5.0. The version number 1200 corresponds to Visual C++ version 6.0, and so on.

</dd> </dl>

## Remarks

In particular, version values of 1100 or greater cause the MIDL compiler to generate code utilizing the **\_\_declspec(uuid())** directive. It also activates macros that use the **\_\_declspec(selectany)** and **\_\_declspec(novtable)** directives.

 

 




