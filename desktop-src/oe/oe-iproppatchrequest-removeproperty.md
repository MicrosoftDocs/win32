---
title: IPropPatchRequest RemoveProperty method
description: Adds the name of the property to the list of properties to remove.
ms.assetid: c45a63c0-99cd-4e75-8c5e-25c8190941a6
keywords:
- RemoveProperty method Windows Mail (formerly Outlook Express)
- RemoveProperty method Windows Mail (formerly Outlook Express) , IPropPatchRequest interface
- IPropPatchRequest interface Windows Mail (formerly Outlook Express) , RemoveProperty method
topic_type:
- apiref
api_name:
- IPropPatchRequest.RemoveProperty
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

# IPropPatchRequest::RemoveProperty method

\[**IPropPatchRequest::RemoveProperty** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds the name of the property to the list of properties to remove. The property name is prefixed with the namespace that contains it.

## Syntax


```C++
HRESULT RemoveProperty(
  [in] DWORD  dwNamespaceID,
  [in] LPCSTR pszPropertyName
);
```



## Parameters

<dl> <dt>

*dwNamespaceID* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the DAV namespace ID of the namespace that the property is part of. This parameter can be one of the following values.

<dl> <dt>

<span id="DAVNAMESPACE_DAV"></span><span id="davnamespace_dav"></span>**DAVNAMESPACE\_DAV** (0)
</dt> <dt>

<span id="DAVNAMESPACE_HOTMAIL"></span><span id="davnamespace_hotmail"></span>**DAVNAMESPACE\_HOTMAIL** (1)
</dt> <dt>

<span id="DAVNAMESPACE_HTTPMAIL"></span><span id="davnamespace_httpmail"></span>**DAVNAMESPACE\_HTTPMAIL** (2)
</dt> <dt>

<span id="DAVNAMESPACE_MAIL"></span><span id="davnamespace_mail"></span>**DAVNAMESPACE\_MAIL** (3)
</dt> <dt>

<span id="DAVNAMESPACE_CONTACTS"></span><span id="davnamespace_contacts"></span>**DAVNAMESPACE\_CONTACTS** (4)
</dt> </dl> </dd> <dt>

*pszPropertyName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the name of the property to remove.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *dwNamespaceID* is **NULL** or *pszPropertyName* is out of bounds. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                              |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





