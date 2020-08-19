---
title: Window Station and Desktop Creation
description: The system automatically creates the interactive window station.
ms.assetid: 5b908cb6-3a72-4afc-aed0-8411e8d0888f
ms.topic: article
ms.date: 05/31/2018
---

# Window Station and Desktop Creation

The system automatically creates the interactive window station. When an interactive user logs on, the system associates the interactive window station with the user logon session. The system also creates the default input desktop for the interactive window station (Winsta0\\default). Processes started by the logged-on user are associated with the Winsta0\\default desktop.

A process can use the [**CreateWindowStation**](/windows/win32/api/winuser/nf-winuser-createwindowstationa) function to create a new window station, and the **CreateDesktop** or [**CreateDesktopEx**](/windows/win32/api/winuser/nf-winuser-createdesktopexa) function to create a new desktop. The number of desktops that can be created is limited by the size of the system desktop heap. For more information, see [**CreateDesktop**](/windows/win32/api/winuser/nf-winuser-createdesktopa).

When a noninteractive process such as a service application attempts to connect to a window station and no window station exists for the process logon session, the system attempts to create a window station and desktop for the session. The name of the created window station is based on the logon session identifier, and the desktop is named default, as described here:

-   If a service is running in the security context of the LocalSystem account but does not include the SERVICE\_INTERACTIVE\_PROCESS attribute, it uses the following window station and desktop: Service-0x0-3e7$\\default. This window station is not interactive, so the service cannot display a user interface. In addition, processes created by the service cannot display a user interface.
-   If the service is running in the security context of a user account, the name of the window station is based on the user SID Service-0x*Z1*-*Z2*$, where *Z1* is the high part of the logon SID and *Z2* is the low part of the logon SID. Because a SID is unique to the logon session, two services running in the same security context receive unique window stations. These window stations are not interactive.

The discretionary access control list (DACL) for the window station and desktop includes the following access rights for the service's user account:

Window Station:

<dl> WINSTA\_ACCESSCLIPBOARD  
WINSTA\_ACCESSGLOBALATOMS  
WINSTA\_CREATEDESKTOP  
WINSTA\_EXITWINDOWS  
WINSTA\_READATTRIBUTES  
STANDARD\_RIGHTS\_REQUIRED  
</dl>

Desktop:

<dl> DESKTOP\_CREATEMENU  
DESKTOP\_CREATEWINDOW  
DESKTOP\_ENUMERATE  
DESKTOP\_HOOKCONTROL  
DESKTOP\_READOBJECTS  
DESKTOP\_WRITEOBJECTS  
STANDARD\_RIGHTS\_REQUIRED  
</dl>

 

 