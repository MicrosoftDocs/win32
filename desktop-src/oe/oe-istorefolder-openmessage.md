---
title: IStoreFolder OpenMessage method
description: Opens a specific message and retrieves a read-only stream that can be used to read the message body.
ms.assetid: 77b23e65-11c1-42ee-a5e9-a1e1e7daee00
keywords:
- OpenMessage method Windows Mail (formerly Outlook Express)
- OpenMessage method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , OpenMessage method
topic_type:
- apiref
api_name:
- IStoreFolder.OpenMessage
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

# IStoreFolder::OpenMessage method

Opens a specific message and retrieves a read-only stream that can be used to read the message body.

## Syntax


```C++
HRESULT OpenMessage(
  [in]  MESSAGEID dwMessageId,
  [in]  REFIID    riid,
  [out] LPVOID    *ppvObject
);
```



## Parameters

<dl> <dt>

*dwMessageId* \[in\]
</dt> <dd>

Type: **MESSAGEID**

Specifies the message to be opened.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the type of stream that *ppvObject* will receive. Must be either IID\_IStream, or IID\_IMimeMessage.

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **LPVOID\***

Reference to a pointer that receives the stream.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value of the *dwMessageId* is invalid, the value of *ppvObject* is **NULL**, or the *riid* parameter is not IID\_IStream or IID\_IMimeMessage.<br/> |



 

## Remarks

This method will attempt to open the message body in a read-only mode. To obtain more information and properties about the message itself, call [**IStoreFolder::GetMessageProps**](oe-istorefolder-getmessageprops.md).

The object that is received by *ppvObject* has memory associated with it, and must be freed by calling its [IUnknown::Release](http://msdn.microsoft.com/library/com/htm/cmi_q2z_59np.asp) method after use.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





