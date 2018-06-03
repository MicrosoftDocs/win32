---
title: Resize method of the WT\_Disk class
description: Resize iSCSI virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: af96ca45-a9ee-4571-b83b-df64765490cb
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Resize method iSCSI Software Target API
- Resize method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , Resize method
topic_type:
- apiref
api_name:
- WT_Disk.Resize
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resize method of the WT\_Disk class

Resize iSCSI virtual disk. When the *Shrink* parameter is **TRUE**, **Resize** will do reduction with reduction size *DeltaInMB*. When *Shrink* parameter is **FALSE**, **Resize** will do expansion with *DeltaInMB* as additional size. By default, *Shrink* is **FALSE**.

## Syntax


```mof
void Resize(
  [in] uint32  DeltaInMB,
  [in] boolean Shrink
);
```



## Parameters

<dl> <dt>

*DeltaInMB* \[in\]
</dt> <dd>

iSCSI Disk Resize increment (MB)

</dd> <dt>

*Shrink* \[in\]
</dt> <dd>

Whether to reduce or expand virtual disk.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                            |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>Wmiwtprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Disk**](wt-disk.md)
</dt> </dl>

 

 





