---
title: AddByClientDownlevelSGGpo method of the PS\_DAClient class
description: This cmdlet performs the following operations for W8 and down-level (W7) clients 1.
audience: developer
ms.assetid: bf9fc446-8176-43f7-9298-edba76c07c92
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByClientDownlevelSGGpo method
- AddByClientDownlevelSGGpo method, PS_DAClient class
- PS_DAClient class, AddByClientDownlevelSGGpo method
topic_type:
- apiref
api_name:
- PS_DAClient.AddByClientDownlevelSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByClientDownlevelSGGpo method of the PS\_DAClient class

This cmdlet performs the following operations for W8 and down-level (W7) clients 1. Adds one or more client machine security group(s) to the DA deployment2. Adds one or more DA client GPO(s) in domain(s)3. In a multi-site deployment, adds one or more security group(s) of down-level clients to the DA deployment. These down-level clients can then connect only to the specified site4. In a multi-site deployment, adds one or more down-level DA client GPO(s) in a domain(s).

## Syntax


```mof
uint32 AddByClientDownlevelSGGpo(
  [in]  string   DownlevelSecurityGroupNameList[],
  [in]  string   DownlevelGpoName[],
  [in]  string   ComputerName,
  [in]  string   EntrypointName,
  [in]  boolean  PassThru,
  [out] DAClient cmdletOutput
);
```



## Parameters

<dl> <dt>

*DownlevelSecurityGroupNameList* \[in\]
</dt> <dd>

This parameter is only applicable in case of a multi-site deployment and represent the names of one or more downlevel client security groups that are not already part of the DA deployment. Specified in DOMAIN\\SG\_NAME format. These down-level clients can then connect only to the site specified in the EntryPointName param (see description of EntryPointName parameter for more details)

</dd> <dt>

*DownlevelGpoName* \[in\]
</dt> <dd>

This parameter is applicable only in case of multi-site deployment and represents the name to be used when creating the down-level client GPO in the specified domain or represents the domain in which a down-level client GPO with the default name should be created. GPO is specified in the format DOMAIN\\GPO\_NAME. Domain is specified in the format DOMAIN. These GPOs correspond to the down-level security groups added using the DownlevelSecurityGroup parameter If the parameter contains only the domain name then the following default GPO name is used: \[domain\] client policy for \[DA connection friendly name\]-\[entrypoint name\] A list of GPOs can be specified

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

</dd> <dt>

*EntrypointName* \[in\]
</dt> <dd>

Entrypoint refers to the identity of a site in a multi-site deployment to which down-level clients are added, i.e., these clients can only connect to the specified site. If entrypoint parameter is not specified then the site to which the computer on which the cmdlet is executed belongs is used (user may or may not be specifying a ComputerName). If both entrypoint and computername are specified and the ComputerName doesn't belong to the site represented by the entrypoint then the entrypoint takes precedence and the authentication type is configured for it

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns the client settings object. By default this cmdlet does not generate any output

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. List of client SGs present in the DA deployment. 2. List of client GPOs present in the DA deployment. 3. Status of force tunnel. 4. NRPT object (for force tunnel properties). 5. Support for down-level (enable/disable). 6. Laptop-only deployment (enable/disable).

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

[**PS\_DAClient**](ps-daclient.md)
</dt> </dl>

 

 





