---
description: The CIM\_ActionSequence association defines a series of operations that transition the software element (referenced by the CIM\_SoftwareElementActions association) to its next state, or removes the software element from its current state.
ms.assetid: b539c424-bc2a-414b-b56c-72550004720f
ms.tgt_platform: multiple
title: CIM_ActionSequence class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ActionSequence
- CIM_ActionSequence.Next
- CIM_ActionSequence.Prior
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ActionSequence class

The **CIM\_ActionSequence** association defines a series of operations that transition the software element (referenced by the [**CIM\_SoftwareElementActions**](cim-softwareelementactions.md) association) to its next state, or removes the software element from its current state.

The next-state actions and uninstall actions associated with a particular software element must be a continuous sequence. Since **CIM\_ActionSequence** is an association, the loops on the [**CIM\_Action**](cim-action.md) class, with roles for the "prior" action and "next" action, form a sequence.

The need for a continuous sequence implies:

-   Within the set of next-state or uninstall actions, there is only one action that does not have an instance of the **CIM\_ActionSequence** association referencing it in the "next" role. This is the first action in the sequence.
-   Within the set of next-state or uninstall actions, there is only one action that does not have an instance of the **CIM\_ActionSequence** association referencing it in the "prior" role. This is the last action in the sequence.
-   All other actions within the set of next-state and uninstall actions must participate in two instances of the **CIM\_ActionSequence** association, one in a "prior" role and one in the "next" role.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{F127E50E-E3E0-11d2-8601-0000F8102E5F}"), AMENDMENT]
class CIM_ActionSequence
{
  CIM_Action REF Next;
  CIM_Action REF Prior;
};
```

## Members

The **CIM\_ActionSequence** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ActionSequence** class has these properties.

<dl> <dt>

**Next**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0)
</dt> </dl>

Reference to the next action.

</dd> <dt>

**Prior**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0)
</dt> </dl>

Reference to the prior action.

</dd> </dl>

## Remarks

The [**CIM\_Action**](cim-action.md) classes participating in this association must have the same value for the **Direction** property.

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[CIM Classes](/windows/desktop/WmiSdk/cimclas)
</dt> </dl>

 

