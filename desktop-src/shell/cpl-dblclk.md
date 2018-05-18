---
Description: 'Sent to the CPlApplet function of a Control Panel application when the user double-clicks the icon of a dialog box supported by the application.'
title: 'CPL\_DBLCLK message'
---

# CPL\_DBLCLK message

Sent to the [**CPlApplet**](cplapplet.md) function of a Control Panel application when the user double-clicks the icon of a dialog box supported by the application.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number. This number must be in the range zero through one less than the value returned in response to the [**CPL\_GETCOUNT**](cpl-getcount.md) message (CPL\_GETCOUNT – 1).

</dd> <dt>

*lData* 
</dt> <dd>

The value that the Control Panel application loaded into the **lpData** member of the [**CPLINFO**](cplinfo.md) or [**NEWCPLINFO**](newcplinfo.md) structure for the dialog box. The application loads the **lpData** member in response to the [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message.

</dd> </dl>

## Return value

If the [**CPlApplet**](cplapplet.md) function processes this message successfully, the return value is zero; otherwise, it is nonzero.

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

 

 




