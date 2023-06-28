---
title: External.userLoggedIn
description: Note This topic describes functionality designed for use by online stores. | External.userLoggedIn
ms.assetid: d02d9486-c692-4f46-bc29-f0aaa45cad0f
keywords:
- External.userLoggedIn Windows Media Player
topic_type:
- apiref
api_name:
- External.userLoggedIn
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.userLoggedIn

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **userLoggedIn** property retrieves a value indicating whether the user is logged in to the online store.

## Syntax

``` syntax
window.external.userLoggedIn
```

## Possible Values

This property is a read-only **Boolean**. **TRUE** indicates that the user is logged in, and **FALSE** indicates that the user is logged out.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.attemptLogin**](external-attemptlogin.md)
</dt> <dt>

[**External.OnLoginChange Event**](external-onloginchange-event.md)
</dt> </dl>

 

 





