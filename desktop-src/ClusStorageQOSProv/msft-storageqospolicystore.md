---
title: MSFT\_StorageQoSPolicyStore class
description: Factory class for storage QOS policies.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f13bda89-a85e-479a-aa19-1cdd273470fd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-storage-qos'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_StorageQoSPolicyStore class", "MSFT_StorageQoSPolicyStore class, described"]
topic_type:
- apiref
api_name:
- MSFT_StorageQoSPolicyStore
- MSFT_StorageQoSPolicyStore.Id
- MSFT_StorageQoSPolicyStore.IOPSNormalizationSize
api_location:
- StorageQOS.dll
api_type:
- DllExport
---

# MSFT\_StorageQoSPolicyStore class

Factory class for storage QOS policies.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("STORAGEQOS"), AMENDMENT]
class MSFT_StorageQoSPolicyStore
{
  string Id;
  uint32 IOPSNormalizationSize;
};
```

## Members

The **MSFT\_StorageQoSPolicyStore** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageQoSPolicyStore** class has these methods.



| Method                                                            | Description                                      |
|:------------------------------------------------------------------|:-------------------------------------------------|
| [**CreatePolicy**](createpolicy-msft-storageqospolicystore.md)   | Creates a storage QOS policy.<br/>         |
| [**SetAttributes**](msft-storageqospolicystore-setattributes.md) | Sets attributes for the policy store.<br/> |



 

### Properties

The **MSFT\_StorageQoSPolicyStore** class has these properties.

<dl> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A UUID uniquely identifying the policy store.

</dd> <dt>

**IOPSNormalizationSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Normalized I/O size in bytes.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>StorageQOS.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StorageQOS.dll</dt> </dl> |



 

 





