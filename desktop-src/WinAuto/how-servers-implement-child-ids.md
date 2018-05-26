---
title: How Servers Implement Child IDs
description: Server developers can assign child IDs to both simple elements and accessible objects. However, the recommended approach is to support the standard Component Object Model (COM) interface IEnumVARIANT in every accessible object that has children.
ms.assetid: 236de46e-8fe0-4f53-b989-267c9ee87545
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How Servers Implement Child IDs

Server developers can assign child IDs to both simple elements and accessible objects. However, the recommended approach is to support the standard Component Object Model (COM) interface [IEnumVARIANT](http://go.microsoft.com/fwlink/p/?linkid=120799) in every accessible object that has children.

If you implement [IEnumVARIANT](http://go.microsoft.com/fwlink/p/?linkid=120799), you must:

-   Enumerate all children, both simple elements and accessible objects. Provide child IDs for all simple elements and provide the [**IDispatch**](idispatch-interface.md) to each accessible object.
-   For accessible objects, set the **vt** member of the [**VARIANT**](variant-structure.md) to VT\_DISPATCH. The **pdispVal** member must contain a pointer to the [**IDispatch**](idispatch-interface.md) interface. Note that the **VARIANT** is allocated and freed by the client.
-   For simple elements, the child ID is any 32-bit positive integer. Note that zero and negative integers are reserved by Microsoft Active Accessibility. Set the [**VARIANT**](variant-structure.md) structure **vt** member to VT\_I4 and the **lVal** member to the child ID.

If you do not support [IEnumVARIANT](http://go.microsoft.com/fwlink/p/?linkid=120799), you must assign child IDs and number the children in each object sequentially starting with one.

It is recommended that clients use the Microsoft Active Accessibility function [**AccessibleChildren**](/windows/win32/Oleacc/nf-oleacc-accessiblechildren?branch=master) rather than call the server [IEnumVARIANT](http://go.microsoft.com/fwlink/p/?linkid=120799) interface directly.

 

 




