---
title: IDatabase Repair method
description: Will attempt to repair the database.
ms.assetid: 63b5803e-e2cf-41dc-a705-29f8d55c7442
keywords:
- Repair method Windows Mail (formerly Outlook Express)
- Repair method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , Repair method
topic_type:
- apiref
api_name:
- IDatabase.Repair
api_location:
- Directdb.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDatabase::Repair method

\[**Repair** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Will attempt to repair the database.

## Syntax


```C++
HRESULT Repair();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                        |
|----------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**SUCCESS**</dt> </dl> | The function succeeded.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





