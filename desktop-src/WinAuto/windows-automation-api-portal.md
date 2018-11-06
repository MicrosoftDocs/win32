---
title: Windows Automation API
description: Microsoft Windows offers two API specifications for user interface accessibility and software test automation Microsoft Active Accessibility, and Microsoft UI Automation.
ms.assetid: 73acc580-9573-40ea-8727-b0e7292b2a4c
ms.topic: article
ms.date: 05/31/2018
---

# Windows Automation API

## Purpose

Microsoft Windows offers two API specifications for user interface accessibility and software test automation: Microsoft Active Accessibility, and Microsoft UI Automation. Microsoft Active Accessibility is the legacy API that was introduced in Windows 95 as a platform add-in. UI Automation is a Windows implementation of the UI Automation specification (see [UI Automation Specification]( http://go.microsoft.com/fwlink/p/?linkid=198404) ).

By using the Windows Automation API and following accessible design practices, developers can make applications running on Windows more accessible to many people with vision, hearing, or motion disabilities. Also, UI Automation is specifically designed to provide robust functionality for automated testing scenarios.

## Developer audience

The Windows Automation API is designed for experienced C/C++ developers. In general, developers need a moderate level of understanding about Component Object Model (COM) objects and interfaces, Unicode, and Windows API programming.

For information about UI Automation for managed code, please see [Accessibility]( http://go.microsoft.com/fwlink/p/?linkid=195587) in the .NET Framework Developer's Guide section of MSDN.

## Run-time requirements

The Windows Automation API is supported on the following operating systems: Windows XP, Windows Server 2003 R2, Windows Vista, Windows 7, and Windows Server 2008 R2. Note that Windows XP and Windows Server 2003 also require Microsoft .NET Framework 3.0. Microsoft Active Accessibility is also supported on Microsoft Windows NT 4.0 with Service Pack 6 and Windows 98.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Windows Automation API Overview](windows-automation-api-overview.md)<br/> | Provides a high-level overview of Microsoft Windows Automation API 3.0, highlights the similarities and differences between Microsoft Active Accessibility and UI Automation, describes the components and features that enable the two technologies to work together, and provides guidelines for choosing which technology to implement.<br/> |
| [UI Automation](entry-uiauto-win32.md)<br/>                                | Provides conceptual overviews and detailed reference documention about the UI Automation API.<br/>                                                                                                                                                                                                                                              |
| [Microsoft Active Accessibility](microsoft-active-accessibility.md)<br/>   | Provides conceptual overviews and detailed reference documention about the Microsoft Active Accessibility API.<br/>                                                                                                                                                                                                                             |
| [Common Infrastructure](common-infrastructure.md)<br/>                     | Describes the features and components that are common to both Microsoft Active Accessibility and UI Automation, and that enable them to interoperate.<br/>                                                                                                                                                                                      |
| [Testing Tools](testing-tools.md)<br/>                                     | Describes how to test the accessibility implementation of your application to ensure that the UI is fully accessible to client applications, and to users who access your application though the keyboard. It describes the available tools for testing UI Automation and Microsoft Active Accessibility implementations.<br/>                  |
| [Glossary](uiauto-glossary.md)<br/>                                        | A reference for new or unfamiliar terminology used in Microsoft Active Accessibility.<br/>                                                                                                                                                                                                                                                      |



 

 

 





