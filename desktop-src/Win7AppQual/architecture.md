---
description: Loosely-coupled Internet Explorer (LCIE) improves the browser’s reliability by separating its components and loosening their interdependence.
ms.assetid: 7609090E-7E2B-4B1F-80FF-192B30A40244
title: Architecture (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)
ms.topic: article
ms.date: 05/31/2018
---

# Architecture (Windows 7 and Windows Server 2008 R2 Application Quality Cookbook)

*Loosely-coupled Internet Explorer* (LCIE) improves the browser’s reliability by separating its components and loosening their interdependence.

In particular, LCIE tries to isolate the Windows Internet Explorer frame and its tabs into separate processes. In Windows Internet Explorer 8, this isolation improves performance and scalability. This architectural change might affect the compatibility of extensions and add-ons, including ActiveX Controls, Browser Helper Objects (BHOs), and UI toolbar components that are built by using older programming techniques.

## Related topics

<dl> <dt>

[Design Updates that Impact Compatibility between Browsers](design-updates-that-impact-compatibility-between-browsers.md)
</dt> </dl>

 

 



