---
title: IRangeList Load method
description: Replaces the internal message range list representation with one saved by the IRangeList Save method.
ms.assetid: cf023226-31f7-4f31-a32c-2b807953653f
keywords:
- Load method Windows Mail (formerly Outlook Express)
- Load method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , Load method
topic_type:
- apiref
api_name:
- IRangeList.Load
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

# IRangeList::Load method

\[**IRangeList::Load** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Replaces the internal message range list representation with one saved by the [**IRangeList::Save**](oe-irangelist-save.md) method.

## Syntax


```C++
HRESULT Load(
  [in]       byte  *pbSource,
  [in] const ULONG ulSizeOfSource
);
```



## Parameters

<dl> <dt>

*pbSource* \[in\]
</dt> <dd>

Type: **byte\***

Specifies a pointer to the saved internal range list representation to load.

</dd> <dt>

*ulSizeOfSource* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies a **ULONG** that contains the size of the data pointed to by *pbSource*.

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



 

 





