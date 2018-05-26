---
title: IHTTPMailTransport CommandPUT method
description: Sends the PUT command to the HTTPMail server.
ms.assetid: 9d326a2c-3523-4031-8e88-7d1f645d2f52
keywords:
- CommandPUT method Windows Mail (formerly Outlook Express)
- CommandPUT method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandPUT method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandPUT
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

# IHTTPMailTransport::CommandPUT method

\[**IHTTPMailTransport::CommandPUT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the PUT command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandPUT(
  [in] LPCSTR pszPath,
  [in] LPVOID lpvData,
  [in] ULONG  cbSize,
  [in] DWORD  dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL under which the entity should be stored.

</dd> <dt>

*lpvData* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies a **LPVOID** that contains the data to send to the server.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the size in bytes of *lpvData*.

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* or *lpvData* is **NULL** or *cbSize* is zero. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                   |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





