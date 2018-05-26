---
title: CIM\_ConcreteDependency class
description: A generic association used to establish dependency relationships between ManagedElements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 531b4f37-5a90-4f30-84f9-4d3a1112ce5a
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ConcreteDependency class iSCSI Software Target API
- CIM_ConcreteDependency class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_ConcreteDependency
- CIM_ConcreteDependency.Antecedent
- CIM_ConcreteDependency.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_ConcreteDependency class

A generic association used to establish dependency relationships between ManagedElements. It is defined as a concrete subclass of the abstract CIM\_Dependency class, to be used in place of many specific subclasses of Dependency that add no semantics, that is subclasses that do not clarify the type of dependency, update cardinalities, or add or remove qualifiers. Note that when you define additional semantics for Dependency, this class must not be subclassed. Specific semantics continue to be defined as subclasses of the abstract CIM\_Dependency. ConcreteDependency is limited in its use as a concrete form of a general dependency.

It was deemed more prudent to create this concrete subclass than to change Dependency from an abstract to a concrete class. Dependency already had multiple abstract subclasses in the CIM Schema, and wider industry usage and impact could not be anticipated.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::CoreElements")]
class CIM_ConcreteDependency : CIM_Dependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **CIM\_ConcreteDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ConcreteDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

Antecedent represents the independent object in this association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

Dependent represents the object that is dependent on the Antecedent.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





