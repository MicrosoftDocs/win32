---
title: IDatabase RegisterNotify method
description: Registers an object implementing the IDatabaseNotify interface with the database.
ms.assetid: 'fd58746d-bf17-480a-9d3a-1421f22a850a'
keywords: ["RegisterNotify method Windows Mail (formerly Outlook Express)", "RegisterNotify method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , RegisterNotify method"]
topic_type:
- apiref
api_name:
- IDatabase.RegisterNotify
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::RegisterNotify method

\[**RegisterNotify** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Registers an object implementing the IDatabaseNotify interface with the database. It will be called when transactions affect a member of the index specified by iIndex.

## Syntax


```C++
HRESULT RegisterNotify(
  [in] INDEXORDINAL        iIndex,
  [in] REGISTERNOTIFYFLAGS dwFlags,
  [in] DWORD_PTR           dwCookie,
  [in] IDatabaseNotify     *pNotify
);
```



## Parameters

<dl> <dt>

*iIndex* \[in\]
</dt> <dd>

Type: **[**INDEXORDINAL**](oe-indexordinal.md)**

Specifies the index to be monitored for changes

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **[**REGISTERNOTIFYFLAGS**](oe-registernotifyflags.md)**

Specifies the options to modify the notifications and how the IDatabaseNotify interface is handled.

</dd> <dt>

*dwCookie* \[in\]
</dt> <dd>

Type: **DWORD\_PTR**

Specifies the value that will be used for the dwCookie value when IDatabaseNotify::OnTransaction is called.

</dd> <dt>

*pNotify* \[in\]
</dt> <dd>

Type: **IDatabaseNotify\***

The IDatabaseNotify interface that is being registered.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.



| Return code                                                                                             | Description                                                                            |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates the IDatabaseNotify object could be registered for notifications.<br/> |
| <dl> <dt>**DB\_E\_ALREADYREGISTERED**</dt> </dl> | Indicates pNotify has already been registered for notifications.<br/>            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





