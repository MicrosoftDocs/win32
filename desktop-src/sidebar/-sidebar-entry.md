---
title: Windows Sidebar
description: The Windows Sidebar is a lockable panel on the Windows Vista desktop, similar to the Windows Taskbar, that is able to host and manage mini-applications known as \ 0034;gadgets \ 0034;.
ms.assetid: 152ef1c6-ebbb-48d2-ad30-c70acdf2e25e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Sidebar

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

The Windows Sidebar is a lockable panel on the Windows Vista desktop, similar to the Windows Taskbar, that is able to host and manage mini-applications known as "gadgets".

-   [Introduction to Gadgets](#introduction-to-gadgets)
-   [For More Information](#for-more-information)

## Introduction to Gadgets

A gadget is an HTML and script-based application designed to present the user with a limited set of information or functionality obtained from other applications, controls, or websites and services. Gadgets, although hosted by the Sidebar, are not confined to the Sidebar area; the user can undock and move them onto the desktop as desired.

A gadget is distributed as a .gadget file a renamed .zip archive consisting of a collection of XML, HTML, Microsoft JScript, and Cascading Style Sheets (CSS) files. Installation consists of downloading the .gadget file and allowing the download process to install the gadget or saving the .gadget file to the local system and double-clicking to start the installation process.

Users can run multiple instances of a gadget simultaneously. For example, if users want to know the time in different time zones, they can run multiple instances of the clock gadget, setting each clock to a specific time zone. A user might want to view slideshows of pictures from two or more different folders at the same time. This is possible because the gadget platform provides methods to store settings and automatically associate settings with the correct instance of each gadget. All current gadget settings are saved when the user logs out or restarts. If the Sidebar is on by default, then all gadget instances will run automatically upon startup, and each gadget instance will run with the correct settings.

## In this section



| Topic                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Gadgets for Windows Sidebar Manifest](-sidebar-gadget-manifest.md)<br/>                                                                                      | The gadget "manifest" is an XML file that contains general configuration and presentation information for a gadget. This information is presented to the user through the **Gadget Picker** as gadget and developer details, along with various functional or informational icons. Each gadget package must include a manifest. <br/>                                                                                                               |
| [Developing a Gadget for Windows Sidebar Part 1: The Basics](-sidebar-overview-gdo.md)<br/>                                                                   | The first of three overviews that describe how to create a basic gadget for the Sidebar. In this overview, we demonstrate a simple "Hello World" gadget and the steps required to install and display it in the Sidebar. <br/>                                                                                                                                                                                                                      |
| [Developing a Gadget for Windows Sidebar Part 2: The G:BACKGROUND, G:IMAGE, G:TEXT Presentation Elements and GIMAGE Protocol](-sidebar-overview-gdo2.md)<br/> | The second of three overviews that describe how to create a basic gadget for the Sidebar. In this overview, we demonstrate how to declare a background image and add some simple text and graphics to a gadget using the three presentation elements in the Sidebar `g` namespace ([**g:background**](background-element.md), [**g:image**](image-element.md), and [**g:text**](gtext.md)) and the native Sidebar image protocol (gimage). <br/> |
| [Developing a Gadget for Windows Sidebar Part 3: Settings and Flyouts](-sidebar-overview-gdo3.md)<br/>                                                        | The last of three overviews that describe how to create a basic gadget for the Sidebar. In this overview, we explain the difference between **Settings** (or **Options** as specified in the gadget context menu) and **Flyout** functionality and demonstrate how to incorporate both into a gadget. <br/>                                                                                                                                         |
| [Gadgets for Windows Sidebar Debugging](-sidebar-overview-debugging.md)<br/>                                                                                  | This overview describes the various methods and techniques that can be used to debug gadgets. <br/>                                                                                                                                                                                                                                                                                                                                                 |
| [Gadgets for Windows Sidebar Packaging, Updating, and Refreshing](-sidebar-overview-updating.md)<br/>                                                         | This overview describes how to install or refresh a gadget when updates are made to gadget files during development, debugging, and distribution. <br/>                                                                                                                                                                                                                                                                                             |
| [Gadgets for Windows Sidebar Accessibility and Localization](-sidebar-overview-accessibility-localization.md)<br/>                                            | This overview provides information on how to provide a more accessible and localizable gadget. <br/>                                                                                                                                                                                                                                                                                                                                                |
| [Gadgets for Windows Sidebar Security](-sidebar-gadget-security.md)<br/>                                                                                      | This overview contains information about the security model of the Sidebar. <br/>                                                                                                                                                                                                                                                                                                                                                                   |
| [Windows Sidebar Object Reference](-sidebar-ref-entry.md)<br/>                                                                                                | The Sidebar and gadget architecture consists of three components. The functionality of these components is exposed through the scripting elements described in this section.<br/>                                                                                                                                                                                                                                                                   |
| [Gadget Samples For Windows Sidebar](-sidebar-sample-entry.md)<br/>                                                                                           | This overview provides details about the gadget samples that support the Sidebar documentation. <br/>                                                                                                                                                                                                                                                                                                                                               |



 

## For More Information

For Windows Vista User Experience Guidelines, see [Windows Vista User Experience Guidelines for the Sidebar](http://msdn.microsoft.com/library/aa974179.aspx)

To read posts from the Sidebar team, including gadget authoring tips, links to gadget information, and news about the platform, see the [Gadget Corner blog](http://blogs.msdn.com/sidebar/default.aspx).

To participate in developer community discussions on writing gadgets for the Sidebar, see the [Sidebar Gadget Development forum](http://go.microsoft.com/fwlink/p/?linkid=142587).

 

 





