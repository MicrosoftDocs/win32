---
title: IRangeList Cardinality method
description: Counts the members in the message range list.
ms.assetid: 86af4a86-986a-4b56-821e-e3d127d05ae3
keywords:
- Cardinality method Windows Mail (formerly Outlook Express)
- Cardinality method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , Cardinality method
topic_type:
- apiref
api_name:
- IRangeList.Cardinality
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

# IRangeList::Cardinality method

\[**IRangeList::Cardinality** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Counts the members in the message range list.

## Syntax


```C++
HRESULT Cardinality(
   ULONG *pulCardinality
);
```



## Parameters

<dl> <dt>

*pulCardinality* 
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the total number of members in the range list. A value of zero indicates that the range list is empty.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example, for the range list "10 20,31,44,50 65", **Cardinality**(&pulCardinality) returns 29.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





