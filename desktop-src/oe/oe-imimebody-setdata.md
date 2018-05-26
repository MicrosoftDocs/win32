---
title: IMimeBody SetData method
description: Sets the data for the body.
ms.assetid: 8617e31d-1c87-4cf4-8650-252770a3cfc8
keywords:
- SetData method Windows Mail (formerly Outlook Express)
- SetData method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , SetData method
topic_type:
- apiref
api_name:
- IMimeBody.SetData
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

# IMimeBody::SetData method

Sets the data for the body.

## Syntax


```C++
HRESULT SetData(
  [in] ENCODINGTYPE ietEncoding,
  [in] LPCSTR       pszPriType,
  [in] LPCSTR       pszSubType,
  [in] REFIID       riid,
  [in] LPVOID       pvObject
);
```



## Parameters

<dl> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the current [**ENCODINGTYPE**](oe-encodingtype.md) for the data store in *pvObject*.

</dd> <dt>

*pszPriType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp), for example, multipart or text. MimeOLE sets the PID\_ATT\_PRITYPE property for this body.

</dd> <dt>

*pszSubType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the secondary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp), for example, mixed or html. MimeOLE sets the PID\_ATT\_SUBTYPE property for this body.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the type of interface object in the *pvObject* parameter. Valid values for this parameter include:



| Value                                                                                                                                                                                                                     | Meaning                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="IID_IStream"></span><span id="iid_istream"></span><span id="IID_ISTREAM"></span><dl> <dt>**IID\_IStream**</dt> </dl>                                     |                                           |
| <span id="IID_ILockBytes"></span><span id="iid_ilockbytes"></span><span id="IID_ILOCKBYTES"></span><dl> <dt>**IID\_ILockBytes**</dt> </dl>                         |                                           |
| <span id="IID_IMimeBody"></span><span id="iid_imimebody"></span><span id="IID_IMIMEBODY"></span><dl> <dt>**IID\_IMimeBody**</dt> </dl>                             |                                           |
| <span id="IID_IMimeMessage"></span><span id="iid_imimemessage"></span><span id="IID_IMIMEMESSAGE"></span><dl> <dt>**IID\_IMimeMessage**</dt> </dl>                 | Creates a message/rfc822 body.<br/> |
| <span id="IID_IMimeWebDocument"></span><span id="iid_imimewebdocument"></span><span id="IID_IMIMEWEBDOCUMENT"></span><dl> <dt>**IID\_IMimeWebDocument**</dt> </dl> |                                           |



 

</dd> <dt>

*pvObject* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies a pointer to the storage object. The type of object must match the type specified in the *riid* parameter. MimeOLE adds a reference for this object and holds onto it until the whole message object is freed or until [**HandsOffStorage**](oe-imimemessagetree-handsoffstorage.md) is called.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                                                                                                                                                               |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                                                                                                                                                                    |
| <dl> <dt>**MIME\_E\_MULTIPART\_NO\_DATA**</dt> </dl> | Indicates that the body has a multipart primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) and setting data on this body type is not allowed. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *riid* is not a supported interface ID, that *pvObject* is **NULL**, or that *ietEncoding* is greater than or equal to [**IET\_UNKNOWN**](oe-encodingtype.md).<br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                             |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





