---
title: IDatabase Compact method
description: Compacts the database.
ms.assetid: 15dcc347-e933-41a8-a978-b703b23d0e82
keywords:
- Compact method Windows Mail (formerly Outlook Express)
- Compact method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , Compact method
topic_type:
- apiref
api_name:
- IDatabase.Compact
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

# IDatabase::Compact method

\[**Compact** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Compacts the database.

## Syntax


```C++
HRESULT Compact(
  [in] IDatabaseProgress pProgress,
  [in] dwReserved        DWORD
);
```



## Parameters

<dl> <dt>

*pProgress* \[in\]
</dt> <dd>

Type: **[**IDatabaseProgress**](oe-idatabaseprogress.md)**

An IDatabaseProgress object that will have IDatabaseProgress::Update called periodically during the course of compaction.

</dd> <dt>

*DWORD* \[in\]
</dt> <dd>

Type: **dwReserved**

A reserved value, should always be 0.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                              | Description                                                                        |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | The function succeeded.<br/>                                                 |
| <dl> <dt>**DB\_E\_DATABASE\_CHANGED**</dt> </dl>  | Indicates the database has changed during the course of the compaction.<br/> |
| <dl> <dt>**DB\_E\_MOVEFILE**</dt> </dl>           | Indicates there was an error when attempting to move the database file.<br/> |
| <dl> <dt>**DB\_E\_COMPACT\_PREEMPTED**</dt> </dl> | Indicates that the compatct operation was preempted.<br/>                    |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





