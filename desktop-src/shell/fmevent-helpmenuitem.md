---
description: Sent to a File Manager extension DLL procedure when the user presses F1 on a menu or toolbar command item. The extension should call WinHelp, with that function's hwnd parameter set to the value of the extension's hwnd parameter.
title: FMEVENT_HELPMENUITEM message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMEVENT_HELPMENUITEM
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 6298061d-7e24-45ab-8bc4-96b28e071080

---

# FMEVENT\_HELPMENUITEM message

Sent to a File Manager extension DLL procedure when the user presses F1 on a menu or toolbar command item. The extension should call [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa), with that function's *hwnd* parameter set to the value of the extension's *hwnd* parameter.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*uItem* 
</dt> <dd>

A value that identifies the menu or toolbar command item for which Help is desired. The extension procedure uses this value to determine how best to call [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa).

</dd> </dl>

## Return value

An extension DLL procedure should return zero if it processes this message.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> <dt>

[**FMEVENT\_HELPSTRING**](fmevent-helpstring.md)
</dt> </dl>

 

 




