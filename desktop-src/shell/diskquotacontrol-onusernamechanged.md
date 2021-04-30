---
description: Occurs when the name information for a DIDiskQuotaUser object has been resolved.
ms.assetid: df32cb17-ad90-4535-a36b-60c5b4e9999f
title: OnUserNameChanged function (Dskquota.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OnUserNameChanged
api_type: 
- DllExport
api_location: 
- Shell32.dll
---

# OnUserNameChanged function

Occurs when the name information for a [**DIDiskQuotaUser**](didiskquotauser-object.md) object has been resolved.

## Parameters

<dl> <dt>

*oUser* 
</dt> <dd>

The **Object** that evaluates to the [**DIDiskQuotaUser**](didiskquotauser-object.md) object associated with the user whose name has been resolved.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

When a client [**enumerates users**](didiskquotauser-object.md), or calls the [**AddUser**](diskquotacontrol-adduser.md) or [**FindUser**](diskquotacontrol-finduser.md) method, the user name must be resolved to the associated security ID (SID). Because this procedure can be time-consuming, a client can have name resolution done asynchronously on a background thread. When a user's name is resolved, the [**DiskQuotaControl**](diskquotacontrol-object.md) object notifies its client by firing the **OnUserNameChanged** event. A **DIDiskQuotaUser** object associated with the user is passed as a parameter. This object allows the client to modify the user's quota settings.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Dskquota.h</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




