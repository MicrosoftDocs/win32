---
title: RemoveByClientDownlevelSGGpo method of the PS\_DAClient class
description: This cmdlet performs the following operations1.
audience: developer
ms.assetid: '56023003-034d-4d8a-a2c4-42dd292f5774'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByClientDownlevelSGGpo method", "RemoveByClientDownlevelSGGpo method, PS_DAClient class", "PS_DAClient class, RemoveByClientDownlevelSGGpo method"]
topic_type:
- apiref
api_name:
- PS_DAClient.RemoveByClientDownlevelSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# RemoveByClientDownlevelSGGpo method of the PS\_DAClient class

This cmdlet performs the following operations1. Removes one or more client machine security group(s) from the DA deployment 2. Removes one or more DA client GPO(s) from domain(s) 3. In a multi-site deployment, removes one or more security group(s) of down-level clients from the DA deployment. These down-level clients can connect only to the specified site 4. In a multi-site deployment, removes one or more down-level DA client GPO(s) from domain(s).

## Syntax


```mof
uint32 RemoveByClientDownlevelSGGpo(
  [in]  string   DownlevelSecurityGroupNameList[],
  [in]  string   ComputerName,
  [in]  boolean  PassThru,
  [in]  string   DownlevelDomainName[],
  [in]  string   EntrypointName,
  [out] DAClient cmdletOutput
);
```



## Parameters

<dl> <dt>

*DownlevelSecurityGroupNameList* \[in\]
</dt> <dd>

Names of one or more downlevel client security groups that are part of the DA deployment which need to be removed. Specified in DOMAIN\\SG\_NAME format . These down-level clients can connect only to the site specified in the EntryPointName param (see description of EntryPointName parameter for more details)

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the DA client object. By default this cmdlet does not generate any output

</dd> <dt>

*DownlevelDomainName* \[in\]
</dt> <dd>

List of domains in which client GPOs need to be removed. Domain is specified in the format DOMAIN

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment from which down-level clients are removed (these clients can only connect to the specified site). If entrypoint parameter is not specified then the site to which the computer on which the cmdlet is executed belongs is used (user may or may not be specifying a ComputerName). If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the authentication type is configured for it

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of client SGs present in the DA deployment. 2. List of client GPOs present in the DA deployment. 3. Status of force tunnel 4. NRPT object (for force tunnel properties) 5. Support for down-level (enable/disable) 6. Laptop-only deployment (enable/disable)

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

[**PS\_DAClient**](ps-daclient.md)
</dt> </dl>

 

 





