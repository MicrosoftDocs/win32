---
title: Wait method of the MSFT\_FSRMStorageReport class
description: Waits for the report to complete its execution.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33f7d43c-1233-40ca-9d06-556443e7bcb1
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Wait method File Server Resource Manager
- Wait method File Server Resource Manager , MSFT_FSRMStorageReport class
- MSFT_FSRMStorageReport class File Server Resource Manager , Wait method
topic_type:
- apiref
api_name:
- MSFT_FSRMStorageReport.Wait
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Wait method of the MSFT\_FSRMStorageReport class

Waits for the report to complete its execution. If 10 minutes pass without the report completing, the method returns. The [**Stop**](msft-fsrmstoragereport-stop.md) method then ensures the report is no longer running.

## Syntax


```mof
uint64 Wait(
  [in]  sint32                 Timeout,
  [out] MSFT_FSRMStorageReport StorageReport
);
```



## Parameters

<dl> <dt>

*Timeout* \[in\]
</dt> <dd>

The amount of time to wait on the report to complete before returning from the method, in seconds. If the value is &lt;=0, the method will wait until the report process completes. If the process is not running or the value is 0, the method returns immediately. The default value is -1.

</dd> <dt>

*StorageReport* \[out\]
</dt> <dd>

Returns an instance of the [**MSFT\_FSRMStorageReport**](msft-fsrmstoragereport.md) class representing the storage report.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMStorageReport**](msft-fsrmstoragereport.md)
</dt> </dl>

 

 





