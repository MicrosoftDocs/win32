---
title: Active Accessibility and UI Automation
description: Microsoft Active Accessibility is designed for use with Windows XP and earlier operating systems.
ms.assetid: 8eb36d2c-0c2f-4311-8690-52ce070c9f33
ms.topic: article
ms.date: 05/31/2018
---

# Active Accessibility and UI Automation

Microsoft Active Accessibility is designed for use with Windows XP and earlier operating systems. Developers of custom controls and accessible technology client applications for Windows XP and Windows Vista should consider using Microsoft [UI Automation](entry-uiauto-win32.md) instead.

Microsoft UI Automation is a full-featured system that provides more precise information about the user interface and gives the user more ability to interact with controls. In particular, it provides greatly enhanced support for text.

A set of proxy objects provides UI Automation support for standard Microsoft Win32 and Windows Forms controls. Richer support is available for controls specifically written with UI Automation in mind, including native Windows Presentation Foundation (WPF) elements, which do not directly support Microsoft Active Accessibility. Custom controls that support UI Automation can be written in either managed or unmanaged code.

Microsoft Active Accessibility clients have limited access, through a bridging layer, to UI elements that support only UI Automation. For more information, see [Appendix G: Active Accessibility Bridge to UI Automation](appendix-g--active-accessibility-bridge-to-ui-automation.md).

For more information about the similarities and differences between Microsoft Active Accessibility and UI Automation, see [Microsoft Active Accessibility and UI Automation Compared](microsoft-active-accessibility-and-ui-automation-compared.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Getting Started](getting-started.md)
</dt> <dt>

[UI Automation](entry-uiauto-win32.md)
</dt> </dl>

 

 




