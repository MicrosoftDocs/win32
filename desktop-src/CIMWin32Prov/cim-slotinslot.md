---
description: The CIM\_SlotInSlot relationship represents the ability of a special adapter to extend the existing slot structure to enable otherwise incompatible cards to be plugged into a frame or hosting board.
ms.assetid: 688231de-49fd-415d-b2c8-ef0dd4dcaee4
ms.tgt_platform: multiple
title: CIM_SlotInSlot class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SlotInSlot
- CIM_SlotInSlot.Dependent
- CIM_SlotInSlot.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_SlotInSlot class

The **CIM\_SlotInSlot** relationship represents the ability of a special adapter to extend the existing slot structure to enable otherwise incompatible cards to be plugged into a frame or hosting board. Slots are special types of connectors into which adapter cards are typically inserted. The adapter effectively creates a new slot and can be thought of (conceptually) as a slot in a slot. Cards that would otherwise be physically or electrically incompatible with the existing slots would be supported by interfacing to the slot provided by the adapter. For example, networking boards are very expensive. As new hardware becomes available, chassis and card configurations change. To protect the investment of their customers, networking vendors will manufacture special adapters that enable old cards to fit into new chassis or hosting boards or new cards to fit into old cards by using a special adapter that fits over one or more existing slots and presents a new slot into which the card can fit.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B87-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_SlotInSlot : CIM_ConnectedTo
{
  CIM_Slot REF Dependent;
  CIM_Slot REF Antecedent;
};
```

## Members

The **CIM\_SlotInSlot** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SlotInSlot** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Slot**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_Slot**](cim-slot.md) that describes the existing slot(s) of the hosting board, or frame that are being adapted to accommodate a card that would otherwise not be physically and/or electrically compatible with it.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Slot**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_Slot**](cim-slot.md) that describes the new slot provided by the adapter board.

</dd> </dl>

## Remarks

The **CIM\_SlotInSlot** class is derived from [**CIM\_ConnectedTo**](cim-connectedto.md).

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

[**CIM\_ConnectedTo**](cim-connectedto.md)
</dt> </dl>

 

