---
title: AddByClientSGGpo method of the PS\_DAClient class
description: This cmdlet performs the following operations for W8 and down-level (W7) clients 1.
audience: developer
ms.assetid: e0fc063f-a77f-4ec1-8c8a-516b1020f814
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByClientSGGpo method
- AddByClientSGGpo method, PS_DAClient class
- PS_DAClient class, AddByClientSGGpo method
topic_type:
- apiref
api_name:
- PS_DAClient.AddByClientSGGpo
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByClientSGGpo method of the PS\_DAClient class

This cmdlet performs the following operations for W8 and down-level (W7) clients 1. Adds one or more client machine security group(s) to the DA deployment2. Adds one or more DA client GPO(s) in domain(s)3. In a multi-site deployment, adds one or more security group(s) of down-level clients to the DA deployment. These down-level clients can then connect only to the specified site4. In a multi-site deployment, adds one or more down-level DA client GPO(s) in a domain(s).

## Syntax


```mof
uint32 AddByClientSGGpo(
  [in]  string   SecurityGroupNameList[],
  [in]  string   GpoName[],
  [in]  string   ComputerName,
  [in]  boolean  PassThru,
  [out] DAClient cmdletOutput
);
```



## Parameters

<dl> <dt>

*SecurityGroupNameList* \[in\]
</dt> <dd>

List of client security groups that are to be added to the DA deployment. Each SG is specified in DOMAIN\\SG\_NAME format

</dd> <dt>

*GpoName* \[in\]
</dt> <dd>

This parameter represents the name to be used when creating the client GPO in the specified domain or represents the domain in which a client GPO with the default name should be created. GPO is specified in the format DOMAIN\\GPO\_NAME. Domain is specified in the format DOMAIN. If the parameter contains only the domain name then the following default GPO name is used: \[domain\] client policy for \[DA connection friendly name\] A list of GPOs can be specified

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

IPv4/IPv6 address or hostname of the machine on which the remote access server machine specific tasks should be executed

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

 

 





