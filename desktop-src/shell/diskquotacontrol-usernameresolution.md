---
description: Sets or gets a value that controls how user security identifier (SID) are resolved to user names.
title: DiskQuotaControl.UserNameResolution property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.UserNameResolution
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: dc936421-e66d-4762-912a-c586f9cdace4
api_name: 
 - DiskQuotaControl.UserNameResolution
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DiskQuotaControl.UserNameResolution property

Sets or gets a value that controls how user security identifier (SID) are resolved to user names.

This property is read/write.

## Syntax


```JScript
iUserNameResolution = DiskQuotaControl.UserNameResolution
DiskQuotaControl.UserNameResolution = iUserNameResolution
```



## Property value

This property can be set to one of the following values.



| Resolution Type | Value | Description                                                                                                                                              |
|-----------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| dqResolveNone   | 0     | Do not resolve user name information.                                                                                                                    |
| dqResolveSync   | 1     | Wait while resolving name information.                                                                                                                   |
| dqResolveAsync  | 2     | Do not wait while resolving name information. The [**OnUserNameChanged**](diskquotacontrol-onusernamechanged.md) event fires when the name is resolved. |



 

## Remarks

This property affects the enumeration of [**DIDiskQuotaUser**](didiskquotauser-object.md) objects, and the [**AddUser**](diskquotacontrol-adduser.md) and [**FindUser**](diskquotacontrol-finduser.md) methods.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




