---
title: "WESP registry and other object property IDs"
description: "Windows endpoint security platform API reference for registry and other object property IDs, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_REGISTRY_KEY_PROPERTY_ID
- ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID
- ESP_DESKTOP_PROPERTY_ID
- ESP_KTM_TRANSACTION_PROPERTY_ID
- ESP_PIPE_PROPERTY_ID
- ESP_MAILSLOT_PROPERTY_ID
---

# Registry and other object property IDs

This page contains reference entries in the [Property queries API family](wesp-api-reference.md#property-queries). Each entry includes its declaration and requirements.

## Registry key properties

### ESP_REGISTRY_KEY_PROPERTY_ID

Registry key properties are defined in the enum `ESP_REGISTRY_KEY_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_REGISTRY_KEY_PROPERTY_ID
{
    ESP_REGISTRY_KEY_PROPERTY_ID_NONE = 0,
    ESP_REGISTRY_KEY_PROPERTY_ID_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_REGISTRY_KEY_PROPERTY_ID_DOS_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_REGISTRY_KEY_PROPERTY_ID_IS_SYMLINK, // ESP_BOOL_COMPARISON - BOOL
    ESP_REGISTRY_KEY_PROPERTY_ID_SECURITY_DESCRIPTOR // ESP_SECURITY_DESCRIPTOR_COMPARISON - SECURITY_DESCRIPTOR
} ESP_REGISTRY_KEY_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_REGISTRY_KEY_PROPERTY_ID_NT_PATH` | The registry key NT path (e.g. "\Registry\Machine\System\ControlSet001"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_REGISTRY_KEY_PROPERTY_ID_DOS_PATH` | The registry key DOS path (e.g. HKLM\System\ControlSet001"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_REGISTRY_KEY_PROPERTY_ID_IS_SYMLINK` | Whether the registry key is a symbolic key, | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_REGISTRY_KEY_PROPERTY_ID_SECURITY_DESCRIPTOR` | The registry key's security descriptor. | `ESP_VARIANT_TYPE_SECURITY_DESCRIPTOR` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_SECURITY_DESCRIPTOR_COMPARISON`](wesp-filter-security-comparisons.md#esp_security_descriptor_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Registry key object properties

### ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID

Registry key object properties are defined in the enum `ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID
{
    ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_NONE = 0,
    ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_IS_TRANSACTED, // ESP_BOOL_COMPARISON - BOOL
    ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_OBJECT_ID // ESP_INTEGER_COMPARISON - UINT64
} ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_IS_TRANSACTED` | Indicates whether the registry key object has an associated KTM transaction. | `ESP_VARIANT_TYPE_BOOL` |
| `ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_OBJECT_ID` | The registry-key-object's ObjectID returned by CmCallbackGetKeyObjectIDEx. | `ESP_VARIANT_TYPE_UINT64` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Desktop properties

### ESP_DESKTOP_PROPERTY_ID

Desktop properties are defined in the enum `ESP_DESKTOP_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_DESKTOP_PROPERTY_ID
{
    ESP_DESKTOP_PROPERTY_ID_NONE = 0,
    ESP_DESKTOP_PROPERTY_ID_NAME // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
} ESP_DESKTOP_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_DESKTOP_PROPERTY_ID_NAME` | The desktop name. | `ESP_VARIANT_TYPE_UNICODE_STRING` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## KTM transaction properties

### ESP_KTM_TRANSACTION_PROPERTY_ID

KTM transaction properties are defined in the enum `ESP_KTM_TRANSACTION_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_KTM_TRANSACTION_PROPERTY_ID
{
    ESP_KTM_TRANSACTION_PROPERTY_ID_NONE = 0,
    ESP_KTM_TRANSACTION_PROPERTY_ID_TRANSACTION_ID, // ESP_BINARY_COMPARISON - GUID
    ESP_KTM_TRANSACTION_PROPERTY_ID_STATE, // ESP_INTEGER_COMPARISON - TRANSACTION_STATE
    ESP_KTM_TRANSACTION_PROPERTY_ID_OUTCOME // ESP_INTEGER_COMPARISON - TRANSACTION_OUTCOME
} ESP_KTM_TRANSACTION_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_KTM_TRANSACTION_PROPERTY_ID_TRANSACTION_ID` | The KTM transaction ID. This is the equivalent of "TRANSACTION_BASIC_INFORMATION.TransactionId". | `ESP_VARIANT_TYPE_GUID` |
| `ESP_KTM_TRANSACTION_PROPERTY_ID_STATE` | The KTM transaction state. This is the equivalent of "TRANSACTION_BASIC_INFORMATION.State". | `ESP_VARIANT_TYPE_TRANSACTION_STATE` |
| `ESP_KTM_TRANSACTION_PROPERTY_ID_OUTCOME` | The KTM transaction outcome. This is the equivalent of "TRANSACTION_BASIC_INFORMATION.Outcome". | `ESP_VARIANT_TYPE_TRANSACTION_OUTCOME` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Pipe properties

### ESP_PIPE_PROPERTY_ID

Pipe properties are defined in the enum `ESP_PIPE_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_PIPE_PROPERTY_ID
{
    ESP_PIPE_PROPERTY_ID_NONE = 0,
    ESP_PIPE_PROPERTY_ID_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_PIPE_PROPERTY_ID_DOS_PATH // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
} ESP_PIPE_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_PIPE_PROPERTY_ID_NT_PATH` | The pipe NT path (e.g. "\Device\NamedPipe\PipeFoo"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_PIPE_PROPERTY_ID_DOS_PATH` | The pipe DOS path (e.g. "\\.\pipe\PipeFoo"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Mailslot properties

### ESP_MAILSLOT_PROPERTY_ID

Mailslot properties are defined in the enum `ESP_MAILSLOT_PROPERTY_ID`. The expected comparison structure for each property ID and its property data is commented next to each enum value below.

#### Syntax

```cpp
typedef enum ESP_MAILSLOT_PROPERTY_ID
{
    ESP_MAILSLOT_PROPERTY_ID_NONE = 0,
    ESP_MAILSLOT_PROPERTY_ID_NT_PATH, // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
    ESP_MAILSLOT_PROPERTY_ID_DOS_PATH // ESP_STRING_COMPARISON - ESP_UNICODE_STRING
} ESP_MAILSLOT_PROPERTY_ID;
```

#### Values

| Property ID | Description | Property Variant Type |
| --- | --- | --- |
| `ESP_MAILSLOT_PROPERTY_ID_NT_PATH` | The pipe NT path (e.g. "\Device\Mailslot\MailslotFoo"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |
| `ESP_MAILSLOT_PROPERTY_ID_DOS_PATH` | The pipe DOS path (e.g. "\\.\mailslot\MailslotFoo"). | `ESP_VARIANT_TYPE_UNICODE_STRING` |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
