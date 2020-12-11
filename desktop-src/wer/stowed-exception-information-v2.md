---
title: STOWED_EXCEPTION_INFORMATION_V2 structure
description: Contains stowed exception info.
ms.assetid: 79267974-EE1B-4427-A6D6-265F6BC5D73A
keywords:
- STOWED_EXCEPTION_INFORMATION_V2 structure Windows Error Reporting
- PSTOWED_EXCEPTION_INFORMATION_V2 structure pointer Windows Error Reporting
topic_type:
- apiref
api_name:
- STOWED_EXCEPTION_INFORMATION_V2
api_location:
- none
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# STOWED\_EXCEPTION\_INFORMATION\_V2 structure

Contains stowed exception info.

## Syntax


```C++
typedef struct _STOWED_EXCEPTION_INFORMATION_V2 {
  STOWED_EXCEPTION_INFORMATION_HEADER Header;
  HRESULT                             ResultCode;
  struct {
    DWORD ExceptionForm  :2;
    DWORD ThreadId  :30;
  };
  union {
    struct {
      PVOID ExceptionAddress;
      ULONG StackTraceWordSize;
      ULONG StackTraceWords;
      PVOID StackTrace;
    };
    struct {
      PWSTR ErrorText;
    };
  };
  ULONG                               NestedExceptionType;
  PVOID                               NestedException;
} STOWED_EXCEPTION_INFORMATION_V2, *PSTOWED_EXCEPTION_INFORMATION_V2;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Type: **[**STOWED\_EXCEPTION\_INFORMATION\_HEADER**](stowed-exception-information-header.md)**

</dd> <dd>

The [**STOWED\_EXCEPTION\_INFORMATION\_HEADER**](stowed-exception-information-header.md) structure that contains info for this parent structure.

</dd> <dt>

**ResultCode**
</dt> <dd>

Type: **[**HRESULT**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

The [**HRESULT**](/windows/desktop/WinProg/windows-data-types) code for the stowed exception.

</dd> <dt>

**ExceptionForm**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A 2-bit value that identifies the form of the exception.



| Value                                                                                                                                                                                                                                                                  | Meaning                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <span id="STOWED_EXCEPTION_FORM_BINARY"></span><span id="stowed_exception_form_binary"></span><dl> <dt>**STOWED\_EXCEPTION\_FORM\_BINARY**</dt> <dt>0x01</dt> </dl> | This value indicates that the form of the exception is binary.<br/> |
| <span id="STOWED_EXCEPTION_FORM_TEXT"></span><span id="stowed_exception_form_text"></span><dl> <dt>**STOWED\_EXCEPTION\_FORM\_TEXT**</dt> <dt>0x02</dt> </dl>       | This value indicates that the form of the exception is text.<br/>   |



 

</dd> <dt>

**ThreadId**
</dt> <dd>

Type: **[**DWORD**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A 30-bit value that identifies the thread that raised the exception. The value is shifted to the right by 2 bits when it's stored. To convert it back to a valid thread ID, shift the value to the left by 2. For example:

``` syntax
DWORD ActualThreadId = (StowedException.ThreadId << 2);
```

</dd> <dt>

(*unnamed struct*)
</dt> <dd>

The members of this nested structure are valid only if the **ExceptionForm** member is set to **STOWED\_EXCEPTION\_FORM\_BINARY**.

<dl> <dt>

**ExceptionAddress**
</dt> <dd>

Type: **[**PVOID**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A pointer that contains the exception address.

</dd> <dt>

**StackTraceWordSize**
</dt> <dd>

Type: **[**ULONG**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

Size, in bytes, of each word in the stack trace that the **StackTrace** member points to. This value is set to 4 for 32-bit platforms and 8 for 64-bit platforms.

</dd> <dt>

**StackTraceWords**
</dt> <dd>

Type: **[**ULONG**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

The number of words in the stack trace that the **StackTrace** member points to. The number of words is equal to the number of elements in the array.

</dd> <dt>

**StackTrace**
</dt> <dd>

Type: **[**PVOID**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A pointer to a memory block that contains the stack trace.

</dd> </dl> </dd> <dt>

(*unnamed struct*)
</dt> <dd>

The member of this nested structure is valid only if the **ExceptionForm** member is set to **STOWED\_EXCEPTION\_FORM\_TEXT**.

<dl> <dt>

**ErrorText**
</dt> <dd>

Type: **[**PWSTR**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A pointer to a null-terminated string that contains the error text of the exception.

</dd> </dl> </dd> <dt>

**NestedExceptionType**
</dt> <dd>

Type: **[**ULONG**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A 32-bit value that specifies the type of object that the **NestedException** member points to. Define the value with this byte swap type-definition macro that assumes little-endian:

``` syntax
#define STOWED_EXCEPTION_NESTED_TYPE(t) ((((((ULONG)(t)) >> 24) & 0xFF) <<  0) | \
                                         (((((ULONG)(t)) >> 16) & 0xFF) <<  8) | \
                                         (((((ULONG)(t)) >>  8) & 0xFF) << 16) | \
                                         (((((ULONG)(t)) >>  0) & 0xFF) << 24))
```

Here are some common type definitions:



| Value                                                                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STOWED_EXCEPTION_NESTED_TYPE_NONE"></span><span id="stowed_exception_nested_type_none"></span><dl> <dt>**STOWED\_EXCEPTION\_NESTED\_TYPE\_NONE**</dt> <dt>(0x00000000)</dt> </dl>                                  | This value specifies that there is no nested exception object.<br/>                                                                                                                                                                                                                                                                                                                                |
| <span id="STOWED_EXCEPTION_NESTED_TYPE_WIN32"></span><span id="stowed_exception_nested_type_win32"></span><dl> <dt>**STOWED\_EXCEPTION\_NESTED\_TYPE\_WIN32**</dt> <dt>STOWED\_EXCEPTION\_NESTED\_TYPE('W32E')</dt> </dl>    | This value specifies that the **NestedException** member points to an [**EXCEPTION\_RECORD**](/windows/desktop/api/winnt/ns-winnt-exception_record) object.<br/>                                                                                                                                                                                                                                                              |
| <span id="STOWED_EXCEPTION_NESTED_TYPE_STOWED"></span><span id="stowed_exception_nested_type_stowed"></span><dl> <dt>**STOWED\_EXCEPTION\_NESTED\_TYPE\_STOWED**</dt> <dt>STOWED\_EXCEPTION\_NESTED\_TYPE('STOW')</dt> </dl> | This value specifies that the **NestedException** member points to another stowed exception object. The other stowed exception object can be a **STOWED\_EXCEPTION\_INFORMATION\_V2** object or a different version with a valid **Header** member, that is, a **Header** member that contains a valid [**STOWED\_EXCEPTION\_INFORMATION\_HEADER**](stowed-exception-information-header.md).<br/> |
| <span id="STOWED_EXCEPTION_NESTED_TYPE_CLR"></span><span id="stowed_exception_nested_type_clr"></span><dl> <dt>**STOWED\_EXCEPTION\_NESTED\_TYPE\_CLR**</dt> <dt>STOWED\_EXCEPTION\_NESTED\_TYPE('CLR1')</dt> </dl>          | This value specifies that the **NestedException** member points to a 'CLR1' exception object.<br/>                                                                                                                                                                                                                                                                                                 |
| <span id="STOWED_EXCEPTION_NESTED_TYPE_LEO"></span><span id="stowed_exception_nested_type_leo"></span><dl> <dt>**STOWED\_EXCEPTION\_NESTED\_TYPE\_LEO**</dt> <dt>STOWED\_EXCEPTION\_NESTED\_TYPE('LEO1')</dt> </dl>          | This value specifies that the **NestedException** member points to a language exception object.<br/>                                                                                                                                                                                                                                                                                               |



 

</dd> <dt>

**NestedException**
</dt> <dd>

Type: **[**PVOID**](/windows/desktop/WinProg/windows-data-types)**

</dd> <dd>

A pointer to a nested exception type. The type of object is indicated by the **NestedExceptionType** member.

</dd> </dl>

## Remarks

**STOWED\_EXCEPTION\_INFORMATION\_V2** and [**STOWED\_EXCEPTION\_INFORMATION\_HEADER**](stowed-exception-information-header.md) currently aren't defined in a header that is publicly available so you need to define them in your source code before you use them.

The **STOWED\_EXCEPTION\_INFORMATION\_V1** structure is identical to this structure except it doesn't contain the **NestedExceptionType** and **NestedException** members.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                         |
| Header<br/>                   | <dl> <dt>None</dt> </dl> |



## See also

<dl> <dt>

[**EXCEPTION\_RECORD**](/windows/desktop/api/winnt/ns-winnt-exception_record)
</dt> <dt>

[**STOWED\_EXCEPTION\_INFORMATION\_HEADER**](stowed-exception-information-header.md)
</dt> </dl>

 

