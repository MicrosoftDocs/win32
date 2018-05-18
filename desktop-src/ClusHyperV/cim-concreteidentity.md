---
title: CIM\_ConcreteIdentity class
description: Represents an association between two managed elements that represent different aspects of the same underlying entity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f6fee9d4-aa09-4e36-a0cd-b7562ddecfea'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ConcreteIdentity class", "CIM_ConcreteIdentity class, described"]
topic_type:
- apiref
api_name:
- CIM_ConcreteIdentity
- CIM_ConcreteIdentity.SystemElement
- CIM_ConcreteIdentity.SameElement
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_ConcreteIdentity class

Represents an association between two managed elements that represent different aspects of the same underlying entity.

This is a concrete subclass of [**CIM\_LogicalIdentity**](cim-logicalidentity.md) that is used when the additional semantics supported by some of the **CIM\_LogicalIdentity** subclasses are not needed. This class must not be subclassed to define additional semantics. Instead, you can subclass **CIM\_LogicalIdentity**.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_ConcreteIdentity : CIM_LogicalIdentity
{
  CIM_ManagedElement REF SystemElement;
  CIM_ManagedElement REF SameElement;
};
```

## Members

The **CIM\_ConcreteIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ConcreteIdentity** class has these properties.

<dl> <dt>

**SameElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SameElement")
</dt> </dl>

The second aspect in the association.

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SystemElement")
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

[**CIM\_LogicalIdentity**](cim-logicalidentity.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





