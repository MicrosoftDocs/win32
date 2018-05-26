---
title: AddWTDisk method of the WT\_Host class
description: Assigns the specified virtual disk to the iSCSI target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 07b40cde-e550-4ca0-8f55-a96f4df89b1c
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddWTDisk method iSCSI Software Target API
- AddWTDisk method iSCSI Software Target API , WT_Host class
- WT_Host class iSCSI Software Target API , AddWTDisk method
topic_type:
- apiref
api_name:
- WT_Host.AddWTDisk
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddWTDisk method of the WT\_Host class

Assigns the specified virtual disk to the iSCSI target.

## Syntax


```mof
void AddWTDisk(
  [in] uint32 WTD
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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Host**](wt-host.md)
</dt> </dl>

 

 





