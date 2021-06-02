---
description: This control enables a user to change the selection state of features listed in the Feature table.
ms.assetid: 0daf5b44-ba07-47f1-95d9-28c59f7cf985
title: SelectionTree Control
ms.topic: article
ms.date: 05/31/2018
---

# SelectionTree Control

This control enables a user to change the selection state of features listed in the [Feature table](feature-table.md). The control is associated with a string valued property that the user can set by a [Browse dialog](browse-dialog.md). You can associate the control with a property by entering the property's name in the Property column of the [Control table](control-table.md).

The SelectionTree control automatically publishes the following [Control Events](control-events.md) on Windows XP or earlier operating systems. The SelectionTree control publishes these events when the selected item is changed from one node to another. If the selection tree has no nodes, the control publishes these events and erases the contents of controls that subscribe to the event. These ControlEvents are not required to be listed in the [ControlEvent table](controlevent-table.md).



| Control event                                                 | Description                                                                                        |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [SelectionAction](selectionaction-controlevent.md)           | Publishes a string from the [UIText table](uitext-table.md) describing the highlighted item.      |
| [SelectionBrowse](selectionbrowse-controlevent.md)           | Generates a Browse dialog box used to modify the path of the highlighted item.                     |
| [SelectionDescription](selectiondescription-controlevent.md) | Publishes a string from the [Feature table](feature-table.md) describing the highlighted item.    |
| [SelectionNoItems](selectionnoitems-controlevent.md)         | Deletes the descriptive text or disables the buttons of an obsolete item.                          |
| [SelectionPath](selectionpath-controlevent.md)               | Publishes the path for the highlighted item.                                                       |
| [SelectionPathOn](selectionpathon-controlevent.md)           | Publishes whether or not there is a selection path associated with the currently selected feature. |
| [SelectionSize](selectionsize-controlevent.md)               | Publishes the size of the highlighted item.                                                        |



 

Beginning with the Windows Server 2003 systems, SelectionTree controls publish all of the events in the above table, and in addition, publish a [DoAction ControlEvent](doaction-controlevent.md) or a [SetProperty ControlEvent](setproperty-controlevent.md). Records must be added to the [ControlEvent table](controlevent-table.md) to publish DoAction or SetProperty ControlEvents.



| Control event                               | Description                                        |
|---------------------------------------------|----------------------------------------------------|
| [DoAction](doaction-controlevent.md)       | Notifies the installer to execute a custom action. |
| [SetProperty](setproperty-controlevent.md) | Sets a property to a new value.                    |



 

Beginning with Windows Installer version 3.0, SelectionTree controls publish an event that runs [custom actions](custom-actions.md) listed in the [ControlEvent table](controlevent-table.md). The SelectionTree control publishes this event whenever the feature selection changes in the control or whenever a different selection state is chosen for the current feature. The custom actions run each time the event is published. The SelectionTree control sends information to the custom action by setting the values of the following properties. All these properties are all cleared when the SelectionTree control is closed.

**Windows Installer 2.0:** Not supported. The SelectionTree control does not publish the event and does not set the following properties.



| Property                                | Description                                                                                                                                                      |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MsiSelectionTreeSelectedFeature         | The selected feature's name in the Feature field of the [Feature table](feature-table.md).                                                                      |
| MsiSelectionTreeSelectedAction          | The selected feature's installation action state. The value may be INSTALLSTATE\_ABSENT, INSTALLSTATE\_LOCAL, INSTALLSTATE\_SOURCE, or INSTALLSTATE\_ADVERTISED. |
| MsiSelectonTreeChildrenCount            | Number of direct child nodes.                                                                                                                                    |
| MsiSelectionTreeInstallingChildrenCount | Number of direct child nodes that are INSTALLSTATE\_LOCAL, INSTALLSTATE\_SOURCE, or INSTALLSTATE\_ADVERTISED.                                                    |
| MsiSelectionTreeSelectedCost            | Cost of installing the selected feature in units of 512 bytes.                                                                                                   |
| MsiSelectionTreeChildrenCost            | Cost of installing all the children features in units of 512 bytes.                                                                                              |
| MsiSelectionTreeSelectedPath            | Path where the selected feature is being installed. Defined only if the feature is being installed as INSTALLSTATE\_LOCAL.                                       |



 

> [!Note]
>
> The contents of the Text field of the [Control table](control-table.md) is never displayed by the SelectionTree control. Instead this field specifies the style of text to be displayed by the control and contains a description of the control used by screen review utilities. To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&*style*}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font is used. The information following this is read by screen review utilities as the description of the control. See [Accessibility](accessibility.md).

 

## Control Attributes

You can use the following attributes with this control. To change the value of an attribute using an event, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md) and list the attribute's identifier in the Attribute column. Enter the identifier of the ControlEvent in the Event column.



| Attribute identifier                                               | Hexadecimal bit                  | Description                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IndirectPropertyName](indirectpropertyname-control-attribute.md) |                                  | Name of an indirect property associated with the control. If the Indirect attribute bit is set, the control displays or changes the value of the property having this name. If the Indirect attribute bit is set, this name is also the value of the property listed in the Property column of the [Control table](control-table.md).                                    |
| [Position](position-control-attribute.md)                         |                                  | Position of the control in the dialog box. Enter the control's width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control table](control-table.md). Use [installer units](installer-units.md) for length and distance.<br/>                                                                             |
| [PropertyName](propertyname-control-attribute.md)                 |                                  | Name of the property associated with this control. If the Indirect attribute bit is not set, the control displays or changes the value of the property having this name. This attribute is specified in the Property column of the [Control table](control-table.md).                                                                                                    |
| [PropertyValue](propertyvalue-control-attribute.md)               |                                  | Current value of the property displayed or changed by this control. If the Indirect attribute bit is not set, this is the value of PropertyName. If the Indirect attribute bit is set, this is the value of IndirectPropertyName. If the attribute changes, the control reflects the new value.                                                                           |
| [Text](text-control-attribute.md)                                 |                                  | Displays text in screenreaders according to text entered into the Text column of the [Control table](control-table.md). See [Accessibility](accessibility.md).                                                                                                                                                                                                          |
| [Visible](visible-control-attribute.md)                           | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control table](control-table.md) to make the control visible or hidden upon its creation.<br/> You can also hide or show a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                     |
| [Enabled](enabled-control-attribute.md)                           | 0x00000000 0x00000002<br/> | Control in a disabled state. Control in an enabled state.<br/> Include this bit in the bit word in the Attributes column of the [Control](control-table.md) to enable the control on creation.<br/> You can also enable or disable a control by using the [ControlCondition table](controlcondition-table.md).<br/>                                   |
| [Sunken](sunken-control-attribute.md)                             | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3D, look.<br/> Include these bits in the bit word in the Attributes column of the [Control table](control-table.md).<br/>                                                                                                                                                             |
| [Indirect](indirect-control-attribute.md)                         | 0x00000000 0x00000008<br/> | The control displays or changes the value of the property in the Property column of the [Control table](control-table.md). The control displays or changes the value of the property that has the Identifier listed in the Property column of the Control table.<br/> Determines if the property associated with this control is referenced indirectly.<br/> |
| [RTLRO](rtlro-control-attribute.md)                               | 0x00000000 0x00000020<br/> | Text in the control is displayed in left-to-right reading order. Text in the control is displayed in right-to-left reading order.<br/>                                                                                                                                                                                                                              |
| [RightAligned](rightaligned-control-attribute.md)                 | 0x00000000 0x00000040<br/> | Text in the control is aligned to the left. Text in the control is aligned to the right.<br/>                                                                                                                                                                                                                                                                       |
| [LeftScroll](leftscroll-control-attribute.md)                     | 0x00000000 0x00000080<br/> | The scroll bar is located on the right side of the control. The scroll bar is located on the left side of the control.<br/>                                                                                                                                                                                                                                         |
| [BiDi](bidi-control-attribute.md)                                 | 0x000000E0                       | Set this value for a combination of the [RTLRO](rtlro-control-attribute.md), [RightAligned](rightaligned-control-attribute.md), and [LeftScroll](leftscroll-control-attribute.md) attributes.                                                                                                                                                                          |



 

## Remarks

This control can be created from the WC\_TREEVIEW class by using the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. It has the **WS\_BORDER**, **TVS\_HASLINES**, **TVS\_HASBUTTONS**, **TVS\_LINESATROOT**, **TVS\_DISABLEDRAGDROP**, **TVS\_SHOWSELALWAYS**, **WS\_CHILD**, **WS\_TABSTOP**, and **WS\_GROUP** styles.

The selection tree is only populated if the [CostInitialize action](costinitialize-action.md) and [CostFinalize action](costfinalize-action.md) have been called.

The following string in the [UIText table](uitext-table.md) is related to this control.



| Term                                                                                                         | Description                                                    |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="AbsentPath"></span><span id="absentpath"></span><span id="ABSENTPATH"></span>AbsentPath<br/> | The path displayed for an item in the absent state.<br/> |



 

The following six strings are used to display the number of children selected and the size associated with the highlighted item:

-   SelChildCostPos
-   SelChildCostNeg
-   SelParentCostPosPos
-   SelParentCostPosNeg
-   SelParentCostNegPos
-   SelParentCostNegNeg

The following strings are used to display the available selection options for an item in a popup menu:

-   MenuAbsent
-   MenuLocal
-   MenuCD
-   MenuNetwork
-   MenuAllLocal
-   MenuAllCD
-   MenuAllNetwork

The following strings are used to explain the present selection in the [SelectionDescription](selectiondescription-controlevent.md) ControlEvent.

-   SelAbsentAbsent
-   SelAbsentLocal
-   SelAbsentCD
-   SelAbsentNetwork
-   SelLocalAbsent
-   SelLocalLocal
-   SelLocalCD
-   SelLocalNetwork
-   SelCDAbsent
-   SelNetworkAbsent
-   SelCDLocal
-   SelNetworkLocal
-   SelCDCD
-   SelNetworkNetwork

The following four localized strings are used in formatting the size of a file:

-   Bytes
-   KB
-   MB
-   GB

 

 
