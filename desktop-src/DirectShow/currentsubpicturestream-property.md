---
description: The CurrentSubpictureStream property sets or retrieves the current subpicture stream.
ms.assetid: 66473c87-ddfe-4555-89ad-90e210a75694
title: CurrentSubpictureStream Property
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentSubpictureStream Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentSubpictureStream` property sets or retrieves the current subpicture stream.

``` syntax
[ iSPStream = ] MSWebDVD.CurrentSubpictureStream
```

## Return Value

Returns an integer value representing the stream.

## Remarks

The possible values of this property are:



| Value   | Description              |
|---------|--------------------------|
| 0 to 31 | The subpicture stream    |
| 63      | Muted low-bitrate stream |



 

This property is read/write with no default value. Before setting a new subpicture stream, call [**IsSubpictureStreamEnabled**](issubpicturestreamenabled-method.md) to verify that the stream is available.

Setting this property causes the [**SubpictureOn**](subpictureon-property.md) property to toggle to **True**.

## See also

<dl> <dt>

[**SubpictureOn**](subpictureon-property.md)
</dt> <dt>

[**SubpictureStreamsAvailable**](subpicturestreamsavailable-property.md)
</dt> </dl>

 

 



