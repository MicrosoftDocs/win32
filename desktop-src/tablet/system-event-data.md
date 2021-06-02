---
description: Contains information about a tablet system event.
ms.assetid: 725f4b43-0bcb-4452-a87f-b24a85de0049
title: SYSTEM_EVENT_DATA structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SYSTEM_EVENT_DATA
api_type: 
- NA
api_location: 
---

# SYSTEM\_EVENT\_DATA structure

Contains information about a tablet system event.

## Syntax


```C++
typedef struct tagSYSTEM_EVENT_DATA {
  BYTE  bModifier;
  WCHAR wKey;
  LONG  xPos;
  LONG  yPos;
  BYTE  bCursorMode;
  DWORD dwButtonState;
} SYSTEM_EVENT_DATA;
```



## Members

<dl> <dt>

**bModifier**
</dt> <dd>

Bit values for the modifiers. See the remarks section for more information.

</dd> <dt>

**wKey**
</dt> <dd>

Scan code for the keyboard character.

</dd> <dt>

**xPos**
</dt> <dd>

X position of the event.

</dd> <dt>

**yPos**
</dt> <dd>

Y position of the event.

</dd> <dt>

**bCursorMode**
</dt> <dd>

The type of cursor that caused the event. See the remarks section for more information.

</dd> <dt>

**dwButtonState**
</dt> <dd>

State of the buttons at the time of the system event.

</dd> </dl>

## Remarks

The following system events are defined for use in the **bModifier** member.



| Value               | Description                  |
|---------------------|------------------------------|
| SE\_MODIFIER\_CTRL  | The Control key was pressed. |
| SE\_MODIFIER\_ALT   | The Alt key was pressed.     |
| SE\_MODIFIER\_SHIFT | The Shift key was pressed.   |



 

The following system events are defined for use in the **bCursorMode** member.



| Value              | Description               |
|--------------------|---------------------------|
| SE\_NORMAL\_CURSOR | Indicates the pen tip.    |
| SE\_ERASER\_CURSOR | Indicates the pen eraser. |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                                     |



## See also

<dl> <dt>

[**IStylusPlugin::SystemEvent Method**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-systemevent)
</dt> <dt>

[**ITabletEventSink::SystemEvent Method**](itableteventsink-systemevent.md)
</dt> </dl>

 

 




