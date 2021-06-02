---
description: The TRIGGER structure indicates an action to be taken by the driver at a specified time.
ms.assetid: 63541796-b0d8-456c-8544-697fedbe05f7
title: TRIGGER structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRIGGER
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# TRIGGER structure

The **TRIGGER** structure indicates an action to be taken by the driver at a specified time.

## Syntax


```C++
typedef struct _TRIGGER {
  BOOL         TriggerActive;
  BYTE         TriggerType;
  BYTE         TriggerAction;
  DWORD        TriggerFlags;
  PATTERNMATCH TriggerPatternMatch;
  DWORD        TriggerBufferSize;
  DWORD        Reserved;
} TRIGGER, *LPTRIGGER;
```



## Members

<dl> <dt>

**TriggerActive**
</dt> <dd>

A Boolean value that determines if the trigger should be paid attention to by the driver.

</dd> <dt>

**TriggerType**
</dt> <dd>

The op code of the trigger.

</dd> <dt>

**TriggerAction**
</dt> <dd>

Action that the trigger is to take if it is fired.

</dd> <dt>

**TriggerFlags**
</dt> <dd>

Trigger flags.

</dd> <dt>

**TriggerPatternMatch**
</dt> <dd>

The trigger pattern match.

</dd> <dt>

**TriggerBufferSize**
</dt> <dd>

Trigger buffer size.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




