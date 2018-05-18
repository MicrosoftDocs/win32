---
Description: 'The CIM\_AdjacentSlots association describes the layout of slots on a hosting board or adapter card.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'd604647f-7b2f-4f99-8d98-adf115ae9dfb'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CIM\_AdjacentSlots class'
---

# CIM\_AdjacentSlots class

The **CIM\_AdjacentSlots** association describes the layout of slots on a hosting board or adapter card. Information, such as the distance between the slots and whether they are "shared" (if one is populated, then the other slot cannot be used), is conveyed as association properties.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Association, UUID("{FAF76B88-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_AdjacentSlots
{
  real32       DistanceBetweenSlots;
  boolean      SharedSlots;
  CIM_Slot REF SlotA;
  CIM_Slot REF SlotB;
};
```

## Members

The **CIM\_AdjacentSlots** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_AdjacentSlots** class has these properties.

<dl> <dt>

**DistanceBetweenSlots**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("inches")
</dt> </dl>

Distance, in inches, between adjacent slots.

</dd> <dt>

**SharedSlots**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, one of the slots is populated by an adapter card; the other slot must be left empty.

</dd> <dt>

**SlotA**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Slot**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to one of the adjacent slots.

</dd> <dt>

**SlotB**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Slot**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the "other" adjacent slot.

</dd> </dl>

## Remarks

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[CIM Classes](https://msdn.microsoft.com/library/aa386179)
</dt> </dl>

 

 




