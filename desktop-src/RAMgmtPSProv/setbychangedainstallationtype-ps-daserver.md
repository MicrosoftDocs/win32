---
title: SetByChangeDAInstallationType method of the PS\_DAServer class
description: This cmdlet sets the properties specific to the DA server.
audience: developer
ms.assetid: b9de7626-ac5a-4b2d-8a9f-49163e75b2ab
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByChangeDAInstallationType method
- SetByChangeDAInstallationType method, PS_DAServer class
- PS_DAServer class, SetByChangeDAInstallationType method
topic_type:
- apiref
api_name:
- PS_DAServer.SetByChangeDAInstallationType
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByChangeDAInstallationType method of the PS\_DAServer class

This cmdlet sets the properties specific to the DA server.

## Syntax


```mof
uint32 SetByChangeDAInstallationType(
  [in]  string   ComputerName,
  [in]  string   DAInstallType,
  [in]  boolean  Force,
  [in]  boolean  PassThru,
  [out] DAServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the DirectAccess server machine specific tasks should be executed

</dd> <dt>

*DAInstallType* \[in\]
</dt> <dd>

This parameter is used to change the configuration in which DA has been deployed. It can take one of the following values. 1. FullInstall. 2. ManageOut. The DAInstallType is a global configuration and applies to the entire DA deployment.

<dt>

<span id="FullInstall"></span><span id="fullinstall"></span><span id="FULLINSTALL"></span>

**FullInstall** ("FullInstall")


</dt> <dd></dd> <dt>

<span id="ManageOut"></span><span id="manageout"></span><span id="MANAGEOUT"></span>

**ManageOut** ("ManageOut")


</dt> <dd></dd> </dl> </dd> <dt>

*Force* \[in\]
</dt> <dd>

Switch parameter used to suppress user confirmation prompts for the following conditions. When suppressed the cmdlet assumes user confirmation for the below mentioned changes. 1. ConnectTo change would result in a change in the SSL certificate. 2. During SSL cert change if an appropriate cert is not found then a self-signed cert is created 3. Changing DirectAccess installation type

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object that conveys the properties of the DA server. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

DA server properties. 1. Authentication type 2. Internal IPv6 prefix 3. Client IPHTTPS IPv6 prefix 4. Usage of machine cert auth for 1st tunnel 5. IPsec cert 6. IPsec intermediate cert usage 7. Status of health check. Common properties 1. SSL cert 2. ConnectTo address 3. Internal interface 4. Internet interface

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

 

 





