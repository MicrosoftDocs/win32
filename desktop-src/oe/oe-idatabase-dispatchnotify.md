---
title: IDatabase DispatchNotify method
description: Dispatches any pending notifications.
ms.assetid: 42cf8c88-4968-4908-a1d2-ba31b4f0bea6
keywords:
- DispatchNotify method Windows Mail (formerly Outlook Express)
- DispatchNotify method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , DispatchNotify method
topic_type:
- apiref
api_name:
- IDatabase.DispatchNotify
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

# IDatabase::DispatchNotify method

\[**DispatchNotify** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Dispatches any pending notifications. Note that this function must be called on the same thread that RegisterNotify was called on. This function will return after all queued notifications have been dispatched.

## Syntax


```C++
HRESULT DispatchNotify(
  [in] IDatabaseNotify *pNotify
);
```



## Parameters

<dl> <dt>

*pNotify* \[in\]
</dt> <dd>

Type: **IDatabaseNotify\***

Specifies the IDatabaseNotify that will be notified.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                       | Description                                                                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Indicates no errors occurred.<br/>                                                                   |
| <dl> <dt>**DB\_E\_WRONGTHREAD**</dt> </dl> | Indicates that the function was called on a different thread than RegisterNotify was called on.<br/> |
| <dl> <dt>**DB\_E\_NOTFOUND**</dt> </dl>    | Indicates that pNotify has not been properly regsitered for notifications.<br/>                      |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





