---
description: Prior to Windows Vista, you created a Control Panel item by creating a .dll file and naming it with a .cpl extension.
ms.assetid: 258dae28-c054-4392-b0e9-99493f23c814
title: Using CPLApplet
ms.topic: article
ms.date: 05/31/2018
---

# Using CPLApplet

Prior to Windows Vista, you created a Control Panel item by creating a .dll file and naming it with a .cpl extension. This file exported the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function. This scheme is still supported in Windows Vista and later versions and is discussed in this topic. However, the guidelines for new Control Panel items recommend a simpler approach with the Control Panel item built as a .exe file that uses a task flow layout.

When Control Panel loads a .dll (or .cpl) file, it calls the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function to get information such as the number of Control Panel items the file hosts, as well as information about each item. Control Panel also calls the function when the item's window is initialized, opened, or closed.

When Windows first loads the Control Panel item, it retrieves the address of the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function and subsequently uses that address to call the function and pass it messages. It might send the following messages.



| Message                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CPL\_DBLCLK**](cpl-dblclk.md)           | Sent to notify [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) that the user has chosen the icon associated with a given Control Panel item. **CPlApplet** should display the dialog box for the specified item and carry out any user-specified tasks. The **CPlApplet** *lParam1* parameter is an integer that represents the zero-based index of the Control Panel item. The *lParam2* parameter is the **lpData** pointer returned in the [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) or [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure in the [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message. The return value is ignored.                                                                |
| [**CPL\_EXIT**](cpl-exit.md)               | Sent after the last CPL\_STOP message and immediately before Windows uses the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function to free the DLL that contains the Control Panel item. [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) should free any remaining memory and prepare to close. The return value is ignored.                                                                                                                                                                                                                                                                                                                                                                                                |
| [**CPL\_GETCOUNT**](cpl-getcount.md)       | Sent after the CPL\_INIT message to prompt [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) to return a number that indicates how many subprograms it supports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**CPL\_INIT**](cpl-init.md)               | Sent immediately after the DLL that contains the Control Panel item is loaded. The message prompts [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) to perform initialization procedures, including memory allocation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**CPL\_INQUIRE**](cpl-inquire.md)         | Sent after the CPL\_GETCOUNT message to prompt [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) to provide information about a specified subprogram. The *lParam1* value is an integer that represents the zero-based index of the subprogram about which information is being requested. The *lParam2* parameter of **CPlApplet** points to a [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) structure. The return value is ignored.                                                                                                                                                                                                                                                                                                    |
| [**CPL\_NEWINQUIRE**](cpl-newinquire.md)   | Sent after the CPL\_GETCOUNT message to prompt [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) to provide information about a specified Control Panel item. The *lParam1* value is an integer that represents the zero-based index of the subprogram about which information is being requested. The *lParam2* parameter is a pointer to a [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure. CPL\_NEWINQUIRE normally should be ignored. Your application should process only CPL\_INQUIRE on Windows 95, Microsoft Windows NT 4.0, and later systems since Control Panel performance suffers when CPL\_NEWINQUIRE is used. This is because the returned strings and icons cannot be cached. The return value is ignored. |
| [**CPL\_SELECT**](cpl-select.md)           | Obsolete. Current versions of Windows do not send this message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**CPL\_STARTWPARMS**](cpl-startwparms.md) | Sent to notify [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) that the user has chosen the icon associated with a given dialog box. **CPlApplet** should display the corresponding dialog box and carry out any user-specified tasks. This message is similar to CPL\_DBLCLK, but there might be some additional information. The *lParam1* parameter is the Control Panel item number and *lParam2* is an **LPCTSTR** to any extra directions that might be necessary. Return **TRUE** if this message is handled; otherwise, **FALSE**. This message is valid for [version 5.00](versions.md) and later of Shell32.dll.                                                                                         |
| [**CPL\_STOP**](cpl-stop.md)               | Sent once for each Control Panel item in the .cpl file before Windows unloads the Control Panel extension. [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) should free any memory associated with the item number provided in *lParam1*. The *lParam2* parameter is **lpData** pointer returned in the [**CPLINFO**](/windows/win32/api/cpl/ns-cpl-cplinfo) or [**NEWCPLINFO**](/windows/win32/api/cpl/ns-cpl-newcplinfoa) structure in the [**CPL\_INQUIRE**](cpl-inquire.md) or [**CPL\_NEWINQUIRE**](cpl-newinquire.md) message. The return value is ignored.                                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[User Experience Guidelines](user-experience-guidelines.md)
</dt> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[Control Panel Message Processing](message-processing.md)
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

 

 
