---
description: Sets or gets the user's current quota limit.
title: DIDiskQuotaUser.QuotaLimit property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DIDiskQuotaUser.QuotaLimit
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 7eee1be7-8ad5-4796-910c-987fe3fd6338
api_name: 
 - DIDiskQuotaUser.QuotaLimit
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DIDiskQuotaUser.QuotaLimit property

Sets or gets the user's current [**quota limit**](diskquotacontrol-object.md).

This property is read/write.

## Syntax


```JScript
iQuotaLimit = DIDiskQuotaUser.QuotaLimit
DIDiskQuotaUser.QuotaLimit = iQuotaLimit
```



## Property value

An **Integer** value that specifies or receives the user's current quota limit, in bytes.

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

[**DIDiskQuotaUser**](didiskquotauser-object.md)
</dt> <dt>

[**QuotaLimitText**](didiskquotauser-quotalimittext.md)
</dt> </dl>

 

 




