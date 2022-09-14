---
title: Implementing IAccessibleEx for Providers
description: This section explains how to add Microsoft UI Automation provider capabilities to a Microsoft Active Accessibility server by implementing the IAccessibleEx interface.
ms.assetid: c03dc552-7919-4a35-8ff2-4cdd822bc0b7
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IAccessibleEx for Providers

This section explains how to add Microsoft UI Automation provider capabilities to a Microsoft Active Accessibility server by implementing the [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) interface.

Before implementing [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex), consider the following requirements:

-   The baseline Microsoft Active Accessibility accessible object hierarchy must be clean. [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) cannot correct problems with existing accessible object hierarchies. Any problems with the object model structure must be corrected in the Microsoft Active Accessibility implementation before implementing **IAccessibleEx**.
-   The [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementation must comply with both the Microsoft Active Accessibility specification and the UI Automation specification. Tools are available to validate compliance under both specifications. For more information, see [Testing Tools](testing-tools.md) and [UI Automation Verify (UIA Verify) Test Automation Framework](https://www.codeplex.com/UIAutomationVerify/).

Implementing [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) requires these main steps:

-   Implement **IServiceProvider** on the accessible object so that the [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) interface can be found on this or a separate object.
-   Implement [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) on the accessible object.
-   Create accessible objects for any Microsoft Active Accessibility child items, which in Microsoft Active Accessibility are represented by the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface on the parent object (for example, list items). Implement [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) on these objects.
-   Implement [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) on all the accessible objects.
-   Implement the appropriate control pattern interfaces on the accessible objects.

### Implementing the IServiceProvider Interface

Because the implementation of [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) for a control may reside in a separate object, client applications cannot rely on [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to obtain this interface. Instead, clients are expected to call **IServiceProvider::QueryService**. In the following example implementation of this method, it is assumed that **IAccessibleEx** is not implemented on a separate object; therefore the method simply calls through to **QueryInterface**.


```C++
           
HRESULT CListboxAccessibleObject::QueryService(REFGUID guidService, REFIID riid, LPVOID *ppvObject)
{
    if (ppvObject == NULL)
    {
        return E_INVALIDARG;
    }
    *ppvObject = NULL;
    if (guidService == __uuidof(IAccessibleEx))
    {
        return QueryInterface(riid, ppvObject);
    }
    else 
    {
        return E_NOINTERFACE;
    }
};      
```



### Implementing the IAccessibleEx Interface

In Microsoft Active Accessibility, a UI element is always identified by an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface and a child ID. A single instance of **IAccessible** can represent multiple UI elements.

Because each [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) instance represents only a single UI element, each [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) and child ID pair must be mapped to a single **IAccessibleEx** instance. **IAccessibleEx** includes two methods to handle this mapping:

-   [**GetObjectForChild**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iaccessibleex-getobjectforchild)—Retrieves the [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) interface for the specified child. This method returns **NULL** if the **IAccessibleEx** implementation does not recognize the specified child ID, does not have an **IAccessibleEx** for the specified child, or represents a child element.
-   [**GetIAccessiblePair**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iaccessibleex-getiaccessiblepair)—Retrieves the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface and child ID for the [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) element. For **IAccessible** implementations that do not use a child ID, this method retrieves the corresponding **IAccessible** object and CHILDID\_SELF.

The following example shows the implementation of the [**GetObjectForChild**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iaccessibleex-getobjectforchild) and [**GetIAccessiblePair**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iaccessibleex-getiaccessiblepair) methods for an item in a custom list view. The methods enable UI Automation to map the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) and child ID pair to a corresponding [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) instance.


```C++
           
HRESULT CListboxAccessibleObject::GetObjectForChild(
    long idChild, IAccessibleEx **ppRetVal)
{ 
    VARIANT vChild;
    vChild.vt = VT_I4;
    vChild.lVal = idChild;
    HRESULT hr = ValidateChildId(vChild);
    if (FAILED(hr))
    {
        return E_INVALIDARG;
    }
    // List item accessible objects are stored as an array of
    // pointers; for the purpose of this example it is assumed that 
    // the list contents will not change. Accessible objects are
    // created only when needed.
    if (itemProviders[idChild - 1] == NULL)
    {
        // Create an object that supports UI Automation and
        // IAccessibleEx for the item.
        itemProviders[idChild - 1] = 
          new CListItemAccessibleObject(idChild, 
          g_pListboxControl);
        if (itemProviders[idChild - 1] == NULL)
        {
            return E_OUTOFMEMORY;
        }
    }
    IAccessibleEx* pAccEx = static_cast<IAccessibleEx*>
      (itemProviders[idChild - 1]);
    if (pAccEx != NULL)
    {
      pAccEx->AddRef();
    }
    *ppRetVal = pAccEx;
    return S_OK; 
}

HRESULT CListItemAccessibleObject::GetIAccessiblePair(
    IAccessible **ppAcc, long *pidChild)
{ 
    if (ppAcc == NULL || pidChild == NULL)
    {
        return E_INVALIDARG;   
    }

                CListboxAccessibleObject* pParent = 
        m_control->GetAccessibleObject();

    HRESULT hr = pParent->QueryInterface( 
        __uuidof(IAccessible), (void**)ppAcc);
    if (FAILED(hr))
    {
        *pidChild = 0;
        return E_NOINTERFACE;
    }
    *pidChild = m_childID; 
    return S_OK; 
}
}
```



If an accessible object implementation does not use a child ID, the methods can still be implemented as shown in the following code snippet.


```C++
           

    // This sample implements IAccessibleEx on the same object; it could use a tear-off
    // or inner object instead.
    class MyAccessibleImpl: public IAccessible,
                        public IAccessibleEx,
                        public IRawElementProviderSimple
    {
    public:
    ...
   HRESULT STDMETHODCALLTYPE GetObjectForChild( long idChild, IAccessibleEx **ppRetVal )
    {
        // This implementation does not support child IDs.
        *ppRetVal = NULL;
        return S_OK;
    }

    HRESULT STDMETHODCALLTYPE GetIAccessiblePair( IAccessible ** ppAcc, long * pidChild )
    {
        // This implementation assumes that IAccessibleEx is implemented on same object as
        // IAccessible.
        *ppAcc = static_cast<IAccessible *>(this);
        (*ppAcc)->AddRef();
        *pidChild = CHILDID_SELF;
        return S_OK;
    }
```



### Implement the IRawElementProviderSimple Interface

Servers use [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) to expose information about UI Automation properties and control patterns. **IRawElementProviderSimple** includes the following methods:

-   [**GetPatternProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpatternprovider)—This method is used to expose control pattern interfaces. It returns an object that supports the specified control pattern, or **NULL** if the control pattern is not supported.
-   [**GetPropertyValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpropertyvalue)—This method is used to expose UI Automation property values.
-   [**HostRawElementProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-get_hostrawelementprovider)—This method is not used with [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementations.
-   [**ProviderOptions**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-get_provideroptions)—This method is not used with [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) implementations.

An [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) server exposes control patterns by implementing [**IRawElementProviderSimple::GetPatternProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpatternprovider). This method takes an integer parameter that specifies the control pattern. The server returns **NULL** if the pattern is not supported. If the control pattern interface is supported, servers return an [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) and the client then calls [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to get the appropriate control pattern.

An [**IAccessibleEx**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iaccessibleex) server can support UI Automation properties (such as LabeledBy, and IsRequiredForForm) by implementing [**IRawElementProviderSimple::GetPropertyValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpropertyvalue) and supplying an integer PROPERTYID identifying the property as a parameter. This technique applies only to UI Automation properties that are not included in a control pattern interface. Properties associated with a control pattern interface are exposed through the control pattern interface method. For example, the IsSelected property from the [SelectionItem](uiauto-implementingselectionitem.md) control pattern would be exposed with [**ISelectionItemProvider::get\_IsSelected**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-get_isselected).

 

 