---
title: "WESP shared comparison types and context key comparison"
description: "Windows endpoint security platform API reference for shared comparison types and context key comparison, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_COMPARISON_TYPE
- ESP_VALUE_SOURCE_TYPE
- ESP_NUMERICAL_TRANSFORM_TYPE
- ESP_NUMERICAL_TRANSFORM
- ESP_NUMERICAL_TRANSFORM_LIST
- ESP_CONTEXT_KEY_COMPARISON_TYPE
- ESP_CONTEXT_KEY_COMPARISON
---

# Shared comparison types and context key comparison

This page contains reference entries in the [Filters API family](wesp-api-reference.md#filters). Each entry includes its declaration and requirements.

## Shared comparison types

### ESP_COMPARISON_TYPE

Identifies the comparison structure supplied when creating a WESP filter.

#### Syntax

```cpp
typedef enum ESP_COMPARISON_TYPE
{
    ESP_COMPARISON_TYPE_NONE = 0,
    ESP_COMPARISON_TYPE_CONTEXT_KEY, // ESP_CONTEXT_KEY_COMPARISON
    ESP_COMPARISON_TYPE_BOOL, // ESP_BOOL_COMPARISON
    ESP_COMPARISON_TYPE_INTEGER, // ESP_INTEGER_COMPARISON
    ESP_COMPARISON_TYPE_STRING, // ESP_STRING_COMPARISON
    ESP_COMPARISON_TYPE_STRING_LIST, // ESP_STRING_LIST_COMPARISON
    ESP_COMPARISON_TYPE_BINARY, // ESP_BINARY_COMPARISON
    ESP_COMPARISON_TYPE_EA_LIST, // ESP_EA_LIST_COMPARISON
    ESP_COMPARISON_TYPE_ECP_LIST, // ESP_ECP_LIST_COMPARISON
    ESP_COMPARISON_TYPE_BYTE_RANGE, // ESP_BYTE_RANGE_COMPARISON
    ESP_COMPARISON_TYPE_REG_DATA, // ESP_REG_DATA_COMPARISON
    ESP_COMPARISON_TYPE_SID, // ESP_SID_COMPARISON
    ESP_COMPARISON_TYPE_TOKEN_GROUPS, // ESP_TOKEN_GROUPS_COMPARISON
    ESP_COMPARISON_TYPE_TOKEN_PRIVILEGES, // ESP_TOKEN_PRIVILEGES_COMPARISON
    ESP_COMPARISON_TYPE_PATH, // ESP_PATH_COMPARISON
    ESP_COMPARISON_TYPE_NETWORK_IP_ADDRESS, // ESP_NETWORK_IP_ADDRESS_COMPARISON
    ESP_COMPARISON_TYPE_NETWORK_PORT, // ESP_NETWORK_PORT_COMPARISON
    ESP_COMPARISON_TYPE_MEMORY_ADDRESS_BASIC, // ESP_MEMORY_ADDRESS_BASIC_COMPARISON
    ESP_COMPARISON_TYPE_SECURITY_DESCRIPTOR // ESP_SECURITY_DESCRIPTOR_COMPARISON
} ESP_COMPARISON_TYPE;
```

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_BYTE_RANGE_COMPARISON`](wesp-filter-domain-comparisons.md#esp_byte_range_comparison)
- [`ESP_CONTEXT_KEY_COMPARISON`](wesp-filter-comparison-types.md#esp_context_key_comparison)
- [`ESP_EA_LIST_COMPARISON`](wesp-filter-domain-comparisons.md#esp_ea_list_comparison)
- [`ESP_ECP_LIST_COMPARISON`](wesp-filter-domain-comparisons.md#esp_ecp_list_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_MEMORY_ADDRESS_BASIC_COMPARISON`](wesp-filter-domain-comparisons.md#esp_memory_address_basic_comparison)
- [`ESP_NETWORK_IP_ADDRESS_COMPARISON`](wesp-filter-domain-comparisons.md#esp_network_ip_address_comparison)
- [`ESP_NETWORK_PORT_COMPARISON`](wesp-filter-domain-comparisons.md#esp_network_port_comparison)
- [`ESP_PATH_COMPARISON`](wesp-filter-string-comparisons.md#esp_path_comparison)
- [`ESP_REG_DATA_COMPARISON`](wesp-filter-domain-comparisons.md#esp_reg_data_comparison)
- [`ESP_SECURITY_DESCRIPTOR_COMPARISON`](wesp-filter-security-comparisons.md#esp_security_descriptor_comparison)
- [`ESP_SID_COMPARISON`](wesp-filter-security-comparisons.md#esp_sid_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_STRING_LIST_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_list_comparison)
- [`ESP_TOKEN_GROUPS_COMPARISON`](wesp-filter-security-comparisons.md#esp_token_groups_comparison)
- [`ESP_TOKEN_PRIVILEGES_COMPARISON`](wesp-filter-security-comparisons.md#esp_token_privileges_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_VALUE_SOURCE_TYPE

The enum `ESP_VALUE_SOURCE_TYPE` specifies the source type of a value.

#### Syntax

```cpp
typedef enum ESP_VALUE_SOURCE_TYPE
{
    ESP_VALUE_SOURCE_TYPE_NONE = 0,
    ESP_VALUE_SOURCE_TYPE_RAW,
    ESP_VALUE_SOURCE_TYPE_BINDING_KEY
} ESP_VALUE_SOURCE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_VALUE_SOURCE_TYPE_RAW` | The value is a raw value. |
| `ESP_VALUE_SOURCE_TYPE_BINDING_KEY` | The value is a binding key. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NUMERICAL_TRANSFORM_TYPE

The enum `ESP_NUMERICAL_TRANSFORM_TYPE` defines a numerical transform type.

#### Syntax

```cpp
typedef enum ESP_NUMERICAL_TRANSFORM_TYPE
{
    ESP_NUMERICAL_TRANSFORM_TYPE_NONE = 0,
    ESP_NUMERICAL_TRANSFORM_TYPE_ADD,
    ESP_NUMERICAL_TRANSFORM_TYPE_SUBTRACT,
    ESP_NUMERICAL_TRANSFORM_TYPE_MULTIPLY,
    ESP_NUMERICAL_TRANSFORM_TYPE_DIVIDE,
    ESP_NUMERICAL_TRANSFORM_TYPE_MODULO,
    ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_AND,
    ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_OR,
    ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_XOR,
    ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_NOT
} ESP_NUMERICAL_TRANSFORM_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_NUMERICAL_TRANSFORM_TYPE_ADD` | Transforms a value as "Value + TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_SUBTRACT` | Transforms a value as "Value - TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_MULTIPLY` | Transforms a value as "Value * TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_DIVIDE` | Transforms a value as "Value / TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_MODULO` | Transforms a value as "Value % TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_AND` | Transforms a value as "Value & TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_OR` | Transforms a value as "Value \| TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_XOR` | Transforms a value as "Value ^ TransformValue". |
| `ESP_NUMERICAL_TRANSFORM_TYPE_BITWISE_NOT` | Transforms a value as "~Value". |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NUMERICAL_TRANSFORM

The structure `ESP_NUMERICAL_TRANSFORM` is used to represent a numerical transformation. This is used when comparing integer values to transform the value being compared against.

#### Syntax

```cpp
typedef struct ESP_NUMERICAL_TRANSFORM
{
    ESP_NUMERICAL_TRANSFORM_TYPE Type;
    UINT64 Value;
} ESP_NUMERICAL_TRANSFORM;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Type | Specifies the numerical transform type. The supported types are:<br>Add: the value is transformed as "Value + TransformValue".<br>Subtract: the value is transformed as "Value - TransformValue".<br>Multiply: the value is transformed as "Value * TransformValue".<br>Divide: the value is transformed as "Value / TransformValue".<br>Modulo: the value is transformed as "Value % TransformValue".<br>Bitwise And: the value is transformed as "Value & TransformValue".<br>Bitwise Or: the value is transformed as "Value \| TransformValue".<br>Bitwise Xor: the value is transformed as "Value ^ TransformValue".<br>Bitwise Not: the value is transformed as "~Value".<br>If there is an arithmetic overflow, the value wraps around. |
| Value | Specifies the transform value. This field is ignored for bitwise not. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_NUMERICAL_TRANSFORM_TYPE`](wesp-filter-comparison-types.md#esp_numerical_transform_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NUMERICAL_TRANSFORM_LIST

The structure `ESP_NUMERICAL_TRANSFORM_LIST` is used to represent a numerical transform list. This is used when comparing integer values to transform the value being compared against.

#### Syntax

```cpp
typedef struct ESP_NUMERICAL_TRANSFORM_LIST
{
    UINT32 TransformsCount;
    _Field_size_(TransformsCount) const ESP_NUMERICAL_TRANSFORM* Transforms;
} ESP_NUMERICAL_TRANSFORM_LIST;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TransformsCount | Specifies the number of elements in the transforms array. |
| Transforms | Specifies an array of `ESP_NUMERICAL_TRANSFORM` structures. Each transform is applied in the array order on the value being compared against. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_NUMERICAL_TRANSFORM`](wesp-filter-comparison-types.md#esp_numerical_transform)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Context key comparison

### ESP_CONTEXT_KEY_COMPARISON_TYPE

The enum `ESP_CONTEXT_KEY_COMPARISON_TYPE` defines a context key comparison type.

#### Syntax

```cpp
typedef enum ESP_CONTEXT_KEY_COMPARISON_TYPE
{
    ESP_CONTEXT_KEY_COMPARISON_TYPE_NONE,
    ESP_CONTEXT_KEY_COMPARISON_TYPE_KEY_EXISTS,
    ESP_CONTEXT_KEY_COMPARISON_TYPE_KEY_NOT_FOUND,
    ESP_CONTEXT_KEY_COMPARISON_TYPE_INTEGER,
    ESP_CONTEXT_KEY_COMPARISON_TYPE_STRING,
    ESP_CONTEXT_KEY_COMPARISON_TYPE_BINARY,
} ESP_CONTEXT_KEY_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_CONTEXT_KEY_COMPARISON_TYPE_KEY_EXISTS` | The comparison matches if the context key exists. |
| `ESP_CONTEXT_KEY_COMPARISON_TYPE_KEY_NOT_FOUND` | The comparison matches if the context key does not exist. |
| `ESP_CONTEXT_KEY_COMPARISON_TYPE_INTEGER` | The comparison matches if the context key's value is an integer and it matches the integer comparison. |
| `ESP_CONTEXT_KEY_COMPARISON_TYPE_STRING` | The comparison matches if the context key's value is a string and it matches the string comparison. |
| `ESP_CONTEXT_KEY_COMPARISON_TYPE_BINARY` | The comparison matches if the context key's value is a binary value and it matches the binary comparison. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_CONTEXT_KEY_COMPARISON

The structure `ESP_CONTEXT_KEY_COMPARISON` is used to compare a context key.

#### Syntax

```cpp
typedef struct ESP_CONTEXT_KEY_COMPARISON
{
    ESP_CONTEXT_KEY_COMPARISON_TYPE ComparisonType;

    union
    {
        ESP_INTEGER_COMPARISON Integer;
        ESP_STRING_COMPARISON String;
        ESP_BINARY_COMPARISON Binary;
    } Comparison;
} ESP_CONTEXT_KEY_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the comparison type for the context key. |
| Comparison.Integer | Specifies an integer comparison structure if the comparison type is integer. |
| Comparison.String | Specifies a string comparison structure if the comparison type is string. |
| Comparison.Binary | Specifies a binary comparison structure if the comparison type is binary. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_CONTEXT_KEY_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_context_key_comparison_type)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
