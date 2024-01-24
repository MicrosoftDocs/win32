---
title: ProgressBar Control Type
description: This topic provides information about Microsoft UI Automation support for the ProgressBar control type.
ms.assetid: 2ea0c1f1-1a0a-4360-bdcb-8edc13cc3c31
keywords:
- UI Automation,support for ProgressBar control type
- UI Automation,ProgressBar control type
- UI Automation,tree structure for ProgressBar control type
- UI Automation,properties for ProgressBar control type
- UI Automation,control patterns for ProgressBar control type
- UI Automation,events for ProgressBar control type
- tree structures,ProgressBar control type
- properties,ProgressBar control type
- control patterns,ProgressBar control type
- events,ProgressBar control type
- support for ProgressBar control type
- ProgressBar control type
- control types,tree structure for ProgressBar control type
- control types,control patterns for ProgressBar control type
- control types,support for ProgressBar
- control types,ProgressBar
ms.topic: article
ms.date: 12/04/2019
---

# ProgressBar Control Type

This topic provides information about Microsoft UI Automation support for the **ProgressBar** control type.

Progress bar controls indicate the progress of a lengthy operation. The control consists of a rectangle that is gradually filled with the system highlight color as an operation progresses.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **ProgressBar** control type. The UI Automation requirements apply to all progress bar controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

- [Typical Tree Structure](#typical-tree-structure)
- [Relevant Properties](#relevant-properties)
- [Required Control Patterns](#required-control-patterns)
- [Required Events](#required-events)
- [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to progress bar controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).


| Control View | Content View | 
|--------------|--------------|
| <ul><li>ProgressBar</li></ul> | <ul><li>ProgressBar</li></ul> | 


The progress bar controls do not have any children in the control or content view of the UI Automation tree.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to progress bars. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).

| UI Automation Property                                                                                              | Value           | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.      | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.      | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.      | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **ProgressBar** |                                                                                                                                                                                                      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**        | The progress bar control is always included in the content view of the UI Automation tree.                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**        | The progress bar control is always included in the control view of the UI Automation tree.                                                                                                           |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.      | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes.      | If there is a static text label, this property must expose a reference to that control.                                                                                                              |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.      | Localized string corresponding to the **ProgressBar** control type. The default value is "progress bar" for en-US or English (United States).                                                        |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.      | The progress bar control typically gets its name from a static text label. If there is not a static text label the application developer must expose a value for the Name property.                  |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by progress bar controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                              | Support/Value | Notes                                                                                                                                      |
|---------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**IRangeValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irangevalueprovider)     | Depends       | Progress bar controls that take a numeric range must implement the [RangeValue](uiauto-implementingrangevalue.md) control pattern.        |
| [**Minimum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_minimum)         | Depends           | The value of this property is the minimum value that the control can be set to. This value should be less than [**Maximum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_maximum).                                                      |
| [**Maximum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_maximum)         | Depends         | The value of this property is the maximum value that the control can be set to. This value should be greater than [**Minimum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_minimum).                                                        |
| [**SmallChange**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_smallchange) | **NaN**       | This property is not required because progress bar controls are read-only.                                                                 |
| [**LargeChange**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_largechange) | **NaN**       | This property is not required because progress bar controls are read-only.                                                                 |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)               | Depends       | Progress bar controls that give a textual indication of progress must implement the [Value](uiauto-implementingvalue.md) control pattern. |
| [**IsReadOnly**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_isreadonly)        | **TRUE**      | The value for this property is always **TRUE**.                                                                                            |
| [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_value)                  | See notes.    | This property exposes textual progress of a progress bar control.                                                                          |



 

## Required Events

The following table lists the UI Automation events that progress bars are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                           |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                  |                                                                                                                            |
| [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.        | If the control supports the [RangeValue](uiauto-implementingrangevalue.md) control pattern, it must support this event.   |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                  | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.             |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




