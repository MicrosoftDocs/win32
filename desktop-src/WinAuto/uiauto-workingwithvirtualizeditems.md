---
title: Working with Virtualized Items
description: This topic describes how to use functionality provided by the ItemContainer and VirtualizedItem control patterns to find and retrieve information about virtualized items.
ms.assetid: e1898ba0-5ffa-4c61-b378-c7ef7c4a2c52
keywords:
- clients,UI Automation virtualized items
- clients,virtualized items
- clients,control patterns
- clients,VirtualizedItem control patterns
- clients,ItemContainer control patterns
- clients,UI Automation VirtualizedItem control patterns
- clients,UI Automation control patterns
- clients,UI Automation ItemContainer control patterns
- UI Automation,virtualized items
- UI Automation,control patterns
- UI Automation,VirtualizedItem control patterns
- UI Automation,ItemContainer control patterns
- VirtualizedItem control patterns
- ItemContainer control patterns
- control patterns,VirtualizedItem
- control patterns,ItemContainer
ms.topic: article
ms.date: 05/31/2018
---

# Working with Virtualized Items

This topic describes how to use functionality provided by the [ItemContainer](uiauto-implementingitemcontainer.md) and [VirtualizedItem](uiauto-implementingvirtualizeditem.md) control patterns to find and retrieve information about virtualized items.

-   [Overview of Virtualization](#overview-of-virtualization)
-   [How a Control Supports Virtualization](#how-a-control-supports-virtualization)
-   [How Clients Find and Realize Virtualized Items](#how-clients-find-and-realize-virtualized-items)
-   [Example](#example)
-   [Related topics](#related-topics)

## Overview of Virtualization

Controls that contain a large number of child items can use virtualization to efficiently manage the items. With virtualization, the control maintains full information in memory for only a subset of items at any given time. Typically, the subset includes only those items that are currently visible to the user. Full information about the remaining virtualized items is kept in storage and is loaded into memory, or realized, as the control needs it, for example, as new items become visible to the user.

Controls that use virtualization represent a challenge because only realized items are fully available as Microsoft UI Automation elements in the UI Automation tree. Virtualized items do not exist in the tree, so information about them is not available to clients. To retrieve information about virtualized items, clients need a way to force UI Automation to pass the request to realize the items to the control. After the items have been realized, UI Automation can create UI Automation elements for them. UI Automation includes two control patterns to enable clients to work with virtualized items: [ItemContainer](uiauto-implementingitemcontainer.md) and [VirtualizedItem](uiauto-implementingvirtualizeditem.md).

## How a Control Supports Virtualization

Any control that can contain virtualized items must support the [ItemContainer](uiauto-implementingitemcontainer.md) control pattern. Further, any item that can be virtualized must support the [VirtualizedItem](uiauto-implementingvirtualizeditem.md) control pattern. The functionality that is exposed by the ItemContainer and VirtualizedItem control patterns is accessible to clients through the [**IUIAutomationItemContainerPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationitemcontainerpattern) and [**IUIAutomationVirtualizedItemPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationvirtualizeditempattern) interfaces.

## How Clients Find and Realize Virtualized Items

Clients can use the [**IUIAutomationItemContainerPattern::FindItemByProperty**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationitemcontainerpattern-finditembyproperty) method to search for child items in the container based on the value of a particular property. The method can also retrieve the first item in the container or the item that follows the specified item. If a matching child item is found, the **FindItemByProperty** retrieves an [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface for the item. However, if the child item is virtualized, the **IUIAutomationElement** interface is a placeholder. The [**UIA\_E\_ELEMENTNOTAVAILABLE**](uiauto-error-codes.md) error occurs when the client attempts to use the **IUIAutomationElement** interface to retrieve property values or call methods that are not yet available. Which properties or methods are available through a placeholder depends on the control implementation. The only requirement for a placeholder is to support the [**IUIAutomationVirtualizedItemPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationvirtualizeditempattern) interface.

The [**UIA\_E\_ELEMENTNOTAVAILABLE**](uiauto-error-codes.md) error is an indication to the client that an item may be virtualized. The client should respond by retrieving the [**IUIAutomationVirtualizedItemPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationvirtualizeditempattern) interface for the item, and then realizing the item by calling the [**IUIAutomationVirtualizedItemPattern::Realize**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationvirtualizeditempattern-realize) method. If this succeeds, the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface is fully functional with all appropriate properties available.

Depending on the control implementation, calling [**IUIAutomationVirtualizedItemPattern::Realize**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationvirtualizeditempattern-realize) may cause the control to scroll the item into view. However, a client should not rely on the item scrolling into view or made visible. To ensure that the item is visible, the client can use the [**IUIAutomationScrollItemPattern::ScrollIntoView**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationscrollitempattern-scrollintoview) method.

## Example

For example code that shows how to use the UI Automation support for virtualization, see [How to Retrieve a Virtualized Item](uiauto-howto-retrieve-virtualized-item.md).

## Related topics

<dl> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 




