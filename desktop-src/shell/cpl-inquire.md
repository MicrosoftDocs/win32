---
Description: Sent to the CPlApplet function of a Control Panel application to request information about a dialog box that the application supports.
title: CPL_INQUIRE message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CPL\_INQUIRE message

Sent to the [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) function of a Control Panel application to request information about a dialog box that the application supports.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number. This number must be in the range zero through one less than the value returned in response to the [**CPL\_GETCOUNT**](cpl-getcount.md) message (CPL\_GETCOUNT – 1).

</dd> <dt>

*lpcpli* 
</dt> <dd>

The address of a [**CPLINFO**](/windows/desktop/api/Cpl/ns-cpl-tagcplinfo) structure. The application must fill this structure with resource identifiers for the icon, short name, description, and any user-defined value associated with the dialog box.

</dd> </dl>

## Return value

If the [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) function processes this message successfully, it should return zero.

## Remarks

The Control Panel sends the **CPL\_INQUIRE** message once for each dialog box supported by your application. The Control Panel also sends a [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message for each dialog box. These messages are sent immediately after the [**CPL\_GETCOUNT**](cpl-getcount.md) message. However, the system does not guarantee the order in which the **CPL\_INQUIRE** and **CPL\_NEWINQUIRE** messages are sent.

You can perform initialization for the dialog box when you receive **CPL\_INQUIRE**. If you must allocate memory, do so in response to the [**CPL\_INIT**](cpl-init.md) message.

The [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message returns information in a form that the system cannot cache. For this reason, most [**CPlApplet**](https://msdn.microsoft.com/en-us/library/Bb776392(v=VS.85).aspx) functions should process **CPL\_INQUIRE** and ignore **CPL\_NEWINQUIRE**.

The only applications that should use [**CPL\_NEWINQUIRE**](cpl-newinquire.md) are those that need to change their icon or display strings based on the state of the computer. In this case, your **CPL\_INQUIRE** handler should specify the CPL\_DYNAMIC\_RES value for the **idIcon**, **idName**, or **idInfo** members of the [**CPLINFO**](/windows/desktop/api/Cpl/ns-cpl-tagcplinfo) structure, rather than specifying a valid resource identifier. This causes the Control Panel to send the **CPL\_NEWINQUIRE** message each time it needs the icon and display strings, allowing you to specify information based on the current state of the computer. This is significantly slower than using cached information.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



 

 




