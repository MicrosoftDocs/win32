---
title: Create method of the WT\_Snapshot class
description: Creates a shadow copy of the specified virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '221efe53-b77c-4d80-8dbe-1579374f76c0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Create method iSCSI Software Target API", "Create method iSCSI Software Target API , WT_Snapshot class", "WT_Snapshot class iSCSI Software Target API , Create method"]
topic_type:
- apiref
api_name:
- WT_Snapshot.Create
api_location:
- WtWmiProv.dll
api_type:
- COM
---

# Create method of the WT\_Snapshot class

Creates a shadow copy of the specified virtual disk.

## Syntax


```mof
void Create(
  [in]  uint32 WTD,
  [out] string Id
);
```



## Parameters

<dl> <dt>

*WTD* \[in\]
</dt> <dd>

The iSCSI Disk Index for the virtual disk.

</dd> <dt>

*Id* \[out\]
</dt> <dd>

The shadow copy identifier for the shadow copy.

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

[**WT\_Snapshot**](wt-snapshot.md)
</dt> </dl>

 

 





