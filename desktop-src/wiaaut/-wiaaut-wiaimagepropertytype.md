---
title: WiaImagePropertyType enumeration
description: Specifies the type of the value of an image property. Image properties can be found in the Properties (ImageFile) collection of an ImageFile object.
ms.assetid: 31bad79f-4a55-4cb3-9bef-097768f14755
keywords:
- WiaImagePropertyType enumeration WIA Automation
- WiaDeviceType enumeration WIA Automation
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# WiaImagePropertyType enumeration

Specifies the type of the value of an image property. Image properties can be found in the [**Properties (ImageFile)**](-wiaaut-iimagefile-properties.md) collection of an [**ImageFile**](-wiaaut-imagefile.md) object.

## Members



| Member                                         | Description                                                                                                                                                                   | Value |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **UndefinedImagePropertyType**                 | The value of the image property is undefined and returned as a Byte.<br/>                                                                                               | 1000  |
| **ByteImagePropertyType**                      | The value of the image property is a Byte.<br/>                                                                                                                         | 1001  |
| **StringImagePropertyType**                    | The value of the image property is a String.<br/>                                                                                                                       | 1002  |
| **UnsignedIntegerImagePropertyType**           | The value of the image property is returned as a non-negative Integer.<br/>                                                                                             | 1003  |
| **LongImagePropertyType**                      | The value of the image property is a Long.<br/>                                                                                                                         | 1004  |
| **UnsignedLongImagePropertyType**              | The value of the image property is returned as a non-negative Long.<br/>                                                                                                | 1005  |
| **RationalImagePropertyType**                  | The value of the image property is returned as a [**Rational**](-wiaaut-rational.md) Object.<br/>                                                                      | 1006  |
| **UnsignedRationalImagePropertyType**          | The value of the image property is returned as an unsigned [**Rational**](-wiaaut-rational.md) Object.<br/>                                                            | 1007  |
| **VectorOfUndefinedImagePropertyType**         | The value of the image property is returned as a [**Vector**](-wiaaut-vector.md) object containing Byte elements.<br/>                                                 | 1100  |
| **VectorOfBytesImagePropertyType**             | The value of the image property is a [**Vector**](-wiaaut-vector.md) object containing Byte elements.<br/>                                                             | 1101  |
| **VectorOfUnsignedIntegersImagePropertyType**  | The value of the image property is returned as a [**Vector**](-wiaaut-vector.md) object containing Integer elements.<br/>                                              | 1102  |
| **VectorOfLongsImagePropertyType**             | The value of the image property is a [**Vector**](-wiaaut-vector.md) object containing Long elements.<br/>                                                             | 1103  |
| **VectorOfUnsignedLongsImagePropertyType**     | The value of the image property is returned as a [**Vector**](-wiaaut-vector.md) object containing Long elements.<br/>                                                 | 1104  |
| **VectorOfRationalsImagePropertyType**         | The value of the image property is returned as a [**Vector**](-wiaaut-vector.md) object containing [**Rational**](-wiaaut-rational.md) object elements.<br/>          | 1105  |
| **VectorOfUnsignedRationalsImagePropertyType** | The value of the image property is returned as a [**Vector**](-wiaaut-vector.md) object containing unsigned [**Rational**](-wiaaut-rational.md) object elements.<br/> | 1106  |



## Remarks

The value of the Type property on a [**Property**](-wiaaut-property.md) object when it comes from a [**Properties**](-wiaaut-properties.md) collection on an [**ImageFile**](-wiaaut-imagefile.md) object can return one of the members of the WiaImagePropertyType enumeration. This provides more information about the type of value contained in the Value property. A member of the **WiaImagePropertyType** enumeration can also be used as the value of the Type property in an Exchangeable Image File (EXIF) filter to specify the type of property to add to an image.

For example code, see [Display all ImageFile Properties](https://www.bing.com/search?q=Display all ImageFile Properties) and [Exif Filter: Write a New Title Tag to an Image](https://www.bing.com/search?q=Exif Filter: Write a New Title Tag to an Image).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





