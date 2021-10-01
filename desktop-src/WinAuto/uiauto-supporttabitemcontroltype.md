---
title: TabItem Control Type
description: This topic provides information about Microsoft UI Automation support for the TabItem control type.
ms.assetid: 97b8c043-1ac5-4e14-be80-8687300a10a2
keywords:
- UI Automation,support for TabItem control type
- UI Automation,TabItem control type
- UI Automation,tree structure for TabItem control type
- UI Automation,properties for TabItem control type
- UI Automation,control patterns for TabItem control type
- UI Automation,events for TabItem control type
- tree structures,TabItem control type
- properties,TabItem control type
- control patterns,TabItem control type
- events,TabItem control type
- support for TabItem control type
- TabItem control type
- control types,tree structure for TabItem control type
- control types,control patterns for TabItem control type
- control types,support for TabItem
- control types,TabItem
ms.topic: article
ms.date: 05/31/2018
---

# TabItem Control Type

This topic provides information about Microsoft UI Automation support for the **TabItem** control type.

A tab item control is used as the control within a tab control that selects a specific page to be shown in a window.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **TabItem** control type. The UI Automation requirements apply to all tab item controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to tab item controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>TabItem<ul><li>Image (0 or 1)</li><li>Text</li><li>Pane<ul><li>Various controls (0 or more)</li></ul></li></ul></li></ul> | <ul><li>TabItem<ul><li>Pane<ul><li>Various controls (0 or more)</li></ul></li></ul></li></ul> | 




 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **TabItem** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value       | Notes                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.  | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.  | The outermost rectangle that contains the whole control.                                                                                    |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.  | The tab item control must have a clickable point that causes the item to become selected.                                                   |
| [**UIA\_ControllerForPropertyId**](uiauto-automation-element-propids.md)               | See notes.  | This property can be used as pointer to the associated tab pane. This is useful when it cannot host a pane as child of the tab item object. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **TabItem** | This value is the same for all UI frameworks.                                                                                               |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE        | The tab item control is always included in the content view of the UI Automation tree.                                                      |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE        | The tab item control is always included in the control view of the UI Automation tree.                                                      |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.  | If the control can receive keyboard focus, it must support this property.                                                                   |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | Null        | The tab item control does not have a static text label.                                                                                     |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.  | Localized string corresponding to the **TabItem** control type. The default value is "tab item" for en-US or English (United States).       |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.  | The tab item control self-labeled.                                                                                                          |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all tab item controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                 | Support  | Notes                                                                                                                    |
|-----------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------|
| [**ISelectionItemProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionitemprovider) | Required | The tab item control must support [**IUIAutomationSelectionItemPattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationselectionitempattern). |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)               | Never    | The tab item control never supports [**IUIAutomationInvokePattern**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationinvokepattern).             |



 

## Required Events

The following table lists the UI Automation events that tab item controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                     | Notes                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                        |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.   |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                   | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.               | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_SelectionItem\_ElementRemovedFromSelectionEventId**](uiauto-event-ids.md) |                                                                                                                            |
| [**UIA\_SelectionItem\_ElementSelectedEventId**](uiauto-event-ids.md)                         |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                    |                                                                                                                            |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




