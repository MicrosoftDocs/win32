---
title: InRibbonGallery element
description: Represents the In-Ribbon Gallery, a gallery-based control that exposes a default subset of items directly in the Ribbon. Any remaining items are displayed when a drop-down menu button is clicked.
ms.assetid: 07d035e2-e6db-49fa-b786-a37cbceb58f6
keywords:
- InRibbonGallery element Windows Ribbon
topic_type:
- apiref
api_name:
- InRibbonGallery
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# InRibbonGallery element

Represents the [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md), a gallery-based control that exposes a default subset of items directly in the Ribbon. Any remaining items are displayed when a drop-down menu button is clicked.

## Usage

``` syntax
<InRibbonGallery
  CommandName = "xs:positiveInteger or xs:string"
  HasLargeItems = "Boolean"
  ItemHeight = "xs:integer"
  ItemWidth = "xs:integer"
  MinColumnsLarge = "xs:integer"
  MaxColumnsMedium = "xs:integer"
  MinColumnsMedium = "xs:integer"
  MaxColumns = "xs:integer"
  MaxRows = "xs:integer"
  TextPosition = "TextPositionType"
  Type = "xs:string">
  child elements
</InRibbonGallery>
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
<tr class="odd">
<td><strong>ItemHeight</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Together with <em>ItemWidth</em>, determines the size of the item image that is displayed in the gallery control. <br/>
<blockquote>
[!Note]<br />
Applies only to galleries where the value of the <em>Type</em> attribute is equal to <code>Item</code>.
</blockquote>
<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> The default is -1. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>ItemWidth</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Together with <em>ItemHeight</em>, determines the size of the item image that is displayed in the gallery control. <br/>
<blockquote>
[!Note]<br />
Applies only to galleries where the value of the <em>Type</em> attribute is equal to <code>Item</code>.
</blockquote>
<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> The default is -1. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>MaxColumns</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the maximum number of columns that the <strong>InRibbonGallery</strong> displays, for example, in the <em>Large</em> group layout drop-down.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="even">
<td><strong>MaxColumnsMedium</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the maximum number of columns that the <strong>InRibbonGallery</strong> displays in the <em>Medium</em> group layout, before switching to <em>Large</em> layout. <br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>MaxRows</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the maximum number of rows for the layout of <strong>InRibbonGallery</strong> items. <br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd> The default is 1. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>MinColumnsLarge</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the minimum number of columns that the <strong>InRibbonGallery</strong> displays in the <em>Large</em> group layout, before switching to <em>Medium</em>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>MinColumnsMedium</strong><br/></td>
<td>xs:integer<br/></td>
<td>No<br/></td>
<td>Specifies the minimum number of columns that the <strong>InRibbonGallery</strong> displays in the <em>Medium</em> group layout, before switching to <em>Small</em>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:integer)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="even">
<td><strong>TextPosition</strong><br/></td>
<td>TextPositionType<br/></td>
<td>No<br/></td>
<td>Specifies where the item label is displayed, relative to the image. <br/> Restricted to one of the following values:<br/> <br/>
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
| [**CheckBox**](windowsribbon-element-checkbox.md)<br/>                                     | May occur one or more times<br/> <br/> |
| [**InRibbonGallery.MenuGroups**](windowsribbon-element-inribbongallery-menugroups.md)<br/> | Must occur exactly once<br/> <br/>     |
| [**InRibbonGallery.MenuLayout**](windowsribbon-element-inribbongallery-menulayout.md)<br/> | May occur at most once<br/> <br/>      |
| [**Button**](windowsribbon-element-button.md)<br/>                                       | May occur one or more times<br/> <br/> |
| [**SplitButton**](windowsribbon-element-splitbutton.md)<br/>                               | May occur one or more times<br/> <br/> |
| [**ToggleButton**](windowsribbon-element-togglebutton.md)<br/>                             | May occur one or more times<br/> <br/> |



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
<td><a href="windowsribbon-element-group.md"><strong>Group</strong></a><br/></td>

</tr>
<tr class="odd">
<td><a href="windowsribbon-element-quickaccesstoolbar-applicationdefaults.md"><strong>QuickAccessToolbar.ApplicationDefaults</strong></a><br/></td>
<td><blockquote>
[!Note]<br />
Windows 8 and newer.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



## Remarks

Optional.

May occur at most once for each [**ControlGroup**](windowsribbon-element-controlgroup.md) or [**Group**](windowsribbon-element-group.md) element.

The following screen shot illustrates the Ribbon [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md) control in Microsoft Paint for Windows 7.

![screen shot of an in-ribbon gallery control in the microsoft paint ribbon.](images/controls/inribbongallery.png)

## Examples

The following example demonstrates the basic markup for an [In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md).

This section of code shows the **InRibbonGallery** Command declarations, with an associated [**Group**](windowsribbon-element-group.md) that acts as the parent container for the **InRibbonGallery** element.


```XML
<!-- InRibbonGallery -->
<Command Name="cmdInRibbonGalleryGroup"
         Symbol="cmdInRibbonGalleryGroup"
         Comment="InRibbonGallery Group"
         LabelTitle="InRibbonGallery"/>
<Command Name="cmdInRibbonGallery"
         Symbol="cmdInRibbonGallery"
         Comment="InRibbonGallery"
         LabelTitle="InRibbonGallery"/>
```



This section of code shows the **InRibbonGallery** control declarations.


```XML
<!-- InRibbonGallery -->
<Group CommandName="cmdInRibbonGalleryGroup" SizeDefinition="OneInRibbonGallery">
  <InRibbonGallery CommandName="cmdInRibbonGallery"
                   MaxColumns="10"
                   MaxColumnsMedium="5"
                   MinColumnsLarge="5"
                   MinColumnsMedium="3"
                   Type="Items">
    <InRibbonGallery.MenuLayout>
      <VerticalMenuLayout Rows="2"
                          Gripper="Vertical"/>
    </InRibbonGallery.MenuLayout>
    <InRibbonGallery.MenuGroups>
      <MenuGroup>
        <Button CommandName="cmdButton1"></Button>
        <Button CommandName="cmdButton2"></Button>
      </MenuGroup>
      <MenuGroup>
        <Button CommandName="cmdButton3"></Button>
      </MenuGroup>
    </InRibbonGallery.MenuGroups>            
  </InRibbonGallery>
</Group>
```



## Element information


* **Minimum supported system**: Windows 7
* **Can be empty**: No



## See also

<dl> <dt>

[In-Ribbon Gallery control](windowsribbon-controls-inribbongallery.md)
</dt> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[Gallery Sample](windowsribbon-gallerysample.md)
</dt> </dl>

 

 





