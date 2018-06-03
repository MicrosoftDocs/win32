---
title: Remove method of the PS\_DAEntryPoint class
description: Removes an entry point from a multisite deployment.
audience: developer
ms.assetid: 0a0bcc0a-e671-43aa-b26c-6a2352a5c7df
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DAEntryPoint class
- PS_DAEntryPoint class, Remove method
topic_type:
- apiref
api_name:
- PS_DAEntryPoint.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_DAEntryPoint class

Removes an entry point from a multisite deployment.

## Syntax


```mof
uint32 Remove(
  [in]  string       ComputerName,
  [in]  string       Name,
  [in]  boolean      PassThru,
  [in]  boolean      Force,
  [out] DAEntryPoint cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name or address (IPv4 or IPV6) of a server included in the multisite deployment from which an entry point should be removed. If no value is specified, the name of the local server on which the cmdlet runs is used.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the entry point to be removed. If no value is specified the name of the entry point associated with the computer specified in the ComputerName parameter is used.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the object which was removed.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Suppresses the user confirmation that prompts during running the cmdlet.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

If the PassThru flag is specified, the output will provide the entry point name, the IP address used for global load balancing to the entry point, and a list of servers in the entry point. If the flag is not specified nothing is returned.

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

[**PS\_DAEntryPoint**](ps-daentrypoint.md)
</dt> </dl>

 

 





