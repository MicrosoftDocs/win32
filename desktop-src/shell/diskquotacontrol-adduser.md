---
description: Assigns a nondefault disk quota to a new user.
title: DiskQuotaControl.AddUser method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.AddUser
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: de20d016-83da-42ac-962f-86faf9b25419

---

# DiskQuotaControl.AddUser method

Assigns a nondefault disk quota to a new user.

## Syntax


```JScript
objRetVal = DiskQuotaControl.AddUser(
  sLogonName
)
```



## Parameters

<dl> <dt>

*sLogonName* 
</dt> <dd>

Type: **CHAR**

A string value that contains the user's logon name. Use the [**UserNameResolution**](diskquotacontrol-usernameresolution.md) property to specify how the name is to be resolved.

</dd> </dl>

## Return value

Type: **Object**

Returns an object expression that evaluates to the user's [**DIDiskQuotaUser**](didiskquotauser-object.md) object.

## Remarks

The NTFS file system automatically creates a user quota entry when a user first writes to the volume. Entries that are created in this way are assigned the default warning threshold and hard quota limit values for the volume. This method allows you to create a user quota entry before a user writes information to the volume. It returns a [**DIDiskQuotaUser**](didiskquotauser-object.md) object that can be used to assign a warning threshold or quota limit value that differs from the default settings for the volume.

If the user already exists, no new entry is created. The method returns the [**DIDiskQuotaUser**](didiskquotauser-object.md) object associated with the existing entry.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DefaultQuotaLimit**](diskquotacontrol-defaultquotalimit.md)
</dt> <dt>

[**DefaultQuotaThreshold**](diskquotacontrol-defaultquotathreshold.md)
</dt> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




