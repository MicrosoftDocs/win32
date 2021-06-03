---
title: RecentItems element
description: Represents the Recent Items control in the Application Menu.
ms.assetid: a3df0bb0-e0f8-413a-879d-8e39164535d0
keywords:
- RecentItems element Windows Ribbon
topic_type:
- apiref
api_name:
- RecentItems
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RecentItems element

Represents the [Recent Items](windowsribbon-controls-recentitems.md) control in the [Application Menu](windowsribbon-controls-applicationmenu.md).

## Usage

``` syntax
<RecentItems
  CommandName = "xs:positiveInteger or xs:string"
  MaxCount = "xs:nonNegativeInteger"
  EnablePinning = "Boolean"/>
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
<td><strong>EnablePinning</strong><br/></td>
<td>Boolean<br/></td>
<td>No<br/></td>
<td>Restricted to one of the following values (0 and 1 are not valid):<br/> <br/>
<dt><span></span><span></span><strong></strong> (true)<br/> </dt> <dd> Default. <br/> </dd> <dt><span></span><span></span><strong></strong> (false)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>MaxCount</strong><br/></td>
<td>xs:nonNegativeInteger<br/></td>
<td>No<br/></td>
<td>The number of recent items to display.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:nonNegativeInteger)<br/> </dt> <dd> An integer value of 0 or greater.<br/> Default is <strong>10</strong>.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



| Element                                                                                             |
|-----------------------------------------------------------------------------------------------------|
| [**ApplicationMenu.RecentItems**](windowsribbon-element-applicationmenu-recentitems.md)<br/> |



## Remarks

Required.

Must occur exactly once for each [**ApplicationMenu.RecentItems**](windowsribbon-element-applicationmenu-recentitems.md) element.

The [Recent Items](windowsribbon-controls-recentitems.md) control displays the most recently used (MRU) items list of the Ribbon application.

## Examples

The following example demonstrates the basic markup for the [Recent Items](windowsribbon-controls-recentitems.md) control.

The following example shows a **RecentItems** Command declaration.


```XML
<!-- Command declaration for most recently used items. -->
<Command Name="cmdMRUItems"
         Symbol="ID_FILE_MRUITEMS"
         Id="25050"/>
```



The following example shows the associated **RecentItems** controls declaration.


```XML
<!-- Most recently used items collection. -->
<ApplicationMenu.RecentItems>
  <RecentItems CommandName="cmdMRUItems"/>
</ApplicationMenu.RecentItems>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: Yes


## See also

<dl> <dt>

[Application Menu control](windowsribbon-controls-applicationmenu.md)
</dt> <dt>

[Recent Items control](windowsribbon-controls-recentitems.md)
</dt> </dl>

 

 





