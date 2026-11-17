---
title: "WESP process events"
description: "Windows endpoint security platform API reference for process events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_PROCESS_CREATE_CONFIG
- ESP_PROCESS_CREATE_PARAMETERS
- ESP_PROCESS_TERMINATE_CONFIG
- ESP_PROCESS_TERMINATE_PARAMETERS
- ESP_PROCESS_LOAD_IMAGE_CONFIG
- ESP_PROCESS_LOAD_IMAGE_PARAMETERS
---

# Process events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Process creation

### ESP_PROCESS_CREATE_CONFIG

The structure `ESP_PROCESS_CREATE_CONFIG` is used to configure a process create event.

#### Syntax

```cpp
typedef struct ESP_PROCESS_CREATE_CONFIG
{
    ESP_PROCESS_CONFIG ProcessConfig;
    ESP_FILE_OBJECT_CONFIG FileObjectConfig;
    ESP_STRING_CONFIG OriginalCommandLineConfig;
    ESP_THREAD_CONFIG CreatingThreadConfig;
} ESP_PROCESS_CREATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ProcessConfig | Specifies configuration for the process being created. Note that the "ParentProcessConfig" field in the process config structure can be used to configure the parent process. |
| FileObjectConfig | Specifies configuration for the process executable file. |
| OriginalCommandLineConfig | Specifies string configuration for the original command line. |
| CreatingThreadConfig | Specifies configuration for the creating thread. Note that the "OwningProcessConfig" field in the creating thread config structure can be used to configure the creating process. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROCESS_CREATE_PARAMETERS

The structure `ESP_PROCESS_CREATE_PARAMETERS` contains the parameters associated with a process create event notification.

#### Syntax

```cpp
typedef struct ESP_PROCESS_CREATE_PARAMETERS
{
    ESP_PROCESS_INFO Process;
    ESP_FILE_OBJECT_INFO FileObject;
    ESP_UNICODE_STRING OriginalCommandLine;
    ESP_THREAD_INFO CreatingThread;
} ESP_PROCESS_CREATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Process | The process being created. |
| FileObject | The file object for the process executable file. |
| OriginalCommandLine | The command line for the process. By default, the original command line is not supplied. The client must specify to include the command line through the "OriginalCommandLineConfig" field in the structure `ESP_PROCESS_CREATE_CONFIG`. |
| CreatingThread | The thread creating the new process. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Process termination

### ESP_PROCESS_TERMINATE_CONFIG

The structure `ESP_PROCESS_TERMINATE_CONFIG` is used to configure a process terminate event.

#### Syntax

```cpp
typedef struct ESP_PROCESS_TERMINATE_CONFIG
{
    ESP_PROCESS_CONFIG ProcessConfig;
} ESP_PROCESS_TERMINATE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ProcessConfig | Specifies configuration for the process being terminated. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROCESS_TERMINATE_PARAMETERS

The structure `ESP_PROCESS_TERMINATE_PARAMETERS` contains the parameters associated with a process terminate event notification.

#### Syntax

```cpp
typedef struct ESP_PROCESS_TERMINATE_PARAMETERS
{
    ESP_PROCESS_INFO Process;
} ESP_PROCESS_TERMINATE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Process | The process being terminated. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Image loading

### ESP_PROCESS_LOAD_IMAGE_CONFIG

The structure `ESP_PROCESS_LOAD_IMAGE_CONFIG` is used to configure a process load image event.

#### Syntax

```cpp
typedef struct ESP_PROCESS_LOAD_IMAGE_CONFIG
{
    ESP_PROCESS_CONFIG ProcessConfig;
    ESP_FILE_OBJECT_CONFIG ImageFileConfig;
    ESP_INTEGER_CONFIG ImageBaseConfig;
    ESP_MEMORY_ADDRESS_BASIC_CONFIG ImageBaseBasicConfig;
    ESP_PATH_CONFIG ImageBaseMappedFilePathConfig;
    ESP_INTEGER_CONFIG ImageSizeConfig;
    ESP_INTEGER_CONFIG PropertiesConfig;
} ESP_PROCESS_LOAD_IMAGE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| ProcessConfig | Specifies configuration for the process in which the image is being loaded. |
| ImageFileConfig | Specifies configuration for the image file being loaded. |
| ImageBaseConfig | Specifies configuration for the image base. |
| ImageBaseBasicConfig | Specifies configuration for basic memory address information for the image base. |
| ImageBaseMappedFilePathConfig | Specifies configuration for the image base mapped file path. |
| ImageSizeConfig | Specifies configuration for the image size. |
| PropertiesConfig | Specifies configuration for the image properties. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_MEMORY_ADDRESS_BASIC_CONFIG`](wesp-rule-value-configuration.md#esp_memory_address_basic_config)
- [`ESP_PATH_CONFIG`](wesp-rule-value-configuration.md#esp_path_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_PROCESS_LOAD_IMAGE_PARAMETERS

The structure `ESP_PROCESS_LOAD_IMAGE_PARAMETERS` contains the parameters associated with a process load image event notification.

#### Syntax

```cpp
typedef struct ESP_PROCESS_LOAD_IMAGE_PARAMETERS
{
    ESP_PROCESS_INFO Process;
    ESP_FILE_OBJECT_INFO ImageFile;
    UINT64 ImageBase;
    _Maybenull_ const ESP_MEMORY_ADDRESS_BASIC* ImageBaseBasic;
    ESP_PATH ImageBaseMappedFilePath;
    UINT64 ImageSize;
    UINT32 Properties;
} ESP_PROCESS_LOAD_IMAGE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| Process | The process for which an image is being loaded. |
| ImageFile | The image file being loaded. |
| ImageBase | The base address of the image. |
| ImageBaseBasic | Basic memory address information for the base address. This field is null unless it was configured to be included through the ImageBaseBasicConfig field in the rule's associated `ESP_PROCESS_LOAD_IMAGE_CONFIG` structure. |
| ImageBaseMappedFilePath | Mapped file path for the base address. This field is empty unless it was configured to be included through the ImageBaseMappedFilePathConfig field in the rule's associated `ESP_PROCESS_LOAD_IMAGE_CONFIG` structure. |
| ImageSize | The virtual size in bytes of the image. |
| Properties | Image properties. This is the equivalent of the "Properties" field in the kernel structure "IMAGE_INFO". |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info)
- [`ESP_MEMORY_ADDRESS_BASIC`](wesp-common-value-types.md#esp_memory_address_basic)
- [`ESP_PATH`](wesp-common-utilities.md#esp_path)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
