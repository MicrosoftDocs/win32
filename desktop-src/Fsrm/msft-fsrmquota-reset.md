---
title: Reset method of the MSFT\_FSRMQuota class
description: Applies the property values of the specified quota template to this quota.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 996ed5c0-3275-4dbd-aaba-cfa9582e8433
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Reset method File Server Resource Manager
- Reset method File Server Resource Manager , MSFT_FSRMQuota class
- MSFT_FSRMQuota class File Server Resource Manager , Reset method
topic_type:
- apiref
api_name:
- MSFT_FSRMQuota.Reset
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Reset method of the MSFT\_FSRMQuota class

Applies the property values of the specified quota template to this quota.

## Syntax


```mof
uint64 Reset(
  [in]  string         Template,
  [out] MSFT_FSRMQuota Quota
);
```



## Parameters

<dl> <dt>

*Template* \[in\]
</dt> <dd>

Name of the quota template that should be applied to this quota.

</dd> <dt>

*Quota* \[out\]
</dt> <dd>

Returns an instance of the [**MSFT\_FSRMQuota**](msft-fsrmquota.md) object after the template is applied.

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

[**MSFT\_FSRMQuota**](msft-fsrmquota.md)
</dt> </dl>

 

 





