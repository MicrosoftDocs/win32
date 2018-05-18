---
title: Vector.Picture property
description: Retrieves a Microsoft Visual Basic picture object.
ms.assetid: '36256b72-01ef-4bfb-bc20-d032b442ffab'
keywords: ["Picture property WIA Automation", "Picture property WIA Automation , Vector object", "Vector object WIA Automation , Picture property"]
topic_type:
- apiref
api_name:
- Vector.Picture
api_location:
- Wiaaut.h
api_type:
- COM
---

# Vector.Picture property

Retrieves a Microsoft Visual Basic picture object.

This property is read-only.

## Syntax


```VB
Property Picture( _
  [ ByVal Width As LONG ], _
  [ ByVal Height As LONG ] _
)
```



## Property value

## Remarks

Because vectors can contain an [**ImageFile**](-wiaaut-imagefile.md), this property provides an easy way to access the image as a Visual Basic picture object. Like the [**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md) property, the **Picture** property supports three different types of image vectors. For more information about the three types of image vectors, see the **ImageFile (Vector)** property.

For example code, see [Create an ImageFile Object that Contains a Blank Page](-wiaaut-shared-samples.md#create-an-imagefile-object-that-contains-a-blank-page) in Shared Samples.

Although the previous example uses the [**ImageFile (Vector)**](-wiaaut-ivector-imagefile.md) property instead of the **Picture** property to access the image contained in the [**Vector**](-wiaaut-vector.md), it does demonstrate creating a new image **Vector**.

For more information about raw ARGB Bitmap Data, see the Remarks section of the [**ImageFile**](-wiaaut-imagefile.md) object's [**ARGBData**](-wiaaut-iimagefile-argbdata.md) property. Since raw ARGB Bitmap Data does not contain any information about the height or width, you need to provide these values so that the Windows Image Acquisition (WIA) Automation Library can successfully create the Picture object.

For additional example code, see [Download New Items as They are Created](-wiaaut-shared-samples.md#download-new-items-as-they-are-created) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Vector**](-wiaaut-vector.md)
</dt> </dl>

 

 





