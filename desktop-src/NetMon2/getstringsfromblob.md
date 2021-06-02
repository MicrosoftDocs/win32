---
description: Uses sequential calls to retrieve all of the strings within specified ranges.
ms.assetid: 4e819975-84a5-4b73-9a19-792d3607da9c
title: GetStringsFromBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetStringsFromBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetStringsFromBlob function

The **GetStringsFromBlob** function uses sequential calls to retrieve all of the strings within specified ranges.

## Syntax


```C++
DWORD GetStringsFromBlob(
  _In_        HBLOB hBlob,
  _In_  const char  *pRequestedOwnerName,
  _In_  const char  *pRequestedCategoryName,
  _In_  const char  *pRequestedTagName,
  _Out_ const char  **ppReturnedOwnerName,
  _Out_ const char  **ppReturnedCategoryName,
  _Out_ const char  **ppReturnedTagName,
  _Out_ const char  **ppReturnedString,
  _Out_       DWORD *pRestartKey
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

A handle to the BLOB.

</dd> <dt>

*pRequestedOwnerName* \[in\]
</dt> <dd>

A pointer to the Owner section to get the string from.

</dd> <dt>

*pRequestedCategoryName* \[in\]
</dt> <dd>

A pointer to the Category section to get the string from.

</dd> <dt>

*pRequestedTagName* \[in\]
</dt> <dd>

A pointer to the tag for the requested string.

</dd> <dt>

*ppReturnedOwnerName* \[out\]
</dt> <dd>

A pointer to the variable that points to where the **Owner** name will be returned.

</dd> <dt>

*ppReturnedCategoryName* \[out\]
</dt> <dd>

A pointer to the variable that points to where the **Category** name will be returned.

</dd> <dt>

*ppReturnedTagName* \[out\]
</dt> <dd>

A pointer to the variable that points to where the **Tag** name will be returned.

</dd> <dt>

*ppReturnedString* \[out\]
</dt> <dd>

A pointer to the variable that points to where the string name will be returned.

</dd> <dt>

*pRestartKey* \[out\]
</dt> <dd>

A pointer to the variable where the restart key will be specified and returned.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the problem.

If a specified combination of **Owner**, **Category**, and **Tag** information does not exist, the return value is **NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST**.

When the BLOB is traversed completely within the bounds initially specified, the function returns **NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST**, and the *pRestartKey* parameter points to zero.

## Remarks

On the initial call to the **GetStringsFromBlob** function, the *pRestartKey* parameter points to a variable that contains the value zero. The *pRequested* parameters can be used only when the restart key is zero. In subsequent calls, when *pRestartKey* has nonzero values, the *pRequested* parameters are ignored. On the initial call, all may point to **NULL**, which sets up the query to return every entry in the BLOB, one per subsequent call.

Specifying an owner limits the strings returned to just that owner. A similar limitation is true for categories and tags, with the additional caveat that if a category is specified, an owner must also be specified and if a tag is specified, a category (and therefore an owner) must be specified.

When the initial call to **GetStringsFromBlob** returns, *pRestartKey* points to a new value, which should be specified on the next call to the function to get the next value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



## See also

<dl> <dt>

[SetStringInBlob](setstringinblob.md)
</dt> <dt>

[GetBoolFromBlob](getboolfromblob.md)
</dt> <dt>

[GetClassIDFromBlob](getclassidfromblob.md)
</dt> <dt>

[GetDwordFromBlob](getdwordfromblob.md)
</dt> <dt>

[GetMacAddressFromBlob](getmacaddressfromblob.md)
</dt> <dt>

[GetNetworkInfoFromBlob](getnetworkinfofromblob.md)
</dt> <dt>

[GetNPPAddressFilterFromBlob](getnppaddressfilterfromblob.md)
</dt> <dt>

[GetNPPPatternFilterFromBlob](getnpppatternfilterfromblob.md)
</dt> <dt>

[GetNPPTriggerFromBlob](getnpptriggerfromblob.md)
</dt> <dt>

[GetStringFromBlob](getstringfromblob.md)
</dt> </dl>

 

 




