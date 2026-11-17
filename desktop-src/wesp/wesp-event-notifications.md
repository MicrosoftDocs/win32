---
title: "WESP event notifications"
description: "Windows endpoint security platform API reference for event notifications, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspAllocateEventNotification
- EspFreeEventNotification
- EspArmEventNotification
- EspCompleteEventNotification
- ESP_EVENT_NOTIFICATION_FLAGS
- ESP_EVENT_NOTIFICATION_VERSION
- ESP_EVENT_NOTIFICATION
- ESP_EVENT_NOTIFICATION_DATA_V1
---

# Event notifications

This page contains reference entries in the [Event notifications API family](wesp-api-reference.md#event-notifications). Each entry includes its declaration and requirements.

## Notification functions

### EspAllocateEventNotification

The API `EspAllocateEventNotification` allocates an event notification. In order to receive event notifications in an event queue, clients need to first allocate event notifications, and then arm the notification (i.e. `EspArmEventNotification`).

This API returns NULL if memory allocation fails. Event notifications must be freed by calling `EspFreeEventNotification` when they are no longer needed.

#### Syntax

```cpp
ESP_EVENT_NOTIFICATION*
WINAPI
EspAllocateEventNotification(void);
```

#### Return value

Returns a pointer to an allocated event notification, or `NULL` if allocation fails. The caller must release the notification with `EspFreeEventNotification`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_NOTIFICATION`](wesp-event-notifications.md#esp_event_notification)
- [`EspArmEventNotification`](wesp-event-notifications.md#esparmeventnotification)
- [`EspFreeEventNotification`](wesp-event-notifications.md#espfreeeventnotification)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspFreeEventNotification

The API `EspFreeEventNotification` frees an event notification that was previously allocated by calling `EspAllocateEventNotification`. It is not safe to call this API if the notification is currently armed. Clients must ensure that no event queue is currently using the notification prior to freeing it.

#### Syntax

```cpp
void
WINAPI
EspFreeEventNotification(
    _In_ _Post_invalid_ ESP_EVENT_NOTIFICATION* Notification
    );
```

#### Parameters

##### `Notification`

Supplies the event notification to free. The supplied "Notification" cannot be used after this API returns.

#### Return value

None.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_NOTIFICATION`](wesp-event-notifications.md#esp_event_notification)
- [`EspAllocateEventNotification`](wesp-event-notifications.md#espallocateeventnotification)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspArmEventNotification

The API `EspArmEventNotification` arms an event notification for use with an event queue. When a notification is armed, the event queue temporarily takes ownership of the notification to handle incoming events and uses the supplied `ESP_EVENT_NOTIFICATION` structure to deliver an event.

After a notification is completed, it must be re-armed by calling `EspArmEventNotification` again before it can be reused to receive another notification.  An event notification must not be freed while it is armed as this can lead to a crash in the client process. In general, notifications should be freed after the event queue has been disconnected.

#### Syntax

```cpp
HRESULT
WINAPI
EspArmEventNotification(
    _In_opt_ ESP_EVENT_QUEUE Queue,
    _Inout_ ESP_EVENT_NOTIFICATION* Notification
    );
```

#### Parameters

##### `Queue`

Specifies the queue for which to arm the event notification. If the notification was previously armed, NULL can be passed to re-arm the notification with the same event queue.

##### `Notification`

Specifies the event notification to be re-armed. Clients must pass an event notification that was allocated with `EspAllocateEventNotification`.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_NOTIFICATION`](wesp-event-notifications.md#esp_event_notification)
- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCompleteEventNotification

The API `EspCompleteEventNotification` completes an event notification. This API specifies to the WESP driver that the client has finished processing the event notification. Once an event notification has been completed, all fields and structures within the event notification are no longer valid. Events can be completed out-of-order, and there can be multiple uncompleted events at a time. Additionally, there is no time limit for completing events. Clients can lazily complete event notifications if they wish to do so. In general, clients should re-arm their event notification immediately after completing it by calling `EspArmEventNotification`.

#### Syntax

```cpp
HRESULT
WINAPI
EspCompleteEventNotification(
    _Inout_ ESP_EVENT_NOTIFICATION* Notification
    );
```

#### Parameters

##### `Notification`

Specifies the notification to complete.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_NOTIFICATION`](wesp-event-notifications.md#esp_event_notification)
- [`EspArmEventNotification`](wesp-event-notifications.md#esparmeventnotification)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Notification types

### ESP_EVENT_NOTIFICATION_FLAGS

The enum `ESP_EVENT_NOTIFICATION_FLAGS` defines event notification flags.

#### Syntax

```cpp
typedef enum ESP_EVENT_NOTIFICATION_FLAGS
{
    ESP_EVENT_NOTIFICATION_FLAGS_NONE         = 0x00000000,
    ESP_EVENT_NOTIFICATION_FLAGS_DISCONNECTED = 0x00000001
} ESP_EVENT_NOTIFICATION_FLAGS;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_NOTIFICATION_FLAGS_DISCONNECTED` | Indicates that the event occurred while the event queue was disconnected (e.g. during early boot). |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_NOTIFICATION_VERSION

The enum `ESP_EVENT_NOTIFICATION_VERSION` specifies the version of an event notification.

#### Syntax

```cpp
typedef enum ESP_EVENT_NOTIFICATION_VERSION
{
    ESP_EVENT_NOTIFICATION_VERSION_NONE = 0,
    ESP_EVENT_NOTIFICATION_VERSION_1
} ESP_EVENT_NOTIFICATION_VERSION;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_NOTIFICATION_VERSION_1` | The notification's version is 1. This indicates that the NotificationData received in an `ESP_EVENT_NOTIFICATION` structure points to an `ESP_EVENT_NOTIFICATION_DATA_V1` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_NOTIFICATION

The structure `ESP_EVENT_NOTIFICATION` represents an event notification.

#### Syntax

```cpp
typedef struct ESP_EVENT_NOTIFICATION
{
    GUID EventQueueId;
    ESP_EVENT_NOTIFICATION_VERSION Version;
    void* NotificationData;
} ESP_EVENT_NOTIFICATION;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| EventQueueId | The identifier of the event queue from which the notification originated. |
| Version | The notification's version. Currently, the only supported version is `ESP_EVENT_NOTIFICATION_VERSION_1`. |
| NotificationData | The notification data. This field points to a per-version notification structure. Currently, this field always points to an `ESP_EVENT_NOTIFICATION_DATA_V1` structure. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_NOTIFICATION_VERSION`](wesp-event-notifications.md#esp_event_notification_version)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_NOTIFICATION_DATA_V1

The structure `ESP_EVENT_NOTIFICATION_DATA_V1` represents a version 1 event notification.

#### Syntax

```cpp
typedef struct ESP_EVENT_NOTIFICATION_DATA_V1
{
    UINT64 EventId;
    GUID RuleId;
    ESP_RULE_ACTION RuleAction;
    ESP_EVENT_NOTIFICATION_FLAGS NotificationFlags;
    ESP_THREAD_INFO CurrentThread;
    ESP_PROCESS_INFO CurrentProcess;
    ESP_EVENT_TYPE EventType;
    ESP_PROPERTY_QUERY ClientQuery;
    ESP_PROPERTY_QUERY EventQuery;
    const void* EventParameters;
} ESP_EVENT_NOTIFICATION_DATA_V1;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| EventId | Unique identifier for the event. The event id is sequential. It can be used to determine the ordering of events. |
| RuleId | The matching rule's id. |
| RuleAction | The matching rule's action. |
| NotificationFlags | Supplies a set of flags. The supported flags are:<br>Disconnected: Indicates that the notification was emitted while the event queue was disconnected. |
| CurrentThread | The thread on which the event originated. This is the same thread as PsGetCurrentThread. |
| CurrentProcess | The process on which the event originated. This is the same process as PsGetCurrentProcess. |
| EventType | The event type. |
| ClientQuery | Specifies the client's property query. |
| EventQuery | Specifies the event's property query. |
| EventParameters | Specifies a pointer the event type's parameters structure. Each event type has a specific structure that this field points to. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_NOTIFICATION_FLAGS`](wesp-event-notifications.md#esp_event_notification_flags)
- [`ESP_EVENT_TYPE`](wesp-event-shared-types.md#esp_event_type)
- [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info)
- [`ESP_PROPERTY_QUERY`](wesp-property-queries.md#esp_property_query)
- [`ESP_RULE_ACTION`](wesp-rule-management.md#esp_rule_action)
- [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
