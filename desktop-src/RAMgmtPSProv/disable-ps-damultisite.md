---
title: Disable method of the PS\_DAMultiSite class
description: Disables a multisite deployment that contains a single entry point. After disabling, servers in the entry point will be configured with the remote access settings that were configured before the servers were joined to the multisite deployment.
audience: developer
ms.assetid: 4fd21f3b-060b-464f-bbb8-fecc554d5d3c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Disable method
- Disable method, PS_DAMultiSite class
- PS_DAMultiSite class, Disable method
topic_type:
- apiref
api_name:
- PS_DAMultiSite.Disable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Disable method of the PS\_DAMultiSite class

Disables a multisite deployment that contains a single entry point. After disabling, servers in the entry point will be configured with the remote access settings that were configured before the servers were joined to the multisite deployment.

## Syntax


```mof
uint32 Disable(
  [in]  string      ComputerName,
  [in]  boolean     Force,
  [in]  boolean     PassThru,
  [out] DAMultiSite cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name or IP address of a remote access server that multisite configuration settings will be removed from. If no value is specified the name of the local server on which the cmdlet runs is used.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Suppresses the option to allow a user to override a setting. (ShouldContinue prompts).

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the Multisite object which contained the multisite configuration removed. This cmdlet doesn't generate an object by default.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

None unless PassThru is passed. If passthru is passed then the [**PS\_DAMultiSite**](ps-damultisite.md) object is returned with the last configuration before removed

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAMultiSite**](ps-damultisite.md)
</dt> </dl>

 

 





