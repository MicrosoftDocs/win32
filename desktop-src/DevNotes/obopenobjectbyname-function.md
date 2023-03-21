---
description: Opens an object with full access validation and auditing.
title: ObOpenObjectByName function
ms.topic: reference
ms.date: 03/02/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ObOpenObjectByName
api_type: 
- DllExport
api_location: 
- ntoskrnl.exe
---

# ObOpenObjectByName function

Opens an object with full access validation and auditing.

## Syntax


```C++
NTSTATUS
ObOpenObjectByName (
    __in POBJECT_ATTRIBUTES ObjectAttributes,
    __in POBJECT_TYPE ObjectType,
    __in KPROCESSOR_MODE AccessMode,
    __inout_opt PACCESS_STATE AccessState,
    __in_opt ACCESS_MASK DesiredAccess,
    __inout_opt PVOID ParseContext,
    __out PHANDLE Handle
    )
```



## Parameters

### ObjectAttributes [in]

A pointer to an [OBJECT_ATTRIBUTES](/windows/win32/api/ntdef/ns-ntdef-_object_attributes) structure representing the object attributes.

### ObjectType [in]

The object type. The **OBJECT_TYPE** structure has the following definition:

```cpp
typedef struct _OBJECT_TYPE {
    LIST_ENTRY TypeList;
    UNICODE_STRING Name;            
    PVOID DefaultObject;
    UCHAR Index;
    __volatile ULONG TotalNumberOfObjects;
    __volatile ULONG TotalNumberOfHandles;
    ULONG HighWaterNumberOfObjects;
    ULONG HighWaterNumberOfHandles;
    OBJECT_TYPE_INITIALIZER TypeInfo;
    EX_PUSH_LOCK TypeLock;
    ULONG Key;
} OBJECT_TYPE, *POBJECT_TYPE;
```

### AccessMode [in]

The processor mode of the access. The **KPROCESSOR_MODE** is defined with the following values:

```cpp
typedef enum _KPROCESSOR_MODE {
    KernelMode,
    UserMode,
    MaximumMode
} KPROCESSOR_MODE;
```

### AccessState [in, out, optional]

An optional pointer to the an [ACCESS_STATE](/windows-hardware/drivers/ddi/wdm/ns-wdm-_access_state) representing the current access status describing already granted access types, the privileges used to get them, and any access types yet to be granted.

### DesiredAccess [in, optional]

An [ACCESS_MASK](/windows/win32/secauthz/access-mask) representing the desired access to the object.

### ParseContext [in, out, optional]

An optional pointer to parse context data.

### Handle [out]

Receives pointer to a variable that receives the handle value.

## Return value

S_OK on success.

## Remarks

This function is not defined in an SDK header and must be declared by the caller. This function is exported from ntoskrnl.exe.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 |
| Minimum supported server | Windows 10 |
| DLL | ntoskrnl.exe |



## See also



 

 
