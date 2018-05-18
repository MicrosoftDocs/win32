---
title: IMimeMessage AttachObject method
description: Attaches an object to the message. The data source of the message attachment is a Component Object Model (COM) object.
ms.assetid: '16a1dee8-ed94-4ea0-951c-f722a6a076ac'
keywords: ["AttachObject method Windows Mail (formerly Outlook Express)", "AttachObject method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , AttachObject method"]
topic_type:
- apiref
api_name:
- IMimeMessage.AttachObject
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::AttachObject method

Attaches an object to the message. The data source of the message attachment is a Component Object Model (COM) object.

## Syntax


```C++
HRESULT AttachObject(
  [in]  REFIID  riid,
  [in]  void    *pvObject,
  [out] LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the type of object that *pvObject* points at. Valid values include:

<dl> <dt>

 (IID\_IStream)
</dt> <dt>

 (IID\_ILockBytes)
</dt> <dt>

 (IID\_IMimeBody)
</dt> <dt>

 (IID\_IMimeMessage)
</dt> <dt>

 (IID\_IMimeWebDocument)
</dt> </dl> </dd> <dt>

*pvObject* \[in\]
</dt> <dd>

Type: **void\***

Specifies a pointer to the object in which to create the attachment. MimeOLE increments the reference count for this object and does not release it until the whole message object is freed or until [**HandsOffStorage**](oe-imimemessagetree-handsoffstorage.md) is called.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the new body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *riid* or *pvObject* is **NULL**.<br/>     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

This method creates the attachment in the multipart/mixed section of the message. It creates a multipart/mixed section if one does not exist.

Data in the object that *pvObject* points to must be stored in either [**IET\_BINARY**](oe-encodingtype.md) or **IET\_DECODED** type. For more information, see **ENCODINGTYPE**.

This method sets the PID\_HDR\_CNTDISP property of the new body to "attachment".

After successfully calling this method, a client should use *phBody* to set the PID\_HDR\_CNTTYPE property to a value that corresponds to the type of data stored in *pvObject*.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





