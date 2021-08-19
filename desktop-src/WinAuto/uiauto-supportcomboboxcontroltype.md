---
title: ComboBox Control Type
description: This topic provides information about Microsoft UI Automation support for the ComboBox control type.
ms.assetid: e7c64dc1-e1e3-4f99-adde-d0d63eb6c4c9
keywords:
- UI Automation,support for ComboBox control type
- UI Automation,ComboBox control type
- UI Automation,tree structure for ComboBox control type
- UI Automation,properties for ComboBox control type
- UI Automation,control patterns for ComboBox control type
- UI Automation,events for ComboBox control type
- tree structures,ComboBox control type
- properties,ComboBox control type
- control patterns,ComboBox control type
- events,ComboBox control type
- support for ComboBox control type
- ComboBox control type
- control types,tree structure for ComboBox control type
- control types,control patterns for ComboBox control type
- control types,support for ComboBox
- control types,ComboBox
ms.topic: article
ms.date: 05/31/2018
---

# ComboBox Control Type

This topic provides information about Microsoft UI Automation support for the **ComboBox** control type.

A combo box is a list box combined with a static control or an edit control that displays the currently selected item in the list box portion of the combo box. The list box portion of the control is displayed at all times or only appears when the user selects the drop-down arrow (which is a push button) next to the control. If the selection field is an edit control, the user can enter information that is not in the list; otherwise, the user can only select items in the list.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **ComboBox** control type. The UI Automation requirements apply to all combo box controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to combo box controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).




| Control View | Content View | 
|--------------|--------------|
| <ul><li>ComboBox<ul><li>Edit (0 or 1)</li><li>List (0 or 1)</li><li>List Item (child of List; 0 to many)</li><li>Button (1)</li></ul></li></ul> | <ul><li>ComboBox<ul><li>List Item (0 to many)</li></ul></li></ul> | 




 

The edit control in the control view of the combo box is necessary only if the combo box can be edited to take any input, as is the case of the combo box in the **Run** dialog box.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **ComboBox** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                     |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                         |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)             | See notes. | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point.                                                                                                             |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md)                   | ComboBox   |                                                                                                                                                                                                                                                                                                                  |
| [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md)                         | See notes. | The help text for combo box controls should explain why the user is being asked choose an option from the combo box. The text is similar to information presented through a tooltip. For example, "Select an item to set the display resolution of your monitor."                                                |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | Combo box controls are always included in the content view of the UI Automation tree.                                                                                                                                                                                                                            |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md)         | TRUE       | Combo box controls are always included in the control view of the UI Automation tree.                                                                                                                                                                                                                            |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)   | TRUE       | Combo box controls can receive keyboard focus; however, when a UI Automation client sets focus to a combo box, any item in the combo box subtree can receive the focus.                                                                                                                                          |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md)                       | See notes. | Combo box controls typically have a static text label that this property references.                                                                                                                                                                                                                             |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md) | See notes. | Localized string corresponding to the **ComboBox** control type. The default value is "combo box" for en-US or English (United States).                                                                                                                                                                          |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)                                 | See notes. | The name of the combo box control is typically generated from a static text label. If there is not a static text label, you must assign a value for the **Name** property. The **Name** property should never contain the current contents of the combo box or change when the contents of the combo box change. |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all combo box controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                   | Support  | Notes                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | Required | The [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern must be supported because a combo box control must always contain a drop-down button.                                                                                                                                                                                |
| [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider)           | Depends  | Displays the current selection in the combo box. Support for the [Selection](uiauto-implementingselection.md) control pattern is delegated to the list box beneath the combo box, but may not always be feasible.                                                                                                                               |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)                   | Depends  | If the combo box can take arbitrary text values, the [Value](uiauto-implementingvalue.md) control pattern must be supported. This pattern enables the string contents of the combo box to be set programmatically. If the Value control pattern is not supported, the user must select from the list items within the subtree of the combo box. |
| [**IScrollProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iscrollprovider)                 | Never    | The [Scroll](uiauto-implementingscroll.md) control pattern is never supported directly on a combo box. It is supported if a list box contained within a combo box can scroll, and only when the list box is visible on the screen.                                                                                                              |



 

## Required Events

The following table lists the UI Automation events that combo box controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                                | Notes                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md)                                                                   |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md) property-changed event.                              |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                              | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md) property-changed event.                                          | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md)                                                                               |                                                                                                                            |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md) property-changed event. |                                                                                                                            |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md) property-changed event.                                               | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.             |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




