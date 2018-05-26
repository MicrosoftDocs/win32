---
title: Wait method of the MSFT\_FSRMFileManagementJob class
description: Waits for the specified period of time or until the file management job has finished running.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b6e5fca-773a-4705-9f34-6971f884d1d8
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Wait method File Server Resource Manager
- Wait method File Server Resource Manager , MSFT_FSRMFileManagementJob class
- MSFT_FSRMFileManagementJob class File Server Resource Manager , Wait method
topic_type:
- apiref
api_name:
- MSFT_FSRMFileManagementJob.Wait
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Wait method of the MSFT\_FSRMFileManagementJob class

Waits for the specified period of time or until the file management job has finished running.

## Syntax


```mof
uint64 Wait(
  [in]  sint32                     Timeout,
  [out] MSFT_FSRMFileManagementJob FileManagementJob
);
```



## Parameters

<dl> <dt>

*Timeout* \[in\]
</dt> <dd>

The number of seconds to wait for the file management job to complete. The method returns when the period expires or the file management job completes. To wait indefinitely, set the value to  1. The value must be in the range from  1 through 2,147,483.

</dd> <dt>

*FileManagementJob* \[out\]
</dt> <dd>

An instance of the [**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md) class that represents the file management job.

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

[**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md)
</dt> </dl>

 

 





