---
Description: 'Creates a key from a string.'
ms.assetid: '107138b9-96f0-4144-a4bc-7115b6deab60'
title: SdbMakeIndexKeyFromString function
---

# SdbMakeIndexKeyFromString function

Creates a key from a string.

## Syntax


```C++
ULONGLONG WINAPI SdbMakeIndexKeyFromString(
  _In_ LPCTSTR pwszKey
);
```



## Parameters

<dl> <dt>

*pwszKey* \[in\]
</dt> <dd>

The string.

</dd> </dl>

## Return value

The function returns the key or 0 if there is an error.

## Remarks

The standard index key is the first eight characters of the string, converted to upper case, then cast to a **ULONGLONG** value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



 

 




