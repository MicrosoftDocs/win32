---
title: IHTTPMailTransport CommandPROPFIND method
description: Sends the PROPFIND command to the HTTPMail server.
ms.assetid: 5c947f74-c31a-46d0-8d27-80d6e9b1922f
keywords:
- CommandPROPFIND method Windows Mail (formerly Outlook Express)
- CommandPROPFIND method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandPROPFIND method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandPROPFIND
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

# IHTTPMailTransport::CommandPROPFIND method

\[**IHTTPMailTransport::CommandPROPFIND** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the PROPFIND command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandPROPFIND(
  [in] LPCSTR           pszPath,
  [in] IPropFindRequest *pRequest,
  [in] DWORD            dwDepth,
  [in] DWORD            dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource.

</dd> <dt>

*pRequest* \[in\]
</dt> <dd>

Type: **[**IPropFindRequest**](oe-ipropfindrequest.md)\***

Specifies the property request object.

</dd> <dt>

*dwDepth* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the depth of request.



| Value                                                                                                                                                                                                                            | Meaning                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt></dt> <dt>0</dt> </dl>                                                                                               | Apply only to the specified resource. <br/>                   |
| <dl> <dt></dt> <dt>1</dt> </dl>                                                                                               | Apply to the specified resource and its children. <br/>       |
| <span id="DEPTH_INFINITY"></span><span id="depth_infinity"></span><dl> <dt>**DEPTH\_INFINITY**</dt> <dt>0xFFFFFFFE</dt> </dl> | Apply to the specified resource and to all descendants. <br/> |



 

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* or *pRequest* is **NULL**. <br/>  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





