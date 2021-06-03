---
title: ComboBox element
description: Represents a Combo Box control.
ms.assetid: d796e26b-44c2-4e11-b1a5-2ede5bcff676
keywords:
- ComboBox element Windows Ribbon
topic_type:
- apiref
api_name:
- ComboBox
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ComboBox element

Represents a [Combo Box](windowsribbon-controls-combobox.md) control.

## Usage

``` syntax
<ComboBox
  CommandName = "xs:positiveInteger or xs:string"
  IsEditable = "Boolean"
  ResizeType = "ComboBoxResizeType"
  IsAutoCompleteEnabled = "Boolean"/>
```

## Attributes



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CommandName</strong><br/></td>
<td>xs:positiveInteger or xs:string<br/></td>
<td>No<br/></td>
<td>Associates the element with a <a href="windowsribbon-element-command.md"><strong>Command</strong></a>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:positiveInteger or xs:string)<br/> </dt> <dd> A string, an integer value between 2 and 59999, inclusive, or a hexadecimal value between 0x2 and 0xea5f, inclusive. <br/> The value must be unique within the Ribbon XML document. <br/> Maximum length: 100 characters. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>IsAutoCompleteEnabled</strong><br/></td>
<td>Boolean<br/></td>
<td>No<br/></td>
<td>Restricted to one of the following values (0 and 1 are not valid):<br/> <br/>
<dt><span></span><span></span><strong></strong> (true)<br/> </dt> <dd> Default. <br/> </dd> <dt><span></span><span></span><strong></strong> (false)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>IsEditable</strong><br/></td>
<td>Boolean<br/></td>
<td>No<br/></td>
<td>Restricted to one of the following values (0 and 1 are not valid):<br/> <br/>
<dt><span></span><span></span><strong></strong> (true)<br/> </dt> <dd> Default. <br/> </dd> <dt><span></span><span></span><strong></strong> (false)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="even">
<td><strong>ResizeType</strong><br/></td>
<td>ComboBoxResizeType<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (NoResize)<br/> </dt> <dd> Default. <br/> </dd> <dt><span></span><span></span><strong></strong> (VerticalResize)<br/> </dt> <dd></dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="windowsribbon-element-controlgroup.md"><strong>ControlGroup</strong></a><br/></td>

</tr>
<tr class="even">
<td><a href="windowsribbon-element-dropdownbutton.md"><strong>DropDownButton</strong></a><br/></td>

</tr>
<tr class="odd">
<td><a href="windowsribbon-element-dropdowngallery.md"><strong>DropDownGallery</strong></a><br/></td>

</tr>
<tr class="even">
<td><a href="windowsribbon-element-group.md"><strong>Group</strong></a><br/></td>

</tr>
<tr class="odd">
<td><a href="windowsribbon-element-menugroup.md"><strong>MenuGroup</strong></a><br/></td>

</tr>
<tr class="even">
<td><a href="windowsribbon-element-quickaccesstoolbar-applicationdefaults.md"><strong>QuickAccessToolbar.ApplicationDefaults</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
Windows 8 and newer.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-element-splitbuttongallery.md"><strong>SplitButtonGallery</strong></a><br/></td>

</tr>
</tbody>
</table>



## Remarks

Optional.

May occur one or more times for each [**ControlGroup**](windowsribbon-element-controlgroup.md), [**DropDownButton**](windowsribbon-element-dropdownbutton.md), [**DropDownGallery**](windowsribbon-element-dropdowngallery.md), [**Group**](windowsribbon-element-group.md), [**MenuGroup**](windowsribbon-element-menugroup.md), or [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md) element.

Because the **ComboBox** is exclusively an item gallery, it does not support Command items. It is also the only gallery control that does not support a Command Space (a collection of Commands that are declared in markup and listed at the bottom of an item gallery or Command gallery). For more information, see [Working with Galleries](ribbon-controls-galleries.md).

The following screen shot illustrates a Ribbon [Combo Box](windowsribbon-controls-combobox.md) control from Windows Live Movie Maker.

![screen shot of a combobox control in the microsoft paint ribbon.](images/controls/combobox.png)

## Examples

The following examples demonstrate the basic markup for the **ComboBox**.

This section of code shows the **ComboBox** Command declarations, with an associated [**Group**](windowsribbon-element-group.md) that acts as the parent container for the **ComboBox** element.


```XML
<!-- ComboBox -->
<Command Name="cmdComboBoxGroup"
         Symbol="cmdComboBoxGroup"
         Comment="ComboBox Group"
         LabelTitle="ComboBox"/>
<Command Name="cmdComboBox"
         Symbol="cmdComboBox"
         Comment="ComboBox"
         LabelTitle="ComboBox"/>
```



This section of code shows the **ComboBox** control declarations.


```XML
<!-- ComboBox -->
<Group CommandName="cmdComboBoxGroup">
  <ComboBox CommandName="cmdComboBox">              
  </ComboBox>
</Group>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: Yes



## See also

<dl> <dt>

[Combo Box control](windowsribbon-controls-combobox.md)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

 

 





