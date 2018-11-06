---
title: How to Enable Navigation in a UI Automation Fragment Provider
description: This topic contains example code that shows how to enable navigation in a Microsoft UI Automation provider for an element in a fragment.
ms.assetid: 8c390e19-3c17-4e02-ade8-cd5c1ed9E938
ms.topic: article
ms.date: 05/31/2018
---

# How to Enable Navigation in a UI Automation Fragment Provider

This topic contains example code that shows how to enable navigation in a Microsoft UI Automation provider for an element in a fragment.

The following example code implements the [**IRawElementProviderFragment::Navigate**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate) method for a list item in a custom list control. The parent element is the custom list control, and the sibling elements are other items in the list. The method sets the *pRetVal* parameter to **NULL** if there is no element in the specified direction.


```C++
// Implementation of IRawElementProviderFragment::Navigate.
// Enables UI Automation to locate the element in the tree.
HRESULT STDMETHODCALLTYPE ListItemProvider::Navigate(NavigateDirection direction, IRawElementProviderFragment ** pRetVal)
{
    if (pRetVal == NULL) 
    {
        return E_INVALIDARG;
    }

    IRawElementProviderFragment* pFrag = NULL;
    switch(direction)
    {
        case NavigateDirection_Parent:
            pFrag = (IRawElementProviderFragment*) m_parentProvider;       
            break;

        case NavigateDirection_NextSibling:
            pFrag = (IRawElementProviderFragment*) m_nextSiblingProvider;
            break;

        case NavigateDirection_PreviousSibling:  
            pFrag = (IRawElementProviderFragment*) m_previousSiblingProvider;
            break;
    }
    *pRetVal = pFrag;
    if (pFrag != NULL) 
    {
        pFrag->AddRef();
    }
    return S_OK;
}              
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing a Server-Side UI Automation Provider](uiauto-serversideprovider.md)
</dt> <dt>

[How-To Topics for UI Automation Providers](uiauto-howto-topics-for-uiautomation-providers.md)
</dt> </dl>

 

 




