---
title: IDAVNamespaceArbiter GetNamespaceID method
description: Retrieves the ID for the specified namespace.
ms.assetid: a7989228-60c7-403b-8a82-2c02b7662ad8
keywords:
- GetNamespaceID method Windows Mail (formerly Outlook Express)
- GetNamespaceID method Windows Mail (formerly Outlook Express) , IDAVNamespaceArbiter interface
- IDAVNamespaceArbiter interface Windows Mail (formerly Outlook Express) , GetNamespaceID method
topic_type:
- apiref
api_name:
- IDAVNamespaceArbiter.GetNamespaceID
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

# IDAVNamespaceArbiter::GetNamespaceID method

\[**IDAVNamespaceArbiter::GetNamespaceID** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the ID for the specified namespace.

## Syntax


```C++
HRESULT GetNamespaceID(
  [in]  LPCSTR pszNamespace,
  [out] DWORD  *pdwNamespaceID
);
```



## Parameters

<dl> <dt>

*pszNamespace* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the name of the namespace.

</dd> <dt>

*pdwNamespaceID* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the namespace ID for *pszNamespace*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszNamespace* or *pdwNamespaceID* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





