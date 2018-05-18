---
title: IRangeList Clear method
description: Clears the entries from the message range list.
ms.assetid: '3c8496a8-43ee-4fa3-ba23-33e2bfcb8cf9'
keywords: ["Clear method Windows Mail (formerly Outlook Express)", "Clear method Windows Mail (formerly Outlook Express) , IRangeList interface", "IRangeList interface Windows Mail (formerly Outlook Express) , Clear method"]
topic_type:
- apiref
api_name:
- IRangeList.Clear
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRangeList::Clear method

\[**IRangeList::Clear** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Clears the entries from the message range list. No memory is freed by this operation.

## Syntax


```C++
HRESULT Clear();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





