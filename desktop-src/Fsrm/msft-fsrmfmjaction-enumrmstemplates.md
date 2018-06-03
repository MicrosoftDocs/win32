---
title: EnumRmsTemplates method of the MSFT\_FSRMFMJAction class
description: Enumerates the available Rights Management Services (RMS) templates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a9a42387-c820-42d5-949b-6b8006333362
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- EnumRmsTemplates method File Server Resource Manager
- EnumRmsTemplates method File Server Resource Manager , MSFT_FSRMFMJAction class
- MSFT_FSRMFMJAction class File Server Resource Manager , EnumRmsTemplates method
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJAction.EnumRmsTemplates
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnumRmsTemplates method of the MSFT\_FSRMFMJAction class

Enumerates the available Rights Management Services (RMS) templates.

## Syntax


```mof
uint64 EnumRmsTemplates(
  [out] string TemplateName[]
);
```



## Parameters

<dl> <dt>

*TemplateName* \[out\]
</dt> <dd>

On successful return contains an array of the names of the available RMS templates.

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

[**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md)
</dt> </dl>

 

 





