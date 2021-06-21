---
title: Command element
description: Represents a Command definition.
ms.assetid: f332423d-d258-488d-9233-71687288b462
keywords:
- Command element Windows Ribbon
topic_type:
- apiref
api_name:
- Command
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Command element

Represents a Command definition.

## Usage

``` syntax
<Command
  Name = "xs:string"
  Symbol = "xs:string"
  Id = "xs:positiveInteger union xs:string"
  Comment = "xs:string"
  LabelTitle = "xs:string"
  LabelDescription = "xs:string"
  TooltipTitle = "xs:string"
  TooltipDescription = "xs:string"
  Keytip = "xs:string">
  child elements
</Command>
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
<td><strong>Comment</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>Used to annotate the command element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> Maximum length: 250 characters.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>Id</strong><br/></td>
<td>xs:positiveInteger union xs:string<br/></td>
<td>No<br/></td>
<td>The unique resource ID. <br/> <br/>
<dt><span></span><span></span><strong></strong> (The union of xs:positiveInteger and xs:string)<br/> </dt> <dd> An integer value between 2 and 59999, inclusive, or 0x2 and 0xea5f in hexadecimal, inclusive. <br/> Maximum length is 10 characters, including optional leading zeros. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>Keytip</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>A string that represents the keyboard shortcut of a command element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>LabelDescription</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>A string that represents the text displayed on a command element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>LabelTitle</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>A string that represents the text displayed on a command element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>Name</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string that consists of a letter or underscore followed by any sequence of digits, letters, or underscores.<br/> Maximum length: 100 characters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>Symbol</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string that consists of a letter or underscore followed by any sequence of digits, letters, or underscores.<br/> Maximum length: 100 characters.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>TooltipDescription</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>A string that represents the text displayed on a command element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>TooltipTitle</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>A string that represents the text displayed on a command element.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of any sequence of characters, including white space and line-break characters.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements



| Element                                                                                                     | Description                                   |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [**Command.Comment**](windowsribbon-element-command-comment.md)<br/>                                 | May occur at most once<br/> <br/> |
| [**Command.Id**](windowsribbon-element-command-id.md)<br/>                                           | May occur at most once<br/> <br/> |
| [**Command.Keytip**](windowsribbon-element-command-keytip.md)<br/>                                   | May occur at most once<br/> <br/> |
| [**Command.LabelDescription**](windowsribbon-element-command-labeldescription.md)<br/>               | May occur at most once<br/> <br/> |
| [**Command.LabelTitle**](windowsribbon-element-command-labeltitle.md)<br/>                           | May occur at most once<br/> <br/> |
| [**Command.LargeHighContrastImages**](windowsribbon-element-command-largehighcontrastimages.md)<br/> | May occur at most once<br/> <br/> |
| [**Command.LargeImages**](windowsribbon-element-command-largeimages.md)<br/>                         | May occur at most once<br/> <br/> |
| [**Command.Name**](windowsribbon-element-command-name.md)<br/>                                       | May occur at most once<br/> <br/> |
| [**Command.SmallHighContrastImages**](windowsribbon-element-command-smallhighcontrastimages.md)<br/> | May occur at most once<br/> <br/> |
| [**Command.SmallImages**](windowsribbon-element-command-smallimages.md)<br/>                         | May occur at most once<br/> <br/> |
| [**Command.Symbol**](windowsribbon-element-command-symbol.md)<br/>                                   | May occur at most once<br/> <br/> |
| [**Command.TooltipDescription**](windowsribbon-element-command-tooltipdescription.md)<br/>           | May occur at most once<br/> <br/> |
| [**Command.TooltipTitle**](windowsribbon-element-command-tooltiptitle.md)<br/>                       | May occur at most once<br/> <br/> |



## Parent elements



| Element                                                                               |
|---------------------------------------------------------------------------------------|
| [**Application.Commands**](windowsribbon-element-application-commands.md)<br/> |



## Remarks

Required.

May occur one or more times for each [**Application.Commands**](windowsribbon-element-application-commands.md) element.

The child elements of the **Command** element may occur in any order.

Typically, Command resources are declared in Ribbon markup, but they can also be set at run time with a call to [**SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty). For example, it is possible to set the [UI\_PKEY\_Keytip](windowsribbon-reference-properties-uipkey-keytip.md) property for a Command instead of declaring a value in markup with the [**Command.Keytip**](windowsribbon-element-command-keytip.md) element.

In cases where Command properties, such as labels and images, cannot be set with [**SetUICommandProperty**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setuicommandproperty) they can be invalidated with a call to [**InvalidateUICommand**](/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-invalidateuicommand). After invalidation, the framework queries the host application for the resource details.

> [!Note]  
> A resource cannot be reinstated from the markup resource table after it has been invalidated.

 

A Command definition is added to the Ribbon markup header file for each **Command** declared in markup.

The value of *Keytip* acts as the keyboard accelerator for a Command unless that Command is exposed through a menu item. In this case, the framework ignores the *Keytip* value and instead uses a character preceded by an ampersand as specified by *LabelTitle* or [UI\_PKEY\_Label](windowsribbon-reference-properties-uipkey-label.md). If no ampersand is specified by *LabelTitle* or UI\_PKEY\_Label, no keytip or keyboard accelerator is exposed.

## Examples

The following example shows a manifest of **Command** elements for a **Home** tab.


```XML
<Application.Commands>
```




```XML
<Command Name="cmdHomeTab"
         LabelTitle="Home"
         Keytip="H" />
<Command Name="cmdClipboardGroup"
         Symbol="IDR_CMD_CLIPBOARD"
         Id="10000"
         Comment="Command definition for clipboard group"
         LabelTitle="Clipboard"
         Keytip="CB" />
<Command Name="cmdCopy"
         Symbol="IDR_CMD_COPY"
         LabelTitle="Copy"
         LabelDescription="Copy"
         Keytip="C"
         TooltipTitle="Copy"
         TooltipDescription="Click to copy">
  <Command.SmallImages>
    <Image>res/copyS_16.bmp</Image>
  </Command.SmallImages>
  <Command.LargeImages>
    <Image>res/copyL_32.bmp</Image>
  </Command.LargeImages>
</Command>
<Command Name="cmdPaste"
         Symbol="IDR_CMD_PASTE" >
  <Command.LabelTitle>Paste</Command.LabelTitle>
  <Command.LabelDescription>
    <String Content="Paste contents of clipboard"
            Id="10001"
            Symbol="IDR_RES_LABELDESC_PASTE" />
  </Command.LabelDescription>
  <Command.Keytip>P</Command.Keytip>
  <Command.TooltipTitle>
    <String Content="Paste contents of clipboard"
            Id="10002"
            Symbol="IDR_RES_TOOLTIP_PASTE"/>
  </Command.TooltipTitle>
  <Command.TooltipDescription>
    <String Content="Click to paste contents of clipboard"/>
  </Command.TooltipDescription>
  <Command.SmallImages>
    <Image
      Id="10010"
      MinDPI="96"
      Symbol="IDR_RES_SMALL_IMAGE96">
      <Image.Source>res/pasteS_96bpp.bmp</Image.Source>
    </Image>
    <Image Source="res/pasteS_120bpp.bmp"
           Id="10011"
           MinDPI="120"
           Symbol="IDR_RES_SMALL_IMAGE120" />
  </Command.SmallImages>
  <Command.LargeImages>
    <Image>res/pasteL_32.bmp</Image>
  </Command.LargeImages>
</Command>
<Command Name="cmdMinimize"
         Symbol="IDR_CMD_MINIMIZE"
         Id="10001"
         LabelTitle="Minimize" />
```




```XML
</Application.Commands>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: No



 

