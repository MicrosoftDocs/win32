---
title: "WESP event, client, thread, process, and token property IDs"
description: "Windows endpoint security platform API reference for event, client, thread, process, and token property IDs, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_EVENT_PROPERTY_ID
- ESP_CLIENT_PROPERTY_ID
- ESP_THREAD_PROPERTY_ID
- ESP_PROCESS_PROPERTY_ID
- ESP_TOKEN_PROPERTY_ID
---

# Event, client, thread, process, and token property IDs

This page contains reference entries in the [Property queries API family](wesp-api-reference.md#property-queries). Each entry includes its declaration and requirements.

## Event properties

### ESP_EVENT_PROPERTY_ID

Event properties are defined in the enum `ESP_EVENT_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_EVENT_PROPERTY_ID
{
    ESP_EVENT_PROPERTY_ID_NONE = 0,
    ESP_EVENT_PROPERTY_ID_PREVIOUS_MODE_IS_KERNEL_MODE, // ESP_BOOL_COMPARISON - BOOL
    ESP_EVENT_PROPERTY_ID_NTSTATUS, // ESP_INTEGER_COMPARISON - NTSTATUS
    ESP_EVENT_PROPERTY_ID_EVENT_TIME // ESP_INTEGER_COMPARISON - FILETIME
} ESP_EVENT_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_EVENT_PROPERTY_ID_PREVIOUS_MODE_IS_KERNEL_MODE` | Whether the previous mode is kernel mode when the event occurs. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_EVENT_PROPERTY_ID_NTSTATUS` | The NTSTATUS of the event. This property can only be filtered if the rule action is "NotifyOnCompletion". | `ESP_VARIANT_TYPE_NTSTATUS` |
| `ESP_EVENT_PROPERTY_ID_EVENT_TIME` | The event time. Note that the event time is stamped when the event occurs, not when the event notification is sent. So, if one client receives a synchronous notification for an event and another client receives an asynchronous notification for the same event, the event time will be the same. | `ESP_VARIANT_TYPE_FILETIME` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Client properties

### ESP_CLIENT_PROPERTY_ID

Client properties are defined in the enum `ESP_CLIENT_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_CLIENT_PROPERTY_ID
{
    ESP_CLIENT_PROPERTY_ID_NONE = 0,
    ESP_CLIENT_PROPERTY_ID_IS_CONNECTED // ESP_BOOL_COMPARISON - BOOL
} ESP_CLIENT_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_CLIENT_PROPERTY_ID_IS_CONNECTED` | True if the client is currently connected, false otherwise. | `ESP_VARIANT_TYPE_BOOL` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Thread properties

### ESP_THREAD_PROPERTY_ID

Thread properties are defined in the enum `ESP_THREAD_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_THREAD_PROPERTY_ID
{
    ESP_THREAD_PROPERTY_ID_NONE = 0,
    ESP_THREAD_PROPERTY_ID_TID, // ESP_INTEGER_COMPARISON - UINT32
    ESP_THREAD_PROPERTY_ID_CREATE_TIME, // ESP_INTEGER_COMPARISON - FILETIME
    ESP_THREAD_PROPERTY_ID_IS_SYSTEM_THREAD, // ESP_BOOL_COMPARISON - BOOL
    ESP_THREAD_PROPERTY_ID_IS_ATTACHED_TO_HOST_SILO, // ESP_BOOL_COMPARISON - BOOL
    ESP_THREAD_PROPERTY_ID_BASE_PRIORITY, // ESP_INTEGER_COMPARISON - INT32
    ESP_THREAD_PROPERTY_ID_START_ADDRESS_BASIC, // ESP_MEMORY_ADDRESS_BASIC_COMPARISON - ESP_MEMORY_ADDRESS_BASIC_QUERY
    ESP_THREAD_PROPERTY_ID_START_ADDRESS_MAPPED_FILE_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_THREAD_PROPERTY_ID_START_ADDRESS_MAPPED_FILE_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_THREAD_PROPERTY_ID_WIN32_START_ADDRESS_BASIC, // ESP_MEMORY_ADDRESS_BASIC_COMPARISON - ESP_MEMORY_ADDRESS_BASIC_QUERY
    ESP_THREAD_PROPERTY_ID_WIN32_START_ADDRESS_MAPPED_FILE_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_THREAD_PROPERTY_ID_WIN32_START_ADDRESS_MAPPED_FILE_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
} ESP_THREAD_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_THREAD_PROPERTY_ID_TID` | The thread's id. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_THREAD_PROPERTY_ID_CREATE_TIME` | The thread's create time. | `ESP_VARIANT_TYPE_FILETIME` |
| `ESP_THREAD_PROPERTY_ID_IS_SYSTEM_THREAD` | Whether the thread is a system thread. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_THREAD_PROPERTY_ID_IS_ATTACHED_TO_HOST_SILO` | Whether thread is attached to the host silo. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_THREAD_PROPERTY_ID_BASE_PRIORITY` | The thread's base priority. | `ESP_VARIANT_TYPE_INT32` |
| `ESP_THREAD_PROPERTY_ID_START_ADDRESS_BASIC` | The thread's start address basic information. | `ESP_VARIANT_TYPE_MEMORY_ADDRESS_BASIC` |
| `ESP_THREAD_PROPERTY_ID_START_ADDRESS_MAPPED_FILE_NT_PATH` | The thread's start address mapped file NT path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_THREAD_PROPERTY_ID_START_ADDRESS_MAPPED_FILE_DOS_PATH` | The thread's start address mapped file DOS path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_THREAD_PROPERTY_ID_WIN32_START_ADDRESS_BASIC` | The thread's WIN32 start address basic information. | `ESP_VARIANT_TYPE_MEMORY_ADDRESS_BASIC` |
| `ESP_THREAD_PROPERTY_ID_WIN32_START_ADDRESS_MAPPED_FILE_NT_PATH` | The thread's WIN32 start address mapped file NT path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_THREAD_PROPERTY_ID_WIN32_START_ADDRESS_MAPPED_FILE_DOS_PATH` | The thread's WIN32 start address mapped file DOS path. | `ESP_VARIANT_TYPE_UNICODE_STRING` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_MEMORY_ADDRESS_BASIC_COMPARISON`](wesp-filter-domain-comparisons.md#esp_memory_address_basic_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Process properties

### ESP_PROCESS_PROPERTY_ID

Process properties are defined in the enum `ESP_PROCESS_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_PROCESS_PROPERTY_ID
{
    ESP_PROCESS_PROPERTY_ID_NONE = 0,
    ESP_PROCESS_PROPERTY_ID_COMMAND_LINE, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_PROCESS_PROPERTY_ID_CREATE_TIME, // ESP_INTEGER_COMPARISON - FILETIME
    ESP_PROCESS_PROPERTY_ID_IS_SYSTEM_PROCESS, // ESP_BOOL_COMPARISON - BOOL
    ESP_PROCESS_PROPERTY_ID_IS_CRITICAL, // ESP_BOOL_COMPARISON - BOOL
    ESP_PROCESS_PROPERTY_ID_IS_DEBUGGED, // ESP_BOOL_COMPARISON - BOOL
    ESP_PROCESS_PROPERTY_ID_PID, // ESP_INTEGER_COMPARISON - UINT32
    ESP_PROCESS_PROPERTY_ID_PROTECTION_LEVEL, // ESP_INTEGER_COMPARISON - UINT8 (PS_PROTECTION.Level)
    ESP_PROCESS_PROPERTY_ID_PROTECTION_TYPE, // ESP_INTEGER_COMPARISON - UINT8 (PS_PROTECTION.Type)
    ESP_PROCESS_PROPERTY_ID_PROTECTION_SIGNER, // ESP_INTEGER_COMPARISON - UINT8 (PS_PROTECTION.Signer)
    ESP_PROCESS_PROPERTY_ID_ARCHITECTURE, // ESP_INTEGER_COMPARISON - UINT16 (IMAGE_FILE_MACHINE_*)
    ESP_PROCESS_PROPERTY_ID_IS_WOW64, // ESP_BOOL_COMPARISON - BOOL
    ESP_PROCESS_PROPERTY_ID_SUBSYSTEM_TYPE, // ESP_INTEGER_COMPARISON - ESP_SUBSYSTEM_INFORMATION_TYPE
    ESP_PROCESS_PROPERTY_ID_SESSION_ID, // ESP_INTEGER_COMPARISON - UINT32
    ESP_PROCESS_PROPERTY_ID_SIGNATURE_LEVEL, // ESP_INTEGER_COMPARISON - SE_SIGNING_LEVEL (PsGetProcessSignatureLevel)
    ESP_PROCESS_PROPERTY_ID_SECTION_SIGNATURE_LEVEL, // ESP_INTEGER_COMPARISON - SE_SIGNING_LEVEL (PsGetProcessSignatureLevel)
    ESP_PROCESS_PROPERTY_ID_EXTENDED_INFO_FLAGS, // ESP_INTEGER_COMPARISON - UINT32 (PROCESS_EXTENDED_BASIC_INFORMATION.Flags)
    ESP_PROCESS_PROPERTY_ID_START_KEY, // ESP_INTEGER_COMPARISON - UINT64 (PsGetProcessStartKey)
    ESP_PROCESS_PROPERTY_ID_PACKAGE_FAMILY_NAME, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_PROCESS_PROPERTY_ID_EXIT_STATUS, // ESP_INTEGER_COMPARISON - NTSTATUS
    ESP_PROCESS_PROPERTY_ID_IMAGE_FILE_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_PROCESS_PROPERTY_ID_IMAGE_FILE_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_PROCESS_PROPERTY_ID_IS_WESP_CLIENT, // ESP_BOOL_COMPARISON - BOOL
    ESP_PROCESS_PROPERTY_ID_IS_WESP_CLIENT_SELF, // ESP_BOOL_COMPARISON - BOOL
} ESP_PROCESS_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_PROCESS_PROPERTY_ID_COMMAND_LINE` | The process command line. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_PROCESS_PROPERTY_ID_CREATE_TIME` | The process create time. | `ESP_VARIANT_TYPE_FILETIME` |
| `ESP_PROCESS_PROPERTY_ID_IS_SYSTEM_PROCESS` | Whether the process is a system process. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_PROCESS_PROPERTY_ID_IS_CRITICAL` | Whether the process is critical (e.g. smss.exe). | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_PROCESS_PROPERTY_ID_IS_DEBUGGED` | Whether the process is currently getting debugged. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_PROCESS_PROPERTY_ID_PID` | The process id. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_PROCESS_PROPERTY_ID_PROTECTION_LEVEL` | The process protection level. This is the equivalent of "PS_PROTECTION.Level". | `ESP_VARIANT_TYPE_UINT8` |
| `ESP_PROCESS_PROPERTY_ID_PROTECTION_TYPE` | The process protection type. This is the equivalent of "PS_PROTECTION.Type". | `ESP_VARIANT_TYPE_UINT8` |
| `ESP_PROCESS_PROPERTY_ID_PROTECTION_SIGNER` | The process protection signer. This is the equivalent of "PS_PROTECTION.Signer". | `ESP_VARIANT_TYPE_UINT8` |
| `ESP_PROCESS_PROPERTY_ID_ARCHITECTURE` | The process architecture. This is an "IMAGE_FILE_MACHINE*" constant. | `ESP_VARIANT_TYPE_UINT16` |
| `ESP_PROCESS_PROPERTY_ID_IS_WOW64` | Whether the process is a WOW64 process. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_PROCESS_PROPERTY_ID_SUBSYSTEM_TYPE` | The process subsystem type. | `ESP_VARIANT_TYPE_SUBSYSTEM_INFORMATION_TYPE` |
| `ESP_PROCESS_PROPERTY_ID_SESSION_ID` | The process session id. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_PROCESS_PROPERTY_ID_SIGNATURE_LEVEL` | The process signature level. | `ESP_VARIANT_TYPE_SIGNING_LEVEL` |
| `ESP_PROCESS_PROPERTY_ID_SECTION_SIGNATURE_LEVEL` | The process section signature level. | `ESP_VARIANT_TYPE_SIGNING_LEVEL` |
| `ESP_PROCESS_PROPERTY_ID_EXTENDED_INFO_FLAGS` | Extended information flags for the process. This is the equivalent of "PROCESS_EXTENDED_BASIC_INFORMATION.Flags". | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_PROCESS_PROPERTY_ID_START_KEY` | The process start key returned by PsGetProcessStartKey. | `ESP_VARIANT_TYPE_UINT64` |
| `ESP_PROCESS_PROPERTY_ID_PACKAGE_FAMILY_NAME` | The package family name. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_PROCESS_PROPERTY_ID_EXIT_STATUS` | The process exit status. | `ESP_VARIANT_TYPE_NTSTATUS` |
| `ESP_PROCESS_PROPERTY_ID_IMAGE_FILE_NT_PATH` | The NT path to the process executable file. | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_PROCESS_PROPERTY_ID_IMAGE_FILE_DOS_PATH` | The DOS path to the process executable file. | `ESP_VARIANT_TYPE_UNICODE_STRING` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_SUBSYSTEM_INFORMATION_TYPE`](wesp-common-value-types.md#esp_subsystem_information_type)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Token properties

### ESP_TOKEN_PROPERTY_ID

Token properties are defined in the enum `ESP_TOKEN_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_TOKEN_PROPERTY_ID
{
    ESP_TOKEN_PROPERTY_ID_NONE = 0,
    ESP_TOKEN_PROPERTY_ID_DEFAULT_DACL, // [no filter support] - ACL
    ESP_TOKEN_PROPERTY_ID_IS_IMPERSONATING, // ESP_BOOL_COMPARISON - BOOL
    ESP_TOKEN_PROPERTY_ID_IMPERSONATION_LEVEL, // ESP_INTEGER_COMPARISON - SECURITY_IMPERSONATION_LEVEL
    ESP_TOKEN_PROPERTY_ID_GROUPS, // ESP_TOKEN_GROUPS_COMPARISON - TOKEN_GROUPS
    ESP_TOKEN_PROPERTY_ID_OWNER, // ESP_SID_COMPARISON - SID
    ESP_TOKEN_PROPERTY_ID_PRIMARY_GROUP, // ESP_SID_COMPARISON - SID
    ESP_TOKEN_PROPERTY_ID_PRIVILEGES, // ESP_TOKEN_PRIVILEGES_COMPARISON - TOKEN_PRIVILEGES
    ESP_TOKEN_PROPERTY_ID_SESSION_ID, // ESP_INTEGER_COMPARISON - UINT32
    ESP_TOKEN_PROPERTY_ID_TOKEN_TYPE, // ESP_INTEGER_COMPARISON - TOKEN_TYPE
    ESP_TOKEN_PROPERTY_ID_USER_SID, // ESP_SID_COMPARISON - SID
    ESP_TOKEN_PROPERTY_ID_INTEGRITY_LEVEL, // ESP_INTEGER_COMPARISON - UINT32
    ESP_TOKEN_PROPERTY_ID_ELEVATION_TYPE, // ESP_INTEGER_COMPARISON - TOKEN_ELEVATION_TYPE
} ESP_TOKEN_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_TOKEN_PROPERTY_ID_DEFAULT_DACL` | The token's default DACL. | `ESP_VARIANT_TYPE_ACL` |
| `ESP_TOKEN_PROPERTY_ID_IS_IMPERSONATING` | Whether the token is impersonating. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_TOKEN_PROPERTY_ID_IMPERSONATION_LEVEL` | The token's impersonation level. If the token is not impersonating, this property can't be filtered or retrieved. | `ESP_VARIANT_TYPE_IMPERSONATION_LEVEL` |
| `ESP_TOKEN_PROPERTY_ID_GROUPS` | The token's groups. | `ESP_VARIANT_TYPE_TOKEN_GROUPS` |
| `ESP_TOKEN_PROPERTY_ID_OWNER` | The token's owner. | `ESP_VARIANT_TYPE_SID` |
| `ESP_TOKEN_PROPERTY_ID_PRIMARY_GROUP` | The token's primary group. | `ESP_VARIANT_TYPE_SID` |
| `ESP_TOKEN_PROPERTY_ID_PRIVILEGES` | The token's privileges. | `ESP_VARIANT_TYPE_TOKEN_PRIVILEGES` |
| `ESP_TOKEN_PROPERTY_ID_SESSION_ID` | The token's session id. | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_TOKEN_PROPERTY_ID_TOKEN_TYPE` | The token's type. | `ESP_VARIANT_TYPE_TOKEN_TYPE` |
| `ESP_TOKEN_PROPERTY_ID_USER_SID` | The token's user sid. | `ESP_VARIANT_TYPE_SID` |
| `ESP_TOKEN_PROPERTY_ID_INTEGRITY_LEVEL` | The token's integrity level (e.g. SECURITY_MANDATORY_HIGH_RID). | `ESP_VARIANT_TYPE_UINT32` |
| `ESP_TOKEN_PROPERTY_ID_ELEVATION_TYPE` | The token's elevation type (i.e. TOKEN_ELEVATION_TYPE). | `ESP_VARIANT_TYPE_TOKEN_ELEVATION_TYPE` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_SID_COMPARISON`](wesp-filter-security-comparisons.md#esp_sid_comparison)
- [`ESP_TOKEN_GROUPS_COMPARISON`](wesp-filter-security-comparisons.md#esp_token_groups_comparison)
- [`ESP_TOKEN_PRIVILEGES_COMPARISON`](wesp-filter-security-comparisons.md#esp_token_privileges_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
