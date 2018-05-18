---
title: RemoveWTDisk method of the WT\_Host class
description: Removes the specified virtual disk from the iSCSI target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c3afa696-9901-42f5-93aa-8d1dfb52d1e4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveWTDisk method iSCSI Software Target API", "RemoveWTDisk method iSCSI Software Target API , WT_Host class", "WT_Host class iSCSI Software Target API , RemoveWTDisk method"]
topic_type:
- apiref
api_name:
- WT_Host.RemoveWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
---

# RemoveWTDisk method of the WT\_Host class

Removes the specified virtual disk from the iSCSI target.

## Syntax


```mof
void RemoveWTDisk(
  [in] uint32 WTD
);
```



## Parameters

<dl> <dt>

*WTD* \[in\]
</dt> <dd>

The iSCSI disk index for the virtual disk.

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

[**WT\_Host**](wt-host.md)
</dt> </dl>

 

 





