---
title: "WESP event queue connections and callbacks"
description: "Windows endpoint security platform API reference for event queue connections and callbacks, including declarations and requirements."
author: GrantMeStrength
ms.author: jken
ms.topic: reference
ms.date: 11/03/2026
api_name:
- EspConnectEventQueueWithCallback
- EspConnectEventQueueWithIocp
- EspDisconnectEventQueue
- ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK
- ESP_IOCP_COMPLETION_KEY
- EspSetEventQueueStateChangeCallback
- EspRemoveEventQueueStateChangeCallback
- ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK
- ESP_EVENT_QUEUE_STATE
---

# Event queue connections and callbacks

This page contains reference entries in the [Event queues API family](wesp-api-reference.md#event-queues). Each entry includes its declaration and requirements.

## Connections

### EspConnectEventQueueWithCallback

The API `EspConnectEventQueueWithCallback` connects an event queue with a callback.

#### Syntax

```cpp
HRESULT
WINAPI
EspConnectEventQueueWithCallback(
    _In_ ESP_EVENT_QUEUE Queue,
    _In_ UINT32 MaxWorkerThreadCount,
    _In_ ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK Callback,
    _In_opt_ void* CallbackContext
    );
```

#### Parameters

##### `Queue`

Specifies the queue to connect.

##### `MaxWorkerThreadCount`

Specifies the maximum number of threads that should be used by the event queue to process notifications. If the caller supplies 0, the queue will default to the number of cores on the system. When a notification is dequeued from an event queue, WESP prepares the notification for delivery on a worker thread before invoking the event queue's callback.

##### `Callback`

Supplies a pointer to the callback function.<br>The callback is invoked by a worker thread in the order of events in the queue. The number of worker threads that can invoke the callback is bounded by "MaxWorkerThreadCount". So, it can be called on multiple threads at the same time for different events. If clients require events to be processed serially, "MaxWorkerThreadCount" should be set to 1 to ensure that a single callback is invoked at a time.

##### `CallbackContext`

An optional context which is passed as a parameter to the callback.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_INVALID_STATE` | The event queue is already connected. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [`ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK`](wesp-event-queue-delivery.md#esp_event_queue_notification_callback)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspConnectEventQueueWithIocp

Connects a WESP event queue to an I/O completion port.

#### Syntax

```cpp
HRESULT
WINAPI
EspConnectEventQueueWithIocp(
    _In_ ESP_EVENT_QUEUE Queue,
    _In_ UINT32 MaxWorkerThreadCount,
    _Out_ HANDLE* IocpHandle
    );
```

#### Parameters

##### `Queue`

Specifies the queue to connect.

##### `MaxWorkerThreadCount`

Specifies the maximum number of threads that should be used by the event queue to process notifications. If the caller supplies 0, the queue will default to the number of cores on the system. When a notification is dequeued from an event queue, WESP prepares the notification for delivery on a worker thread before posting it to the IOCP.<br>Notifications are posted to the event queues IOCP in the order of events in the queue.

##### `IocpHandle`

Receives the IOCP. The client must close this handle by calling CloseHandle once it is no longer needed.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_INVALID_STATE` | The event queue is already connected. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspDisconnectEventQueue

The API `EspDisconnectEventQueue` disconnects an event queue. After an event queue is disconnected, rules that reference the queue continue to be evaluated, but notifications are buffered in the driver until the queue is reconnected. Clients can reconnect to the event queue by calling `EspConnectEventQueueWithCallback` or `EspConnectEventQueueWithIocp`. Once reconnected, all notifications that were buffered while the queue was disconnected are delivered to the queue.

When an event queue is disconnected, it synchronizes teardown as follows:

#### Syntax

```cpp
HRESULT
WINAPI
EspDisconnectEventQueue(
    _In_ ESP_EVENT_QUEUE Queue
    );
```

#### Parameters

##### `Queue`

Supplies the event queue to disconnect.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

Documented error conditions include:

| RETURN VALUE | DESCRIPTION |
| --- | --- |
| `ERROR_INVALID_STATE` | The event queue is already disconnected. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [`EspConnectEventQueueWithCallback`](wesp-event-queue-delivery.md#espconnecteventqueuewithcallback)
- [`EspConnectEventQueueWithIocp`](wesp-event-queue-delivery.md#espconnecteventqueuewithiocp)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK

The callback function type `ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK` defines the function signature for an even queue notification callback.

#### Syntax

```cpp
typedef
void
(CALLBACK *ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK)(
    _Inout_ ESP_EVENT_NOTIFICATION* Notification,
    _In_opt_ void* Context
    );
```

#### Parameters

##### `Notification`

Supplies the notification. Once the client has finished processing the notification, the notification should be completed by calling `EspCompleteEventNotification`, and then re-armed by calling `EspArmEventNotification`.

##### `Context`

Supplies the context that was initially supplied in the event queue properties when the event queue was created.

#### Return value

None.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_NOTIFICATION`](wesp-event-notifications.md#esp_event_notification)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_IOCP_COMPLETION_KEY

The enum `ESP_IOCP_COMPLETION_KEY` defines an IOCP completion key.

#### Syntax

```cpp
typedef enum ESP_IOCP_COMPLETION_KEY
{
    ESP_IOCP_COMPLETION_KEY_NOTIFICATION = 0,
    ESP_IOCP_COMPLETION_KEY_TEARDOWN
} ESP_IOCP_COMPLETION_KEY;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_IOCP_COMPLETION_KEY_NOTIFICATION` | The dequeued completion packet contains an event notification. The overlapped pointer received from GetQueuedCompletionStatus can be cast to a `ESP_EVENT_NOTIFICATION` pointer. |
| `ESP_IOCP_COMPLETION_KEY_TEARDOWN` | The event queue is in the process of being disconnected. The client should exit each of its IOCP worker threads. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)

## State change notifications

### EspSetEventQueueStateChangeCallback

The API `EspSetEventQueueStateChangeCallback` configures a state change callback for the event queue. This API can be used by clients to receive notifications when the event queue is full or reaches a certain memory threshold.

#### Syntax

```cpp
HRESULT
WINAPI
EspSetEventQueueStateChangeCallback(
    _In_ ESP_EVENT_QUEUE Queue,
    _In_ ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK Callback,
    _In_opt_ void* Context,
    _In_ UINT8 MemoryThresholdPercent,
    _In_ UINT8 RecoveryThresholdPercent
    );
```

#### Parameters

##### `Queue`

Specifies the event queue for which to set the state change callback.

##### `Callback`

Specifies a callback function that will receive state change notifications.

##### `Context`

Optionally specifies a context that is supplied to the callback function.

##### `MemoryThresholdPercent`

Specifies the event queue memory usage percentage at which a "memory threshold exceeded" notification is sent. This field can be set to 0 if the client doesn't wish to receive "memory threshold exceeded" notifications.

##### `RecoveryThresholdPercent`

Specifies the event queue memory usage percentage at which a "recovery threshold exceeded" notification is sent. This field must be less than MemoryThresholdPercent. A "recovery threshold exceeded" notification is sent when an event queue's memory usage has exceeded the memory threshold percent, and recovered down to the recover threshold percent.<br>This field can be set to 0 if the client doesn't wish to receive "recovery threshold exceeded" notifications.

#### Return value

Returns an `HRESULT` that indicates the result of the operation. Use `SUCCEEDED` or `FAILED` to test the result.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `espclient.h` |
| DLL | `espclient.dll` |

#### See also

- [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue)
- [`ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK`](wesp-event-queue-delivery.md#esp_event_queue_state_change_callback)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### EspRemoveEventQueueStateChangeCallback

The API `EspRemoveEventQueueStateChangeCallback` removes the state change callback from the event queue.

#### Syntax

```cpp
HRESULT
WINAPI
EspRemoveEventQueueStateChangeCallback(
    _In_ ESP_EVENT_QUEUE Queue
    );
```

#### Parameters

##### `Queue`

Specifies the event queue for which to remove the state change callback.

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

### ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK

The callback function type `ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK` defines the function signature for an event queue state change callback.

#### Syntax

```cpp
typedef
void
(CALLBACK *ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK)(
    _In_ ESP_EVENT_QUEUE_STATE State,
    _In_opt_ void* Data,
    _In_opt_ void* Context
    );
```

#### Parameters

##### `State`

Supplies the event queue state. The currently supported states are:<br>Queue Full: Indicates that the event queue has reached maximum capacity. This can happen if the client isn't dequeuing notifications fast enough.<br>Memory Threshold Exceeded: The specified MemoryThresholdPercent in the event queue's state change options has been exceeded.<br>Recovered: The specified RecoveryThresholdPercent in the event queue's state change options has been reached. This notification only fires if a previous "memory threshold percent" notification fired.

##### `Data`

Supplies data associated with the state change. This parameter is currently unused.

##### `Context`

The context supplied when registering the callback with `EspSetEventQueueStateChangeCallback`.

#### Return value

None.

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [`ESP_EVENT_QUEUE_STATE`](wesp-event-queue-delivery.md#esp_event_queue_state)
- [Windows endpoint security platform API reference](wesp-api-reference.md)

### ESP_EVENT_QUEUE_STATE

The enum `ESP_EVENT_QUEUE_STATE` defines an event queue's state.

#### Syntax

```cpp
typedef enum ESP_EVENT_QUEUE_STATE
{
    ESP_EVENT_QUEUE_STATE_NONE = 0,
    ESP_EVENT_QUEUE_STATE_FULL,
    ESP_EVENT_QUEUE_STATE_MEMORY_THRESHOLD_EXCEEDED,
    ESP_EVENT_QUEUE_STATE_RECOVERED
} ESP_EVENT_QUEUE_STATE;
```

#### Values

| VALUE | DESCRIPTION |
| --- | --- |
| `ESP_EVENT_QUEUE_STATE_FULL` | The event queue has reached maximum memory capacity. All new notifications will be dropped. |
| `ESP_EVENT_QUEUE_STATE_MEMORY_THRESHOLD_EXCEEDED` | The event queue has exceeded the memory threshold percent. |
| `ESP_EVENT_QUEUE_STATE_RECOVERED` | The event queue's memory usage has recovered to the recovery threshold percent. |

#### Requirements

| Requirement | Value |
| --- | --- |
| Header | `esptypes.h` |

#### See also

- [Windows endpoint security platform API reference](wesp-api-reference.md)
