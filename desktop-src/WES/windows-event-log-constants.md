---
title: Windows Event Log Constants (WinEvt.h)
description: Windows Event Log defines the following constants
ms.assetid: d3a4a136-ca33-4dad-95ad-af1be6687843
topic_type:
- apiref
api_name:
- EVT_VARIANT_TYPE_MASK
- EVT_VARIANT_TYPE_ARRAY
- EVT_READ_ACCESS
- EVT_WRITE_ACCESS
- EVT_CLEAR_ACCESS
- EVT_ALL_ACCESS
api_location:
- WinEvt.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Event Log Constants

Windows Event Log defines the following constants:

<dl> <dt>

<span id="EVT_VARIANT_TYPE_MASK"></span><span id="evt_variant_type_mask"></span>**EVT\_VARIANT\_TYPE\_MASK**
</dt> <dd> <dl> <dt>

0x7f
</dt> <dt>



A bitmask that you use to mask out the array bit of the variant type, so you can determine the data type of the variant value that the [**EVT\_VARIANT**](/windows/desktop/api/WinEvt/ns-winevt-evt_variant) structure contains.


</dt> </dl> </dd> <dt>

<span id="EVT_VARIANT_TYPE_ARRAY"></span><span id="evt_variant_type_array"></span>**EVT\_VARIANT\_TYPE\_ARRAY**
</dt> <dd> <dl> <dt>

128
</dt> <dt>



The **Type** member of the [**EVT\_VARIANT**](/windows/desktop/api/WinEvt/ns-winevt-evt_variant) structure has this bit set if the variant contains a pointer to an array of values, rather than the value itself.


</dt> </dl> </dd> <dt>

<span id="EVT_READ_ACCESS"></span><span id="evt_read_access"></span>**EVT\_READ\_ACCESS**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>



Read access control permission that allows information to be read from an event log.


</dt> </dl> </dd> <dt>

<span id="EVT_WRITE_ACCESS"></span><span id="evt_write_access"></span>**EVT\_WRITE\_ACCESS**
</dt> <dd> <dl> <dt>

0x2
</dt> <dt>



Write access control permission that allows information to be written to an event log.


</dt> </dl> </dd> <dt>

<span id="EVT_CLEAR_ACCESS"></span><span id="evt_clear_access"></span>**EVT\_CLEAR\_ACCESS**
</dt> <dd> <dl> <dt>

0x4
</dt> <dt>



Clear access control permission that allows all information to be cleared from an event log.


</dt> </dl> </dd> <dt>

<span id="EVT_ALL_ACCESS"></span><span id="evt_all_access"></span>**EVT\_ALL\_ACCESS**
</dt> <dd> <dl> <dt>

0x7
</dt> <dt>



All (read, write, clear, and delete) access control permission.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>WinEvt.h</dt> </dl> |



 

 





