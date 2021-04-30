---
description: Occurs when a system event is available.
ms.assetid: 3d9e98f0-b11e-4a65-a544-9e1998a80d5f
title: ITabletEventSink::SystemEvent method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink.SystemEvent
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink::SystemEvent method

Occurs when a system event is available.

## Syntax


```C++
HRESULT SystemEvent(
  [in] TABLET_CONTEXT_ID tcid,
  [in] CURSOR_ID         cid,
  [in] SYSTEM_EVENT      event,
  [in] SYSTEM_EVENT_DATA eventdata
);
```



## Parameters

<dl> <dt>

*tcid* \[in\]
</dt> <dd>

The identifier of the tablet.

</dd> <dt>

*cid* \[in\]
</dt> <dd>

The identifier of the stylus.

</dd> <dt>

*event* \[in\]
</dt> <dd>

The system event code.

</dd> <dt>

*eventdata* \[in\]
</dt> <dd>

The system event data.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

The following list contains the valid values for the event parameter.

-   SE\_TAP
-   SE\_DBL\_TAP
-   SE\_RIGHT\_TAP
-   SE\_DRAG
-   SE\_RIGHT\_DRAG
-   SE\_HOLD\_ENTER
-   SE\_HOLD\_LEAVE
-   SE\_HOVER\_ENTER
-   SE\_HOVER\_LEAVE
-   SE\_MIDDLE\_CLICK
-   SE\_KEY
-   SE\_MODIFIER\_KEY
-   SE\_GESTURE\_MODE
-   SE\_CURSOR

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletEventSink Interface**](itableteventsink.md)
</dt> </dl>

 

 




