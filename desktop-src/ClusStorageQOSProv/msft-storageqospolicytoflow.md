---
title: MSFT\_StorageQoSPolicyToFlow class
description: Associates a policy to a flow.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0466776f-81e1-4e0b-964a-65762263f55e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-storage-qos'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_StorageQoSPolicyToFlow class", "MSFT_StorageQoSPolicyToFlow class, described"]
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicyToFlow
- MSFT_StorageQoSPolicyToFlow.Policy
- MSFT_StorageQoSPolicyToFlow.Flow
api_location:
- StorageQOS.dll
api_type:
- DllExport
---

# MSFT\_StorageQoSPolicyToFlow class

Associates a policy to a flow.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("STORAGEQOS"), AMENDMENT]
class MSFT_StorageQoSPolicyToFlow
{
  MSFT_StorageQoSPolicy REF Policy;
  MSFT_StorageQoSFlow   REF Flow;
};
```

## Members

The **MSFT\_StorageQoSPolicyToFlow** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageQoSPolicyToFlow** class has these properties.

<dl> <dt>

**Flow**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageQoSFlow**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**MSFT\_StorageQoSFlow**](msft-storageqosflow.md) containing the flow to associate.

</dd> <dt>

**Policy**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageQoSPolicy**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**MSFT\_StorageQoSPolicy**](msft-storageqospolicy.md) containing the policy to associate.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



 

 





