---
title: External.OnLoginChange Event
description: Note This topic describes functionality designed for use by online stores. | External.OnLoginChange Event
ms.assetid: 096794d5-977a-414f-8a98-b7998674c268
keywords:
- External.OnLoginChange Event Windows Media Player
topic_type:
- apiref
api_name:
- External.OnLoginChange Event
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.OnLoginChange Event

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnLoginChange** event occurs when the user's log-in status changes or when an attempt to log in fails.

``` syntax
window.external.OnLoginChange = FunctionName
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this event takes no parameters.

## Remarks

This event occurs every time the online store's plug-in calls [IWMPContentPartnerCallback::Notify](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-notify), passing wmpcnLoginStateChange in the *type* parameter. Sometimes the plug-in makes this call to notify Windows Media Player that there was a change in the user's log-in state. Other times, the plug-in makes this call to notify the Player that an attempt to log in failed. The *pContext* parameter of the **Notify** method specifies whether the notification is for a change of log-in state or for a failed log-in attempt.

Because every call to `Notify(wmpcnLoginStateChange, ...)` causes Windows Media Player to raise the **OnLoginChange** event, the **OnLoginChange** event handler is called sometimes as the result of a change in log-in state and sometimes as the result of a failed log-in attempt. To determine the user's current log-in state, the **OnLoginChange** event handler must call [External.userLoggedIn](external-userloggedin.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.attemptLogin**](external-attemptlogin.md)
</dt> <dt>

[**External.userLoggedIn**](external-userloggedin.md)
</dt> </dl>

 

 





