---
description: You can store and retrieve image metadata with the help of a PropertyItem object. The type data member of a PropertyItem object specifies the data type of the values stored in the value data member of that same PropertyItem object.
ms.assetid: d05cdf42-4b30-45ce-85a1-025d4f4e9d13
title: Image Property Tag Type Constants (Gdiplusimaging.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Image Property Tag Type Constants

You can store and retrieve image metadata with the help of a [**PropertyItem**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-propertyitem) object. The **type** data member of a **PropertyItem** object specifies the data type of the values stored in the value data member of that same **PropertyItem** object.

The following constants, defined in Gdiplusimaging.h, can be assigned to the **type** data member of a [**PropertyItem**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-propertyitem) object.



| Constant                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                              |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PixelFormat4bppIndexed"></span><span id="pixelformat4bppindexed"></span><span id="PIXELFORMAT4BPPINDEXED"></span><dl> <dt>**PixelFormat4bppIndexed**</dt> </dl>         | Specifies that the format is 4 bits per pixel, indexed.<br/>                                                                                                                                                                                                                                                                                                                       |
| <span id="PropertyTagTypeASCII"></span><span id="propertytagtypeascii"></span><span id="PROPERTYTAGTYPEASCII"></span><dl> <dt>**PropertyTagTypeASCII**</dt> </dl>                 | Specifies that the **value** data member is a null-terminated ASCII string. If you set the **type** data member of a [**PropertyItem**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-propertyitem) object to PropertyTagTypeASCII, you should set the **length** data member to the length of the string including the NULL terminator. For example, the string `HELLO` would have a length of 6.<br/> |
| <span id="PropertyTagTypeByte"></span><span id="propertytagtypebyte"></span><span id="PROPERTYTAGTYPEBYTE"></span><dl> <dt>**PropertyTagTypeByte**</dt> </dl>                     | Specifies that the **value** data member is an array of bytes.<br/>                                                                                                                                                                                                                                                                                                                |
| <span id="PropertyTagTypeLong"></span><span id="propertytagtypelong"></span><span id="PROPERTYTAGTYPELONG"></span><dl> <dt>**PropertyTagTypeLong**</dt> </dl>                     | Specifies that the **value** data member is an array of unsigned long (32-bit) integers.<br/>                                                                                                                                                                                                                                                                                      |
| <span id="PropertyTagTypeRational"></span><span id="propertytagtyperational"></span><span id="PROPERTYTAGTYPERATIONAL"></span><dl> <dt>**PropertyTagTypeRational**</dt> </dl>     | Specifies that the **value** data member is an array of pairs of unsigned long integers. Each pair represents a fraction; the first integer is the numerator and the second integer is the denominator.<br/>                                                                                                                                                                       |
| <span id="PropertyTagTypeShort"></span><span id="propertytagtypeshort"></span><span id="PROPERTYTAGTYPESHORT"></span><dl> <dt>**PropertyTagTypeShort**</dt> </dl>                 | Specifies that the **value** data member is an array of unsigned short (16-bit) integers.<br/>                                                                                                                                                                                                                                                                                     |
| <span id="PropertyTagTypeSLONG"></span><span id="propertytagtypeslong"></span><span id="PROPERTYTAGTYPESLONG"></span><dl> <dt>**PropertyTagTypeSLONG**</dt> </dl>                 | Specifies that the **value** data member is an array of signed long (32-bit) integers.<br/>                                                                                                                                                                                                                                                                                        |
| <span id="PropertyTagTypeSRational"></span><span id="propertytagtypesrational"></span><span id="PROPERTYTAGTYPESRATIONAL"></span><dl> <dt>**PropertyTagTypeSRational**</dt> </dl> | Specifies that the **value** data member is an array of pairs of signed long integers. Each pair represents a fraction; the first integer is the numerator and the second integer is the denominator.<br/>                                                                                                                                                                         |
| <span id="PropertyTagTypeUndefined"></span><span id="propertytagtypeundefined"></span><span id="PROPERTYTAGTYPEUNDEFINED"></span><dl> <dt>**PropertyTagTypeUndefined**</dt> </dl> | Specifies that the **value** data member is an array of bytes that can hold values of any data type. <br/>                                                                                                                                                                                                                                                                         |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Gdiplusimaging.h</dt> </dl> |



## See also

<dl> <dt>

[Image Property Tag Constants](-gdiplus-constant-image-property-tag-constants.md)
</dt> <dt>

[Image File Format Specifications](-gdiplus-constant-image-file-format-specifications.md)
</dt> <dt>

[Reading and Writing Metadata](-gdiplus-reading-and-writing-metadata-use.md)
</dt> </dl>

 

 
