---
title: What Are Proxy Objects
description: A proxy object acts as an intermediary between the client and an accessible object. The purpose of the proxy object is to monitor the life span of the accessible object and to forward calls to the accessible object only if it is not destroyed.
ms.assetid: 'fdd5d44a-1797-47e6-8044-37dde926c18a'
---

# What Are Proxy Objects?

A *proxy* object acts as an intermediary between the client and an accessible object. The purpose of the proxy object is to monitor the life span of the accessible object and to forward calls to the accessible object only if it is not destroyed.

When a client calls an [**IAccessible**](iaccessible.md) property to get information about an object, the proxy object must check whether the accessible object is still available. If it is, the proxy object passes the client's request to the accessible object. If the accessible object is destroyed (for example, when a dialog box with custom controls is closed), the proxy object returns an error. To indicate that the object has been destroyed, it is recommended that servers return the error code **CO\_E\_OBJNOTCONNECTED** because this error is returned by Component Object Model (COM) after a server calls [CoDisconnectObject](http://go.microsoft.com/fwlink/p/?linkid=178243).

The proxy object is transparent to the client. When the client calls [**AccessibleObjectFromEvent**](accessibleobjectfromevent.md), [**AccessibleObjectFromPoint**](accessibleobjectfrompoint.md), or [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md), it receives back a pointer to an [**IAccessible**](iaccessible.md) interface. However, when the client uses this pointer to call any of the **IAccessible** properties or methods, the code that is executed is within the proxy object.

 

 




