---
title: CreateThreshold method of the MSFT\_FSRMQuotaThreshold class
description: Creates a MSFT\_FSRMQuotaThreshold instance representing a new quota threshold object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2a1a88d9-54e9-4826-9c46-f5bfd6f312ec
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- CreateThreshold method File Server Resource Manager
- CreateThreshold method File Server Resource Manager , MSFT_FSRMQuotaThreshold class
- MSFT_FSRMQuotaThreshold class File Server Resource Manager , CreateThreshold method
topic_type:
- apiref
api_name:
- MSFT_FSRMQuotaThreshold.CreateThreshold
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateThreshold method of the MSFT\_FSRMQuotaThreshold class

Creates a [**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md) instance representing a new quota threshold object.

## Syntax


```mof
uint64 CreateThreshold(
  [in]  uint32                  Percentage,
  [in]  MSFT_FSRMAction         Action[],
  [out] MSFT_FSRMQuotaThreshold QuotaThreshold
);
```



## Parameters

<dl> <dt>

*Percentage* \[in\]
</dt> <dd>

A positive number up to 100.

</dd> <dt>

*Action* \[in\]
</dt> <dd>

An array of instances of the [**MSFT\_FSRMAction**](msft-fsrmaction.md) class representing action types. Only one notification per type is allowed.

</dd> <dt>

*QuotaThreshold* \[out\]
</dt> <dd>

Returns a [**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md) instance representing a new quota threshold object.

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

[**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md)
</dt> <dt>

[**MSFT\_FSRMAction**](msft-fsrmaction.md)
</dt> </dl>

 

 





