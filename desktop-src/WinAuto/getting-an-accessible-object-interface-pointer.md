---
title: Getting an Accessible Object Interface Pointer
description: Microsoft Active Accessibility client applications retrieve interface pointers to accessible objects by using one of the following functions.
ms.assetid: b82467f0-0d46-482a-8f6d-ad64f236601e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting an Accessible Object Interface Pointer

Microsoft Active Accessibility client applications retrieve interface pointers to accessible objects by using one of the following functions.

**AccessibleObjectFromEvent**

Many clients look up information about specific accessible objects that generate events. Because the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface is the "gateway" to accessible objects, clients must have an easy way to associate [WinEvents](winevents.md) with the **IAccessible** interface of the object generating the events. Microsoft Active Accessibility provides the [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master) function specifically for this purpose.

> [!Note]  
> Clients with [in-context hook functions](in-context-hook-functions.md) must call the [IsWindow](http://go.microsoft.com/fwlink/p/?linkid=178221) function before calling [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master).

 

The [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master) function accepts much of the same information that a client's [*hook function*](/windows/win32/Winuser/nc-winuser-wineventproc?branch=master) receives. When a client hook function receives an event notification, it passes the appropriate parameters from events to **AccessibleObjectFromEvent**.

The function retrieves either the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface of the user interface element that generated the event or the interface of the element's parent object. If the parent object's interface pointer is returned, the client calls the parent's properties and methods to obtain information about the child element that generated the event.

**AccessibleObjectFromPoint**

To retrieve the address of an object's [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface at a specified point on the screen, clients use the [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master) function.

**AccessibleObjectFromWindow**

To retrieve an object's [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface from a window handle, clients use the [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master) function.

It is possible that servers return distinct interface pointers for the same user interface element each time the [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master), [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master), or [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master) function is called. To determine if two pointers refer to the same user interface element, client developers must compare [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties of the object, not pointers.

 

 




