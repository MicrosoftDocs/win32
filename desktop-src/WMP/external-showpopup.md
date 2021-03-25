---
title: External.showPopup method
description: Note This topic describes functionality designed for use by online stores. | External.showPopup method
ms.assetid: 17958543-dbed-45a5-9b02-4800a07cb820
keywords:
- showPopup method Windows Media Player
- showPopup method Windows Media Player , External class
- External class Windows Media Player , showPopup method
topic_type:
- apiref
api_name:
- External.showPopup
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.showPopup method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **showPopup** method instructs Windows Media Player to display a pop-up webpage; that is, a webpage that appears in a separate window.

## Syntax


```JScript
External.showPopup(
  PopupIndex,
  Parameters
)
```



## Parameters

<dl> <dt>

*PopupIndex* \[in\]
</dt> <dd>

**Number** (**long**) that specifies the index of the pop-up webpage.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

**String** that Windows Media Player appends to the URL of the webpage.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The pop-up index is not interpreted by Windows Media Player. Indexes that identify pop-up webpages are created by the online store, and have meaning only to the online store.

The following steps show how Windows Media Player uses the parameters of the **showPopup** method to create a URL for the popup window.

1.  Script on a discovery page calls **showPopup**, passing an integer in *PopupIndex* and a string in *Parameters*.

2.  Windows Media Player passes the index to [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo) to retrieve the URL of the webpage to be displayed.

3.  Windows Media Player appends *Parameters* to the URL as a query string. For example, if **GetItemInfo** returns "https://www.Proseware.com/Pages/Popup1.htm" and *Parameters* is equal to "DlgX=800&DlgY=400&Greeting=Hi", Windows Media Player creates the following URL:

    https://www.Proseware.com/Pages/Popup1.htm?DlgX=800&DlgY=400&Greeting=Hi

You can use *Parameters* to specify the size of the pop-up window. For example, if you set *Parameters* to "DlgX=800&DlgY=400", the pop-up window will have a size of 800 pixels by 400 pixels.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





