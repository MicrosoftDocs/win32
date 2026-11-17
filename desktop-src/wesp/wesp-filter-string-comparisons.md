---
title: "WESP string, string list, and path comparisons"
description: "Windows endpoint security platform API reference for string, string list, and path comparisons, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_STRING_COMPARISON_TYPE
- ESP_STRING_COMPARISON
- ESP_STRING_VALUE_SOURCE
- ESP_STRING_LIST_COMPARISON_TYPE
- ESP_STRING_LIST_COMPARISON
- ESP_PATH_COMPARISON
---

# String, string list, and path comparisons

This page contains reference entries in the [Filters API family](wesp-api-reference.md#filters). Each entry includes its declaration and requirements.

## String comparison

### ESP_STRING_COMPARISON_TYPE

The enum `ESP_STRING_COMPARISON_TYPE` defines a string comparison type.

#### Syntax

```cpp
typedef enum ESP_STRING_COMPARISON_TYPE
{
    ESP_STRING_COMPARISON_TYPE_NONE = 0,
    ESP_STRING_COMPARISON_TYPE_EQUALS,
    ESP_STRING_COMPARISON_TYPE_NOT_EQUALS,
    ESP_STRING_COMPARISON_TYPE_PATTERN_MATCH,
    ESP_STRING_COMPARISON_TYPE_IS_IN_COLLECTION
} ESP_STRING_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_STRING_COMPARISON_TYPE_EQUALS` | The comparison matches if the LHS string is equal to the RHS string using ordinal sort rules. |
| `ESP_STRING_COMPARISON_TYPE_NOT_EQUALS` | The comparison matches if the LHS string is not equal to the RHS string using ordinal sort rules. |
| `ESP_STRING_COMPARISON_TYPE_PATTERN_MATCH` | The comparison matches if the LHS string matches the pattern specified by the RHS string. |
| `ESP_STRING_COMPARISON_TYPE_IS_IN_COLLECTION` | The comparison matches if the LHS is found in the collection specified in the `ESP_STRING_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_STRING_COMPARISON

The structure `ESP_STRING_COMPARISON` is used to compare a string value.

#### Syntax

```cpp
typedef struct ESP_STRING_COMPARISON
{
    ESP_STRING_COMPARISON_TYPE ComparisonType;

    union
    {
        ESP_STRING_VALUE_SOURCE Value;
        ESP_COLLECTION Collection;
    } u;
} ESP_STRING_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the comparison type. |
| Value | Specifies the value to compare against if the comparison type is not `ESP_STRING_COMPARISON_TYPE_IS_IN_COLLECTION` |
| Collection | Specifies the collection to compare against if the comparison type is `ESP_STRING_COMPARISON_TYPE_IS_IN_COLLECTION`. The collection's type must be `ESP_COLLECTION_TYPE_STRING`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_STRING_COMPARISON_TYPE`](wesp-filter-string-comparisons.md#esp_string_comparison_type)
- [`ESP_STRING_VALUE_SOURCE`](wesp-filter-string-comparisons.md#esp_string_value_source)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_STRING_VALUE_SOURCE

The structure `ESP_STRING_VALUE_SOURCE` specifies the source of a string value.

#### Syntax

```cpp
typedef struct ESP_STRING_VALUE_SOURCE
{
    ESP_VALUE_SOURCE_TYPE SourceType;
    BOOL CaseSensitive;

    union
    {
        ESP_UNICODE_STRING Raw;
        UINT64 BindingKey;
    } u;
} ESP_STRING_VALUE_SOURCE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| SourceType | Specifies the value source type. |
| CaseSensitive | Specifies whether the comparison should be case sensitive. |
| Raw | Specifies a raw value to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_RAW`. |
| BindingKey | Specifies a binding key to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_BINDING_KEY`. The binding key must resolve to a string value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [`ESP_VALUE_SOURCE_TYPE`](wesp-filter-comparison-types.md#esp_value_source_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## String list comparison

### ESP_STRING_LIST_COMPARISON_TYPE

The enum `ESP_STRING_LIST_COMPARISON_TYPE` defines a string list comparison type.

#### Syntax

```cpp
typedef enum ESP_STRING_LIST_COMPARISON_TYPE
{
    ESP_STRING_LIST_COMPARISON_TYPE_NONE = 0,
    ESP_STRING_LIST_COMPARISON_TYPE_CONTAINS,
    ESP_STRING_LIST_COMPARISON_TYPE_DOES_NOT_CONTAIN
} ESP_STRING_LIST_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_STRING_LIST_COMPARISON_TYPE_CONTAINS` | The comparison matches if the string list contains an entry that matches the string comparison specified in the `ESP_STRING_LIST_COMPARISON` structure. |
| `ESP_STRING_LIST_COMPARISON_TYPE_DOES_NOT_CONTAIN` | The comparison matches if the string list doesn't contain an entry that matches the string comparison specified in the `ESP_STRING_LIST_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_STRING_LIST_COMPARISON

The structure `ESP_STRING_LIST_COMPARISON` is used to compare against a list of strings.

#### Syntax

```cpp
typedef struct ESP_STRING_LIST_COMPARISON
{
    ESP_STRING_LIST_COMPARISON_TYPE ComparisonType;
    ESP_STRING_COMPARISON String;
} ESP_STRING_LIST_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the string list comparison type. The following types are supported:<br>Contains: The comparison matches if the supplied string comparison matches an entry in the list.<br>Does Not Contain: The opposite of contains. |
| String | Specifies the string comparison. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_STRING_LIST_COMPARISON_TYPE`](wesp-filter-string-comparisons.md#esp_string_list_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Path comparison

### ESP_PATH_COMPARISON

The structure `ESP_PATH_COMPARISON` is used to compare a path value.

#### Syntax

```cpp
typedef struct ESP_PATH_COMPARISON
{
    ESP_PATH_FORMAT Format;
    ESP_STRING_COMPARISON Comparison;
} ESP_PATH_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Format | Specifies the path format. This is either DOS or NT. |
| Comparison | Specifies a string comparison for comparing against the path. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PATH_FORMAT`](wesp-common-utilities.md#esp_path_format)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
