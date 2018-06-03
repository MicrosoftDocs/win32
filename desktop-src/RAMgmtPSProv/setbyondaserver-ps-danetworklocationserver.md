---
title: SetByOnDAServer method of the PS\_DANetworkLocationServer class
description: This cmdlet is used to configure the Network Location Server. It can be present on the DirectAccess server or on some other highly available server.
audience: developer
ms.assetid: 8502a26a-dba7-4259-acad-d7b3a94cb5a7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByOnDAServer method
- SetByOnDAServer method, PS_DANetworkLocationServer class
- PS_DANetworkLocationServer class, SetByOnDAServer method
topic_type:
- apiref
api_name:
- PS_DANetworkLocationServer.SetByOnDAServer
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByOnDAServer method of the PS\_DANetworkLocationServer class

This cmdlet is used to configure the Network Location Server. It can be present on the DirectAccess server or on some other highly available server.

## Syntax


```mof
uint32 SetByOnDAServer(
  [in]  uint8                   Certificate[],
  [in]  string                  ComputerName,
  [in]  boolean                 NlsOnDAServer,
  [in]  boolean                 Force,
  [in]  boolean                 PassThru,
  [out] DANetworkLocationServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*Certificate* \[in\]
</dt> <dd>

Specifies the certificate to be used when the Network Location Server is configured to be on the DirectAccess server

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the DirectAccess server machine specific tasks should be executed

</dd> <dt>

*NlsOnDAServer* \[in\]
</dt> <dd>

Switch parameter which indicates that NLS should be configured on the DA Server (the server on which the cmdlet is executed). In order for the DA server to act as a Network Location Server an appropriate certificate is required to be installed on the server. By default the cmdlet looks for a certificate on the server. If a certificate is not found then a self signed certificate is created for this purpose. Before creating the self-signed certificate the cmdlet asks for user confirmation. If the user wishes to specify a certificate himself explicitly the Certificate parameter can be used.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes 1. Creation of self-signed cert when configuring the NLS on the DA server 2. Moving the NLS from the DA server to an external server - the corresponding URL on the DA server is decommissioned. Clients outside corpnet will not receive the updated policies. When they enter corpnet the URL will be inaccessible and they will be detected to be outside corpnet. As a result they will not be able to access corp resources

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the network location server policy object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. Where the Network Location Server is configured - on the DA server itself or on a different server: 2. URL (if it is configured on a different server) 3. Certificate (if it is configured on the DA server) 4. Reachability to Network Location Server (if on a different server whether the URL is reachable or not)

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

[**PS\_DANetworkLocationServer**](ps-danetworklocationserver.md)
</dt> </dl>

 

 





