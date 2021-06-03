---
title: Image element (Windows Ribbon Framework)
description: Represents an image.
ms.assetid: 2c71bb16-93ac-484f-b81b-1b95842472b3
keywords:
- Image element Windows Ribbon
topic_type:
- apiref
api_name:
- Image
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Image element

Represents an image.

## Usage

``` syntax
<Image
  Source = "xs:anyURI"
  MinDPI = "xs:positiveInteger"
  Symbol = "xs:string"
  Id = "xs:positiveInteger union xs:string">
  child elements
</Image>
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
<td><strong>Id</strong><br/></td>
<td>xs:positiveInteger union xs:string<br/></td>
<td>No<br/></td>
<td>The unique resource ID. <br/> <br/>
<dt><span></span><span></span><strong></strong> (The union of xs:positiveInteger and xs:string)<br/> </dt> <dd> An integer value between 2 and 59999, inclusive, or 0x2 and 0xea5f in hexadecimal, inclusive. <br/> The maximum length is 10 characters including optional leading zeros. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>MinDPI</strong><br/></td>
<td>xs:positiveInteger<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:positiveInteger)<br/> </dt> <dd> Any sequence of digits with a minimum value of 96. <br/> If MinDPI is omitted, the default value is 96. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><strong>Source</strong><br/></td>
<td>xs:anyURI<br/></td>
<td>No<br/></td>
<td><dt><span></span><span></span><strong></strong> (xs:anyURI)<br/> </dt> <dd> Any sequence of characters that represents a URI. The URI value is an absolute or relative (to the Ribbon markup file) path to an image resource of type BMP. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><strong>Symbol</strong><br/></td>
<td>xs:string<br/></td>
<td>No<br/></td>
<td>The resource symbol for the image.<br/> <br/>
<dt><span></span><span></span><strong></strong> (xs:string)<br/> </dt> <dd> A string composed of a letter or underscore followed by any sequence of letters, digits, or underscores up to a maximum of 100 characters. <br/> </dd> </dl></td>
</tr>
</tbody>
</table>



## Child elements



| Element                                                               | Description                                   |
|-----------------------------------------------------------------------|-----------------------------------------------|
| [**Image.Source**](windowsribbon-element-image-source.md)<br/> | May occur at most once<br/> <br/> |



## Parent elements



| Element                                                                                                     |
|-------------------------------------------------------------------------------------------------------------|
| [**Command.LargeHighContrastImages**](windowsribbon-element-command-largehighcontrastimages.md)<br/> |
| [**Command.LargeImages**](windowsribbon-element-command-largeimages.md)<br/>                         |
| [**Command.SmallHighContrastImages**](windowsribbon-element-command-smallhighcontrastimages.md)<br/> |
| [**Command.SmallImages**](windowsribbon-element-command-smallimages.md)<br/>                         |



## Remarks

Optional.

May occur one or more times for each [**Command.SmallImages**](windowsribbon-element-command-smallimages.md), [**Command.SmallHighContrastImages**](windowsribbon-element-command-smallhighcontrastimages.md), [**Command.LargeImages**](windowsribbon-element-command-largeimages.md), or [**Command.LargeHighContrastImages**](windowsribbon-element-command-largehighcontrastimages.md) element.

When a collection of image resources that are designed to support specific screen dots per inch (dpi) settings is supplied to the Ribbon framework through a set of **Image** elements, the framework uses the **Image** with a *MinDPI* attribute value that matches the current screen dpi setting.

If no **Image** element is declared with a *MinDPI* value that matches the current screen dpi setting, the framework picks the **Image** that has the nearest *MinDPI* value less than the current screen dpi setting and scales the image resource up. Otherwise, if no **Image** element is declared with a *MinDPI* attribute value less than the current screen dpi setting, the framework picks the nearest *MinDPI* value greater than the current screen dpi setting and scales the image resource down.

## Examples

The following code example shows the markup required to declare, through a set of **Image** elements, a collection of image resources that are designed to support four specific screen dpi settings.


```XML
<Command Name="cmdSizeAndColor" Symbol="IDR_CMD_SIZEANDCOLOR">
  <Command.LabelTitle>
    <String Id="250">Size and Color</String>
  </Command.LabelTitle>
  <Command.LargeImages>
    <Image Id="251" MinDPI="96">res/sizeAndColor_96.bmp</Image>
    <Image Id="252" MinDPI="120">res/sizeAndColor_120.bmp</Image>
    <Image Id="253" MinDPI="144">res/sizeAndColor_144.bmp</Image>
    <Image Id="254" MinDPI="192">res/sizeAndColor_192.bmp</Image>
  </Command.LargeImages>
</Command>
```



## Element information

* **Minimum supported system**: Windows 7
* **Can be empty**: No



## See also

<dl> <dt>

[Specifying Ribbon Image Resources](windowsribbon-imageformats.md)
</dt> </dl>

 

 





