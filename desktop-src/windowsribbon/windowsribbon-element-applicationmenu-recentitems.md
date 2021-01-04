---
title: ApplicationMenu.RecentItems property
description: Represents a container for the Recent Items control in the Application Menu.
ms.assetid: 26ed38b6-17de-423f-a113-ccbaf3780a91
keywords:
- ApplicationMenu.RecentItems property Windows Ribbon
topic_type:
- apiref
api_name:
- ApplicationMenu.RecentItems
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ApplicationMenu.RecentItems property

Represents a container for the [Recent Items](windowsribbon-controls-recentitems.md) control in the [Application Menu](windowsribbon-controls-applicationmenu.md).

## Usage

``` syntax
<ApplicationMenu.RecentItems
  CommandName = "xs:positiveInteger or xs:string"
>
  child elements
</ApplicationMenu.RecentItems>
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
</tbody>
</table>



## Child elements



| Element                                                             | Description                                    |
|---------------------------------------------------------------------|------------------------------------------------|
| [**RecentItems**](windowsribbon-element-recentitems.md)<br/> | Must occur exactly once<br/> <br/> |



## Parent elements



| Element                                                                     |
|-----------------------------------------------------------------------------|
| [**ApplicationMenu**](windowsribbon-element-applicationmenu.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**ApplicationMenu**](windowsribbon-element-applicationmenu.md) element.

The [Recent Items](windowsribbon-controls-recentitems.md) control displays the most recently used (MRU) items list of the Ribbon application.

## Examples

The following example demonstrates the basic markup for the [Recent Items](windowsribbon-controls-recentitems.md) control.

The following example shows a [**RecentItems**](windowsribbon-element-recentitems.md) Command declaration.


```XML
<!-- Command declaration for most recently used items. -->
<Command Name="cmdMRUItems"
         Symbol="ID_FILE_MRUITEMS"
         Id="25050"/>
```



The following example shows the associated **ApplicationMenu.RecentItems** and [**RecentItems**](windowsribbon-element-recentitems.md) controls declaration.


```XML
<!-- Most recently used items collection. -->
<ApplicationMenu.RecentItems>
  <RecentItems CommandName="cmdMRUItems"/>
</ApplicationMenu.RecentItems>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Application Menu control](windowsribbon-controls-applicationmenu.md)
</dt> <dt>

[Recent Items control](windowsribbon-controls-recentitems.md)
</dt> </dl>

 

 





