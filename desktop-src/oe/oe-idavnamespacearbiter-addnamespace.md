---
title: IDAVNamespaceArbiter AddNamespace method
description: Adds the specified namespace to a list of namespaces and generates an ID.
ms.assetid: 9e5a9450-c7cd-4771-a7f4-5eb410fb8c35
keywords:
- AddNamespace method Windows Mail (formerly Outlook Express)
- AddNamespace method Windows Mail (formerly Outlook Express) , IDAVNamespaceArbiter interface
- IDAVNamespaceArbiter interface Windows Mail (formerly Outlook Express) , AddNamespace method
topic_type:
- apiref
api_name:
- IDAVNamespaceArbiter.AddNamespace
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

# IDAVNamespaceArbiter::AddNamespace method

\[**IDAVNamespaceArbiter::AddNamespace** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds the specified namespace to a list of namespaces and generates an ID.

## Syntax


```C++
HRESULT AddNamespace(
  [in]  LPCSTR pszNamespace,
  [out] DWORD  *pdwNamespaceID
);
```



## Parameters

<dl> <dt>

*pszNamespace* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the name of the namespace to add.

</dd> <dt>

*pdwNamespaceID* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the generated ID for *pszNamespace*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszNamespace* or *pdwNamespaceID* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>           |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





