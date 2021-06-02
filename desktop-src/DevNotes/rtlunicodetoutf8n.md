---
description: Translates the specified Unicode string into a new character string, using the 8-bit Unicode Transformation Format (UTF-8) code page.
ms.assetid: ecd63eee-bf86-42b5-93d8-3c7871aa6324
title: RtlUnicodeToUTF8N function (Wdm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlUnicodeToUTF8N
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# RtlUnicodeToUTF8N function

Translates the specified Unicode string into a new character string, using the 8-bit Unicode Transformation Format (UTF-8) code page.

## Syntax


```C++
NTSTATUS WINAPI RtlUnicodeToUTF8N(
  _Out_     PCHAR  UTF8StringDestination,
  _In_      ULONG  UTF8StringMaxByteCount,
  _Out_opt_ PULONG UTF8StringActualByteCount,
  _In_      PCWSTR UnicodeStringSource,
  _In_      ULONG  UnicodeStringByteCount
);
```



## Parameters

<dl> <dt>

*UTF8StringDestination* \[out\]
</dt> <dd>

A pointer to a caller-allocated buffer to receive the translated string.

</dd> <dt>

*UTF8StringMaxByteCount* \[in\]
</dt> <dd>

Maximum number of bytes to be written to *UTF8StringDestination*. If this value causes the translated string to be truncated, **RtlUnicodeToUTF8N** returns an error status.

</dd> <dt>

*UTF8StringActualByteCount* \[out, optional\]
</dt> <dd>

A pointer to a caller-allocated variable that receives the length, in bytes, of the translated string. This parameter is optional and can be **NULL**. If the string is truncated then the returned number counts the actual truncated string count.

</dd> <dt>

*UnicodeStringSource* \[in\]
</dt> <dd>

A pointer to the Unicode source string to be translated.

</dd> <dt>

*UnicodeStringByteCount * \[in\]
</dt> <dd>

Specifies the number of bytes in the Unicode source string that the *UnicodeStringSource* parameter points to.

</dd> </dl>

## Return value

**RtlUnicodeToUTF8N** returns one of the following NTSTATUS values:



| Return code                                                                                                  | Description                                                                                                     |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_SUCCESS**</dt> </dl>               | The Unicode string was converted to UTF-8.<br/>                                                           |
| <dl> <dt>**STATUS\_SOME\_NOT\_MAPPED**</dt> </dl>     | An invalid input character was encountered and replaced. This status is considered a success status.<br/> |
| <dl> <dt>**STATUS\_INVALID\_PARAMETER**</dt> </dl>    | Both pointers to *UTF8StringDestination* and *UTF8StringActualByteCount* were **NULL**.<br/>              |
| <dl> <dt>**STATUS\_INVALID\_PARAMETER\_4**</dt> </dl> | The *UnicodeStringSource* was **NULL**.<br/>                                                              |
| <dl> <dt>**STATUS\_BUFFER\_TOO\_SMALL**</dt> </dl>    | *UTF8StringDestination* was truncated.<br/>                                                               |



 

## Remarks

Although *UTF8StringActualByteCount* is optional and can be **NULL**, callers should provide storage for it, because the received length can be used to determine whether the conversion was successful. This routine does not modify the source string. It returns a null-terminated UTF-8 string if the given *UnicodeStringSource* included a NULL terminator and if the given *UTF8StringMaxByteCount* did not cause truncation.

If the output is truncated and an invalid input character is encountered then the function returns STATUS\_BUFFER\_TOO\_SMALL error.

If the *UTF8StringDestination* is set to **NULL** the function will return the required number of bytes to host the translated string without any truncation in *UTF8StringActualByteCount*.

Callers of **RtlUnicodeToUTF8N** must be running at IRQL < DISPATCH\_LEVEL.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wdm.h</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**RtlUTF8ToUnicodeN**](rtlutf8tounicoden.md)
</dt> </dl>

 

 




