---
description: Controls and text placed on dialog boxes and billboards enable the user to interact with the installation process.
ms.assetid: 2c6204c7-535d-4dda-8394-723ddbf46b96
title: Adding Controls and Text
ms.topic: article
ms.date: 05/31/2018
---

# Adding Controls and Text

Controls and text placed on dialog boxes and billboards enable the user to interact with the installation process. Add a dialog box to the user interface by including it in the [Dialog table](dialog-table.md) as described in [Using the User Interface](using-the-user-interface.md). Fill dialog boxes and billboards with controls by populating the [Control table](control-table.md) and [BBControl table](bbcontrol-table.md), respectively.

The initial attributes of control can be specified in the Attributes column of the [Control table](control-table.md). See [Control Attributes](control-attributes.md).

To make control attributes dependent upon a condition, use the [ControlCondition table](controlcondition-table.md) to disable, enable, hide, or show a control according to the value of a property or conditional statement. You can also use this table to override the specification of the default control entered into the [Dialog table](dialog-table.md).

To have an event change a control attribute, subscribe the control to a ControlEvent in the [EventMapping table](eventmapping-table.md). A ControlEvent specifies an action to be taken by the installer or a change in the attributes of one or more controls in the dialog box. See [ControlEvent Overview](controlevent-overview.md). Enter the attribute's identifier in the Attribute column and the ControlEvent's identifier in the Event column of the [EventMapping table](eventmapping-table.md).

Some controls facilitate the collection of information from the user. For example, a check box enables the user to set the value of a property. See the [CheckBox table](checkbox-table.md), the [ComboBox table](combobox-table.md), the [ListBox table](listbox-table.md), the [RadioButton table](radiobutton-table.md), and the [ListView table](listview-table.md).

Note that for security reasons, private properties cannot be changed by the user interacting with the user interface. If a property is to be set by the user interface it needs to be a public property and have a name in all upper case. See [About Properties](about-properties.md).

You can either make your dialog box present information to the user or write it to a log in response to installation actions by filling in the [ActionText table](actiontext-table.md).

Controls can have a predefined font style. To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&*style*}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font will be used.

It is recommended that the [**DefaultUIFont**](defaultuifont.md) property of every installation package with a UI be set in the [Property table](property-table.md) to one of the predefined styles listed in the [TextStyle table](textstyle-table.md). If this property is not specified, the installer uses the System font. This can cause the installer to improperly display text strings if the package's code page is different from the user's default UI code page.

For most controls, text is displayed using the character set that is specified by the code page of the database. This ensures that the correct character set is used with the information contained in the database. The exceptions to this are the [Edit](edit-control.md), [DirectoryList](directorylist-control.md), [PathEdit](pathedit-control.md), and [DirectoryCombo](directorycombo-control.md) controls, which always display text using the user's default UI character set. The [Text](text-control.md), [ListBox](listbox-control.md), and [ComboBox](combobox-control.md) controls use the user's default UI character set if the [UsersLanguage Control Attribute](userslanguage-control-attribute.md) is set.

In some cases a control may be redrawn incorrectly when canceling out of a dialog box. This has to do with the order in which the controls receive WM\_PAINT messages after the **Cancel** dialog box is removed. To fix this, try changing the order of the controls in the Control table.

Controls should be made large enough to accommodate the entire text viewed at all font size settings. Controls should be made large enough to accommodate the entire localized text, if the text in the UI may be localized. Larger font sizes or localized text can require more space than the original text and can become truncated by a control that is made too small. For more information about localizing UI text see the section: [A Localization Example](a-localization-example.md).

 

 



