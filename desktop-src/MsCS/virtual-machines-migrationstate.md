---
title: MigrationState
description: Specifies the state of a live migration of a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4824b60-be57-4c51-b0f5-41fe5fd044a2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MigrationState Failover Cluster ,for virtual machines
- MigrationState Failover Cluster
topic_type:
- apiref
api_name:
- MigrationState
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MigrationState

Specifies the state of a live migration of a virtual machine (VM) from one node of the cluster to another node of the cluster. The following table summarizes the attributes of the **MigrationState** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 5                                         |
| Default   | 0                                         |



 

## Remarks

The following table summarizes the values for **MigrationState**.



| Name                     | Value                  | Description                                                                                                                                               |
|--------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| No Migration<br/>  | 0 (Default)<br/> | No migration is in progress.<br/>                                                                                                                   |
| Setup<br/>         | 1<br/>           | The migration of the VM was started and the setup of the migration is in progress.<br/>                                                             |
| Data Transfer<br/> | 2<br/>           | The VM data (including the contents of the VM memory) is being transferred to the target node.<br/>                                                 |
| Move<br/>          | 3<br/>           | The move of the VM resource group is in progress.<br/>                                                                                              |
| Canceled<br/>      | 4<br/>           | An earlier migration attempt was canceled.<br/>                                                                                                     |
| Failure<br/>       | 5<br/>           | An earlier migration attempt failed. The **MigrationState** property will retain this value until it is reset or another migration is started.<br/> |



 

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





