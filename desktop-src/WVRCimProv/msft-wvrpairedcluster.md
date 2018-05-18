---
title: MSFT\_WvrPairedCluster class
description: This class represents a storage replica paired cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6986c5d5-91e9-4067-babb-3901be4478a9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WvrPairedCluster class", "MSFT_WvrPairedCluster class, described"]
topic_type:
- apiref
api_name:
- MSFT_WvrPairedCluster
- MSFT_WvrPairedCluster.ClusterName
- MSFT_WvrPairedCluster.PairedClusterName
api_location:
- wvrcimprov.dll
api_type:
- DllExport
---

# MSFT\_WvrPairedCluster class

This class represents a storage replica paired cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrPairedCluster
{
  string ClusterName;
  string PairedClusterName;
};
```

## Members

The **MSFT\_WvrPairedCluster** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrPairedCluster** class has these properties.

<dl> <dt>

**ClusterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the cluster.

</dd> <dt>

**PairedClusterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the paired cluster.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



 

 





