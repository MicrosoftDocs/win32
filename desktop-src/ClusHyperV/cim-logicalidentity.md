---
title: CIM\_LogicalIdentity class
description: Represents a generic association between two managed elements that represent different aspects of the same underlying entity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c3218f20-4893-4bc0-9535-2b3e52e3257e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_LogicalIdentity class", "CIM_LogicalIdentity class, described"]
topic_type:
- apiref
api_name:
- CIM_LogicalIdentity
- CIM_LogicalIdentity.SystemElement
- CIM_LogicalIdentity.SameElement
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_LogicalIdentity class

Represents a generic association between two managed elements that represent different aspects of the same underlying entity. This relationship conveys what could be defined with multiple inheritance. In most scenarios, a logical identity association is determined by the equivalence of keys or some other identifying properties of the associated elements.

An example of this association is a [**CIM\_LogicalDevice**](cim-logicaldevice.md) object that is both a bus entity (USB) and a functional entity (keyboard).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_LogicalIdentity
{
  CIM_ManagedElement REF SystemElement;
  CIM_ManagedElement REF SameElement;
};
```

## Members

The **CIM\_LogicalIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LogicalIdentity** class has these properties.

<dl> <dt>

**SameElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The second aspect in the association.

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The first aspect in the association. The use of System in the property name does not limit the scope of the association.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





