---
description: The CPlApplet callback function processes all messages sent to a Control Panel item by Windows. Messages sent to the function are in a specific order. By the same token, the .cpl item requires the messages to be processed in a specific way.
ms.assetid: 70302698-f9d5-4de4-a662-4815002eea52
title: Control Panel Message Processing
ms.topic: article
ms.date: 05/31/2018
---

# Control Panel Message Processing

The [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) callback function processes all messages sent to a Control Panel item by Windows. Messages sent to the function are in a specific order. By the same token, the .cpl item requires the messages to be processed in a specific way.

First, the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function receives the CPL\_INIT message when Windows first loads the Control Panel item. The function should carry out any initialization, such as allocating memory, and return nonzero. If **CPlApplet** cannot complete the initialization, it must return zero, directing Windows to terminate communication and release the DLL.

Next, if the CPL\_INIT message succeeded, Windows sends the CPL\_GETCOUNT message. The function must then return the number of Control Panel items supported by the .dll file.

The [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function then receives one CPL\_INQUIRE message and one CPL\_NEWINQUIRE message for each Control Panel item supported by the .dll file. The function fills in a [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) or [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure with information about your item, such as its name, icon, and a descriptive string. Most applications should process the CPL\_INQUIRE message and ignore the CPL\_NEWINQUIRE message. The CPL\_INQUIRE message provides information in a form that Windows can cache, which results in much better performance. The CPL\_NEWINQUIRE message is used only if you need to change your item's icon or display strings based on the state of the computer. Control Panel items that use CPL\_NEWINQUIRE cannot be found by a **Start** menu search in Windows Vista because it relies on caching.

The [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function next receives a CPL\_DBLCLK message as a notification that the user has chosen the icon that represents the Control Panel item. The function might receive this message any number of times. The message includes the item identifier and the **lpData** pointer returned in the [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) or [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure in the call to [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md). The function should display the corresponding dialog box and process subsequent user input.

Besides CPL\_DBLCLK, the CPL\_STARTWPARMS message can be sent if a Control Panel item is invoked with input parameters, such as from a command prompt or from another program. The message includes the item identifier along with the additional parameter string.

Before the controlling application terminates, [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) receives the CPL\_STOP message once for each Control Panel item supported by the .dll file. The message includes the identifier for the Control Panel item and the **lpData** pointer returned in the [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) or [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure in the call to [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md). The function should free any memory that it allocated for the specified dialog box.

After the last CPL\_STOP message, [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) receives a CPL\_EXIT message. The function should free all remaining allocated memory and unregister any private window classes that it might have registered. Immediately after the function returns from this message, Windows releases the Control Panel item by calling the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function.

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[User Experience Guidelines](user-experience-guidelines.md)
</dt> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[Using CPLApplet](using-cplapplet.md)
</dt> <dt>

[Executing Control Panel Items](executing-control-panel-items.md)
</dt> <dt>

[Extending System Control Panel Items](extending-system-control-panel-items.md)
</dt> <dt>

[Assigning Control Panel Categories](assigning-control-panel-categories.md)
</dt> <dt>

[Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md)
</dt> <dt>

[Accessing the Control Panel in Safe Mode under Windows Vista](accessing-the-cp-in-safe-mode-under-vista.md)
</dt> </dl>

 

 
