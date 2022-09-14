---
title: Command.SmallHighContrastImages property
description: Represents a container of images; in this case, small images for use with high-contrast system settings.
ms.assetid: d1c441eb-885a-4dc1-b98d-5a36cab2f837
keywords:
- Command.SmallHighContrastImages property Windows Ribbon
topic_type:
- apiref
api_name:
- Command.SmallHighContrastImages
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Command.SmallHighContrastImages property

Represents a container of images; in this case, small images for use with high-contrast system settings.

## Usage

``` syntax
<Command.SmallHighContrastImages>
  child elements
</Command.SmallHighContrastImages>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                        |
|---------------------------------------------------------|----------------------------------------------------|
| [**Image**](windowsribbon-element-image.md)<br/> | May occur one or more times<br/> <br/> |



## Parent elements



| Element                                                     |
|-------------------------------------------------------------|
| [**Command**](windowsribbon-element-command.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Command**](windowsribbon-element-command.md).

Image resources must conform to the standard bitmap (BMP) graphics format used in Windows.

## Examples

The following example demonstrates the basic markup for the [**SplitButton**](windowsribbon-element-splitbutton.md) with a [**MenuGroup**](windowsribbon-element-menugroup.md) element.

This section of code shows the [**SplitButton**](windowsribbon-element-splitbutton.md) and [**MenuGroup**](windowsribbon-element-menugroup.md) Command declarations with large and small high contrast image resources. An associated [**Group**](windowsribbon-element-group.md) that acts as the parent container for the **SplitButton** element is also declared.


```XML
<!-- SplitButton -->
<Command Name="cmdSplitButtonGroup"
         Symbol="cmdSplitButtonGroup"
         Comment="SplitButton Group"
         LabelTitle="SplitButton"/>
<Command Name="cmdSplitButton"
         Symbol="cmdSplitButton"
         Comment="SplitButton"
         LabelTitle="SplitButton"/>
<Command Name="cmdSBButtonItem"
         Symbol="cmdSBButtonItem"
         Comment="SBButtonItem"
         LabelTitle="SB ButtonItem"/>
<Command Name="cmdSBButton1"
         Symbol="cmdSBButton1"
         Comment="SBButton1"
         LabelTitle="SB Button">
  <Command.LargeImages>
    <Image Source="res/copyL_32.bmp"/>
  </Command.LargeImages>
  <Command.SmallImages>
    <Image Source="res/copyS_16.bmp"/>
  </Command.SmallImages>
  <Command.LargeHighContrastImages>
    <Image Source="res/copyLHC_32.bmp"/>
  </Command.LargeHighContrastImages>
  <Command.SmallHighContrastImages>
    <Image Source="res/copySHC_16.bmp"/>
  </Command.SmallHighContrastImages>
</Command>
<Command Name="cmdSBMajorItems"
         Comment="Major Items Category"
         LabelTitle="Major Items"/>
<Command Name="cmdSBStandardItems"
         Comment="Standard Items Category"
         LabelTitle="Standard Items"/>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Specifying Ribbon Image Resources](windowsribbon-imageformats.md)
</dt> <dt>

[UI\_PKEY\_SmallHighContrastImage](windowsribbon-reference-properties-uipkey-smallhighcontrastimage.md)
</dt> </dl>

 

 





