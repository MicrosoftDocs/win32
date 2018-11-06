---
title: How to Use Caching
description: This topic contains example code that shows how to use the caching (or bulk fetching) capabilities of Microsoft UI Automation tree.
ms.assetid: d72fa637-35ca-4c28-922d-263f469cb1c8
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Caching

This topic contains example code that shows how to use the caching (or bulk fetching) capabilities of Microsoft UI Automation tree. It discusses the following topics:

-   [Fetching Properties and Control Patterns into the Cache](#fetching-properties-and-control-patterns-into-the-cache)
-   [Retrieving Properties and Control Patterns from the Cache](#retrieving-properties-and-control-patterns-from-the-cache)
-   [Related topics](#related-topics)

## Fetching Properties and Control Patterns into the Cache

The following code example shows a function that retrieves items from a list control and caches the SelectionItem control pattern and Name property for each item. By default, the list items are returned with a full reference, so that all current properties are still available.


```C++
// Given a list element, caches a control pattern and a property for
// all the list items.
IUIAutomationElementArray* FindAndCacheListItems(IUIAutomationElement* pList)
{
    if (pList == NULL)
        return NULL;
    
    IUIAutomationCondition* pCondition = NULL;
    IUIAutomationCacheRequest* pCacheRequest = NULL;
    IUIAutomationElementArray* pFound = NULL;

    HRESULT hr = g_pAutomation->CreateTrueCondition(&pCondition);
    if (FAILED(hr))
        goto cleanup;

    hr = g_pAutomation->CreateCacheRequest(&pCacheRequest);
    if (FAILED(hr))
        goto cleanup;

    hr = pCacheRequest->AddPattern(UIA_SelectionItemPatternId);
    if (FAILED(hr))
        goto cleanup;

    hr = pCacheRequest->AddProperty(UIA_NamePropertyId);
    if (FAILED(hr))
        goto cleanup;

    pList->FindAllBuildCache(TreeScope_Children, pCondition, pCacheRequest, &pFound);
    
cleanup:
    if (pCondition != NULL)
        pCondition->Release();

    if (pCacheRequest != NULL)
        pCacheRequest->Release();

    return pFound;
}
```



## Retrieving Properties and Control Patterns from the Cache

The following code demonstrates how to retrieve properties and control patterns from the cache. It retrieves the SelectionItem control pattern and Name property for a list item.


```C++
// Demonstrates retrieval of cached properties from a list item
// obtained in FindAndCacheListItems.
HRESULT GetCachedListItem(IUIAutomationElement* pItem)
{           
    if (pItem == NULL)
    {
        return E_INVALIDARG;
    }

    IUIAutomationSelectionItemPattern* pSelectionItemPattern;
    HRESULT hr = pItem->GetCachedPatternAs(UIA_SelectionItemPatternId, 
        IID_IUIAutomationSelectionItemPattern, (void**)&pSelectionItemPattern);
    if (pSelectionItemPattern != NULL)
    {
        // ... To do: Do something with the pattern.

        pSelectionItemPattern->Release();
    }

    // Retrieve a cached property.
    BSTR bstrName;
    hr = pItem->get_CachedName(&bstrName);
    if (SUCCEEDED(hr))
    {
        // ... To do: Do something with the property.

        // Clean up when done with name.
        SysFreeString(bstrName);
        bstrName = NULL;
    }

    BOOL isControl;

    // The following returns E_INVALIDARG because the property was not cached.
    // hr = pItem->get_CachedIsControlElement(&isControl);

    // The following is valid because we have a full reference to the object, therefore
    // we can get current properties. If the cache request had been made with 
    // AutomationElementMode_None, no current properties would be available from
    // this IUIAutomationElement.
    hr = pItem->get_CurrentIsControlElement(&isControl);
    return hr;
}
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Caching UI Automation Properties and Control Patterns](uiauto-cachingforclients.md)
</dt> <dt>

[How-To Topics for UI Automation Clients](uiauto-howto-topics-for-uiautomation-clients.md)
</dt> </dl>

 

 




