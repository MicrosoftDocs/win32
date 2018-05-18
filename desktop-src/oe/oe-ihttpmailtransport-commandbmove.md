---
title: IHTTPMailTransport CommandBMOVE method
description: Sends the BMOVE command to the HTTPMail server.
ms.assetid: '3397214c-44be-459e-8094-75c9ff23391e'
keywords: ["CommandBMOVE method Windows Mail (formerly Outlook Express)", "CommandBMOVE method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface", "IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandBMOVE method"]
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandBMOVE
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHTTPMailTransport::CommandBMOVE method

\[**IHTTPMailTransport::CommandBMOVE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the BMOVE command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandBMOVE(
  [in] LPCSTR           pszSourceCollection,
  [in] LPHTTPTARGETLIST pTargets,
  [in] LPCSTR           pszDestCollection,
  [in] LPHTTPTARGETLIST pDestinations,
  [in] BOOL             fAllowRename,
  [in] DWORD            dwContext
);
```



## Parameters

<dl> <dt>

*pszSourceCollection* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the collection resource that contains the target resources.

</dd> <dt>

*pTargets* \[in\]
</dt> <dd>

Type: **LPHTTPTARGETLIST**

Specifies a pointer to a [**HTTPTARGETLIST**](oe-httptargetlist.md) structure that contains the list of target resources to move.

</dd> <dt>

*pszDestCollection* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the collection resource that contains the destination resources.

</dd> <dt>

*pDestinations* \[in\]
</dt> <dd>

Type: **LPHTTPTARGETLIST**

Specifies a pointer to a [**HTTPTARGETLIST**](oe-httptargetlist.md) structure that contains the list of destination resources that exactly match up with the target resources specified by *pTargets*.

</dd> <dt>

*fAllowRename* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether the destination resources already exist and should be overwritten.



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



| Return code                                                                                   | Description                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszSourceCollection*, *pTargets*, or *pszDestCollection* is **NULL** or that *pTargets* and *pDestinations* structures are of unequal length. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                                                                                                          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





