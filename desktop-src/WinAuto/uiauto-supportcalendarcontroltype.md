---
title: Calendar Control Type
description: This topic provides information about Microsoft UI Automation support for the Calendar control type. A calendar control allows the user to easily determine the date and select other dates.
ms.assetid: 886cf1a4-0e6f-4ae1-9dc4-e97ac6a22359
keywords:
- UI Automation,support for Calendar control type
- UI Automation,Calendar control type
- UI Automation,tree structure for Calendar control type
- UI Automation,properties for Calendar control type
- UI Automation,control patterns for Calendar control type
- UI Automation,events for Calendar control type
- tree structures,Calendar control type
- properties,Calendar control type
- control patterns,Calendar control type
- events,Calendar control type
- support for Calendar control type
- Calendar control type
- control types,tree structure for Calendar control type
- control types,control patterns for Calendar control type
- control types,support for Calendar
- control types,Calendar
ms.topic: article
ms.date: 05/31/2018
---

# Calendar Control Type

This topic provides information about Microsoft UI Automation support for the **Calendar** control type. A calendar control allows the user to easily determine the date and select other dates.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Calendar** control type. The UI Automation requirements apply to all calendar controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to calendar controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Calendar<ul><li>DataGrid<ul><li>Header (0 or 1)<ul><li>HeaderItem (0 or 7, quantity depends on how many days are displayed in columns)</li></ul></li><li>ListItem (quantity depends on how many days are displayed)</li><li>Button (0 or 2; for paging calendar view)</li></ul></li></ul></li></ul> | <ul><li>Calendar<ul><li>ListItem (quantity depends on how many days are displayed)</li></ul></li></ul> | 




 

Calendar controls can be represented in many different forms within the user interface. The only controls guaranteed to be in the control view of the UI Automation tree are the data grid, header, header item, and list item controls.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **Calendar** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value        | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes.   | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes.   | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes.   | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Calendar** | This value is the same for all UI frameworks.                                                                                                                                                        |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The calendar control is always included in the content view of the UI Automation tree.                                                                                                               |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE         | The calendar control is always included in the control view of the UI Automation tree.                                                                                                               |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes.   | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes.   | The value of this property should be the label of the document control. Typically, the title of the document is used.                                                                                |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes.   | Localized string corresponding to the **Calendar** control type. The default value is "calendar" for en-US or English (United States).                                                               |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes.   | The calendar control typically gets its name from the current date.                                                                                                                                  |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all calendar controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                        | Support/Value | Notes                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IGridProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-igridprovider)           | Required      | The calendar control always supports the [Grid](uiauto-implementinggrid.md) control pattern because the days within a month are items that can be navigated spatially.                                                                                                                                                        |
| [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider)       | Depends       | Most calendar controls support flipping the view by page. The [Scroll](uiauto-implementingscroll.md) control pattern is recommended in order to support paging navigation.                                                                                                                                                    |
| [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider) | Depends       | Most of calendar controls retain a specific day, month, or year as a selection of the subelement. Some calendars are multi-selectable and other only single-selectable. Calendar control with selectable subelements should support the [Selection](uiauto-implementingselection.md) control pattern.                         |
| [**ITableProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itableprovider)         | Required      | Because the calendar control always has a header within its subtree for the days of the week, the [Table](uiauto-implementingtable.md) control pattern must be supported.                                                                                                                                                     |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)         | No            | The [Value](uiauto-implementingvalue.md) control pattern is not necessary for calendar controls because the element cannot set the value directly on the control. If a specific date is associated with the control, the information should be provided by the [Selection](uiauto-implementingselection.md) control pattern. |



 

## Required Events

The following table lists the UI Automation events that calendar controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                           |                                                                                                                                                                                                              |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                      |                                                                                                                                                                                                              |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.                                                                                     |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.                                                                                   |
| [**UIA\_LayoutInvalidatedEventId**](uiauto-event-ids.md)                                                                     |                                                                                                                                                                                                              |
| [**UIA\_MultipleViewCurrentViewPropertyId**](uiauto-control-pattern-propids.md) property-changed event.             | If the control supports the [**CurrentView**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-imultipleviewprovider-get_currentview) property of the [MultipleView](uiauto-implementingmultipleview.md) control pattern, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                       |                                                                                                                                                                                                              |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.   | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                             |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event. | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                             |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.           | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                             |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event.     | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                             |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.       | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                             |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.               | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.                                                                                             |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md)                                                            |                                                                                                                                                                                                              |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




