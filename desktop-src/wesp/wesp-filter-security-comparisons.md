---
title: "WESP SID, token, and security descriptor comparisons"
description: "Windows endpoint security platform API reference for SID, token, and security descriptor comparisons, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_SID_COMPARISON_TYPE
- ESP_SID_FORMAT
- ESP_SID_COMPARISON
- ESP_TOKEN_GROUPS_COMPARISON_TYPE
- ESP_TOKEN_GROUPS_COMPARISON
- ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE
- ESP_TOKEN_PRIVILEGES_COMPARISON
- ESP_SECURITY_DESCRIPTOR_FORMAT
- ESP_SECURITY_DESCRIPTOR_COMPARISON
---

# SID, token, and security descriptor comparisons

This page contains reference entries in the [Filters API family](wesp-api-reference.md#filters). Each entry includes its declaration and requirements.

## SID comparison

### ESP_SID_COMPARISON_TYPE

The enum `ESP_SID_COMPARISON_TYPE` defines a SID comparison type.

#### Syntax

```cpp
typedef enum ESP_SID_COMPARISON_TYPE
{
    ESP_SID_COMPARISON_TYPE_NONE = 0,
    ESP_SID_COMPARISON_TYPE_EQUALS,
    ESP_SID_COMPARISON_TYPE_NOT_EQUALS
} ESP_SID_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_SID_COMPARISON_TYPE_EQUALS` | The comparison matches if the LHS SID is equal to the RHS SID. |
| `ESP_SID_COMPARISON_TYPE_NOT_EQUALS` | The comparison matches if the LHS SID is not equal to the RHS SID. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_SID_FORMAT

The enum `ESP_SID_FORMAT` defines a SID format.

#### Syntax

```cpp
typedef enum ESP_SID_FORMAT
{
    ESP_SID_FORMAT_NONE = 0,
    ESP_SID_FORMAT_BINDING_KEY,
    ESP_SID_FORMAT_RAW,
    ESP_SID_FORMAT_SDDL
} ESP_SID_FORMAT;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_SID_FORMAT_BINDING_KEY` | The SID is specified as a binding key. |
| `ESP_SID_FORMAT_RAW` | The SID is specified in raw form (i.e. PSID). |
| `ESP_SID_FORMAT_SDDL` | The SID is specified as a string SDDL. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_SID_COMPARISON

The structure `ESP_SID_COMPARISON` is used to compare against a SID value.

#### Syntax

```cpp
typedef struct ESP_SID_COMPARISON
{
    ESP_SID_COMPARISON_TYPE ComparisonType;
    ESP_SID_FORMAT Format;

    union
    {
        UINT64 BindingKey;
        const SID* Raw;
        PCWSTR Sddl;
    } Sid;
} ESP_SID_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the SID comparison type. |
| Format | Specifies SID format. |
| Sid.BindingKey | Specifies a binding key that is resolved as a SID. |
| Sid.Raw | Specifies a PSID if the SID format is raw. |
| Sid.Sddl | Specifies the SID as an SDDL string if the SID format is SDDL. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_SID_COMPARISON_TYPE`](wesp-filter-security-comparisons.md#esp_sid_comparison_type)
- [`ESP_SID_FORMAT`](wesp-filter-security-comparisons.md#esp_sid_format)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Token groups comparison

### ESP_TOKEN_GROUPS_COMPARISON_TYPE

The enum `ESP_TOKEN_GROUPS_COMPARISON_TYPE` defines a token groups comparison type.

#### Syntax

```cpp
typedef enum ESP_TOKEN_GROUPS_COMPARISON_TYPE
{
    ESP_TOKEN_GROUPS_COMPARISON_TYPE_NONE = 0,
    ESP_TOKEN_GROUPS_COMPARISON_TYPE_CONTAINS,
    ESP_TOKEN_GROUPS_COMPARISON_TYPE_DOES_NOT_CONTAIN
} ESP_TOKEN_GROUPS_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_TOKEN_GROUPS_COMPARISON_TYPE_CONTAINS` | The comparison matches if the token groups contain an entry that matches the sid and attributes comparison specified in the `ESP_TOKEN_GROUPS_COMPARISON` structure. |
| `ESP_TOKEN_GROUPS_COMPARISON_TYPE_DOES_NOT_CONTAIN` | The comparison matches if the token groups don't contain an entry that matches the sid and attributes comparison specified in the `ESP_TOKEN_GROUPS_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_TOKEN_GROUPS_COMPARISON

The structure `ESP_TOKEN_GROUPS_COMPARISON` is used to compare against token groups.

#### Syntax

```cpp
typedef struct ESP_TOKEN_GROUPS_COMPARISON
{
    ESP_TOKEN_GROUPS_COMPARISON_TYPE ComparisonType;
    ESP_SID_COMPARISON SidComparison;
    ESP_INTEGER_COMPARISON AttributesComparison;
} ESP_TOKEN_GROUPS_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the token groups comparison type. |
| SidComparison | Specifies a comparison for a group SID. |
| AttributesComparison | Specifies an integer comparison for the group SID attributes. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_SID_COMPARISON`](wesp-filter-security-comparisons.md#esp_sid_comparison)
- [`ESP_TOKEN_GROUPS_COMPARISON_TYPE`](wesp-filter-security-comparisons.md#esp_token_groups_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Token privileges comparison

### ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE

The enum `ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE` defines a token privileges comparison type.

#### Syntax

```cpp
typedef enum ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE
{
    ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE_NONE = 0,
    ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE_CONTAINS,
    ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE_DOES_NOT_CONTAIN
} ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE_CONTAINS` | The comparison matches if the token privileges contain an entry that matches the LUID and attributes comparison specified in the `ESP_TOKEN_PRIVILEGES_COMPARISON` structure. |
| `ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE_DOES_NOT_CONTAIN` | The comparison matches if the token privileges don't contain an entry that matches the LUID and attributes comparison specified in the `ESP_TOKEN_PRIVILEGES_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_TOKEN_PRIVILEGES_COMPARISON

The structure `ESP_TOKEN_PRIVILEGES_COMPARISON` is used to compare against token privileges.

#### Syntax

```cpp
typedef struct ESP_TOKEN_PRIVILEGES_COMPARISON
{
    ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE ComparisonType;
    ESP_BINARY_COMPARISON LuidComparison;
    ESP_INTEGER_COMPARISON AttributesComparison;
} ESP_TOKEN_PRIVILEGES_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the token privileges comparison type. |
| LuidComparison | Specifies a binary comparison for the privilege LUID. |
| AttributesComparison | Specifies an integer comparison for the privilege attributes. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE`](wesp-filter-security-comparisons.md#esp_token_privileges_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Security descriptor comparison

### ESP_SECURITY_DESCRIPTOR_FORMAT

The enum `ESP_SECURITY_DESCRIPTOR_FORMAT` specifies the format of a security descriptor.

#### Syntax

```cpp
typedef enum ESP_SECURITY_DESCRIPTOR_FORMAT
{
    ESP_SECURITY_DESCRIPTOR_FORMAT_NONE = 0,
    ESP_SECURITY_DESCRIPTOR_FORMAT_BINDING_KEY,
    ESP_SECURITY_DESCRIPTOR_FORMAT_RAW,
    ESP_SECURITY_DESCRIPTOR_FORMAT_SDDL
} ESP_SECURITY_DESCRIPTOR_FORMAT;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_SECURITY_DESCRIPTOR_FORMAT_BINDING_KEY` | The security descriptor should be resolved from a binding key. The binding key's data type must be binary. |
| `ESP_SECURITY_DESCRIPTOR_FORMAT_RAW` | The format is a raw security descriptor (i.e. PSECURITY_DESCRIPTOR). |
| `ESP_SECURITY_DESCRIPTOR_FORMAT_SDDL` | The format is an SDDL string. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_SECURITY_DESCRIPTOR_COMPARISON

The structure `ESP_SECURITY_DESCRIPTOR_COMPARISON` performs a security descriptor comparison.

#### Syntax

```cpp
typedef struct ESP_SECURITY_DESCRIPTOR_COMPARISON
{
    ESP_SID_COMPARISON Owner;
    ESP_SID_COMPARISON PrimaryGroup;
    ESP_BINARY_COMPARISON Raw;
} ESP_SECURITY_DESCRIPTOR_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Owner | Specifies a SID comparison for the security descriptor's owner. |
| PrimaryGroup | Specifies a SID comparison for the security descriptor's primary group. |
| Raw | Specifies a binary comparison for the raw security descriptor bytes. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_SID_COMPARISON`](wesp-filter-security-comparisons.md#esp_sid_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
