---
description: Occurs when the cursor moves over the tablet digitizer.
ms.assetid: cd2863af-59a9-4dd0-a679-84861a70ef53
title: ITabletEventSink::CursorMove method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink.CursorMove
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink::CursorMove method

Occurs when the cursor moves over the tablet digitizer.

## Syntax


```C++
HRESULT CursorMove(
   TABLET_CONTEXT_ID tcid,
   CURSOR_ID         cid,
   HWND              hWnd,
   LONG              xPos,
   LONG              yPos
);
```



## Parameters

<dl> <dt>

*tcid* 
</dt> <dd>

Unique dentifier of the tablet digitizer.

</dd> <dt>

*cid* 
</dt> <dd>

Unique identifier of the tablet stylus.

</dd> <dt>

*hWnd* 
</dt> <dd>

The window over which the cursor moved.

</dd> <dt>

*xPos* 
</dt> <dd>

The X position of the stylus.

</dd> <dt>

*yPos* 
</dt> <dd>

The Y position of the stylus.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

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

 

 




