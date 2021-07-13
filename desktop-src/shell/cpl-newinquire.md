---
description: CPL_NEWINQUIRE message - Sent to the CPlApplet function of a Control Panel application to request information about a dialog box that the application supports.
title: CPL_NEWINQUIRE message (Cpl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: af52889c-7180-4690-8ed1-a0eb0a9dff35
api_name: 
 - CPL_NEWINQUIRE
api_type: 
 - HeaderDef
api_location: 
 - Cpl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# CPL\_NEWINQUIRE message

Sent to the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function of a Control Panel application to request information about a dialog box that the application supports.

## Parameters

<dl> <dt>

*uAppNum* 
</dt> <dd>

The dialog box number. This number must be in the range zero through one less than the value returned in response to the [**CPL\_GETCOUNT**](cpl-getcount.md) message (CPL\_GETCOUNT – 1).

</dd> <dt>

*lpncpli* 
</dt> <dd>

The address of a [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure. The Control Panel application should fill this structure with information about the dialog box.

</dd> </dl>

## Return value

If the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function processes this message successfully, it should return zero.

## Remarks

For better performance, most applications should ignore **CPL\_NEWINQUIRE** and process the [**CPL\_INQUIRE**](cpl-inquire.md) message instead.

The Control Panel sends the **CPL\_NEWINQUIRE** message once for each dialog box supported by your application. The Control Panel also sends a [**CPL\_INQUIRE**](cpl-inquire.md) message for each dialog box. These messages are sent immediately after the [**CPL\_GETCOUNT**](cpl-getcount.md) message. However, the system does not guarantee the order in which the **CPL\_INQUIRE** and **CPL\_NEWINQUIRE** messages are sent.

You can perform initialization for the dialog box when you receive [**CPL\_INQUIRE**](cpl-inquire.md). If you must allocate memory, do so in response to the [**CPL\_INIT**](cpl-init.md) message.

[**CPL\_INQUIRE**](cpl-inquire.md) is the preferred message. This is because **CPL\_NEWINQUIRE** returns information in a form that the system cannot cache. Consequently, applications that process **CPL\_NEWINQUIRE** must be loaded each time the Control Panel needs the information, resulting in a significant reduction in performance.

The only applications that should use **CPL\_NEWINQUIRE** are those that need to change their icon or display strings based on the state of the computer. In this case, your [**CPL\_INQUIRE**](cpl-inquire.md) handler should specify the CPL\_DYNAMIC\_RES value for the **idIcon**, **idName**, or **idInfo** members of the [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) structure, rather than specifying a valid resource identifier. This causes the Control Panel to send the **CPL\_NEWINQUIRE** message each time it needs the icon and display strings, allowing you to specify information based on the current state of the computer. Of course, this is significantly slower than using cached information.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Cpl.h</dt> </dl> |



 

 
