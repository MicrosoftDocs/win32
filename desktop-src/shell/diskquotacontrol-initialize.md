---
description: Opens a specified volume and initializes its quota control object.
ms.assetid: 20eae2a3-f602-48a2-bf1c-65570e7a5d21
title: DiskQuotaControl.Initialize method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.Initialize
api_type: 
- COM
api_location: 
- Shell32.dll
---

# DiskQuotaControl.Initialize method

Opens a specified volume and initializes its quota control object.

## Syntax


```JScript
DiskQuotaControl.Initialize(
  sPath,
  bReadWrite
)
```



## Parameters

<dl> <dt>

*sPath* 
</dt> <dd>

Type: **String**

A string value that contains the fully qualified path of the volume to be initialized.

</dd> <dt>

*bReadWrite* 
</dt> <dd>

Type: **Boolean**

A Boolean value that specifies how the volume is to be opened. Set *bReadWrite* to **TRUE** for read/write access or **FALSE** for read-only access.

</dd> </dl>

## Return value

This method does not return a value.

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

 

 




