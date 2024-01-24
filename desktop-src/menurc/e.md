---
title: E (Menus and Other Resources)
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 14e12ba3-8451-4a93-a555-e1c9e6040a67
ms.topic: article
ms.date: 05/31/2018
---

# E (Menus and Other Resources)

[A](a.md) [B](b.md) [C](c.md) D E [F](f.md) G H [I](i.md) J K L M [N](n.md) [O](o.md) P Q [R](r.md) S [T](t.md) [U](u.md) [V](v.md) [W](w.md) X Y Z

<dl> <dt>

<span id="tools.e_1_gly"></span><span id="TOOLS.E_1_GLY"></span>**Empty menus not allowed**
</dt> <dd>

An **END** keyword appears before any menu items are defined in the [**MENU**](menu-resource.md) statement. Empty menus are not permitted by Microsoft Windows 32 Resource Compiler (RC). Make sure that you do not have any opening quotation marks within the **MENU** statement.

</dd> <dt>

<span id="tools.e_2_gly"></span><span id="TOOLS.E_2_GLY"></span>**END expected in Dialog**
</dt> <dd>

The **END** keyword must appear at the end of a [**DIALOG**](dialog-resource.md) statement. Make sure that there are no opening quotation marks left from the preceding statement.

</dd> <dt>

<span id="tools.e_3_gly"></span><span id="TOOLS.E_3_GLY"></span>**END expected in menu**
</dt> <dd>

The **END** keyword must appear at the end of a [**MENU**](menu-resource.md) statement. Make sure that there are no mismatched **BEGIN** and **END** statements.

</dd> <dt>

<span id="tools.e_4_gly"></span><span id="TOOLS.E_4_GLY"></span>**Error Creatingresource-name**
</dt> <dd>

Microsoft Windows 32 Resource Compiler (RC) could not create the specified binary resource (.RES) file. Make sure that it is not being created on a read-only drive. Use the **/v** option to find out whether the file is being created.

</dd> <dt>

<span id="tools.e_5_gly"></span><span id="TOOLS.E_5_GLY"></span>**Expected Comma in Accelerator Table**
</dt> <dd>

Microsoft Windows 32 Resource Compiler (RC) requires a comma between the *event* and *idvalue* parameters in the [**ACCELERATORS**](accelerators-resource.md) statement.

</dd> <dt>

<span id="tools.e_6_gly"></span><span id="TOOLS.E_6_GLY"></span>**Expected control class name**
</dt> <dd>

The *class* parameter of a [**CONTROL**](control-control.md) statement in the [**DIALOG**](dialog-resource.md) statement must be one of the following control types: **BUTTON**, [**COMBOBOX**](combobox-control.md), **EDIT**, [**LISTBOX**](listbox-control.md), [**SCROLLBAR**](scrollbar-control.md), **STATIC**, or user-defined. Make sure that the class is spelled correctly.

</dd> <dt>

<span id="tools.e_7_gly"></span><span id="TOOLS.E_7_GLY"></span>**Expected font face name**
</dt> <dd>

The *typeface* parameter of the **FONT** statement in the [**DIALOG**](dialog-resource.md) statement must be a character string enclosed in double quotation marks ("). This parameter specifies the name of a font.

</dd> <dt>

<span id="tools.e_8_gly"></span><span id="TOOLS.E_8_GLY"></span>**Expected ID value for Menuitem**
</dt> <dd>

The [**MENU**](menu-resource.md) statement must contain a [**MENUITEM**](menuitem-statement.md) statement, which has either an integer or a symbolic constant in the *MenuID* parameter.

</dd> <dt>

<span id="tools.e_9_gly"></span><span id="TOOLS.E_9_GLY"></span>**Expected Menu String**
</dt> <dd>

Each [**MENUITEM**](menuitem-statement.md) and [**POPUP**](popup-resource.md) statement must contain a *text* parameter. This parameter is a string enclosed in double quotation marks (") that specifies the name of the menu item or pop-up menu. A **MENUITEM SEPARATOR** statement requires no quoted string.

</dd> <dt>

<span id="tools.e_10_gly"></span><span id="TOOLS.E_10_GLY"></span>**Expected numeric command value**
</dt> <dd>

Microsoft Windows Resource Compiler (RC) was expecting a numeric *idvalue* parameter in the [**ACCELERATORS**](accelerators-resource.md) statement. Make sure that you have used a [**\#define**](-define.md) statement to specify the value and that the constant used is spelled correctly.

</dd> <dt>

<span id="tools.e_11_gly"></span><span id="TOOLS.E_11_GLY"></span>**Expected numeric constant in string table**
</dt> <dd>

A numeric constant, defined in a [**\#define**](-define.md) statement, must immediately follow the **BEGIN** keyword in a [**STRINGTABLE**](stringtable-resource.md) statement.

</dd> <dt>

<span id="tools.e_12_gly"></span><span id="TOOLS.E_12_GLY"></span>**Expected numeric point size**
</dt> <dd>

The *pointsize* parameter of the [**FONT**](font-statement.md) statement in the [**DIALOG**](dialog-resource.md) statement must be an integer point-size value.

</dd> <dt>

<span id="tools.e_13_gly"></span><span id="TOOLS.E_13_GLY"></span>**Expected Numerical Dialog constant**
</dt> <dd>

A [**DIALOG**](dialog-resource.md) statement requires integer values for the *x*, *y*, *width*, and *height* parameters. Make sure that these values, which are included after the **DIALOG** keyword, are not negative.

</dd> <dt>

<span id="tools.e_14_gly"></span><span id="TOOLS.E_14_GLY"></span>**Expected String in STRINGTABLE**
</dt> <dd>

A string is expected after each numeric *stringid* parameter in a [**STRINGTABLE**](stringtable-resource.md) statement.

</dd> <dt>

<span id="tools.e_15_gly"></span><span id="TOOLS.E_15_GLY"></span>**Expected String or Constant Accelerator command**
</dt> <dd>

Microsoft Windows Resource Compiler (RC) was not able to determine which key was being set up for the accelerator. The *event* parameter in the [**ACCELERATORS**](accelerators-resource.md) statement might be invalid.

</dd> <dt>

<span id="tools.e_16_gly"></span><span id="TOOLS.E_16_GLY"></span>**Expected VALUE, BLOCK, or END keyword.**
</dt> <dd>

The [**VERSIONINFO**](versioninfo-resource.md) structure requires a **VALUE**, **BLOCK**, or **END** keyword.

</dd> <dt>

<span id="tools.e_17_gly"></span><span id="TOOLS.E_17_GLY"></span>**Expecting number for ID**
</dt> <dd>

A number is expected for the *id* parameter of a [**CONTROL**](control-control.md) statement in the [**DIALOG**](dialog-resource.md) statement. Make sure that you have a number or a [**\#define**](-define.md) statement for the control identifier.

</dd> <dt>

<span id="tools.e_18_gly"></span><span id="TOOLS.E_18_GLY"></span>**Expecting quoted string for key**
</dt> <dd>

The key string following the **BLOCK** or **VALUE** keyword should be enclosed in double quotation marks.

</dd> <dt>

<span id="tools.e_19_gly"></span><span id="TOOLS.E_19_GLY"></span>**Expecting quoted string in dialog class**
</dt> <dd>

The *class* parameter of the [**CLASS**](class-statement.md) statement in the [**DIALOG**](dialog-resource.md) statement must be an integer or a string enclosed in double quotation marks (").

</dd> <dt>

<span id="tools.e_20_gly"></span><span id="TOOLS.E_20_GLY"></span>**Expecting quoted string in dialog title**
</dt> <dd>

The *captiontext* parameter of the [**CAPTION**](caption-statement.md) statement in the [**DIALOG**](dialog-resource.md) statement must be a character string, enclosed in double quotation marks (").

</dd> </dl>

 

 




