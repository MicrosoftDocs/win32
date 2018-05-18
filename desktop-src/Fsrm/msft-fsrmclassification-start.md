---
title: Start method of the MSFT\_FSRMClassification class
description: Starts a classification job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ea9c61be-ce6d-47dd-a0f1-a90de14268c1'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["Start method File Server Resource Manager", "Start method File Server Resource Manager , MSFT_FSRMClassification class", "MSFT_FSRMClassification class File Server Resource Manager , Start method"]
topic_type:
- apiref
api_name:
- MSFT_FSRMClassification.Start
api_location:
- SrmSvc.dll
api_type:
- COM
---

# Start method of the MSFT\_FSRMClassification class

Starts a classification job.

## Syntax


```mof
uint64 Start(
  [in]  boolean                 Queue,
  [in]  sint32                  RunDuration,
  [out] MSFT_FSRMClassification Classification
);
```



## Parameters

<dl> <dt>

*Queue* \[in\]
</dt> <dd>

Indicates whether the classification job should be added to a queue and is expected to run in the next 5 minutes. Any jobs queued during that 5 minute window will be run together. If **False** the classification job will be executed immediately.

</dd> <dt>

*RunDuration* \[in\]
</dt> <dd>

Indicates how many hours to run the classification job before it will be automatically canceled. If 0 then the classification job will run to completion.

</dd> <dt>

*Classification* \[out\]
</dt> <dd>

Returns a [**MSFT\_FSRMClassification**](msft-fsrmclassification.md) instance representing the classification job.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMClassification**](msft-fsrmclassification.md)
</dt> </dl>

 

 





