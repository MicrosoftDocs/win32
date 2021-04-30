---
description: Associates an instance of an allocated resource with the resource pool from which it was allocated.
ms.assetid: BA3168C7-E4F1-414B-827B-1A811069F223
title: Msvm_ElementAllocatedFromPool class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ElementAllocatedFromPool
- Msvm_ElementAllocatedFromPool.Antecedent
- Msvm_ElementAllocatedFromPool.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ElementAllocatedFromPool class

Associates an instance of an allocated resource with the resource pool from which it was allocated.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementAllocatedFromPool : CIM_ElementAllocatedFromPool
{
  CIM_ResourcePool   REF Antecedent;
  CIM_LogicalElement REF Dependent;
};
```

## Members

The **Msvm\_ElementAllocatedFromPool** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementAllocatedFromPool** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ResourcePool**](/previous-versions//cc136903(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override**, **Max** (1)
</dt> </dl>

The resource pool. This property is inherited from [**CIM\_ElementAllocatedFromPool**](/previous-versions//cc150668(v=vs.85)).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalElement**](/windows/desktop/CIMWin32Prov/cim-logicalelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The allocated resource. This property is inherited from [**CIM\_ElementAllocatedFromPool**](/previous-versions//cc150668(v=vs.85)).

</dd> </dl>

## Remarks

Access to the **Msvm\_ElementAllocatedFromPool** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md)
</dt> <dt>

[**CIM\_ElementAllocatedFromPool**](/previous-versions//cc150668(v=vs.85))
</dt> <dt>

[**Msvm\_ElementAllocatedFromPool (V1)**](/previous-versions/windows/desktop/virtual/msvm-elementallocatedfrompool)
</dt> <dt>

[Resource Management Classes](resource-management-classes.md)
</dt> </dl>

 

