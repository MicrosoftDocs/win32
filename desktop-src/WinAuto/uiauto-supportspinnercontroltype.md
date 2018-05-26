---
title: Spinner Control Type
description: This topic provides information about Microsoft UI Automation support for the Spinner control type.
ms.assetid: 28673ad5-645d-4314-96c4-81a951226256
keywords:
- UI Automation,support for Spinner control type
- UI Automation,Spinner control type
- UI Automation,tree structure for Spinner control type
- UI Automation,properties for Spinner control type
- UI Automation,control patterns for Spinner control type
- UI Automation,events for Spinner control type
- tree structures,Spinner control type
- properties,Spinner control type
- control patterns,Spinner control type
- events,Spinner control type
- support for Spinner control type
- Spinner control type
- control types,tree structure for Spinner control type
- control types,control patterns for Spinner control type
- control types,support for Spinner
- control types,Spinner
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Spinner Control Type

This topic provides information about Microsoft UI Automation support for the **Spinner** control type.

Spinner controls are used to select from a domain of items or a range of numbers.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Spinner** control type. The UI Automation requirements apply to all spinner controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertain to spinner controls when they support the **RangeValue** and **Selection** control patterns and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).

**RangeValue control pattern**



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Control View</th>
<th>Content View</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>Spinner
<ul>
<li>Edit (0 or 1)</li>
<li>Button (2)</li>
</ul></li>
</ul></td>
<td><ul>
<li>Spinner</li>
</ul></td>
</tr>
</tbody>
</table>



 

**Selection control pattern**



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Control View</th>
<th>Content View</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li>Spinner
<ul>
<li>Edit (0 or 1)</li>
<li>Button (2)</li>
<li>List Item (0 or more)</li>
</ul></li>
</ul></td>
<td><ul>
<li>Spinner
<ul>
<li>ListItem (0 or more)</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

To ensure that the two buttons in the control view subtree can be distinguished by automated test tools, assign the **ScrollAmount\_SmallIncrement** or [**ScrollAmount\_SmallDecrement**](uiauto-scrollamount.md#scrollamount-smalldecrement) value to the **AutomationId** property as appropriate. For some implementations, the associated edit control may be a peer of the spinner control.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to spinner controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value       | Notes                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md#uia-automationidpropertyid)                 | See notes.  | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                               |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)       | See notes.  | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                   |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)             | See notes.  | The spinner control's clickable point gives focus to the edit portion of the control.                                                                                                                                                                                                                                      |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md#uia-controltypepropertyid)                   | **Spinner** | This value is the same for all frameworks.                                                                                                                                                                                                                                                                                 |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)         | TRUE        | The spinner control must always be content.                                                                                                                                                                                                                                                                                |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)         | TRUE        | The spinner control must always be a control.                                                                                                                                                                                                                                                                              |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)   | See notes.  | If the control can receive keyboard focus, it must support this property. A spinner control rarely takes the focus, but when it does, the focus should remain on the spinner control itself, not on the child buttons. The user should be able to perform all scrolling actions by using the UP ARROW and DOWN ARROW keys. |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md#uia-labeledbypropertyid)                       | See notes.  | Spinner controls have a static text label.                                                                                                                                                                                                                                                                                 |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid) | See notes.  | Localized string corresponding to the **Spinner** control type. The default value is "spinner" for en-US or English (United States).                                                                                                                                                                                       |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)                                 | See notes.  | The spinner control typically gets its name from a static text label.                                                                                                                                                                                                                                                      |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all spinner controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                         | Support/Value | Notes                                                                                                                                     |
|--------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**IRangeValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-irangevalueprovider?branch=master)                | Depends       | Spinner controls that span a numeric range can support the [RangeValue](uiauto-implementingrangevalue.md) control pattern.               |
| [**ISelectionProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iselectionprovider?branch=master)                  | Depends       | Spinner controls that have a list of items to be selected must support the [Selection](uiauto-implementingselection.md) control pattern. |
| [**CanSelectMultiple**](/windows/win32/UIAutomationCore/nf-uiautomationcore-iselectionprovider-get_canselectmultiple?branch=master) | FALSE         | Spinner controls are always single selection containers.                                                                                  |
| [**IValueProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-ivalueprovider?branch=master)                          | Depends       | Spinner controls that span a descrete set of options or numbers can support the [Value](uiauto-implementingvalue.md) control pattern.    |



 

## Required Events

The following table lists the UI Automation events that spinner controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md#uia-automationfocuschangedeventid)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md#uia-rangevaluevaluepropertyid) property-changed event.        | If the control supports the [RangeValue](uiauto-implementingrangevalue.md) control pattern, it must support this event.   |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md#uia-selection-invalidatedeventid) property-changed event.               | If the control supports the [Selection](uiauto-implementingselection.md) control pattern, it must support this event.     |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md#uia-structurechangedeventid)                                                  |                                                                                                                            |
| [**UIA\_ValueValuePropertyId**](uiauto-control-pattern-propids.md#uia-valuevaluepropertyid) property-changed event.                  | If the control supports the [Value](uiauto-implementingvalue.md) control pattern, it must support this event.             |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




