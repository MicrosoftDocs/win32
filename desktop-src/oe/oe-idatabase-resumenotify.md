---
title: IDatabase ResumeNotify method
description: Tells the database to resume sending notifications to the given IDatabaseNotify.
ms.assetid: 'b828d912-1bf4-4f1b-8046-2b7c390564b2'
keywords: ["ResumeNotify method Windows Mail (formerly Outlook Express)", "ResumeNotify method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , ResumeNotify method"]
topic_type:
- apiref
api_name:
- IDatabase.ResumeNotify
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::ResumeNotify method

Tells the database to resume sending notifications to the given IDatabaseNotify.

## Syntax


```C++
void ResumeNotify(
  [in] IDatabaseNotify *pNotify
);
```



## Parameters

<dl> <dt>

*pNotify* \[in\]
</dt> <dd>

Type: **IDatabaseNotify\***

Specifies the IDatabaseNotify that will have its notifications resumed.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





