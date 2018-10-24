---
Description: Sent to the CPlApplet function of a Control Panel application to retrieve the number of dialog boxes supported by the application.
title: CPL_GETCOUNT message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CPL\_GETCOUNT message

Sent to the [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) function of a Control Panel application to retrieve the number of dialog boxes supported by the application.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) function returns the number of dialog boxes that the Control Panel application supports.

## Remarks

This message is sent immediately after the [**CPL\_INIT**](cpl-init.md) message.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



 

 




