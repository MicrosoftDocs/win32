---
description: Clears the object's cached user information.
title: DIDiskQuotaUser.Invalidate method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIDiskQuotaUser.Invalidate
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: e0ffd5b7-db1d-40a4-810a-ff43549b0c9b
api_name: 
 - DIDiskQuotaUser.Invalidate
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DIDiskQuotaUser.Invalidate method

Clears the object's cached user information.

## Syntax


```JScript
DIDiskQuotaUser.Invalidate()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method clears the user information stored in the object's cache. The next time a request is made for quota-related information, the object retrieves the information from the NTFS volume and refreshes the cache.

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

 

 




