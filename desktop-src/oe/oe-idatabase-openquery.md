---
title: IDatabase OpenQuery method
description: After this function is called, any notifications will be queued instead of sent directly to the IDatabaseNotify.
ms.assetid: '0dd322fc-d686-4add-932a-cdebae28830a'
keywords: ["OpenQuery method Windows Mail (formerly Outlook Express)", "OpenQuery method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , OpenQuery method"]
topic_type:
- apiref
api_name:
- IDatabase.OpenQuery
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::OpenQuery method

After this function is called, any notifications will be queued instead of sent directly to the IDatabaseNotify. If called on the same thread that RegisterNotify was called on, it will first dispatch any queued notifications. Notifications will resume when ResumeNotify.

## Syntax


```C++
void OpenQuery(
  [in] IDatabaseNotify *pNotify
);
```



## Parameters

<dl> <dt>

*pNotify* \[in\]
</dt> <dd>

Type: **IDatabaseNotify\***

Specifies the IDatabaseNotify that will have its notifications suspended.

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



 

 





