---
title: FlowMenuLayout element
description: Represents a horizontal layout with line breaks for items in a gallery.
ms.assetid: 40c3a2e1-e58a-4d34-a237-b1bea116c82e
keywords:
- FlowMenuLayout element Windows Ribbon
topic_type:
- apiref
api_name:
- FlowMenuLayout
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# FlowMenuLayout element

Represents a horizontal layout with line breaks for items in a gallery.

## Usage

``` syntax
<FlowMenuLayout
  Rows = "xs:integer"
  Columns = "xs:integer"
  Gripper = "xs:string"/>
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
<td><strong>Columns</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the number of items to display in a single row.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> Any positive or negative integer. <br/> The default is <strong>2</strong>. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>Gripper</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>A resizing handle attached to the gallery drop down. <br/> <img src="images/controls/gripper.png" alt="Screen shot of a vertical gripper." /><br/> Restricted to one of the following values:<br/> <br/>
<dt><span></span><span></span><strong></strong> (None)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Vertical)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Corner)<br/> </dt> <dd> Default. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>Rows</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the number of item rows to be visible without scrolling. <br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> Any positive or negative integer. <br/> The default is <strong>-1</strong> which specifies to display as many item rows as possible.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



| Element                                                                                                 |
|---------------------------------------------------------------------------------------------------------|
| [**DropDownGallery.MenuLayout**](windowsribbon-element-dropdowngallery-menulayout.md)<br/>       |
| [**InRibbonGallery.MenuLayout**](windowsribbon-element-inribbongallery-menulayout.md)<br/>       |
| [**SplitButtonGallery.MenuLayout**](windowsribbon-element-splitbuttongallery-menulayout.md)<br/> |



## Remarks

Required.

Either the [**VerticalMenuLayout**](windowsribbon-element-verticalmenulayout.md) or the **FlowMenuLayout** element must occur one time for each [**DropDownGallery.MenuLayout**](windowsribbon-element-dropdowngallery-menulayout.md), [**InRibbonGallery.MenuLayout**](windowsribbon-element-inribbongallery-menulayout.md), or [**SplitButtonGallery.MenuLayout**](windowsribbon-element-splitbuttongallery-menulayout.md) element.

Elements are arranged according to the line-break properties inherent to the *row* and *column* attributes. When content exceeds the length of a single line, the menu breaks lines, wraps lines, and aligns content appropriately.

## Examples

The following example demonstrates the basic markup for the [**DropDownGallery**](windowsribbon-element-dropdowngallery.md).

This section of code shows the [**DropDownGallery.MenuLayout**](windowsribbon-element-dropdowngallery-menulayout.md) control declaration with a **FlowMenuLayout** specification.


```XML
<!-- DropDownGallery -->
<Group CommandName="cmdDropDownGalleryGroup">
  <DropDownGallery CommandName="cmdDropDownGallery"
                   TextPosition="Hide"
                   Type="Commands"
                   ItemHeight="32"
                   ItemWidth="32">
    <DropDownGallery.MenuLayout>
      <FlowMenuLayout Rows="2"
                      Columns="3"
                      Gripper="None"/>
    </DropDownGallery.MenuLayout>
    <DropDownGallery.MenuGroups>
      <MenuGroup>
        <Button CommandName="cmdButton1"></Button>
        <Button CommandName="cmdButton2"></Button>
       </MenuGroup>
       <MenuGroup>
        <Button CommandName="cmdButton3"></Button>
      </MenuGroup>
    </DropDownGallery.MenuGroups>
  </DropDownGallery>
</Group>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: Yes


 

 





