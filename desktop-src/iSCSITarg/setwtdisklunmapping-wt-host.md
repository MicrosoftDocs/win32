---
title: SetWTDiskLunMapping method of the WT\_Host class
description: Sets the SCSI Logical Unit Number (LUN) number of the specified virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3bd245b3-da59-48e6-a97a-70ffeb3ad490'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetWTDiskLunMapping method iSCSI Software Target API", "SetWTDiskLunMapping method iSCSI Software Target API , WT_Host class", "WT_Host class iSCSI Software Target API , SetWTDiskLunMapping method"]
topic_type:
- apiref
api_name:
- WT_Host.SetWTDiskLunMapping
api_location:
- WtWmiProv.dll
api_type:
- COM
---

# SetWTDiskLunMapping method of the WT\_Host class

Sets the SCSI Logical Unit Number (LUN) number of the specified virtual disk.

## Syntax


```mof
void SetWTDiskLunMapping(
  [in] uint32 WTD,
  [in] uint32 LUN
);
```



## Parameters

<dl> <dt>

*WTD* \[in\]
</dt> <dd>

The iSCSI disk index for the virtual disk.

</dd> <dt>

*LUN* \[in\]
</dt> <dd>

The SCSI LUN number.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Each virtual disk within an iSCSI target has a unique Logical Unit Number (LUN). The uniqueness is only per iSCSI target. A virtual disk may have different LUNs if it is assigned to multiple iSCSI targets.

When a virtual disk is assigned to an iSCSI target, the LUN is determined automatically. Use this method only if you need to specify a LUN.

In order for an initiator to access a virtual disk over an iSCSI Storage Area Network (SAN), the virtual disk should be assigned to a [**WT\_Host**](wt-host.md) object that is configured to allow the initiator access to the LUNs that the virtual disk contains.

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

 

 





