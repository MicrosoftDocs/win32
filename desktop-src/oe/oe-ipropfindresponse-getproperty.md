---
title: IPropFindResponse GetProperty method
description: IPropFindResponse GetProperty method
ms.assetid: 8cd72061-0f7e-4bbc-b3e9-d5e375d86b33
keywords:
- GetProperty method Windows Mail (formerly Outlook Express)
- GetProperty method Windows Mail (formerly Outlook Express) , IPropFindResponse interface
- IPropFindResponse interface Windows Mail (formerly Outlook Express) , GetProperty method
topic_type:
- apiref
api_name:
- IPropFindResponse.GetProperty
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

# IPropFindResponse::GetProperty method

\[**IPropFindResponse::GetProperty** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT GetProperty(
  [in]  DWORD  dwNamespaceID,
  [in]  LPCSTR pszPropertyName,
  [out] LPSTR  *ppszPropertyValue
);
```



## Parameters

<dl> <dt>

*dwNamespaceID* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*pszPropertyName* \[in\]
</dt> <dd>

Type: **LPCSTR**

</dd> <dt>

*ppszPropertyValue* \[out\]
</dt> <dd>

Type: **LPSTR\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





