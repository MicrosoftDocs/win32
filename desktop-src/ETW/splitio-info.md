---
Description: This class is the event type class for split IO events. The following syntax is simplified from MOF code.
ms.assetid: 0eb1f712-8b1c-4de1-b701-5c7dbabb0f55
title: SplitIo\_Info class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SplitIo\_Info class

This class is the event type class for split IO events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{32}, EventTypeName{"VolMgr"}]
class SplitIo_Info : SplitIo
{
  uint32 ParentIrp;
  uint32 ChildIrp;
};
```

## Members

The **SplitIo\_Info** class has these types of members:

-   [Properties](#properties)

### Properties

The **SplitIo\_Info** class has these properties.

<dl> <dt>

**ChildIrp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(2), Pointer
</dt> </dl>

Child IO request packet.

</dd> <dt>

**ParentIrp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: WmiDataId(1), Pointer
</dt> </dl>

Parent IO request packet.

</dd> </dl>

## Remarks

Indicates that the volume manager split the IRP into two IRPs.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




