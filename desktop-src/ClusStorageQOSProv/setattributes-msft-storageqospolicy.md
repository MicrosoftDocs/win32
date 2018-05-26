---
title: SetAttributes method of the MSFT\_StorageQoSPolicy class
description: Sets the attributes on a policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bfdc2c37-8acf-4916-9d8c-ca4578284c28
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-storage-qos
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetAttributes method
- SetAttributes method, MSFT_StorageQoSPolicy class
- MSFT_StorageQoSPolicy class, SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicy.SetAttributes
api_location:
- StorageQOS.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetAttributes method of the MSFT\_StorageQoSPolicy class

Sets the attributes on a policy.

## Syntax


```mof
sint32 SetAttributes(
  [in] string NewName,
  [in] uint64 Limit,
  [in] uint64 Reservation,
  [in] uint64 BandwidthLimit
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

The new name of the policy.

</dd> <dt>

*Limit* \[in\]
</dt> <dd>

The new limit of the policy.

</dd> <dt>

*Reservation* \[in\]
</dt> <dd>

The new reservation of the policy.

</dd> <dt>

*BandwidthLimit* \[in\]
</dt> <dd>

The new bandwidth limit in bytes per second.

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

[**MSFT\_StorageQoSPolicy**](msft-storageqospolicy.md)
</dt> </dl>

 

 





