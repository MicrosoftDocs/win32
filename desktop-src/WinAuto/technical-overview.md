---
title: Technical Overview
description: Microsoft Active Accessibility improves the way accessibility aids (specialized programs that help people with disabilities use computers more effectively) work with applications running on Microsoft Windows.
ms.assetid: d71ef40e-4c58-4ee6-8909-04ff4f8d20d3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Technical Overview

Microsoft Active Accessibility improves the way accessibility aids (specialized programs that help people with disabilities use computers more effectively) work with applications running on Microsoft Windows.

Microsoft Active Accessibility is based on the Component Object Model (COM), which was developed by Microsoft and is an industry standard that defines a common way for applications and operating systems to communicate. Microsoft Active Accessibility consists of the following components:

-   The COM interface [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master), which exposes information about UI elements. **IAccessible** also has properties and methods for obtaining information about and manipulating that UI element.
-   WinEvents, an event system that allows servers to notify clients when an accessible object changes.
-   Oleacc.dll, a support or run-time DLL.

The Microsoft Active Accessibility DLL, Oleacc.dll, consists of the following components:

-   Functions that allow clients to request an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer (for example, [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master)).
-   Functions that allow servers to return an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer to a client (for example, [**LresultFromObject**](/windows/win32/Oleacc/nf-oleacc-lresultfromobject?branch=master)).
-   Functions for getting localized text for the role and state codes (for example, [**GetRoleText**](/windows/win32/Oleacc/nf-oleacc-getroletexta?branch=master) and [**GetStateText**](/windows/win32/Oleacc/nf-oleacc-getstatetexta?branch=master)).
-   Some helper functions ([**AccessibleChildren**](/windows/win32/Oleacc/nf-oleacc-accessiblechildren?branch=master)).
-   Code that provides the default implementation of [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) for standard USER and COMCTL controls. Because these implement **IAccessible** on behalf of the system controls, they are known as *proxies*.

## In this section

-   [How Active Accessibility Works](how-active-accessibility-works.md)
-   [Active Accessibility Basics](active-accessibility-basics.md)
-   [Server Guidelines](server-guidelines.md)
-   [Client Guidelines](client-guidelines.md)
-   [COM and Unicode Guidelines](com-and-unicode-guidelines.md)

 

 




