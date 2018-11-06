---
title: Accessing the Control from Visual Basic and Other Programming Languages
description: Accessing the Control from Visual Basic and Other Programming Languages
ms.assetid: 869b8eb1-1f40-4d87-8501-e41d6c0a3a97
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the Control from Visual Basic and Other Programming Languages

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

You can also use Microsoft Agent's control from Visual Basic and other programming languages. Make sure that the language fully supports the ActiveX control interface, and follow its conventions for adding and accessing ActiveX controls. To access the control, Agent must already be installed on the target system.

You can then download Agent's self-installing cabinet file from the website (using the Save rather than Run option). You can include this file in your installation setup program. Whenever it is executed, it will automatically install Agent on the target system. For further details on installation, see the Microsoft Agent distribution license agreement. Installation other than using Agent's self-installing cabinet file, such as attempting to copy and register Agent component files, is not supported. This ensures consistent and complete installation. Note that the Microsoft Agent self-installing file will not install on Microsoft Windows 2000 because that version of the operating system already includes its own version of Agent.

To successfully install Agent on a target system, you must also ensure that the target system has a recent version of the Microsoft Visual C++ runtime (Msvcrt.dll), Microsoft registration tool (Regsvr32.dll), and Microsoft COM dlls. The easiest way to ensure that the necessary components are on the target system is to require that Microsoft Internet Explorer 3.02 or later is installed. Alternatively, you can install the first two components which are available as part of Microsoft Visual C++. The necessary COM dlls can be installed as part of the Microsoft DCOM update, available at the Microsoft website. You can find further information and licensing information for these components at the Microsoft website.

Agent's language components can be installed the same way. Similarly, you can use this technique to install the ACS format of the Microsoft characters available for distribution from the Microsoft Agent website. The character files automatically install to the Microsoft Agent \\Chars subdirectory.

Because Microsoft Agent's components are designed as operating system components, Agent may not be uninstalled. Similarly, where Agent is already installed as part of the Windows operating system, the Agent self-installing cabinet may not install.

 

 




