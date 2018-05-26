---
title: GetRollbackProgress method of the WT\_Disk class
description: Retrieves the rollback progress information for the disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8F3EC053-9C51-4C24-AA84-7E76D1F1CFA1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetRollbackProgress method iSCSI Software Target API
- GetRollbackProgress method iSCSI Software Target API , WT_Disk class
- WT_Disk class iSCSI Software Target API , GetRollbackProgress method
topic_type:
- apiref
api_name:
- WT_Disk.GetRollbackProgress
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetRollbackProgress method of the WT\_Disk class

Retrieves the rollback progress information for the disk.

**Windows Server 2012 R2:** This method is deprecated. Use [**GetAsyncOperationProgress**](getasyncoperationprogress-wt-disk.md) instead.

## Syntax


```mof
void GetRollbackProgress(
  [out] uint32 ProgressPercent,
  [out] sint32 RollbackLastError
);
```



## Parameters

<dl> <dt>

*ProgressPercent* \[out\]
</dt> <dd>

Progress percentage (0-100).

The value of the *ProgressPercent* parameter is only valid when the *RollbackLastError* parameter is **ERROR\_SUCCESS**. At the start of the rollback operation, this parameter is set to zero and the **Status** property of the [**WT\_Disk**](wt-disk.md) object is set to **Reverting**. When the rollback operation is complete, this parameter is set to 100 and **Status** is set to set to **Ide** or **InUse**.

</dd> <dt>

*RollbackLastError* \[out\]
</dt> <dd>

Last error code of the rollback operation.

If there is an error during rollback, the error code is returned in the *RollbackLastError* parameter. This value can be used to determine if the value of the *RollbackProgress* parameter is valid, or to check the status of the rollback operation after the initial call to this method. If the value of *RollbackProgress* is 100 and the value of *RollbackLastError* is **ERROR\_SUCCESS**, the rollback has completed successfully.

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

[**WT\_Disk**](wt-disk.md)
</dt> <dt>

[**GetAsyncOperationProgress**](getasyncoperationprogress-wt-disk.md)
</dt> </dl>

 

 





