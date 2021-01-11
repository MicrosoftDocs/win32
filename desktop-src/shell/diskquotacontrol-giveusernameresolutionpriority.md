---
description: Places the specified user object next in line for name resolution.
ms.assetid: 4c75f966-2e7d-4415-b1db-c98f8bdd4ce3
title: DiskQuotaControl.GiveUserNameResolutionPriority method (Dskquota.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.GiveUserNameResolutionPriority
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.GiveUserNameResolutionPriority method

Places the specified user object next in line for name resolution.

## Syntax


```JScript
DiskQuotaControl.GiveUserNameResolutionPriority(
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

If asynchronous name resolution is enabled, user objects are placed in a queue. By default, they are serviced in the order they are placed in the queue. The **GiveUserNameResolutionPriority** method moves an object to the front of the queue so that it is next in line to be serviced.

Use the [**UserNameResolution**](diskquotacontrol-usernameresolution.md) property to enable asynchronous name resolution.

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

 

 




