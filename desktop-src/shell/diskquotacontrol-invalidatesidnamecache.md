---
description: Invalidates the security ID user name cache.
ms.assetid: 52f4a051-0caf-43c1-b190-c83c20e9fcf8
title: DiskQuotaControl.InvalidateSidNameCache method (Dskquota.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.InvalidateSidNameCache
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.InvalidateSidNameCache method

Invalidates the security ID user name cache.

## Syntax


```JScript
DiskQuotaControl.InvalidateSidNameCache()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

User names and associated security IDs are stored in a cache. You can clear this cache by calling **InvalidateSidNameCache**. If you subsequently create a new user object, the information will have to be obtained from the domain controller, and the cache will have to be reestablished.

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

 

 




