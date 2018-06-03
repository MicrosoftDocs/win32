---
title: IMimeMessage GetSender method
description: Gets the sender of the message.
ms.assetid: 7fa56654-60cb-4564-97f5-3daf0d42215c
keywords:
- GetSender method Windows Mail (formerly Outlook Express)
- GetSender method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , GetSender method
topic_type:
- apiref
api_name:
- IMimeMessage.GetSender
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeMessage::GetSender method

Gets the sender of the message.

## Syntax


```C++
HRESULT GetSender(
  [in, out] LPADDRESSPROPS pAddress
);
```



## Parameters

<dl> <dt>

*pAddress* \[in, out\]
</dt> <dd>

Type: **LPADDRESSPROPS**

Receives the specified [**ADDRESSPROPS**](oe-addressprops.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                                                           |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred.<br/>                                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pAddress* is **NULL**.<br/>                                                     |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that a sender address cannot be found or that the sender header does not exist. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>                                       |



 

## Remarks

The sender is the value of the "From" header. If there is no "From" header, the sender is the value from the "Sender" header. If there is no "Sender" header, this method returns MIME\_E\_NOT\_FOUND.

This method is equivalent to:

pMessage-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(HBODY\_ROOT, IID\_IMimeAddressTable, (LPVOID \*)&pAddressTable);

pAddressTable-&gt;[**GetSender**](oe-imimeaddresstable-getsender.md)(*pAddress*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





