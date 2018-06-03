---
title: SetAttributes method of the MSFT\_StorageQoSPolicyStore class
description: Sets attributes for the policy store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 664A37EF-725C-433D-9582-C777A5B8AAAF
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-storage-qos
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetAttributes method
- SetAttributes method, MSFT_StorageQoSPolicyStore interface
- MSFT_StorageQoSPolicyStore interface, SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicyStore.SetAttributes
api_location:
- StorageQOS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_StorageQoSPolicyStore class

Sets attributes for the policy store.

## Syntax


```mof
sint32 SetAttributes(
  [in] uint32 IOPSNormalizationSize
);
```



## Parameters

<dl> <dt>

*IOPSNormalizationSize* \[in\]
</dt> <dd>

Normalized I/O size in bytes.

</dd> </dl>

## Return value

<dl> <dt>

**Policy ID cannot be zero.**
</dt> <dd>

1

</dd> <dt>

**Default policy cannot be modified.**
</dt> <dd>

2

</dd> <dt>

**Default policy cannot be removed.**
</dt> <dd>

3

</dd> <dt>

**Policy name cannot be empty.**
</dt> <dd>

4

</dd> <dt>

**Parent policy not found.**
</dt> <dd>

5

</dd> <dt>

**Limit cannot be higher than 1 billion IOPS.**
</dt> <dd>

6

</dd> <dt>

**Reservation cannot be higher than 1 billion IOPS.**
</dt> <dd>

7

</dd> <dt>

**Reservation cannot be higher than the limit.**
</dt> <dd>

8

</dd> <dt>

**Policy type not recognized.**
</dt> <dd>

9

</dd> <dt>

**Policy type cannot be changed**
</dt> <dd>

10

Policy type cannot be changed.

</dd> <dt>

**Multi-instance policies cannot have child policies**
</dt> <dd>

11

Multi-instance policies cannot have child policies.

</dd> <dt>


</dt> <dd>

12

</dd> <dt>


</dt> <dd>

1024

Reserved.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageQoSPolicyStore**](msft-storageqospolicystore.md)
</dt> </dl>

 

 





