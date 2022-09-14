---
title: ScrollBar Control Type
description: This topic provides information about Microsoft UI Automation support for the ScrollBar control type.
ms.assetid: c89ca087-3e93-4e86-ac79-731e3e7a361d
keywords:
- UI Automation,support for ScrollBar control type
- UI Automation,ScrollBar control type
- UI Automation,tree structure for ScrollBar control type
- UI Automation,properties for ScrollBar control type
- UI Automation,control patterns for ScrollBar control type
- UI Automation,events for ScrollBar control type
- tree structures,ScrollBar control type
- properties,ScrollBar control type
- control patterns,ScrollBar control type
- events,ScrollBar control type
- support for ScrollBar control type
- ScrollBar control type
- control types,tree structure for ScrollBar control type
- control types,control patterns for ScrollBar control type
- control types,support for ScrollBar
- control types,ScrollBar
ms.topic: article
ms.date: 05/31/2018
---

# ScrollBar Control Type

This topic provides information about Microsoft UI Automation support for the **ScrollBar** control type.

Scroll bar controls enable a user to scroll content within a window or item container. The control consists of a set of buttons and a thumb control.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **ScrollBar** control type. The UI Automation requirements apply to all scroll bar controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to scroll bar controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>ScrollBar<ul><li>Button (0, 2, or 4)</li><li>Thumb (0 or 1)</li></ul></li></ul> | Not applicable. (The scroll bar control has no content.) | 




 

The scroll bar control can have zero to five children. Because the subtree has more than one button control, the element must set a specific [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md) value to each item to make them discoverable for automated testing tools.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to scroll bar controls. Note that a scroll bar control never has content; its functionality is exposed through the [Scroll](uiauto-implementingscroll.md) control pattern, which is supported on the container being scrolled.

For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value         | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.    | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                                    |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.    | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | NaN           | The scroll bar control does not have clickable points.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **ScrollBar** | This value is the same for all frameworks. Scroll bars that function as sliders must use the [Slider](uiauto-supportslidercontroltype.md) control type.                                                                                                                                                                                                                                                                                                                        |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | FALSE         | The scroll bar control is never a content element. If the scroll bar is a standalone control, it must fulfill the [Slider](uiauto-supportslidercontroltype.md) control type and return [**UIA\_SliderControlTypeId**](uiauto-controltype-ids.md) for the [**IUIAutomationElement::CurrentControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentcontroltype) (or [**CachedControlType**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedcontroltype)) property. |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE          | The scroll bar control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                                                        |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.    | If the control can receive keyboard focus, it must support this property. A scroll bar control rarely takes the focus, but when it does, the focus should remain on the scroll bar control itself, not on the child buttons or the thumb. The user should be able to perform all scrolling actions by using the UP ARROW and DOWN ARROW (or RIGHT ARROW and LEFT ARROW) keys, or the PAGE UP and PAGE DOWN keys.                                                                |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | NULL          | Scroll bars do not have labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.    | Localized string corresponding to the **ScrollBar** control type. The default value is "scroll bar" for en-US or English (United States).                                                                                                                                                                                                                                                                                                                                       |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | NULL          | The scroll bar control does not have content elements and the [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property is not required to be set.                                                                                                                                                                                                                                                                                           |
| [**UIA\_OrientationPropertyId**](uiauto-automation-element-propids.md)                   | See notes.    | The scroll bar control must always expose its horizontal or vertical orientation.                                                                                                                                                                                                                                                                                                                                                                                               |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all scroll bar controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).

> [!Note]  
> When a scroll bar is used as a control for mouse manipulation only, it does not support control patterns. If it is used as a slider control within an application, it must be given the [Slider](uiauto-supportslidercontroltype.md) control type.

 



| Control Pattern                                           | Support | Notes                                                                                                                                                                                                                          |
|-----------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IRangeValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irangevalueprovider) | Depends | The [RangeValue](uiauto-implementingrangevalue.md) control pattern is required to be supported only if the [Scroll](uiauto-implementingscroll.md) control pattern is not supported on the container that has the scroll bar. |
| [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider)         | Never   | The [Scroll](uiauto-implementingscroll.md) control pattern is never directly supported on the scroll bar.                                                                                                                     |



 

## Required Events

The following table lists the UI Automation events that scroll bar controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |
| [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.        | If the control supports the [RangeValue](uiauto-implementingrangevalue.md) control pattern, it must support this event.   |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




