---
title: AddClusterNameAccount method of the MSCluster\_Cluster class
description: Creates a cluster name account in Active Directory Domain Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a270efe-1b7a-4e8c-bc34-41d9893bea64
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddClusterNameAccount method
- AddClusterNameAccount method, MSCluster_Cluster class
- MSCluster_Cluster class, AddClusterNameAccount method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.AddClusterNameAccount
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddClusterNameAccount method of the MSCluster\_Cluster class

Creates a cluster name account in Active Directory Domain Services.

## Syntax


```mof
void AddClusterNameAccount(
  [in] string Name,
  [in] string DomainName,
  [in] string UserName,
  [in] string Password,
  [in] uint32 AdministrativeAccessPoint
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the cluster name account that this method creates.

</dd> <dt>

*DomainName* \[in\]
</dt> <dd>

Specifies the Active Directory Domain Services domain in which this method creates a cluster name account. When NULL, the caller information is used. Should be used with *UserName* and *Password*.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

Specified the account name to use when connecting to the Active Directory Domain Service. When NULL, the caller information is used. Should be used with *DomainName* and *Password*.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

Specifies the user account password to use when connecting to the Active Directory Domain Service. When NULL, the caller informatin is used. Should be used with *DomainName* and *UserName*.

</dd> <dt>

*AdministrativeAccessPoint* \[in\]
</dt> <dd>

The type of the cluster management point.

<dt>

<span id="ActiveDirectoryAndDns"></span><span id="activedirectoryanddns"></span><span id="ACTIVEDIRECTORYANDDNS"></span>

**ActiveDirectoryAndDns** (1)


</dt> <dd></dd> <dt>

<span id="Dns"></span><span id="dns"></span><span id="DNS"></span>

**Dns** (2)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWMI.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





