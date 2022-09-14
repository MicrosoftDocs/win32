---
title: Caching UI Automation Properties and Control Patterns
description: When using Microsoft UI Automation, clients often need to retrieve multiple properties for multiple automation elements.
ms.assetid: 948b3bb9-75a9-4197-9680-e6fe7bb86feb
keywords:
- caching,UI Automation properties
- caching,properties
- caching,UI Automation control patterns
- caching,control patterns
- UI Automation,caching properties
- UI Automation,property caching
- clients,caching UI Automation properties
- clients,caching UI Automation control patterns
- UI Automation,caching control patterns
- UI Automation,control pattern caching
- control patterns,caching
ms.topic: article
ms.date: 05/31/2018
---

# Caching UI Automation Properties and Control Patterns

When using Microsoft UI Automation, clients often need to retrieve multiple properties for multiple automation elements. A client could retrieve individual properties one element at a time by using the property retrieval methods such as [**IUIAutomationElement::CurrentName**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentname) or [**CurrentAccessKey**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentaccesskey). However, this method is slow and inefficient because it requires a cross-process call for each property being retrieved. To improve performance, clients can use the caching (also called bulk fetching) capabilities of UI Automation. Caching enables a client to retrieve all of the desired properties for all of the desired elements with a single method call. The client can then retrieve the individual properties from the cache as needed, and can get a new snapshot of the cache periodically, generally in response to events that signify changes in the UI.

The application can request caching when it retrieves a UI Automation element by using a method, such as [**IUIAutomation::ElementFromPointBuildCache**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompointbuildcache), [**IUIAutomationTreeWalker::GetFirstChildElementBuildCache**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationtreewalker-getfirstchildelementbuildcache), or [**IUIAutomationElement::FindFirstBuildCache**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirstbuildcache).

Caching also occurs when you specify a cache request while subscribing to events. The UI Automation element passed to your event handler as the source of an event contains the cached properties and control patterns that are specified by the cache request. Any changes made to the cache request after you subscribe to the event have no effect.

This topic contains the following sections.

-   [Cache Requests](#cache-requests)
    -   [Specifying Property and Control Patterns to Cache](#specifying-property-and-control-patterns-to-cache)
    -   [Specifying the Scoping and Filtering of a Caching Request](#specifying-the-scoping-and-filtering-of-a-caching-request)
    -   [Strength of Element References](#strength-of-element-references)
-   [Retrieving Cached Children and Parents](#retrieving-cached-children-and-parents)
-   [Retrieving a New Snapshot of the Cache](#retrieving-a-new-snapshot-of-the-cache)
-   [Examples](#examples)
-   [Related topics](#related-topics)

## Cache Requests

Caching involves determining which properties to retrieve and which elements to retrieve them from, and then using this information to create a cache request. Whenever the client obtains an [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface for UI item, UI Automation caches the information that is specified in the cache request.

To create a cache request, begin by using the [**IUIAutomation::CreateCacheRequest**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-createcacherequest) method to retrieve an [**IUIAutomationCacheRequest**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationcacherequest) interface pointer. Next, configure the cache request by using the methods of **IUIAutomationCacheRequest**.

### Specifying Property and Control Patterns to Cache

You can specify properties to cache by calling [**IUIAutomationCacheRequest::AddProperty**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationcacherequest-addproperty). You can specify control patterns to cache by calling [**IUIAutomationCacheRequest::AddPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationcacherequest-addpattern). When a control pattern is cached, its properties are not automatically cached; you must specify the properties you want to cache by using **AddProperty**.

You can retrieve a control pattern property (for example, the Value property of the [Value](uiauto-implementingvalue.md) control pattern), without having to retrieve the entire control pattern into the cache. You must retrieve the control pattern only if you need to use a control pattern method.

### Specifying the Scoping and Filtering of a Caching Request

You can specify the elements whose properties and control patterns you want to cache by setting the [**IUIAutomationCacheRequest::TreeScope**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationcacherequest-get_treescope) property before using the request. The scope is relative to the elements that are retrieved by the method to which the cache request is passed. For example, if you set only [**TreeScope\_Children**](/windows/desktop/api/UIAutomationClient/ne-uiautomationclient-treescope), and then retrieve a UI Automation element, the properties and control patterns of children of that element are cached, but the properties and control patterns of the element itself are not cached. To ensure that caching is done for the retrieved element itself, you must include **TreeScope\_Element** in the **IUIAutomationCacheRequest::TreeScope** property. It is not possible to set the scope to **TreeScope\_Parent** or **TreeScope\_Ancestors**. However, a parent element can be cached when a child element is cached; see Retrieving Cached Children and Parents in this topic.

The extent of caching is also affected by the [**IUIAutomationCacheRequest::TreeFilter**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationcacherequest-get_treefilter) property. By default, caching is performed only for elements that appear in the control view of the UI Automation tree. However, you can change this property to apply caching to all elements, or only to elements that appear in the content view.

### Strength of Element References

When you retrieve an automation element, by default you have access to all properties and control patterns of that element, including those properties and control patterns that were not cached. However, you can specify that the reference to the element refers to cached data only, by setting the [**IUIAutomationCacheRequest::AutomationElementMode**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationcacherequest-get_automationelementmode) property to **AutomationElementMode\_None**. In this case, you do not have access to any uncached properties and control patterns of retrieved elements. This means that you cannot access any current properties such as [**IUIAutomationElement::CurrentIsEnabled**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentisenabled) or retrieve a control pattern by using [**IUIAutomationElement::GetCurrentPattern**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcurrentpattern). On cached control patterns, you cannot call methods that perform actions on the control, such as [**IUIAutomationInvokePattern::Invoke**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationinvokepattern-invoke).

An example of an application that might not need full references to objects is a screen reader, which might prefetch the name and control type properties of elements in a window without needing the automation element objects themselves.

## Retrieving Cached Children and Parents

When you retrieve an automation element and request caching for children of that element through the [**IUIAutomationCacheRequest::TreeScope**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationcacherequest-get_treescope) property of the request, it is possible to get the child elements by calling [**IUIAutomationElement::GetCachedChildren**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedchildren) on the element you retrieved.

If [**TreeScope\_Element**](/windows/desktop/api/UIAutomationClient/ne-uiautomationclient-treescope) was included in the scope of the cache request, the root element of the request can be retrieved by calling [**IUIAutomationElement::GetCachedParent**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getcachedparent) on any of the child elements.

> [!Note]  
> You cannot cache parents or ancestors of the root element of the request.

 

## Retrieving a New Snapshot of the Cache

The cache is valid only as long as nothing changes in the UI. Your application is responsible for retrieving a new snapshot of the cache, typically, in response to events.

If you subscribe to an event with a cache request, you obtain an [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) new snapshot of the cache as the source of the event whenever your event handler is called. You can also retrieve a new snapshot of cached information for an element by calling [**IUIAutomationElement::BuildUpdatedCache**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-buildupdatedcache). You can pass in the original [**IUIAutomationCacheRequest**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationcacherequest) to get a new snapshot of all information that was previously cached.

Retrieving a new snapshot of the cache does not modify the properties of any existing [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) references.

## Examples

For code examples that show how to use the caching capabilities of UI Automation, see [How to Use Caching](uiauto-howto-use-caching.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[Obtaining UI Automation Elements](uiauto-obtainingelements.md)
</dt> <dt>

[UI Automation Properties Overview](uiauto-propertiesoverview.md)
</dt> </dl>

 

 




