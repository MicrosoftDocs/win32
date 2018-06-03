---
title: Stop method of the MSFT\_FSRMFileManagementJob class
description: Stops the running instance of a file management job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72f5cfac-b7b0-4276-aaa8-3640b0ac6b0a
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Stop method File Server Resource Manager
- Stop method File Server Resource Manager , MSFT_FSRMFileManagementJob class
- MSFT_FSRMFileManagementJob class File Server Resource Manager , Stop method
topic_type:
- apiref
api_name:
- MSFT_FSRMFileManagementJob.Stop
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stop method of the MSFT\_FSRMFileManagementJob class

Stops the running instance of a file management job.

## Syntax


```mof
uint64 Stop(
  [out] MSFT_FSRMFileManagementJob FileManagementJob
);
```



## Parameters

<dl> <dt>

*FileManagementJob* \[out\]
</dt> <dd>

An instance of the [**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md) class that represents FSRM classification.

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

 

 





