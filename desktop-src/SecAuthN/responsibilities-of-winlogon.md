---
description: Lists and explains the responsibilities of Winlogon.
ms.assetid: 5aef4164-11bd-4acc-b851-de982e35d2b5
title: Responsibilities of Winlogon
ms.topic: article
ms.date: 05/31/2018
---

# Responsibilities of Winlogon

[*Winlogon*](../secgloss/w-gly.md) has the following responsibilities:

-   Window station and desktop protection

    Winlogon sets the protection of the window station and corresponding desktops to ensure that each is properly accessible. In general, this means that the local system will have full access to these objects and that an interactively logged-on user will have read access to the window station object and full access to the application desktop object.

-   Standard SAS recognition

    Winlogon has special hooks into the User32 server that allow it to monitor CTRL+ALT+DEL [*secure attention sequence*](../secgloss/s-gly.md) (SAS) events. Winlogon makes this SAS event information available to GINAs to use as their SAS, or as part of their SAS. In general, GINAs should monitor SASs on their own; however, any [*GINA*](../secgloss/g-gly.md) that has the standard CTRL+ALT+DEL SAS as one of the SASs it recognizes should use the Winlogon support provided for this purpose.

-   SAS routine dispatching

    When Winlogon encounters a SAS event or when a SAS is delivered to Winlogon by the GINA, Winlogon sets the state accordingly, changes to the Winlogon desktop, and calls one of the SAS processing functions of the GINA.

-   User profile loading

    When users log on, their user profiles are loaded into the registry. In this way, the processes of the user can use the special registry key HKEY\_CURRENT\_USER. Winlogon does this automatically after a successful logon but before activation of the shell for the newly logged-on user.

-   Assignment of security to user shell

    When a user logs on, the GINA is responsible for creating one or more initial processes for that user. Winlogon provides a support function for the GINA to apply the security of the newly logged-on user to these processes. However, the preferred way to do this is for the GINA to call the Windows function [**CreateProcessAsUser**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasusera), and let the system provide the service.

-   Screen saver control

    Winlogon monitors keyboard and mouse activity to determine when to activate screen savers. After the screen saver is activated, Winlogon continues to monitor keyboard and mouse activity to determine when to terminate the screen saver. If the screen saver is marked as secure, Winlogon treats the workstation as locked. When there is mouse or keyboard activity, Winlogon invokes the [**WlxDisplayLockedNotice**](/windows/desktop/api/Winwlx/nf-winwlx-wlxdisplaylockednotice) function of the GINA and locked workstation behavior resumes. If the screen saver is not secure, any keyboard or mouse activity terminates the screen saver without notification to the GINA.

-   Multiple network provider support

    Multiple networks installed on a Windows system can be included in the authentication process and in password-updating operations. This inclusion lets additional networks gather identification and authentication information all at once during normal logon, using the secure desktop of Winlogon. Some of the parameters required in the Winlogon services available to GINAs explicitly support these additional network providers.

 

 
