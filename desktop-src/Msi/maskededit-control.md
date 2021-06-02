---
description: The MaskedEdit Control is an edit field control that contains a mask in the text field of the control. You can associate the control with a string value property by entering the property name into the Property column of the Control Table.
ms.assetid: 8cc14683-3dbb-404f-87af-09a5f5b90b19
title: MaskedEdit Control
ms.topic: article
ms.date: 05/31/2018
---

# MaskedEdit Control

The MaskedEdit Control is an edit field control that contains a mask in the text field of the control. You can associate the control with a string value property by entering the property name into the Property column of the [Control Table](control-table.md).

You can use the MaskedEdit Control to create a template for user entry of information such as a telephone number or Product ID code. For example, the [**PIDKEY**](pidkey.md) Property can be entered by the user through a MaskedEdit Control that is specified by setting the [**PIDTemplate**](pidtemplate.md) Property to a string like the following:

12345<\#\#\# -%%%%%%%>@@@@@

The string defines the masking template for the entry of the [**PIDKEY**](pidkey.md) Property by the user. The visible segment of the string is enclosed by a pair of bracket (<>) characters.

The following table identified the syntax of the mask.



| Character | Meaning                                                                                                                                                                                                                                                                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <      | The left end of the visible segment of the template. This character and everything to its left are hidden in the user interface. There should be no more than one instance of this character in the template.                                                                               |
| >      | The right end of the visible segment of the template. This character and everything to its right are hidden in the user interface. This character is replaced by a dash during validation. If there is a visible segment begins with <, then it must be terminated with a matching >. |
| \#        | This character can be a digit (numeral.)                                                                                                                                                                                                                                                    |
| %         | This character can be an alternate digit (numeral) that enables the mask to control the way a custom action differentiates fields.                                                                                                                                                          |
| @         | This character can be a random digit (numeral.) This character should not appear in the visible part of the template.                                                                                                                                                                       |
| &         | This character can be any character.                                                                                                                                                                                                                                                        |
| ^         | This character can be an alternate character that enables the mask to control the way a custom action differentiates fields.                                                                                                                                                                |
| ?         | This character can be an alternate character that enables the mask to control the way a custom action differentiates fields.                                                                                                                                                                |
| \`        | Grave accent marks \` (ASCII value 96) can represent an alternate character that enables the mask to control the way a custom action differentiates fields.                                                                                                                                 |
| \_        | This character is a literal underscore character.                                                                                                                                                                                                                                           |
| =         | This character is the field terminator. This must follow a \#, %, ^, or \`. This creates one more input position of the same type as the preceding positions and terminates the field with a '-' separator.                                                                                 |



 

Any other character is treated as a literal constant.

For characters that can be edited, the control creates separate edit windows with one window for each block of contiguous characters of the same kind.

## Control Attributes

To change the value of an attribute that is using an event, subscribe the control to a Control event in the [EventMapping Table](eventmapping-table.md) and list the attribute identifier in the Attribute column. Enter the identifier of the Control event in the Event column. You can use the following attributes with the MaskedEdit Control.



| Attribute                                                          | Hexadecimal Bit                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IndirectPropertyName](indirectpropertyname-control-attribute.md) |                                  | This is the name of an indirect property that is associated with the control. If the indirect attribute bit is set, the control displays or changes the value of the property that has this name. If the indirect attribute bit is set, this name is also the value of the property that is listed in the Property column of the [Control Table](control-table.md).                                                                                                                                   |
| [Position](position-control-attribute.md)                         |                                  | Position of the control in the dialog box. Enter the control width, height, and coordinates of the control's left corner into the Width, Height, X, and Y columns of the [Control Table](control-table.md). Use [Installer Units](installer-units.md) for length and distance.<br/>                                                                                                                                                                                                            |
| [PropertyName](propertyname-control-attribute.md)                 |                                  | This is the name of the property that is associated with this control. If the indirect attribute bit is not set, the control displays or changes the value of the property that has this name. This attribute is specified in the Property column of the [Control Table](control-table.md).                                                                                                                                                                                                           |
| [PropertyValue](propertyvalue-control-attribute.md)               |                                  | Current value of the property that is displayed or changed by this control. If the indirect attribute bit is not set, this is the value of PropertyName. If the indirect attribute bit is set, this is the value of IndirectPropertyName. If the attribute changes, the control reflects the new value.                                                                                                                                                                                                |
| [Text](text-control-attribute.md)                                 |                                  | To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&style}. Where style is an identifier listed in the Style column of the [TextStyle Table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) Property is defined as a valid text style, that font is used. The string that specifies the masking template follows this prefix and uses the syntax described previously in this topic. |
| [Visible](visible-control-attribute.md)                           | 0x00000000 0x00000001<br/> | Hidden control. Visible control.<br/> Include this bit in the bit word of the Attributes column in the [Control Table](control-table.md) to make the control visible or hidden when it is created.<br/> You can also hide or show a control by using the [ControlCondition Table](controlcondition-table.md).<br/>                                                                                                                                                                 |
| [Enabled](enabled-control-attribute.md)                           | 0x00000000 0x00000002<br/> | Control in a disabled state. Control in an enabled state.<br/> Include this bit in the bit word in the Attributes column of the [Control Table](control-table.md) to enable the control on creation.<br/> You can also enable or disable a control by using the [ControlCondition Table](controlcondition-table.md).<br/>                                                                                                                                                          |
| [Sunken](sunken-control-attribute.md)                             | 0x00000000 0x00000004<br/> | Displays the default visual style. Displays the control with a sunken, 3-D look.<br/> Include these bits in the bit word in the Attributes column of the [Control Table](control-table.md).<br/>                                                                                                                                                                                                                                                                                          |
| [Indirect](indirect-control-attribute.md)                         | 0x00000000 0x00000008<br/> | The control displays or changes the value of the property in the Property column of the [Control Table](control-table.md). The control displays or changes the value of the property that has the identifier listed in the Property column of the [Control Table](control-table.md).<br/> Determines if the property that is associated with this control is referenced indirectly.<br/>                                                                                                 |



 

## Remarks

The MaskedEdit Control creates one parent window of the **BUTTON** class with the **BS\_OWNERDRAW** and **WS\_EX\_CONTROLPARENT** styles. It creates several child windows to this window.

-   For constant text parts, it creates STATIC windows with the **SS\_LEFT** and **WS\_CHILD** styles.
-   For editable fields, it creates an EDIT window with the **WS\_CHILD**, **WS\_BORDER**, and **WS\_TABSTOP** styles.
-   For numeric fields, the window also has the **ES\_NUMBER** style.

The alternate digit, %, and alternate alphanumeric characters, ^, ?, and \` fields allow custom actions to differentiate between fields in a way that can be controlled by the mask, for example, ^ can be used for fields that should be uppercase.

 

 




