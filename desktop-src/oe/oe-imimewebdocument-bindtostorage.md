---
title: IMimeWebDocument BindToStorage method
description: Obtains an interface that can be used to read the data associated with the Web document.
ms.assetid: 44fc40a4-79d4-490e-aa60-870ae1f0ae69
keywords:
- BindToStorage method Windows Mail (formerly Outlook Express)
- BindToStorage method Windows Mail (formerly Outlook Express) , IMimeWebDocument interface
- IMimeWebDocument interface Windows Mail (formerly Outlook Express) , BindToStorage method
topic_type:
- apiref
api_name:
- IMimeWebDocument.BindToStorage
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

# IMimeWebDocument::BindToStorage method

\[**IMimeWebDocument::BindToStorage** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Obtains an interface that can be used to read the data associated with the Web document. An implementation should support IID\_IStream and IID\_ILockBytes as possible values.

## Syntax


```C++
HRESULT BindToStorage(
  [in]  REFIID riid,
  [out] LPVOID *ppvObject
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

Type: **REFIID**

Specifies the requested interface ID. Valid values for this parameter include: IID\_IStream or IID\_ILockBytes

</dd> <dt>

*ppvObject* \[out\]
</dt> <dd>

Type: **LPVOID\***

On success, contains a pointer to the requested storage object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                                            |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success. <br/>                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *ppvObject* is not a supported interface ID or is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>    | Indicates that an attempt to allocate memory failed. <br/>                       |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl> | Indicates that no storage object is available. <br/>                             |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





