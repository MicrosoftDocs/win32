---
title: MigrationProgress
description: Provides the estimated percentage of the completion of the migration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b99a2494-3962-467e-8934-e5f20528db94'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MigrationProgress Failover Cluster ,for virtual machines", "MigrationProgress Failover Cluster"]
topic_type:
- apiref
api_name:
- MigrationProgress
api_type:
- NA
---

# MigrationProgress

Provides the estimated percentage of the completion of the migration. The following table summarizes the attributes of the **MigrationProgress** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 100                                       |
| Default   | 0                                         |



 

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





