---
description: Node in the dynamic function table linked list
title: DYNAMIC_FUNCTION_TABLE structure
ms.topic: reference
ms.date: 09/17/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DYNAMIC_FUNCTION_TABLE
api_type: 
- HeaderDef
api_location: 
- None
---

# DYNAMIC_FUNCTION_TABLE structure

The **DYNAMIC_FUNCTION_TABLE** structure is an entry in a linked list which is used by a debugger to discover all of the dynamic function tables in a target process. The root node in this linked list is returned from [**RtlGetFunctionTableListHead**](rtlgetfunctiontablelisthead.md)

## Syntax

```C++
typedef struct _DYNAMIC_FUNCTION_TABLE {
    LIST_ENTRY ListEntry;
    PRUNTIME_FUNCTION FunctionTable;
    LARGE_INTEGER Reserved1;
    ULONG64 MinimumAddress;
    ULONG64 MaximumAddress;
    ULONG64 BaseAddress;
    PVOID Reserved2[2];
    PWSTR OutOfProcessCallbackDll;
    FUNCTION_TABLE_TYPE Type;
    ULONG EntryCount;
} DYNAMIC_FUNCTION_TABLE, * PDYNAMIC_FUNCTION_TABLE;
```

## Members

<dt>

**ListEntry**

</dt> 

<dd>

[**LIST_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-list_entry) structure used to point at next and previous entries in the list.

</dd>

<dt>

**FunctionTable**

</dt> 

<dd>

For function tables which are not `RF_CALLBACK`, this points at an array of [**RUNTIME_FUNCTION**](/windows/win32/api/winnt/ns-winnt-runtime_function) structures.

</dd>

<dt>

**Reserved1**

</dt> 

<dd>

Reserved.

</dd>

<dt>

**MinimumAddress**

</dt> 

<dd>

Smallest instruction address described by this table.

</dd>

<dt>

**MaximumAddress**

</dt> 

<dd>

Largest instruction address described by this table.

</dd>

<dt>

**BaseAddress**

</dt> 

<dd>

The base address to use when computing full virtual addresses from relative virtual addresses of function table entries.

</dd>

<dt>

**Reserved2**

</dt> 

<dd>

Reserved.

</dd>

<dt>

**OutOfProcessCallbackDll**

</dt> 

<dd>

For function tables which are `RF_CALLBACK`, this contains an optional pointer to a string that specifies the path of a DLL that provides function table entries from outside of the target process.

When a debugger unwinds to a function in the range of addresses managed by the callback function, it loads this DLL and calls the **OUT_OF_PROCESS_FUNCTION_TABLE_CALLBACK_EXPORT_NAME**
function, whose type is [**POUT_OF_PROCESS_FUNCTION_TABLE_CALLBACK**](pout_of_process_function_table_callback.md).

</dd>

<dt>

**Type**

</dt> 

<dd>

A member of the [FUNCTION_TABLE_TYPE](function_table_type_enum.md) enumeration.

</dd>

<dt>

**EntryCount**

</dt> 

<dd>

The number of entries in the `FunctionTable` array.

</dd>

## Remarks

This struct has no associated import library or header file. The structure may be changed or removed from Windows without further notice.
