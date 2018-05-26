---
title: MimeOleOpenFileStream function
description: Do not use. Opens or, if non-existing, creates a file stream with specified read/write properties.
ms.assetid: a30593f4-8f9c-4ff6-8986-e73312528d37
keywords:
- MimeOleOpenFileStream function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleOpenFileStream
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleOpenFileStream function

Do not use. Opens or, if non-existing, creates a file stream with specified read/write properties.

## Syntax


```C++
HRESULT MimeOleOpenFileStream(
  _In_  LPCSTR  pszFilePath,
  _In_  DWORD   dwCreationDistribution,
  _In_  DWORD   dwAccess,
  _Out_ IStream **ppstmFile
);
```



## Parameters

<dl> <dt>

*pszFilePath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the file path.

</dd> <dt>

*dwCreationDistribution* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies whether file should be created if it does not exist.

</dd> <dt>

*dwAccess* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies whether file is to be opened for write.

</dd> <dt>

*ppstmFile* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Receives the address of a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the stream to be opened/created.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                          |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszFilePath* or *ppstmFile* is **NULL**. <br/> |



 

## Remarks

> [!Note]  
> User of this function is responsible for freeing the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object pointed to by *ppstmFile*.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





