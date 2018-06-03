---
title: Export method of the WT\_Snapshot class
description: Exports the current shadow copy as a virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cbf16cf1-6ff8-49a0-8ef3-eb48c3e08a87
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Export method iSCSI Software Target API
- Export method iSCSI Software Target API , WT_Snapshot class
- WT_Snapshot class iSCSI Software Target API , Export method
topic_type:
- apiref
api_name:
- WT_Snapshot.Export
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Export method of the WT\_Snapshot class

Exports the current shadow copy as a virtual disk.

## Syntax


```mof
void Export(
  [out] uint32 WTD
);
```



## Parameters

<dl> <dt>

*WTD* \[out\]
</dt> <dd>

The exported shadow copy's iSCSI disk index.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Snapshot**](wt-snapshot.md)
</dt> </dl>

 

 





