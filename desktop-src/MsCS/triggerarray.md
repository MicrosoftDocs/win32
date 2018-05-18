---
title: TriggerArray
description: Triggers for the Volume Shadow Copy Service resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '605a9722-6122-4886-9adf-478832e7894c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["TriggerArray Failover Cluster , for Volume Shadow Copy Service Task private properties", "TriggerArray Failover Cluster"]
topic_type:
- apiref
api_name:
- TriggerArray
api_type:
- NA
---

# TriggerArray

Specifies the triggers for the Volume Shadow Copy Service resource. The following table summarizes the attributes of the **TriggerArray** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **BYTE**                                                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_BINARY**](clusprop-binary.md)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | TBD                                                              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_VSSTASK\_TRIGGERARRAY**.

The content of the **TriggerArray** property is an array of [**TASK\_TRIGGER**](https://msdn.microsoft.com/library/windows/desktop/aa383618) structures.

The [**CLUSPROP\_BINARY\_DECLARE**](clusprop-binary-declare.md) macro creates a [**CLUSPROP\_BINARY**](clusprop-binary.md) structure with an array of the correct size.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Volume Shadow Copy Service Task Private Properties](volume-shadow-copy-service-task-private-properties.md)
</dt> <dt>

[**CLUSPROP\_BINARY**](clusprop-binary.md)
</dt> <dt>

[**CLUSPROP\_BINARY\_DECLARE**](clusprop-binary-declare.md)
</dt> <dt>

[**TASK\_TRIGGER**](https://msdn.microsoft.com/library/windows/desktop/aa383618)
</dt> </dl>

 

 





