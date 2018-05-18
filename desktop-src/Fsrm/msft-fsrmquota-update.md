---
title: Update method of the MSFT\_FSRMQuota class
description: Starts a quota scan on the specified path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '72c2d34b-7597-459d-83de-8162ef1e5101'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["Update method File Server Resource Manager", "Update method File Server Resource Manager , MSFT_FSRMQuota class", "MSFT_FSRMQuota class File Server Resource Manager , Update method"]
topic_type:
- apiref
api_name:
- MSFT_FSRMQuota.Update
api_location:
- SrmSvc.dll
api_type:
- COM
---

# Update method of the MSFT\_FSRMQuota class

Starts a quota scan on the specified path.

## Syntax


```mof
uint64 Update();
```



## Parameters

This method has no parameters.

## Remarks

Although quota usage is monitored on an ongoing basis, there may be some instances in which the quota usage may be out of sync with the actual usage, in which case you can call this method to refresh the quota usage. For example, if an administrator disables a quota (to investigate or troubleshoot an issue) and later enables it, then this method should be called to perform a manual scan.

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

[**MSFT\_FSRMQuota**](msft-fsrmquota.md)
</dt> </dl>

 

 





