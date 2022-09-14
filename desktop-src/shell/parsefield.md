---
description: Reads a line from Setup.inf and extracts the specified field from the string.
ms.assetid: 621e85f8-af30-4f1f-bab1-b7f824daa363
title: ParseField function (Util.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ParseField
api_type: 
- DllExport
api_location: 
- Shell32.dll
---

# ParseField function

\[The **ParseField** function is currently expected to be available for use in the next version of the Microsoft Windows operating system. It might be altered or unavailable in subsequent versions.\]

Reads a line from Setup.inf and extracts the specified field from the string.

## Syntax


```C++
bool ParseField(
  _In_ LPCTSTR *szData,
  _In_ int     n,
  _In_ LPTSTR  *szBuf,
  _In_ int     iBufLen
);
```



## Parameters

<dl> <dt>

*szData* \[in\]
</dt> <dd>

Type: **LPCTSTR\***

A pointer to the line from Setup.inf.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **int**

**INT** that indicates which field to extract.

<dt>



 (0)


</dt> <dd>

Indicates the field before an equals sign (=).

</dd> <dt>



 (1)


</dt> <dd>

Indicates the first field.

</dd> </dl> </dd> <dt>

*szBuf* \[in\]
</dt> <dd>

Type: **LPTSTR\***

A pointer to the buffer that receives the extracted field.

</dd> <dt>

*iBufLen* \[in\]
</dt> <dd>

Type: **int**

**INT** that receives the size of the buffer that receives the extracted field.

</dd> </dl>

## Return value

Type: **bool**

Returns **TRUE** if the function is successful and **FALSE** if it fails.

## Remarks

The fields in the string must be separated by commas.

Leading and trailing spaces are removed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Util.h</dt> </dl>                             |
| Library<br/>                  | <dl> <dt>Shell32.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 




