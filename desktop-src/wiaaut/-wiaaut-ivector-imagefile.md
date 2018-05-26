---
title: Vector.ImageFile property
description: Retrieves the image file thumbnail of an ImageFile object, the RGB data thumbnail of an Item object, or creates an ImageFile object from raw ARGB data. Retrieves an ImageFile object on success.
ms.assetid: 0bba6ade-d31c-4570-9f3d-c3c8e25d4a0b
keywords:
- ImageFile property WIA Automation
- ImageFile property WIA Automation , Vector object
- Vector object WIA Automation , ImageFile property
topic_type:
- apiref
api_name:
- Vector.ImageFile
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Vector.ImageFile property

Retrieves the image file thumbnail of an [**ImageFile**](-wiaaut-imagefile.md) object, the RGB data thumbnail of an [**Item**](-wiaaut-item.md) object, or creates an **ImageFile** object from raw ARGB data. Retrieves an **ImageFile** object on success.

This property is read-only.

## Syntax


```VB
Property ImageFile( _
  [ ByVal Width As LONG ], _
  [ ByVal Height As LONG ] _
)
```



## Property value

## Remarks

Since vectors can contain an image, this property provides an easy way to access the Image as an [**ImageFile**](-wiaaut-imagefile.md) object. Like the Picture property, the **ImageFile (Vector)** property supports three different types of Image Vectors.

The first type of Image [**Vector**](-wiaaut-vector.md) is a vector of bytes that contains the literal bytes of an image file. There are two common ways to acquire such a vector. First, by using the [**FileData**](-wiaaut-iimagefile-filedata.md) property of an [**ImageFile**](-wiaaut-imagefile.md) object to get the image file as a vector of bytes. Second, most JPEG images created by digital cameras contain a "ThumbnailData" property. The value of this property is a vector of bytes that is a thumbnail sized .jpg file. When the vector contains an image of this type the *Height* and *Width* parameters to the **ImageFile (Vector)** property are ignored.

The second type of Image [**Vector**](-wiaaut-vector.md) is a vector of bytes that contains raw RGB bitmap data. The most common way to acquire a vector like this is from the "Thumbnail Data" property of an [**Item**](-wiaaut-item.md) object. Since raw RGB Bitmap Data does not contain any information about the height or width, you need to provide these values so that the Windows Image Acquisition (WIA) Automation Library can successfully create the [**ImageFile**](-wiaaut-imagefile.md) object (or Microsoft Visual Basic picture object if you are using the [**Picture**](-wiaaut-ivector-picture.md) property). In the case where the raw RGB bitmap data was acquired from the "Thumbnail Data" property of an **Item** object, you can obtain the height from the "Thumbnail Height" property and the width from the "Thumbnail Width" property on the same **Item** object.

The third type of Image [**Vector**](-wiaaut-vector.md) is a vector of **Long** values that contains raw ARGB bitmap data. There are two common ways to create this kind of vector. First, you can create this type of vector by using the [**ARGBData**](-wiaaut-iimagefile-argbdata.md) property of an [**ImageFile**](-wiaaut-imagefile.md) object to get the raw ARGB bitmap data of the [**ActiveFrame**](-wiaaut-iimagefile-activeframe.md) property. Second, because the structure of raw ARGB bitmap data is not nearly as complex as raw RGB bitmap data, it is possible to create a **Vector** containing raw ARGB data from scratch as in the following sample.

For example code, see [Create an ImageFile Object that Contains a Blank Page](-wiaaut-shared-samples.md#create-an-imagefile-object-that-contains-a-blank-page) in Shared Samples.

For a similar method, see the [**Picture**](-wiaaut-ivector-picture.md) method.

For more information about raw ARGB bitmap data, see the Remarks section of the [**ImageFile**](-wiaaut-imagefile.md) object's [**ARGBData**](-wiaaut-iimagefile-argbdata.md) property. Since raw ARGB bitmap data does not contain any information about the height or width, you need to provide these values so that the WIA Automation Library can successfully create the **ImageFile** object.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**ShowAcquireImage**](-wiaaut-icommondialog-showacquireimage.md)
</dt> <dt>

[**Apply**](-wiaaut-iimageprocess-apply.md)
</dt> </dl>

 

 





