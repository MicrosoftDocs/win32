---
title: IMimeEditTagCollection Init method
description: Initializes a document for inclusion in the collection.
ms.assetid: a9d3bd25-4256-4208-b4a5-bb6846b02dbb
keywords:
- Init method Windows Mail (formerly Outlook Express)
- Init method Windows Mail (formerly Outlook Express) , IMimeEditTagCollection interface
- IMimeEditTagCollection interface Windows Mail (formerly Outlook Express) , Init method
topic_type:
- apiref
api_name:
- IMimeEditTagCollection.Init
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

# IMimeEditTagCollection::Init method

\[**IMimeEditTagCollection::Init** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes a document for inclusion in the collection.

## Syntax


```C++
HRESULT Init(
  [in] IUnknown *pHtmlDoc
);
```



## Parameters

<dl> <dt>

*pHtmlDoc* \[in\]
</dt> <dd>

Type: **[IUnknown](http://msdn.microsoft.com/library/com/htm/cmi_q2z_9dwu.asp)\***

Specifies the document to initialize.

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
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





