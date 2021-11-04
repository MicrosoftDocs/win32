---
description: Sent to a File Manager extension DLL procedure when File Manager wants a Help string for a menu or toolbar command item.
title: FMEVENT_HELPSTRING message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMEVENT_HELPSTRING
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 55fb5bfe-2889-40e5-9798-85f63727e31f

---

# FMEVENT\_HELPSTRING message

Sent to a File Manager extension DLL procedure when File Manager wants a Help string for a menu or toolbar command item.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lpfmshs* 
</dt> <dd>

The address of an [**FMS\_HELPSTRING**](fms-helpstring.md) structure that communicates command item Help string data. The **FMS\_HELPSTRING** structure identifies the command item for which a Help string is wanted, along with a handle to its menu. An application then writes the appropriate Help string to the **FMS\_HELPSTRING** structure's **szHelp** member.

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

[**FMEVENT\_HELPMENUITEM**](fmevent-helpmenuitem.md)
</dt> </dl>

 

 




