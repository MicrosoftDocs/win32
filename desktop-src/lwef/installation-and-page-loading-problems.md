---
title: Installation and Page Loading Problems
description: Installation and Page Loading Problems
ms.assetid: 1611c3f1-0411-4631-a64c-e7637fc7edd9
ms.topic: article
ms.date: 05/31/2018
---

# Installation and Page Loading Problems

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

### When I attempt to install Microsoft Agent on Microsoft Windows NT, I get a message indicating that I need to be an administrator.

Because Microsoft Agent writes files to your system directory when it installs, you must have administrator (not user) privileges to install.

### When I attempt to install Microsoft Agent, I get one of the following errors: Process (Regsvr32 /s windows\\msagent\\AgentCtl.dll). Error while creating this file. Cannot find this file. (Note: The directory location cited in the error message varies depending on how you installed Windows.) A required DLL MSVCRT.DLL was not found. Error creating process <c:\\windows\\msagent\\agentsvr.exe /regserver>. Reason: One of the library files needed to run this application cannot be found. (Note: The directory location cited in the error message varies depending on how you installed Windows.)

Installation of Microsoft Agent requires the proper installation of Regsvr32.exe, Msvcrt.dll (the Microsoft C run-time library), and up-to-date OLE dlls. See DCOM update: (<https://docs.microsoft.com/openspecs/windows_protocols/ms-dcom/4a893f3d-bd29-48cd-9f43-d9777a4415b0>). The best way to ensure that all the correct system files are present is to install [Microsoft Internet Explorer 4.0](https://www.microsoft.com/ie/download) or later.

### When I attempt to load a page scripted for Microsoft Agent, I get a scripting error: "VBScript Runtime Error, Object required."

One of the following conditions may cause the message to display:

-   Your security options for Microsoft Internet Explorer must be set to enable ActiveX controls and plug-ins. Check your browser's security page. In Microsoft Internet Explorer, open the View menu, choose Options, click the Security tab, and make sure the Enable ActiveX Controls And Plug-Ins check box is checked.
-   You are running on a dual-boot Windows 9x or Windows NT system and you have installed Microsoft Agent on one operating system but are trying to access the page from the other operating system. Although the operating systems may share directories and files, the registry information used by Microsoft Agent is not shared, so you must install Microsoft Agent on the operating system you use to access webpages scripted with the character.

### When I attempt to load a page scripted for Microsoft Agent, nothing happens.

This can occur if one of the following conditions exists:

-   Check your browser's security options. Your browser must be set to enable the loading of ActiveX scripts and playing of ActiveX controls.
-   If you are accessing pages scripted with Microsoft Agent and using Microsoft Internet Explorer, you must have version 3.02 or later (download the latest version of Internet Explorer at [https://www.microsoft.com/windows/ie/](https://www.microsoft.com/windows/internet-explorer/default.aspx)<https://www.microsoft.com/windows/ie/>). In Microsoft Internet Explorer, open the View menu, choose Options, click the Security tab, and select all the Active Content check boxes.
-   A Java applet on the page can also cause this error. To run Microsoft Agent on the same page as a Java applet requires version 2.0 of the Microsoft Virtual Machine (VM). For more information, see the [Programming/Scripting FAQ](programming-scripting-faq.yml).

### When I attempt to load a page scripted for Microsoft Agent, I get the message, "Unable to initialize Microsoft Agent."

This usually occurs when you don't have Microsoft Agent or some other control that page uses installed, and choose No when you are prompted to install the control. Try refreshing the page, though the page may work only if you install all the components it requires.

### When I attempt to load a page scripted for Microsoft Agent, I get the message, "The component has been digitally "signed" by its publisher, but the signature does not match the component. It is possible that this component has been damaged or tampered with? Do you want to continue?"

This may appear if you attempt to install Microsoft Agent on Microsoft Internet Explorer 3.02. You can either continue with the installation or update your browser to Internet Explorer 4.0 or later.

### When I attempt to load a page scripted for Microsoft Agent using Netscape Navigator (or other Internet browsers), I get errors.

Microsoft Agent is implemented using ActiveX interfaces. You can use it only with a browser (such as Microsoft Internet Explorer) that supports embedding ActiveX objects through script on a page, and only on systems running Microsoft Windows 95, Windows 98, and Windows NT 4.0 (or later). If you are not using Microsoft Internet Explorer ([https://www.microsoft.com/windows/ie/](https://www.microsoft.com/windows/internet-explorer/default.aspx)), check with your browser vendor for further information on ActiveX support.

 

 




