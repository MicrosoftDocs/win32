---
title: IWMPMetadataPicture pictureType property
description: The pictureType property gets the picture type of the image represented by the metadata attribute.
ms.assetid: d36bbac5-93b8-4ef4-aa78-191d90942d3d
keywords:
- pictureType property Windows Media Player
- pictureType property Windows Media Player , IWMPMetadataPicture interface
- IWMPMetadataPicture interface Windows Media Player , pictureType property
topic_type:
- apiref
api_name:
- IWMPMetadataPicture.pictureType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMetadataPicture::pictureType property

The `pictureType` property gets the picture type of the image represented by the metadata attribute.

## Syntax


```CSharp
public System.String pictureType {get; set;}
```


```VB

Public ReadOnly Property pictureType As System.String
```





## Property value

A **System.String** that is the picture type of the image.

## Remarks

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMetadataPicture Interface (VB and C#)**](iwmpmetadatapicture--vb-and-c.md)
</dt> </dl>

 

 





