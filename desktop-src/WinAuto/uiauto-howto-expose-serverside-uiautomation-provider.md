---
title: How to Expose a Server-Side UI Automation Provider
description: This topic contains example code that shows how to expose a server-side Microsoft UI Automation provider for a custom control.
ms.assetid: 68bf16c7-fbab-478a-97be-47d1195028f3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Expose a Server-Side UI Automation Provider

This topic contains example code that shows how to expose a server-side Microsoft UI Automation provider for a custom control.

Microsoft UI Automation sends the [**WM\_GETOBJECT**](wm-getobject.md) message to a provider application to retrieve information about an accessible object supported by the provider. UI Automation sends **WM\_GETOBJECT** when a client calls [**IUIAutomation::ElementFromHandle**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromhandle?branch=master), [**ElementFromPoint**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint?branch=master), and [**GetFocusedElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement?branch=master), and when handling events for which the client has registered.

When a provider receives a [**WM\_GETOBJECT**](wm-getobject.md) message, it should check whether the *lParam* parameter is equal to **UiaRootObjectId**. If it is, the provider should return the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface of the object. The provider returns the interface by calling the [**UiaReturnRawElementProvider**](/windows/win32/UIAutomationCoreApi/nf-uiautomationcoreapi-uiareturnrawelementprovider?branch=master) function.

The following example demonstrates shows how to respond to [**WM\_GETOBJECT**](wm-getobject.md).


```C++
    // Expose the custom button's server-side provider to UI Automation.
    case WM_GETOBJECT:
        {
            // If lParam matches UiaRootObjectId, return IRawElementProviderSimple.
            if (static_cast<long>(lParam) == static_cast<long>(UiaRootObjectId))
            {
                // Retrieve the pointer to the custom button object from the
                // window data.
                CustomButton* pControl = reinterpret_cast<CustomButton*>(
                    GetWindowLongPtr(hwnd, GWLP_USERDATA));

                // Call an application-defined method to get the
                // IRawElementProviderSimple pointer.
                IRawElementProviderSimple* pRootProvider = 
                    pControl->GetUIAutomationProvider(hwnd);

                // Return the IRawElementProviderSimple pointer to UI Automation.
                return UiaReturnRawElementProvider(hwnd, wParam, lParam, 
                    pRootProvider);
            }
            return 0;
        }
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing a Server-Side UI Automation Provider](uiauto-serversideprovider.md)
</dt> <dt>

[The WM\_GETOBJECT Message](the-wm-getobject-message.md)
</dt> <dt>

[How-To Topics for UI Automation Providers](uiauto-howto-topics-for-uiautomation-providers.md)
</dt> </dl>

 

 




