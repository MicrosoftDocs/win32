---
title: "WESP event queue creation and management"
description: "Windows endpoint security platform API reference for event queue creation and management, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspCreateEventQueue
- EspOpenEventQueue
- EspCloseEventQueue
- EspGetEventQueueId
- EspClearEventQueue
- EspEnumerateEventQueueIds
- ESP_EVENT_QUEUE
- ESP_EVENT_QUEUE_TYPE
- ESP_EVENT_QUEUE_LIFETIME
- ESP_EVENT_QUEUE_DESCRIPTOR
---

# Event queue creation and management

This page contains reference entries in the [Event queues API family](wesp-api-reference.md#event-queues). Each entry includes its declaration and requirements.

## Queue functions

### EspCreateEventQueue

The API `EspCreateEventQueue` creates an event queue for a client.

#### Syntax

```cpp
HRESULT
WINAPI
EspCreateEventQueue(
    _In_ ESP_CLIENT Client,
    _In_ const ESP_EVENT_QUEUE_DESCRIPTOR* Descriptor,
    _Out_ ESP_EVENT_QUEUE* Queue
    );
```

#### Parameters

##### `Client`

Specifies the client for which to create the event queue.

##### `Descriptor`

Specifies an `ESP_EVENT_QUEUE_DESCRIPTOR` structure that describes the event queue.

##### `Queue`

Receives the event queue handle. This handle must be closed by calling `EspCloseEventQueue` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_ALREADY_EXISTS` | An event queue with the specified ID already exists. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [`ESP_EVENT_QUEUE_DESCRIPTOR`](wesp-event-queue-management.md#esp_event_queue_descriptor)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspOpenEventQueue

The API `EspOpenEventQueue` opens an existing event queue.

#### Syntax

```cpp
HRESULT
WINAPI
EspOpenEventQueue(
    _In_ ESP_CLIENT Client,
    _In_ const GUID* QueueId,
    _Out_ ESP_EVENT_QUEUE* Queue
    );
```

#### Parameters

##### `Client`

Specifies the client for which to open the event queue.

##### `QueueId`

Specifies the queue ID to open.

##### `Queue`

Receives the event queue handle. This handle must be closed by calling `EspCloseEventQueue` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_NOT_FOUND` | An event queue with the specified ID doesn't exist. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspCloseEventQueue

The API `EspCloseEventQueue` closes an event queue handle. If the event queue was connected through this handle (e.g. `EspConnectEventQueueWithIocp`), it will be disconnected as part of this API.

#### Syntax

```cpp
HRESULT
WINAPI
EspCloseEventQueue(
    _In_ _Post_invalid_ ESP_EVENT_QUEUE Queue
    );
```

#### Parameters

##### `Queue`

Specifies the event queue.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [`EspConnectEventQueueWithIocp`](wesp-event-queue-delivery.md#espconnecteventqueuewithiocp)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspGetEventQueueId

The API `EspGetEventQueueId` retrieves the ID of an event queue.

#### Syntax

```cpp
HRESULT
WINAPI
EspGetEventQueueId(
    _In_ ESP_EVENT_QUEUE Queue,
    _Out_ GUID* QueueId
    );
```

#### Parameters

##### `Queue`

Specifies the event queue.

##### `QueueId`

Receives the event queue's ID.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspClearEventQueue

The API `EspClearEventQueue` clears all pending event notifications from an event queue. Note that this API clears all notifications that haven't been dequeued. If a notification has already been posted to the event queue's IOCP port, it is considered dequeued, and therefore will not be cleared.

#### Syntax

```cpp
HRESULT
WINAPI
EspClearEventQueue(
    _In_ ESP_EVENT_QUEUE Queue
    );
```

#### Parameters

##### `Queue`

Supplies the event queue to clear.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspEnumerateEventQueueIds

The API `EspEnumerateEventQueueIds` enumerates event queue IDs associated with the client. Clients might use this API when their service comes up to connect to each of their persisted event queues such that they can process notifications for their persisted rules.

#### Syntax

```cpp
HRESULT
WINAPI
EspEnumerateEventQueueIds(
    _In_ ESP_CLIENT Client,
    _In_ ESP_EVENT_QUEUE_LIFETIME Lifetime,
    _Out_ UINT32* EventQueueIdsCount,
    _Outptr_result_buffer_all_(*EventQueueIdsCount) GUID** EventQueueIds
    );
```

#### Parameters

##### `Client`

Specifies the client.

##### `Lifetime`

Specifies the lifetime to enumerate.

##### `EventQueueIdsCount`

Receives the number of elements in the "EventQueueIds" array.

##### `EventQueueIds`

Receives an array of event queue IDs. This array must be freed by calling `EspFreeMemory` once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_CLIENT`](wesp-clients.md#esp_client)
- [`ESP_EVENT_QUEUE_LIFETIME`](wesp-event-queue-management.md#esp_event_queue_lifetime)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

## Queue handle and types

### ESP_EVENT_QUEUE

Identifies a WESP event queue.

#### Syntax

```cpp
DECLARE_HANDLE(ESP_EVENT_QUEUE);
```

#### Remarks

Obtain this handle with `EspCreateEventQueue`. Release it with `EspCloseEventQueue`.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_QUEUE_TYPE

The enum `ESP_EVENT_QUEUE_TYPE` defines an event queue type.

#### Syntax

```cpp
typedef enum ESP_EVENT_QUEUE_TYPE
{
    ESP_EVENT_QUEUE_TYPE_NONE = 0,
    ESP_EVENT_QUEUE_TYPE_ASYNC
} ESP_EVENT_QUEUE_TYPE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_QUEUE_TYPE_ASYNC` | An event queue that receives asynchronous event notifications. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_QUEUE_LIFETIME

The enum `ESP_RULE_LIFETIME` specifies the lifetime for an event queue.

#### Syntax

```cpp
typedef enum ESP_EVENT_QUEUE_LIFETIME
{
    ESP_EVENT_QUEUE_LIFETIME_NONE = 0,
    ESP_EVENT_QUEUE_LIFETIME_CLIENT_SESSION,
    ESP_EVENT_QUEUE_LIFETIME_BOOT_SESSION,
    ESP_EVENT_QUEUE_LIFETIME_PERSISTED
} ESP_EVENT_QUEUE_LIFETIME;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_QUEUE_LIFETIME_CLIENT_SESSION` | The event queue's lifetime is tied to the client's session. If the client disconnects, the event queue is destroyed. |
| `ESP_EVENT_QUEUE_LIFETIME_BOOT_SESSION` | The event queue's lifetime is tied to the current boot session. The event queue is deleted when the machine reboots. |
| `ESP_EVENT_QUEUE_LIFETIME_PERSISTED` | The event queue's lifetime is persisted across boot sessions. If a rule is persisted, it can be associated with a persisted event queue. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_RULE_LIFETIME`](wesp-rule-management.md#esp_rule_lifetime)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_QUEUE_DESCRIPTOR

The structure `ESP_EVENT_QUEUE_DESCRIPTOR` is used to configure an event queue as part of calling the API `EspCreateEventQueue`.

#### Syntax

```cpp
typedef struct ESP_EVENT_QUEUE_DESCRIPTOR
{
    GUID QueueId;
    ESP_EVENT_QUEUE_TYPE QueueType;
    ESP_EVENT_QUEUE_LIFETIME Lifetime;
    UINT32 MaxCapacityBytes;
    ESP_EVENT_NOTIFICATION_VERSION NotificationVersion;
} ESP_EVENT_QUEUE_DESCRIPTOR;
```

#### Members

| FIELD | DESCRIPTION |
| --- | --- |
| QueueId | The "QueueId" is used to uniquely identify the event queue. Each event queue has a unique id. The client can pass a zeroed GUID to indicate that a random event queue id should be generated. |
| QueueType | Specifies the queue type. Currently, the only supported value is `ESP_EVENT_QUEUE_TYPE_ASYNC`. |
| Lifetime | Specifies the event queue's lifetime. The following lifetimes are supported:<br>Client Session: The event queue's lifetime is tied to the client's lifetime. If the client disconnects, the event queue is destroyed.<br>Persisted: The event queue is persisted across boot sessions. Clients can re-connect to their persisted event queue by using the same queue id. |
| MaxCapacityBytes | Specifies the maximum amount of memory in bytes that the event queue can use to store notifications. If the event queue runs out of memory, incoming notifications will be dropped. If the caller supplies 0, this field will be defaulted by the API. |
| NotificationVersion | Specifies the version to use for notifications received by this event queue. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_NOTIFICATION_VERSION`](wesp-event-notifications.md#esp_event_notification_version)
- [`ESP_EVENT_QUEUE_LIFETIME`](wesp-event-queue-management.md#esp_event_queue_lifetime)
- [`ESP_EVENT_QUEUE_TYPE`](wesp-event-queue-management.md#esp_event_queue_type)
- [`EspCreateEventQueue`](wesp-event-queue-management.md#espcreateeventqueue)
- [Windows endpoint security platform API reference](wesp-api-reference.md)
