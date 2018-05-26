---
title: VirtualizedItem Control Pattern
description: Describes guidelines and conventions for implementing IVirtualizedItemProvider, including information about properties and methods.
ms.assetid: 7a95e92f-7ccb-4c9b-8986-1d2de7038e47
keywords:
- UI Automation,implementing VirtualizedItem control pattern
- UI Automation,VirtualizedItem control pattern
- UI Automation,IVirtualizedItemProvider
- IVirtualizedItemProvider
- implementing UI Automation VirtualizedItem control patterns
- VirtualizedItem control patterns
- control patterns,IVirtualizedItemProvider
- control patterns,implementing UI Automation VirtualizedItem
- control patterns,VirtualizedItem
- interfaces,IVirtualizedItemProvider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VirtualizedItem Control Pattern

Describes guidelines and conventions for implementing [**IVirtualizedItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ivirtualizeditemprovider?branch=master), including information about properties and methods. The **VirtualizedItem** control pattern is used to support virtualized items, which are items that are represented by placeholder automation elements in the Microsoft UI Automation tree.

Virtualized items can include items retrieved from a control that supports the [ItemContainer](uiauto-implementingitemcontainer.md) control pattern, or a virtualized embedded object retrieved from a control that supports the [Text](uiauto-implementingtextandtextrange.md) control pattern. The placeholder for a virtualized item might not have loaded data for all UI Automation properties, and may return [**UIA\_E\_ELEMENTNOTAVAILABLE**](uiauto-error-codes.md#uia-e-elementnotavailable) in response to queries for properties that are not available. The **VirtualizedItem** control pattern provides a method for realizing a virtual item so that full information is made available for the item, and a full automation element can be created for the item in the UI Automation tree.

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IVirtualizedItemProvider**](#required-members-for-ivirtualizeditemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **VirtualizedItem** control pattern, note the following guidelines and conventions:

-   Any UI Automation placeholder element that can be virtualized must support the **VirtualizedItem** control pattern by exposing the [**IVirtualizedItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ivirtualizeditemprovider?branch=master) interface.
-   When [**IVirtualizedItemProvider::Realize**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ivirtualizeditemprovider-realize?branch=master) is called, the placeholder object must be updated with full implementations of its properties and control patterns.
-   When [**IVirtualizedItemProvider::Realize**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ivirtualizeditemprovider-realize?branch=master) is called, the provider can change the viewport so that the virtualized item comes into view. Bringing the item into view is not required; however, off-screen, non-virtualized items should support the [**IScrollItemProvider::ScrollIntoView**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iscrollitemprovider-scrollintoview?branch=master) method.

## Required Members for **IVirtualizedItemProvider**

The following properties and methods are required for implementing the [**IVirtualizedItemProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ivirtualizeditemprovider?branch=master) interface.



| Required members                                           | Member type | Notes |
|------------------------------------------------------------|-------------|-------|
| [**Realize**](/windows/win32/UIAutomationCore/nf-uiautomationcore-ivirtualizeditemprovider-realize?branch=master) | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Implementing the UI Automation ItemContainer Control Pattern](uiauto-implementingitemcontainer.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[Working with Virtualized Items](uiauto-workingwithvirtualizeditems.md)
</dt> </dl>

 

 




