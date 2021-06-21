---
title: HelpButton element
description: Represents the Help Button control.
ms.assetid: 24c709da-539e-4ea0-bd3e-d3fbd72dfb97
keywords:
- HelpButton element Windows Ribbon
topic_type:
- apiref
api_name:
- HelpButton
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# HelpButton element

Represents the [Help Button](windowsribbon-controls-helpbutton.md) control.

## Usage

``` syntax
<HelpButton
  CommandName = "xs:positiveInteger or xs:string"/>
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

There are no child elements.

## Parent elements



| Element                                                                         |
|---------------------------------------------------------------------------------|
| [**Ribbon.HelpButton**](windowsribbon-element-ribbon-helpbutton.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Ribbon.HelpButton**](windowsribbon-element-ribbon-helpbutton.md).

Launches an application help dialog box when clicked.

## Examples

The following example demonstrates the basic markup that is required to implement a Ribbon [Help Button](windowsribbon-controls-helpbutton.md) control.

This section of code shows the **HelpButton** Command declaration.


```XML
<Command Name="cmdHelp"
         Symbol="IDR_CMD_HELP">      
</Command>
```



This section of code shows the **HelpButton** control declaration.


```XML
<Ribbon.HelpButton>
  <HelpButton CommandName="cmdHelp"/>
</Ribbon.HelpButton>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: Yes



## See also

<dl> <dt>

[Help Button control](windowsribbon-controls-helpbutton.md)
</dt> </dl>

 

 





