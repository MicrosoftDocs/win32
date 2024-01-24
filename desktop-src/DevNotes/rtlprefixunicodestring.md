---
description: Compares two Unicode strings to determine whether one string is a prefix of the other.
ms.assetid: 7D859C0A-2F72-49A4-8B49-130DCA103F37
title: RtlPrefixUnicodeString function (Ntddk.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlPrefixUnicodeString
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlPrefixUnicodeString function

Compares two Unicode strings to determine whether one string is a prefix of the other.

## Syntax


```C++
BOOLEAN RtlPrefixUnicodeString(
  _In_ PCUNICODE_STRING String1,
  _In_ PCUNICODE_STRING String2,
  _In_ BOOLEAN          CaseInSensitive
);
```



## Parameters

<dl> <dt>

*String1* \[in\]
</dt> <dd>

Pointer to the first string, which might be a prefix of the buffered Unicode string at *String2*.

</dd> <dt>

*String2* \[in\]
</dt> <dd>

Pointer to the second string.

</dd> <dt>

*CaseInSensitive* \[in\]
</dt> <dd>

If **TRUE**, case should be ignored when doing the comparison.

</dd> </dl>

## Return value

**TRUE** if *String1* is a prefix of *String2*.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                    |
| Target platform<br/>          | <dl> <dt>[Universal](https://msdn.microsoft.com/Library/Windows/Hardware/EB2264A4-BAE8-446B-B9A5-19893936DDCA)</dt> </dl> |
| Header<br/>                   | <dl> <dt>Ntddk.h (include Ntddk.h)</dt> </dl>                                    |
| Library<br/>                  | <dl> <dt>Ntdll.lib</dt> </dl>                                                    |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**RtlCompareUnicodeString**](rtlcompareunicodestring.md)
</dt> </dl>

 

 




