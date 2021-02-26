---
title: External.OnSendMessageComplete Event
description: Note This topic describes functionality designed for use by online stores. | External.OnSendMessageComplete Event
ms.assetid: 9ae60aa5-4ecd-41dd-aeb0-afb1a3686982
keywords:
- External.OnSendMessageComplete Event Windows Media Player
topic_type:
- apiref
api_name:
- External.OnSendMessageComplete Event
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.OnSendMessageComplete Event

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnSendMessageComplete** event occurs when the online store has finished processing a message. Script on the discovery page previously sent the message by calling [External.sendMessage](external-sendmessage.md).

``` syntax
window.external.OnSendMessageComplete = FunctionName
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this event has the following parameters.

<dl> <dt>

<span id="Msg"></span><span id="msg"></span><span id="MSG"></span>*Msg*
</dt> <dd>

The same string that was passed in the **Msg** parameter of **sendMessage**.

</dd> <dt>

<span id="Param"></span><span id="param"></span><span id="PARAM"></span>*Param*
</dt> <dd>

The same string that was passed in the **Param** parameter of **sendMessage**.

</dd> <dt>

<span id="Result"></span><span id="result"></span><span id="RESULT"></span>*Result*
</dt> <dd>

**String** that contains the result of the message handling. See Remarks.

</dd> </dl>

## Remarks

The **sendMessage** method calls [IWMPContentPartner::SendMessage](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-sendmessage), which returns asynchronously. That is, it returns before the online store finishes processing the message. When the online store finishes processing the message, it calls [IWMPContentPartnerCallback::SendMessageComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-sendmessagecomplete), which in turn calls the script's **OnSendMessageComplete** event handler.

When the online store calls **IWMPContentPartnerCallback::SendMessageComplete**, it supplies a result code in the *bstrResult* parameter. Windows Media Player does not interpret that result code. Instead, Windows Media Player passes the result code along to the **OnSendMessageComplete** event handler in the *Result* parameter.

None of the parameters (*Msg*, *Param*, *Result*) of the **OnSendMessageComplete** event handler is interpreted by Windows Media Player. The parameters have meaning only to the online store.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.sendMessage**](external-sendmessage.md)
</dt> <dt>

[**IWMPContentPartner::SendMessage**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-sendmessage)
</dt> <dt>

[**IWMPContentPartnerCallback::SendMessageComplete**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-sendmessagecomplete)
</dt> </dl>

 

 





