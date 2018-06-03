---
title: HTTPMAILPROPFIND structure
description: Contains the response information for the PROPFIND command.
ms.assetid: fcecb19a-1f7b-49fd-92d1-5d81fe3d9bc0
keywords:
- HTTPMAILPROPFIND structure Windows Mail (formerly Outlook Express)
- LPHTTPMAILPROPFIND structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- HTTPMAILPROPFIND
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# HTTPMAILPROPFIND structure

\[**HTTPMAILPROPFIND** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the PROPFIND command.

## Syntax


```C++
typedef struct tagHTTPMAILPROPFIND {
  IPropFindMultiResponse *pMultiResponse;
} HTTPMAILPROPFIND, *LPHTTPMAILPROPFIND;
```



## Members

<dl> <dt>

**pMultiResponse**
</dt> <dd>

Type: **[**IPropFindMultiResponse**](oe-ipropfindmultiresponse.md)\***

</dd> <dd>

parsed propfind response

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





