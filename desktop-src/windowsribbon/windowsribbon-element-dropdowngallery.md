---
title: DropDownGallery element
description: Represents a Drop-Down Gallery control with a gallery-based menu.
ms.assetid: fee6b3ad-fc84-49da-97da-2d53ff4dd0d8
keywords:
- DropDownGallery element Windows Ribbon
topic_type:
- apiref
api_name:
- DropDownGallery
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# DropDownGallery element

Represents a [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md) control with a gallery-based menu.

## Usage

``` syntax
<DropDownGallery
  ApplicationModes = "xs:string"
  CommandName = "xs:positiveInteger or xs:string"
  HasLargeItems = "Boolean"
  ItemHeight = "xs:integer"
  ItemWidth = "xs:integer"
  TextPosition = "TextPositionType"
  Type = "xs:string">
  child elements
</DropDownGallery>
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
<td>Valid only if <a href="windowsribbon-element-menugroup.md"><strong>MenuGroup</strong></a> is the parent element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string that contains a comma-separated list of integers between 0 and 31.<br/> White space is valid and ignored.<br/> Maximum length: 250 characters. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>CommandName</strong><br/></td>
<td>xs:positiveInteger or xs:string<br/></td>
<td>No<br/></td>
<td>Associates the element with a <a href="windowsribbon-element-command.md"><strong>Command</strong></a>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:positiveInteger or xs:string)<br/> </dt> <dd> A string, an integer value between 2 and 59999, inclusive, or a hexadecimal value between 0x2 and 0xea5f, inclusive. <br/> The value must be unique within the Ribbon XML document. <br/> Maximum length: 100 characters. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>HasLargeItems</strong><br/></td>
<td>Boolean<br/></td>
<td>No<br/></td>
<td>Determines whether the large or small image resource of the Command is displayed in the gallery control. <br/>
<blockquote>
[!Note]<br />
Applies only to galleries where the value of the <em>Type</em> attribute is equal to <code>Command</code>.
</blockquote>
<br/> Restricted to one of the following values (0 and 1 are not valid):<br/> <br/>
<dt><span></span><span></span><strong></strong> (true)<br/> </dt> <dd> Default. <br/> </dd> <dt><span></span><span></span><strong></strong> (false)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="even">
<td><strong>ItemHeight</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> The default is -1. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>ItemWidth</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> The default is -1. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>TextPosition</strong><br/></td>
<td>TextPositionType<br/></td>
<td>No<br/></td>
<td>Restricted to one of the following values:<br/> <br/>
<dt><span></span><span></span><strong></strong> (Bottom)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Hide)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Left)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Overlap)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Right)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Top)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>Type</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>Restricted to one of the following values:<br/> <br/>
<dt><span></span><span></span><strong></strong> (Items)<br/> </dt> <dd></dd> <dt><span></span><span></span><strong></strong> (Commands)<br/> </dt> <dd></dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements



| Element                                                                                           | Description                                        |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [**Button**](windowsribbon-element-button.md)<br/>                                         | May occur one or more times<br/> <br/> |
| [**CheckBox**](windowsribbon-element-checkbox.md)<br/>                                     | May occur one or more times<br/> <br/> |
| [**DropDownGallery.MenuGroups**](windowsribbon-element-dropdowngallery-menugroups.md)<br/> | Must occur exactly once<br/> <br/>     |
| [**DropDownGallery.MenuLayout**](windowsribbon-element-dropdowngallery-menulayout.md)<br/> | May occur at most once<br/> <br/>      |
| [**SplitButton**](windowsribbon-element-splitbutton.md)<br/>                               | May occur one or more times<br/> <br/> |
| [**ToggleButton**](windowsribbon-element-togglebutton.md)<br/>                             | May occur one or more times<br/> <br/> |



## Parent elements



<table>
<colgroup>
<col  />
<col  />
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
<td><a href="windowsribbon-element-group.md"><strong>Group</strong></a><br/></td>

</tr>
<tr class="odd">
<td><a href="windowsribbon-element-menugroup.md"><strong>MenuGroup</strong></a><br/></td>
<td>When contained in an <a href="windowsribbon-element-applicationmenu.md"><strong>ApplicationMenu</strong></a>. This element is only supported on the first level and must have no child elements.<br/> <br/></td>
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
<td><a href="windowsribbon-element-splitbutton.md"><strong>SplitButton</strong></a><br/></td>

</tr>
</tbody>
</table>



## Remarks

Optional.

May occur one or more times for each [**ControlGroup**](windowsribbon-element-controlgroup.md), [**DropDownButton**](windowsribbon-element-dropdownbutton.md), [**Group**](windowsribbon-element-group.md), [**MenuGroup**](windowsribbon-element-menugroup.md), or [**SplitButton**](windowsribbon-element-splitbutton.md) element.

**DropDownGallery** supports [application modes](ribbon-applicationmodes.md).

The following screen shot illustrates the Ribbon [Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md) control in Microsoft Paint for Windows 7.

![screen shot of a drop-down gallery control in microsoft paint for windows 7.](images/controls/dropdowngallery.png)

## Examples

The following example demonstrates the basic markup for the **DropDownGallery**.

This section of code shows the **DropDownGallery** Command declarations, with an associated [**Group**](windowsribbon-element-group.md) that acts as the parent container for the **DropDownGallery** element.


```XML
<!-- DropDownGallery -->
<Command Name="cmdDropDownGalleryGroup"
         Symbol="cmdDropDownGalleryGroup"
         Comment="DropDownGallery Group"
         LabelTitle="DropDownGallery"/>
<Command Name="cmdDropDownGallery"
         Symbol="cmdDropDownGallery"
         Comment="DropDownGallery"
         LabelTitle="DropDownGallery"/>
```



This section of code shows the **DropDownGallery** control declarations.


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
* **Can be empty**: No



## See also

<dl> <dt>

[**Drop-Down Gallery control**](windowsribbon-element-dropdowngallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[**SetModes**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

 

