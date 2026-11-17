---
title: "WESP common shared value types"
description: "Windows endpoint security platform API reference for common shared value types, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_SUBSYSTEM_INFORMATION_TYPE
- ESP_FO_TARGET_OBJECT_TYPE
- ESP_NETWORK_ADDRESS_FAMILY
- ESP_NETWORK_RANGE_TYPE
- ESP_BYTE_RANGE
- ESP_EA_DESCRIPTOR
- ESP_EA_LIST
- ESP_MEMORY_ADDRESS_BASIC
- ESP_NETWORK_IP_ADDRESS
- ESP_NETWORK_IP_ADDRESS_RANGE
---

# Common shared value types

This page contains reference entries in the [Common API family](wesp-api-reference.md#common). Each entry includes its declaration and requirements.

## Shared enumerations

### ESP_SUBSYSTEM_INFORMATION_TYPE

The enum `ESP_SUBSYSTEM_INFORMATION_TYPE` represents a process subsystem type.

#### Syntax

```cpp
typedef enum ESP_SUBSYSTEM_INFORMATION_TYPE {
  ESP_SUBSYSTEM_INFORMATION_TYPE_NONE = 0,
  ESP_SUBSYSTEM_INFORMATION_TYPE_WIN32,
  ESP_SUBSYSTEM_INFORMATION_TYPE_WSL
} ESP_SUBSYSTEM_INFORMATION_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_SUBSYSTEM_INFORMATION_TYPE_WIN32` | The process's subsystem is WIN32. |
| `ESP_SUBSYSTEM_INFORMATION_TYPE_WSL` | The process's subsystem is WSL. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_FO_TARGET_OBJECT_TYPE

The enum `ESP_FO_TARGET_OBJECT_TYPE` specifies the target object type for a file object.

#### Syntax

```cpp
typedef enum ESP_FO_TARGET_OBJECT_TYPE
{
    ESP_FO_TARGET_OBJECT_TYPE_NONE = 0,
    ESP_FO_TARGET_OBJECT_TYPE_FILE_STREAM,
    ESP_FO_TARGET_OBJECT_TYPE_VOLUME,
    ESP_FO_TARGET_OBJECT_TYPE_PIPE,
    ESP_FO_TARGET_OBJECT_TYPE_MAILSLOT
} ESP_FO_TARGET_OBJECT_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_FO_TARGET_OBJECT_TYPE_FILE_STREAM` | The file object is targeting a file stream. |
| `ESP_FO_TARGET_OBJECT_TYPE_VOLUME` | The file object is targeting a volume. |
| `ESP_FO_TARGET_OBJECT_TYPE_PIPE` | The file object is targeting a pipe. |
| `ESP_FO_TARGET_OBJECT_TYPE_MAILSLOT` | The file object is targeting a mailslot. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_ADDRESS_FAMILY

The enum `ESP_NETWORK_ADDRESS_FAMILY` defines a network address family.

#### Syntax

```cpp
typedef enum ESP_NETWORK_ADDRESS_FAMILY
{
    ESP_NETWORK_ADDRESS_FAMILY_NONE = 0,
    ESP_NETWORK_ADDRESS_FAMILY_IPV4,
    ESP_NETWORK_ADDRESS_FAMILY_IPV6
} ESP_NETWORK_ADDRESS_FAMILY;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_NETWORK_ADDRESS_FAMILY_IPV4` | An IPv4 address. |
| `ESP_NETWORK_ADDRESS_FAMILY_IPV6` | An IPv6 address. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_RANGE_TYPE

The enum `ESP_NETWORK_RANGE_TYPE` represents a kind of network range.

#### Syntax

```cpp
typedef enum ESP_NETWORK_RANGE_TYPE
{
    ESP_NETWORK_RANGE_TYPE_NONE = 0,
    ESP_NETWORK_RANGE_TYPE_SPAN,
    ESP_NETWORK_RANGE_TYPE_SUBNET
} ESP_NETWORK_RANGE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_NETWORK_RANGE_TYPE_SPAN` | The network range type is a span. This is an inclusive range of IP addresses defined by a start address and end address. An IP address matches the range if its address is greater than or equal to the range's StartAddress and less than or equal to the range's EndAddress. |
| `ESP_NETWORK_RANGE_TYPE_SUBNET` | The network range type is a subnet. This is a prefix based match. An IP address matches a subnet range if its most significant bit, determined by the PrefixLength are identical to the Address specified in the `ESP_NETWORK_IP_ADDRESS_RANGE` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Shared structures

### ESP_BYTE_RANGE

The structure `ESP_BYTE_RANGE` represents a byte range.

#### Syntax

```cpp
typedef struct ESP_BYTE_RANGE
{
    UINT64 Offset;
    UINT64 Length;
} ESP_BYTE_RANGE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Offset | Specifies the offset in bytes where the range starts. |
| Length | Specifies the length in bytes of the range. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EA_DESCRIPTOR

The structure `ESP_EA_DESCRIPTOR` describes an extended attribute.

#### Syntax

```cpp
typedef struct ESP_EA_DESCRIPTOR
{
    UINT8 Flags;
    PCSTR EaName;
    UINT32 EaValueSize;
    _Field_size_bytes_(EaValueSize) const void* EaValue;
} ESP_EA_DESCRIPTOR;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Flags | Specifies flags for the EA. This is either 0 or FILE_NEED_EA. |
| EaName | Specifies the EA name. |
| EaValueSize | Specifies the size in bytes of the EA value. |
| EaValue | Specifies the EA's value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EA_LIST

The structure `ESP_EA_LIST` is used to describe a list of extended attributes.

#### Syntax

```cpp
typedef struct ESP_EA_LIST
{
    UINT32 DescriptorsCount;
    _Field_size_(DescriptorsCount) const ESP_EA_DESCRIPTOR* Descriptors;
} ESP_EA_LIST;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DescriptorsCount | Specifies the number of elements in the descriptors array. |
| Descriptors | Specifies an array of `ESP_EA_DESCRIPTOR` structures. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EA_DESCRIPTOR`](wesp-common-value-types.md#esp_ea_descriptor)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_MEMORY_ADDRESS_BASIC

The structure `ESP_MEMORY_ADDRESS_BASIC_QUERY` specifies information for a basic memory address query.

#### Syntax

```cpp
typedef struct ESP_MEMORY_ADDRESS_BASIC
{
    UINT64 BaseAddress;
    UINT64 AllocationBase;
    UINT32 AllocationProtect;
    UINT16 PartitionId;
    SIZE_T RegionSize;
    UINT32 State;
    UINT32 Protect;
    UINT32 Type;
} ESP_MEMORY_ADDRESS_BASIC;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| BaseAddress | Specifies the base address of the region of pages. |
| AllocationBase | Specifies a pointer to the base address of a range of pages allocated by the VirtualAlloc function. The page pointed to by the BaseAddress member is contained within this allocation range. |
| AllocationProtect | Specifies the memory protection option when the region was initially allocated. |
| PartitionId | Specifies the partition id. |
| RegionSize | Specifies the size of the region beginning at the base address in which all pages have identical attributes, in bytes. |
| State | Specifies the state of the pages in the region. This can be one of the following:<br>MEM_COMMIT<br>MEM_FREE<br>MEM_RESERVE |
| Protect | Specifies the access protection of the pages in the region. |
| Type | Specifies the type of pages in the region. This can be one of the following:<br>MEM_IMAGE<br>MEM_MAPPED<br>MEM_PRIVATE |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_IP_ADDRESS

The structure `ESP_NETWORK_IP_ADDRESS` represents an IP address.

#### Syntax

```cpp
typedef struct ESP_NETWORK_IP_ADDRESS
{
    ESP_NETWORK_ADDRESS_FAMILY AddressFamily;

    union
    {
        IN_ADDR V4;
        IN6_ADDR V6;
    } Address;
} ESP_NETWORK_IP_ADDRESS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| AddressFamily | Specifies the address family. The supported values are:<br>IPv4<br>IPv6 |
| Address.V4 | Specifies an IPv4 address if the address family is IPv4. |
| Address.V6 | Specifies an IPv6 address if the address family is IPv6. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_NETWORK_ADDRESS_FAMILY`](wesp-common-value-types.md#esp_network_address_family)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_IP_ADDRESS_RANGE

The structure `ESP_NETWORK_IP_ADDRESS_RANGE` represents a range of IP addresses.

#### Syntax

```cpp
typedef struct ESP_NETWORK_IP_ADDRESS_RANGE
{
    ESP_NETWORK_RANGE_TYPE RangeType;

    union
    {
        struct
        {
            ESP_NETWORK_IP_ADDRESS StartAddress;
            ESP_NETWORK_IP_ADDRESS EndAddress;
        } Span;

        struct
        {
            ESP_NETWORK_IP_ADDRESS Address;
            UINT8 PrefixLength;
        } Subnet;
    } Range;
} ESP_NETWORK_IP_ADDRESS_RANGE;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RangeType | Specifies the range type. The supported values are:<br>Span<br>Subnet |
| Span.StartAddress | Specifies the start address when the range is span. |
| Span.EndAddress | Specifies the end address when the range is span. The end address is included in the range. |
| Subnet.Address | Specifies the address when the range is subnet. |
| Subnet.PrefixLength | Specifies the prefix length when the range is subnet. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_NETWORK_IP_ADDRESS`](wesp-common-value-types.md#esp_network_ip_address)
- [`ESP_NETWORK_RANGE_TYPE`](wesp-common-value-types.md#esp_network_range_type)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
