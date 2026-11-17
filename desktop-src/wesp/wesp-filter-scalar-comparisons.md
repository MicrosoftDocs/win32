---
title: "WESP boolean, integer, and binary comparisons"
description: "Windows endpoint security platform API reference for boolean, integer, and binary comparisons, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_BOOL_COMPARISON_TYPE
- ESP_BOOL_COMPARISON
- ESP_INTEGER_COMPARISON_TYPE
- ESP_INTEGER_COMPARISON
- ESP_INTEGER_VALUE_SOURCE
- ESP_BINARY_COMPARISON_TYPE
- ESP_BINARY_COMPARISON
- ESP_BINARY_VALUE_SOURCE
---

# Boolean, integer, and binary comparisons

This page contains reference entries in the [Filters API family](wesp-api-reference.md#filters). Each entry includes its declaration and requirements.

## Boolean comparison

### ESP_BOOL_COMPARISON_TYPE

The enum `ESP_BOOL_COMPARISON_TYPE` defines a bool comparison type.

#### Syntax

```cpp
typedef enum ESP_BOOL_COMPARISON_TYPE
{
    ESP_BOOL_COMPARISON_TYPE_NONE = 0,
    ESP_BOOL_COMPARISON_TYPE_EQUALS,
    ESP_BOOL_COMPARISON_TYPE_NOT_EQUALS
} ESP_BOOL_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_BOOL_COMPARISON_TYPE_EQUALS` | The comparison matches if the LHS of the comparison is equal to the Value specified in the `ESP_BOOL_COMPARISON` structure. |
| `ESP_BOOL_COMPARISON_TYPE_NOT_EQUALS` | The comparison matches if the LHS of the comparison is not equal to the Value specified in the `ESP_BOOL_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BOOL_COMPARISON

The structure `ESP_STRING_COMPARISON` is used to compare a boolean value.

#### Syntax

```cpp
typedef struct ESP_BOOL_COMPARISON
{
    ESP_BOOL_COMPARISON_TYPE ComparisonType;
    ESP_VALUE_SOURCE_TYPE SourceType;

    union
    {
        BOOL Raw;
        UINT64 BindingKey;
    } u;
} ESP_BOOL_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the comparison type. |
| SourceType | Specifies the value source type. |
| u.Raw | Specifies a raw value to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_RAW`. |
| u.BindingKey | Specifies a binding key to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_BINDING_KEY`. The binding key must resolve to an integer value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_COMPARISON_TYPE`](wesp-filter-scalar-comparisons.md#esp_bool_comparison_type)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [`ESP_VALUE_SOURCE_TYPE`](wesp-filter-comparison-types.md#esp_value_source_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Integer comparison

### ESP_INTEGER_COMPARISON_TYPE

The enum `ESP_INTEGER_COMPARISON_TYPE` defines an integer comparison type.

#### Syntax

```cpp
typedef enum ESP_INTEGER_COMPARISON_TYPE
{
    ESP_INTEGER_COMPARISON_TYPE_NONE = 0,
    ESP_INTEGER_COMPARISON_TYPE_EQUALS,
    ESP_INTEGER_COMPARISON_TYPE_NOT_EQUALS,
    ESP_INTEGER_COMPARISON_TYPE_LESS_THAN,
    ESP_INTEGER_COMPARISON_TYPE_LESS_THAN_OR_EQUALS,
    ESP_INTEGER_COMPARISON_TYPE_GREATER_THAN,
    ESP_INTEGER_COMPARISON_TYPE_GREATER_THAN_OR_EQUALS,
    ESP_INTEGER_COMPARISON_TYPE_ARE_ALL_FLAGS_SET,
    ESP_INTEGER_COMPARISON_TYPE_ARE_ALL_FLAGS_CLEAR,
    ESP_INTEGER_COMPARISON_TYPE_IS_ANY_FLAG_SET,
    ESP_INTEGER_COMPARISON_TYPE_IS_ANY_FLAG_CLEAR,
    ESP_INTEGER_COMPARISON_TYPE_IS_IN_COLLECTION
} ESP_INTEGER_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_INTEGER_COMPARISON_TYPE_EQUALS` | The comparison matches if:<br>LHS == RHS |
| `ESP_INTEGER_COMPARISON_TYPE_NOT_EQUALS` | The comparison matches if:<br>LHS != RHS |
| `ESP_INTEGER_COMPARISON_TYPE_LESS_THAN` | The comparison matches if:<br>LHS < RHS |
| `ESP_INTEGER_COMPARISON_TYPE_LESS_THAN_OR_EQUALS` | The comparison matches if:<br>LHS <= RHS |
| `ESP_INTEGER_COMPARISON_TYPE_GREATER_THAN` | The comparison matches if:<br>LHS > RHS |
| `ESP_INTEGER_COMPARISON_TYPE_GREATER_THAN_OR_EQUALS` | The comparison matches if:<br>LHS >= RHS |
| `ESP_INTEGER_COMPARISON_TYPE_ARE_ALL_FLAGS_SET` | The comparison matches if all bits set in the RHS are also set in the LHS. |
| `ESP_INTEGER_COMPARISON_TYPE_ARE_ALL_FLAGS_CLEAR` | The comparison matches if all clear bits in the RHS are also clear in the LHS. |
| `ESP_INTEGER_COMPARISON_TYPE_IS_ANY_FLAG_SET` | The comparison matches if any bit set in the RHS is also set in the LHS. |
| `ESP_INTEGER_COMPARISON_TYPE_IS_ANY_FLAG_CLEAR` | The comparison matches if any bit clear in the RHS is also clear in the LHS. |
| `ESP_INTEGER_COMPARISON_TYPE_IS_IN_COLLECTION` | The comparison matches if the LHS is found in the collection specified in the integer comparison structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_INTEGER_COMPARISON

The structure `ESP_INTEGER_COMPARISON` is used to compare an integer value.

#### Syntax

```cpp
typedef struct ESP_INTEGER_COMPARISON
{
    ESP_INTEGER_COMPARISON_TYPE ComparisonType;
    ESP_NUMERICAL_TRANSFORM_LIST LhsTransformList;

    union
    {
        ESP_INTEGER_VALUE_SOURCE Value;
        ESP_COLLECTION Collection;
    } u;
} ESP_INTEGER_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the comparison type. |
| LhsTransformList | Specifies a list of numerical transforms applied to the left-hand side of the comparison. |
| Value | Specifies the value to compare against if the comparison type is not `ESP_INTEGER_COMPARISON_TYPE_IS_IN_COLLECTION` |
| Collection | Specifies the collection to compare against if the comparison type is `ESP_INTEGER_COMPARISON_TYPE_IS_IN_COLLECTION`. The collection's type must be `ESP_COLLECTION_TYPE_INTEGER`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_INTEGER_COMPARISON_TYPE`](wesp-filter-scalar-comparisons.md#esp_integer_comparison_type)
- [`ESP_INTEGER_VALUE_SOURCE`](wesp-filter-scalar-comparisons.md#esp_integer_value_source)
- [`ESP_NUMERICAL_TRANSFORM_LIST`](wesp-filter-comparison-types.md#esp_numerical_transform_list)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_INTEGER_VALUE_SOURCE

The structure `ESP_INTEGER_VALUE_SOURCE` specifies the source of an integer value.

#### Syntax

```cpp
typedef struct ESP_INTEGER_VALUE_SOURCE
{
    ESP_VALUE_SOURCE_TYPE SourceType;
    ESP_NUMERICAL_TRANSFORM_LIST TransformList;

    union
    {
        UINT64 Raw;
        UINT64 BindingKey;
    } u;
} ESP_INTEGER_VALUE_SOURCE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| SourceType | Specifies the value source type. |
| TransformList | Specifies a list of numerical transforms applied to the value. |
| Raw | Specifies a raw value to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_RAW`. |
| BindingKey | Specifies a binding key to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_BINDING_KEY`. The binding key must resolve to an integer value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_NUMERICAL_TRANSFORM_LIST`](wesp-filter-comparison-types.md#esp_numerical_transform_list)
- [`ESP_VALUE_SOURCE_TYPE`](wesp-filter-comparison-types.md#esp_value_source_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Binary comparison

### ESP_BINARY_COMPARISON_TYPE

The enum `ESP_BINARY_COMPARISON_TYPE` defines a binary comparison type.

#### Syntax

```cpp
typedef enum ESP_BINARY_COMPARISON_TYPE
{
    ESP_BINARY_COMPARISON_TYPE_NONE = 0,
    ESP_BINARY_COMPARISON_TYPE_EQUALS,
    ESP_BINARY_COMPARISON_TYPE_NOT_EQUALS,
    ESP_BINARY_COMPARISON_TYPE_IS_IN_COLLECTION
} ESP_BINARY_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_BINARY_COMPARISON_TYPE_EQUALS` | The comparison matches if the LHS binary blob is equal to the RHS binary blob. |
| `ESP_BINARY_COMPARISON_TYPE_NOT_EQUALS` | The comparison matches if the LHS binary blob is not equal to the RHS binary blob. |
| `ESP_BINARY_COMPARISON_TYPE_IS_IN_COLLECTION` | The comparison matches if the LHS is found in the collection specified in the `ESP_BINARY_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BINARY_COMPARISON

The structure `ESP_BINARY_COMPARISON` is used to compare a binary value.

#### Syntax

```cpp
typedef struct ESP_BINARY_COMPARISON
{
    ESP_BINARY_COMPARISON_TYPE ComparisonType;
    UINT32 LhsOffset;
    UINT32 LhsLength;

    union
    {
        ESP_BINARY_VALUE_SOURCE Value;
        ESP_COLLECTION Collection;
    } u;
} ESP_BINARY_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | The comparison type. |
| LhsOffset | Specifies the offset within the LHS binary value at which the comparison should start. |
| LhsLength | Specifies the length of LHS binary value to compare starting at the specified offset. This field can be set to 0 to indicate to compare until the end of the binary value. If the length exceeds the binary value's length, the comparison evaluates to "equals false". |
| Value | Specifies the value to compare against if the comparison type is not `ESP_BINARY_COMPARISON_TYPE_IS_IN_COLLECTION` |
| Collection | Specifies the collection to compare against if the comparison type is `ESP_BINARY_COMPARISON_TYPE_IS_IN_COLLECTION`. The collection's type must be `ESP_COLLECTION_TYPE_BINARY`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON_TYPE`](wesp-filter-scalar-comparisons.md#esp_binary_comparison_type)
- [`ESP_BINARY_VALUE_SOURCE`](wesp-filter-scalar-comparisons.md#esp_binary_value_source)
- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BINARY_VALUE_SOURCE

The structure `ESP_BINARY_VALUE_SOURCE` specifies the source of a binary value.

#### Syntax

```cpp
typedef struct ESP_BINARY_VALUE_SOURCE
{
    ESP_VALUE_SOURCE_TYPE SourceType;
    UINT32 Offset;
    UINT32 Length;

    union
    {
        ESP_BUFFER Raw;
        UINT64 BindingKey;
    } u;
} ESP_BINARY_VALUE_SOURCE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| SourceType | Specifies the value source type. |
| Offset | Specifies the offset within the binary value at which the comparison should start. |
| Length | Specifies the length of binary value to compare starting at the specified offset. This field can be set to 0 to indicate to compare until the end of the binary value. If the length exceeds the binary value's length, the comparison evaluates to "equals false". |
| Raw | Specifies a raw value to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_RAW`. |
| BindingKey | Specifies a binding key to compare against when the source type is `ESP_VALUE_SOURCE_TYPE_BINDING_KEY`. The binding key must resolve to a binary value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer)
- [`ESP_VALUE_SOURCE_TYPE`](wesp-filter-comparison-types.md#esp_value_source_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
