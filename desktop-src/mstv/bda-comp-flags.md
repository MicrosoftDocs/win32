---
title: BDA\_Comp\_Flags enumeration
description: Defines flags for the IBDAComparable interface.
ms.assetid: 3bf4b82d-29d2-442e-ad20-bdb7ef66dfb5
keywords:
- BDA_Comp_Flags enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- BDA_Comp_Flags
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BDA\_Comp\_Flags enumeration

Defines flags for the [**IBDAComparable**](/windows/previous-versions/tuner/nn-tuner-ibdacomparable?branch=master) interface.

## Syntax


```C++
typedef enum  { 
  BDACOMP_NOT_DEFINED               = 0x00000000,
  BDACOMP_EXCLUDE_TS_FROM_TR        = 0x00000001,
  BDACOMP_INCLUDE_LOCATOR_IN_TR     = 0x00000002,
  BDACOMP_INCLUDE_COMPONENTS_IN_TR  = 0x00000004
} BDA_Comp_Flags;
```



## Constants

<dl> <dt>

<span id="BDACOMP_NOT_DEFINED"></span><span id="bdacomp_not_defined"></span>**BDACOMP\_NOT\_DEFINED**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="BDACOMP_EXCLUDE_TS_FROM_TR"></span><span id="bdacomp_exclude_ts_from_tr"></span>**BDACOMP\_EXCLUDE\_TS\_FROM\_TR**
</dt> <dd>

Exclude the tuning space from the comparison.

</dd> <dt>

<span id="BDACOMP_INCLUDE_LOCATOR_IN_TR"></span><span id="bdacomp_include_locator_in_tr"></span>**BDACOMP\_INCLUDE\_LOCATOR\_IN\_TR**
</dt> <dd>

Include the locator in the comparison.

</dd> <dt>

<span id="BDACOMP_INCLUDE_COMPONENTS_IN_TR"></span><span id="bdacomp_include_components_in_tr"></span>**BDACOMP\_INCLUDE\_COMPONENTS\_IN\_TR**
</dt> <dd>

Include components in the comparison.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h</dt> </dl> |



## See also

<dl> <dt>

[BDA Enumeration Types](bda-types.md)
</dt> <dt>

[**IBDAComparable**](/windows/previous-versions/tuner/nn-tuner-ibdacomparable?branch=master)
</dt> </dl>

 

 





