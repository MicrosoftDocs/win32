---
title: ObjectModel Control Pattern
description: Describes guidelines and conventions for implementing IObjectModelProvider, including information about methods. The ObjectModel control pattern is used to expose a pointer to the underlying object model of a document.
ms.assetid: 90A6937E-0E98-41EF-8EEB-E23CB71510E4
keywords:
- UI Automation,implementing ObjectModel control pattern
- UI Automation,ObjectModel control pattern
- UI Automation,IObjectModelProvider
- IObjectModelProvider
- implementing UI Automation ObjectModel control pattern
- ObjectModel control pattern
- control patterns,IObjectModelProvider
- control patterns,implementing UI Automation ObjectModel
- control patterns,ObjectModel
- interfaces,IObjectModelProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ObjectModel Control Pattern

Describes guidelines and conventions for implementing [**IObjectModelProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448776), including information about methods. The **ObjectModel** control pattern is used to expose a pointer to the underlying object model of a document.

Many applications implement rich object models that add value beyond what Microsoft UI Automation provides. This control pattern allows a client to navigate from a UI Automation element into the underlying object model.

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IObjectModelProvider**](#required-members-for-iobjectmodelprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **ObjectModel** control pattern, note the following guidelines and conventions:

-   The [**IObjectModelProvider::GetUnderlyingObjectModel**](https://msdn.microsoft.com/library/windows/desktop/hh448778) method should return a pointer to the object that is as close as possible to the source UI element. For example, in a web browser, a UI Automation provider for a single element should return an object model pointer for the element. Returning an object model pointer for the document root would be far less useful.
-   The client of the **ObjectModel** control pattern is expected to have the IID for the interface they are seeking, which is why it is enough to return a simple [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) pointer.
-   Because UI Automation marshals the pointer to the client process, the provider should expect the client to access the object model using standard Component Object Model (COM) practices.

## Required Members for **IObjectModelProvider**

The following method is required for implementing the [**IObjectModelProvider**](https://msdn.microsoft.com/library/windows/desktop/hh448776) interface.



| Required members                                                                             | Member type | Notes                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetUnderlyingObjectModel**](https://msdn.microsoft.com/library/windows/desktop/hh448778) | Method      | Returns a COM pointer to the underlying object model. The client is expected to call the [**IUnknown::QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) method to retrieve specific object model pointers. |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




