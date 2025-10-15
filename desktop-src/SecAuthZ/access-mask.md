---
description: Defines standard, specific, and generic rights. These rights are used in access control entries (ACEs) and are the primary means of specifying the requested or granted access to an object.
ms.assetid: f115ee54-3333-4109-8004-d71904a7a943
title: ACCESS_MASK (Winnt.h)
ms.topic: reference
ms.date: 10/14/2025
---

# ACCESS_MASK

The **ACCESS_MASK** data type is a **DWORD** value that defines standard, specific, and generic rights. These rights are used in [access control entries](/windows/win32/SecGloss/a-gly) (ACEs) and are the primary means of specifying the requested or granted access to an object.

```C++
typedef DWORD ACCESS_MASK;
typedef ACCESS_MASK* PACCESS_MASK;
```

## Remarks

The bits in this value are allocated as follows:

| Bits | Meaning |
|------|---------|
| 0-15 | Specific rights. Contains the access mask specific to the object type associated with the mask. See [Object-Specific Access Rights](#object-specific-access-rights) for links to access rights for different object types. |
| 16-23 | Standard rights. Contains the object's standard access rights. |
| 24 | Access system security (**ACCESS_SYSTEM_SECURITY**). It is used to indicate access to a [*system access control list*](/windows/win32/SecGloss/s-gly) (SACL). This type of access requires the calling process to have the **SE_SECURITY_NAME** (Manage auditing and security log) privilege. If this flag is set in the access mask of an audit access ACE (successful or unsuccessful access), the SACL access will be audited. |
| 25 | Maximum allowed (**MAXIMUM_ALLOWED**). |
| 26-27 | Reserved. |
| 28 | Generic all (**GENERIC_ALL**). |
| 29 | Generic execute (**GENERIC_EXECUTE**). |
| 30 | Generic write (**GENERIC_WRITE**). |
| 31 | Generic read (**GENERIC_READ**). |

Standard rights bits, 16 to 23, contain the object's standard access rights and can be a combination of the following predefined flags:

| Bit | Flag | Meaning |
|-----|------|---------|
| 16 | **DELETE** | Delete access. |
| 17 | **READ_CONTROL** | Read access to the owner, group, and [*discretionary access control list*](/windows/win32/SecGloss/d-gly) (DACL) of the security descriptor. |
| 18 | **WRITE_DAC** | Write access to the DACL. |
| 19 | **WRITE_OWNER** | Write access to owner. |
| 20 | **SYNCHRONIZE** | Synchronize access. |

The following constants defined in Winnt.h represent the specific and standard access rights.

```cpp
#define DELETE                           (0x00010000L)
#define READ_CONTROL                     (0x00020000L)
#define WRITE_DAC                        (0x00040000L)
#define WRITE_OWNER                      (0x00080000L)
#define SYNCHRONIZE                      (0x00100000L)

#define STANDARD_RIGHTS_REQUIRED         (0x000F0000L)

#define STANDARD_RIGHTS_READ             (READ_CONTROL)
#define STANDARD_RIGHTS_WRITE            (READ_CONTROL)
#define STANDARD_RIGHTS_EXECUTE          (READ_CONTROL)

#define STANDARD_RIGHTS_ALL              (0x001F0000L)

#define SPECIFIC_RIGHTS_ALL              (0x0000FFFFL)
```

## Object-Specific Access Rights

The low 16 bits (bits 0-15) of the **ACCESS_MASK** are used for object-specific access rights. The meaning of these bits depends on the type of object being accessed. For detailed information about access rights for specific object types, see the following topics:

### Common Object Types

- **Files and Directories** - [File Access Rights Constants](/windows/win32/FileIO/file-access-rights-constants)  
  Defines specific access rights such as FILE_READ_DATA, FILE_WRITE_DATA, FILE_APPEND_DATA, FILE_EXECUTE, FILE_DELETE_CHILD, FILE_READ_ATTRIBUTES, and FILE_WRITE_ATTRIBUTES.
- **Registry Keys** - [Registry Key Security and Access Rights](/windows/win32/SysInfo/registry-key-security-and-access-rights)
  Defines specific access rights such as KEY_QUERY_VALUE, KEY_SET_VALUE, KEY_CREATE_SUB_KEY, KEY_ENUMERATE_SUB_KEYS, and KEY_NOTIFY.
- **Processes** - [Process Security and Access Rights](/windows/win32/ProcThread/process-security-and-access-rights)  
  Defines specific access rights such as PROCESS_TERMINATE, PROCESS_CREATE_THREAD, PROCESS_VM_OPERATION, PROCESS_VM_READ, PROCESS_VM_WRITE, PROCESS_QUERY_INFORMATION, and PROCESS_SET_INFORMATION.
- **Threads** - [Thread Security and Access Rights](/windows/win32/ProcThread/thread-security-and-access-rights)  
  Defines specific access rights such as THREAD_TERMINATE, THREAD_SUSPEND_RESUME, THREAD_GET_CONTEXT, THREAD_SET_CONTEXT, THREAD_QUERY_INFORMATION, and THREAD_SET_INFORMATION.

### Additional Object Types

- **Window Stations** - [Window Station Security and Access Rights](/windows/win32/winstation/window-station-security-and-access-rights)
- **Desktops** - [Desktop Security and Access Rights](/windows/win32/winstation/desktop-security-and-access-rights)
- **Services** - [Service Security and Access Rights](/windows/win32/Services/service-security-and-access-rights)
- **Files Mapped Objects** - [File Mapping Security and Access Rights](/windows/win32/Memory/file-mapping-security-and-access-rights)
- **Job Objects** - [Job Object Security and Access Rights](/windows/win32/ProcThread/job-object-security-and-access-rights)
- **Named Pipes** - [Named Pipe Security and Access Rights](/windows/win32/ipc/named-pipe-security-and-access-rights)

For a comprehensive list of securable objects and their access rights, see [Access Rights and Access Masks](access-rights-and-access-masks.md).

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows XP \[desktop apps only\] |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header | `Winnt.h` (include `Windows.h`) |

## Related content

[Access Control](access-control.md)

[Basic Access Control Structures](authorization-structures.md)

[Access Rights and Access Masks](access-rights-and-access-masks.md)

[GENERIC_MAPPING](/windows/win32/api/Winnt/ns-winnt-generic_mapping)
