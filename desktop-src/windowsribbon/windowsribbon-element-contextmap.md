---
title: ContextMap element
description: Represents a ContextMenu and MiniToolbar pair mapping.
ms.assetid: 84379578-24c6-4bf7-8dcf-8e21e5665d29
keywords:
- ContextMap element Windows Ribbon
topic_type:
- apiref
api_name:
- ContextMap
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ContextMap element

Represents a [**ContextMenu**](windowsribbon-element-contextmenu.md) and [**MiniToolbar**](windowsribbon-element-minitoolbar.md) pair mapping.

## Usage

``` syntax
<ContextMap
  CommandName = "xs:positiveInteger or xs:string"
  MiniToolbar = "xs:string"
  ContextMenu = "xs:string"/>
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
<td><strong>ContextMenu</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>Must correspond to an existing <a href="windowsribbon-element-contextmenu.md"><strong>ContextMenu</strong></a> <em>Name</em>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>MiniToolbar</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>Must correspond to an existing <a href="windowsribbon-element-minitoolbar.md"><strong>MiniToolbar</strong></a> <em>Name</em>.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements

There are no child elements.

## Parent elements



| Element                                                                                       |
|-----------------------------------------------------------------------------------------------|
| [**ContextPopup.ContextMaps**](windowsribbon-element-contextpopup-contextmaps.md)<br/> |



## Remarks

Optional.

May occur one or more times for each [**ContextPopup.ContextMaps**](windowsribbon-element-contextpopup-contextmaps.md).

## Examples

The following example demonstrates the basic markup for a [**ContextPopup**](windowsribbon-element-contextpopup.md) View.

This section of code shows a set of **ContextMap** control declarations.


```XML
    <ContextPopup>
      <!--
        The MiniToolbars and Context Menus are the basic ingredients for 
        the contextual UI popup. 
        Mix-and-match and associate each combination with a ContextMap Command 
        invoked in code.
      -->
      <ContextPopup.MiniToolbars>
        <MiniToolbar Name="MiniToolbar1">
          <MenuGroup Class="MajorItems">
            <Button CommandName="cmdCut" />
            <Button CommandName="cmdCopy" />
            <Button CommandName="cmdPaste" />
          </MenuGroup>
          <MenuGroup>
            <ToggleButton CommandName="cmdToggleButton" />
            <DropDownButton CommandName="cmdButtons">
              <MenuGroup>
                <Button CommandName="cmdButton1" />
                <Button CommandName="cmdButton2" />
                <Button CommandName="cmdButton3" />
              </MenuGroup>
            </DropDownButton>
          </MenuGroup>
        </MiniToolbar>
        <MiniToolbar Name="MiniToolbar2">
          <MenuGroup>
            <Button CommandName="cmdButton1" />
            <Button CommandName="cmdButton2" />
            <Button CommandName="cmdButton3" />
          </MenuGroup>
        </MiniToolbar>
      </ContextPopup.MiniToolbars>
      <ContextPopup.ContextMenus>
        <ContextMenu Name="ContextMenu1">
          <MenuGroup>
            <Button CommandName="cmdCut" />
            <Button CommandName="cmdCopy" />
            <Button CommandName="cmdPaste" />
          </MenuGroup>
        </ContextMenu>
        <ContextMenu Name="ContextMenu2">
          <MenuGroup>
            <ToggleButton CommandName="cmdToggleButton" />
          </MenuGroup>
          <MenuGroup>
            <Button CommandName="cmdButton1" />
            <Button CommandName="cmdButton2" />
            <Button CommandName="cmdButton3" />
          </MenuGroup>
        </ContextMenu>
        <ContextMenu Name="ContextMenu4">
          <MenuGroup>
            <Button CommandName="cmdCut" />
            <Button CommandName="cmdCopy" />
            <Button CommandName="cmdPaste" />
          </MenuGroup>
          <MenuGroup>
            <ToggleButton CommandName="cmdToggleButton" />
          </MenuGroup>
          <MenuGroup>
            <Button CommandName="cmdButton1" />
            <Button CommandName="cmdButton2" />
            <Button CommandName="cmdButton3" />
          </MenuGroup>
        </ContextMenu>
      </ContextPopup.ContextMenus>
      <ContextPopup.ContextMaps>
        <ContextMap CommandName="cmdContextMap1"
                    ContextMenu="ContextMenu1"/>
        <ContextMap CommandName="cmdContextMap2"
                    ContextMenu="ContextMenu2"
                    MiniToolbar="MiniToolbar1"/>
        <ContextMap CommandName="cmdContextMap3"
                    MiniToolbar="MiniToolbar2"/>
        <ContextMap CommandName="cmdContextMap4"
                    ContextMenu="ContextMenu4"/>
      </ContextPopup.ContextMaps>
    </ContextPopup>
```



## Element information


* **Minimum supported system**: Windows 7
* **Can be empty**: Yes



## See also

<dl> <dt>

[Context Popup control](windowsribbon-controls-contextpopup.md)
</dt> </dl>

 

 





