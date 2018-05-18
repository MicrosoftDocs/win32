---
title: PS\_DAClient class
description: Represents the client machines in a DA deployment.
audience: developer
ms.assetid: 'bf9fc446-8176-43f7-9298-edba76c07c92'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DAClient class", "PS_DAClient class, described"]
topic_type:
- apiref
api_name:
- PS_DAClient
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_DAClient class

Represents the client machines in a DA deployment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAClient
{
};
```

## Members

The **PS\_DAClient** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAClient** class has these methods.



| Method                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddByClientDownlevelSGGpo**](addbyclientdownlevelsggpo-ps-daclient.md)       | This cmdlet performs the following operations for W8 and down-level (W7) clients 1. Adds one or more client machine security group(s) to the DA deployment2. Adds one or more DA client GPO(s) in domain(s)3. In a multi-site deployment, adds one or more security group(s) of down-level clients to the DA deployment. These down-level clients can then connect only to the specified site4. In a multi-site deployment, adds one or more down-level DA client GPO(s) in a domain(s)<br/> |
| [**AddByClientSGGpo**](addbyclientsggpo-ps-daclient.md)                         | This cmdlet performs the following operations for W8 and down-level (W7) clients 1. Adds one or more client machine security group(s) to the DA deployment2. Adds one or more DA client GPO(s) in domain(s)3. In a multi-site deployment, adds one or more security group(s) of down-level clients to the DA deployment. These down-level clients can then connect only to the specified site4. In a multi-site deployment, adds one or more down-level DA client GPO(s) in a domain(s)<br/> |
| [**Get**](get-ps-daclient.md)                                                   | This cmdlet displays the list of client security groups that are part of the DA deployment and the client properties<br/>                                                                                                                                                                                                                                                                                                                                                                    |
| [**RemoveByClientDownlevelSGGpo**](removebyclientdownlevelsggpo-ps-daclient.md) | This cmdlet performs the following operations1. Removes one or more client machine security group(s) from the DA deployment 2. Removes one or more DA client GPO(s) from domain(s) 3. In a multi-site deployment, removes one or more security group(s) of down-level clients from the DA deployment. These down-level clients can connect only to the specified site 4. In a multi-site deployment, removes one or more down-level DA client GPO(s) from domain(s)<br/>                     |
| [**RemoveByClientSGGpo**](removebyclientsggpo-ps-daclient.md)                   | This cmdlet performs the following operations1. Removes one or more client machine security group(s) from the DA deployment 2. Removes one or more DA client GPO(s) from domain(s) 3. In a multi-site deployment, removes one or more security group(s) of down-level clients from the DA deployment. These down-level clients can connect only to the specified site 4. In a multi-site deployment, removes one or more down-level DA client GPO(s) from domain(s)<br/>                     |
| [**Set**](set-ps-daclient.md)                                                   | This cmdlet configures the properties related to a DA client.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                           |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





