---
title: Image.Source property
description: Represents the directory path of an image.
ms.assetid: 174a518a-e9a3-4461-a9a3-d61b62d2b718
keywords:
- Image.Source property Windows Ribbon
topic_type:
- apiref
api_name:
- Image.Source
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Image.Source property

Represents the directory path of an image.

## Usage

``` syntax
<Image.Source/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                                 |
|---------------------------------------------------------|
| [**Image**](windowsribbon-element-image.md)<br/> |



## Remarks

Optional.

May occur at most once for each [**Image**](windowsribbon-element-image.md).

This element contains a value of type *xs:anyURI* or any sequence of characters that represents a Uniform Resource Identifier (URI). The URI value is an absolute or relative (to the Ribbon markup file) directory path of an image resource of type bitmap (BMP).

## Examples

The following code example shows the markup required to declare, through a set of [**Image**](windowsribbon-element-image.md) elements, a collection of image resources that are designed to support four specific screen dpi settings. The **Image.Source** property is used to specify the path to the image resource.


```C++
<Command Name="cmdSizeAndColor" Symbol="IDR_CMD_SIZEANDCOLOR">
  <Command.LabelTitle>
    <String Id="250">Size and Color</String>
  </Command.LabelTitle>
  <Command.LargeImages>
    <Image Id="251" MinDPI="96">
      <Image.Source>res/sizeAndColor_96.bmp</Image.Source>
    </Image>
    <Image Id="252" MinDPI="120">
      <Image.Source>res/sizeAndColor_120.bmp</Image.Source>
    </Image>
    <Image Id="253" MinDPI="144">
      <Image.Source>res/sizeAndColor_144.bmp</Image.Source>
    </Image>
    <Image Id="254" MinDPI="192">
      <Image.Source>res/sizeAndColor_192.bmp</Image.Source>
    </Image>
  </Command.LargeImages>
</Command>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





