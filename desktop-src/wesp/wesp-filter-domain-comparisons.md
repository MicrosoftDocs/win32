---
title: "WESP file, registry, network, and memory comparisons"
description: "Windows endpoint security platform API reference for file, registry, network, and memory comparisons, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_EA_LIST_COMPARISON_TYPE
- ESP_EA_LIST_COMPARISON
- ESP_ECP_LIST_COMPARISON_TYPE
- ESP_ECP_LIST_COMPARISON
- ESP_BYTE_RANGE_COMPARISON_TYPE
- ESP_BYTE_RANGE_COMPARISON
- ESP_REG_DATA_COMPARISON_TYPE
- ESP_REG_DATA_COMPARISON
- ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE
- ESP_NETWORK_IP_ADDRESS_COMPARISON
- ESP_NETWORK_PORT_COMPARISON_TYPE
- ESP_NETWORK_PORT_COMPARISON
- ESP_MEMORY_ADDRESS_BASIC_COMPARISON
---

# File, registry, network, and memory comparisons

This page contains reference entries in the [Filters API family](wesp-api-reference.md#filters). Each entry includes its declaration and requirements.

## Extended attribute list comparison

### ESP_EA_LIST_COMPARISON_TYPE

The enum `ESP_EA_LIST_COMPARISON_TYPE` defines an EA list comparison type.

#### Syntax

```cpp
typedef enum ESP_EA_LIST_COMPARISON_TYPE
{
    ESP_EA_LIST_COMPARISON_TYPE_NONE = 0,
    ESP_EA_LIST_COMPARISON_TYPE_CONTAINS,
    ESP_EA_LIST_COMPARISON_TYPE_DOES_NOT_CONTAIN
} ESP_EA_LIST_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EA_LIST_COMPARISON_TYPE_CONTAINS` | The comparison matches if the EA list contains an entry that matches the EaName and EaValue comparison specified in the `ESP_EA_LIST_COMPARISON` structure. |
| `ESP_EA_LIST_COMPARISON_TYPE_DOES_NOT_CONTAIN` | The comparison matches if the EA list doesn't contain an entry that matches the EaName and EaValue comparison specified in the `ESP_EA_LIST_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EA_LIST_COMPARISON

The structure `ESP_EA_LIST_COMPARISON` is used to compare an EA list.

#### Syntax

```cpp
typedef struct ESP_EA_LIST_COMPARISON
{
    ESP_EA_LIST_COMPARISON_TYPE ComparisonType;
    ESP_BINARY_COMPARISON EaName;
    ESP_BINARY_COMPARISON EaValue;
} ESP_EA_LIST_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the EA list comparison type. |
| EaName | Specifies an `ESP_BINARY_COMPARISON` struct to perform a comparison against the EA's name. |
| EaValue | Specifies an `ESP_BINARY_COMPARISON` struct to perform a comparison against the EA's value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_EA_LIST_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_ea_list_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## ECP list comparison

### ESP_ECP_LIST_COMPARISON_TYPE

The enum `ESP_ECP_LIST_COMPARISON_TYPE` defines an ECP list comparison type.

#### Syntax

```cpp
typedef enum ESP_ECP_LIST_COMPARISON_TYPE
{
    ESP_ECP_LIST_COMPARISON_TYPE_NONE = 0,
    ESP_ECP_LIST_COMPARISON_TYPE_CONTAINS,
    ESP_ECP_LIST_COMPARISON_TYPE_DOES_NOT_CONTAIN
} ESP_ECP_LIST_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_ECP_LIST_COMPARISON_TYPE_CONTAINS` | The comparison matches if the ECP list contains an entry that matches the Ecp, IsFromUserMode and Contents comparison specified in the `ESP_ECP_LIST_COMPARISON` structure. |
| `ESP_ECP_LIST_COMPARISON_TYPE_DOES_NOT_CONTAIN` | The comparison matches if the ECP list doesn't contain an entry that matches the Ecp, IsFromUserMode and Contents comparison specified in the `ESP_ECP_LIST_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ECP_LIST_COMPARISON

The structure `ESP_ECP_LIST_COMPARISON` is used to compare an ECP list.

#### Syntax

```cpp
typedef struct ESP_ECP_LIST_COMPARISON
{
    ESP_ECP_LIST_COMPARISON_TYPE ComparisonType;
    ESP_BINARY_COMPARISON Ecp;
    ESP_BOOL_COMPARISON IsFromUserMode;
    ESP_BINARY_COMPARISON Contents;
} ESP_ECP_LIST_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the ECP list comparison type. |
| Ecp | Specifies the ECP. |
| IsFromUserMode | Specifies a boolean comparison structure to compare against whether the ECP originated from user mode or kernel mode. |
| Contents | Specifies an `ESP_BINARY_COMPARISON` struct to perform a comparison against the ECP's contents. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison)
- [`ESP_ECP_LIST_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_ecp_list_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Byte range comparison

### ESP_BYTE_RANGE_COMPARISON_TYPE

The enum `ESP_BYTE_RANGE_COMPARISON_TYPE` defines a byte range comparison type.

#### Syntax

```cpp
typedef enum ESP_BYTE_RANGE_COMPARISON_TYPE
{
    ESP_BYTE_RANGE_COMPARISON_TYPE_NONE = 0,
    ESP_BYTE_RANGE_COMPARISON_TYPE_SUBSET,
    ESP_BYTE_RANGE_COMPARISON_TYPE_INTERSECTING,
    ESP_BYTE_RANGE_COMPARISON_TYPE_DISJOINT
} ESP_BYTE_RANGE_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_BYTE_RANGE_COMPARISON_TYPE_SUBSET` | The comparison matches if the LHS byte range is a subset of the RHS byte range. |
| `ESP_BYTE_RANGE_COMPARISON_TYPE_INTERSECTING` | The comparison matches if the LHS byte range intersects with the RHS byte range. |
| `ESP_BYTE_RANGE_COMPARISON_TYPE_DISJOINT` | The comparison matches if the LHS byte range and RHS byte range are disjoint. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BYTE_RANGE_COMPARISON

The structure `ESP_BYTE_RANGE_COMPARISON` is used to compare a byte range value.

#### Syntax

```cpp
typedef struct ESP_BYTE_RANGE_COMPARISON
{
    ESP_BYTE_RANGE_COMPARISON_TYPE ComparisonType;
    UINT64 Offset;
    UINT64 Length;
} ESP_BYTE_RANGE_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the byte range comparison type. |
| Offset | Specifies the byte range offset. |
| Length | Specifies the byte range length. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BYTE_RANGE_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_byte_range_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Registry data comparison

### ESP_REG_DATA_COMPARISON_TYPE

The enum `ESP_REG_DATA_COMPARISON_TYPE` defines a registry data comparison type.

#### Syntax

```cpp
typedef enum ESP_REG_DATA_COMPARISON_TYPE
{
    ESP_REG_DATA_COMPARISON_TYPE_NONE = 0,
    ESP_REG_DATA_COMPARISON_TYPE_INTEGER,
    ESP_REG_DATA_COMPARISON_TYPE_STRING,
    ESP_REG_DATA_COMPARISON_TYPE_BINARY
} ESP_REG_DATA_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_REG_DATA_COMPARISON_TYPE_INTEGER` | The registry data comparison should use an `ESP_INTEGER_COMPARISON` structure. |
| `ESP_REG_DATA_COMPARISON_TYPE_STRING` | The registry data comparison should use an `ESP_STRING_COMPARISON` structure. |
| `ESP_REG_DATA_COMPARISON_TYPE_BINARY` | The registry data comparison should use an `ESP_BINARY_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_DATA_COMPARISON

The structure `ESP_REG_DATA_COMPARISON` is used to compare registry data.

#### Syntax

```cpp
typedef struct ESP_REG_DATA_COMPARISON
{
    ESP_REG_DATA_COMPARISON_TYPE ComparisonType;

    union
    {
        ESP_INTEGER_COMPARISON Integer;
        ESP_STRING_COMPARISON String;
        ESP_BINARY_COMPARISON Binary;
    } Comparison;
} ESP_REG_DATA_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the comparison type for the registry data. |
| Comparison.Integer | Specifies an integer comparison for the data if the comparison type is integer. |
| Comparison.String | Specifies a string comparison for the data if the comparison type is string. |
| Comparison.Binary | Specifies a binary comparison for the data if the comparison type is binary. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison)
- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [`ESP_REG_DATA_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_reg_data_comparison_type)
- [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Network IP address comparison

### ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE

The enum `ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE` defines a network IP address comparison type.

#### Syntax

```cpp
typedef enum ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE
{
    ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_NONE = 0,
    ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_INCLUDES,
    ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_RANGE,
    ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_IS_IN_COLLECTION
} ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_INCLUDES` | The comparison matches if the LHS IP address includes the IP address specified in the `ESP_NETWORK_IP_ADDRESS_COMPARISON` structure. |
| `ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_RANGE` | The comparison matches if the LHS IP address is included in the range specified in the `ESP_NETWORK_IP_ADDRESS_COMPARISON` structure. |
| `ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE_IS_IN_COLLECTION` | The comparison matches if the LHS is found in the collection specified in the `ESP_NETWORK_IP_ADDRESS_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_IP_ADDRESS_COMPARISON

The structure `ESP_NETWORK_IP_ADDRESS_COMPARISON` is used to compare an IP address value.

#### Syntax

```cpp
typedef struct ESP_NETWORK_IP_ADDRESS_COMPARISON
{
    ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE ComparisonType;

    union
    {
        ESP_NETWORK_IP_ADDRESS Includes;
        ESP_NETWORK_IP_ADDRESS_RANGE Range;
        ESP_COLLECTION Collection;
    } u;
} ESP_NETWORK_IP_ADDRESS_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the IP address comparison type. |
| Includes | Specifies an IP address to compare against if the comparison type is includes. |
| Range | Specifies the IP address range if the comparison type is range. |
| Collection | Specifies a collection to compare against if the comparison type is IsInCollection. The filter matches if the IP address is present in the collection. The collection's type must be binary and its entries must hold "IN_ADDR" structures for IPv4 addresses and "IN6_ADDR" structures for IPv6 addresses. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_NETWORK_IP_ADDRESS`](wesp-common-value-types.md#esp_network_ip_address)
- [`ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_network_ip_address_comparison_type)
- [`ESP_NETWORK_IP_ADDRESS_RANGE`](wesp-common-value-types.md#esp_network_ip_address_range)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Network port comparison

### ESP_NETWORK_PORT_COMPARISON_TYPE

The enum `ESP_NETWORK_PORT_COMPARISON_TYPE` defines a network port comparison type.

#### Syntax

```cpp
typedef enum ESP_NETWORK_PORT_COMPARISON_TYPE
{
    ESP_NETWORK_PORT_COMPARISON_TYPE_NONE = 0,
    ESP_NETWORK_PORT_COMPARISON_TYPE_EQUALS,
    ESP_NETWORK_PORT_COMPARISON_TYPE_NOT_EQUALS,
    ESP_NETWORK_PORT_COMPARISON_TYPE_RANGE,
    ESP_NETWORK_PORT_COMPARISON_TYPE_IS_IN_COLLECTION
} ESP_NETWORK_PORT_COMPARISON_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_NETWORK_PORT_COMPARISON_TYPE_EQUALS` | The comparison matches if the LHS network port is equal to the network port specified in the `ESP_NETWORK_PORT_COMPARISON` structure. |
| `ESP_NETWORK_PORT_COMPARISON_TYPE_NOT_EQUALS` | The comparison matches if the LHS network port isn't equal to the network port specified in the `ESP_NETWORK_PORT_COMPARISON` structure. |
| `ESP_NETWORK_PORT_COMPARISON_TYPE_RANGE` | The comparison matches if the LHS network port is included in the range specified in the `ESP_NETWORK_PORT_COMPARISON` structure. |
| `ESP_NETWORK_PORT_COMPARISON_TYPE_IS_IN_COLLECTION` | The comparison matches if the LHS network port is found in the collection specified in the `ESP_NETWORK_PORT_COMPARISON` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_PORT_COMPARISON

The structure `ESP_NETWORK_PORT_COMPARISON` is used to compare a socket's network port.

#### Syntax

```cpp
typedef struct ESP_NETWORK_PORT_COMPARISON
{
    ESP_NETWORK_PORT_COMPARISON_TYPE ComparisonType;

    union
    {
        struct
        {
            UINT16 Port;
        } Equals, NotEquals;

        struct
        {
            UINT16 StartPort;
            UINT16 EndPort;
        } Range;

        ESP_COLLECTION Collection;
    } u;
} ESP_NETWORK_PORT_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ComparisonType | Specifies the comparison type. |
| Equals.Port | Specifies the port to compare against if the comparison type is Equals or NotEquals. The port must be specified in host-byte-order. |
| Range.StartPort | Specifies the starting port of the range if the comparison type is range. The port must be specified in host-byte-order. |
| Range.EndPort | Specifies the ending port of the range if the comparison type is range. The port must be specified in host-byte-order. Note that the ending port is included in the range. |
| Collection | Specifies a collection of ports if the comparison is IsInCollection. The collection's type must be integer. The port entries in the collection must be specified in host-byte-order. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection)
- [`ESP_NETWORK_PORT_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_network_port_comparison_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Memory address comparison

### ESP_MEMORY_ADDRESS_BASIC_COMPARISON

The `ESP_MEMORY_ADDRESS_BASIC_COMPARISON` structure defines comparisons for a basic memory address query.

#### Syntax

```cpp
typedef struct ESP_MEMORY_ADDRESS_BASIC_COMPARISON
{
    ESP_INTEGER_COMPARISON BaseAddress;
    ESP_INTEGER_COMPARISON AllocationBase;
    ESP_INTEGER_COMPARISON AllocationProtect;
    ESP_INTEGER_COMPARISON PartitionId;
    ESP_INTEGER_COMPARISON RegionSize;
    ESP_INTEGER_COMPARISON State;
    ESP_INTEGER_COMPARISON Protect;
    ESP_INTEGER_COMPARISON Type;
} ESP_MEMORY_ADDRESS_BASIC_COMPARISON;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| BaseAddress | Specifies an integer comparison for the base address. |
| AllocationBase | Specifies an integer comparison for the allocation base. |
| AllocationProtect | Specifies an integer comparison for the allocation protect. |
| PartitionId | Specifies an integer comparison for the partition id. |
| RegionSize | Specifies an integer comparison for the region size. |
| State | Specifies an integer comparison for the state of the pages. |
| Protect | Specifies an integer comparison for the protection of the pages. |
| Type | Specifies an integer comparison for the type of pages. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
