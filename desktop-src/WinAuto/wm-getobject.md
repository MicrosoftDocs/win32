---
title: WM_GETOBJECT message (Winuser.h)
description: Sent by both Microsoft Active Accessibility and Microsoft UI Automation to obtain information about an accessible object contained in a server application.
ms.assetid: '59350aa1-1697-4110-b9a6-f30ee56c4cff'
keywords:
- WM_GETOBJECT message Windows Accessibility
topic_type:
- apiref
api_name:
- WM_GETOBJECT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETOBJECT message

Sent by both Microsoft Active Accessibility and Microsoft UI Automation to obtain information about an accessible object contained in a server application.

Applications never send this message directly. Microsoft Active Accessibility sends this message in response to calls to [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint), [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent), or [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow). However, server applications handle this message. UI Automation sends this message in response to calls to [**IUIAutomation::ElementFromHandle**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromhandle), [**ElementFromPoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint), and [**GetFocusedElement**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement), and when handling events for which a client has registered.


```C++
dwFlags = (WPARAM)(DWORD) wParam;
dwObjId = (LPARAM)(DWORD) lParam;
```



## Parameters

<dl> <dt>

*dwFlags* 
</dt> <dd>

Provides additional information about the message and is used only by the system. Servers pass *dwFlags* as the *wParam* parameter in the call to [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) when handling the message.

</dd> <dt>

*dwObjId* 
</dt> <dd>

Object identifier. This value is one of the [object identifier](object-identifiers.md) constants or a custom object identifier. A server application must check this value to identify the type of information being requested. Before comparing this value against the OBJID\_ values, the server must cast it to **DWORD**; otherwise, on 64-bit Windows, the sign extension of the *lParam* can interfere with the comparison.

-   If *dwObjId* is one of the OBJID\_ values such as [**OBJID\_CLIENT**](object-identifiers.md), the request is for a Microsoft Active Accessibility object that implements [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).
-   If *dwObjId* is equal to **UiaRootObjectId**, the request is for a UI Automation provider. If the server is implementing UI Automation, it should return a provider using the [**UiaReturnRawElementProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider) function.
-   If *dwObjId* is [**OBJID\_NATIVEOM**](object-identifiers.md), the request is for the control's underlying object model. If the control supports this request, it should return an appropriate COM interface by calling the [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) function.
-   If *dwObjId* is [**OBJID\_QUERYCLASSNAMEIDX**](object-identifiers.md), the request is for the control to identify itself as a standard Windows control or a common control implemented by the common control library (ComCtrl.dll).

</dd> </dl>

## Return value

If the window or control does not need to respond to this message, it should pass the message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function; otherwise, the window or control should return a value that corresponds to the request specified by *dwObjId*:

-   If the window or control implements UI Automation, the window or control should return the value obtained by a call to the [**UiaReturnRawElementProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider) function.
-   If *dwObjId* is [**OBJID\_NATIVEOM**](object-identifiers.md) and the window exposes a native Object Model, the windows should return the value obtained by a call to the [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) function.
-   If *dwObjId* is [**OBJID\_CLIENT**](object-identifiers.md) and the window implements [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible), the window should return the value obtained by a call to the [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) function.

## Remarks

When a client calls [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) or any of the other **AccessibleObjectFrom***X* functions that retrieve an interface to an object, Microsoft Active Accessibility sends the **WM\_GETOBJECT** message to the appropriate window procedure within the appropriate server application. While processing **WM\_GETOBJECT**, server applications call [**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject) and use the return value of this function as the return value for the message. Microsoft Active Accessibility, in conjunction with the COM library, performs the appropriate marshaling and passes the interface pointer from the server back to the client.

Servers do not respond to **WM\_GETOBJECT** before the object is fully initialized or after it begins to close down. When an application creates a new window, the system sends [**EVENT\_OBJECT\_CREATE**](event-constants.md) to notify clients before it sends the [WM\_CREATE](../winmsg/wm-create.md) message to the application's window procedure. Because many applications use WM\_CREATE to start their initialization process, servers do not respond to the **WM\_GETOBJECT** message until finished processing the **WM\_CREATE** message.

A server uses **WM\_GETOBJECT** to perform the following tasks:

-   [Create New Accessible Objects](create-new-accessible-objects.md)
-   [Reuse Existing Pointers to Objects](reuse-existing-pointers-to-objects.md)
-   [Create New Interfaces to the Same Object](create-new-interfaces-to-the-same-object.md)

For clients, this means that they might receive distinct interface pointers for the same user interface element, depending on the server's action. To determine if two interface pointers point to the same user interface element, clients compare [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties of the object. Comparing pointers does not work.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Redistributable<br/>          | Active Accessibility 1.3 RDK on Windows NT 4.0 with SP6 and later and Windows 95<br/>              |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[How to Handle WM\_GETOBJECT](how-to-handle-wm-getobject.md)
</dt> <dt>

[How WM\_GETOBJECT Works](how-wm-getobject-works.md)
</dt> <dt>

[**LresultFromObject**](/windows/desktop/api/Oleacc/nf-oleacc-lresultfromobject)
</dt> </dl>

 

