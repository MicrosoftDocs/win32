---
Description: Sent to the CPlApplet function of a Control Panel application when the controlling application of the Control Panel closes. The controlling application sends the message once for each dialog box that the application supports.
title: CPL_STOP message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CPL\_STOP message

Sent to the [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) function of a Control Panel application when the controlling application of the Control Panel closes. The controlling application sends the message once for each dialog box that the application supports.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number.

</dd> <dt>

*lData* 
</dt> <dd>

The value that the Control Panel application loaded into the **lpData** member of the [**CPLINFO**](/windows/desktop/api/Cpl/ns-cpl-tagcplinfo) or [**NEWCPLINFO**](/windows/desktop/api/Cpl/ns-cpl-tagnewcplinfoa) structure for the dialog box. The application loads the **lpData** member in response to the [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message.

</dd> </dl>

## Return value

If the [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) function processes this message successfully, it should return zero.

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

 

 




