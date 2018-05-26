---
title: IStoreFolder GetFirstMessage method
description: Begins enumeration of messages in the folder represented by this interface and retrieves properties about the first result.
ms.assetid: ae8048a5-2058-483a-b426-033e515ba493
keywords:
- GetFirstMessage method Windows Mail (formerly Outlook Express)
- GetFirstMessage method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , GetFirstMessage method
topic_type:
- apiref
api_name:
- IStoreFolder.GetFirstMessage
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IStoreFolder::GetFirstMessage method

Begins enumeration of messages in the folder represented by this interface and retrieves properties about the first result.

## Syntax


```C++
HRESULT GetFirstMessage(
  [in]      DWORD          dwFlags,
  [in]      DWORD          dwMsgFlags,
  [in]      MESSAGEID      dwMsgIdFirst,
  [in, out] LPMESSAGEPROPS pProps,
  [out]     LPHENUMSTORE   phEnum
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Flags that determine how the operation will be performed. Set to 0 to retrieve all properties of the message. Set to MSGPROPS\_FAST to expedite retrieval and return a limited set of message information.

</dd> <dt>

*dwMsgFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Not used. Set to 0.

</dd> <dt>

*dwMsgIdFirst* \[in\]
</dt> <dd>

Type: **MESSAGEID**

Specifies the first message at which to begin enumeration. Must be set to MESSAGEID\_FIRST.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPMESSAGEPROPS**

Pointer to a [**MESSAGEPROPS**](oe-messageprops.md) structure that receives the properties for the retrieved message.

</dd> <dt>

*phEnum* \[out\]
</dt> <dd>

Type: **LPHENUMSTORE**

Pointer that receives a handle that allows for further enumeration.

</dd> </dl>

## Return value

Type: **HRESULT**

The function will return S\_OK if there are more messages to enumerate. If there are no more messages, the function will return S\_FALSE. If an error occurs, the following error code will be returned.



| Return code                                                                                  | Description                                                                      |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *phEnum* parameter is invalid, or the *pProps* value is **NULL**.<br/> |



 

## Remarks

If *dwFlags* is set to MSGPROPS\_FAST, only the following members of the structure referenced by the *pProps* structure will be valid.

-   cbSize
-   dwReserved
-   dwMessageId
-   dwLanguage
-   dwState

The [**MESSAGEPROPS**](oe-messageprops.md) structure that is received by the *pProps* parameter must be freed after use using the [**IStoreFolder::FreeMessageProps**](oe-istorefolder-freemessageprops.md) method.

This method will begin enumeration to list the messages in the folder represented by this interface, but will only return the first result. To continue enumerating messages, call [**IStoreFolder::GetNextMessage**](oe-istorefolder-getnextmessage.md), passing the handle stored in *phEnum* as the first argument.

When you have completed enumerating messages, call [**IStoreFolder::GetMessageClose**](oe-istorefolder-getmessageclose.md) to free memory associated with the enumeration.

The enumeration is not recursive.

> [!Note]  
> A call to **IStoreFolder::GetFirstMessage** can be invoked a second time in a process only after invoking [**IStoreFolder::GetMessageClose**](oe-istorefolder-getmessageclose.md).

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IStoreFolder**](oe-istorefolder.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**GetNextMessage**](oe-istorefolder-getnextmessage.md)
</dt> <dt>

[**GetMessageClose**](oe-istorefolder-getmessageclose.md)
</dt> </dl>

 

 





