---
title: External.sendMessage method
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The sendMessage method sends a message to the online store's plug-in.
ms.assetid: 72d34dcc-3284-4446-804f-0fc93a7d8dab
keywords:
- sendMessage method Windows Media Player
- sendMessage method Windows Media Player , External class
- External class Windows Media Player , sendMessage method
topic_type:
- apiref
api_name:
- External.sendMessage
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.sendMessage method

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **sendMessage** method sends a message to the online store's plug-in.

## Syntax


```JScript
External.sendMessage(
  Msg,
  Param
)
```



## Parameters

<dl> <dt>

*Msg* \[in\]
</dt> <dd>

**String** containing the message.

</dd> <dt>

*Param* \[in\]
</dt> <dd>

**String** containing parameters associated with the message.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The message is sent asynchronously. That is, this method returns immediately rather than waiting for the message to be processed. When the plug-in finishes processing the message, it calls the [IWMPContentPartnerCallback::SendMessageComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-sendmessagecomplete) method, which in turn calls the script's [OnSendMessageComplete](external-onsendmessagecomplete-event.md) event handler.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.OnSendMessageComplete**](external-onsendmessagecomplete-event.md)
</dt> <dt>

[**IWMPContentPartner::SendMessage**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-sendmessage)
</dt> <dt>

[**IWMPContentPartnerCallback::SendMessageComplete**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-sendmessagecomplete)
</dt> </dl>

 

 





