---
title: External.download method
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The download method initiates the download of a set of media items.
ms.assetid: 10bae41c-0658-4712-8a7e-375a1ec6dc25
keywords:
- download method Windows Media Player
- download method Windows Media Player , External class
- External class Windows Media Player , download method
topic_type:
- apiref
api_name:
- External.download
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.download method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **download** method initiates the download of a set of media items.

## Syntax


```JScript
External.download(
  Type,
  IDs
)
```



## Parameters

<dl> <dt>

*Type* \[in\]
</dt> <dd>

A [library location constant](library-location-constants.md) that specifies the type of item to be downloaded. For example, CPTrackID specifies that one or more tracks are to be downloaded.

</dd> <dt>

*IDs* \[in\]
</dt> <dd>

**String** containing the IDs, delimited by semicolons, of the media items to be downloaded.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Downloading Media Content**](downloading-media-content.md)
</dt> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.buy**](external-buy.md)
</dt> <dt>

[**IWMPContentPartner::Download**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-download)
</dt> </dl>

 

 





