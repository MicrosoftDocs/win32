---
title: IHTTPMailTransport FindFolders method
description: Discovers the collection hierarchy that exists underneath the URL to the root of the folder hierarchy.
ms.assetid: 'cc11d365-269b-4015-8a20-e57172dfdd86'
keywords: ["FindFolders method Windows Mail (formerly Outlook Express)", "FindFolders method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface", "IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , FindFolders method"]
topic_type:
- apiref
api_name:
- IHTTPMailTransport.FindFolders
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHTTPMailTransport::FindFolders method

\[**IHTTPMailTransport::FindFolders** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Discovers the collection hierarchy that exists underneath the URL to the root of the folder hierarchy. The response is identical to the MemberInfo response. This method causes a non-DAV 1.0 verb (SEARCH) to be sent to the server. Callers should be prepared to fallback to other forms of folder discovery if this method fails.

## Syntax


```C++
HRESULT FindFolders(
  [in] LPCSTR pszPath,
  [in] DWORD  dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the root of the folder hierarchy. The collection at *pszPath* is excluded from the response.

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





