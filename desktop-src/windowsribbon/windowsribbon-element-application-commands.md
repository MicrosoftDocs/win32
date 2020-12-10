---
title: Application.Commands property
description: Represents a container for all the Commands that are defined by the application.
ms.assetid: 160d7d28-2d64-4cbc-b2b9-2da6b2f5b3c8
keywords:
- Application.Commands property Windows Ribbon
topic_type:
- apiref
api_name:
- Application.Commands
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Application.Commands property

Represents a container for all the Commands that are defined by the application.

## Usage

``` syntax
<Application.Commands>
  child elements
</Application.Commands>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                     | Description                                        |
|-------------------------------------------------------------|----------------------------------------------------|
| [**Command**](windowsribbon-element-command.md)<br/> | May occur one or more times<br/> <br/> |



## Parent elements



| Element                                                             |
|---------------------------------------------------------------------|
| [**Application**](windowsribbon-element-application.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Application**](windowsribbon-element-application.md) element.

## Examples

The following example shows an **Application.Commands** element that contains a manifest of clipboard Commands.


```C++
<Application.Commands>
```




```C++
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




```C++
</Application.Commands>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Application.Views**](windowsribbon-element-application-views.md)
</dt> </dl>

 

 





