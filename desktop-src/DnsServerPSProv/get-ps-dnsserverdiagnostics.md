---
title: Get method of the PS\_DnsServerDiagnostics class
description: Retrieve DNS Event logging details.
audience: developer
ms.assetid: 0898931e-5531-4eaa-b4ce-2049c9062593
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerDiagnostics class
- PS_DnsServerDiagnostics class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerDiagnostics.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerDiagnostics class

Retrieve DNS Event logging details.

## Syntax


```mof
uint32 Get(
  [in]  string               ComputerName,
  [out] DnsServerDiagnostics cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerDiagnostics**](dnsserverdiagnostics.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDiagnostics**](ps-dnsserverdiagnostics.md)
</dt> </dl>

 

 





