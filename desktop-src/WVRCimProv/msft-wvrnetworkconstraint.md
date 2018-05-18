---
title: MSFT\_WvrNetworkConstraint class
description: This class represents the Network constraints for Storage Replica partnerships.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c25fcd63-e7a5-48fe-aa36-96b1625d6566'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WvrNetworkConstraint class", "MSFT_WvrNetworkConstraint class, described"]
topic_type:
- apiref
api_name:
- MSFT_WvrNetworkConstraint
- MSFT_WvrNetworkConstraint.SourceRGName
- MSFT_WvrNetworkConstraint.DestinationRGName
- MSFT_WvrNetworkConstraint.SourceComputerName
- MSFT_WvrNetworkConstraint.DestinationComputerName
- MSFT_WvrNetworkConstraint.DestinationNWInterface
- MSFT_WvrNetworkConstraint.SourceNWInterface
api_location:
- wvrcimprov.dll
api_type:
- DllExport
---

# MSFT\_WvrNetworkConstraint class

This class represents the Network constraints for Storage Replica partnerships.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrNetworkConstraint
{
  string SourceRGName;
  string DestinationRGName;
  string SourceComputerName;
  string DestinationComputerName;
  string DestinationNWInterface[];
  string SourceNWInterface[];
};
```

## Members

The **MSFT\_WvrNetworkConstraint** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WvrNetworkConstraint** class has these properties.

<dl> <dt>

**DestinationComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

FQDN or NetBIOS name of the computer hosting destination replication group.

</dd> <dt>

**DestinationNWInterface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of constraints containing destination Network indexes.

</dd> <dt>

**DestinationRGName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Destination replication group within this partnership.

</dd> <dt>

**SourceComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

FQDN or NetBIOS name of the computer hosting source replication group.

</dd> <dt>

**SourceNWInterface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of constraints containing source Network indexes.

</dd> <dt>

**SourceRGName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Source replication group within this partnership.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



 

 





