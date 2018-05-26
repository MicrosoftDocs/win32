---
title: IHTTPMailTransport2 FolderMemberInfo method
description: Returns the properties for the specified collection resource.
ms.assetid: e1254fe6-ad26-4ee2-9fce-4ba54f5f0f4a
keywords:
- FolderMemberInfo method Windows Mail (formerly Outlook Express)
- FolderMemberInfo method Windows Mail (formerly Outlook Express) , IHTTPMailTransport2 interface
- IHTTPMailTransport2 interface Windows Mail (formerly Outlook Express) , FolderMemberInfo method
topic_type:
- apiref
api_name:
- IHTTPMailTransport2.FolderMemberInfo
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

# IHTTPMailTransport2::FolderMemberInfo method

\[**IHTTPMailTransport2::FolderMemberInfo** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the properties for the specified collection resource.

## Syntax


```C++
HRESULT FolderMemberInfo(
  [in] LPCSTR          pszPath,
  [in] MEMBERINFOFLAGS flags,
  [in] DWORD           dwDepth,
  [in] BOOL            fIncludeRoot,
  [in] DWORD           dwContext,
  [in] LPCSTR          pszFolderTimeStamp,
  [in] LPCSTR          pszFolderName
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the collection resource.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **[**MEMBERINFOFLAGS**](oe-memberinfoflags-constants.md)**

Specifies one or more values from the [**MEMBERINFOFLAGS**](oe-memberinfoflags-constants.md) enumeration.

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

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*pszFolderTimeStamp* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the timestamp to log.

</dd> <dt>

*pszFolderName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains folder name.

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



 

 





