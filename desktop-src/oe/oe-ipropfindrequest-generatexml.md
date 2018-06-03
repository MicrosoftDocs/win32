---
title: IPropFindRequest GenerateXML method
description: IPropFindRequest GenerateXML method
ms.assetid: ea7316ed-1a32-4840-b6af-429b0e96e5cd
keywords:
- GenerateXML method Windows Mail (formerly Outlook Express)
- GenerateXML method Windows Mail (formerly Outlook Express) , IPropFindRequest interface
- IPropFindRequest interface Windows Mail (formerly Outlook Express) , GenerateXML method
topic_type:
- apiref
api_name:
- IPropFindRequest.GenerateXML
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

# IPropFindRequest::GenerateXML method

\[**IPropFindRequest::GenerateXML** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT GenerateXML(
  [out] LPSTR *pszXML
);
```



## Parameters

<dl> <dt>

*pszXML* \[out\]
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



 

 





