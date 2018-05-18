---
title: Extend method of the WT\_Disk class
description: Extends a virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '707973da-ed79-4017-8fdd-dea73989c0db'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Extend method iSCSI Software Target API", "Extend method iSCSI Software Target API , WT_Disk class", "WT_Disk class iSCSI Software Target API , Extend method"]
topic_type:
- apiref
api_name:
- WT_Disk.Extend
api_location:
- WtWmiProv.dll
api_type:
- COM
---

# Extend method of the WT\_Disk class

Extends a virtual disk.

**Windows Server 2012 R2:** This method is deprecated. Use [**Resize**](resize-wt-disk.md) instead.

## Syntax


```mof
void Extend(
  [in] uint32 AdditionalSizeInMB
);
```



## Parameters

<dl> <dt>

*AdditionalSizeInMB* \[in\]
</dt> <dd>

The size, in megabytes, to add to the size of the disk.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Disk**](wt-disk.md)
</dt> <dt>

[**Resize**](resize-wt-disk.md)
</dt> </dl>

 

 





