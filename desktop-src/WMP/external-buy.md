---
title: External.buy method
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The buy method initiates the purchase of a set of media items.
ms.assetid: 78496de6-214e-4712-8fbc-11e002adce88
keywords:
- buy method Windows Media Player
- buy method Windows Media Player , External class
- External class Windows Media Player , buy method
topic_type:
- apiref
api_name:
- External.buy
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.buy method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **buy** method initiates the purchase of a set of media items.

## Syntax


```JScript
External.buy(
  ViewType,
  ViewIDs
)
```



## Parameters

<dl> <dt>

*ViewType* \[in\]
</dt> <dd>

**String** that specifies the type of item to be purchased. The caller must set this parameter to one of the following [library location constants](library-location-constants.md):

CPListID

CPTrackID

CPAlbumID

</dd> <dt>

*ViewIDs* \[in\]
</dt> <dd>

**String** containing the IDs, delimited by semicolons, of the items to be purchased.

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

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.download**](external-download.md)
</dt> <dt>

[**IWMPContentPartner::Buy**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-buy)
</dt> <dt>

[**Purchasing Media Content**](purchasing-media-content.md)
</dt> </dl>

 

 





