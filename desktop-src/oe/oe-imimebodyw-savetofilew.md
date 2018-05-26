---
title: IMimeBodyW SaveToFileW method
description: Saves the body data to a file in the specified encoding.
ms.assetid: 86980033-ce91-493b-afd3-a6b1ae37f3d9
keywords:
- SaveToFileW method Windows Mail (formerly Outlook Express)
- SaveToFileW method Windows Mail (formerly Outlook Express) , IMimeBodyW interface
- IMimeBodyW interface Windows Mail (formerly Outlook Express) , SaveToFileW method
topic_type:
- apiref
api_name:
- IMimeBodyW.SaveToFileW
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

# IMimeBodyW::SaveToFileW method

Saves the body data to a file in the specified encoding.

## Syntax


```C++
HRESULT SaveToFileW(
  [in] ENCODINGTYPE ietEncoding,
  [in] LPCWSTR      pwszFilePath
);
```



## Parameters

<dl> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies the [**ENCODINGTYPE**](oe-encodingtype.md) value to save the body data in.

</dd> <dt>

*pwszFilePath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies a **LPCWSTR** that contains the file path to save the body in and overwrites the specified file.

> [!Note]  
> MimeOLE requires write access to this file.

 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                  |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred.<br/>                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pwszFilePath* is **NULL**. <br/>                                                       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                                              |
| <dl> <dt>**MIME\_E\_INVALID\_ENCODINGTYPE**</dt> </dl> | Indicates that *ietEncoding* is greater than or equal to [**IET\_UNKNOWN**](oe-encodingtype.md).<br/> |



 

## Remarks

[**IET\_DECODED**](oe-encodingtype.md) is the most common value for *ietEncoding*. It causes all encodings to be removed.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





