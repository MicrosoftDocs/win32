---
Description: Sent to the CPlApplet function of a Control Panel application when the user double-clicks the icon of a dialog box supported by the application.
title: CPL\_DBLCLK message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPL\_DBLCLK message

Sent to the [**CPlApplet**](/windows/win32/Cpl/nc-cpl-applet_proc?branch=master) function of a Control Panel application when the user double-clicks the icon of a dialog box supported by the application.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number. This number must be in the range zero through one less than the value returned in response to the [**CPL\_GETCOUNT**](cpl-getcount.md) message (CPL\_GETCOUNT – 1).

</dd> <dt>

*lData* 
</dt> <dd>

The value that the Control Panel application loaded into the **lpData** member of the [**CPLINFO**](/windows/win32/Cpl/ns-cpl-tagcplinfo?branch=master) or [**NEWCPLINFO**](/windows/win32/Cpl/ns-cpl-tagnewcplinfoa?branch=master) structure for the dialog box. The application loads the **lpData** member in response to the [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message.

</dd> </dl>

## Return value

If the [**CPlApplet**](/windows/win32/Cpl/nc-cpl-applet_proc?branch=master) function processes this message successfully, the return value is zero; otherwise, it is nonzero.

## Remarks

In response to this message, a Control Panel application must display the corresponding dialog box.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



## See also

<dl> <dt>

[**CPL\_SELECT**](cpl-select.md)
</dt> </dl>

 

 




