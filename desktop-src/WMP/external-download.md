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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.download method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





