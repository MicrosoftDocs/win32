---
title: Security Considerations for Assistive Technologies
description: Assistive technologies are applications that run on the Windows desktop and help accessibility users to interact with the operating system and other applications running on the computer, including applications in the new Windows UI.
ms.assetid: 0c3689e1-2124-4142-b0bd-233e95ee1285
f1_keywords:
- "vs.debug.error.launch_elevation_requirements"
keywords:
- uiAccess attribute
- UI Automation,uiAccess attribute
- security,uiAccess attribute
- requestedExecutionLevel tag
- UI Automation,requestedExecutionLevel tag
- UI Automation,security considerations
- UI Automation,manifest files
- manifest files
- user account control
- security,user account control
- security,manifest files
- security,requestedExecutionLevel tag
ms.topic: article
ms.date: 05/31/2018
---

# Security Considerations for Assistive Technologies

Assistive technologies are applications that run on the Windows desktop and help accessibility users interact with the operating system and other applications running on the computer, including applications in the new Windows UI. Assistive technology applications work by retrieving information from the operating system and other applications, and then presenting the information in a way that is accessible to the user. An assistive technology application can also programmatically "drive" the operating system and other applications based on input from the user.

The nature of assistive technology applications requires that they cross process boundaries, and that they have access to processes that run at a higher integrity level (IL) than themselves. (An assistive technology application runs at medium IL.) For example, when the user attempts to perform a task that requires administrative privileges, Windows presents a dialog box asking the user for consent to continue. This dialog box runs at a higher IL to protect it from cross-process communication, so that malicious software cannot simulate user input. Similarly, the desktop logon screen runs at a higher IL to prevent it from being accessed by other processes.

Assistive technology applications typically need access to the protected system UI elements, or to other processes that might be running at a higher privilege level. Therefore, assistive technology applications must be trusted by the system, and must run with special privileges.

To get access to higher IL processes, an assistive technology application must set the UIAccess flag in the application's manifest and be launched by a user with administrator privileges.

> [!NOTE]
> Access privileges are constrained as follows:
>
> - An application that doesn't have UIAccess in the manifest starts with medium IL and cannot access elevated ("medium+" IL) process UI.
> - An application that has UIAccess in the manifest and is launched by a user who is not in the administrators group, starts as "medium+" IL and cannot access elevated UI (nothing running as "high" IL, such as apps launched through a **Right click -> Run as administrator**).
> - An application has UI Access and is launched by an admin user starts as "high" IL and can access elevated UI because it has the same IL.
>
> UIAccess is not enough for a process to move up through the IL boundary.

In addition to having access to higher IL processes, an assistive technology application with these privileges can run as the topmost application in the z-order at any time, meaning that an assistive technology application can be visible and available whenever the user needs it.

> [!Important]
> None of the previously listed scenarios provide access to UI running under the system IL. This is only possible if the process is launched in the user account control (UAC) desktop under SYSTEM (and system IL). In this case, setting UIAccess has no effect.

## UIAccess Requirements for Assistive Technology Applications

An assistive technology application is a Windows Windows desktop application that interacts with other processes running on the desktop and in the new Windows UI to get information from the system and applications. The assistive technology application can then provide the information to accessibility users.

An assistive technology application gets access to other processes by setting the UIAccess flag in the application manifest. To use the UIAccess flag, an assistive technology application must meet the following requirements.

-   Require to display, interact with, or reflect information from another application to provide information for an accessibility scenario, and/or
-   Require running as the top-most window to obtain or display this information.

To use UIAccess, an assistive technology application needs to:

-   Be signed with a certificate to interact with applications running at a higher privilege level.
-   Be trusted by the system. The application must be installed in a secure location that requires a user account control (UAC) prompt for access. For example, the Program Files folder.
-   Be built with a manifest file that includes the uiAccess flag.

UIAccess should not be used:

-   By applications that are not assistive technologies.
-   By assistive technology applications that display information or UI that is not relevant to the accessibility scenario they target.
-   By applications that just want to appear above other applications in the new Windows UI.
    > [!Note]  
    > Applications developed for the new Windows UI do not have UIAccess as an available option.

     

## Setting UIAccess in the Application Manifest File

To gain access to the protected system UI, applications must be built with a manifest file that includes a special attribute in the manifest file. This **uiAccess** attribute is included in the **requestedExecutionLevel** tag, as shown in the following code example.


```XML
<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3"> 
    <security> 
        <requestedPrivileges> 
        <requestedExecutionLevel 
            level="highestAvailable" 
            uiAccess="true" /> 
        </requestedPrivileges> 
    </security> 
</trustInfo> 
```



The value of the **level** attribute in this code is an example only.

**UIAccess** is "false" by default. If the attribute is omitted, or if there is no manifest, the application cannot gain access to the protected UI.

For more information on Windows security, on signing applications, and on creating manifests, see [The Windows Vista and Windows Server 2008 Developer Story: Windows Vista Application Development Requirements for User Account Control (UAC)](/previous-versions/aa905330(v=msdn.10)) on MSDN.

## Related topics

<dl> <dt>

[UI Automation Fundamentals](entry-uiautocore-overview.md)
</dt> </dl>

 

 