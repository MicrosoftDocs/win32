---
description: For each password that must be entered by the user, add an edit control on a dialog that stores the value of the password into a property.
ms.assetid: aa4ff8b8-cbbb-4b18-83b3-279e52d9f6d3
title: Authoring the User Interface for Password Input
ms.topic: article
ms.date: 05/31/2018
---

# Authoring the User Interface for Password Input

For each password that must be entered by the user, add an edit control on a dialog that stores the value of the password into a property. This [edit control](edit-control.md) should have the [Password Control Attribute](password-control-attribute.md). This specifies that the property entered is a password and prevents the installer from writing the property to the log file.

The [control attributes](control-attributes.md) for the password edit control are msidbControlAttributesVisible, msidbControlAttributesEnabled, and msidbControlAttributesPasswordInput (1 + 2 + 2097152). The X, Y, Width, Height, and Control\_Next depend on the layout of the control on the dialog.

[Control Table](control-table.md)



| Dialog\_ | Control\_            | Type | X   | Y   | Width | Height | Attributes | Property         | Text | Control\_Next | Help |
|----------|----------------------|------|-----|-----|-------|--------|------------|------------------|------|---------------|------|
| MyDialog | TestUserPasswordEdit | Edit | 25  | 120 | 300   | 20     | 2097155    | TESTUSERPASSWORD |      | Cancel        |      |



 

Continue to [Securing the installation](securing-the-installation.md).

 

 



