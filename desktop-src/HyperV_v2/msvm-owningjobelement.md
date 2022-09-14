---
description: Represents an association between a job and the managed element responsible for the creation of the job.
ms.assetid: 1a100c7e-7e17-47dd-b730-c05c5e4dccda
title: Msvm_OwningJobElement class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_OwningJobElement
- Msvm_OwningJobElement.OwningElement
- Msvm_OwningJobElement.OwnedElement
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_OwningJobElement class

Represents an association between a job and the managed element responsible for the creation of the job.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_OwningJobElement : CIM_OwningJobElement
{
  CIM_ManagedElement REF OwningElement;
  Msvm_ConcreteJob   REF OwnedElement;
};
```

## Members

The **Msvm\_OwningJobElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_OwningJobElement** class has these properties.

<dl> <dt>

**OwnedElement**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ConcreteJob**](msvm-concretejob.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The job created by the managed element.

</dd> <dt>

**OwningElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The managed element responsible for the creation of the job.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

