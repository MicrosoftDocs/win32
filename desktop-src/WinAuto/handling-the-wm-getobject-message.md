---
title: Handling the WM\_GETOBJECT Message
description: Both Microsoft Active Accessibility and Microsoft UI Automation send the WM\_GETOBJECT message to a server or provider application to retrieve information about an accessible object supported by the server or provider.
ms.assetid: 4b8e551f-aba7-4a89-8874-ba690175f525
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Handling the WM\_GETOBJECT Message

Both Microsoft Active Accessibility and Microsoft UI Automation send the [**WM\_GETOBJECT**](wm-getobject.md) message to a server or provider application to retrieve information about an accessible object supported by the server or provider. Clients never send **WM\_GETOBJECT** directly. Instead, Microsoft Active Accessibility sends this message when a client calls the [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master), [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master), and [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master) functions. UI Automation sends **WM\_GETOBJECT** when a client calls [**IUIAutomation::ElementFromHandle**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromhandle?branch=master), [**ElementFromPoint**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint?branch=master), and [**GetFocusedElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement?branch=master), and when handling events for which the client has registered.

Microsoft Active Accessibility or UI Automation specifies the type of object it needs information for by passing a valued called an *object identifier* with the [**WM\_GETOBJECT**](wm-getobject.md) message. When it receives the message, the server or provider examines the object identifier to determine how to respond to the message. The response depends on whether the receiving application implements Microsoft Active Accessibility (a server), UI Automation (a provider), or neither, for the specified object.

-   If the receiving application is an Microsoft Active Accessibility server and the [**WM\_GETOBJECT**](wm-getobject.md) message includes an object identifier of [**OBJID\_CLIENT**](object-identifiers.md#objid-client), the server should return the value obtained by passing the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface of the object to the [**LresultFromObject**](/windows/win32/Oleacc/nf-oleacc-lresultfromobject?branch=master) function.
-   If the receiving application is aUI Automation provider and the object identifier is **UiaRootObjectId**, the provider should return the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface of the object. The provider obtains the interface by calling the [**UiaReturnRawElementProvider**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider?branch=master) function.
-   If the receiving application implements neither Microsoft Active Accessibility nor UI Automation, it should pass the [**WM\_GETOBJECT**](wm-getobject.md) message to the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function. Passing the message enables the accessibility framework to determine if a proxy is available for the specified object.
-   If the object identifier is neither [**OBJID\_CLIENT**](object-identifiers.md#objid-client) nor UiaRootObjectId, the receiving application should pass the [**WM\_GETOBJECT**](wm-getobject.md) message to the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function. Passing the message enables the accessibility framework to use the default providers for standard UI elements.

Microsoft Active Accessibility and UI Automation can pass custom object identifiers in a [**WM\_GETOBJECT**](wm-getobject.md) message to retrieve application-defined values or objects from a server or provider. The [**OBJID\_NATIVEOM**](object-identifiers.md#objid-nativeom) or [**OBJID\_QUERYCLASSNAMEIDX**](object-identifiers.md#objid-queryclassnameidx) object identifier can be used to retrieve a native Object Model interface, or to request a specific proxy object that is supported by Oleacc.dll.

By handling both the [**OBJID\_CLIENT**](object-identifiers.md#objid-client) and **UiaRootObjectId** object identifiers, a Microsoft Active Accessibility server implementation can co-exist alongside a UI Automation provider implementation. Because most standard Windows controls and common controls implemented by the common control library (ComCtl32.dll) do not implement either Microsoft Active Accessibility or UI Automation, these controls typically do not handle the [**WM\_GETOBJECT**](wm-getobject.md) message. Instead, the Microsoft Active Accessibility or UI Automation framework checks if a proxy object is available for a particular UI element. Otherwise, it provides the default proxy object for the host window object.

 

 




