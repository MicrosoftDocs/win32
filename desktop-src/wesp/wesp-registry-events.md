---
title: "WESP registry events"
description: "Windows endpoint security platform API reference for registry events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_REG_CREATE_KEY_CONFIG
- ESP_REG_CREATE_KEY_PARAMETERS
- ESP_REG_OPEN_KEY_CONFIG
- ESP_REG_OPEN_KEY_PARAMETERS
- ESP_REG_DELETE_KEY_CONFIG
- ESP_REG_DELETE_KEY_PARAMETERS
- ESP_REG_SET_VALUE_KEY_CONFIG
- ESP_REG_SET_VALUE_KEY_PARAMETERS
- ESP_REG_DELETE_VALUE_KEY_CONFIG
- ESP_REG_DELETE_VALUE_KEY_PARAMETERS
- ESP_REG_RENAME_KEY_CONFIG
- ESP_REG_RENAME_KEY_PARAMETERS
- ESP_REG_REPLACE_KEY_CONFIG
- ESP_REG_REPLACE_KEY_PARAMETERS
- ESP_REG_RESTORE_KEY_CONFIG
- ESP_REG_RESTORE_KEY_PARAMETERS
- ESP_REG_SET_KEY_SECURITY_CONFIG
- ESP_REG_SET_KEY_SECURITY_PARAMETERS
- ESP_REG_QUERY_KEY_CONFIG
- ESP_REG_QUERY_KEY_PARAMETERS
- ESP_REG_QUERY_VALUE_KEY_CONFIG
- ESP_REG_QUERY_VALUE_KEY_PARAMETERS
- ESP_REG_VALUE_QUERY
- ESP_REG_SAVE_KEY_CONFIG
- ESP_REG_SAVE_KEY_PARAMETERS
- ESP_REG_LOAD_KEY_CONFIG
- ESP_REG_LOAD_KEY_PARAMETERS
- ESP_REG_ENUM_KEY_CONFIG
- ESP_REG_ENUM_KEY_PARAMETERS
- ESP_REG_ENUM_VALUE_KEY_CONFIG
- ESP_REG_ENUM_VALUE_KEY_PARAMETERS
---

# Registry events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Key creation

### ESP_REG_CREATE_KEY_CONFIG

The structure `ESP_REG_CREATE_KEY_CONFIG` is used to configure a registry create key event.

#### Syntax

```cpp
typedef struct ESP_REG_CREATE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_CONFIG RegistryKeyConfig;
    ESP_INTEGER_CONFIG CreateOptionsConfig;
    ESP_STRING_CONFIG ClassConfig;
    ESP_SECURITY_DESCRIPTOR_CONFIG SecurityDescriptorConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG GrantedAccessConfig;
    ESP_INTEGER_CONFIG Wow64FlagsConfig;
    ESP_INTEGER_CONFIG AttributesConfig;
    ESP_REGISTRY_KEY_OBJECT_CONFIG ResultObjectConfig;
} ESP_REG_CREATE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyConfig | Specifies configuration for the registry key. |
| CreateOptionsConfig | Specifies configuration for the create options. |
| ClassConfig | Specifies configuration for the class. |
| SecurityDescriptorConfig | Specifies configuration for the security descriptor. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| GrantedAccessConfig | Specifies configuration for the granted access. |
| Wow64FlagsConfig | Specifies configuration for the Wow64 flags. |
| AttributesConfig | Specifies configuration for the attributes. |
| ResultObjectConfig | Specifies configuration for the result object. This field can only be set for the NotifyOnCompletion rule action. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_CONFIG`](wesp-other-event-objects.md#esp_registry_key_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_SECURITY_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_security_descriptor_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_CREATE_KEY_PARAMETERS

The structure `ESP_REG_CREATE_KEY_PARAMETERS` contains the parameters associated with a create key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_CREATE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_INFO RegistryKey;
    UINT32 CreateOptions;
    ESP_UNICODE_STRING Class;
    _Maybenull_ const SECURITY_DESCRIPTOR* SecurityDescriptor;
    ACCESS_MASK DesiredAccess;
    ACCESS_MASK GrantedAccess;
    UINT32 Wow64Flags;
    UINT32 Attributes;
    ESP_REGISTRY_KEY_OBJECT_INFO ResultObject;
} ESP_REG_CREATE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKey | The registry key being created. |
| CreateOptions | Create options that were supplied to create the key. |
| Class | The registry key's object class. |
| SecurityDescriptor | The registry key's security descriptor. |
| DesiredAccess | The access mask that was specified for the key. |
| GrantedAccess | The access mask that has been granted for the key. |
| Wow64Flags | Contains the Wow64 flags from the access mask that was passed as an input parameter in the call to create the new registry key. |
| Attributes | Contains the object-attribute flags from the Attributes member of the OBJECT_ATTRIBUTES structure that was passed as an input parameter in the call to create the new registry key. |
| ResultObject | The registry key object that was created. This parameter is only supplied for the NotifyOnCompletion action. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_INFO`](wesp-other-event-objects.md#esp_registry_key_info)
- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key open

### ESP_REG_OPEN_KEY_CONFIG

The structure `ESP_REG_OPEN_KEY_CONFIG` is used to configure a registry open key event.

#### Syntax

```cpp
typedef struct ESP_REG_OPEN_KEY_CONFIG
{
    ESP_REGISTRY_KEY_CONFIG RegistryKeyConfig;
    ESP_INTEGER_CONFIG OptionsConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG GrantedAccessConfig;
    ESP_INTEGER_CONFIG Wow64FlagsConfig;
    ESP_INTEGER_CONFIG AttributesConfig;
    ESP_REGISTRY_KEY_OBJECT_CONFIG ResultObjectConfig;
} ESP_REG_OPEN_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyConfig | Specifies configuration for the registry key. |
| OptionsConfig | Specifies configuration for the options. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| GrantedAccessConfig | Specifies configuration for the granted access. |
| Wow64FlagsConfig | Specifies configuration for the Wow64 flags. |
| AttributesConfig | Specifies configuration for the attributes. |
| ResultObjectConfig | Specifies configuration for the result object. This field can only be set for the NotifyOnCompletion rule action. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_CONFIG`](wesp-other-event-objects.md#esp_registry_key_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_OPEN_KEY_PARAMETERS

The structure `ESP_REG_OPEN_KEY_PARAMETERS` contains the parameters associated with an open key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_OPEN_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_INFO RegistryKey;
    UINT32 Options;
    ACCESS_MASK DesiredAccess;
    ACCESS_MASK GrantedAccess;
    UINT32 Wow64Flags;
    UINT32 Attributes;
    ESP_REGISTRY_KEY_OBJECT_INFO ResultObject;
} ESP_REG_OPEN_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKey | Information about the registry key being opened. |
| Options | Options that were supplied to open the key. |
| DesiredAccess | The access mask that was specified for the key. |
| GrantedAccess | The access mask that has been granted for the key. The client can modify this value as part of processing a synchronous notification. |
| Wow64Flags | Contains the Wow64 flags from the access mask that was passed as an input parameter in the call to create the new registry key. |
| Attributes | Contains the object-attribute flags from the Attributes member of the OBJECT_ATTRIBUTES structure that was passed as an input parameter in the call to create the new registry key. |
| ResultObject | The registry key object that was opened. This parameter is only supplied for the NotifyOnCompletion action. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_INFO`](wesp-other-event-objects.md#esp_registry_key_info)
- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key deletion

### ESP_REG_DELETE_KEY_CONFIG

The structure `ESP_REG_DELETE_KEY_CONFIG` is used to configure a registry delete key event.

#### Syntax

```cpp
typedef struct ESP_REG_DELETE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
} ESP_REG_DELETE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_DELETE_KEY_PARAMETERS

The structure `ESP_REG_DELETE_KEY_PARAMETERS` contains the parameters associated with a delete key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_DELETE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
} ESP_REG_DELETE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | A registry key object for the registry key being deleted. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Value updates

### ESP_REG_SET_VALUE_KEY_CONFIG

The structure `ESP_REG_SET_VALUE_KEY_CONFIG` is used to configure a registry set value key event.

#### Syntax

```cpp
typedef struct ESP_REG_SET_VALUE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_STRING_CONFIG ValueNameConfig;
    ESP_REG_VALUE_QUERY_CONFIG OldDataConfig;
    ESP_REG_VALUE_QUERY_CONFIG NewDataConfig;
} ESP_REG_SET_VALUE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| ValueNameConfig | Specifies configuration for the value name. |
| OldDataConfig | Specifies configuration for the old data being replaced. |
| NewDataConfig | Specifies configuration for the new data being set. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_REG_VALUE_QUERY_CONFIG`](wesp-rule-value-configuration.md#esp_reg_value_query_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_SET_VALUE_KEY_PARAMETERS

The structure `ESP_REG_SET_VALUE_KEY_PARAMETERS` contains the parameters associated with a set value key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_SET_VALUE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_UNICODE_STRING ValueName;
    ESP_REG_VALUE_QUERY OldData;
    ESP_REG_VALUE_QUERY NewData;
} ESP_REG_SET_VALUE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| ValueName | The registry value name being set. |
| OldData | The value's old data. By default, the OIdData is not provided. The client must specify to include the old data through the "OldDataConfig" field in the structure `ESP_REG_SET_VALUE_KEY_CONFIG`. |
| NewData | The value's new data. By default, the NewData is not provided. The client must specify to include the new data through the "NewDataConfig" field in the structure `ESP_REG_SET_VALUE_KEY_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [`ESP_REG_VALUE_QUERY`](wesp-registry-events.md#esp_reg_value_query)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Value deletion

### ESP_REG_DELETE_VALUE_KEY_CONFIG

The structure `ESP_REG_DELETE_VALUE_KEY_CONFIG` is used to configure a registry delete value key event.

#### Syntax

```cpp
typedef struct ESP_REG_DELETE_VALUE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_STRING_CONFIG ValueNameConfig;
    ESP_REG_VALUE_QUERY_CONFIG DataConfig;
} ESP_REG_DELETE_VALUE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| ValueNameConfig | Specifies configuration for the value name. |
| DataConfig | Specifies configuration for the data being deleted. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_REG_VALUE_QUERY_CONFIG`](wesp-rule-value-configuration.md#esp_reg_value_query_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_DELETE_VALUE_KEY_PARAMETERS

The structure `ESP_REG_DELETE_VALUE_KEY_PARAMETERS` contains the parameters associated with a delete value key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_DELETE_VALUE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_UNICODE_STRING ValueName;
    ESP_REG_VALUE_QUERY Data;
} ESP_REG_DELETE_VALUE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| ValueName | The value name being deleted. |
| Data | The value's data. By default, the data is not provided. The client must specify to include the data through the "DataConfig" field in the structure `ESP_REG_DELETE_VALUE_KEY_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [`ESP_REG_VALUE_QUERY`](wesp-registry-events.md#esp_reg_value_query)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key renaming

### ESP_REG_RENAME_KEY_CONFIG

The structure `ESP_REG_RENAME_KEY_CONFIG` is used to configure a registry rename key event.

#### Syntax

```cpp
typedef struct ESP_REG_RENAME_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_STRING_CONFIG NewNameConfig;
} ESP_REG_RENAME_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| NewNameConfig | Specifies configuration for the new name. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_RENAME_KEY_PARAMETERS

The structure `ESP_REG_RENAME_KEY_PARAMETERS` contains the parameters associated with a rename key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_RENAME_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_UNICODE_STRING NewName;
} ESP_REG_RENAME_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| NewName | The new name for the registry key. By default, the NewName is not provided. The client must specify to include the new name through the "NewNameConfig" field in the structure `ESP_REG_RENAME_KEY_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key replacement

### ESP_REG_REPLACE_KEY_CONFIG

The structure `ESP_REG_REPLACE_KEY_CONFIG` is used to configure a registry replace key event.

#### Syntax

```cpp
typedef struct ESP_REG_REPLACE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_PATH_CONFIG OldFilePathConfig;
    ESP_PATH_CONFIG NewFilePathConfig;
} ESP_REG_REPLACE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| OldFilePathConfig | Specifies configuration for the old file path. |
| NewFilePathConfig | Specifies configuration for the new file path. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PATH_CONFIG`](wesp-rule-value-configuration.md#esp_path_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_REPLACE_KEY_PARAMETERS

The structure `ESP_REG_REPLACE_KEY_PARAMETERS` contains the parameters associated with a replace key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_REPLACE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_PATH OldFilePath;
    ESP_PATH NewFilePath;
} ESP_REG_REPLACE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| OldFilePath | The path of the file that receives a backup copy of the registry information being replaced. By default, the OldFilePath is not provided. The client must specify to include it through the "OldFilePathConfig" field in the structure `ESP_REG_REPLACE_KEY_CONFIG`. |
| NewFilePath | The path of the new file with the registry information. By default, the NewFilePath is not provided. The client must specify to include it through the "NewFilePathConfig" field in the structure `ESP_REG_REPLACE_KEY_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PATH`](wesp-common-utilities.md#esp_path)
- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key restore

### ESP_REG_RESTORE_KEY_CONFIG

The structure `ESP_REG_RESTORE_KEY_CONFIG` is used to configure a registry restore key event.

#### Syntax

```cpp
typedef struct ESP_REG_RESTORE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_FILE_OBJECT_CONFIG FileConfig;
    ESP_INTEGER_CONFIG FlagsConfig;
} ESP_REG_RESTORE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| FileConfig | Specifies configuration for the file. |
| FlagsConfig | Specifies configuration for the flags. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_RESTORE_KEY_PARAMETERS

The structure `ESP_REG_RESTORE_KEY_PARAMETERS` contains the parameters associated with a restore key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_RESTORE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_FILE_OBJECT_INFO File;
    UINT32 Flags;
} ESP_REG_RESTORE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| File | The file from which the hive will be restored. |
| Flags | Flags for the restore operation. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key security

### ESP_REG_SET_KEY_SECURITY_CONFIG

The structure `ESP_REG_SET_KEY_SECURITY_CONFIG` is used to configure a registry set key security event.

#### Syntax

```cpp
typedef struct ESP_REG_SET_KEY_SECURITY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_INTEGER_CONFIG SecurityInformationConfig;
    ESP_SECURITY_DESCRIPTOR_CONFIG SecurityDescriptorConfig;
} ESP_REG_SET_KEY_SECURITY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| SecurityInformationConfig | Specifies configuration for the security information. |
| SecurityDescriptorConfig | Specifies configuration for the security descriptor. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_SECURITY_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_security_descriptor_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_SET_KEY_SECURITY_PARAMETERS

The structure `ESP_REG_SET_KEY_SECURITY_PARAMETERS` contains the parameters associated with a set key security event notification.

#### Syntax

```cpp
typedef struct ESP_REG_SET_KEY_SECURITY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    SECURITY_INFORMATION SecurityInformation;
    _Maybenull_ const SECURITY_DESCRIPTOR* SecurityDescriptor;
} ESP_REG_SET_KEY_SECURITY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| SecurityInformation | Security information that is being set for the registry key. |
| SecurityDescriptor | Security descriptor for the registry key. By default, the SecurityDescriptor is not provided. The client must specify to include it through the "SecurityDescriptorConfig" field in the structure `ESP_REG_SET_KEY_SECURITY_CONFIG`. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key queries

### ESP_REG_QUERY_KEY_CONFIG

The structure `ESP_REG_QUERY_KEY_CONFIG` is used to configure a registry query key event.

#### Syntax

```cpp
typedef struct ESP_REG_QUERY_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
} ESP_REG_QUERY_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| InformationClassConfig | Specifies configuration for the information class. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_QUERY_KEY_PARAMETERS

The structure `ESP_REG_QUERY_KEY_PARAMETERS` contains the parameters associated with a query key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_QUERY_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    UINT32 InformationClass;
} ESP_REG_QUERY_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| InformationClass | The information class that was supplied (KEY_INFORMATION_CLASS). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Value queries

### ESP_REG_QUERY_VALUE_KEY_CONFIG

The structure `ESP_REG_QUERY_VALUE_KEY_CONFIG` is used to configure a registry query value key event.

#### Syntax

```cpp
typedef struct ESP_REG_QUERY_VALUE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_STRING_CONFIG ValueNameConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
} ESP_REG_QUERY_VALUE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| ValueNameConfig | Specifies configuration for the value name. |
| InformationClassConfig | Specifies configuration for the information class. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_QUERY_VALUE_KEY_PARAMETERS

The structure `ESP_REG_QUERY_VALUE_KEY_PARAMETERS` contains the parameters associated with a query value key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_QUERY_VALUE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_UNICODE_STRING ValueName;
    UINT32 InformationClass;
} ESP_REG_QUERY_VALUE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| ValueName | The value name being queried. By default, the ValueName is not provided. The client must specify to include it through the "ValueNameConfig" field in the structure `ESP_REG_QUERY_VALUE_KEY_CONFIG`. |
| InformationClass | The information class that was supplied (KEY_VALUE_INFORMATION_CLASS). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_VALUE_QUERY

The structure `ESP_REG_VALUE_QUERY` is used to represent a registry value query.

#### Syntax

```cpp
typedef struct ESP_REG_VALUE_QUERY
{
    UINT32 DataType;
    UINT32 DataSize;
    _Field_size_bytes_(DataSize) const void* Data;
} ESP_REG_VALUE_QUERY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DataType | Specifies the registry value's data type (e.g. REG_DWORD, REG_SZ, etc). |
| DataSize | Specifies the size in bytes of the registry value's data. |
| Data | Specifies the registry value's data. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key save

### ESP_REG_SAVE_KEY_CONFIG

The structure `ESP_REG_SAVE_KEY_CONFIG` is used to configure a registry save key event.

#### Syntax

```cpp
typedef struct ESP_REG_SAVE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_FILE_OBJECT_CONFIG FileConfig;
    ESP_INTEGER_CONFIG FormatConfig;
} ESP_REG_SAVE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| FileConfig | Specifies configuration for the file. |
| FormatConfig | Specifies configuration for the format. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_SAVE_KEY_PARAMETERS

The structure `ESP_REG_SAVE_KEY_PARAMETERS` contains the parameters associated with a save key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_SAVE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_FILE_OBJECT_INFO File;
    UINT32 Format;
} ESP_REG_SAVE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| File | The file the registry key is being saved to. |
| Format | The format for the file. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key loading

### ESP_REG_LOAD_KEY_CONFIG

The structure `ESP_REG_LOAD_KEY_CONFIG` is used to configure a registry load key event.

#### Syntax

```cpp
typedef struct ESP_REG_LOAD_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_STRING_CONFIG RootKeyNameConfig;
    ESP_PATH_CONFIG SourceFilePathConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_TOKEN_CONFIG FileAccessTokenConfig;
} ESP_REG_LOAD_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| RootKeyNameConfig | Specifies configuration for the root key name. |
| SourceFilePathConfig | Specifies configuration for the source file path. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| FileAccessTokenConfig | Specifies configuration for the file access token. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_PATH_CONFIG`](wesp-rule-value-configuration.md#esp_path_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [`ESP_TOKEN_CONFIG`](wesp-execution-objects.md#esp_token_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_LOAD_KEY_PARAMETERS

The structure `ESP_REG_LOAD_KEY_PARAMETERS` contains the parameters associated with a load key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_LOAD_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    ESP_UNICODE_STRING RootKeyName;
    ESP_PATH SourceFilePath;
    ACCESS_MASK DesiredAccess;
    ESP_TOKEN_INFO FileAccessToken;
} ESP_REG_LOAD_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object for the root key of the hive that is about to be loaded. |
| RootKeyName | The name of the root key. |
| SourceFilePath | The source file path being loaded. |
| DesiredAccess | The access mask that was specified by the thread that is trying to load the registry key. |
| FileAccessToken | A token that is used when accessing the hive file being loaded into the registry. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PATH`](wesp-common-utilities.md#esp_path)
- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [`ESP_TOKEN_INFO`](wesp-execution-objects.md#esp_token_info)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Key enumeration

### ESP_REG_ENUM_KEY_CONFIG

The structure `ESP_REG_ENUM_KEY_CONFIG` is used to configure a registry enum key event.

#### Syntax

```cpp
typedef struct ESP_REG_ENUM_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_INTEGER_CONFIG IndexConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
} ESP_REG_ENUM_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| IndexConfig | Specifies configuration for the index. |
| InformationClassConfig | Specifies configuration for the information class. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_ENUM_KEY_PARAMETERS

The structure `ESP_REG_ENUM_KEY_PARAMETERS` contains the parameters associated with an enum key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_ENUM_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    UINT32 Index;
    UINT32 InformationClass;
} ESP_REG_ENUM_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| Index | The zero-based index of the subkey within the key. |
| InformationClass | The information class that was supplied (KEY_INFORMATION_CLASS). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Value enumeration

### ESP_REG_ENUM_VALUE_KEY_CONFIG

The structure `ESP_REG_ENUM_VALUE_KEY_CONFIG` is used to configure a registry enum value key event.

#### Syntax

```cpp
typedef struct ESP_REG_ENUM_VALUE_KEY_CONFIG
{
    ESP_REGISTRY_KEY_OBJECT_CONFIG RegistryKeyObjectConfig;
    ESP_INTEGER_CONFIG IndexConfig;
    ESP_INTEGER_CONFIG InformationClassConfig;
} ESP_REG_ENUM_VALUE_KEY_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObjectConfig | Specifies configuration for the registry key object. |
| IndexConfig | Specifies configuration for the index. |
| InformationClassConfig | Specifies configuration for the information class. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_REG_ENUM_VALUE_KEY_PARAMETERS

The structure `ESP_REG_ENUM_VALUE_KEY_PARAMETERS` contains the parameters associated with an enum value key event notification.

#### Syntax

```cpp
typedef struct ESP_REG_ENUM_VALUE_KEY_PARAMETERS
{
    ESP_REGISTRY_KEY_OBJECT_INFO RegistryKeyObject;
    UINT32 Index;
    UINT32 InformationClass;
} ESP_REG_ENUM_VALUE_KEY_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| RegistryKeyObject | The registry key object. |
| Index | The zero-based index of the subkey within the key. |
| InformationClass | The information class that was supplied (KEY_VALUE_INFORMATION_CLASS). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
