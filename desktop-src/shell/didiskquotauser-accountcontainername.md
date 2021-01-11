---
description: Gets the name of the user's account container.
title: DIDiskQuotaUser.AccountContainerName property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIDiskQuotaUser.AccountContainerName
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 5b9b0355-ea69-4c34-b0be-fc8e5855ec73
api_name: 
 - DIDiskQuotaUser.AccountContainerName
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DIDiskQuotaUser.AccountContainerName property

Gets the name of the user's account container.

This property is read-only.

## Syntax


```JScript
AccountContainerName = DIDiskQuotaUser.AccountContainerName
```



## Property value

A string value that is set to the user's account container name.

## Remarks

For accounts without directory services information, this property contains the domain name. For accounts with directory services information, this property contains a canonical name with the terminating object name removed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DIDiskQuotaUser Object**](didiskquotauser-object.md)
</dt> </dl>

 

 




