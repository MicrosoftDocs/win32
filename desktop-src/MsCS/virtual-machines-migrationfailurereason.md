---
title: MigrationFailureReason
description: Provides the HRESULT that details the reason for a failed live migration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7f5887dc-478d-45b1-9b8c-350dc68fb5e0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MigrationFailureReason Failover Cluster ,for virtual machines
- MigrationFailureReason Failover Cluster
topic_type:
- apiref
api_name:
- MigrationFailureReason
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MigrationFailureReason

Provides the **HRESULT** that details the reason for a failed live migration. The following table summarizes the attributes of the **MigrationFailureReason** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 0                                         |



 

## Remarks

The following table summarizes the values for **MigrationFailureReason**.



| Name                   | Value                  | Description                                                                |
|------------------------|------------------------|----------------------------------------------------------------------------|
| **S\_OK**<br/>   | 0 (Default)<br/> | The migration completed successfully.<br/>                           |
| **E\_BUSY**<br/> | 0x800700AA<br/>  | The migration failed because another migration was in progress.<br/> |
| **E\_FAIL**<br/> | 0x80004005<br/>  | The migration failed for some other reason.<br/>                     |



 

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

 

 





