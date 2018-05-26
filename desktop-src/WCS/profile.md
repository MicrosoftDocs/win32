---
title: PROFILE structure
description: The PROFILE structure contains information that defines a color profile. See Using Device Profiles with WCS for more information.
ms.assetid: 49656afa-64fc-4421-8948-34a65c9f829e
keywords:
- PROFILE structure Windows Color System
topic_type:
- apiref
api_name:
- PROFILE
api_location:
- Icm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PROFILE structure

The **PROFILE** structure contains information that defines a color profile. See [Using Device Profiles with WCS](using-device-profiles-with-wcs.md) for more information.

## Syntax


```C++
typedef struct tagPROFILE {
  DWORD dwType;
  PVOID pProfileData;
  DWORD cbDataSize;
} PROFILE;
```



## Members

<dl> <dt>

**dwType**
</dt> <dd>

Must be set to one of the following values.



| Value              | Meaning                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------|
| PROFILE\_FILENAME  | Indicates that the **pProfileData** member contains a null-terminated string that holds the name of a device profile file. |
| PROFILE\_MEMBUFFER | Indicates that the **pProfileData** member contains a pointer to a device profile in a memory buffer.                      |



 

</dd> <dt>

**pProfileData**
</dt> <dd>

The contents of this member is indicated by the **dwTYPE** member. It will either be a pointer to a null-terminated string containing the file name of the device profile, or it will be a pointer to a buffer in memory containing the device profile data.

</dd> <dt>

**cbDataSize**
</dt> <dd>

The size in bytes of the data buffer pointed to by the **pProfileData** member.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[Using Device Profiles with WCS](using-device-profiles-with-wcs.md)
</dt> </dl>

 

 





