---
title: Wait method of the MSFT\_FSRMClassification class
description: Waits for the specified period of time or until classification has finished running.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 466c8c92-05ae-4a04-9da1-129332530ab9
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Wait method File Server Resource Manager
- Wait method File Server Resource Manager , MSFT_FSRMClassification class
- MSFT_FSRMClassification class File Server Resource Manager , Wait method
topic_type:
- apiref
api_name:
- MSFT_FSRMClassification.Wait
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Wait method of the MSFT\_FSRMClassification class

Waits for the specified period of time or until classification has finished running.

## Syntax


```mof
uint64 Wait(
  [in]  sint32                  Timeout,
  [out] MSFT_FSRMClassification Classification
);
```



## Parameters

<dl> <dt>

*Timeout* \[in\]
</dt> <dd>

The number of seconds to wait for classification and the reports to complete. The method returns when the period expires or classification and the reports complete. To wait indefinitely, set the value to  1. The value must be in the range from  1 through 2,147,483.

</dd> <dt>

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

 

 





