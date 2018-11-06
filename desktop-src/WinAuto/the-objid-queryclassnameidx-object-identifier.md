---
title: The OBJID_QUERYCLASSNAMEIDX Object Identifier
description: Microsoft Active Accessibility uses the OBJID\_QUERYCLASSNAMEIDX object identifier with the WM\_GETOBJECT message to determine the class to which a standard Windows control or common control belongs.
ms.assetid: 2167df6d-5df3-40b7-bebe-142f4bd98cd7
ms.topic: article
ms.date: 05/31/2018
---

# The OBJID\_QUERYCLASSNAMEIDX Object Identifier

Microsoft Active Accessibility uses the [**OBJID\_QUERYCLASSNAMEIDX**](object-identifiers.md) object identifier with the [**WM\_GETOBJECT**](wm-getobject.md) message to determine the class to which a standard Windows control or common control belongs. A control responds to this message by returning a value that Microsoft Active Accessibility maps to the class name of the control. Microsoft Active Accessibility uses this information to provide accessibility support for standard Windows controls and common controls.

Generally, only the standard Windows controls and the common controls respond to the [**OBJID\_QUERYCLASSNAMEIDX**](object-identifiers.md) object identifier. However, a custom control can also respond if it includes all of the same functionality as an existing standard Windows control or common control. This enables the custom control to be supported by one of the standard proxy objects provided by Microsoft Active Accessibility.

For more information, see [Appendix F: Object Identifier Values for OBJID\_QUERYCLASSNAMEIDX](appendix-f--object-identifier-values-for-objid-queryclassnameidx.md).

 

 




