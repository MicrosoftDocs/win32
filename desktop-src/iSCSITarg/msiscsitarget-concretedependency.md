---
title: MSISCSITARGET\_ConcreteDependency class
description: A generic association that is used to represent dependency relationships between CIM\_ManagedElement instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 379a9bb2-bc13-456d-a25b-e598c9cce676
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_ConcreteDependency class iSCSI Software Target API
- MSISCSITARGET_ConcreteDependency class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_ConcreteDependency
- MSISCSITARGET_ConcreteDependency.Antecedent
- MSISCSITARGET_ConcreteDependency.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSISCSITARGET\_ConcreteDependency class

A generic association that is used to represent dependency relationships between [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/cc136871) instances. The **MSISCSITARGET\_ConcreteDependency** class is a concrete subclass of the abstract [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238) class.

> [!Note]  
> The **MSISCSITARGET\_ConcreteDependency** class is limited in its use to instances of a general dependency and should not be used as a base class for more specific dependency classes. Instead, define a concrete subclass of [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238) or one of its abstract subclasses.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_ConcreteDependency : CIM_ConcreteDependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **MSISCSITARGET\_ConcreteDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_ConcreteDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Antecedent represents the independent object in this association.

This property is inherited from [**CIM\_ConcreteDependency**](cim-concretedependency.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Dependent represents the object that is dependent on the Antecedent.

This property is inherited from [**CIM\_ConcreteDependency**](cim-concretedependency.md).

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

[**CIM\_ConcreteDependency**](cim-concretedependency.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





