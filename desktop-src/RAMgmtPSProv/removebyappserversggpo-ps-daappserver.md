---
title: RemoveByAppServerSGGpo method of the PS\_DAAppServer class
description: This cmdlet performs the following operations1.
audience: developer
ms.assetid: 'a21db4cf-5c38-45d3-a892-f5d853544feb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByAppServerSGGpo method", "RemoveByAppServerSGGpo method, PS_DAAppServer class", "PS_DAAppServer class, RemoveByAppServerSGGpo method"]
topic_type:
- apiref
api_name:
- PS_DAAppServer.RemoveByAppServerSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# RemoveByAppServerSGGpo method of the PS\_DAAppServer class

This cmdlet performs the following operations1. Removes the specified lit of application server Security groups from the DA deployment2. Removes the specified application servers from the specified DA application server security group3. Removes the application server GPOs in the specified domains. This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.

## Syntax


```mof
uint32 RemoveByAppServerSGGpo(
  [in]  string      SecurityGroupNameList[],
  [in]  string      ComputerName,
  [in]  boolean     PassThru,
  [in]  string      DomainName[],
  [out] DAAppServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*SecurityGroupNameList* \[in\]
</dt> <dd>

List of application server security groups that are to be deleted from the DA deployment. Each security group is specified in DOMAIN\\SG\_NAME format

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DA Application Server object. By default this cmdlet does not generate any output

</dd> <dt>

*DomainName* \[in\]
</dt> <dd>

List of domains from which application server GPOs need to be removed. Domain is specified in the format DOMAIN.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The entire app server policy object is outputted. Consists of the following: a. List of app server SGs present in the DA deployment. b. List of all app server GPOs in the DA deployment. c. App server connection properties, viz. 1. Connectivity type. 2. IPsec traffic protection

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

[**PS\_DAAppServer**](ps-daappserver.md)
</dt> </dl>

 

 





