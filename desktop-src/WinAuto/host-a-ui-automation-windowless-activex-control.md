---
title: Host a UI Automation Windowless ActiveX Control
description: Learn how to create a control container that can host windowless Microsoft ActiveX controls that implement Microsoft UI Automation.
ms.assetid: A0F82968-F434-4F5E-8052-CF7CE65DB120
keywords:
- UI Automation, Windowless ActiveX control
- Windowless ActiveX control, UI Automation
ms.topic: article
ms.date: 05/31/2018
---

# Host a UI Automation Windowless ActiveX Control

Learn how to create a control container able to host windowless Microsoft ActiveX controls that implement Microsoft UI Automation. By using the steps described here, you can ensure that any UI Automation windowless controls hosted in your control container are accessible to assistive technology (AT) client applications.

## What you need to know

### Technologies

-   [ActiveX Controls](/windows/desktop/com/activex-controls)
-   [UI Automation](entry-uiauto-win32.md)

### Prerequisites

-   C/C++
-   Microsoft Win32 and Component Object Model (COM) programming
-   Windowless ActiveX controls
-   UI Automation providers

## Instructions

### Step 1: Provide the IRawElementProviderSimple interface on behalf of the windowless control.

Whenever the system needs the [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) pointer for the root of a windowless control, the system queries the control container. To retrieve the pointer, the container calls the windowless control's implementation of the [**IServiceProvider::QueryService**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/cc678966(v=vs.85)) method.

If the control container has a UI Automation implementation, it can return the windowless control's [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) pointer to the system.

If the control container has a Microsoft Active Accessibility implementation, call the [**UiaIAccessibleFromProvider**](/windows/desktop/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaiaccessiblefromprovider) function to obtain an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer that represents the control, and then return the **IAccessible** interface pointer to the system.

### Step 2: Implement the IRawElementProviderWindowlessSite interface.

A control container implements the [**IRawElementProviderWindowlessSite**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-irawelementproviderwindowlesssite) interface to enable a UI Automation-based windowless control to communicate its accessibility information.

1.  Implement [**IRawElementProviderWindowlessSite::GetRuntimeIdPrefix**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-irawelementproviderwindowlesssite-getruntimeidprefix).

    A windowless control fragment must create a unique runtime ID for itself. To create its runtime ID, a windowless control fragment retrieves a prefix value by calling the control site's [**GetRuntimeIdPrefix**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-irawelementproviderwindowlesssite-getruntimeidprefix) method, and then appends to the prefix an integer value that is unique relative to all other fragments in the windowless control.

    The control site for a windowless control should implement the [**GetRuntimeIdPrefix**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-irawelementproviderwindowlesssite-getruntimeidprefix) method by forming a **SAFEARRAY** that contains the constant **UiaAppendRuntimeId**, followed by an integer value that is unique to the site.

    This example shows how to return a runtime ID prefix for a windowless control.

    ```C++
    IFACEMETHODIMP CProviderWindowlessSite::GetRuntimeIdPrefix(   
         SAFEARRAY **ppsaPrefix)   
    {   
        if (ppsaPrefix == NULL) 
        {
            return E_INVALIDARG;
        }

        // m_siteIndex is the index of the windowless control's
        // site. It is defined by the control container.
        int rId[] = { UiaAppendRuntimeId, m_siteIndex };
        SAFEARRAY *psa = SafeArrayCreateVector(VT_I4, 0, 2);  
        if (psa == NULL)
        {
            return E_OUTOFMEMORY;
        }

        for (LONG i = 0; i < 2; i++)
        {
            SafeArrayPutElement(psa, &i, (void*)&(rId[i]));
        }

        *ppsaPrefix = psa;  
        return S_OK;  
    }  
    ```

    

2.  Implement the [**IRawElementProviderWindowlessSite::GetAdjacentFragment**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-irawelementproviderwindowlesssite-getadjacentfragment) method.

    A control that implements UI Automation must return a pointer to the control's parent fragment provider.

    To return the parent of the fragment, an object that implements the [**IRawElementProviderFragment**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment) interface must be able to implement the [**Navigate**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate) method. Implementing **Navigate** is difficult for a windowless control because the control might be unable to determine its location in the accessible tree of the parent object. The [**IRawElementProviderWindowlessSite::GetAdjacentFragment**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-irawelementproviderwindowlesssite-getadjacentfragment) method enables the windowless control to query its site for the adjacent fragment, and then return that fragment to the client that called **Navigate**.

    This example shows how a control container retrieves the parent fragment of a windowless control.

    ```C++
    IFACEMETHODIMP CProviderWindowlessSite::GetAdjacentFragment(
            enum NavigateDirection direction, IRawElementProviderFragment **ppFragment)   
    {
        if (ppFragment == NULL)
        {
            return E_INVALIDARG;
        }
        
        *ppFragment = NULL;
        HRESULT hr = S_OK;

        switch (direction)
        {
            case NavigateDirection_Parent:
                {  
                    IRawElementProviderSimple *pSimple = NULL;

                    // Call an application-defined function to retrieve the
                    // parent provider interface.
                    hr = GetParentProvider(&pSimple);  
                    if (SUCCEEDED(hr))  
                    {  
                        // Get the parent's IRawElementProviderFragment interface.
                        hr = pSimple->QueryInterface(IID_PPV_ARGS(ppFragment));  
                        pSimple->Release();  
                    } 
                }  
                break;  
      
            case NavigateDirection_FirstChild:
            case NavigateDirection_LastChild:
                hr = E_INVALIDARG;
                break;

            // Ignore NavigateDirection_NextSibling and NavigateDirection_PreviousSibling
            // because there are no adjacent fragments.
            default:  
                break;  
        }  
      
        return hr;  
    }   
    ```

    

### Step 3: Optional: Implement the IRawElementProviderHostingAccessibles interface.

Implement the [**IRawElementProviderHostingAccessibles**](/windows/desktop/api/uiautomationcore/nn-uiautomationcore-irawelementproviderhostingaccessibles) interface if your control container has a UI Automation provider implementation that is the root of an accessibility tree that includes windowless ActiveX controls that support Microsoft Active Accessibility. The **IRawElementProviderHostingAccessibles** interface has a single method, [**GetEmbeddedAccessibles**](/windows/desktop/api/uiautomationcore/nf-uiautomationcore-irawelementproviderhostingaccessibles-getembeddedaccessibles), which retrieves the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointers of all Microsoft Active Accessibility-based windowless ActiveX controls hosted by your control container.

## Related topics

<dl> <dt>

[How to Host an MSAA Windowless ActiveX Control](host-an-msaa-windowless-activex-control.md)
</dt> <dt>

[Windowless ActiveX Control Accessibility](windowless-activex-control-accessibility.md)
</dt> </dl>

 

 
