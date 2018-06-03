---
title: IHashTable Reset method
description: Resets the enumerator to the beginning of the table.
ms.assetid: e55f888c-4d51-49e1-a6d6-275f574256b1
keywords:
- Reset method Windows Mail (formerly Outlook Express)
- Reset method Windows Mail (formerly Outlook Express) , IHashTable interface
- IHashTable interface Windows Mail (formerly Outlook Express) , Reset method
topic_type:
- apiref
api_name:
- IHashTable.Reset
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

# IHashTable::Reset method

\[**IHashTable::Reset** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resets the enumerator to the beginning of the table.

## Syntax


```C++
HRESULT Reset();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                                                  |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The enumerator is at the beginning of the table. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





