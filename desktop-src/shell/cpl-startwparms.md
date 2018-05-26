---
Description: Sent to notify CPlApplet that the user has chosen the icon associated with a given dialog box. CPlApplet should display the corresponding dialog box and carry out any user-specified tasks.
title: CPL\_STARTWPARMS message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPL\_STARTWPARMS message

Sent to notify [**CPlApplet**](/windows/win32/Cpl/nc-cpl-applet_proc?branch=master) that the user has chosen the icon associated with a given dialog box. **CPlApplet** should display the corresponding dialog box and carry out any user-specified tasks.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number. This number must be in the range zero through one less than the value returned in response to the [**CPL\_GETCOUNT**](cpl-getcount.md) message (CPL\_GETCOUNT – 1).

</dd> <dt>

*lpszExtra* 
</dt> <dd>

A string with additional directions for execution.

</dd> </dl>

## Return value

Returns **TRUE** if the message was handled, or **FALSE** otherwise.

## Remarks

**CPL\_STARTWPARMS** is similar to [**CPL\_DBLCLK**](cpl-dblclk.md) but allows you to pass a string to [**CPlApplet**](/windows/win32/Cpl/nc-cpl-applet_proc?branch=master) instead of an **int**. You can use this string as a flexible way to provide detailed directions for execution.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



 

 




