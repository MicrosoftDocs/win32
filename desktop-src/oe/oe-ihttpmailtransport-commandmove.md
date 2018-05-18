---
title: IHTTPMailTransport CommandMOVE method
description: Sends the MOVE command to the HTTPMail server.
ms.assetid: '05499645-f402-480d-bbe6-7fff235de9c6'
keywords: ["CommandMOVE method Windows Mail (formerly Outlook Express)", "CommandMOVE method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface", "IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandMOVE method"]
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandMOVE
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHTTPMailTransport::CommandMOVE method

\[**IHTTPMailTransport::CommandMOVE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the MOVE command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandMOVE(
  [in] LPCSTR pszPath,
  [in] LPCSTR pszDestination,
  [in] BOOL   fAllowRename,
  [in] DWORD  dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource to move.

</dd> <dt>

*pszDestination* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the destination resource.

</dd> <dt>

*fAllowRename* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether the destination resource already exists and should be overwritten.



| Value                                                                                                                                                                                      | Meaning                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> <dt></dt> </dl> | Do not send the Overwrite request header. <br/>                 |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> <dt></dt> </dl>    | Send the Overwrite request header and set it to **TRUE**. <br/> |



 

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                           |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* or *pszDestination* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>      |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





