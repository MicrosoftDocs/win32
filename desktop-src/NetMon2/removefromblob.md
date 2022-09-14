---
description: The RemoveFromBlob function deletes any level of BLOB entry (Owner, Category, or Tag).
ms.assetid: b8bb01e0-8b97-4c95-96f5-f2a30c8700e9
title: RemoveFromBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RemoveFromBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# RemoveFromBlob function

The **RemoveFromBlob** function deletes any level of BLOB entry (**Owner**, **Category**, or **Tag**).

## Syntax


```C++
DWORD RemoveFromBlob(
  _In_       HBLOB hBlob,
  _In_ const char  *pOwnerName,
  _In_ const char  *pCategoryName,
  _In_ const char  *pTagName
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the BLOB from which an entry is deleted.

</dd> <dt>

*pOwnerName* \[in\]
</dt> <dd>

Pointer to the **Owner** name.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

Pointer to the **Category** name. A **NULL** parameter value indicates the caller is attempting to delete the given **Owner** information and all of its child entries. Note that if the *pCategoryName* parameter value is **NULL**, the *pTagName* parameter must also be **NULL**.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

Pointer to the **Tag** name. A **NULL***pTagName* value indicates the caller is attempting to delete the given **Category** and all of its child entries. If the parameter value is not **NULL**, the caller is asking that only that the specified **Tag** entries be deleted.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 




