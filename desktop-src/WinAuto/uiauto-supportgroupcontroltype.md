---
title: Group Control Type
description: This topic provides information about Microsoft UI Automation support for the Group control type.
ms.assetid: f8363c2f-dbff-43a3-831f-d30151829ef9
keywords:
- UI Automation,support for Group control type
- UI Automation,Group control type
- UI Automation,tree structure for Group control type
- UI Automation,properties for Group control type
- UI Automation,control patterns for Group control type
- UI Automation,events for Group control type
- tree structures,Group control type
- properties,Group control type
- control patterns,Group control type
- events,Group control type
- support for Group control type
- Group control type
- control types,tree structure for Group control type
- control types,control patterns for Group control type
- control types,support for Group
- control types,Group
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Group Control Type

This topic provides information about Microsoft UI Automation support for the **Group** control type.

A group control represents a node within a hierarchy. The **Group** control type creates a separation in the UI Automation tree so items that are grouped together have a logical division within the UI Automation tree.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Group** control type. The UI Automation requirements apply to all group controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to group controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>Group
<ul>
<li>0 or many controls</li>
</ul></li>
</ul></td>
<td><ul>
<li>Group
<ul>
<li>0 or many controls</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

Group controls typically include UI Automation support for control types found below them in the subtree, including the [ListItem](uiauto-supportlistitemcontroltype.md), [TreeItem](uiauto-supporttreeitemcontroltype.md), and [DataItem](uiauto-supportdataitemcontroltype.md) control types. Because a group control is a generic container, it is possible for any type of control to be under the group control in the tree.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the group controls. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md#uia-automationidpropertyid)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)             | See notes. | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md#uia-controltypepropertyid)                   | **Group**  |                                                                                                                                                                                                      |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)         | **TRUE**   | The group control is always included in the content view of the UI Automation tree.                                                                                                                  |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)         | **TRUE**   | The group control is always included in the control view of the UI Automation tree.                                                                                                                  |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md#uia-labeledbypropertyid)                       | See notes. | Group controls are typically self-labeling. In these cases, return **NULL**. If the group has a static text label, return the label as the value of the **LabeledBy** property.                      |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid) | See notes. | Localized string corresponding to the **Group** control type. The default value is "group" for en-US or English (United States).                                                                     |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)                                 | See notes. | The group control typically gets its name from the text that labels the control.                                                                                                                     |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported for the **Group** control type. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern                                                   | Support | Notes                                                                                                                                                 |
|-------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider?branch=master) | Depends | Group controls that can be used to show or hide information must support the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern. |



 

## Required Events

The following table lists the UI Automation events that group controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                                | Notes                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md#uia-automationfocuschangedeventid)                                                                   |                                                                                                                                                  |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event.                              |                                                                                                                                                  |
| [**UIA\_ExpandCollapseExpandCollapseStatePropertyId**](uiauto-control-pattern-propids.md#uia-expandcollapseexpandcollapsestatepropertyid) property-changed event. | If the control supports the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern control pattern, it must support this event. |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                                              | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.                         |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.                                          | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.                       |
| [**UIA\_ToggleToggleStatePropertyId**](uiauto-control-pattern-propids.md#uia-toggletogglestatepropertyid) property-changed event.                                 | If the control supports the [Toggle](uiauto-implementingtoggle.md) control pattern, it must support this event.                                 |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md#uia-structurechangedeventid)                                                                               |                                                                                                                                                  |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




