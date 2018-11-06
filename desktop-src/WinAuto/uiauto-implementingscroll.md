---
title: Scroll Control Pattern
description: Describes guidelines and conventions for implementing IScrollProvider, including information about properties and methods. The Scroll control pattern is used to support a control that acts as a scrollable container for a collection of child objects.
ms.assetid: baf8012a-52d5-4465-b26d-aa3d7f550b54
keywords:
- UI Automation,implementing Scroll control pattern
- UI Automation,Scroll control pattern
- UI Automation,IScrollProvider
- IScrollProvider
- implementing UI Automation Scroll control patterns
- Scroll control patterns
- control patterns,IScrollProvider
- control patterns,implementing UI Automation Scroll
- control patterns,Scroll
- interfaces,IScrollProvider
ms.topic: article
ms.date: 05/31/2018
---

# Scroll Control Pattern

Describes guidelines and conventions for implementing [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider), including information about properties and methods. The **Scroll** control pattern is used to support a control that acts as a scrollable container for a collection of child objects.

The control is not required to use scroll bars to support the scrolling functionality, although it commonly does. The following image shows a scrolling control that does not use scroll bars. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

![screen shot showing a scrolling control without scroll bars](images/uia-scrollpattern-without-scrollbars.jpg)

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IScrollProvider**](#required-members-for-iscrollprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **Scroll** control pattern, note the following guidelines and conventions:

-   The children of this control must implement [**IScrollItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollitemprovider).
-   The scroll bars of a container control do not support the **Scroll** control pattern. They must support the [RangeValue](uiauto-implementingrangevalue.md) control pattern instead.
-   When scrolling is measured in percentages, all values or amounts related to scroll graduation must be normalized to a range of 0 to 100.
-   The [**IScrollProvider::HorizontallyScrollable**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontallyscrollable) property and [**VerticallyScrollable**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticallyscrollable) property are independent of the **IsEnabled** property.
-   If the [**IScrollProvider::HorizontallyScrollable**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontallyscrollable) property is **FALSE**, the [**HorizontalViewSize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontalviewsize) property should be set to 100 (100%) and [**HorizontalScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontalscrollpercent) property should be set to **UIA\_ScrollPatternNoScroll** (-1). Likewise, if the [**VerticallyScrollable**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticallyscrollable) property is **FALSE**, the [**VerticalViewSize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticalviewsize) property should be set to 100 (100%) and [**VerticalScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticalscrollpercent) property should be set to **UIA\_ScrollPatternNoScroll** (-1). This allows a Microsoft UI Automation client to use these property values within the [**SetScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-setscrollpercent) method while avoiding a race condition if a direction the client is not interested in scrolling becomes activated.
-   The [**IScrollProvider::HorizontalScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontalscrollpercent) property is locale-specific. Setting **HorizontalScrollPercent** to 100 must set the scrolling location of the control to the equivalent of its rightmost position for languages such as English that read left to right. Alternately, for languages such as Arabic that read right to left, setting **HorizontalScrollPercent** to 100 must set the scroll location to the leftmost position.

## Required Members for **IScrollProvider**

The following properties and methods are required for implementing the [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider) interface.



| Required members                                                                  | Member type | Notes |
|-----------------------------------------------------------------------------------|-------------|-------|
| [**HorizontalScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontalscrollpercent) | Property    | None  |
| [**VerticalScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticalscrollpercent)     | Property    | None  |
| [**HorizontalViewSize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontalviewsize)           | Property    | None  |
| [**VerticalViewSize**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticalviewsize)               | Property    | None  |
| [**HorizontallyScrollable**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_horizontallyscrollable)   | Property    | None  |
| [**VerticallyScrollable**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-get_verticallyscrollable)       | Property    | None  |
| [**Scroll**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-scroll)                                   | Method      | None  |
| [**SetScrollPercent**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iscrollprovider-setscrollpercent)               | Method      | None  |



 

This control pattern has no associated events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




