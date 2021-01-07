---
description: TAPI 1.4 added a number of APIs, messages, constants, and structure elements to the 1.3 specification.
ms.assetid: 293f732f-0288-46d1-b542-d948c6179158
title: TAPI 1.4
ms.topic: article
ms.date: 05/31/2018
---

# TAPI 1.4

TAPI 1.4 added a number of APIs, messages, constants, and structure elements to the 1.3 specification. TAPI 1.4 supports only 16-bit TSPs. However, it does allow 32-bit applications to be developed without having to worry about the limitations of 16-bit Windows.

The TAPI and TSPI header files are used to develop both applications for both TAPI 1.4 and TAPI 2.x. While there were not many changes to the structures between these two specifications, there were changes to the API (specifically, Unicode support) that make it very important to note that the headers compile differently, depending on the TAPI\_CURRENT\_VERSION constant. For example:

``` syntax
#define TAPI_CURRENT_VERSION 0x00010004
#include <tapi.h>
```

> [!Note]  
> TAPI\_CURRENT\_VERSION should be defined for all TAPI applications. While it is not strictly necessary for TAPI 2.x development, future changes could occur to require this.

 

 

 



