---
title: MSFT\_SMFabricToZoneSet class
description: Represents a relationship between a Windows Fabric storage service and a collection of DNS zones.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0246e7bc-d6a7-4b0c-96da-9204689b10df'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMFabricToZoneSet class", "MSFT_SMFabricToZoneSet class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMFabricToZoneSet
- MSFT_SMFabricToZoneSet.Parent
- MSFT_SMFabricToZoneSet.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMFabricToZoneSet class

Represents a relationship between a Windows Fabric storage service and a collection of DNS zones.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, dynamic, provider("WMIStorage")]
class MSFT_SMFabricToZoneSet
{
  MSFT_SMFabric  REF Parent;
  MSFT_SMZoneSet REF Child;
};
```

## Members

The **MSFT\_SMFabricToZoneSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMFabricToZoneSet** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMZoneSet**](msft-smzoneset.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMZoneSet**](msft-smzoneset.md) object that represents the collection of DNS zones in the relationship.

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMFabric**](msft-smfabric.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the [**MSFT\_SMFabric**](msft-smfabric.md) object that represents the Windows Fabric storage service in the relationship.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





