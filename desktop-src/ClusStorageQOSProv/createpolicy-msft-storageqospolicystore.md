---
title: CreatePolicy method of the MSFT\_StorageQoSPolicyStore class
description: Creates a storage QoS policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a07834c-90f3-415a-a9bf-0b8fabe8e03f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-storage-qos
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreatePolicy method
- CreatePolicy method, MSFT_StorageQoSPolicyStore class
- MSFT_StorageQoSPolicyStore class, CreatePolicy method
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicyStore.CreatePolicy
api_location:
- StorageQOS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreatePolicy method of the MSFT\_StorageQoSPolicyStore class

Creates a storage QoS policy.

## Syntax


```mof
sint32 CreatePolicy(
  [in, out] MSFT_StorageQoSPolicy Policy
);
```



## Parameters

<dl> <dt>

*Policy* \[in, out\]
</dt> <dd>

a [**MSFT\_StorageQoSPolicy**](msft-storageqospolicy.md) containing the new policy.

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

 

 





