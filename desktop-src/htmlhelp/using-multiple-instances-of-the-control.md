---
title: Using Multiple Instances of the Control
description: Using Multiple Instances of the Control
ms.assetid: BC701354-A40B-49ab-860E-C67E70802FDC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Multiple Instances of the Control

It is not uncommon for a single HTML file to contain multiple instances of the HTML Help ActiveX control. For example, if you want to add a splash screen, provide a list of **Related Topic** links, and open a WinHelp topic all from one HTML file, then that file would contain three instances of the control. Each instance would call one [command](about-commands.md).

If multiple instances of the control are used in the same file, each instance must have a unique name specified in the ID attribute of the **&lt;OBJECT&gt;** tag. The ID attribute is case-sensitive.

## Related topics

<dl> <dt>

[About the HTML Help ActiveX Control](html-help-activex-control-overview.md)
</dt> </dl>

 

 




