---
title: Using IAccessibleEx from a Client
description: This topic explains how clients access the IAccessibleEx implementation of a server and use it to get UI Automation properties and control patterns for UI elements.
ms.assetid: e057bbe8-5dd7-41fc-a5d5-bcf4c1c6433d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using IAccessibleEx from a Client

This topic explains how clients access the [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) implementation of a server and use it to get UI Automation properties and control patterns for UI elements.

The procedures and examples in this section assume an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) client that is already in-process, and an existing Microsoft Active Accessibility server. They also assume that the client has already obtained an **IAccessible** object by using one of the accessibility framework functions such as [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master), [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master), or [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master).

### Obtaining an IAccessibleEx Interface from the IAccessible Interface

A client that has an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface for an accessible object can use it to obtain the corresponding [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) interface by following these steps:

-   Call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) on the original [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) object with an IID of \_\_uuidof(IServiceProvider).
-   Call **IServiceProvider::QueryService** to get the [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master).

### Handling the Child ID

Clients must be prepared for servers with a child ID other than CHILDID\_SELF. After obtaining an [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) interface from an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master), clients must call [**IAccessibleEx::GetObjectForChild**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iaccessibleex-getobjectforchild?branch=master) if the child ID is not CHILDID\_SELF (indicating a parent object).

The following example shows how to get an [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) for a particular [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) object and child ID.


```C++
   
HRESULT GetIAccessibleExFromIAccessible(IAccessible * pAcc, long idChild, 
                                           IAccessibleEx ** ppaex)
{
    *ppaex = NULL;

    // First, get IServiceProvider from the IAccessible.
    IServiceProvider * pSp = NULL;
    HRESULT hr = pAcc->QueryInterface(IID_IServiceProvider, (void **) & pSp);
    if(FAILED(hr))
        return hr;
    if(pSp == NULL)
        return E_NOINTERFACE;

    // Next, get the IAccessibleEx for the parent object.
    IAccessibleEx * paex = NULL;
    hr = pSp->QueryService(__uuidof(IAccessibleEx), __uuidof(IAccessibleEx),
                                                                 (void **)&amp;paex);
    pSp->Release();
    if(FAILED(hr))
        return hr;
    if(paex == NULL)
        return E_NOINTERFACE;

    // If this is for CHILDID_SELF, we're done. Otherwise, we have a child ID and 
    // can request the object for child.
    if(idChild == CHILDID_SELF)
    {
        *ppaex = paex;
        return S_OK;
    }
    else
    {
        // Get the IAccessibleEx for the specified child.
        IAccessibleEx * paexChild = NULL;
        hr = paex->GetObjectForChild(idChild, &amp;paexChild);
        paex->Release();
        if(FAILED(hr))
            return hr;
        if(paexChild == NULL)
            return E_NOINTERFACE;
        *ppaex = paexChild;
        return S_OK;
    }
}
```



### Obtaining the IRawElementProviderSimple Interface

If a client has an [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) interface, it can use QueryInterface to get to the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface, as the following example shows.


```C++
HRESULT GetIRawElementProviderFromIAccessible(IAccessible * pAcc, long idChild,
                                                 IRawElementProviderSimple ** ppEl)
{
    * ppEl = NULL;

    // First, get the IAccessibleEx for the IAccessible and child ID pair.
    IAccessibleEx * paex;
    HRESULT hr = GetIAccessibleExFromIAccessible( pAcc, idChild, &amp;paex );
    if(FAILED(hr))
        return hr;

    // Next, use QueryInterface.
    hr = paex->QueryInterface(__uuidof(IRawElementProviderSimple), (void **)ppEl);
    paex->Release();
    return hr;
}
```



### Retrieving Control Patterns

If a client has access to the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface, it can retrieve control pattern interfaces that have been implemented by providers, and can then call methods on those interfaces. The following example shows how to do this.


```C++
// Helper function to get a pattern interface from an IAccessible and child ID 
// pair. Gets the IAccessibleEx, then calls GetPatternObject and QueryInterface.
HRESULT GetPatternFromIAccessible(IAccessible * pAcc, long idChild,
                                     PATTERNID patternId, REFIID iid, void ** ppv)
{
    // First, get the IAccesibleEx for this IAccessible and child ID pair.
    IRawElementProviderSimple * pel;
    HRESULT hr = GetIRawElementProviderSimpleFromIAccessible(pAcc, idChild, &amp;pel);
    if(FAILED(hr))
        return hr;
    if(pel == NULL)
        return E_NOINTERFACE;

    // Now get the pattern object.
    IUnknown * pPatternObject = NULL;
    hr = pel->GetPatternProvider(patternId, &amp;pPatternObject);
    pel->Release();
    if(FAILED(hr))
        return hr;
    if(pPatternObject == NULL)
        return E_NOINTERFACE;

    // Finally, use QueryInterface to get the correct interface type.
    hr = pPatternObject->QueryInterface(iid, ppv);
    pPatternObject->Release();
    if(*ppv == NULL)
        return E_NOINTERFACE;
    return hr;
}

HRESULT CallInvokePatternMethod(IAccessible * pAcc, long idChild)
{
    IInvokeProvider * pPattern;
    HRESULT hr = GetPatternFromIAccessible(pAcc, varChild,
                                  UIA_InvokePatternId, __uuidof(IInvokeProvider),
                                  (void **)&amp;pPattern);
    if(FAILED(hr))
        return hr;

    hr = pPattern->Invoke();
    pPattern->Release();
    return hr;
}
```



### Retrieving Property Values

If a client has access to [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master), it can retrieve property values. The following example shows how to get values for the AutomationId and LabeledBy Microsoft UI Automation properties.


```C++
#include <initguid.h>
#include <uiautomationcoreapi.h> // Includes the UI Automation property GUID definitions.
#include <uiautomationcoreids.h> // Includes definitions of pattern/property IDs.

// Assume we already have a IRawElementProviderSimple * pEl.

VARIANT varValue;

// Get AutomationId property:
varValue.vt = VT_EMPTY;
HRESULT hr = pEl->GetPropertyValue(UIA_AutomationIdPropertyId, &amp;varValue);
if(SUCCEEDED(hr))
{
    if(varValue.vt == VT_BSTR)
    {
        // AutomationId is varValue.bstrVal.
    }
    VariantClear(&amp;varValue);
}


// Get LabeledBy property:
varValue.vt = VT_EMPTY;
hr = pEl->GetPropertyValue(UIA_LabeledByPropertyId, &amp;varValue);
if(SUCCEEDED(hr))
{
    if(varValue.vt == VT_UNKNOWN || varValue.punkVal != NULL)
    {
        // Use QueryInterface to get IRawElementProviderSimple.
        IRawElementProviderSimple * pElLabel = NULL;
        hr = varValue.punkVal->QueryInterface(__uuidof(IRawElementProviderSimple),
                                              (void**)&amp; pElLabel);
        if (SUCCEEDED(hr))
        {
            if(pElLabel != NULL)
            {
            // Use the pElLabel pointer here.
            pElLabel ->Release();
            }
        }
    }
    VariantClear(&amp;varValue);
}
```



The preceding example applies to properties that are not associated with a control pattern. To access control pattern properties, a client must obtain and use a control pattern interface.

### Retrieving an IAccessible Interface from an IRawElementProviderSimple Interface

If a client obtains the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface for a UI element, the client can use that interface to obtain a corresponding [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface for the element. This is useful if the client needs to access the Microsoft Active Accessibility properties for the element.

A client can obtain the [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface as a property value (for example, by calling [**IRawElementProviderSimple::GetPropertyValue**](/windows/win32/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpropertyvalue?branch=master) with UIA\_LabeledByPropertyId), or as an item retreived by a method (for example, by calling [**ISelectionProvider::GetSelection**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-getselection?branch=master) to retrieve an array of **IRawElementProviderSimple** interfaces of selected elements). After obtaining the **IRawElementProviderSimple** interface, a client can use it to obtain a corresponding [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) by following these steps:

-   Attempt to use QueryInterface to get the [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) interface.
-   If QueryInterface fails, call [**IAccessibleEx::ConvertReturnedElement**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iaccessibleex-convertreturnedelement?branch=master) on the [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) instance from which the property was originally obtained.
-   Call the [**GetIAccessiblePair**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iaccessibleex-getiaccessiblepair?branch=master) method on the new [**IAccessibleEx**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iaccessibleex?branch=master) instance to obtain an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interfae and child ID.

The following code snippet demonstrates how to obtain the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface from a previously-obtained [**IRawElementProviderSimple**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple?branch=master) interface.


```C++
// IRawElementProviderSimple * pVal - an element returned by a property or method
// from another IRawElementProviderSimple.

IAccessible * pAcc = NULL;
long idChild;

// First, try to use QueryInterface to get the IAccessibleEx interface.
IAccessibleEx * pAccEx;
HRESULT hr = pVal->QueryInterface(__uuidof(IAccessibleEx), (void**)&amp;pAccEx);
if (SUCCEEDED(hr)
{
    if (!pAccEx)
    {
        // If QueryInterface fails, and the IRawElementProviderSimple was 
              // obtained as a property or return value from another 
              // IRawElementProviderSimple, pass it to the 
              // IAccessibleEx::ConvertReturnedValue method of the
        // originating element.

        pAccExOrig->ConvertReturnedElement(pVal, &amp;pAccEx);
    }

    if (pAccEx)
    {
        // Call GetIAccessiblePair to get an IAccessible interface and 
              // child ID.
        pAccEx->GetIAccessiblePair(&amp;pAcc, &amp;idChild);
    }

    // Finally, use the IAccessible interface and child ID.
    if (pAcc)
    {
        // Use IAccessible methods to get further information about this UI
              // element, or pass it to existing code that works in terms of 
              // IAccessible.
        ...
    }
}    
```



 

 




