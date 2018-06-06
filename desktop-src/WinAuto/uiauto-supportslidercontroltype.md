---
title: Slider Control Type
description: This topic provides information about Microsoft UI Automation support for the Slider control type.
ms.assetid: dc7bef7a-b68c-4184-a9e7-745bb41b592e
keywords:
- UI Automation,support for Slider control type
- UI Automation,Slider control type
- UI Automation,tree structure for Slider control type
- UI Automation,properties for Slider control type
- UI Automation,control patterns for Slider control type
- UI Automation,events for Slider control type
- tree structures,Slider control type
- properties,Slider control type
- control patterns,Slider control type
- events,Slider control type
- support for Slider control type
- Slider control type
- control types,tree structure for Slider control type
- control types,control patterns for Slider control type
- control types,support for Slider
- control types,Slider
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Slider Control Type

This topic provides information about Microsoft UI Automation support for the **Slider** control type.

A slider control is a composite control with buttons that enable a user to set a numerical range or select from a set of items.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Slider** control type. The UI Automation requirements apply to all slider controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to slider controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>Slider
<ul>
<li>Button (2 or 4)</li>
<li>Thumb (1)</li>
<li>List Item (0 or more)</li>
</ul></li>
</ul></td>
<td><ul>
<li>Slider
<ul>
<li>List Item (0 or more)</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to slider controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md#uia-automationidpropertyid)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                   |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                       |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)             | See notes. | The majority of slider controls must return the [**UIA\_E\_NOCLICKABLEPOINT**](uiauto-error-codes.md#uia-e-noclickablepoint) error because the entire bounding rectangle of the slider control is occupied by child controls. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md#uia-controltypepropertyid)                   | **Slider** | This value is the same for all frameworks.                                                                                                                                                                                     |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)         | TRUE       | The slider control is always included in the content view of the UI Automation tree.                                                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)         | TRUE       | The slider control is always included in the control view of the UI Automation tree.                                                                                                                                           |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)   | See notes. | If the control can receive keyboard focus, it must support this property. The children (buttons and thumb) of a slider control should never take the focus. The focus should always remain on the slider control itself.       |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md#uia-labeledbypropertyid)                       | See notes. | If there is a static text label associated with the control, this property must expose a reference to that control. If the text control is a subcomponent of another control, it will not have a **LabeledBy** property set.   |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid) | See notes. | Localized string corresponding to the **Slider** control type. The default value is "slider" for en-US or English (United States).                                                                                             |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)                                 | See notes. | The name of the slider control is typically generated from a static text label. If there is not a static text label, a property value for **Name** must be assigned by the application developer.                              |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all slider controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                          | Support/Value | Notes                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IRangeValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irangevalueprovider) | Depends       | A slider should support the [RangeValue](uiauto-implementingrangevalue.md) control pattern if the content can be set to a value within a numerical range.                                                                                                                                                 |
| [**ISelectionProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iselectionprovider)   | Depends       | A slider should support the [Selection](uiauto-implementingselection.md) control pattern if the content represents one value among a discrete set of options. When the Selection control pattern is supported, the corresponding selection must be exposed as one or more child list items of the slider. |
| [**IValueProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-ivalueprovider)           | Depends       | A slider should support the [Value](uiauto-implementingvalue.md) control pattern if the content represents one value among a discrete set of options.                                                                                                                                                     |



 

## Required Events

The following table lists the UI Automation events that slider controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md#uia-automationfocuschangedeventid)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event. |                                                                                                                            |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_RangeValueValuePropertyId**](uiauto-control-pattern-propids.md#uia-rangevaluevaluepropertyid) property-changed event.        | If the control supports the [RangeValue](uiauto-implementingrangevalue.md) control pattern, it must support this event.   |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md#uia-selection-invalidatedeventid)                                       | If the control supports the [Selection](uiauto-implementingselection.md) control pattern, it must support this event.     |
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

 

 




