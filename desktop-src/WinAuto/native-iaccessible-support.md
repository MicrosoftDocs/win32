---
title: Native IAccessible Support
description: Oleacc.dll implements IAccIdentity on behalf of OBJID\_CLIENT \ 160;IAccessible interface pointers and their immediate simple element children.
ms.assetid: '98c6d68b-b64d-44d4-93c3-6c7c6732d59d'
---

# Native IAccessible Support

Oleacc.dll implements [**IAccIdentity**](iaccidentity.md) on behalf of [**OBJID\_CLIENT**](object-identifiers.md#objid-client) [**IAccessible**](iaccessible.md) interface pointers and their immediate simple element children. An **OBJID\_CLIENT** **IAccessible** interface pointer is returned when [**WM\_GETOBJECT**](wm-getobject.md) with *lParam* = **OBJID\_CLIENT** is sent to an **HWND**, which represents the client area of the window or the control as a whole. The parent of such an **IAccessible** interface pointer will typically have a role of [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) and is the **IAccessible** object returned when **WM\_GETOBJECT** with *lParam* = [**OBJID\_WINDOW**](object-identifiers.md#objid-window) is sent to an hwnd.

These [**IAccessible**](iaccessible.md) interface pointers typically occur where an Oleacc.dll proxy is subclassed, or where a simple custom control (such as a container **IAccessible** plus one level of simple element children) provides a native **IAccessible** implementation.

More complicated native [**IAccessible**](iaccessible.md) implementations such as where a hierarchy of **IAccessible**s exists or where custom object IDs are used must implement [**IAccIdentity**](iaccidentity.md) themselves.

 

 




