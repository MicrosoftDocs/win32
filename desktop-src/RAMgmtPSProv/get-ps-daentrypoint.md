---
title: Get method of the PS\_DAEntryPoint class
description: Displays the settings for an entry point.
audience: developer
ms.assetid: 'e2cc2c61-a732-4f28-a1de-aade0099b78c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DAEntryPoint class", "PS_DAEntryPoint class, Get method"]
topic_type:
- apiref
api_name:
- PS_DAEntryPoint.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DAEntryPoint class

Displays the settings for an entry point.

## Syntax


```mof
uint32 Get(
  [in]  string       ComputerName,
  [in]  string       Name,
  [out] DAEntryPoint cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name or IP address of the remote access server for which the entry point information should be retrieved. If no value is specified the name of the local remote access server on which the cmdlet runs is used.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the entry point for which information should be retrieved. If no value is specified entry point information is retrieved for the remote access server specified in the ComputerName parameter.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Entry point name 2. Global load balancing server IP address 3. List of NLB servers in the entry point.

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

[**PS\_DAEntryPoint**](ps-daentrypoint.md)
</dt> </dl>

 

 





