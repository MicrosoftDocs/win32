---
title: ScrollItem Control Pattern
description: Describes guidelines and conventions for implementing IScrollItemProvider, including information about methods.
ms.assetid: 'ea0d7438-218c-4925-b24c-a8011f305b9d'
keywords: ["UI Automation,implementing ScrollItem control pattern", "UI Automation,ScrollItem control pattern", "UI Automation,IScrollItemProvider", "IScrollItemProvider", "implementing UI Automation ScrollItem control patterns", "ScrollItem control patterns", "control patterns,IScrollItemProvider", "control patterns,implementing UI Automation ScrollItem", "control patterns,ScrollItem", "interfaces,IScrollItemProvider"]
---

# ScrollItem Control Pattern

Describes guidelines and conventions for implementing [**IScrollItemProvider**](uiauto-iscrollitemprovider.md), including information about methods. The **ScrollItem** control pattern is used to support individual child controls of containers that implement [**IScrollProvider**](uiauto-iscrollprovider.md). The existence of the **ScrollItem** control pattern on a control does not imply that its container or any ancestor must implement the **Scroll** control pattern.

When the container does implement the **Scroll** control pattern, the **ScrollItem** control pattern acts as a communication channel between a child control and its container to ensure that the container can change the currently visible content (or region) within its viewport to display the child control. For examples of controls that implement this control pattern, see [Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md).

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **IScrollItemProvider**](#required-members-for-iscrollitemprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **ScrollItem** control pattern, note the following guidelines and conventions:

-   Items contained within a [Window](uiauto-supportwindowcontroltype.md) or **Canvas** control are not required to implement the [**IScrollItemProvider**](uiauto-iscrollitemprovider.md) interface. As an alternative, however, they must expose a valid location for the [**IUIAutomationElement::CurrentBoundingRectangle**](uiauto-iuiautomationelement-currentboundingrectangle.md) (or [**CachedBoundingRectangle**](uiauto-iuiautomationelement-cachedboundingrectangle.md)) property. This will allow a Microsoft UI Automation client application to use the [**IUIAutomationScrollPattern**](uiauto-iuiautomationscrollpattern.md) control pattern methods on the container to display the child item.

## Required Members for **IScrollItemProvider**

The following method is required for implementing the [**IScrollItemProvider**](uiauto-iscrollitemprovider.md) interface.



| Required members                                                    | Member type | Notes |
|---------------------------------------------------------------------|-------------|-------|
| [**ScrollIntoView**](uiauto-iscrollitemprovider-scrollintoview.md) | Method      | None  |



 

This control pattern has no associated properties or events.

## Related topics

<dl> <dt>

[Control Types and Their Supported Control Patterns](uiauto-controlpatternmapping.md)
</dt> <dt>

[Selection Control Pattern](uiauto-implementingselection.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




