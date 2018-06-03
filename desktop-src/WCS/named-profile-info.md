---
title: NAMED\_PROFILE\_INFO structure
description: The NAMED\_PROFILE\_INFO structure is used to store information about a named color profile.
ms.assetid: decb0b76-872c-4237-a2b0-6da83d49c8cf
keywords:
- NAMED_PROFILE_INFO structure Windows Color System
topic_type:
- apiref
api_name:
- NAMED_PROFILE_INFO
api_location:
- Icm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# NAMED\_PROFILE\_INFO structure

The **NAMED\_PROFILE\_INFO** structure is used to store information about a named color profile.

## Syntax


```C++
typedef struct tagNAMED_PROFILE_INFO {
  DWORD      dwFlags;
  DWORD      dwCount;
  DWORD      dwCountDevCoordinates;
  COLOR_NAME szPrefix;
  COLOR_NAME szSuffix;
} NAMED_PROFILE_INFO;
```



## Members

<dl> <dt>

**dwFlags**
</dt> <dd>

Not currently used by the default CMM.

</dd> <dt>

**dwCount**
</dt> <dd>

Total number of named colors in the profile.

</dd> <dt>

**dwCountDevCoordinates**
</dt> <dd>

Total number of device coordinates for each named color.

</dd> <dt>

**szPrefix**
</dt> <dd>

Pointer to a string containing the prefix for each color name.

</dd> <dt>

**szSuffix**
</dt> <dd>

Pointer to a string containing the suffix for each color name.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



 

 





