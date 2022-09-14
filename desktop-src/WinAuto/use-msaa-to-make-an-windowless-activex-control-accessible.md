---
title: Use MSAA to make a windowless ActiveX control accessible
description: Describes how to use the Microsoft Active Accessibility \ 32;API to ensure that your windowless Microsoft ActiveX control is accessible to assistive technology (AT) client applications.
ms.assetid: 30F874F9-EA45-4365-8798-FEA011C62DA9
keywords:
- ActiveX Control, accessibility
ms.topic: article
ms.date: 05/31/2018
---

# Use MSAA to make a windowless ActiveX control accessible

Describes how to use the Microsoft Active Accessibility API to ensure that your windowless Microsoft ActiveX control is accessible to assistive technology (AT) client applications.

## What you need to know

### Technologies

-   [ActiveX Controls](/windows/desktop/com/activex-controls)
-   [Microsoft Active Accessibility](microsoft-active-accessibility.md)

### Prerequisites

-   C/C++
-   Microsoft Win32 and Component Object Model (COM) programming
-   Windowless ActiveX Controls
-   Microsoft Active Accessibility servers

## Instructions

### Step 1: Implement the IAccessible interface.

To make your windowless ActiveX control accessible, you must implement the Microsoft Active Accessibility [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface, just as you would for a window-based control, except as described in the following steps. For more information about implementing **IAccessible**, see [Developer's Guide for Active Accessibility Servers](developer-s-guide-for-active-accessibility-servers.md).

### Step 2: Implement the IServiceProvider interface.

When a client requests accessibility information about your windowless control, the container calls your control's [**IServiceProvider::QueryService**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678966(v=vs.85)) method to retrieve the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer.

This example shows how to implement the [**QueryService**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678966(v=vs.85)) method.


```C++
STDMETHODIMP CMyAccessibleMSAAControl::QueryService(REFGUID guidService, 
        REFIID riid, void **ppvObject)
{      
    if (ppvObject == NULL)
    {
        return E_INVALIDARG;
    }

    *ppvObject = NULL;  
    HRESULT hr = E_FAIL;  

    if (guidService == __uuidof(IAccessible))
    {  
        hr = QueryInterface(riid, ppvObject);  
    }  
    return hr;  
}
```



### Step 3: Delegate IAccessible::get\_accParent method calls to the control site's IAccessibleWindowlessSite::GetParentAccessible method.

When a client requests the parent object of your windowless control, the container calls your control's [**IAccessible::get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent) method. Your **get\_accParent** implementation should delegate to the [**IAccessibleWindowlessSite::GetParentAccessible**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-getparentaccessible) method of the container.

This example shows how to implement the [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent) method.


```C++
HRESULT CMyAccessibleMSAAControl::get_accParent(IDispatch **ppdispParent)  
{  
    if (ppdispParent == NULL)
    {
        return E_INVALIDARG;
    }

    HRESULT hr = S_FALSE;  
    *ppdispParent = NULL;  

    IAccessibleWindowlessSite *pWindowlessSite = NULL;  

    if (SUCCEEDED(m_pClientSite->QueryInterface(IID_PPV_ARGS(&pWindowlessSite))))  
    {  
        IAccessible *pParentAcc = NULL;
        if (SUCCEEDED(pWindowlessSite->GetParentAccessible(&pParentAcc)))
        {
            hr = pParentAcc->QueryInterface(IID_PPV_ARGS(ppdispParent));  
        }
    }  

    SafeRelease(&pWindowlessSite);
    return hr;  
}
```



### Step 4: Acquire a range of object IDs to assign to the event sources in your windowless control.

Like window-based controls, a windowless ActiveX control calls the [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) function to notify clients of important events. The function parameters include the object ID of the item that is raising the event. Your windowless control must assign object IDs by using a value from a range acquired by calling the control site’s [**IAccessibleWindowlessSite::AcquireObjectIdRange**](/windows/desktop/api/oleacc/nf-oleacc-iaccessiblewindowlesssite-acquireobjectidrange) method.

This example shows how to acquire a range of object ID values from the control container.


```C++
IAccessibleWindowlessSite *pWindowlessSite = NULL;

if (SUCCEEDED(m_pClientSite->QueryInterface(
        IID_PPV_ARGS(&pWindowlessSite))))  
{  
    if (FAILED(pWindowlessSite->AcquireObjectIdRange(100, this, 
            &m_idObjectBase)))  
    {  
        m_idObjectBase = -1;  
    } 
}

SafeRelease(&pWindowlessSite);
```



### Step 5: Implement the IAccessibleHandler interface.

When a windowless control calls the [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) function, the control specifies the object ID of the UI item that is raising the event, and specifies the control container as the window that will respond to [**WM\_GETOBJECT**](wm-getobject.md) messages on behalf of the control.

If a client application responds to the event, the control container receives a [**WM\_GETOBJECT**](wm-getobject.md) message that includes the object ID of the UI item that raised the event. The control container responds by looking up the windowless control that "owns" the object ID, and then calling that control's [**IAccessibleHandler::AccessibleObjectFromID**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessiblehandler-accessibleobjectfromid) method. The **AccessibleObjectFromID** method returns the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer for the UI item, and the control container forwards the pointer to the client application.

## Related topics

<dl> <dt>

[Use UI Automation to Make a Windowless ActiveX Control Accessible](use-ui-automation-to-make-an-windowless-activex-control-accessible.md)
</dt> <dt>

[Windowless ActiveX Control Accessibility](windowless-activex-control-accessibility.md)
</dt> </dl>

 

 