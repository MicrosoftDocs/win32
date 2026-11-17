---
title: Windows endpoint security platform (WESP) API overview (preview)
description: Learn how the preview Windows endpoint security platform (WESP) models events, rules, filters, notifications, properties, and context
author: GrantMeStrength
ms.author: jken
ms.topic: overview
ms.date: 11/16/2026
---

# Windows endpoint security platform (WESP) API overview (preview)

> [!IMPORTANT]
> **PREVIEW**: The Windows endpoint security platform and the APIs described in this article are in preview. The API surface, supported events, properties, and behavior can change. This article is a conceptual overview, not API reference documentation. Verify declarations and availability for your target Windows build.

The Windows endpoint security platform is a Win32 user-mode framework for security products. It is available in preview starting with the October 2026 (10D) Windows 11 client releases: version 25H2 (OS build 26200.9818) and version 26H2 (OS build 26300.9818). The platform uses a shared OS-provided driver to observe system activity and deliver events to user-mode clients. Clients define rules to observe or affect supported events without each product implementing its own kernel-mode monitoring driver.

This article describes the event model, client lifecycle, property and context APIs, filters, collections, rules, and event queues. Use the headers and materials provided for your Windows build to verify exact declarations and availability.

## Register and connect a client

A WESP product is a program or service that uses the platform. A product can register one or more client IDs. Registration persists across connections; each client ID can have only one active connection at a time. Each connection is represented by an opaque `ESP_CLIENT` handle, which the product passes to APIs that require a connected client.

The client library is `espclient.dll`; the platform driver is `wesp.sys`.

| API | Purpose |
| --- | --- |
| `EspRegisterClient` | Registers a client descriptor. The client ID and altitude must be unique. |
| `EspUnregisterClient` | Removes a registration and its persisted client state. Disconnect the client first. |
| `EspConnectClient` | Connects a registered client and returns an `ESP_CLIENT` handle. |
| `EspDisconnectClient` | Disconnects the handle and releases client-associated memory. Process termination also disconnects the client. |
| `EspQueryClientDescriptor` | Retrieves a descriptor for a registered or connected client. The returned allocation is released with `EspFreeMemory`. |
| `EspEnumerateRegisteredClients` | Lists registered client IDs. Free the returned array with `EspFreeMemory`. |
| `EspEnumerateConnectedClients` | Lists connected client IDs. Free the returned array with `EspFreeMemory`. |
| `EspGetEventCapabilities` | Reports the current client's supported capabilities for an event type. |

`EspRegisterClient` and `EspUnregisterClient` are installation and uninstallation operations, respectively. Don't register a client each time its service starts. A product can use multiple client IDs, but each ID supports only one active connection at a time. Close the active connection with `EspDisconnectClient` when the service no longer needs it.

`EspFreeMemory` releases buffers allocated by WESP APIs. `EspInitUnicodeString` initializes an `ESP_UNICODE_STRING` from a null-terminated string, and `ESP_CONSTANT_UNICODE_STRING` initializes one from a constant string.

Registration fails if the client ID or altitude is already registered.

## Event capabilities

Call `EspGetEventCapabilities` to obtain the supported capabilities for a specific event and client. Some event types aren't supported on earlier Windows releases, and some events don't support every capability, such as blocking or allowing an operation.

A client's capabilities depend on its enhanced key usage (EKU) being present in the appropriate WESP Code Integrity policy. Future platform updates will provide distinct subsets of capabilities to different client types.

## Events

WESP represents monitored system activity with `ESP_EVENT_TYPE` values. The preview specification describes these event categories:

| Category | Event types |
| --- | --- |
| Thread | `ESP_EVENT_TYPE_THREAD_CREATE`, `ESP_EVENT_TYPE_THREAD_START`, `ESP_EVENT_TYPE_THREAD_TERMINATE` |
| Process | `ESP_EVENT_TYPE_PROCESS_CREATE`, `ESP_EVENT_TYPE_PROCESS_TERMINATE`, `ESP_EVENT_TYPE_PROCESS_LOAD_IMAGE` |
| File object | `ESP_EVENT_TYPE_FO_CREATE`, `ESP_EVENT_TYPE_FO_OPEN`, `ESP_EVENT_TYPE_FO_READ`, `ESP_EVENT_TYPE_FO_WRITE`, `ESP_EVENT_TYPE_FO_CLEANUP` |
| File system | `ESP_EVENT_TYPE_FS_CREATE_FILE_SECTION`, `ESP_EVENT_TYPE_FS_QUERY_FILE_INFORMATION`, `ESP_EVENT_TYPE_FS_SET_FILE_INFORMATION`, `ESP_EVENT_TYPE_FS_SET_FILE_SECURITY`, `ESP_EVENT_TYPE_FS_QUERY_DIRECTORY_INFORMATION`, `ESP_EVENT_TYPE_FS_FSCTL_FILE`, `ESP_EVENT_TYPE_FS_SET_EA`, `ESP_EVENT_TYPE_FS_QUERY_OPEN_FILE`, `ESP_EVENT_TYPE_FS_LOCK_FILE`, `ESP_EVENT_TYPE_FS_UNLOCK_FILE` |
| KTM transaction | `ESP_EVENT_TYPE_KTM_TRANSACTION_COMMIT`, `ESP_EVENT_TYPE_KTM_TRANSACTION_ROLLBACK` |
| Volume | `ESP_EVENT_TYPE_VOLUME_MOUNT`, `ESP_EVENT_TYPE_VOLUME_DISMOUNT`, `ESP_EVENT_TYPE_VOLUME_FSCTL` |
| Named pipe | `ESP_EVENT_TYPE_PIPE_CREATE` |
| Mailslot | `ESP_EVENT_TYPE_MAILSLOT_CREATE` |
| Registry | `ESP_EVENT_TYPE_REG_CREATE_KEY`, `ESP_EVENT_TYPE_REG_OPEN_KEY`, `ESP_EVENT_TYPE_REG_DELETE_KEY`, `ESP_EVENT_TYPE_REG_SET_VALUE_KEY`, `ESP_EVENT_TYPE_REG_DELETE_VALUE_KEY`, `ESP_EVENT_TYPE_REG_RENAME_KEY`, `ESP_EVENT_TYPE_REG_REPLACE_KEY`, `ESP_EVENT_TYPE_REG_RESTORE_KEY`, `ESP_EVENT_TYPE_REG_SET_KEY_SECURITY`, `ESP_EVENT_TYPE_REG_QUERY_KEY`, `ESP_EVENT_TYPE_REG_QUERY_VALUE_KEY`, `ESP_EVENT_TYPE_REG_SAVE_KEY`, `ESP_EVENT_TYPE_REG_LOAD_KEY`, `ESP_EVENT_TYPE_REG_ENUM_KEY`, `ESP_EVENT_TYPE_REG_ENUM_VALUE_KEY` |
| Object manager | `ESP_EVENT_TYPE_OB_CREATE_HANDLE`, `ESP_EVENT_TYPE_OB_DUPLICATE_HANDLE` |
| Boot | `ESP_EVENT_TYPE_BOOT_LOAD_DRIVER` |

Not every event supports every rule action or completion notification. Check event capabilities and the event-specific configuration before depending on a behavior.

## Event objects, properties, and references

An event can refer to several WESP event objects, such as the current process and thread, a target file, or a registry key. `ESP_EVENT_OBJECT` is an opaque handle to one such object. The platform supports these object types:

| Object | Represents |
| --- | --- |
| Thread and process | A thread or process instance. |
| File stream and file | A physical stream on a volume, or a persistent on-disk file that exists independently of open handles. |
| File object | A single open instance. Multiple file objects can refer to the same file, and a file object can target a file stream, volume, pipe, or mailslot. |
| Volume and disk | A physical volume or disk. |
| Registry key and registry key object | A persistent key, or an open handle to a key. |
| Desktop, KTM transaction, pipe, and mailslot | The corresponding system object or instance. |
| Token | A token instance. |

Call `EspGetEventObjectId` to retrieve an object's ID and `EspGetEventObjectType` to retrieve its type. An event object's ID is unique during a boot session, remains constant for that WESP event object's lifetime, and is consistent across clients.

### Understand event object lifetimes

An `ESP_EVENT_OBJECT` received in a notification is a non-owning handle. WESP keeps the event objects and their IDs valid until the client completes that notification with `EspCompleteEventNotification`. The underlying kernel object or entity might no longer exist by the time an asynchronous notification is processed, so a later property query can fail.

WESP can destroy and recreate an event object while its underlying entity remains alive. The recreated object isn't guaranteed to have the same ID. A strong reference acquired with `EspCreateEventObjectReference` keeps the event object and its context alive, but doesn't keep the underlying kernel object alive. Setting a context key also retains the event object while its backing entity exists; WESP releases that implicit reference when the entity is destroyed. These references let clients stabilize object identity across events without extending the backing entity's lifetime.

### Query properties

Property-query APIs return an array of `ESP_PROPERTY` values in the order of the requested property IDs. Use the matching `EspGetProperty*` helper to extract a typed value. A property can instead contain an error when the driver couldn't retrieve it, for example if its backing object no longer exists. Release returned allocations with `EspFreeMemory`.

| Object or scope | Query API | Support check |
| --- | --- | --- |
| Client | `EspQueryClientProperties` | `EspIsClientPropertySupported` |
| Event | Properties can be requested in event rule configuration. | `EspIsEventPropertySupported` |
| Thread | `EspQueryThreadProperties` | `EspIsThreadPropertySupported` |
| Process | `EspQueryProcessProperties` | `EspIsProcessPropertySupported` |
| File stream | `EspQueryFileStreamProperties` | `EspIsFileStreamPropertySupported` |
| File | `EspQueryFileProperties` | `EspIsFilePropertySupported` |
| File object | `EspQueryFileObjectProperties` | `EspIsFileObjectPropertySupported` |
| Volume | `EspQueryVolumeProperties` | `EspIsVolumePropertySupported` |
| Disk | `EspQueryDiskProperties` | `EspIsDiskPropertySupported` |
| Registry key | `EspQueryRegistryKeyProperties` | `EspIsRegistryKeyPropertySupported` |
| Registry key object | `EspQueryRegistryKeyObjectProperties` | `EspIsRegistryKeyObjectPropertySupported` |
| Desktop | `EspQueryDesktopProperties` | `EspIsDesktopPropertySupported` |
| KTM transaction | `EspQueryKtmTransactionProperties` | `EspIsKtmTransactionPropertySupported` |
| Pipe | `EspQueryPipeProperties` | `EspIsPipePropertySupported` |
| Mailslot | `EspQueryMailslotProperties` | `EspIsMailslotPropertySupported` |
| Token | `EspQueryTokenProperties` | `EspIsTokenPropertySupported` |

The `EspGetProperty*` helper family includes `EspGetPropertyError`, `EspGetPropertyContextKeyInfo`, `EspGetPropertyBool`, `EspGetPropertyUint8`, `EspGetPropertyUint16`, `EspGetPropertyUint32`, `EspGetPropertyUint64`, `EspGetPropertyInt32`, `EspGetPropertyUnicodeString`, `EspGetPropertyNtStatus`, `EspGetPropertyFileTime`, `EspGetPropertyMemoryAddressBasic`, `EspGetPropertyFileId128`, `EspGetPropertyUsn`, `EspGetPropertySigningLevel`, `EspGetPropertyEaList`, `EspGetPropertySecurityDescriptor`, `EspGetPropertyBuffer`, `EspGetPropertyStringList`, `EspGetPropertyGuid`, `EspGetPropertyAcl`, `EspGetPropertySid`, `EspGetPropertyImpersonationLevel`, `EspGetPropertyTokenPrivileges`, `EspGetPropertyTokenGroups`, `EspGetPropertyTokenType`, `EspGetPropertyTokenElevationType`, `EspGetPropertyTransactionOutcome`, `EspGetPropertyTransactionState`, `EspGetPropertyStorageBusType`, `EspGetPropertyDeviceType`, `EspGetPropertySubsystemInformationType`, and `EspGetPropertyFoTargetObjectType`. Each helper checks the property's variant type and returns an error if it doesn't match.

When a notification must contain data that might no longer be queryable later, request the property in the rule configuration. WESP captures configured properties at event time and includes them with the notification. A property can report an HRESULT error if the driver couldn't retrieve its value.

### Retain event objects

WESP provides general reference APIs and typed creation APIs:

| API group | APIs |
| --- | --- |
| General references | `EspCreateEventObjectReference`, `EspCreateEventObjectReferenceById`, `EspDuplicateEventObjectReference`, `EspCloseEventObjectReference`, `EspGetEventObjectFromReference` |
| Thread and process | `EspCreateThreadReference`, `EspCreateProcessReference` |
| File stream and file | `EspCreateFileStreamReferenceById`, `EspCreateFileStreamReferenceByPath`, `EspCreateFileReferenceById`, `EspCreateFileReferenceByPath` |
| Other objects | `EspCreateVolumeReference`, `EspCreateDiskReference`, `EspCreateRegistryKeyReference`, `EspCreateDesktopReference`, `EspCreatePipeReference`, `EspCreateMailslotReference`, `EspCreateThreadTokenReference`, `EspCreateProcessTokenReference` |

Use an explicit reference when you need to query an event object or update its context after completing the notification that supplied it. A strong reference keeps the WESP event object and its context alive, but doesn't keep the underlying kernel object or entity alive. WESP closes explicit references when the client disconnects or its process terminates; call `EspCloseEventObjectReference` when a reference is no longer needed.

## Context keys

Context keys let a client associate client-private state with an event object, an event, or the client itself. A key is a `UINT32` with at most 31 bits; its value is an integer, Unicode string, or buffer. Each client has an independent context-key namespace.

| API | Purpose |
| --- | --- |
| `EspSetEventObjectContextKey` | Adds, changes, or removes a key on an event object. |
| `EspEnumerateAllEventObjectContextKeys` | Lists keys on an event object. Free the returned array with `EspFreeMemory`. |
| `EspSetClientContextKey` | Adds, changes, or removes a key on a client. |
| `EspEnumerateAllClientContextKeys` | Lists keys on a client. Free the returned array with `EspFreeMemory`. |

The `ESP_*_PROPERTY_ID_CONTEXT_KEY(key)` macros expose context keys through the typed property system. WESP defines macros for event, client, thread, process, file stream, file, file object, volume, disk, registry key, registry key object, desktop, KTM transaction, pipe, mailslot, and token properties. The macro sets the high bit in the property ID; keep the supplied key within the 31-bit range.

Rules can update context keys automatically, cache properties or event parameters in a key, and use key values in filters. Context updates are atomic for an individual client, event, or event object, but a group of updates targeting different objects isn't guaranteed to be atomic as a whole.

Setting a context key on an event object implicitly keeps that event object alive while its backing kernel object or entity exists. When the backing object is destroyed, WESP releases this reference, so context keys don't keep event objects alive indefinitely.

## Filters and collections

Filters test event, client, or event-object values. Typed filter APIs use property IDs for the corresponding object type; `EspCreateFilter` creates a non-typed filter for event parameters that don't have a property ID.

| Filter scope | Creation API |
| --- | --- |
| Non-typed comparison | `EspCreateFilter` |
| Event and client | `EspCreateEventFilter`, `EspCreateClientFilter` |
| Thread and process | `EspCreateThreadFilter`, `EspCreateProcessFilter` |
| File stream, file, and file object | `EspCreateFileStreamFilter`, `EspCreateFileFilter`, `EspCreateFileObjectFilter` |
| Volume and disk | `EspCreateVolumeFilter`, `EspCreateDiskFilter` |
| Registry key and registry key object | `EspCreateRegistryKeyFilter`, `EspCreateRegistryKeyObjectFilter` |
| Desktop and KTM transaction | `EspCreateDesktopFilter`, `EspCreateKtmTransactionFilter` |
| Pipe, mailslot, and token | `EspCreatePipeFilter`, `EspCreateMailslotFilter`, `EspCreateTokenFilter` |

Use `EspCreateAndFilter`, `EspCreateOrFilter`, `EspCreateXorFilter`, and `EspCreateNotFilter` to compose filters. `EspCloseFilter` releases a filter reference. Typed filters can only be combined with filters for the same object type. Non-typed filters can only be combined with non-typed filters that use the same comparison type.

The comparison structures support integer, Boolean, string, binary, context-key, and other WESP-defined comparison types. A comparison can use a raw value, a binding key, or a collection where supported. If WESP can't evaluate a filter or the data doesn't apply to that event, the filter doesn't match.

`EspStringMatchesPattern` accepts `ESP_UNICODE_STRING` values for a string and pattern and returns whether they match.

Collections provide reusable sets of integer, string, or variable-size binary values for filters. They are private to a client and are reference-counted. A persisted rule can reference only persisted collections; WESP deletes a persisted collection when no rules reference it.

| API | Purpose |
| --- | --- |
| `EspCreateCollection`, `EspOpenCollection` | Create a collection or open one by ID. |
| `EspCloseCollection` | Release a collection reference. |
| `EspGetCollectionId`, `EspGetCollectionType` | Retrieve collection identity and type. |
| `EspUpdateCollection` | Add or remove entries in an atomic update; affected filters see the update immediately. |
| `EspEnumerateCollectionEntries` | Retrieve collection entries; free the returned allocation with `EspFreeMemory`. |
| `EspEnumerateCollectionIds` | Enumerate a client's collection IDs for a specified lifetime. |

## Rules and rule configuration

A rule describes an event type, filters, configuration, lifetime, and action. `EspCreateRule` creates a rule object but doesn't activate it. Call `EspUpdateRules` to add it to a client.

| API | Purpose |
| --- | --- |
| `EspCreateRule`, `EspCloseRule`, `EspGetRuleId` | Create, release, and retrieve the ID of a rule. Closing a local rule reference doesn't remove the rule from WESP. |
| `EspUpdateRules` | Atomically add, add or replace, enable, disable, or remove rules in the supplied order. |
| `EspRemoveAllRulesForClient` | Remove all rules for a client. |
| `EspRemoveRulesForClient` | Remove rules with a specified lifetime. |
| `EspEnumerateAllRulesForClient`, `EspEnumerateRuleIds` | Enumerate rule IDs; free returned arrays with `EspFreeMemory`. |

Rule lifetimes have different retention and startup behavior:

| Lifetime | Behavior and limits |
| --- | --- |
| `ESP_RULE_LIFETIME_CLIENT_SESSION` | The rule is removed when the client disconnects. |
| `ESP_RULE_LIFETIME_BOOT_SESSION` | The rule remains for the current boot session and is deleted when the computer restarts. |
| `ESP_RULE_LIFETIME_PERSISTED` | The rule persists across restarts and continues to apply while the client is disconnected. It can only use a persisted event queue. |
| `ESP_RULE_LIFETIME_PERSISTED_EARLY_BOOT` | The rule persists across restarts and is also applied during the Early Launch Anti-Malware (ELAM) phase of early boot. This lifetime is limited to registry events and boot-driver-load events, can't reference filesystem-related objects in its configuration, and requires a persisted event queue. The rule continues to apply after the ELAM phase. |

The rule actions define how WESP handles a match:

| Action | Behavior |
| --- | --- |
| `ESP_RULE_ACTION_NOTIFY` | Sends an asynchronous notification when the rule matches. |
| `ESP_RULE_ACTION_NOTIFY_ON_COMPLETION` | Sends a notification when a supported event completes. A matching pre-operation rule must opt in with `ESP_RULE_FLAGS_NOTIFY_ON_COMPLETION`; not every event supports this action. |
| `ESP_RULE_ACTION_NO_NOTIFY` | Updates context keys or modifies event data without notifying the client, then ends rule evaluation for the client. |
| `ESP_RULE_ACTION_IGNORE` | Ignores the event to stop rule processing early, for example for events originating from the client's own process. |
| `ESP_RULE_ACTION_BLOCK` | Blocks the event, if the client has the capability and the event supports blocking. A block ends evaluation for that event. |
| `ESP_RULE_ACTION_ALLOW` | Explicitly allows an event for a limited set of event types; another client can still block it. |
| `ESP_RULE_ACTION_MATCH_SUBRULES` | Evaluates the rule's subrules after the parent rule matches. |
| `ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_RULE` | Continues to the next top-level rule for the client. |
| `ESP_RULE_ACTION_CONTINUE_MATCHING_NEXT_SUBRULE` | Continues to the next subrule; this action is valid only on a subrule. |

Rule evaluation proceeds by client altitude, with higher altitudes evaluated first. Within a client, top-level rules are evaluated by ascending `OrderGroup`; WESP doesn't guarantee order within one group. A matching rule normally ends evaluation for that client. Continue actions advance to another rule or subrule, and `MATCH_SUBRULES` evaluates the matching rule's subrules. A block ends evaluation for the event. Rules generally run before an operation. `NOTIFY_ON_COMPLETION` rules run after it, and an event can therefore produce both pre-operation and completion notifications when configured.

Each event type has an `ESP_*_CONFIG` structure that configures its event parameters and related event objects. Rule configuration can:

- Apply event, client, and nested object filters.
- Request event, client, or object properties to capture into notifications.
- Update event, client, or object context keys.
- Bind values from event parameters, properties, or context keys for comparisons elsewhere in the rule.
- Specify subrules and, for supported events, event modifications.

Binding keys are numeric identifiers scoped to a rule. A key resolves to an integer, string, or binary value during evaluation, allowing a filter to compare fields from different objects or event parameters.

Event modification is configured through `ESP_EVENT_MODIFY` and an event-specific modification structure. It can change supported event data before WESP builds a notification. Use only modifications supported for the event type and available to the client; don't assume that every observed operation can be modified.

## Event queues and notifications

An event queue receives notifications from rules that reference it. A client can connect a queue with a callback or an I/O completion port (IOCP). Callbacks can execute concurrently when the queue uses multiple worker threads. Use one worker thread when your callback processing requires serialization. Notifications have event IDs that help identify event order.

| API | Purpose |
| --- | --- |
| `EspCreateEventQueue`, `EspOpenEventQueue`, `EspCloseEventQueue` | Create, open, or release an event queue. |
| `EspGetEventQueueId` | Retrieve the queue ID. |
| `EspConnectEventQueueWithCallback` | Connect a queue using a callback. Multiple worker threads can invoke the callback concurrently; set the worker count to one when processing must be serialized. |
| `EspConnectEventQueueWithIocp` | Connect a queue to an IOCP and return its handle. Close the returned handle with `CloseHandle`. |
| `EspDisconnectEventQueue` | Disconnect a queue. Rules continue to be evaluated, and notifications are buffered until reconnection. |
| `EspClearEventQueue` | Clear notifications that haven't been dequeued. |
| `EspEnumerateEventQueueIds` | Enumerate queue IDs for a client and lifetime. |
| `EspSetEventQueueStateChangeCallback` | Receive notifications when queue memory usage crosses configured thresholds. |
| `EspRemoveEventQueueStateChangeCallback` | Remove a queue's state-change callback. |
| `EspAllocateEventNotification`, `EspArmEventNotification` | Allocate a notification object and arm it to receive events. |
| `EspCompleteEventNotification` | Complete a received notification. Its fields and structures are invalid after completion. |
| `EspFreeEventNotification` | Free an allocated notification after no queue is using it. |

An event queue remains alive while it has references, including references held by rules. Its `MaxCapacityBytes` setting limits memory used to buffer notifications; when the queue reaches its maximum capacity, WESP drops new notifications. A state-change callback can report that the queue is full, that a configured memory threshold was exceeded, or that usage recovered to its recovery threshold. Remove the callback with `EspRemoveEventQueueStateChangeCallback` when it is no longer needed.

Notifications are queued in event order, but multiple worker threads can cause callbacks or IOCP messages to be processed out of order. Use one worker thread when processing order must be preserved. Call `EspCompleteEventNotification` only after the client has finished using the notification's data; completion invalidates its fields and structures. Re-arm the notification to receive another event. Don't free an armed notification. Disconnect the queue before freeing its notification objects.

For persisted rules, notifications can be buffered while the client is disconnected. On connection, enumerate and reconnect the persisted event queue using the same queue ID. Check `ESP_EVENT_NOTIFICATION_FLAGS_DISCONNECTED` to identify notifications from activity while the client was disconnected.

## Related content

- [Security and identity in Win32](/windows/win32/security)
- [Download the Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk/)
