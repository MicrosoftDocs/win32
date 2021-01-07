---
description: Gets a Boolean value that indicates whether the quota file for the volume is currently being rebuilt.
ms.assetid: 66a6bafe-bda4-41b3-9207-2ea6b8e63835
title: DiskQuotaControl.QuotaFileRebuilding property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.QuotaFileRebuilding
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.QuotaFileRebuilding property

Gets a Boolean value that indicates whether the quota file for the volume is currently being rebuilt.

This property is read-only.

## Syntax


```JScript
bQuotaFileRebuilding = DiskQuotaControl.QuotaFileRebuilding
```



## Property value

This property is set to **TRUE** if the quota file is being rebuilt, or **FALSE** otherwise.

## Remarks

The quota file is automatically rebuilt when quotas are enabled on the system or when one or more user entries are marked for deletion.

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

 

 




