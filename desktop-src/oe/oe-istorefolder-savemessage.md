---
title: IStoreFolder SaveMessage method
description: Saves a stream as a new message to the folder associated with the interface.
ms.assetid: '2b2f5722-e03e-41dc-ab57-08eba13fe055'
keywords: ["SaveMessage method Windows Mail (formerly Outlook Express)", "SaveMessage method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , SaveMessage method"]
topic_type:
- apiref
api_name:
- IStoreFolder.SaveMessage
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::SaveMessage method

Saves a stream as a new message to the folder associated with the interface.

## Syntax


```C++
HRESULT SaveMessage(
  [in]  REFIID      riid,
  [in]  LPVOID      pvObject,
  [in]  DWORD       dwMsgFlags,
  [out] LPMESSAGEID pdwMessageId
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the type of stream that *pvObject* represents. Must be either IID\_IStream or IID\_IMimeMessage.

</dd> <dt>

*pvObject* \[in\]
</dt> <dd>

Type: **LPVOID**

Pointer to a stream that represents the message body.

</dd> <dt>

*dwMsgFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a combination of state flags to apply to the message associated with the stream. For a list of flags, see [**Message State Flags**](oe-message-state-flags.md).

</dd> <dt>

*pdwMessageId* \[out\]
</dt> <dd>

Type: **LPMESSAGEID**

Pointer that receives an ID value that identifies the new message.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                                                       |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value of *pvObject* is **NULL**, or the *riid* parameter is not IID\_IStream or IID\_IMimeMessage.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





