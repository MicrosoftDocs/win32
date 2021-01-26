---
title: WCS\_PROFILE\_MANAGEMENT\_SCOPE enumeration
description: Specifies the scope of a profile management operation, such as associating a profile with a device.
ms.assetid: 6895a807-81da-4263-b370-977ecfaffac8
keywords:
- WCS_PROFILE_MANAGEMENT_SCOPE enumeration Windows Color System
topic_type:
- apiref
api_name:
- WCS_PROFILE_MANAGEMENT_SCOPE
api_location:
- Icm.h
api_type:
- HeaderDef
ms.localizationpriority: high


ms.topic: enumeration
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# WCS\_PROFILE\_MANAGEMENT\_SCOPE enumeration

Specifies the scope of a profile management operation, such as associating a profile with a device.

## Syntax


```C++
typedef enum tagWCS_PROFILE_MANAGEMENT_SCOPE { 
  WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE,
  WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER
} WCS_PROFILE_MANAGEMENT_SCOPE;
```



## Constants

<dl> <dt>

<span id="WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE"></span><span id="wcs_profile_management_scope_system_wide"></span>**WCS\_PROFILE\_MANAGEMENT\_SCOPE\_SYSTEM\_WIDE**
</dt> <dd>

Indicates that the profile management operation affects all users.

</dd> <dt>

<span id="WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER"></span><span id="wcs_profile_management_scope_current_user"></span>**WCS\_PROFILE\_MANAGEMENT\_SCOPE\_CURRENT\_USER**
</dt> <dd>

Indicates that the profile management operation affects only the current user.

</dd> </dl>

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



 

 





