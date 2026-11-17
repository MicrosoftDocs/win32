---
title: "WESP property query functions and shared types"
description: "Windows endpoint security platform API reference for property query functions and shared types, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspQueryClientProperties
- EspQueryThreadProperties
- EspQueryProcessProperties
- EspQueryFileStreamProperties
- EspQueryFileProperties
- EspQueryFileObjectProperties
- EspQueryVolumeProperties
- EspQueryDiskProperties
- EspQueryRegistryKeyProperties
- EspQueryRegistryKeyObjectProperties
- EspQueryDesktopProperties
- EspQueryKtmTransactionProperties
- EspQueryPipeProperties
- EspQueryMailslotProperties
- EspQueryTokenProperties
- ESP_VARIANT_TYPE
- ESP_VARIANT_VALUE
- ESP_PROPERTY
- ESP_PROPERTY_QUERY
---

# Property query functions and shared types

This page contains reference entries in the [Property queries API family](wesp-api-reference.md#property-queries). Each entry includes its declaration and requirements.

## Property query functions

### EspQueryClientProperties

The API `EspQueryClientProperties` is used to query properties associated with the client.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryClientProperties(
    _In_ ESP_CLIENT Client,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_CLIENT_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Client`

Supplies the client.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_CLIENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_client_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryThreadProperties

The API `EspQueryThreadProperties` is used to query properties for a thread event object. The list of supported thread properties is defined in the enum `ESP_THREAD_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryThreadProperties(
    _In_ ESP_EVENT_OBJECT Thread,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount)  const ESP_THREAD_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Thread`

Supplies the thread.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_THREAD_PROPERTY_ID`](wesp-execution-property-ids.md#esp_thread_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryProcessProperties

The API `EspQueryProcessProperties` is used to query properties for a process event object. The list of supported process properties is defined in the enum `ESP_PROCESS_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryProcessProperties(
    _In_ ESP_EVENT_OBJECT Process,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_PROCESS_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Process`

Supplies the process.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROCESS_PROPERTY_ID`](wesp-execution-property-ids.md#esp_process_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryFileStreamProperties

The API `EspQueryFileStreamProperties` is used to query properties for a file stream event object. The list of supported file stream properties is defined in the enum `ESP_FILE_STREAM_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryFileStreamProperties(
    _In_ ESP_EVENT_OBJECT Stream,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_FILE_STREAM_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Stream`

Supplies the file stream.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_FILE_STREAM_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_stream_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryFileProperties

The API `EspQueryFileProperties` is used to query properties for a file event object. The list of supported file properties is defined in the enum `ESP_FILE_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryFileProperties(
    _In_ ESP_EVENT_OBJECT File,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_FILE_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `File`

Supplies the file.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_FILE_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryFileObjectProperties

The API `EspQueryFileObjectProperties` is used to query properties for a file object event object. The list of supported file object properties is defined in the enum `ESP_FILE_OBJECT_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryFileObjectProperties(
    _In_ ESP_EVENT_OBJECT FileObject,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_FILE_OBJECT_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `FileObject`

Supplies the file object.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_FILE_OBJECT_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_object_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryVolumeProperties

The API `EspQueryVolumeProperties` is used to query properties for a volume event object. The list of supported volume properties is defined in the enum `ESP_VOLUME_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryVolumeProperties(
    _In_ ESP_EVENT_OBJECT Volume,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_VOLUME_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Volume`

Supplies the volume.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_VOLUME_PROPERTY_ID`](wesp-file-property-ids.md#esp_volume_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryDiskProperties

The API `EspQueryDiskProperties` is used to query properties for a disk event object. The list of supported disk properties is defined in the enum `ESP_DISK_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryDiskProperties(
    _In_ ESP_EVENT_OBJECT Disk,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_DISK_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Disk`

Supplies the disk.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_DISK_PROPERTY_ID`](wesp-file-property-ids.md#esp_disk_property_id)
- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryRegistryKeyProperties

The API `EspQueryRegistryKeyProperties` is used to query properties for a registry key event object. The list of supported registry key properties is defined in the enum `ESP_REGISTRY_KEY_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryRegistryKeyProperties(
    _In_ ESP_EVENT_OBJECT RegistryKey,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_REGISTRY_KEY_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `RegistryKey`

Supplies the registry key.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_REGISTRY_KEY_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryRegistryKeyObjectProperties

The API `EspQueryRegistryKeyObjectProperties` is used to query properties for a registry key object event object. The list of supported registry key object properties is defined in the enum `ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryRegistryKeyObjectProperties(
    _In_ ESP_EVENT_OBJECT RegistryKeyObject,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `RegistryKeyObject`

Supplies the registry key object.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_object_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryDesktopProperties

The API `EspQueryDesktopProperties` is used to query properties for a desktop event object. The list of supported desktop properties is defined in the enum `ESP_DESKTOP_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryDesktopProperties(
    _In_ ESP_EVENT_OBJECT Desktop,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_DESKTOP_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Desktop`

Supplies the desktop.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_DESKTOP_PROPERTY_ID`](wesp-other-property-ids.md#esp_desktop_property_id)
- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryKtmTransactionProperties

The API `EspQueryKtmTransactionProperties` is used to query properties for a KTM transaction event object. The list of supported KTM transaction properties is defined in the enum `ESP_KTM_TRANSACTION_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryKtmTransactionProperties(
    _In_ ESP_EVENT_OBJECT KtmTransaction,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_KTM_TRANSACTION_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `KtmTransaction`

Supplies the KTM transaction.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_KTM_TRANSACTION_PROPERTY_ID`](wesp-other-property-ids.md#esp_ktm_transaction_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryPipeProperties

The API `EspQueryPipeProperties` is used to query properties for a pipe event object. The list of supported pipe properties is defined in the enum `ESP_PIPE_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryPipeProperties(
    _In_ ESP_EVENT_OBJECT Pipe,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_PIPE_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Pipe`

Supplies the pipe.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PIPE_PROPERTY_ID`](wesp-other-property-ids.md#esp_pipe_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryMailslotProperties

The API `EspQueryMailslotProperties` is used to query properties for a mailslot event object. The list of supported mailslot properties is defined in the enum `ESP_MAILSLOT_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryMailslotProperties(
    _In_ ESP_EVENT_OBJECT Mailslot,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_MAILSLOT_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Mailslot`

Supplies the mailslot.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_MAILSLOT_PROPERTY_ID`](wesp-other-property-ids.md#esp_mailslot_property_id)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspQueryTokenProperties

The API `EspQueryTokenProperties` is used to query properties for a token event object. The list of supported token properties is defined in the enum `ESP_TOKEN_PROPERTY_ID`.

#### Syntax

```cpp
HRESULT
WINAPI
EspQueryTokenProperties(
    _In_ ESP_EVENT_OBJECT Token,
    _In_ UINT32 PropertyIdsCount,
    _In_reads_(PropertyIdsCount) const ESP_TOKEN_PROPERTY_ID* PropertyIds,
    _Outptr_result_buffer_all_(PropertyIdsCount) ESP_PROPERTY** Properties
    );
```

#### Parameters

##### `Token`

Supplies the token.

##### `PropertyIdsCount`

Supplies the number of elements in the property IDs array.

##### `PropertyIds`

Supplies an array of property IDs to query.

##### `Properties`

Receives the queried properties. This buffer must be freed by calling `EspFreeMemory`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_TOKEN_PROPERTY_ID`](wesp-execution-property-ids.md#esp_token_property_id)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Shared property types

### ESP_VARIANT_TYPE

The enum `ESP_VARIANT_TYPE` identifies which memory of the `ESP_VARIANT_VALUE` union is active. When a property is queried, the returned `ESP_VARIANT_TYPE` indicates the data type of the result, allowing the caller to access the correct union member. The property's variant type also determines which binding key value type (integer, string, binary) the property resolves to. Details can be found in the table below.

#### Syntax

```cpp
typedef enum ESP_VARIANT_TYPE
{
    ESP_VARIANT_TYPE_ERROR,
    ESP_VARIANT_TYPE_CONTEXT_KEY_INFO,
    ESP_VARIANT_TYPE_BOOL,
    ESP_VARIANT_TYPE_UINT8,
    ESP_VARIANT_TYPE_UINT16,
    ESP_VARIANT_TYPE_UINT32,
    ESP_VARIANT_TYPE_UINT64,
    ESP_VARIANT_TYPE_INT32,
    ESP_VARIANT_TYPE_UNICODE_STRING,
    ESP_VARIANT_TYPE_NTSTATUS,
    ESP_VARIANT_TYPE_FILETIME,
    ESP_VARIANT_TYPE_MEMORY_ADDRESS_BASIC,
    ESP_VARIANT_TYPE_FILE_ID_128,
    ESP_VARIANT_TYPE_USN,
    ESP_VARIANT_TYPE_SIGNING_LEVEL,
    ESP_VARIANT_TYPE_EA_LIST,
    ESP_VARIANT_TYPE_SECURITY_DESCRIPTOR,
    ESP_VARIANT_TYPE_BUFFER,
    ESP_VARIANT_TYPE_STRING_LIST,
    ESP_VARIANT_TYPE_GUID,
    ESP_VARIANT_TYPE_ACL,
    ESP_VARIANT_TYPE_SID,
    ESP_VARIANT_TYPE_IMPERSONATION_LEVEL,
    ESP_VARIANT_TYPE_TOKEN_PRIVILEGES,
    ESP_VARIANT_TYPE_TOKEN_GROUPS,
    ESP_VARIANT_TYPE_TOKEN_TYPE,
    ESP_VARIANT_TYPE_TOKEN_ELEVATION_TYPE,
    ESP_VARIANT_TYPE_TRANSACTION_OUTCOME,
    ESP_VARIANT_TYPE_TRANSACTION_STATE,
    ESP_VARIANT_TYPE_STORAGE_BUS_TYPE,
    ESP_VARIANT_TYPE_DEVICE_TYPE,
    ESP_VARIANT_TYPE_SUBSYSTEM_INFORMATION_TYPE,
    ESP_VARIANT_TYPE_FO_TARGET_OBJECT_TYPE
} ESP_VARIANT_TYPE;
```

#### Values

| VALUE | BINDING KEY TYPE |
| --- | --- |
| `ESP_VARIANT_TYPE_ERROR` | N/A |
| `ESP_VARIANT_TYPE_CONTEXT_KEY_INFO` | Resolves to the context key value.<br>Integer, if the context key value type is UINT64<br>String, if the context key value type is string.<br>Binary, if the context key value type is binary. |
| `ESP_VARIANT_TYPE_BOOL` | Integer |
| `ESP_VARIANT_TYPE_UINT8` | Integer |
| `ESP_VARIANT_TYPE_UINT16` | Integer |
| `ESP_VARIANT_TYPE_UINT32` | Integer |
| `ESP_VARIANT_TYPE_UINT64` | Integer |
| `ESP_VARIANT_TYPE_INT32` | Integer |
| `ESP_VARIANT_TYPE_UNICODE_STRING` | String |
| `ESP_VARIANT_TYPE_NTSTATUS` | Integer |
| `ESP_VARIANT_TYPE_FILETIME` | Integer |
| `ESP_VARIANT_TYPE_MEMORY_ADDRESS_BASIC` | Binary |
| `ESP_VARIANT_TYPE_FILE_ID_128` | Binary |
| `ESP_VARIANT_TYPE_USN` | Integer |
| `ESP_VARIANT_TYPE_SIGNING_LEVEL` | Integer |
| `ESP_VARIANT_TYPE_EA_LIST` | [Not Supported] |
| `ESP_VARIANT_TYPE_SECURITY_DESCRIPTOR` | Binary |
| `ESP_VARIANT_TYPE_BUFFER` | Binary |
| `ESP_VARIANT_TYPE_STRING_LIST` | [Not Supported] |
| `ESP_VARIANT_TYPE_GUID` | Binary |
| `ESP_VARIANT_TYPE_ACL` | Binary |
| `ESP_VARIANT_TYPE_SID` | Binary |
| `ESP_VARIANT_TYPE_IMPERSONATION_LEVEL` | Integer |
| `ESP_VARIANT_TYPE_TOKEN_PRIVILEGES` | [Not Supported] |
| `ESP_VARIANT_TYPE_TOKEN_GROUPS` | [Not Supported] |
| `ESP_VARIANT_TYPE_TOKEN_TYPE` | Integer |
| `ESP_VARIANT_TYPE_TOKEN_ELEVATION_TYPE` | Integer |
| `ESP_VARIANT_TYPE_TRANSACTION_OUTCOME` | Integer |
| `ESP_VARIANT_TYPE_TRANSACTION_STATE` | Integer |
| `ESP_VARIANT_TYPE_STORAGE_BUS_TYPE` | Integer |
| `ESP_VARIANT_TYPE_DEVICE_TYPE` | Integer |
| `ESP_VARIANT_TYPE_SUBSYSTEM_INFORMATION_TYPE` | Integer |
| `ESP_VARIANT_TYPE_FO_TARGET_OBJECT_TYPE` | Integer |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_VARIANT_VALUE`](wesp-property-queries.md#esp_variant_value)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VARIANT_VALUE

`ESP_VARIANT_VALUE` contains a property value. `ESP_PROPERTY`.Type identifies the active union member. Some members store values directly; others point to value structures.

#### Syntax

```cpp
typedef union ESP_VARIANT_VALUE
{
    HRESULT Error;
    ESP_CONTEXT_KEY_INFO* ContextKeyInfo;
    BOOL Bool;
    UINT8 Uint8;
    UINT16 Uint16;
    UINT32 Uint32;
    UINT64 Uint64;
    INT32 Int32;
    ESP_UNICODE_STRING* UnicodeString;
    NTSTATUS NtStatus;
    FILETIME FileTime;
    ESP_MEMORY_ADDRESS_BASIC* MemoryAddressBasic;
    FILE_ID_128* FileId128;
    USN Usn;
    SE_SIGNING_LEVEL SigningLevel;
    ESP_EA_LIST* EaList;
    SECURITY_DESCRIPTOR* SecurityDescriptor;
    ESP_BUFFER* Buffer;
    ESP_STRING_LIST* StringList;
    GUID* Guid;
    ACL* Acl;
    SID* Sid;
    SECURITY_IMPERSONATION_LEVEL ImpersonationLevel;
    TOKEN_PRIVILEGES* TokenPrivileges;
    TOKEN_GROUPS* TokenGroups;
    TOKEN_TYPE TokenType;
    TOKEN_ELEVATION_TYPE TokenElevationType;
    TRANSACTION_OUTCOME TransactionOutcome;
    TRANSACTION_STATE TransactionState;
    STORAGE_BUS_TYPE StorageBusType;
    DEVICE_TYPE DeviceType;
    ESP_SUBSYSTEM_INFORMATION_TYPE SubsystemInformationType;
    ESP_FO_TARGET_OBJECT_TYPE FoTargetObjectType;
} ESP_VARIANT_VALUE;
```

#### Members

| Member | Description |
| --- | --- |
| Error | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_ERROR`. |
| ContextKeyInfo | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_CONTEXT_KEY_INFO`. |
| Bool | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_BOOL`. |
| Uint8 | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_UINT8`. |
| Uint16 | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_UINT16`. |
| Uint32 | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_UINT32`. |
| Uint64 | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_UINT64`. |
| Int32 | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_INT32`. |
| UnicodeString | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_UNICODE_STRING`. |
| NtStatus | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_NTSTATUS`. |
| FileTime | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_FILETIME`. |
| MemoryAddressBasic | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_MEMORY_ADDRESS_BASIC`. |
| FileId128 | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_FILE_ID_128`. |
| Usn | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_USN`. |
| SigningLevel | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_SIGNING_LEVEL`. |
| EaList | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_EA_LIST`. |
| SecurityDescriptor | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_SECURITY_DESCRIPTOR`. |
| Buffer | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_BUFFER`. |
| StringList | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_STRING_LIST`. |
| Guid | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_GUID`. |
| Acl | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_ACL`. |
| Sid | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_SID`. |
| ImpersonationLevel | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_IMPERSONATION_LEVEL`. |
| TokenPrivileges | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_TOKEN_PRIVILEGES`. |
| TokenGroups | Pointer to the value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_TOKEN_GROUPS`. |
| TokenType | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_TOKEN_TYPE`. |
| TokenElevationType | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_TOKEN_ELEVATION_TYPE`. |
| TransactionOutcome | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_TRANSACTION_OUTCOME`. |
| TransactionState | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_TRANSACTION_STATE`. |
| StorageBusType | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_STORAGE_BUS_TYPE`. |
| DeviceType | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_DEVICE_TYPE`. |
| SubsystemInformationType | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_SUBSYSTEM_INFORMATION_TYPE`. |
| FoTargetObjectType | The value when `ESP_PROPERTY`.Type is `ESP_VARIANT_TYPE_FO_TARGET_OBJECT_TYPE`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_CONTEXT_KEY_INFO`](wesp-context-key-management.md#esp_context_key_info)
- [`ESP_EA_LIST`](wesp-common-value-types.md#esp_ea_list)
- [`ESP_FO_TARGET_OBJECT_TYPE`](wesp-common-value-types.md#esp_fo_target_object_type)
- [`ESP_MEMORY_ADDRESS_BASIC`](wesp-common-value-types.md#esp_memory_address_basic)
- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [`ESP_STRING_LIST`](wesp-common-utilities.md#esp_string_list)
- [`ESP_SUBSYSTEM_INFORMATION_TYPE`](wesp-common-value-types.md#esp_subsystem_information_type)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROPERTY

The structure `ESP_PROPERTY` stores the result of a property query.

#### Syntax

```cpp
typedef struct ESP_PROPERTY
{
    UINT32 PropertyId;
    ESP_VARIANT_TYPE Type;
    ESP_VARIANT_VALUE Value;
} ESP_PROPERTY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| PropertyId | Specifies the property ID. |
| Type | The variant type for the property's value. |
| Value | The property's value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_VARIANT_TYPE`](wesp-property-queries.md#esp_variant_type)
- [`ESP_VARIANT_VALUE`](wesp-property-queries.md#esp_variant_value)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROPERTY_QUERY

The structure `ESP_PROPERTY_QUERY` stores an array of queried properties.

#### Syntax

```cpp
typedef struct ESP_PROPERTY_QUERY
{
    UINT32 PropertiesCount;
    _Field_size_(PropertiesCount) const ESP_PROPERTY* Properties;
} ESP_PROPERTY_QUERY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| PropertiesCount | Specifies the number of elements in the properties array. |
| Properties | The array of queried properties. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PROPERTY`](wesp-property-queries.md#esp_property)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
