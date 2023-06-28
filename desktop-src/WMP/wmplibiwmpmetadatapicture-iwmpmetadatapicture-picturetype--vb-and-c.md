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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMetadataPicture::pictureType property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





