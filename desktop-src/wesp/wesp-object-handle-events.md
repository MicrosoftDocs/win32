---
title: "WESP object handle events"
description: "Windows endpoint security platform API reference for object handle events, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- ESP_OB_CREATE_HANDLE_CONFIG
- ESP_OB_CREATE_HANDLE_PARAMETERS
- ESP_OB_CREATE_HANDLE_MODIFY
- ESP_OB_DUPLICATE_HANDLE_CONFIG
- ESP_OB_DUPLICATE_HANDLE_PARAMETERS
- ESP_OB_DUPLICATE_HANDLE_MODIFY
---

# Object handle events

This page contains reference entries in the [Events API family](wesp-api-reference.md#events). Each entry includes its declaration and requirements.

## Handle creation

### ESP_OB_CREATE_HANDLE_CONFIG

The structure `ESP_OB_CREATE_HANDLE_CONFIG` is used to configure a create handle event.

#### Syntax

```cpp
typedef struct ESP_OB_CREATE_HANDLE_CONFIG
{
    ESP_EVENT_OBJECT_TYPE TargetObjectType;

    union
    {
        ESP_THREAD_CONFIG ThreadConfig;
        ESP_PROCESS_CONFIG ProcessConfig;
        ESP_DESKTOP_CONFIG DesktopConfig;
    } TargetObject;

    ESP_BOOL_CONFIG KernelHandleConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG OriginalDesiredAccessConfig;
} ESP_OB_CREATE_HANDLE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TargetObjectType | Specifies the event object type of the target object. |
| TargetObject.ThreadConfig | Specifies configuration for the thread if the target object type is thread. |
| TargetObject.ProcessConfig | Specifies configuration for the process if the target object type is process. |
| TargetObject.DesktopConfig | Specifies configuration for the desktop if the target object type is desktop. |
| KernelHandleConfig | Specifies configuration for the kernel handle. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| OriginalDesiredAccessConfig | Specifies configuration for the original desired access. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_DESKTOP_CONFIG`](wesp-other-event-objects.md#esp_desktop_config)
- [`ESP_EVENT_OBJECT_TYPE`](wesp-event-object-references.md#esp_event_object_type)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_OB_CREATE_HANDLE_PARAMETERS

The `ESP_OB_CREATE_HANDLE_PARAMETERS` struct is supplied as part of a create handle event notification.

#### Syntax

```cpp
typedef struct ESP_OB_CREATE_HANDLE_PARAMETERS
{
    ESP_EVENT_OBJECT_TYPE TargetObjectType;

    union
    {
        ESP_THREAD_INFO Thread;
        ESP_PROCESS_INFO Process;
        ESP_DESKTOP_INFO Desktop;
    } TargetObject;

    BOOL KernelHandle;
    ACCESS_MASK DesiredAccess;
    ACCESS_MASK OriginalDesiredAccess;
} ESP_OB_CREATE_HANDLE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TargetObjectType | The target object type. This must be one of the following:<br>`ESP_EVENT_OBJECT_TYPE_NONE`<br>`ESP_EVENT_OBJECT_TYPE_THREAD`<br>`ESP_EVENT_OBJECT_TYPE_PROCESS`<br>`ESP_EVENT_OBJECT_TYPE_DESKTOP` |
| TargetObject.Thread | The thread event object if the target object type is thread. |
| TargetObject.Process | The process event object if the target object type is process. |
| TargetObject.Desktop | The desktop event object if the target object type is desktop. |
| KernelHandle | True if the handle is a kernel handle. |
| DesiredAccess | The desired access for the handle. To change the access mask before notification, configure `ESP_OB_CREATE_HANDLE_MODIFY` through `ESP_RULE_DESCRIPTOR.EventModify`; don't modify the received notification. |
| OriginalDesiredAccess | The desired access that was originally requested. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DESKTOP_INFO`](wesp-other-event-objects.md#esp_desktop_info)
- [`ESP_EVENT_OBJECT_TYPE`](wesp-event-object-references.md#esp_event_object_type)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_OB_CREATE_HANDLE_MODIFY

The structure `ESP_OB_CREATE_HANDLE_MODIFY` is used to modify event data for the OB create handle event.

#### Syntax

```cpp
typedef struct ESP_OB_CREATE_HANDLE_MODIFY
{
    ESP_ACCESS_MASK_MODIFICATION_LIST DesiredAccess;
} ESP_OB_CREATE_HANDLE_MODIFY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DesiredAccess | The modifications to make to the DesiredAccess field of an OB create handle event. This can be used to set or clear the access mask. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_MASK_MODIFICATION_LIST`](wesp-rule-event-modification.md#esp_access_mask_modification_list)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Handle duplication

### ESP_OB_DUPLICATE_HANDLE_CONFIG

The structure `ESP_OB_DUPLICATE_HANDLE_CONFIG` is used to configure a duplicate handle event.

#### Syntax

```cpp
typedef struct ESP_OB_DUPLICATE_HANDLE_CONFIG
{
    ESP_EVENT_OBJECT_TYPE TargetObjectType;

    union
    {
        ESP_THREAD_CONFIG ThreadConfig;
        ESP_PROCESS_CONFIG ProcessConfig;
        ESP_DESKTOP_CONFIG DesktopConfig;
    } TargetObject;

    ESP_PROCESS_CONFIG SourceProcessConfig;
    ESP_PROCESS_CONFIG TargetProcessConfig;
    ESP_BOOL_CONFIG KernelHandleConfig;
    ESP_INTEGER_CONFIG DesiredAccessConfig;
    ESP_INTEGER_CONFIG OriginalDesiredAccessConfig;
} ESP_OB_DUPLICATE_HANDLE_CONFIG;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TargetObjectType | Specifies the event object type of the target object. |
| TargetObject.ThreadConfig | Specifies configuration for the thread if the target object type is thread. |
| TargetObject.ProcessConfig | Specifies configuration for the process if the target object type is process. |
| TargetObject.DesktopConfig | Specifies configuration for the desktop if the target object type is desktop. |
| SourceProcessConfig | Specifies configuration for the source process. |
| TargetProcessConfig | Specifies configuration for the target process. |
| KernelHandleConfig | Specifies configuration for the kernel handle. |
| DesiredAccessConfig | Specifies configuration for the desired access. |
| OriginalDesiredAccessConfig | Specifies configuration for the original desired access. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config)
- [`ESP_DESKTOP_CONFIG`](wesp-other-event-objects.md#esp_desktop_config)
- [`ESP_EVENT_OBJECT_TYPE`](wesp-event-object-references.md#esp_event_object_type)
- [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config)
- [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config)
- [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_OB_DUPLICATE_HANDLE_PARAMETERS

The `ESP_OB_DUPLICATE_HANDLE_PARAMETERS` struct is supplied as part of a duplicate handle event notification.

#### Syntax

```cpp
typedef struct ESP_OB_DUPLICATE_HANDLE_PARAMETERS
{
    ESP_EVENT_OBJECT_TYPE TargetObjectType;

    union
    {
        ESP_THREAD_INFO Thread;
        ESP_PROCESS_INFO Process;
        ESP_DESKTOP_INFO Desktop;
    } TargetObject;

    ESP_PROCESS_INFO SourceProcess;
    ESP_PROCESS_INFO TargetProcess;
    BOOL KernelHandle;
    ACCESS_MASK DesiredAccess;
    ACCESS_MASK OriginalDesiredAccess;
} ESP_OB_DUPLICATE_HANDLE_PARAMETERS;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| TargetObjectType | The target object type. This must be one of the following:<br>`ESP_EVENT_OBJECT_TYPE_NONE`<br>`ESP_EVENT_OBJECT_TYPE_THREAD`<br>`ESP_EVENT_OBJECT_TYPE_PROCESS`<br>`ESP_EVENT_OBJECT_TYPE_DESKTOP` |
| TargetObject.Thread | The thread event object if the target object type is thread. |
| TargetObject.Process | The process event object if the target object type is process. |
| TargetObject.Desktop | The desktop event object if the target object type is desktop. |
| SourceProcess | The process that is the source of the handle. |
| TargetProcess | The process that receives the duplicated handle. |
| KernelHandle | True if the handle is a kernel handle. |
| DesiredAccess | The desired access for the handle. To change the access mask before notification, configure `ESP_OB_DUPLICATE_HANDLE_MODIFY` through `ESP_RULE_DESCRIPTOR.EventModify`; don't modify the received notification. |
| OriginalDesiredAccess | The desired access that was originally requested. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_DESKTOP_INFO`](wesp-other-event-objects.md#esp_desktop_info)
- [`ESP_EVENT_OBJECT_TYPE`](wesp-event-object-references.md#esp_event_object_type)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_OB_DUPLICATE_HANDLE_MODIFY

The structure `ESP_OB_DUPLICATE_HANDLE_MODIFY` is used to modify event data for the OB duplicate handle event.

#### Syntax

```cpp
typedef struct ESP_OB_DUPLICATE_HANDLE_MODIFY
{
    ESP_ACCESS_MASK_MODIFICATION_LIST DesiredAccess;
} ESP_OB_DUPLICATE_HANDLE_MODIFY;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| DesiredAccess | The modifications to make to the DesiredAccess field of an OB duplicate handle event. This can be used to set or clear the access mask. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_ACCESS_MASK_MODIFICATION_LIST`](wesp-rule-event-modification.md#esp_access_mask_modification_list)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
