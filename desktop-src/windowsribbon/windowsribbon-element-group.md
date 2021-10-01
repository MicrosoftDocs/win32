---
title: Group element
description: Represents a Group control that functions as a container for a group of elements.
ms.assetid: b0d3fcda-7165-40f4-9e57-c7ab88b31711
keywords:
- Group element Windows Ribbon
topic_type:
- apiref
api_name:
- Group
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Group element

Represents a [Group](windowsribbon-controls-group.md) control that functions as a container for a group of elements.

## Usage

``` syntax
<Group
  SizeDefinition = "xs:string"
  ApplicationModes = "xs:string"
  CommandName = "xs:positiveInteger or xs:string">
  child elements
</Group>
```

## Attributes



<table>
<colgroup>
<col  />
<col  />
<col  />
<col  />
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
<td><strong>ApplicationModes</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string that contains a comma-separated list of integers between 0 and 31.<br/> White space is valid and ignored.<br/> Maximum length: 250 characters. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>CommandName</strong><br/></td>
<td>xs:positiveInteger or xs:string<br/></td>
<td>No<br/></td>
<td>Associates the element with a <a href="windowsribbon-element-command.md"><strong>Command</strong></a>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:positiveInteger or xs:string)<br/> </dt> <dd> A string, an integer value between 2 and 59999, inclusive, or a hexadecimal value between 0x2 and 0xea5f, inclusive. <br/> The value must be unique within the Ribbon XML document. <br/> Maximum length: 100 characters. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>SizeDefinition</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>When specified, the value of <em>SizeDefinition</em> is constrained to one of the <a href="windowsribbon-templates.md">layout templates</a> defined by the Ribbon framework. <br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> Any sequence of zero or more characters.<br/> The maximum length is unbounded.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements



| Element                                                                             | Description                                        |
|-------------------------------------------------------------------------------------|----------------------------------------------------|
| [**Button**](windowsribbon-element-button.md)<br/>                           | May occur one or more times<br/> <br/> |
| [**CheckBox**](windowsribbon-element-checkbox.md)<br/>                       | May occur one or more times<br/> <br/> |
| [**ComboBox**](windowsribbon-element-combobox.md)<br/>                       | May occur one or more times<br/> <br/> |
| [**ControlGroup**](windowsribbon-element-controlgroup.md)<br/>               | May occur one or more times<br/> <br/> |
| [**DropDownButton**](windowsribbon-element-dropdownbutton.md)<br/>           | May occur one or more times<br/> <br/> |
| [**DropDownColorPicker**](windowsribbon-element-dropdowncolorpicker.md)<br/> | May occur one or more times<br/> <br/> |
| [**DropDownGallery**](windowsribbon-element-dropdowngallery.md)<br/>         | May occur one or more times<br/> <br/> |
| [**FontControl**](windowsribbon-element-fontcontrol.md)<br/>                 | May occur at most once<br/> <br/>      |
| [**InRibbonGallery**](windowsribbon-element-inribbongallery.md)<br/>         | May occur one or more times<br/> <br/> |
| [**SizeDefinition**](windowsribbon-element-sizedefinition.md)<br/>           | May occur at most once<br/> <br/>      |
| [**Spinner**](windowsribbon-element-spinner.md)<br/>                         | May occur one or more times<br/> <br/> |
| [**SplitButton**](windowsribbon-element-splitbutton.md)<br/>                 | May occur one or more times<br/> <br/> |
| [**SplitButtonGallery**](windowsribbon-element-splitbuttongallery.md)<br/>   | May occur one or more times<br/> <br/> |
| [**ToggleButton**](windowsribbon-element-togglebutton.md)<br/>               | May occur one or more times<br/> <br/> |



## Parent elements



| Element                                             |
|-----------------------------------------------------|
| [**Tab**](windowsribbon-element-tab.md)<br/> |



## Remarks

Optional.

May occur one or more times for each [**Tab**](windowsribbon-element-tab.md) element.

[**Tab**](windowsribbon-element-tab.md) supports [application modes](ribbon-applicationmodes.md).

The Ribbon markup is valid only when the child elements of **Group** correspond to the template specified for *SizeDefinition*.

## Examples

The following code example illustrates the use of a custom template in a **Group**.


```
<Group CommandName="cmdCustomGroup1" SizeDefinition="CustomTemplate">
  <Button CommandName="cmdCommand1" />
</Group>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: No



## See also

<dl> <dt>

[Customizing a Ribbon Through Size Definitions and Scaling Policies](windowsribbon-templates.md)
</dt> <dt>

[Group control](windowsribbon-controls-group.md)
</dt> <dt>

[**SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes)
</dt> </dl>

 

