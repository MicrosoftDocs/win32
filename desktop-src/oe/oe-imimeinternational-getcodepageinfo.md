---
title: IMimeInternational GetCodePageInfo method
description: Gets information about the specified code page.
ms.assetid: 3da4f262-5ab1-4b95-aba0-0206640658c1
keywords:
- GetCodePageInfo method Windows Mail (formerly Outlook Express)
- GetCodePageInfo method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , GetCodePageInfo method
topic_type:
- apiref
api_name:
- IMimeInternational.GetCodePageInfo
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

# IMimeInternational::GetCodePageInfo method

Gets information about the specified code page.

## Syntax


```C++
HRESULT GetCodePageInfo(
  [in]      CODEPAGEID     cpiCodePage,
  [in, out] LPCODEPAGEINFO pCodePageInfo
);
```



## Parameters

<dl> <dt>

*cpiCodePage* \[in\]
</dt> <dd>

Type: **[**CODEPAGEID**](oe-codepageid-constants.md)**

Specifies the code page ID. For more information, see [**CODEPAGEID**](oe-codepageid-constants.md).

</dd> <dt>

*pCodePageInfo* \[in, out\]
</dt> <dd>

Type: **LPCODEPAGEINFO**

Receives a pointer to a [**CODEPAGEINFO**](oe-codepageinfo.md) structure that contains information about the code page.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                             |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pCodePageInfo* is **NULL**. <br/>                 |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *cpiCodePage* is invalid or cannot be found. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>         |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





