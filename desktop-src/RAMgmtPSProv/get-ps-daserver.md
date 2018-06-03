---
title: Get method of the PS\_DAServer class
description: This cmdlet displays the properties of the DA Server.
audience: developer
ms.assetid: b105dfda-b568-4067-a095-126221c37932
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DAServer class
- PS_DAServer class, Get method
topic_type:
- apiref
api_name:
- PS_DAServer.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DAServer class

This cmdlet displays the properties of the DA Server.

## Syntax


```mof
uint32 Get(
  [in]  string   ComputerName,
  [in]  string   EntrypointName,
  [out] DAServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the DirectAccess server machine specific tasks should be executed

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment and when specified indicates that the configuration of the DA server at that site should be retrieved. If an entrypoint is not specified in a multi-site deployment then the entrypoint to which the server on which the cmdlet is executed belongs is used. The server could also be represented by using the ComputerName parameter. If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the configuration is returned for it

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

DA server properties. 1. Authentication type. 2. Internal IPv6 prefix 3. Client IPHTTPS IPv6 prefix. 4. Usage of machine cert auth for 1st tunnel. 5. IPsec cert. 6. IPsec intermediate cert usage. 7. Status of health check. Common properties. 1. SSL cert. 2. ConnectTo address. 3. Internal interface. 4. Internet interface.

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

[**PS\_DAServer**](ps-daserver.md)
</dt> </dl>

 

 





