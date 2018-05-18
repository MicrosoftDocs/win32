---
Description: 'Sent to the CPlApplet function of a Control Panel application when the controlling application of the Control Panel closes. The controlling application sends the message once for each dialog box that the application supports.'
title: 'CPL\_STOP message'
---

# CPL\_STOP message

Sent to the [**CPlApplet**](cplapplet.md) function of a Control Panel application when the controlling application of the Control Panel closes. The controlling application sends the message once for each dialog box that the application supports.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number.

</dd> <dt>

*lData* 
</dt> <dd>

The value that the Control Panel application loaded into the **lpData** member of the [**CPLINFO**](cplinfo.md) or [**NEWCPLINFO**](newcplinfo.md) structure for the dialog box. The application loads the **lpData** member in response to the [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message.

</dd> </dl>

## Return value

If the [**CPlApplet**](cplapplet.md) function processes this message successfully, it should return zero.

## Remarks

In response to this message, a Control Panel application must perform cleanup for the given dialog box.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



## See also

<dl> <dt>

[**CPL\_EXIT**](cpl-exit.md)
</dt> <dt>

[**CPL\_GETCOUNT**](cpl-getcount.md)
</dt> </dl>

 

 




