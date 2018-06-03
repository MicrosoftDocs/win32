---
title: Button Control Type
description: This topic provides information about Microsoft UI Automation support for the Button control type.
ms.assetid: a2942067-461c-4281-80cf-385e3c08c874
keywords:
- UI Automation,support for Button control type
- UI Automation,Button control type
- UI Automation,tree structure for Button control type
- UI Automation,properties for Button control type
- UI Automation,control patterns for Button control type
- UI Automation,events for Button control type
- tree structures,Button control type
- properties,Button control type
- control patterns,Button control type
- events,Button control type
- support for Button control type
- Button control type
- control types,tree structure for Button control type
- control types,control patterns for Button control type
- control types,support for Button
- control types,Button
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Button Control Type

This topic provides information about Microsoft UI Automation support for the **Button** control type.

A button is an object that a user interacts with to perform an action such as the OK and Cancel buttons on a dialog box. The button control is a simple control to expose because it maps to a single command that the user wishes to complete.

The following sections define the required UI Automation tree structure, properties, control patterns, and events for the **Button** control type. The UI Automation requirements apply to all button controls where the UI framework/platform integrates UI Automation support for control types and control patterns.

This topic contains the following sections.

-   [Typical Tree Structure](#typical-tree-structure)
-   [Relevant Properties](#relevant-properties)
-   [Required Control Patterns](#required-control-patterns)
-   [Required Events](#required-events)
-   [Related topics](#related-topics)

## Typical Tree Structure

The following table depicts a typical control and content view of the UI Automation tree that pertains to button controls and describes what can be contained in each view. For more information about the UI Automation tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).



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
<li>Button
<ul>
<li>Image (0 or more)</li>
<li>Text (0 or more)</li>
</ul></li>
</ul></td>
<td><ul>
<li>Button</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Relevant Properties

The following table lists the UI Automation properties whose value or definition is especially relevant to the controls that implement the **Button** control type (such as button controls). For more information about UI Automation properties, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).



| UI Automation Property                                                                                              | Value      | Notes                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AcceleratorKeyPropertyId**](https://www.bing.com/search?q=**UIA\_AcceleratorKeyPropertyId**)             | See notes. | A button control typically supports an accelerator key to enable the end user to quickly perform the action represented by the button from the keyboard.                                             |
| [**UIA\_AutomationIdPropertyId**](https://www.bing.com/search?q=**UIA\_AutomationIdPropertyId**)                 | See notes. | The value of this property must be unique among all peer elements in the raw view of the UI Automation tree.                                                                                         |
| [**UIA\_BoundingRectanglePropertyId**](https://www.bing.com/search?q=**UIA\_BoundingRectanglePropertyId**)       | See notes. | The outermost rectangle that contains the whole control.                                                                                                                                             |
| [**UIA\_ClickablePointPropertyId**](https://www.bing.com/search?q=**UIA\_ClickablePointPropertyId**)             | See notes. | Supported if there is a bounding rectangle. If not every point within the bounding rectangle is clickable, and the element performs specialized hit testing, override and provide a clickable point. |
| [**UIA\_ControlTypePropertyId**](https://www.bing.com/search?q=**UIA\_ControlTypePropertyId**)                   | **Button** |                                                                                                                                                                                                      |
| [**UIA\_HelpTextPropertyId**](https://www.bing.com/search?q=**UIA\_HelpTextPropertyId**)                         | See notes. | The help text should indicate what the end result of activating the button will be. This is typically the same type of information presented through a tooltip.                                      |
| [**UIA\_IsContentElementPropertyId**](https://www.bing.com/search?q=**UIA\_IsContentElementPropertyId**)         | TRUE       | The button control must always be content.                                                                                                                                                           |
| [**UIA\_IsControlElementPropertyId**](https://www.bing.com/search?q=**UIA\_IsControlElementPropertyId**)         | TRUE       | The button control must always be a control.                                                                                                                                                         |
| [**UIA\_IsKeyboardFocusablePropertyId**](https://www.bing.com/search?q=**UIA\_IsKeyboardFocusablePropertyId**)   | See notes. | If the control can receive keyboard focus, it must support this property.                                                                                                                            |
| [**UIA\_LabeledByPropertyId**](https://www.bing.com/search?q=**UIA\_LabeledByPropertyId**)                       | Null       | Button controls are self-labeled by their contents.                                                                                                                                                  |
| [**UIA\_LocalizedControlTypePropertyId**](https://www.bing.com/search?q=**UIA\_LocalizedControlTypePropertyId**) | See notes. | Localized string corresponding to the **Button** control type. The default value is "button" for en-US or English (United States).                                                                   |
| [**UIA\_NamePropertyId**](https://www.bing.com/search?q=**UIA\_NamePropertyId**)                                 | See notes. | The name of the button control is the text used to label it. Whenever an image is used to label a button, alternate text must be supplied for the button's **Name** property.                        |



 

## Required Control Patterns

The following table lists the UI Automation control patterns required to be supported by all button controls. For more information on control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).



| Control Pattern/Pattern Property                                  | Support/Value | Notes                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IExpandCollapseProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iexpandcollapseprovider) | See notes.    | When a button is hosted as a child of a split button, the child button can support the [ExpandCollapse](uiauto-implementingexpandcollapse.md) control pattern instead of the [Invoke](uiauto-implementinginvoke.md) or [Toggle](uiauto-implementingtoggle.md) control pattern. The ExpandCollapse control pattern can be used for opening or closing a menu or other sub-structure associated with the button element. |
| [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider)                 | See notes.    | All buttons should support the [Invoke](uiauto-implementinginvoke.md) control pattern or the [Toggle](uiauto-implementingtoggle.md) control pattern but not both. The Invoke control pattern must be supported when the button performs a command at the request of the user. This command maps to a single operation such as Cut, Copy, Paste, or Delete.                                                              |
| [**IToggleProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-itoggleprovider)                 | See notes.    | All buttons should support the [Invoke](uiauto-implementinginvoke.md) control pattern or the [Toggle](uiauto-implementingtoggle.md) control pattern but not both. The Toggle control pattern must be supported if the button can cycle through a series of up to three states. Typically this is seen as an on/off switch for specific features.                                                                        |



 

## Required Events

The following table lists the UI Automation events that button controls are required to support. For more information on events, see [UI Automation Events Overview](uiauto-eventsoverview.md).



| UI Automation Event                                                                                                                   | Notes                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**UIA\_AutomationFocusChangedEventId**](https://www.bing.com/search?q=**UIA\_AutomationFocusChangedEventId**)                                      |                                                                                                                            |
| [**UIA\_BoundingRectanglePropertyId**](https://www.bing.com/search?q=**UIA\_BoundingRectanglePropertyId**) property-changed event. |                                                                                                                            |
| [**UIA\_Invoke\_InvokedEventId**](https://www.bing.com/search?q=**UIA\_Invoke\_InvokedEventId**)                                                     | If the control supports the [Invoke](uiauto-implementinginvoke.md) control pattern, it must support this event.           |
| [**UIA\_IsEnabledPropertyId**](https://www.bing.com/search?q=**UIA\_IsEnabledPropertyId**) property-changed event.                 | If the control supports the [**IsEnabled**](uiauto-automation-element-propids.md) property, it must support this event.   |
| [**UIA\_IsOffscreenPropertyId**](https://www.bing.com/search?q=**UIA\_IsOffscreenPropertyId**) property-changed event.             | If the control supports the [**IsOffscreen**](uiauto-automation-element-propids.md) property, it must support this event. |
| [**UIA\_NamePropertyId**](https://www.bing.com/search?q=**UIA\_NamePropertyId**) property-changed event.                           |                                                                                                                            |
| [**UIA\_StructureChangedEventId**](https://www.bing.com/search?q=**UIA\_StructureChangedEventId**)                                                  |                                                                                                                            |
| [**UIA\_ToggleToggleStatePropertyId**](https://www.bing.com/search?q=**UIA\_ToggleToggleStatePropertyId**) property-changed event.    | If the control supports the [Toggle](uiauto-implementingtoggle.md) control pattern, it must support this event.           |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Overview](uiauto-uiautomationoverview.md)
</dt> </dl>

 

 




