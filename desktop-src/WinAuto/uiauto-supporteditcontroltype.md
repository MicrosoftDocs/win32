---
title: Edit Control Type
description: This topic provides information about Microsoft UI Automation support for the Edit control type.
ms.assetid: ec45ec5e-4faa-4635-8726-5bbe1f20b843
keywords:
- UI Automation,support for Edit control type
- UI Automation,Edit control type
- UI Automation,tree structure for Edit control type
- UI Automation,properties for Edit control type
- UI Automation,control patterns for Edit control type
- UI Automation,events for Edit control type
- tree structures,Edit control type
- properties,Edit control type
- control patterns,Edit control type
- events,Edit control type
- support for Edit control type
- Edit control type
- control types,tree structure for Edit control type
- control types,control patterns for Edit control type
- control types,support for Edit
- control types,Edit
ms.topic: article
ms.date: 05/31/2018
---

# Edit Control Type

This topic provides information about Microsoft UI Automation support for the **Edit** control type.

Edit controls enable a user to view and edit a simple line of text without rich formatting support.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the edit control type. The UI Automation requirements apply to all edit controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Remarks](#remarks)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to edit controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>Edit</li></ul> | <ul><li>Edit</li></ul> | 




 

The controls that implement the **Edit** control type will always have zero scroll bars in the control view of the UI Automation tree because it is a single-line control. The single line of text may wrap in some layout scenarios. The **Edit** control type is only meant for small amounts of text.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the edit controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | The edit control must have a clickable point that gives input focus to the edit portion of the control when a user clicks the mouse there.                                                                                                                                           |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | **Edit**   |                                                                                                                                                                                                                                                                                      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**   | The edit control is always included in the content view of the UI Automation tree.                                                                                                                                                                                                   |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | **TRUE**   | The edit control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                   |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                            |
| [**UIA\_IsPasswordPropertyId**](uiauto-automation-element-propids.md)                     | See notes. | Must be set to **TRUE** on edit controls that contain passwords. If an edit control does contain Password contents then this property can be used by a screen reader to determine whether keystrokes should be read out as the user types them.                                      |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes. | If there is a static text label associated with the control, this property must expose a reference to that control. If the text control is a subcomponent of another control, it will not have a **LabeledBy** property set.                                                         |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **Edit** control type. The default value is "edit" for en-US or English (United States).                                                                                                                                                       |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The name of the edit control is typically generated from a static text label. If there is not a static text label, a property value for **Name** must be assigned by the application developer. The **Name** property should never contain the textual contents of the edit control. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by edit controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                              | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IRangeValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irangevalueprovider)     | Depends       | All edit controls that take a numeric range must expose the [RangeValue](uiauto-implementingrangevalue.md) control pattern.                                                                                                                                                                                                                                                                                       |
| [**Minimum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_minimum)         | See notes.    | This property must be the smallest value to which the contents of the edit control can be set.                                                                                                                                                                                                                                                                                                                     |
| [**Maximum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_maximum)         | See notes.    | This property must be the largest value to which the contents of the edit control can be set.                                                                                                                                                                                                                                                                                                                      |
| [**SmallChange**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_smallchange) | See notes.    | This property must indicate the number of decimal places that the value can be set to. If the edit control only takes integers, the **SmallChange** property value must be 1. If the edit control takes a range from 1.0 to 2.0, then the **SmallChange** property value must be 0.1. If the edit control takes a range from 1.00 to 2.00 then the **SmallChange** property value must be 0.001.                   |
| [**LargeChange**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_largechange) | **NULL**      | This property does not need to be exposed on an edit control.                                                                                                                                                                                                                                                                                                                                                      |
| [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_value)             | See notes.    | This property indicates the numeric contents of the edit control. When a more precise value is set by a UI Automation client within the ranges specified in the [**Minimum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_minimum) and [**Maximum**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_maximum) properties, the [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irangevalueprovider-get_value) property is automatically rounded to the closest accepted value. |
| [**ITextProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itextprovider)                 | Required      | All edit controls must support the [Text](uiauto-implementingtextandtextrange.md) control pattern because detailed information must always be available for assistive technology clients.                                                                                                                                                                                                                     |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)               | Depends       | All edit controls that take a string must expose the [Value](uiauto-implementingvalue.md) control pattern.                                                                                                                                                                                                                                                                                                        |
| [**IsReadOnly**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_isreadonly)        | See notes.    | This property must be set to indicate whether the control can have a value set programmatically, or that can be edited by the user.                                                                                                                                                                                                                                                                                |
| [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_value)                  | See notes.    | This property contains the textual contents of the edit control. If the [**UIA\_IsPasswordPropertyId**](uiauto-automation-element-propids.md) property is set to **TRUE**, querying the [**Value**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-ivalueprovider-get_value) property must return an error.                                                                                                                      |



 

## Required Events

The following table lists the UI Automation events that edit controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                           |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                      |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md) property-changed event.                                                |                                                                                                                            |
| [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                             | If the control supports the [RangeValue](uiauto-implementingrangevalue.md) control pattern, it must support this event.   |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.   | An edit control never supports the [Scroll](uiauto-implementingscroll.md) control pattern.                                |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event. | An edit control never supports the [Scroll](uiauto-implementingscroll.md) control pattern.                                |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.           | An edit control never supports the [Scroll](uiauto-implementingscroll.md) control pattern.                                |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md) property-changed event.       | An edit control never supports the [Scroll](uiauto-implementingscroll.md) control pattern.                                |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md) property-changed event.     | An edit control never supports the [Scroll](uiauto-implementingscroll.md) control pattern.                                |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md) property-changed event.               | An edit control never supports the [Scroll](uiauto-implementingscroll.md) control pattern.                                |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                       |                                                                                                                            |
| [**UIA\_Text\_TextChangedEventId**](uiauto-event-ids.md)                                                                      | If the control supports the [Text](uiauto-implementingtextandtextrange.md) control pattern, it must support this event.   |
| [**UIA\_Text\_TextSelectionChangedEventId**](uiauto-event-ids.md)                                                    | If the control supports the [Text](uiauto-implementingtextandtextrange.md) control pattern, it must support this event.   |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event .                                      | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.             |



 

## Remarks

An edit control can be used as a read-only text field that does not support the selection or editing of text. Such an edit control behaves as a field object that has a specific name and value.

If an edit control contains placeholder text (for example, a cue banner), the text should be used as the **HelpText** property unless the text can be edited by the user and then reused as placeholder text. For example, the Windows Internet Explorer address bar contains the text "about:Tabs" when a new tab is opened. This is not **HelpText** because it is a programmatic address that can be used or edited by the user.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




