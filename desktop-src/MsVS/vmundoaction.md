---
title: VMUndoAction enumeration
description: The VMUndoAction enumeration specifies what happens to undo drives when a virtual machine is shut down or turned off.
ms.assetid: '49885878-cd90-4ecd-863d-0dd33fa6fc98'
keywords: ["VMUndoAction enumeration Virtual Server"]
topic_type:
- apiref
api_name:
- VMUndoAction
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMUndoAction enumeration

The **VMUndoAction** enumeration specifies what happens to undo drives when a virtual machine is shut down or turned off.

## Syntax


```C++
typedef enum  { 
  vmUndoAction_Discard  = 0,
  vmUndoAction_Keep     = 1,
  vmUndoAction_Commit   = 2
} VMUndoAction;
```



## Constants

<dl> <dt>

<span id="vmUndoAction_Discard"></span><span id="vmundoaction_discard"></span><span id="VMUNDOACTION_DISCARD"></span>**vmUndoAction\_Discard**
</dt> <dd>

Discard undo drives. Parent drives remain unchanged.

</dd> <dt>

<span id="vmUndoAction_Keep"></span><span id="vmundoaction_keep"></span><span id="VMUNDOACTION_KEEP"></span>**vmUndoAction\_Keep**
</dt> <dd>

Keep undo drives. Parent drives remain unchanged, but changes will be maintained the next time the virtual machine starts.

</dd> <dt>

<span id="vmUndoAction_Commit"></span><span id="vmundoaction_commit"></span><span id="VMUNDOACTION_COMMIT"></span>**vmUndoAction\_Commit**
</dt> <dd>

Commit changes to parent drives.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





