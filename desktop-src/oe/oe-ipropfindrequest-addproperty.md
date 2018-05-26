---
title: IPropFindRequest AddProperty method
description: IPropFindRequest AddProperty method
ms.assetid: f4b398fc-a3a6-4103-8af1-a0ff6ca3aa49
keywords:
- AddProperty method Windows Mail (formerly Outlook Express)
- AddProperty method Windows Mail (formerly Outlook Express) , IPropFindRequest interface
- IPropFindRequest interface Windows Mail (formerly Outlook Express) , AddProperty method
topic_type:
- apiref
api_name:
- IPropFindRequest.AddProperty
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

# IPropFindRequest::AddProperty method

\[**IPropFindRequest::AddProperty** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT AddProperty(
  [in] DWORD  dwNamespaceID,
  [in] LPCSTR pszPropertyName
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



 

 





