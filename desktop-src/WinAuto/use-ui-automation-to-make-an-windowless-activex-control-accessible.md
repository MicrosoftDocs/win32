---
title: How to Use UI Automation to Make a Windowless ActiveX Control Accessible
description: Describes how to use the Microsoft UI Automation \ 32;API to ensure that your windowless Microsoft ActiveX control is accessible to assistive technology (AT) client applications.
ms.assetid: D584E90D-6537-4F48-8553-0DCA061FAF2A
keywords:
- Windowless ActiveX Control, Accessibility
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Use UI Automation to Make a Windowless ActiveX Control Accessible

Describes how to use the Microsoft UI Automation API to ensure that your windowless Microsoft ActiveX control is accessible to assistive technology (AT) client applications.

## What you need to know

### Technologies

-   [ActiveX Controls](https://msdn.microsoft.com/library/windows/desktop/ms693753)
-   [UI Automation](entry-uiauto-win32.md)

### Prerequisites

-   C/C++
-   Microsoft Win32 and Component Object Model (COM) programming
-   Windowless ActiveX Controls
-   UI Automation providers

## Instructions

### Step 1: Implement the UI Automation provider interfaces.

To make your application accessible, you must implement the UI Automation provider interfaces for your windowless ActiveX control, including [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master), [**IRawElementProviderFragment**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment?branch=master), [**IRawElementProviderFragmentRoot**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot?branch=master), and [**IRawElementProviderAdviseEvents**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovideradviseevents?branch=master). You should implement these interfaces just as you would for a window-based control, except as described in the following steps. For more information about implementing UIA provider interfaces, see [UI Automation Provider Programmer's Guide](uiauto-providerportal.md).

### Step 2: Implement the IServiceProvider interface.

When a client needs accessibility information about your windowless control, the control container calls your control's **IServiceProvider::QueryService** method to retrieve the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface pointer for your control.

The following example shows how to implement the **QueryService** method.


```C++
STDMETHODIMP CMyAccessibleUIAControl::QueryService(REFGUID guidService,
        REFIID riid, void **ppvObject)
{  
    if (ppvObject == NULL)
    {
        return E_INVALIDARG;
    }

    *ppvObject = NULL;  
    HRESULT hr = E_FAIL; 
 
    if (guidService == __uuidof(IRawElementProviderSimple))
    {  
        hr = QueryInterface(riid, ppvObject);  
    }  
    return hr;  
}
```



### Step 3: Implement the IRawElementProviderFragment::Navigate method.

When your windowless control’s [**IRawElementProviderFragment::Navigate**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate?branch=master) method is called to navigate to the parent or a sibling of the windowless control's root provider, your **Navigate** method should delegate to the [**IRawElementProviderWindowlessSite::GetAdjacentFragment**](https://msdn.microsoft.com/library/windows/desktop/hh448788) method of the control container.

The following example shows how to implement the [**Navigate**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate?branch=master) method.


```C++
STDMETHODIMP CMyAccessibleUIAControl::Navigate(NavigateDirection direction,
     IRawElementProviderFragment **ppRetVal) 
{   
    if (ppRetVal == NULL)
    {
        return E_INVALIDARG;
    }

    *ppRetVal = NULL;  
    HRESULT hr = E_FAIL;
    IRawElementProviderWindowlessSite *pWindowlessSite = NULL;  
    
    if (direction == NavigateDirection_Parent)  
    {  
        // Query the control container's windowless site 
        // for the parent.
         if (SUCCEEDED(m_pClientSite->QueryInterface(
                IID_PPV_ARGS(&amp;pWindowlessSite))))  
        {  
            hr =  pWindowlessSite->GetAdjacentFragment(direction, ppRetVal);  
        }  
    }  

    else if (direction == NavigateDirection_FirstChild)  
    {  
        // GetFragmentForChild is an application-defined function that 
        // retrieves the first or last child fragment.
        hr =  GetFragmentForChild(FIRST, ppRetVal);  
    }  

    else if (direction == NavigateDirection_LastChild)  
    {  
        hr = GetFragmentForChild(LAST, ppRetVal);  
    }  

    SafeRelease(&amp;pWindowlessSite);
    return S_OK;   
}
```



### Step 4: Implement the IRawElementProviderFragment::GetRuntimeId method.

When your windowless control receives a call to its [**IRawElementProviderFragment::GetRuntimeId**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-getruntimeid?branch=master) method, the control must do the following:

1.  Retrieve a runtime ID prefix by calling the control site's [**IRawElementProviderWindowlessSite::GetRuntimeIdPrefix**](https://msdn.microsoft.com/library/windows/desktop/hh448789) method.
2.  Create a unique runtime ID for the control by appending an integer to the runtime ID prefix.
3.  Return the runtime ID to the caller.

The following example shows how to implement the [**GetRuntimeId**](https://msdn.microsoft.com/library/windows/desktop/hh448789) method.


```C++
STDMETHODIMP CMyAccessibleUIAControl::GetRuntimeId(SAFEARRAY **ppRetVal)  
{   
    if (ppRetVal == NULL)
    {
        return E_INVALIDARG;
    }

    *ppRetVal = NULL;  
    HRESULT hr = E_FAIL;
    IRawElementProviderWindowlessSite *pWindowlessSite = NULL;  

    if (SUCCEEDED(m_pClientSite->QueryInterface(IID_PPV_ARGS(&amp;pWindowlessSite))))  
    {  
        // Create a safe array to hold runtime ID.
        SAFEARRAY *psa = SafeArrayCreateVector(VT_I4, 1, 3);  
        if (psa == NULL)
        {
            hr = E_OUTOFMEMORY;
        }

        // Retrieve the runtime ID prefix from the control container. The prefix
        // consists of UiaAppendRuntimeId followed by the windowless site ID.
        if (SUCCEEDED(hr))
        {    
            hr = pWindowlessSite->GetRuntimeIdPrefix(&amp;psa);  
        } 

        if (SUCCEEDED(hr))
        {
        // Append this fragment's ID to the retrieved runtime ID prefix.
            long i = 2;
            hr = SafeArrayPutElement(psa, &amp;i, (void*)&amp;m_Id);        
        }

        if (SUCCEEDED(hr))
        {
            *ppRetVal = psa;  
        }
    }

    SafeRelease(&amp;pWindowlessSite);
    return hr;  
}
```



## Related topics

<dl> <dt>

[Use MSAA to Make a Windowless ActiveX Control Accessible](use-msaa-to-make-an-windowless-activex-control-accessible.md)
</dt> <dt>

[Windowless ActiveX Control Accessibility](windowless-activex-control-accessibility.md)
</dt> </dl>

 

 




