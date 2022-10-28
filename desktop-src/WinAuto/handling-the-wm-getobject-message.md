---
title: Handling the WM_GETOBJECT Message
description: Both Microsoft Active Accessibility and Microsoft UI Automation send the WM\_GETOBJECT message to a server or provider application to retrieve information about an accessible object supported by the server or provider.
ms.assetid: 4b8e551f-aba7-4a89-8874-ba690175f525
ms.topic: article
ms.date: 05/31/2018
---

# Handling the WM\_GETOBJECT Message

Both Microsoft Active Accessibility and Microsoft UI Automation send the [**WM\_GETOBJECT**](wm-getobject.md) message to a server or provider application to retrieve information about an accessible object supported by the server or provider. Clients never send **WM\_GETOBJECT** directly. Instead, Microsoft Active Accessibility sends this message when a client calls the [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint), [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent), and [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) functions. UI Automation sends **WM\_GETOBJECT** when a client calls [**IUIAutomation::ElementFromHandle**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromhandle), [**ElementFromPoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint), and [**GetFocusedElement**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement), and when handling events for which the client has registered.

Microsoft Active Accessibility or UI Automation specifies the type of object it needs information for by passing a valued called an *object identifier* with the [**WM\_GETOBJECT**](wm-getobject.md) message. When it receives the message, the server or provider examines the object identifier to determine how to respond to the message. The response depends on whether the receiving application implements Microsoft Active Accessibility (a server), UI Automation (a provider), or neither, for the specified object.

-   If the receiving application is an Microsoft Active Accessibility server and the [**WM\_GETOBJECT**](wm-getobject.md) message includes an object identifier of [**OBJID\_CLIENT**](object-identifiers.md), the server should return the value obtained by passing the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface of the object to the [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) function.
-   If the receiving application is a UI Automation provider and the object identifier is **UiaRootObjectId**, the provider should return the [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) interface of the object. The provider obtains the interface by calling the [**UiaReturnRawElementProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider) function.
-   If the receiving application implements neither Microsoft Active Accessibility nor UI Automation, it should pass the [**WM\_GETOBJECT**](wm-getobject.md) message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. Passing the message enables the accessibility framework to determine if a proxy is available for the specified object.
-   If the object identifier is neither [**OBJID\_CLIENT**](object-identifiers.md) nor UiaRootObjectId, the receiving application should pass the [**WM\_GETOBJECT**](wm-getobject.md) message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. Passing the message enables the accessibility framework to use the default providers for standard UI elements.

Microsoft Active Accessibility and UI Automation can pass custom object identifiers in a [**WM\_GETOBJECT**](wm-getobject.md) message to retrieve application-defined values or objects from a server or provider. The [**OBJID\_NATIVEOM**](object-identifiers.md) or [**OBJID\_QUERYCLASSNAMEIDX**](object-identifiers.md) object identifier can be used to retrieve a native Object Model interface, or to request a specific proxy object that is supported by Oleacc.dll.

By handling both the [**OBJID\_CLIENT**](object-identifiers.md) and **UiaRootObjectId** object identifiers, a Microsoft Active Accessibility server implementation can co-exist alongside a UI Automation provider implementation. Because most standard Windows controls and common controls implemented by the common control library (ComCtl32.dll) do not implement either Microsoft Active Accessibility or UI Automation, these controls typically do not handle the [**WM\_GETOBJECT**](wm-getobject.md) message. Instead, the Microsoft Active Accessibility or UI Automation framework checks if a proxy object is available for a particular UI element. Otherwise, it provides the default proxy object for the host window object.

 

 
