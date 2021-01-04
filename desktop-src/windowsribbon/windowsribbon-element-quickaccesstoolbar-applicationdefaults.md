---
title: QuickAccessToolbar.ApplicationDefaults property
description: Represents a container for default Commands in the Quick Access Toolbar (QAT).
ms.assetid: 8f44d7c0-1a39-4a88-ae01-7d7d1bb6bf7e
keywords:
- QuickAccessToolbar.ApplicationDefaults property Windows Ribbon
topic_type:
- apiref
api_name:
- QuickAccessToolbar.ApplicationDefaults
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# QuickAccessToolbar.ApplicationDefaults property

Represents a container for default Commands in the [Quick Access Toolbar (QAT)](windowsribbon-controls-quickaccesstoolbar.md).

## Usage

``` syntax
<QuickAccessToolbar.ApplicationDefaults>
  child elements
</QuickAccessToolbar.ApplicationDefaults>
```

## Attributes

There are no attributes.

## Child elements



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
<td><a href="windowsribbon-element-button.md"><strong>Button</strong></a><br/></td>
<td>Must occur at least once.<br/> <br/></td>
</tr>
<tr class="even">
<td><a href="windowsribbon-element-checkbox.md"><strong>CheckBox</strong></a><br/></td>
<td>Must occur at least once.<br/> <br/></td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-element-combobox.md"><strong>ComboBox</strong></a><br/></td>
<td>Must occur at least once.<br/>
<blockquote>
[!Note]<br />
Windows 8 and newer.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><a href="windowsribbon-element-dropdowngallery.md"><strong>DropDownGallery</strong></a><br/></td>
<td>Must occur at least once.<br/>
<blockquote>
[!Note]<br />
Windows 8 and newer.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-element-inribbongallery.md"><strong>InRibbonGallery</strong></a><br/></td>
<td>Must occur at least once.<br/>
<blockquote>
[!Note]<br />
Windows 8 and newer.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><a href="windowsribbon-element-splitbuttongallery.md"><strong>SplitButtonGallery</strong></a><br/></td>
<td>Must occur at least once.<br/>
<blockquote>
[!Note]<br />
Windows 8 and newer.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><a href="windowsribbon-element-togglebutton.md"><strong>ToggleButton</strong></a><br/></td>
<td>Must occur at least once.<br/> <br/></td>
</tr>
</tbody>
</table>



## Parent elements



| Element                                                                           |
|-----------------------------------------------------------------------------------|
| [**QuickAccessToolbar**](windowsribbon-element-quickaccesstoolbar.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**QuickAccessToolbar**](windowsribbon-element-quickaccesstoolbar.md).

A minimum of one child element must be specified.

A maximum of 20 child elements can be specified.

## Examples

The following example demonstrates the basic markup for the [**QuickAccessToolbar**](windowsribbon-element-quickaccesstoolbar.md).

This section of code shows the **QuickAccessToolbar.ApplicationDefaults** control declaration.


```XML
      <Ribbon.QuickAccessToolbar>
        <QuickAccessToolbar CommandName="cmdQAT"
                            CustomizeCommandName="cmdCustomizeQAT">
          <QuickAccessToolbar.ApplicationDefaults>
            <Button CommandName="cmdButton1"/>
            <ToggleButton CommandName="cmdMinimize"
                          ApplicationDefaults.IsChecked="false"/>
          </QuickAccessToolbar.ApplicationDefaults>
        </QuickAccessToolbar>
      </Ribbon.QuickAccessToolbar>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Quick Access Toolbar control](windowsribbon-controls-quickaccesstoolbar.md)
</dt> </dl>

 

 





