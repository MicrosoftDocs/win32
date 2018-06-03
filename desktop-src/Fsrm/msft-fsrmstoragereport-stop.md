---
title: Stop method of the MSFT\_FSRMStorageReport class
description: Stops the execution of the provided storage report on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e3ce6119-9a71-4b98-b332-60980f363ecd
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Stop method File Server Resource Manager
- Stop method File Server Resource Manager , MSFT_FSRMStorageReport class
- MSFT_FSRMStorageReport class File Server Resource Manager , Stop method
topic_type:
- apiref
api_name:
- MSFT_FSRMStorageReport.Stop
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stop method of the MSFT\_FSRMStorageReport class

Stops the execution of the provided storage report on the server.

If the provided storage report is:

-   Not currently actively running on the server: Returns success.
-   Currently canceling on the server: Returns success.
-   Currently running on the server: Upon successfully starting the cancellation of the report, returns success.
-   Currently queued on the server: Upon successfully removing the report from the queue, returns success.

If a running or queued storage report on the server is unable to be stopped, the following error will be returned: "The report running against &lt;paths&gt; could not be stopped."

## Syntax


```mof
uint64 Stop(
  [out] MSFT_FSRMStorageReport StorageReport
);
```



## Parameters

<dl> <dt>

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

 

 





