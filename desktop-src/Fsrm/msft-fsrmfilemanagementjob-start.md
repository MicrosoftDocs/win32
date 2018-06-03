---
title: Start method of the MSFT\_FSRMFileManagementJob class
description: Starts the file management job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f582d44f-2790-42a7-b329-51d0e6dd8da2
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Start method File Server Resource Manager
- Start method File Server Resource Manager , MSFT_FSRMFileManagementJob class
- MSFT_FSRMFileManagementJob class File Server Resource Manager , Start method
topic_type:
- apiref
api_name:
- MSFT_FSRMFileManagementJob.Start
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Start method of the MSFT\_FSRMFileManagementJob class

Starts the file management job.

## Syntax


```mof
uint64 Start(
  [in]  boolean                    Queue,
  [in]  sint32                     RunDuration,
  [out] MSFT_FSRMFileManagementJob FileManagementJob
);
```



## Parameters

<dl> <dt>

*Queue* \[in\]
</dt> <dd>

Indicates whether the file management job should be added to a queue and is expected to run in the next 5 minutes. Any jobs queued during that 5 minute window will be run together. If **False** the file management job will be executed immediately.

</dd> <dt>

*RunDuration* \[in\]
</dt> <dd>

Indicates how many hours to run the file management job before it will be automatically canceled. If 0 then the file management job will run to completion.

</dd> <dt>

*FileManagementJob* \[out\]
</dt> <dd>

Returns a [**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md) instance representing the file management job.

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

 

 





