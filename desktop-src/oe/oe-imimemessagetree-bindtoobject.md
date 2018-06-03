---
title: IMimeMessageTree BindToObject method
description: Obtains an interface in the message tree for the specified body.
ms.assetid: ca9cbf3c-6f6a-400c-9f18-0232d85ba970
keywords:
- BindToObject method Windows Mail (formerly Outlook Express)
- BindToObject method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , BindToObject method
topic_type:
- apiref
api_name:
- IMimeMessageTree.BindToObject
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

# IMimeMessageTree::BindToObject method

Obtains an interface in the message tree for the specified body.

## Syntax


```C++
HRESULT BindToObject(
  [in]  const HBODY  hBody,
  [in]        REFIID riid,
  [out]       void   **ppvObject
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **const HBODY**

Specifies a handle to a message body.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the interface ID to return.



| Value                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>IID\_IMimeAddressTable</dt> </dl> | Indicates the [**IMimeAddressTable**](oe-imimeaddresstable.md) interface for a body. <br/>                                                                                                                                                                         |
| <dl> <dt></dt> <dt>IID\_IMimeBody</dt> </dl>         | Indicates the [**IMimeBody**](oe-imimebody.md) interface for a body. <br/>                                                                                                                                                                                         |
| <dl> <dt></dt> <dt>IID\_IMimeHeaderTable</dt> </dl>  | Indicates the [**IMimeHeaderTable**](oe-imimeheadertable.md) interface for a body. <br/>                                                                                                                                                                           |
| <dl> <dt></dt> <dt>IID\_IMimeMessage</dt> </dl>      | Indicates the [**IMimeMessage**](oe-imimemessage.md) interface for a body that is a message attachment; for example, where [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) is "message/rfc822". <br/> |
| <dl> <dt></dt> <dt>IID\_IMimePropertySet</dt> </dl>  | Indicates the [**IMimePropertySet**](oe-imimepropertyset.md) interface for a body. <br/>                                                                                                                                                                           |
| <dl> <dt></dt> <dt>IID\_IStream</dt> </dl>           | Indicates the IET\_BINARY body data. This is equivalent to calling the following method. <br/> [**GetData**](oe-imimebody-getdata.md)(IET\_BINARY,&pStream);<br/>                                                                                            |
| <dl> <dt></dt> <dt>IID\_IUnicodeStream</dt> </dl>    | Indicates the IET\_UNICODE body data. This is equivalent to calling the following method. <br/> [**GetData**](oe-imimebody-getdata.md)(IET\_UNICODE,&pStream);<br/>                                                                                          |



 

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **void\*\***

Receives the address of a pointer to the requested object. The client is responsible for releasing the object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                        |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *ppvObject* is **NULL**. <br/>                                                |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>        | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hBody* is an invalid handle. <br/>                                           |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>           | Indicates that the interface ID specified by *riid* is not supported.<br/>                   |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





