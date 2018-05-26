---
title: Stop method of the MSFT\_FSRMClassification class
description: Stops the running instance of a classification job if it is running.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1edd54e7-ccd3-4c9d-ad49-5010b9ebf9b7
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Stop method File Server Resource Manager
- Stop method File Server Resource Manager , MSFT_FSRMClassification class
- MSFT_FSRMClassification class File Server Resource Manager , Stop method
topic_type:
- apiref
api_name:
- MSFT_FSRMClassification.Stop
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Stop method of the MSFT\_FSRMClassification class

Stops the running instance of a classification job if it is running.

## Syntax


```mof
uint64 Stop(
  [out] MSFT_FSRMClassification Classification
);
```



## Parameters

<dl> <dt>

*Classification* \[out\]
</dt> <dd>

An instance of the [**MSFT\_FSRMClassification**](msft-fsrmclassification.md) class that represents FSRM classification.

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

[**MSFT\_FSRMClassification**](msft-fsrmclassification.md)
</dt> </dl>

 

 





