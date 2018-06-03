---
title: Set method of the PS\_DAEntryPoint class
description: Configures settings for the entry point.
audience: developer
ms.assetid: d0cd8c51-c4a7-4623-a0ac-a419e89b50ea
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DAEntryPoint class
- PS_DAEntryPoint class, Set method
topic_type:
- apiref
api_name:
- PS_DAEntryPoint.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DAEntryPoint class

Configures settings for the entry point.

## Syntax


```mof
uint32 Set(
  [in]  string       ComputerName,
  [in]  string       Name,
  [in]  string       GslbIP,
  [in]  boolean      PassThru,
  [in]  string       NewName,
  [out] DAEntryPoint cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name or IP address of the remote access server in the entry point. If no value is specified the name of the local remote access server on which the cmdlet runs is used.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the entry point. If no value is specified entry point information is configured for the remote access server specified in the ComputerName parameter.

</dd> <dt>

*GslbIP* \[in\]
</dt> <dd>

IPv4 or IPv6 address used for global load balancing for the entry point.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the DAEntrypoint object which contains the DAEntrypoint configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*NewName* \[in\]
</dt> <dd>

Specifies the name of the entry point.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Entry point name 2. IPv4 or IPv6 address used for global load balancing 3. List of servers in the entry point

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

 

 





