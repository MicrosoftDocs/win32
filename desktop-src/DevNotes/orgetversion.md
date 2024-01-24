---
description: This function retrieves the version of the offline registry library.
ms.assetid: 625f088a-db5e-47ea-aa48-39b1c70cf15b
title: ORGetVersion function (Offreg.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ORGetVersion
api_type: 
- DllExport
api_location: 
- Offreg.dll
---

# ORGetVersion function

This function retrieves the version of the offline registry library.

## Syntax


```C++
VOID ORGetVersion(
  _Out_ PDWORD pdwMajorVersion,
  _Out_ PDWORD pdwMinorVersion
);
```



## Parameters

<dl> <dt>

*pdwMajorVersion* \[out\]
</dt> <dd>

A pointer to a variable to receive the major version of the offline registry library. For the initial release of the library, the value is 1.

</dd> <dt>

*pdwMinorVersion* \[out\]
</dt> <dd>

A pointer to a variable to receive the minor version of the offline registry library. For the initial release of the library, the value is 0.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|----------------------------|---------------------------------------------------------------------------------------|
| Redistributable<br/> | Windows Offline Registry library version 1.0 or later<br/>                      |
| Header<br/>          | <dl> <dt>Offreg.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Offreg.dll</dt> </dl> |



 

 




