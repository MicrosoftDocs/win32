---
title: List Control Type
description: This topic provides information about Microsoft UI Automation support for the List control type.
ms.assetid: 'e4cde080-32d1-4150-a6be-8bd750e972c9'
keywords: ["UI Automation,support for List control type", "UI Automation,List control type", "UI Automation,tree structure for List control type", "UI Automation,properties for List control type", "UI Automation,control patterns for List control type", "UI Automation,events for List control type", "tree structures,List control type", "properties,List control type", "control patterns,List control type", "events,List control type", "support for List control type", "List control type", "control types,tree structure for List control type", "control types,control patterns for List control type", "control types,support for List", "control types,List"]
---

# List Control Type

This topic provides information about Microsoft UI Automation support for the **List** control type.

The **List** control type provides a way to organize a flat group or groups of items and allows a user to select one or more of those items. The **List** control type has a loose restriction on what types of child elements it may contain. This enables UI Automation providers to support a well-known element for selection containers.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **List** control type. The UI Automation requirements apply to all list controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns and Properties](#required-control-patterns-and-properties)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to list controls, and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<td>Contains the elements that correspond to controls.</td>
<td>Removes redundant information from the tree so that assistive technologies work with the smallest set of information that is meaningful to the end user.</td>
</tr>
<tr class="even">
<td><ul>
<li>List
<ul>
<li>DataItem (0 or more)</li>
<li>ListItem (0 or more)</li>
<li>Group (0 or more)</li>
<li>ScrollBar (0, 1 or 2)</li>
</ul></li>
</ul></td>
<td><ul>
<li>List
<ul>
<li>DataItem (0 or more)</li>
<li>ListItem (0 or more)</li>
<li>Group (0 or more)</li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>



 

The control view for a control that implements the List control type (such as a list control) consists of:

-   Zero or more items within the list control (items can be based on the [ListItem](uiauto-supportlistitemcontroltype.md) or [DataItem](uiauto-supportdataitemcontroltype.md) control types)
-   Zero or more group controls within a list control
-   Zero, one, or two scroll bar controls

The content view of a control that implements the List control type (such as a list control) consists of:

-   Zero or more items within the list control (items can be based on the [ListItem](uiauto-supportlistitemcontroltype.md) or [DataItem](uiauto-supportdataitemcontroltype.md) control types)
-   Zero or more groups within the list control

A list control must not have items that have a hierarchical relationship other than being grouped together. If the items have children in the UI Automation tree, then the list container should be based on the [Tree](uiauto-supporttreecontroltype.md) control type.

The selectable items within the list control will be available from the descendants in the UI Automation tree of the list control. All items within the list control must belong to the same selection group. The selectable items in the list should be exposed as [ListItem](uiauto-supportlistitemcontroltype.md) (instead of [DataItem](uiauto-supportdataitemcontroltype.md)) control types.

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the **List** control type. For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationIdPropertyId**](uiauto-automation-element-propids.md#uia-automationidpropertyid)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md#uia-clickablepointpropertyid)             | See notes. | If the list control has a clickable point (a point that can be clicked to cause the list to take focus), that point must be exposed through this property. If the value of the [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property is **TRUE**, attempting to retrieve this property results in the [**UIA\_E\_NOCLICKABLEPOINT**](uiauto-error-codes.md#uia-e-noclickablepoint) error.                      |
| [**UIA\_ControlTypePropertyId**](uiauto-automation-element-propids.md#uia-controltypepropertyid)                   | **List**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**UIA\_HelpTextPropertyId**](uiauto-automation-element-propids.md#uia-helptextpropertyid)                         | See notes. | The Help text for list controls should explain why the user is being asked to make a choice from a list of options. For example, "Selection an item from this list will set the display resolution for your monitor."                                                                                                                                                                                                                                                |
| [**UIA\_IsContentElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontentelementpropertyid)         | **TRUE**   | The list control is always included in the content view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                                                   |
| [**UIA\_IsControlElementPropertyId**](uiauto-automation-element-propids.md#uia-iscontrolelementpropertyid)         | **TRUE**   | The list control is always included in the control view of the UI Automation tree.                                                                                                                                                                                                                                                                                                                                                                                   |
| [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md#uia-iskeyboardfocusablepropertyid)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                                                                                                                                                                                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](uiauto-automation-element-propids.md#uia-labeledbypropertyid)                       | See notes. | If there is a static text label then this property must expose a reference to that control.                                                                                                                                                                                                                                                                                                                                                                          |
| [**UIA\_LocalizedControlTypePropertyId**](uiauto-automation-element-propids.md#uia-localizedcontroltypepropertyid) | See notes. | Localized string corresponding to the **List** control type. The default value is "list" for en-US or English (United States).                                                                                                                                                                                                                                                                                                                                       |
| [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md#uia-namepropertyid)                                 | See notes. | The value of a list control's **Name** property should convey the category of options that the user is being asked to select from. This property typically gets its name from a static text label. If there is not a static text label the application developer must expose a value for the **Name** property.<br/> The only time this property is not required for list controls is if the control is used within the subtree of another control.<br/> |



 

## Required Control Patterns and Properties

The following table lists the UI Automation control patterns required to be supported by all list controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                             | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IGridProvider**](uiauto-igridprovider.md)                                | Depends       | Implement the [Grid](uiauto-implementinggrid.md) control pattern when grid navigation needs to be available on an item by item basis.                                                                                                                                                                                                                                           |
| [**IMultipleViewProvider**](uiauto-imultipleviewprovider.md)                | Depends       | Implement the [MultipleView](uiauto-implementingmultipleview.md) control pattern if the control can support multiple views of the items in the container.                                                                                                                                                                                                                       |
| [**IScrollProvider**](uiauto-iscrollprovider.md)                            | Depends       | Implement the [Scroll](uiauto-implementingscroll.md) control pattern if items in the container are scrollable.                                                                                                                                                                                                                                                                  |
| [**ISelectionProvider**](uiauto-iselectionprovider.md)                      | Depends       | If a control supports the List control type that supports selection, the control must implement the [Selection](uiauto-implementingselection.md) control pattern when a selection state is maintained between the items contained in the control. If the items within the control are not selectable, the [Group](uiauto-supportgroupcontroltype.md) control type can be used. |
| [**CanSelectMultiple**](uiauto-iselectionprovider-canselectmultiple.md)     | Depends       | List controls can be single or multiple-selection containers.                                                                                                                                                                                                                                                                                                                    |
| [**IsSelectionRequired**](uiauto-iselectionprovider-isselectionrequired.md) | Depends       | List controls do not always require that an item be selected.                                                                                                                                                                                                                                                                                                                    |
| [**ITableProvider**](uiauto-itableprovider.md)                              | Never         | The [Table](uiauto-implementingtable.md) control pattern is never supported for the **List** control type. If the control needs to support this control pattern, the control should be based on the [DataGrid](uiauto-supportdatagridcontroltype.md) control type.                                                                                                             |



 

## Required Events

The following table lists the UI Automation events that list controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                                        | Notes                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](uiauto-event-ids.md#uia-automationfocuschangedeventid)                                                           |                                                                                                                              |
| [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md#uia-boundingrectanglepropertyid) property-changed event.                      |                                                                                                                              |
| [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md#uia-isenabledpropertyid) property-changed event.                                      | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.     |
| [**UIA\_IsOffscreenPropertyId**](uiauto-automation-element-propids.md#uia-isoffscreenpropertyid) property-changed event.                                  | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_LayoutInvalidatedEventId**](uiauto-event-ids.md#uia-layoutinvalidatedeventid)                                                                     | If the layout of child items can be changed, the control must support this event.                                            |
| [**UIA\_MultipleViewCurrentViewPropertyId**](uiauto-control-pattern-propids.md#uia-multipleviewcurrentviewpropertyid) property-changed event.             | If the control supports the [MultipleView](uiauto-implementingmultipleview.md) control pattern, it must support this event. |
| [**UIA\_ScrollHorizontallyScrollablePropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontallyscrollablepropertyid) property-changed event.   | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.             |
| [**UIA\_ScrollHorizontalScrollPercentPropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontalscrollpercentpropertyid) property-changed event. | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.             |
| [**UIA\_ScrollHorizontalViewSizePropertyId**](uiauto-control-pattern-propids.md#uia-scrollhorizontalviewsizepropertyid) property-changed event.           | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.             |
| [**UIA\_ScrollVerticalScrollPercentPropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticalscrollpercentpropertyid) property-changed event.     | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.             |
| [**UIA\_ScrollVerticallyScrollablePropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticallyscrollablepropertyid) property-changed event.       | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.             |
| [**UIA\_ScrollVerticalViewSizePropertyId**](uiauto-control-pattern-propids.md#uia-scrollverticalviewsizepropertyid) property-changed event.               | If the control supports the [Scroll](uiauto-implementingscroll.md) control pattern, it must support this event.             |
| [**UIA\_Selection\_InvalidatedEventId**](uiauto-event-ids.md#uia-selection-invalidatedeventid)                                                            | If the control supports the [Selection](uiauto-implementingselection.md) control pattern, it must support this event.       |
| [**UIA\_StructureChangedEventId**](uiauto-event-ids.md#uia-structurechangedeventid)                                                                       |                                                                                                                              |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 





