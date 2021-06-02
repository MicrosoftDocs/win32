---
description: Translates the specified source string into a Unicode string, using the 8-bit Unicode Transformation Format (UTF-8) code page.
ms.assetid: 2871a81b-74f9-462e-9e5c-c59d06bb6841
title: RtlUTF8ToUnicodeN function (Wdm.h)
ms.topic: reference
ms.date: 02/21/2019
topic_type:
- APIRef
- kbSyntax
api_name:
- RtlUTF8ToUnicodeN
api_type:
- DllExport
api_location:
- Ntdll.dll
---

# RtlUTF8ToUnicodeN function

Translates the specified source string into a Unicode string, using the 8-bit Unicode Transformation Format (UTF-8) code page.

## Syntax


```C++
NTSTATUS WINAPI RtlUTF8ToUnicodeN(
  _Out_     PWSTR  UnicodeStringDestination,
  _In_      ULONG  UnicodeStringMaxByteCount,
  _Out_opt_ PULONG UnicodeStringActualByteCount,
  _In_      PCCH   UTF8StringSource,
  _In_      ULONG  UTF8StringByteCount
);
```



## Parameters

<dl> <dt>

*UnicodeStringDestination* \[out\]
</dt> <dd>

A pointer to a caller-allocated buffer that receives the translated string.

</dd> <dt>

*UnicodeStringMaxByteCount* \[in\]
</dt> <dd>

Maximum number of bytes to be written at *UnicodeStringDestination*. If this value causes the translated string to be truncated, **RtlUTF8ToUnicodeN** returns an error status.

</dd> <dt>

*UnicodeStringActualByteCount* \[out, optional\]
</dt> <dd>

A pointer to a caller-allocated variable that receives the length, in bytes, of the translated string. This parameter is optional and can be **NULL**. If the string is truncated then the returned number counts the actual truncated string count.

</dd> <dt>

*UTF8StringSource* \[in\]
</dt> <dd>

A pointer to the string to be translated.

</dd> <dt>

*UTF8StringByteCount* \[in\]
</dt> <dd>

Size, in bytes, of the string at *UTF8StringSource*.

</dd> </dl>

## Return value

**RtlUTF8ToUnicodeN** returns one of the following NTSTATUS values:



| Return code                                                                                                  | Description                                                                                                     |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STATUS\_SUCCESS**</dt> </dl>               | The string was converted to Unicode.<br/>                                                                 |
| <dl> <dt>**STATUS\_SOME\_NOT\_MAPPED**</dt> </dl>     | An invalid input character was encountered and replaced. This status is considered a success status.<br/> |
| <dl> <dt>**STATUS\_INVALID\_PARAMETER**</dt> </dl>    | Both pointers to *UnicodeStringDestination* and *UnicodeStringActualByteCount* were **NULL**.<br/>       |
| <dl> <dt>**STATUS\_INVALID\_PARAMETER\_4**</dt> </dl> | The *UTF8StringSource* was **NULL**.<br/>                                                                 |
| <dl> <dt>**STATUS\_BUFFER\_TOO\_SMALL**</dt> </dl>    | *UnicodeStringDestination* was truncated.<br/>                                                            |



 

## Remarks

Although *UnicodeStringActualByteCount* is optional and can be **NULL**, callers should provide storage for it, because the received length can be used to determine whether the conversion was successful.

If the output is truncated and an invalid input character is encountered then the function returns STATUS\_BUFFER\_TOO\_SMALL error.

If the *UnicodeStringDestination* is set to **NULL** the function will return the required number of bytes to host the translated string without any truncation in *UnicodeStringActualByteCount*.

**RtlUTF8ToUnicodeN** does not modify the source string unless the *UnicodeStringDestination* and *UTF8StringSource* pointers are equivalent. The returned Unicode string is not null-terminated.

Callers of **RtlUTF8ToUnicodeN** must be running at IRQL < DISPATCH\_LEVEL.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wdm.h</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**RtlUnicodeToUTF8N**](rtlunicodetoutf8n.md)
</dt> </dl>

 

 




