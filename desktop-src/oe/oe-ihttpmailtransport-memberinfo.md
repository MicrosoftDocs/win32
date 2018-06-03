---
title: IHTTPMailTransport MemberInfo method
description: Returns properties for the specified resource.
ms.assetid: e9052ac0-4c8b-4a2f-a436-c4dc88ebe065
keywords:
- MemberInfo method Windows Mail (formerly Outlook Express)
- MemberInfo method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , MemberInfo method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.MemberInfo
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

# IHTTPMailTransport::MemberInfo method

\[**IHTTPMailTransport::MemberInfo** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns properties for the specified resource.

## Syntax


```C++
HRESULT MemberInfo(
  [in] LPCSTR          pszPath,
  [in] MEMBERINFOFLAGS flags,
  [in] DWORD           dwDepth,
  [in] BOOL            fIncludeRoot,
  [in] DWORD           dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **[**MEMBERINFOFLAGS**](oe-memberinfoflags-constants.md)**

Specifies [**MEMBERINFOFLAGS**](oe-memberinfoflags-constants.md) values that indicate which properties should be requested for the resource specified by *pszPath*.

</dd> <dt>

*dwDepth* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that indicates the value of the DEPTH request header.



| Value                                                                                                                                                                                                                            | Meaning                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt></dt> <dt>0</dt> </dl>                                                                                               | Apply only to the specified resource. <br/>                   |
| <dl> <dt></dt> <dt>1</dt> </dl>                                                                                               | Apply to the specified resource and its children. <br/>       |
| <span id="DEPTH_INFINITY"></span><span id="depth_infinity"></span><dl> <dt>**DEPTH\_INFINITY**</dt> <dt>0xFFFFFFFE</dt> </dl> | Apply to the specified resource and to all descendants. <br/> |



 

</dd> <dt>

*fIncludeRoot* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether to exclude the resource and apply the command only to its childen by including the "noroot" token in the DEPTH header. If *dwDepth* is **0** then this parameter must be **FALSE**.



| Value                                                                                                                                                                                      | Meaning                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> <dt></dt> </dl> | Do not include the "noroot" token in the DEPTH header. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> <dt></dt> </dl>    | Include the "noroot" token in the DEPTH header. <br/>        |



 

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* is **NULL**. <br/>                |
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



 

 





