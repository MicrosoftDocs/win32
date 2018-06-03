---
title: GetAsyncOperationProgress method of the WT\_Disk class
description: Get the asynchronous operation progress information for this iSCSI virtual disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ee7ab35-429d-42e9-be58-90873424f167
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetAsyncOperationProgress method iSCSI Software Target API
- GetAsyncOperationProgress method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , GetAsyncOperationProgress method
topic_type:
- apiref
api_name:
- WT_Disk.GetAsyncOperationProgress
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetAsyncOperationProgress method of the WT\_Disk class

Get the asynchronous operation progress information for this iSCSI virtual disk.

## Syntax


```mof
void GetAsyncOperationProgress(
  [out] uint32 ProgressPercent,
  [out] sint32 LastError
);
```



## Parameters

<dl> <dt>

*ProgressPercent* \[out\]
</dt> <dd>

Progress percentage (0-100)

</dd> <dt>

*LastError* \[out\]
</dt> <dd>

Last error code of the asynchronous operation

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

 

 





