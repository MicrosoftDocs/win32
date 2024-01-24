---
description: Deletes a user from the volume.
ms.assetid: 56a07388-b7d8-41a4-b29a-8a57fe0b9d19
title: DiskQuotaControl.DeleteUser method (Dskquota.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.DeleteUser
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.DeleteUser method

Deletes a user from the volume.

## Syntax


```JScript
DiskQuotaControl.DeleteUser(
  oUser
)
```



## Parameters

<dl> <dt>

*oUser* 
</dt> <dd>

Type: **Object**

An object expression that evaluates to the user's [**DIDiskQuotaUser**](didiskquotauser-object.md) object.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method fails if the user owns any storage on the volume. Before you delete a user from a volume, all storage for that user must be deleted, be moved to another volume, or have its ownership transferred to another user.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Dskquota.h</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**AddUser**](diskquotacontrol-adduser.md)
</dt> <dt>

[**DiskQuotaControl**](diskquotacontrol-object.md)
</dt> </dl>

 

 




