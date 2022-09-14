---
description: Represents a package of four calls.
MS-HAID: vspixengine.PackedCallPkg
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PackedCallPkg structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: BE345C1A-9F6E-4FE0-99C7-6B332A1ED079
api_name: 
 - PackedCallPkg
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.packedcallpkg"></span>PackedCallPkg structure

Represents a package of four calls.

## Syntax


```C++
typedef struct PackedCallPkg {
  UINT pcp1;
  UINT pcp2;
  UINT pcp3;
  UINT pcp4;
} PackedCallPkg;
```

## Members

**pcp1**  
The first call in the package.

**pcp2**  
The second call in the package.

**pcp3**  
The third call in the package.

**pcp4**  
The fourth call in the package.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



