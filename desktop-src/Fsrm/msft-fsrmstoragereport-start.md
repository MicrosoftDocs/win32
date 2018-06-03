---
title: Start method of the MSFT\_FSRMStorageReport class
description: Starts the generation of the provided storage report on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43527922-8bfd-4937-a250-b3a08dea0fa8
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Start method File Server Resource Manager
- Start method File Server Resource Manager , MSFT_FSRMStorageReport class
- MSFT_FSRMStorageReport class File Server Resource Manager , Start method
topic_type:
- apiref
api_name:
- MSFT_FSRMStorageReport.Start
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Start method of the MSFT\_FSRMStorageReport class

Starts the generation of the provided storage report on the server.

## Syntax


```mof
uint64 Start(
  [in]  boolean                Queue,
  [in]  sint32                 RunDuration,
  [out] MSFT_FSRMStorageReport StorageReport
);
```



## Parameters

<dl> <dt>

*Queue* \[in\]
</dt> <dd>

If set to **True**, the report will be queued for up to 5 minutes before evaluation. If set to **False**, the report will be generated immediately. The default value is **False**.

</dd> <dt>

*RunDuration* \[in\]
</dt> <dd>

The number of hours to run the report before canceling it. The value 0 indicates that the job will run to completion, and is the default value.

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

 

 





