---
title: InstallByDAPrerequisiteChecks method of the PS\_RemoteAccess class
description: This cmdlet does the following 1.
audience: developer
ms.assetid: '43508e20-09f5-448f-8360-094be61f9881'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["InstallByDAPrerequisiteChecks method", "InstallByDAPrerequisiteChecks method, PS_RemoteAccess class", "PS_RemoteAccess class, InstallByDAPrerequisiteChecks method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccess.InstallByDAPrerequisiteChecks
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# InstallByDAPrerequisiteChecks method of the PS\_RemoteAccess class

This cmdlet does the following 1. Performs pre-requisite checks for DirectAccess to ensure that it can be installed2. Installs DirectAccess for remote access (includes management of remote clients) or for management of remote clients only3. Installs VPN (both Remote Access VPN and site-to-site VPN).

## Syntax


```mof
uint32 InstallByDAPrerequisiteChecks(
  [in]  string  ComputerName,
  [in]  boolean Prerequisite,
  [out] boolean Status
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*Prerequisite* \[in\]
</dt> <dd>

Indicates that pre-requisite checks should be performed. This parameter is part of a separate parameter set used to only run the pre-requisite checks for DA

</dd> <dt>

*Status* \[out\]
</dt> <dd>

Returns True when all the pre-requisites have passed, and False when one or more have failed.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccess**](ps-remoteaccess.md)
</dt> </dl>

 

 





