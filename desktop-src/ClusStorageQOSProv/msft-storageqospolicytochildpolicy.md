---
title: MSFT\_StorageQoSPolicyToChildPolicy class
description: Associates a parent policy to a child policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ad5d848a-c32a-42c1-8d50-4da4c1cf30c9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-storage-qos'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_StorageQoSPolicyToChildPolicy class", "MSFT_StorageQoSPolicyToChildPolicy class, described"]
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicyToChildPolicy
- MSFT_StorageQoSPolicyToChildPolicy.ParentPolicy
- MSFT_StorageQoSPolicyToChildPolicy.ChildPolicy
api_location:
- StorageQOS.dll
api_type:
- DllExport
---

# MSFT\_StorageQoSPolicyToChildPolicy class

Associates a parent policy to a child policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("STORAGEQOS"), AMENDMENT]
class MSFT_StorageQoSPolicyToChildPolicy
{
  MSFT_StorageQoSPolicy REF ParentPolicy;
  MSFT_StorageQoSPolicy REF ChildPolicy;
};
```

## Members

The **MSFT\_StorageQoSPolicyToChildPolicy** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageQoSPolicyToChildPolicy** class has these properties.

<dl> <dt>

**ChildPolicy**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageQoSPolicy**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The child policy to associate.

</dd> <dt>

**ParentPolicy**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageQoSPolicy**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The parent policy to associate.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



 

 





