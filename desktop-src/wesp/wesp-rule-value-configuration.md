---
title: "WESP rule value configuration"
description: "Windows endpoint security platform API reference for rule value configuration, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_INTEGER_CONFIG
- ESP_BOOL_CONFIG
- ESP_STRING_CONFIG
- ESP_BINARY_CONFIG
- ESP_PATH_CONFIG
- ESP_BYTE_RANGE_CONFIG
- ESP_SID_CONFIG
- ESP_SECURITY_DESCRIPTOR_CONFIG
- ESP_MEMORY_ADDRESS_BASIC_CONFIG
- ESP_NETWORK_IP_ADDRESS_CONFIG
- ESP_NETWORK_PORT_CONFIG
- ESP_EA_LIST_CONFIG
- ESP_ECP_DESCRIPTOR_CONFIG
- ESP_ECP_LIST_CONFIG
- ESP_REG_DATA_CONFIG
- ESP_REG_VALUE_QUERY_CONFIG
- ESP_REMOTE_CLIENT_CONFIG
- ESP_ACCESS_STATE_CONFIG
---

# Rule value configuration

This page contains reference entries in the [Rules API family](wesp-api-reference.md#rules). Each entry includes its declaration and requirements.

## Value configuration structures

### ESP_INTEGER_CONFIG

The structure `ESP_INTEGER_CONFIG` is used to configure an integer value.

#### Syntax

```cpp
typedef struct ESP_INTEGER_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
} ESP_INTEGER_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the integer value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_INTEGER`. |
| BindingKey | Specifies a binding key for the integer value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BOOL_CONFIG

The structure `ESP_BOOL_CONFIG` is used to configure a boolean value.

#### Syntax

```cpp
typedef struct ESP_BOOL_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
} ESP_BOOL_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the boolean value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_BOOL`. |
| BindingKey | Specifies a binding key for the boolean value. The binding key is resolved as an integer value where TRUE is equal to 1 and FALSE is equal to 0. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_STRING_CONFIG

The structure `ESP_STRING_CONFIG` is used to configure a string value.

#### Syntax

```cpp
typedef struct ESP_STRING_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    BOOL IncludeInNotification;
} ESP_STRING_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the string value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_STRING`. |
| BindingKey | Specifies a binding key for the string value. |
| IncludeInNotification | Specifies whether the string value should be sent as part of the event notification. If false, the notification will not include the string. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BINARY_CONFIG

The structure `ESP_BINARY_CONFIG` is used to configure a binary value.

#### Syntax

```cpp
typedef struct ESP_BINARY_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    BOOL IncludeInNotification;
} ESP_BINARY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the binary value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_BINARY`. |
| BindingKey | Specifies a binding key for the binary value. |
| IncludeInNotification | Specifies whether the binary value should be sent as part of the event notification. If false, the notification will not include the binary value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PATH_CONFIG

The structure `ESP_PATH_CONFIG` is used to configure a path value.

#### Syntax

```cpp
typedef struct ESP_PATH_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    BOOL IncludeInNotification;
    ESP_PATH_FORMAT NotificationFormat;
} ESP_PATH_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the path value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_PATH`. |
| BindingKey | Specifies a binding key for the path value. The binding key is interpreted as a string containing a path formatted according to the specified "NotificationFormat". |
| IncludeInNotification | Specifies whether the path value should be sent as part of the event notification. If false, the notification will not include the path value. |
| NotificationFormat | Specifies the format for the path value in the notification. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [`ESP_PATH_FORMAT`](wesp-common-utilities.md#esp_path_format)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_BYTE_RANGE_CONFIG

The structure `ESP_BYTE_RANGE_CONFIG` is used to configure a byte range value.

#### Syntax

```cpp
typedef struct ESP_BYTE_RANGE_CONFIG
{
    ESP_FILTER Filter;
    UINT64 OffsetBindingKey;
    UINT64 LengthBindingKey;
} ESP_BYTE_RANGE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the byte range value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_BYTE_RANGE`. |
| OffsetBindingKey | Specifies a binding key for the byte range's offset. The binding key is interpreted as an integer value. |
| LengthBindingKey | Specifies a binding key for the byte range's length. The binding key is interpreted as an integer value. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_SID_CONFIG

The structure `ESP_SID_CONFIG` is used to configure a SID value.

#### Syntax

```cpp
typedef struct ESP_SID_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    BOOL IncludeInNotification;
} ESP_SID_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the SID value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_SID`. |
| BindingKey | Specifies a binding key for the SID. The binding key is interpreted as a binary value. |
| IncludeInNotification | Specifies whether the SID should be sent as part of the event notification. If false, the notification will not include the SID. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_SECURITY_DESCRIPTOR_CONFIG

The structure `ESP_SECURITY_DESCRIPTOR_CONFIG` is used to configure a security descriptor value.

#### Syntax

```cpp
typedef struct ESP_SECURITY_DESCRIPTOR_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    BOOL IncludeInNotification;
} ESP_SECURITY_DESCRIPTOR_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the security descriptor value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_SECURITY_DESCRIPTOR`. |
| BindingKey | Specifies a binding key for the security descriptor. The binding key is interpreted as a binary value. |
| IncludeInNotification | Specifies whether the security descriptor should be sent as part of the event notification. If false, the notification will not include the security descriptor. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_MEMORY_ADDRESS_BASIC_CONFIG

The structure `ESP_MEMORY_ADDRESS_BASIC_CONFIG` is used to configure a memory address basic query.

#### Syntax

```cpp
typedef struct ESP_MEMORY_ADDRESS_BASIC_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    BOOL IncludeInNotification;
} ESP_MEMORY_ADDRESS_BASIC_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the memory address basic value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_MEMORY_ADDRESS_BASIC`. |
| BindingKey | Specifies a binding key for the basic memory address query. The binding key resolves as a binary value. |
| IncludeInNotification | Specifies whether a basic query should be included in the notification. If false, a basic query is not included in the notification. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_IP_ADDRESS_CONFIG

The structure `ESP_NETWORK_IP_ADDRESS_CONFIG` specifies configuration for a network IP address.

#### Syntax

```cpp
typedef struct ESP_NETWORK_IP_ADDRESS_CONFIG
{
    ESP_FILTER Filter;
} ESP_NETWORK_IP_ADDRESS_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the IP address value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_NETWORK_IP_ADDRESS`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_NETWORK_PORT_CONFIG

The structure `ESP_NETWORK_PORT_CONFIG` specifies configuration for a network port.

#### Syntax

```cpp
typedef struct ESP_NETWORK_PORT_CONFIG
{
    ESP_FILTER Filter;
} ESP_NETWORK_PORT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the network port value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_NETWORK_PORT`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EA_LIST_CONFIG

The structure `ESP_EA_LIST_CONFIG` is used to configure an EA list value.

#### Syntax

```cpp
typedef struct ESP_EA_LIST_CONFIG
{
    ESP_FILTER Filter;
    BOOL IncludeInNotification;
    BOOL IncludeEaValueBuffers;
} ESP_EA_LIST_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the EA list value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_EA_LIST`. |
| IncludeInNotification | Indicates whether the EA list value should be sent as part of the event notification. If false, the notification will not include the EA list value. |
| IncludeEaValueBuffers | Indicates whether the EA value buffers should be sent as part of the event notification. If false, the notification will not include the EA value buffers. This field is ignored if IncludeInNotification is false. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ECP_DESCRIPTOR_CONFIG

The structure `ESP_ECP_DESCRIPTOR_CONFIG` is used to configure an ECP list descriptor value.

#### Syntax

```cpp
typedef struct ESP_ECP_DESCRIPTOR_CONFIG
{
    GUID Ecp;
    BOOL IncludeInNotification;
    BOOL IncludeEcpContext;
} ESP_ECP_DESCRIPTOR_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Ecp | Specifies the ECP value to configure. |
| IncludeInNotification | Specifies whether the ECP should be sent as part of the event notification. If false, the notification will not include the ECP. |
| IncludeEcpContext | Specifies whether the ECP context should be sent as part of the event notification. If false, the notification will not include the ECP context. This parameter is ignored if IncludeInNotification is false. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ECP_LIST_CONFIG

The structure `ESP_ECP_LIST_CONFIG` is used to configure an ECP list value.

#### Syntax

```cpp
typedef struct ESP_ECP_LIST_CONFIG
{
    ESP_FILTER Filter;
    UINT32 DescriptorsCount;
    _Field_size_(DescriptorsCount) const ESP_ECP_DESCRIPTOR_CONFIG* Descriptors;
} ESP_ECP_LIST_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the ECP list value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_ECP_LIST`. |
| DescriptorsCount | Specifies the number of elements in the Descriptors array. |
| Descriptors | Specifies an array of `ESP_ECP_DESCRIPTOR_CONFIG` structures that describe the list of ECP's to include in the event notification. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ECP_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_ecp_descriptor_config)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_DATA_CONFIG

The structure `ESP_REG_DATA_CONFIG` is used to configure a registry data value.

#### Syntax

```cpp
typedef struct ESP_REG_DATA_CONFIG
{
    ESP_FILTER Filter;
    UINT64 BindingKey;
    ESP_BINDING_KEY_DATA_TYPE BindingKeyDataType;
    BOOL IncludeInNotification;
} ESP_REG_DATA_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Filter | Specifies a filter for the registry data value. The filter must have been created by calling `EspCreateFilter` with `ESP_COMPARISON_TYPE_REG_DATA`. |
| BindingKey | Specifies a binding key for the registry data. |
| BindingKeyDataType | Specifies the data type used to interpret the binding key. |
| IncludeInNotification | Specifies whether the registry data should be sent as part of the event notification. If false, the notification will not include the registry data. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BINDING_KEY_DATA_TYPE`](wesp-rule-configuration.md#esp_binding_key_data_type)
- [`ESP_FILTER`](wesp-filter-creation.md#esp_filter)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_VALUE_QUERY_CONFIG

The structure `ESP_REG_VALUE_QUERY_CONFIG` is used to configure a `ESP_REG_VALUE_QUERY` value.

#### Syntax

```cpp
typedef struct ESP_REG_VALUE_QUERY_CONFIG
{
    ESP_INTEGER_CONFIG DataTypeConfig;
    ESP_INTEGER_CONFIG DataSizeConfig;
    ESP_REG_DATA_CONFIG DataConfig;
    BOOL IncludeInNotification;
} ESP_REG_VALUE_QUERY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DataTypeConfig | Specifies configuration for the data type. |
| DataSizeConfig | Specifies configuration for the data size. |
| DataConfig | Specifies configuration for the data. |
| IncludeInNotification | Indicates whether the registry value query should be sent as part of the event notification. If false, the notification will not include the registry value query.<br>If this value is false, the "IncludeInNotification" settings for DataConfig is ignored. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REG_DATA_CONFIG`](wesp-rule-value-configuration.md#esp_reg_data_config)
- [`ESP_REG_VALUE_QUERY`](wesp-registry-events.md#esp_reg_value_query)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REMOTE_CLIENT_CONFIG

The structure `ESP_REMOTE_CLIENT_CONFIG` is used to configure a remote client structure.

#### Syntax

```cpp
typedef struct ESP_REMOTE_CLIENT_CONFIG
{
    ESP_BOOL_CONFIG IsPresentConfig;
    ESP_STRING_CONFIG ShareNameConfig;
    ESP_SID_CONFIG UserSidConfig;
    ESP_NETWORK_IP_ADDRESS_CONFIG IpAddressConfig;
    ESP_NETWORK_PORT_CONFIG PortConfig;
    BOOL IncludeInNotification;
} ESP_REMOTE_CLIENT_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| IsPresentConfig | Specifies configuration for the IsPresent field of the `ESP_REMOTE_CLIENT` structure. |
| ShareNameConfig | Specifies configuration for the share name. |
| UserSidConfig | Specifies configuration for the user sid. |
| IpAddressConfig | Specifies configuration for the IP address. |
| PortConfig | Specifies configuration for the port. |
| IncludeInNotification | Indicates whether the remote client should be sent as part of the event notification. If false, the notification will not include the remote client.<br>If this value is false, the "IncludeInNotification" settings for ShareNameConfig and UserSidConfig are ignored. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_NETWORK_IP_ADDRESS_CONFIG`](wesp-rule-value-configuration.md#esp_network_ip_address_config)
- [`ESP_NETWORK_PORT_CONFIG`](wesp-rule-value-configuration.md#esp_network_port_config)
- [`ESP_SID_CONFIG`](wesp-rule-value-configuration.md#esp_sid_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_ACCESS_STATE_CONFIG

The structure `ESP_ACCESS_STATE_CONFIG` is used to configure an `ESP_ACCESS_STATE` structure.

#### Syntax

```cpp
typedef struct ESP_ACCESS_STATE_CONFIG
{
    ESP_INTEGER_CONFIG FlagsConfig;
    ESP_INTEGER_CONFIG RemainingDesiredAccessConfig;
    ESP_INTEGER_CONFIG PreviouslyGrantedAccessConfig;
    ESP_INTEGER_CONFIG OriginalGrantedAccessConfig;
    ESP_SECURITY_DESCRIPTOR_CONFIG SecurityDescriptorConfig;
    ESP_TOKEN_CONFIG SubjectTokenConfig;
} ESP_ACCESS_STATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| FlagsConfig | Specifies configuration for the flags. |
| RemainingDesiredAccessConfig | Specifies configuration for the remaining desired access. |
| PreviouslyGrantedAccessConfig | Specifies configuration for the previously granted access. |
| OriginalGrantedAccessConfig | Specifies configuration for the original granted access. |
| SecurityDescriptorConfig | Specifies configuration for the security descriptor. |
| SubjectTokenConfig | Specifies configuration for the subject token. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_STATE`](wesp-event-shared-types.md#esp_access_state)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_SECURITY_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_security_descriptor_config)
- [`ESP_TOKEN_CONFIG`](wesp-execution-objects.md#esp_token_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
