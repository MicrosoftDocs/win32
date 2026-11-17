---
title: Windows endpoint security platform API reference
description: This is a reference for APIs declared in headers for the Windows endpoint security platform
author: tomlavoy
ms.author: tlavoy
ms.topic: reference
ms.date: 11/03/2026
---

# Windows endpoint security platform API reference

The Windows endpoint security platform APIs are declared in `espclient.h` and `esptypes.h`.

Browse the reference by API family below, or use the [alphabetical API index](#alphabetical-api-index) to find a symbol by name. Related functions, callbacks, handles, enumerations, structures, unions, and macros are documented together. Each public symbol has one reference entry and belongs to one API family.

## Clients

| Topic | Entries |
| --- | --- |
| [Clients](wesp-clients.md) | 10 |

## Event capabilities

| Topic | Entries |
| --- | --- |
| [Event capabilities](wesp-event-capabilities.md) | 18 |

## Event queues

| Topic | Entries |
| --- | --- |
| [Event queue creation and management](wesp-event-queue-management.md) | 10 |
| [Event queue connections and callbacks](wesp-event-queue-delivery.md) | 9 |

## Event notifications

| Topic | Entries |
| --- | --- |
| [Event notifications](wesp-event-notifications.md) | 8 |

## Rules

| Topic | Entries |
| --- | --- |
| [Rule creation and management](wesp-rule-management.md) | 17 |
| [Rule configuration and property bindings](wesp-rule-configuration.md) | 6 |
| [Rule value configuration](wesp-rule-value-configuration.md) | 18 |
| [Rule event modification](wesp-rule-event-modification.md) | 4 |

## Filters

| Topic | Entries |
| --- | --- |
| [Filter creation and composition](wesp-filter-creation.md) | 23 |
| [Shared comparison types and context key comparison](wesp-filter-comparison-types.md) | 7 |
| [Boolean, integer, and binary comparisons](wesp-filter-scalar-comparisons.md) | 8 |
| [String, string list, and path comparisons](wesp-filter-string-comparisons.md) | 6 |
| [SID, token, and security descriptor comparisons](wesp-filter-security-comparisons.md) | 9 |
| [File, registry, network, and memory comparisons](wesp-filter-domain-comparisons.md) | 13 |

## Collections

| Topic | Entries |
| --- | --- |
| [Collection creation and management](wesp-collection-management.md) | 11 |
| [Collection updates](wesp-collection-updates.md) | 6 |

## Context keys

| Topic | Entries |
| --- | --- |
| [Context key management](wesp-context-key-management.md) | 11 |
| [Context key property ID macros](wesp-context-key-property-macros.md) | 16 |

## Events

| Topic | Entries |
| --- | --- |
| [Shared event types](wesp-event-shared-types.md) | 8 |
| [Thread events](wesp-thread-events.md) | 7 |
| [Process events](wesp-process-events.md) | 6 |
| [File object events](wesp-file-object-events.md) | 11 |
| [File system events](wesp-file-system-events.md) | 22 |
| [Transaction events](wesp-transaction-events.md) | 4 |
| [Volume events](wesp-volume-events.md) | 6 |
| [Pipe events](wesp-pipe-events.md) | 2 |
| [Mailslot events](wesp-mailslot-events.md) | 2 |
| [Registry events](wesp-registry-events.md) | 31 |
| [Object handle events](wesp-object-handle-events.md) | 6 |
| [Boot driver events](wesp-boot-driver-events.md) | 2 |

## Event objects

| Topic | Entries |
| --- | --- |
| [Shared event object APIs and types](wesp-event-object-references.md) | 12 |
| [Thread, process, and token event objects](wesp-execution-objects.md) | 13 |
| [File stream, file, and file object event objects](wesp-file-objects.md) | 15 |
| [Volume and disk event objects](wesp-storage-objects.md) | 8 |
| [Registry and other event objects](wesp-other-event-objects.md) | 22 |

## Property queries

| Topic | Entries |
| --- | --- |
| [Property query functions and shared types](wesp-property-queries.md) | 19 |
| [Event, client, thread, process, and token property IDs](wesp-execution-property-ids.md) | 5 |
| [File and storage property IDs](wesp-file-property-ids.md) | 5 |
| [Registry and other object property IDs](wesp-other-property-ids.md) | 6 |
| [Scalar, string, and buffer property accessors](wesp-scalar-property-accessors.md) | 13 |
| [Structured and domain-specific property accessors](wesp-domain-property-accessors.md) | 20 |

## Common

| Topic | Entries |
| --- | --- |
| [Common utilities, strings, and buffers](wesp-common-utilities.md) | 9 |
| [Common shared value types](wesp-common-value-types.md) | 10 |

## Alphabetical API index

### Functions and callbacks

| API | Description |
| --- | --- |
| [`ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK`](wesp-event-queue-delivery.md#esp_event_queue_notification_callback) | The callback function type `ESP_EVENT_QUEUE_NOTIFICATION_CALLBACK` defines the function signature for an even queue notification callback. |
| [`ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK`](wesp-event-queue-delivery.md#esp_event_queue_state_change_callback) | The callback function type `ESP_EVENT_QUEUE_STATE_CHANGE_CALLBACK` defines the function signature for an event queue state change callback. |
| [`EspAllocateEventNotification`](wesp-event-notifications.md#espallocateeventnotification) | The API `EspAllocateEventNotification` allocates an event notification. |
| [`EspArmEventNotification`](wesp-event-notifications.md#esparmeventnotification) | The API `EspArmEventNotification` arms an event notification for use with an event queue. |
| [`EspClearEventQueue`](wesp-event-queue-management.md#espcleareventqueue) | The API `EspClearEventQueue` clears all pending event notifications from an event queue. |
| [`EspCloseCollection`](wesp-collection-management.md#espclosecollection) | The API `EspCloseCollection` is used to close a reference to an `ESP_COLLECTION` object. |
| [`EspCloseEventObjectReference`](wesp-event-object-references.md#espcloseeventobjectreference) | The API `EspCloseEventObjectReference` is used to close an event object reference that was previously acquired by calling `EspCreateEventObjectReference`. |
| [`EspCloseEventQueue`](wesp-event-queue-management.md#espcloseeventqueue) | The API `EspCloseEventQueue` closes an event queue handle. |
| [`EspCloseFilter`](wesp-filter-creation.md#espclosefilter) | The API `EspCloseFilter` is used to close a reference to a `ESP_FILTER` object. |
| [`EspCloseRule`](wesp-rule-management.md#espcloserule) | The API `EspCloseRule` closes a client's local reference to the rule, and frees memory associated with this reference. |
| [`EspCompleteEventNotification`](wesp-event-notifications.md#espcompleteeventnotification) | The API `EspCompleteEventNotification` completes an event notification. |
| [`EspConnectClient`](wesp-clients.md#espconnectclient) | The API `EspConnectClient` is used to establish a connection with the WESP framework. |
| [`EspConnectEventQueueWithCallback`](wesp-event-queue-delivery.md#espconnecteventqueuewithcallback) | The API `EspConnectEventQueueWithCallback` connects an event queue with a callback. |
| [`EspConnectEventQueueWithIocp`](wesp-event-queue-delivery.md#espconnecteventqueuewithiocp) | Connects a WESP event queue to an I/O completion port. |
| [`EspCreateAndFilter`](wesp-filter-creation.md#espcreateandfilter) | The API `EspCreateAndFilter` is used to create a composite filter that represents the logical conjunction (AND) of two existing filters. |
| [`EspCreateClientFilter`](wesp-filter-creation.md#espcreateclientfilter) | The API `EspCreateClientFilter` is used to create a client filter. |
| [`EspCreateCollection`](wesp-collection-management.md#espcreatecollection) | The API `EspCreateCollection` is used to create a new collection for a client. |
| [`EspCreateDesktopFilter`](wesp-filter-creation.md#espcreatedesktopfilter) | The API `EspCreateDesktopFilter` is used to create a filter for a desktop event object. |
| [`EspCreateDesktopReference`](wesp-other-event-objects.md#espcreatedesktopreference) | The API `EspCreateDesktopReference` creates an event object reference to an existing desktop. |
| [`EspCreateDiskFilter`](wesp-filter-creation.md#espcreatediskfilter) | The API `EspCreateDiskFilter` is used to create a filter for a disk event object. |
| [`EspCreateDiskReference`](wesp-storage-objects.md#espcreatediskreference) | The API `EspCreateDiskReference` creates an event object reference to an existing disk. |
| [`EspCreateEventFilter`](wesp-filter-creation.md#espcreateeventfilter) | The API `EspCreateEventFilter` is used to create a filter for an event property. |
| [`EspCreateEventObjectReference`](wesp-event-object-references.md#espcreateeventobjectreference) | The API `EspCreateEventObjectReference` is used to create a reference to an event object. |
| [`EspCreateEventObjectReferenceById`](wesp-event-object-references.md#espcreateeventobjectreferencebyid) | The API `EspCreateEventObjectReference` is used to create a reference to an event object using its event object ID. |
| [`EspCreateEventQueue`](wesp-event-queue-management.md#espcreateeventqueue) | The API `EspCreateEventQueue` creates an event queue for a client. |
| [`EspCreateFileFilter`](wesp-filter-creation.md#espcreatefilefilter) | The API `EspCreateFileFilter` is used to create a filter for a file event object. |
| [`EspCreateFileObjectFilter`](wesp-filter-creation.md#espcreatefileobjectfilter) | The API `EspCreateFileObjectFilter` is used to create a filter for a file object event object. |
| [`EspCreateFileReferenceById`](wesp-file-objects.md#espcreatefilereferencebyid) | The API `EspCreateFileReferenceById` creates an event object reference for an existing file by its file id. |
| [`EspCreateFileReferenceByPath`](wesp-file-objects.md#espcreatefilereferencebypath) | The API `EspCreateFileReferenceByPath` creates an event object reference for an existing file by its path. |
| [`EspCreateFileStreamFilter`](wesp-filter-creation.md#espcreatefilestreamfilter) | The API `EspCreateFileStreamFilter` is used to create a filter for a file stream event object. |
| [`EspCreateFileStreamReferenceById`](wesp-file-objects.md#espcreatefilestreamreferencebyid) | The API `EspCreateFileStreamReferenceById` creates an event object reference for an existing file stream by its file id. |
| [`EspCreateFileStreamReferenceByPath`](wesp-file-objects.md#espcreatefilestreamreferencebypath) | The API `EspCreateFileStreamReferenceByPath` creates an event object reference to an existing file stream by its path. |
| [`EspCreateFilter`](wesp-filter-creation.md#espcreatefilter) | The API `EspCreateFilter` is used to create a non-typed filter -- a filter that isn't associated with any property ID. |
| [`EspCreateKtmTransactionFilter`](wesp-filter-creation.md#espcreatektmtransactionfilter) | The API `EspCreateKtmTransactionFilter` is used to create a filter for a KTM transaction event object. |
| [`EspCreateMailslotFilter`](wesp-filter-creation.md#espcreatemailslotfilter) | The API `EspCreateMailslotFilter` is used to create a filter for a mailslot event object. |
| [`EspCreateMailslotReference`](wesp-other-event-objects.md#espcreatemailslotreference) | The API `EspCreateMailslotReference` creates an event object reference to an existing mailslot. |
| [`EspCreateNotFilter`](wesp-filter-creation.md#espcreatenotfilter) | The API `EspCreateNotFilter` is used to create a composite filter that represents the logical negation (NOT) of a filter. |
| [`EspCreateOrFilter`](wesp-filter-creation.md#espcreateorfilter) | The API `EspCreateOrFilter` is used to create a composite filter that represents the logical disjunction (OR) of two existing filters. |
| [`EspCreatePipeFilter`](wesp-filter-creation.md#espcreatepipefilter) | The API `EspCreatePipeFilter` is used to create a filter for a pipe event object. |
| [`EspCreatePipeReference`](wesp-other-event-objects.md#espcreatepipereference) | The API `EspCreatePipeReference` creates an event object reference to an existing pipe. |
| [`EspCreateProcessFilter`](wesp-filter-creation.md#espcreateprocessfilter) | The API `EspCreateProcessFilter` is used to create a filter for a process event object. |
| [`EspCreateProcessReference`](wesp-execution-objects.md#espcreateprocessreference) | The API `EspCreateProcessReference` creates an event object reference for an existing process. |
| [`EspCreateProcessTokenReference`](wesp-execution-objects.md#espcreateprocesstokenreference) | The API `EspCreateProcessTokenReference` creates an event object reference to an existing process's token. |
| [`EspCreateRegistryKeyFilter`](wesp-filter-creation.md#espcreateregistrykeyfilter) | The API `EspCreateRegistryKeyFilter` is used to create a filter for a registry key event object. |
| [`EspCreateRegistryKeyObjectFilter`](wesp-filter-creation.md#espcreateregistrykeyobjectfilter) | The API `EspCreateRegistryKeyObjectFilter` is used to create a filter for a registry key object event object. |
| [`EspCreateRegistryKeyReference`](wesp-other-event-objects.md#espcreateregistrykeyreference) | The API `EspCreateRegistryKeyReference` creates an event object reference to an existing registry key. |
| [`EspCreateRule`](wesp-rule-management.md#espcreaterule) | The API `EspCreateRule` creates a rule. |
| [`EspCreateThreadFilter`](wesp-filter-creation.md#espcreatethreadfilter) | The API `EspCreateThreadFilter` is used to create a filter for a thread event object. |
| [`EspCreateThreadReference`](wesp-execution-objects.md#espcreatethreadreference) | The API `EspCreateThreadReference` creates an event object reference to an existing thread. |
| [`EspCreateThreadTokenReference`](wesp-execution-objects.md#espcreatethreadtokenreference) | The API `EspCreateThreadTokenReference` creates an event object reference to an existing thread's token. |
| [`EspCreateTokenFilter`](wesp-filter-creation.md#espcreatetokenfilter) | The API `EspCreateTokenFilter` is used to create a filter for a token event object. |
| [`EspCreateVolumeFilter`](wesp-filter-creation.md#espcreatevolumefilter) | The API `EspCreateVolumeFilter` is used to create a filter for a volume event object. |
| [`EspCreateVolumeReference`](wesp-storage-objects.md#espcreatevolumereference) | The API `EspCreateVolumeReference` creates an event object reference to an existing volume. |
| [`EspCreateXorFilter`](wesp-filter-creation.md#espcreatexorfilter) | The API `EspCreateXorFilter` is used to create a composite filter that represents the logical exclusive disjunction (XOR) of two existing filters. |
| [`EspDisconnectClient`](wesp-clients.md#espdisconnectclient) | The API `EspDisconnectClient` is used to disconnect a WESP client. |
| [`EspDisconnectEventQueue`](wesp-event-queue-delivery.md#espdisconnecteventqueue) | The API `EspDisconnectEventQueue` disconnects an event queue. |
| [`EspDuplicateEventObjectReference`](wesp-event-object-references.md#espduplicateeventobjectreference) | The API `EspDuplicateEventObjectReference` duplicates an existing event object reference. |
| [`EspEnumerateAllClientContextKeys`](wesp-context-key-management.md#espenumerateallclientcontextkeys) | The API `EspEnumerateAllClientContextKeys` enumerates all the context keys currently associated with a client. |
| [`EspEnumerateAllEventObjectContextKeys`](wesp-context-key-management.md#espenumeratealleventobjectcontextkeys) | The API `EspEnumerateAllEventObjectContextKeys` enumerates all the context keys currently associated with an event object. |
| [`EspEnumerateAllRulesForClient`](wesp-rule-management.md#espenumerateallrulesforclient) | The API `EspEnumerateAllRulesForClient` enumerates all rule IDs for a client. |
| [`EspEnumerateCollectionEntries`](wesp-collection-management.md#espenumeratecollectionentries) | The API `EspEnumerateCollectionEntries` is used to retrieve all the entries in a collection. |
| [`EspEnumerateCollectionIds`](wesp-collection-management.md#espenumeratecollectionids) | The API `EspEnumerateCollectionIds` enumerates the client's collection IDs with the specified lifetime. |
| [`EspEnumerateConnectedClients`](wesp-clients.md#espenumerateconnectedclients) | The API `EspEnumerateConnectedClients` is used to enumerate all the connected WESP clients. |
| [`EspEnumerateEventQueueIds`](wesp-event-queue-management.md#espenumerateeventqueueids) | The API `EspEnumerateEventQueueIds` enumerates event queue IDs associated with the client. |
| [`EspEnumerateRegisteredClients`](wesp-clients.md#espenumerateregisteredclients) | The API `EspEnumerateRegisteredClients` is used to enumerate all the registered WESP clients. |
| [`EspEnumerateRuleIds`](wesp-rule-management.md#espenumerateruleids) | The API `EspEnumerateRuleIds` enumerates rule IDs for a client. |
| [`EspFreeEventNotification`](wesp-event-notifications.md#espfreeeventnotification) | The API `EspFreeEventNotification` frees an event notification that was previously allocated by calling `EspAllocateEventNotification`. |
| [`EspFreeMemory`](wesp-common-utilities.md#espfreememory) | The API `EspFreeMemory` is used to free memory that was allocated by various WESP APIs. |
| [`EspGetCollectionId`](wesp-collection-management.md#espgetcollectionid) | The API `EspGetCollectionId` retrieves the collection identifier. |
| [`EspGetCollectionType`](wesp-collection-management.md#espgetcollectiontype) | The API `EspGetCollectionType` retrieves the collection type. |
| [`EspGetEventCapabilities`](wesp-event-capabilities.md#espgeteventcapabilities) | The API `EspGetEventCapabilities` can be used to obtain the supported capabilities for a specific event for a specific client. |
| [`EspGetEventObjectFromReference`](wesp-event-object-references.md#espgeteventobjectfromreference) | The API `EspGetEventObjectFromReference` retrieves the event object (`ESP_EVENT_OBJECT`) from a strong reference (`ESP_EVENT_OBJECT_REF`). |
| [`EspGetEventObjectId`](wesp-event-object-references.md#espgeteventobjectid) | The API `EspGetEventObjectId` can be used to retrieve an event object's id. |
| [`EspGetEventObjectType`](wesp-event-object-references.md#espgeteventobjecttype) | The API `EspGetEventObjectType` can be used to retrieve an event object's type. |
| [`EspGetEventQueueId`](wesp-event-queue-management.md#espgeteventqueueid) | The API `EspGetEventQueueId` retrieves the ID of an event queue. |
| [`EspGetPropertyAcl`](wesp-domain-property-accessors.md#espgetpropertyacl) | Retrieves the Acl value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyBool`](wesp-scalar-property-accessors.md#espgetpropertybool) | Retrieves the Bool value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyBuffer`](wesp-scalar-property-accessors.md#espgetpropertybuffer) | Retrieves the Buffer value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyContextKeyInfo`](wesp-domain-property-accessors.md#espgetpropertycontextkeyinfo) | Retrieves context-key information from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyDeviceType`](wesp-domain-property-accessors.md#espgetpropertydevicetype) | Retrieves the DeviceType value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyEaList`](wesp-domain-property-accessors.md#espgetpropertyealist) | Retrieves the EaList value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyError`](wesp-scalar-property-accessors.md#espgetpropertyerror) | Retrieves the property-level error stored in an `ESP_PROPERTY` structure. |
| [`EspGetPropertyFileId128`](wesp-domain-property-accessors.md#espgetpropertyfileid128) | Retrieves the FileId128 value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyFileTime`](wesp-scalar-property-accessors.md#espgetpropertyfiletime) | Retrieves the FileTime value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyFoTargetObjectType`](wesp-domain-property-accessors.md#espgetpropertyfotargetobjecttype) | Retrieves the FoTargetObjectType value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyGuid`](wesp-scalar-property-accessors.md#espgetpropertyguid) | Retrieves the Guid value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyImpersonationLevel`](wesp-domain-property-accessors.md#espgetpropertyimpersonationlevel) | Retrieves the ImpersonationLevel value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyInt32`](wesp-scalar-property-accessors.md#espgetpropertyint32) | Retrieves the Int32 value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyMemoryAddressBasic`](wesp-domain-property-accessors.md#espgetpropertymemoryaddressbasic) | Retrieves the MemoryAddressBasic value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyNtStatus`](wesp-scalar-property-accessors.md#espgetpropertyntstatus) | Retrieves the NtStatus value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertySecurityDescriptor`](wesp-domain-property-accessors.md#espgetpropertysecuritydescriptor) | Retrieves the SecurityDescriptor value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertySid`](wesp-domain-property-accessors.md#espgetpropertysid) | Retrieves the Sid value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertySigningLevel`](wesp-domain-property-accessors.md#espgetpropertysigninglevel) | Retrieves the SigningLevel value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyStorageBusType`](wesp-domain-property-accessors.md#espgetpropertystoragebustype) | Retrieves the StorageBusType value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyStringList`](wesp-scalar-property-accessors.md#espgetpropertystringlist) | Retrieves the StringList value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertySubsystemInformationType`](wesp-domain-property-accessors.md#espgetpropertysubsysteminformationtype) | Retrieves the SubsystemInformationType value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyTokenElevationType`](wesp-domain-property-accessors.md#espgetpropertytokenelevationtype) | Retrieves the TokenElevationType value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyTokenGroups`](wesp-domain-property-accessors.md#espgetpropertytokengroups) | Retrieves the TokenGroups value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyTokenPrivileges`](wesp-domain-property-accessors.md#espgetpropertytokenprivileges) | Retrieves the TokenPrivileges value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyTokenType`](wesp-domain-property-accessors.md#espgetpropertytokentype) | Retrieves the TokenType value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyTransactionOutcome`](wesp-domain-property-accessors.md#espgetpropertytransactionoutcome) | Retrieves the TransactionOutcome value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyTransactionState`](wesp-domain-property-accessors.md#espgetpropertytransactionstate) | Retrieves the TransactionState value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyUint16`](wesp-scalar-property-accessors.md#espgetpropertyuint16) | Retrieves the Uint16 value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyUint32`](wesp-scalar-property-accessors.md#espgetpropertyuint32) | Retrieves the Uint32 value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyUint64`](wesp-scalar-property-accessors.md#espgetpropertyuint64) | Retrieves the Uint64 value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyUint8`](wesp-scalar-property-accessors.md#espgetpropertyuint8) | Retrieves the Uint8 value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyUnicodeString`](wesp-scalar-property-accessors.md#espgetpropertyunicodestring) | Retrieves the UnicodeString value from an `ESP_PROPERTY` structure. |
| [`EspGetPropertyUsn`](wesp-domain-property-accessors.md#espgetpropertyusn) | Retrieves the Usn value from an `ESP_PROPERTY` structure. |
| [`EspGetRuleId`](wesp-rule-management.md#espgetruleid) | The API `EspGetRuleId` retrieves the ID from a rule. |
| [`EspInitUnicodeString`](wesp-common-utilities.md#espinitunicodestring) | The API `EspInitUnicodeString` initializes an `ESP_UNICODE_STRING` struct from a null-terminated string. |
| [`EspIsClientPropertySupported`](wesp-event-capabilities.md#espisclientpropertysupported) | The API `EspIsClientPropertySupported` can be used to dynamically check if a client property ID is supported by the WESP framework. |
| [`EspIsDesktopPropertySupported`](wesp-event-capabilities.md#espisdesktoppropertysupported) | The API `EspIsDesktopPropertySupported` can be used to dynamically check if a desktop property ID is supported by the WESP framework. |
| [`EspIsDiskPropertySupported`](wesp-event-capabilities.md#espisdiskpropertysupported) | The API `EspIsDiskPropertySupported` can be used to dynamically check if a disk property ID is supported by the WESP framework. |
| [`EspIsEventPropertySupported`](wesp-event-capabilities.md#espiseventpropertysupported) | The API `EspIsEventPropertySupported` can be used to dynamically check if an event property ID is supported by the WESP framework. |
| [`EspIsFileObjectPropertySupported`](wesp-event-capabilities.md#espisfileobjectpropertysupported) | The API `EspIsFileObjectPropertySupported` can be used to dynamically check if a file object property ID is supported by the WESP framework. |
| [`EspIsFilePropertySupported`](wesp-event-capabilities.md#espisfilepropertysupported) | The API `EspIsFilePropertySupported` can be used to dynamically check if a file property ID is supported by the WESP framework. |
| [`EspIsFileStreamPropertySupported`](wesp-event-capabilities.md#espisfilestreampropertysupported) | The API `EspIsFileStreamPropertySupported` can be used to dynamically check if a file stream property ID is supported by the WESP framework. |
| [`EspIsKtmTransactionPropertySupported`](wesp-event-capabilities.md#espisktmtransactionpropertysupported) | The API `EspIsKtmTransactionPropertySupported` can be used to dynamically check if a KTM transaction property ID is supported by the WESP framework. |
| [`EspIsMailslotPropertySupported`](wesp-event-capabilities.md#espismailslotpropertysupported) | The API `EspIsMailslotPropertySupported` can be used to dynamically check if a mailslot property ID is supported by the WESP framework. |
| [`EspIsPipePropertySupported`](wesp-event-capabilities.md#espispipepropertysupported) | The API `EspIsPipePropertySupported` can be used to dynamically check if a pipe property ID is supported by the WESP framework. |
| [`EspIsProcessPropertySupported`](wesp-event-capabilities.md#espisprocesspropertysupported) | The API `EspIsProcessPropertySupported` can be used to dynamically check if a process property ID is supported by the WESP framework. |
| [`EspIsRegistryKeyObjectPropertySupported`](wesp-event-capabilities.md#espisregistrykeyobjectpropertysupported) | The API `EspIsRegistryKeyObjectPropertySupported` can be used to dynamically check if a registry key object property ID is supported by the WESP framework. |
| [`EspIsRegistryKeyPropertySupported`](wesp-event-capabilities.md#espisregistrykeypropertysupported) | The API `EspIsRegistryKeyPropertySupported` can be used to dynamically check if a registry key property ID is supported by the WESP framework. |
| [`EspIsThreadPropertySupported`](wesp-event-capabilities.md#espisthreadpropertysupported) | The API `EspIsThreadPropertySupported` can be used to dynamically check if a thread property ID is supported by the WESP framework. |
| [`EspIsTokenPropertySupported`](wesp-event-capabilities.md#espistokenpropertysupported) | The API `EspIsTokenPropertySupported` can be used to dynamically check if a token property ID is supported by the WESP framework. |
| [`EspIsVolumePropertySupported`](wesp-event-capabilities.md#espisvolumepropertysupported) | The API `EspIsVolumePropertySupported` can be used to dynamically check if a volume property ID is supported by the WESP framework. |
| [`EspOpenCollection`](wesp-collection-management.md#espopencollection) | The API `EspOpenCollection` is used to open a reference to a collection using its id. |
| [`EspOpenEventQueue`](wesp-event-queue-management.md#espopeneventqueue) | The API `EspOpenEventQueue` opens an existing event queue. |
| [`EspQueryClientDescriptor`](wesp-clients.md#espqueryclientdescriptor) | The API `EspQueryClientDescriptor` can be used to query the descriptor for a given client. |
| [`EspQueryClientProperties`](wesp-property-queries.md#espqueryclientproperties) | The API `EspQueryClientProperties` is used to query properties associated with the client. |
| [`EspQueryDesktopProperties`](wesp-property-queries.md#espquerydesktopproperties) | The API `EspQueryDesktopProperties` is used to query properties for a desktop event object. |
| [`EspQueryDiskProperties`](wesp-property-queries.md#espquerydiskproperties) | The API `EspQueryDiskProperties` is used to query properties for a disk event object. |
| [`EspQueryFileObjectProperties`](wesp-property-queries.md#espqueryfileobjectproperties) | The API `EspQueryFileObjectProperties` is used to query properties for a file object event object. |
| [`EspQueryFileProperties`](wesp-property-queries.md#espqueryfileproperties) | The API `EspQueryFileProperties` is used to query properties for a file event object. |
| [`EspQueryFileStreamProperties`](wesp-property-queries.md#espqueryfilestreamproperties) | The API `EspQueryFileStreamProperties` is used to query properties for a file stream event object. |
| [`EspQueryKtmTransactionProperties`](wesp-property-queries.md#espqueryktmtransactionproperties) | The API `EspQueryKtmTransactionProperties` is used to query properties for a KTM transaction event object. |
| [`EspQueryMailslotProperties`](wesp-property-queries.md#espquerymailslotproperties) | The API `EspQueryMailslotProperties` is used to query properties for a mailslot event object. |
| [`EspQueryPipeProperties`](wesp-property-queries.md#espquerypipeproperties) | The API `EspQueryPipeProperties` is used to query properties for a pipe event object. |
| [`EspQueryProcessProperties`](wesp-property-queries.md#espqueryprocessproperties) | The API `EspQueryProcessProperties` is used to query properties for a process event object. |
| [`EspQueryRegistryKeyObjectProperties`](wesp-property-queries.md#espqueryregistrykeyobjectproperties) | The API `EspQueryRegistryKeyObjectProperties` is used to query properties for a registry key object event object. |
| [`EspQueryRegistryKeyProperties`](wesp-property-queries.md#espqueryregistrykeyproperties) | The API `EspQueryRegistryKeyProperties` is used to query properties for a registry key event object. |
| [`EspQueryThreadProperties`](wesp-property-queries.md#espquerythreadproperties) | The API `EspQueryThreadProperties` is used to query properties for a thread event object. |
| [`EspQueryTokenProperties`](wesp-property-queries.md#espquerytokenproperties) | The API `EspQueryTokenProperties` is used to query properties for a token event object. |
| [`EspQueryVolumeProperties`](wesp-property-queries.md#espqueryvolumeproperties) | The API `EspQueryVolumeProperties` is used to query properties for a volume event object. |
| [`EspRegisterClient`](wesp-clients.md#espregisterclient) | The API `EspRegisterClient` is used to register a client with the WESP framework. |
| [`EspRemoveAllRulesForClient`](wesp-rule-management.md#espremoveallrulesforclient) | Removes all rules for the specified WESP client. |
| [`EspRemoveEventQueueStateChangeCallback`](wesp-event-queue-delivery.md#espremoveeventqueuestatechangecallback) | The API `EspRemoveEventQueueStateChangeCallback` removes the state change callback from the event queue. |
| [`EspRemoveRulesForClient`](wesp-rule-management.md#espremoverulesforclient) | The API `EspRemoveRulesForClient` removes rules with the specified lifetime for the client. |
| [`EspSetClientContextKey`](wesp-context-key-management.md#espsetclientcontextkey) | The API `EspSetClientContextKey` adds, removes, or updates a client context key. |
| [`EspSetEventObjectContextKey`](wesp-context-key-management.md#espseteventobjectcontextkey) | The API `EspSetEventObjectContextKey` is used to add, remove, or update an event object context key. |
| [`EspSetEventQueueStateChangeCallback`](wesp-event-queue-delivery.md#espseteventqueuestatechangecallback) | The API `EspSetEventQueueStateChangeCallback` configures a state change callback for the event queue. |
| [`EspStringMatchesPattern`](wesp-common-utilities.md#espstringmatchespattern) | The API `EspStringMatchesPattern` checks if a string matches a given pattern. |
| [`EspUnregisterClient`](wesp-clients.md#espunregisterclient) | The API `EspUnregisterClient` is used to unregister a client with the WESP framework. |
| [`EspUpdateCollection`](wesp-collection-updates.md#espupdatecollection) | The API `EspUpdateCollection` is used to update a collection. |
| [`EspUpdateRules`](wesp-rule-management.md#espupdaterules) | The API `EspUpdateRules` updates a set of rules. |

### Enumerations

| API | Description |
| --- | --- |
| [`ESP_BINARY_COMPARISON_TYPE`](wesp-filter-scalar-comparisons.md#esp_binary_comparison_type) | The enum `ESP_BINARY_COMPARISON_TYPE` defines a binary comparison type. |
| [`ESP_BINDING_KEY_DATA_TYPE`](wesp-rule-configuration.md#esp_binding_key_data_type) | The enum `ESP_BINDING_KEY_DATA_TYPE` defines the different data types a binding key can resolve as. |
| [`ESP_BLOCK_REASON`](wesp-rule-management.md#esp_block_reason) | The enum `ESP_BLOCK_REASON` defines a block reason. |
| [`ESP_BOOL_COMPARISON_TYPE`](wesp-filter-scalar-comparisons.md#esp_bool_comparison_type) | The enum `ESP_BOOL_COMPARISON_TYPE` defines a bool comparison type. |
| [`ESP_BYTE_RANGE_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_byte_range_comparison_type) | The enum `ESP_BYTE_RANGE_COMPARISON_TYPE` defines a byte range comparison type. |
| [`ESP_CLIENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_client_property_id) | Client properties are defined in the enum `ESP_CLIENT_PROPERTY_ID`. |
| [`ESP_COLLECTION_LIFETIME`](wesp-collection-management.md#esp_collection_lifetime) | The enum `ESP_COLLECTION_LIFETIME` specifies the lifetime of a collection. |
| [`ESP_COLLECTION_TYPE`](wesp-collection-management.md#esp_collection_type) | The enum `ESP_COLLECTION_TYPE` specifies a kind of collection. |
| [`ESP_COLLECTION_UPDATE_FLAGS`](wesp-collection-updates.md#esp_collection_update_flags) | The enum `ESP_COLLECTION_UPDATE_FLAGS` specifies flags for updating a collection. |
| [`ESP_COLLECTION_UPDATE_TYPE`](wesp-collection-updates.md#esp_collection_update_type) | The enum `ESP_COLLECTION_UPDATE_TYPE` defines a collection update type. |
| [`ESP_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_comparison_type) | Identifies the comparison structure supplied when creating a WESP filter. |
| [`ESP_CONTEXT_KEY_COMPARISON_TYPE`](wesp-filter-comparison-types.md#esp_context_key_comparison_type) | The enum `ESP_CONTEXT_KEY_COMPARISON_TYPE` defines a context key comparison type. |
| [`ESP_CONTEXT_KEY_LIFETIME`](wesp-context-key-management.md#esp_context_key_lifetime) | The enum `ESP_CONTEXT_KEY_LIFETIME` defines a context key lifetime. |
| [`ESP_CONTEXT_KEY_UPDATE_FLAGS`](wesp-context-key-management.md#esp_context_key_update_flags) | The enum `ESP_CONTEXT_KEY_UPDATE_FLAGS` specifies flags for a context update. |
| [`ESP_CONTEXT_KEY_UPDATE_TYPE`](wesp-context-key-management.md#esp_context_key_update_type) | The enum `ESP_CONTEXT_KEY_UPDATE_TYPE` defines a context key update type. |
| [`ESP_CONTEXT_KEY_VALUE_TYPE`](wesp-context-key-management.md#esp_context_key_value_type) | The enum `ESP_CONTEXT_KEY_VALUE_TYPE` defines a context key value type. |
| [`ESP_DESKTOP_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_desktop_config_flags) | The enum `ESP_DESKTOP_CONFIG_FLAGS` specifies flags for an `ESP_DESKTOP_CONFIG` structure. |
| [`ESP_DESKTOP_PROPERTY_ID`](wesp-other-property-ids.md#esp_desktop_property_id) | Desktop properties are defined in the enum `ESP_DESKTOP_PROPERTY_ID`. |
| [`ESP_DISK_CONFIG_FLAGS`](wesp-storage-objects.md#esp_disk_config_flags) | The enum `ESP_DISK_CONFIG_FLAGS` specifies flags for an `ESP_DISK_CONFIG` structure. |
| [`ESP_DISK_PROPERTY_ID`](wesp-file-property-ids.md#esp_disk_property_id) | Disk properties are defined in the enum `ESP_DISK_PROPERTY_ID`. |
| [`ESP_EA_LIST_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_ea_list_comparison_type) | The enum `ESP_EA_LIST_COMPARISON_TYPE` defines an EA list comparison type. |
| [`ESP_ECP_LIST_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_ecp_list_comparison_type) | The enum `ESP_ECP_LIST_COMPARISON_TYPE` defines an ECP list comparison type. |
| [`ESP_EVENT_CAPABILITIES`](wesp-event-capabilities.md#esp_event_capabilities) | The enum `ESP_EVENT_CAPABILITIES` defines the set of capabilities that are supported for a given event type. |
| [`ESP_EVENT_MODIFY_TYPE`](wesp-rule-event-modification.md#esp_event_modify_type) | The enum `ESP_EVENT_MODIFY_TYPE` defines an event modification type. |
| [`ESP_EVENT_NOTIFICATION_FLAGS`](wesp-event-notifications.md#esp_event_notification_flags) | The enum `ESP_EVENT_NOTIFICATION_FLAGS` defines event notification flags. |
| [`ESP_EVENT_NOTIFICATION_VERSION`](wesp-event-notifications.md#esp_event_notification_version) | The enum `ESP_EVENT_NOTIFICATION_VERSION` specifies the version of an event notification. |
| [`ESP_EVENT_OBJECT_TYPE`](wesp-event-object-references.md#esp_event_object_type) | The enum `ESP_EVENT_OBJECT_TYPE` defines an event object type. |
| [`ESP_EVENT_PROPERTY_ID`](wesp-execution-property-ids.md#esp_event_property_id) | Event properties are defined in the enum `ESP_EVENT_PROPERTY_ID`. |
| [`ESP_EVENT_QUEUE_LIFETIME`](wesp-event-queue-management.md#esp_event_queue_lifetime) | The enum `ESP_RULE_LIFETIME` specifies the lifetime for an event queue. |
| [`ESP_EVENT_QUEUE_STATE`](wesp-event-queue-delivery.md#esp_event_queue_state) | The enum `ESP_EVENT_QUEUE_STATE` defines an event queue's state. |
| [`ESP_EVENT_QUEUE_TYPE`](wesp-event-queue-management.md#esp_event_queue_type) | The enum `ESP_EVENT_QUEUE_TYPE` defines an event queue type. |
| [`ESP_EVENT_TYPE`](wesp-event-shared-types.md#esp_event_type) | Identifies the system event associated with a WESP rule or notification. |
| [`ESP_FILE_CONFIG_FLAGS`](wesp-file-objects.md#esp_file_config_flags) | The enum `ESP_FILE_CONFIG_FLAGS` specifies flags for an `ESP_FILE_CONFIG` structure. |
| [`ESP_FILE_OBJECT_CONFIG_FLAGS`](wesp-file-objects.md#esp_file_object_config_flags) | The enum `ESP_FILE_OBJECT_CONFIG_FLAGS` specifies flags for an `ESP_FILE_OBJECT_CONFIG` structure. |
| [`ESP_FILE_OBJECT_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_object_property_id) | File object properties are defined in the enum `ESP_FILE_OBJECT_PROPERTY_ID`. |
| [`ESP_FILE_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_property_id) | File properties are defined in the enum `ESP_FILE_PROPERTY_ID`. |
| [`ESP_FILE_STREAM_CONFIG_FLAGS`](wesp-file-objects.md#esp_file_stream_config_flags) | The enum `ESP_FILE_STREAM_CONFIG_FLAGS` specifies flags for an `ESP_FILE_STREAM_CONFIG` structure. |
| [`ESP_FILE_STREAM_PROPERTY_ID`](wesp-file-property-ids.md#esp_file_stream_property_id) | File stream properties are defined in the enum `ESP_FILE_STREAM_PROPERTY_ID`. |
| [`ESP_FILE_UNLOCK_TYPE`](wesp-file-system-events.md#esp_file_unlock_type) | The enum `ESP_FILE_UNLOCK_TYPE` defines a file unlock type. |
| [`ESP_FO_TARGET_OBJECT_TYPE`](wesp-common-value-types.md#esp_fo_target_object_type) | The enum `ESP_FO_TARGET_OBJECT_TYPE` specifies the target object type for a file object. |
| [`ESP_INTEGER_COMPARISON_TYPE`](wesp-filter-scalar-comparisons.md#esp_integer_comparison_type) | The enum `ESP_INTEGER_COMPARISON_TYPE` defines an integer comparison type. |
| [`ESP_IO_OPERATION_FLAGS`](wesp-event-shared-types.md#esp_io_operation_flags) | The enum `ESP_IO_OPERATION_FLAGS` specifies flags for an IO operation. |
| [`ESP_IOCP_COMPLETION_KEY`](wesp-event-queue-delivery.md#esp_iocp_completion_key) | The enum `ESP_IOCP_COMPLETION_KEY` defines an IOCP completion key. |
| [`ESP_KTM_TRANSACTION_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_ktm_transaction_config_flags) | The enum `ESP_KTM_TRANSACTION_CONFIG_FLAGS` specifies flags for an `ESP_KTM_TRANSACTION_CONFIG` structure. |
| [`ESP_KTM_TRANSACTION_PROPERTY_ID`](wesp-other-property-ids.md#esp_ktm_transaction_property_id) | KTM transaction properties are defined in the enum `ESP_KTM_TRANSACTION_PROPERTY_ID`. |
| [`ESP_MAILSLOT_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_mailslot_config_flags) | The enum `ESP_MAILSLOT_CONFIG_FLAGS` specifies flags for an `ESP_MAILSLOT_CONFIG` structure. |
| [`ESP_MAILSLOT_PROPERTY_ID`](wesp-other-property-ids.md#esp_mailslot_property_id) | Mailslot properties are defined in the enum `ESP_MAILSLOT_PROPERTY_ID`. |
| [`ESP_NETWORK_ADDRESS_FAMILY`](wesp-common-value-types.md#esp_network_address_family) | The enum `ESP_NETWORK_ADDRESS_FAMILY` defines a network address family. |
| [`ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_network_ip_address_comparison_type) | The enum `ESP_NETWORK_IP_ADDRESS_COMPARISON_TYPE` defines a network IP address comparison type. |
| [`ESP_NETWORK_PORT_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_network_port_comparison_type) | The enum `ESP_NETWORK_PORT_COMPARISON_TYPE` defines a network port comparison type. |
| [`ESP_NETWORK_RANGE_TYPE`](wesp-common-value-types.md#esp_network_range_type) | The enum `ESP_NETWORK_RANGE_TYPE` represents a kind of network range. |
| [`ESP_NUMERICAL_TRANSFORM_TYPE`](wesp-filter-comparison-types.md#esp_numerical_transform_type) | The enum `ESP_NUMERICAL_TRANSFORM_TYPE` defines a numerical transform type. |
| [`ESP_PATH_FORMAT`](wesp-common-utilities.md#esp_path_format) | The enum `ESP_PATH_FORMAT` defines a path format. |
| [`ESP_PIPE_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_pipe_config_flags) | The enum `ESP_PIPE_CONFIG_FLAGS` specifies flags for an `ESP_PIPE_CONFIG` structure. |
| [`ESP_PIPE_PROPERTY_ID`](wesp-other-property-ids.md#esp_pipe_property_id) | Pipe properties are defined in the enum `ESP_PIPE_PROPERTY_ID`. |
| [`ESP_PROCESS_CONFIG_FLAGS`](wesp-execution-objects.md#esp_process_config_flags) | The enum `ESP_PROCESS_CONFIG_FLAGS` specifies flags for an `ESP_PROCESS_CONFIG` structure. |
| [`ESP_PROCESS_PROPERTY_ID`](wesp-execution-property-ids.md#esp_process_property_id) | Process properties are defined in the enum `ESP_PROCESS_PROPERTY_ID`. |
| [`ESP_REG_DATA_COMPARISON_TYPE`](wesp-filter-domain-comparisons.md#esp_reg_data_comparison_type) | The enum `ESP_REG_DATA_COMPARISON_TYPE` defines a registry data comparison type. |
| [`ESP_REGISTRY_KEY_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_registry_key_config_flags) | The enum `ESP_REGISTRY_KEY_CONFIG_FLAGS` specifies flags for an `ESP_REGISTRY_KEY_CONFIG` structure. |
| [`ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS`](wesp-other-event-objects.md#esp_registry_key_object_config_flags) | The enum `ESP_REGISTRY_KEY_OBJECT_CONFIG_FLAGS` specifies flags for an `ESP_REGISTRY_KEY_OBJECT_CONFIG` structure. |
| [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_object_property_id) | Registry key object properties are defined in the enum `ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID`. |
| [`ESP_REGISTRY_KEY_PROPERTY_ID`](wesp-other-property-ids.md#esp_registry_key_property_id) | Registry key properties are defined in the enum `ESP_REGISTRY_KEY_PROPERTY_ID`. |
| [`ESP_RULE_ACTION`](wesp-rule-management.md#esp_rule_action) | The enum `ESP_RULE_ACTION` defines a rule action. |
| [`ESP_RULE_CONFIG_EXTENSION_TYPE`](wesp-rule-configuration.md#esp_rule_config_extension_type) | Identifies the type of a rule configuration extension. |
| [`ESP_RULE_FLAGS`](wesp-rule-management.md#esp_rule_flags) | The enum `ESP_RULE_FLAGS` defines rule flags. |
| [`ESP_RULE_LIFETIME`](wesp-rule-management.md#esp_rule_lifetime) | The enum `ESP_RULE_LIFETIME` specifies the lifetime for a rule. |
| [`ESP_RULE_UPDATE_FLAGS`](wesp-rule-management.md#esp_rule_update_flags) | The enum `ESP_RULE_UPDATE_FLAGS` specifies flags for updating rules. |
| [`ESP_RULE_UPDATE_TYPE`](wesp-rule-management.md#esp_rule_update_type) | The enum `ESP_RULE_UPDATE_TYPE` defines a rule update type. |
| [`ESP_SECURITY_DESCRIPTOR_FORMAT`](wesp-filter-security-comparisons.md#esp_security_descriptor_format) | The enum `ESP_SECURITY_DESCRIPTOR_FORMAT` specifies the format of a security descriptor. |
| [`ESP_SID_COMPARISON_TYPE`](wesp-filter-security-comparisons.md#esp_sid_comparison_type) | The enum `ESP_SID_COMPARISON_TYPE` defines a SID comparison type. |
| [`ESP_SID_FORMAT`](wesp-filter-security-comparisons.md#esp_sid_format) | The enum `ESP_SID_FORMAT` defines a SID format. |
| [`ESP_STRING_COLLECTION_FLAGS`](wesp-collection-updates.md#esp_string_collection_flags) | The enum `ESP_STRING_COLLECTION_FLAGS` defines string collection flags. |
| [`ESP_STRING_COMPARISON_TYPE`](wesp-filter-string-comparisons.md#esp_string_comparison_type) | The enum `ESP_STRING_COMPARISON_TYPE` defines a string comparison type. |
| [`ESP_STRING_LIST_COMPARISON_TYPE`](wesp-filter-string-comparisons.md#esp_string_list_comparison_type) | The enum `ESP_STRING_LIST_COMPARISON_TYPE` defines a string list comparison type. |
| [`ESP_SUBSYSTEM_INFORMATION_TYPE`](wesp-common-value-types.md#esp_subsystem_information_type) | The enum `ESP_SUBSYSTEM_INFORMATION_TYPE` represents a process subsystem type. |
| [`ESP_THREAD_CONFIG_FLAGS`](wesp-execution-objects.md#esp_thread_config_flags) | The enum `ESP_THREAD_CONFIG_FLAGS` specifies flags for an `ESP_THREAD_CONFIG` structure. |
| [`ESP_THREAD_CREATE_FLAGS`](wesp-thread-events.md#esp_thread_create_flags) | The enum `ESP_THREAD_CREATE_FLAGS` defines flags for the thread create event. |
| [`ESP_THREAD_PROPERTY_ID`](wesp-execution-property-ids.md#esp_thread_property_id) | Thread properties are defined in the enum `ESP_THREAD_PROPERTY_ID`. |
| [`ESP_TOKEN_CONFIG_FLAGS`](wesp-execution-objects.md#esp_token_config_flags) | The enum `ESP_TOKEN_CONFIG_FLAGS` specifies flags for an `ESP_TOKEN_CONFIG` structure. |
| [`ESP_TOKEN_GROUPS_COMPARISON_TYPE`](wesp-filter-security-comparisons.md#esp_token_groups_comparison_type) | The enum `ESP_TOKEN_GROUPS_COMPARISON_TYPE` defines a token groups comparison type. |
| [`ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE`](wesp-filter-security-comparisons.md#esp_token_privileges_comparison_type) | The enum `ESP_TOKEN_PRIVILEGES_COMPARISON_TYPE` defines a token privileges comparison type. |
| [`ESP_TOKEN_PROPERTY_ID`](wesp-execution-property-ids.md#esp_token_property_id) | Token properties are defined in the enum `ESP_TOKEN_PROPERTY_ID`. |
| [`ESP_VALUE_SOURCE_TYPE`](wesp-filter-comparison-types.md#esp_value_source_type) | The enum `ESP_VALUE_SOURCE_TYPE` specifies the source type of a value. |
| [`ESP_VARIANT_TYPE`](wesp-property-queries.md#esp_variant_type) | The enum `ESP_VARIANT_TYPE` identifies which memory of the `ESP_VARIANT_VALUE` union is active. |
| [`ESP_VOLUME_CONFIG_FLAGS`](wesp-storage-objects.md#esp_volume_config_flags) | The enum `ESP_VOLUME_CONFIG_FLAGS` specifies flags for an `ESP_VOLUME_CONFIG` structure. |
| [`ESP_VOLUME_PROPERTY_ID`](wesp-file-property-ids.md#esp_volume_property_id) | Volume properties are defined in the enum `ESP_VOLUME_PROPERTY_ID`. |

### Structures and unions

| API | Description |
| --- | --- |
| [`ESP_ACCESS_MASK_MODIFICATION`](wesp-rule-event-modification.md#esp_access_mask_modification) | The structure `ESP_ACCESS_MASK_MODIFICATION` is used to describe an ACCESS_MASK modification as part of a rule. |
| [`ESP_ACCESS_MASK_MODIFICATION_LIST`](wesp-rule-event-modification.md#esp_access_mask_modification_list) | The structure `ESP_ACCESS_MASK_MODIFICATION_LIST` is used to describe a list of ACCESS_MASK modifications to make as part of a rule. |
| [`ESP_ACCESS_STATE`](wesp-event-shared-types.md#esp_access_state) | The structure `ESP_ACCESS_STATE` is used to represent the state of an access in progress. |
| [`ESP_ACCESS_STATE_CONFIG`](wesp-rule-value-configuration.md#esp_access_state_config) | The structure `ESP_ACCESS_STATE_CONFIG` is used to configure an `ESP_ACCESS_STATE` structure. |
| [`ESP_BINARY_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_binary_comparison) | The structure `ESP_BINARY_COMPARISON` is used to compare a binary value. |
| [`ESP_BINARY_CONFIG`](wesp-rule-value-configuration.md#esp_binary_config) | The structure `ESP_BINARY_CONFIG` is used to configure a binary value. |
| [`ESP_BINARY_VALUE_SOURCE`](wesp-filter-scalar-comparisons.md#esp_binary_value_source) | The structure `ESP_BINARY_VALUE_SOURCE` specifies the source of a binary value. |
| [`ESP_BOOL_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_bool_comparison) | The structure `ESP_STRING_COMPARISON` is used to compare a boolean value. |
| [`ESP_BOOL_CONFIG`](wesp-rule-value-configuration.md#esp_bool_config) | The structure `ESP_BOOL_CONFIG` is used to configure a boolean value. |
| [`ESP_BOOT_LOAD_DRIVER_CONFIG`](wesp-boot-driver-events.md#esp_boot_load_driver_config) | The structure `ESP_BOOT_LOAD_DRIVER_CONFIG` specifies configuration for a boot load driver event. |
| [`ESP_BOOT_LOAD_DRIVER_PARAMETERS`](wesp-boot-driver-events.md#esp_boot_load_driver_parameters) | The structure `ESP_BOOT_LOAD_DRIVER_PARAMETERS` specifies parameters for the boot load driver event. |
| [`ESP_BUFFER`](wesp-common-utilities.md#esp_buffer) | The structure `ESP_BUFFER` represents a buffer. |
| [`ESP_BYTE_RANGE`](wesp-common-value-types.md#esp_byte_range) | The structure `ESP_BYTE_RANGE` represents a byte range. |
| [`ESP_BYTE_RANGE_COMPARISON`](wesp-filter-domain-comparisons.md#esp_byte_range_comparison) | The structure `ESP_BYTE_RANGE_COMPARISON` is used to compare a byte range value. |
| [`ESP_BYTE_RANGE_CONFIG`](wesp-rule-value-configuration.md#esp_byte_range_config) | The structure `ESP_BYTE_RANGE_CONFIG` is used to configure a byte range value. |
| [`ESP_CLIENT_CONFIG`](wesp-clients.md#esp_client_config) | The structure `ESP_CLIENT_CONFIG` is used to set client configuration for a rule. |
| [`ESP_CLIENT_DESCRIPTOR`](wesp-clients.md#esp_client_descriptor) | The structure `ESP_CLIENT_DESCRIPTOR` describes a client. |
| [`ESP_COLLECTION_DESCRIPTOR`](wesp-collection-management.md#esp_collection_descriptor) | The structure `ESP_COLLECTION_DESCRIPTOR` describes a collection. |
| [`ESP_COLLECTION_ENTRY`](wesp-collection-updates.md#esp_collection_entry) | The union `ESP_COLLECTION_ENTRY` represents a collection entry. |
| [`ESP_COLLECTION_UPDATE_ENTRY`](wesp-collection-updates.md#esp_collection_update_entry) | The structure `ESP_COLLECTION_UPDATE_ENTRY` is used with the API `EspUpdateCollection` to update a collection. |
| [`ESP_CONTEXT_KEY_COMPARISON`](wesp-filter-comparison-types.md#esp_context_key_comparison) | The structure `ESP_CONTEXT_KEY_COMPARISON` is used to compare a context key. |
| [`ESP_CONTEXT_KEY_CONFIG`](wesp-context-key-management.md#esp_context_key_config) | The structure `ESP_CONTEXT_KEY_CONFIG` is used to set context key configuration. |
| [`ESP_CONTEXT_KEY_INFO`](wesp-context-key-management.md#esp_context_key_info) | The structure `ESP_CONTEXT_KEY_INFO` stores context key information. |
| [`ESP_CONTEXT_KEY_UPDATE`](wesp-context-key-management.md#esp_context_key_update) | The structure `ESP_CONTEXT_KEY_UPDATE` describes a context key update. |
| [`ESP_DESKTOP_CONFIG`](wesp-other-event-objects.md#esp_desktop_config) | The configuration structure for a desktop event object is `ESP_DESKTOP_CONFIG`. |
| [`ESP_DESKTOP_INFO`](wesp-other-event-objects.md#esp_desktop_info) | The structure `ESP_DESKTOP_INFO` specifies information for a desktop. |
| [`ESP_DISK_CONFIG`](wesp-storage-objects.md#esp_disk_config) | The configuration structure for a disk event object is `ESP_DISK_CONFIG`. |
| [`ESP_DISK_INFO`](wesp-storage-objects.md#esp_disk_info) | The structure `ESP_DISK_INFO` specifies information for a disk. |
| [`ESP_EA_DESCRIPTOR`](wesp-common-value-types.md#esp_ea_descriptor) | The structure `ESP_EA_DESCRIPTOR` describes an extended attribute. |
| [`ESP_EA_LIST`](wesp-common-value-types.md#esp_ea_list) | The structure `ESP_EA_LIST` is used to describe a list of extended attributes. |
| [`ESP_EA_LIST_COMPARISON`](wesp-filter-domain-comparisons.md#esp_ea_list_comparison) | The structure `ESP_EA_LIST_COMPARISON` is used to compare an EA list. |
| [`ESP_EA_LIST_CONFIG`](wesp-rule-value-configuration.md#esp_ea_list_config) | The structure `ESP_EA_LIST_CONFIG` is used to configure an EA list value. |
| [`ESP_ECP_DESCRIPTOR`](wesp-event-shared-types.md#esp_ecp_descriptor) | The structure `ESP_ECP_DESCRIPTOR` describes an extra create parameter. |
| [`ESP_ECP_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_ecp_descriptor_config) | The structure `ESP_ECP_DESCRIPTOR_CONFIG` is used to configure an ECP list descriptor value. |
| [`ESP_ECP_LIST`](wesp-event-shared-types.md#esp_ecp_list) | The structure `ESP_ECP_LIST` is used to describe a list of extra create parameters. |
| [`ESP_ECP_LIST_COMPARISON`](wesp-filter-domain-comparisons.md#esp_ecp_list_comparison) | The structure `ESP_ECP_LIST_COMPARISON` is used to compare an ECP list. |
| [`ESP_ECP_LIST_CONFIG`](wesp-rule-value-configuration.md#esp_ecp_list_config) | The structure `ESP_ECP_LIST_CONFIG` is used to configure an ECP list value. |
| [`ESP_EVENT_CONFIG`](wesp-rule-configuration.md#esp_event_config) | The structure `ESP_EVENT_CONFIG` is used to set event configuration for a rule. |
| [`ESP_EVENT_MODIFY`](wesp-rule-event-modification.md#esp_event_modify) | The structure `ESP_EVENT_MODIFY` is used to describe modifications to make to event data if the rule is associated with matches. |
| [`ESP_EVENT_NOTIFICATION`](wesp-event-notifications.md#esp_event_notification) | The structure `ESP_EVENT_NOTIFICATION` represents an event notification. |
| [`ESP_EVENT_NOTIFICATION_DATA_V1`](wesp-event-notifications.md#esp_event_notification_data_v1) | The structure `ESP_EVENT_NOTIFICATION_DATA_V1` represents a version 1 event notification. |
| [`ESP_EVENT_OBJECT_CONFIG`](wesp-event-object-references.md#esp_event_object_config) | The structure `ESP_EVENT_OBJECT_CONFIG` is used to set configuration for an event object associated with a rule. |
| [`ESP_EVENT_OBJECT_INFO`](wesp-event-object-references.md#esp_event_object_info) | The structure `ESP_EVENT_OBJECT_INFO` specifies information for an event object. |
| [`ESP_EVENT_QUEUE_DESCRIPTOR`](wesp-event-queue-management.md#esp_event_queue_descriptor) | The structure `ESP_EVENT_QUEUE_DESCRIPTOR` is used to configure an event queue as part of calling the API `EspCreateEventQueue`. |
| [`ESP_FILE_CONFIG`](wesp-file-objects.md#esp_file_config) | The configuration structure for a file event object is `ESP_FILE_CONFIG`. |
| [`ESP_FILE_INFO`](wesp-file-objects.md#esp_file_info) | The structure `ESP_FILE_INFO` specifies information for a file. |
| [`ESP_FILE_OBJECT_CONFIG`](wesp-file-objects.md#esp_file_object_config) | The configuration structure for a file object event object is `ESP_FILE_OBJECT_CONFIG`. |
| [`ESP_FILE_OBJECT_INFO`](wesp-file-objects.md#esp_file_object_info) | The structure `ESP_FILE_OBJECT_INFO` specifies information for a file object. |
| [`ESP_FILE_STREAM_CONFIG`](wesp-file-objects.md#esp_file_stream_config) | The configuration structure for a file stream event object is `ESP_FILE_STREAM_CONFIG`. |
| [`ESP_FILE_STREAM_INFO`](wesp-file-objects.md#esp_file_stream_info) | The structure `ESP_FILE_STREAM_INFO` specifies information for a file stream. |
| [`ESP_FO_CLEANUP_CONFIG`](wesp-file-object-events.md#esp_fo_cleanup_config) | The structure `ESP_FO_CLEANUP_CONFIG` is used to configure a file cleanup event. |
| [`ESP_FO_CLEANUP_PARAMETERS`](wesp-file-object-events.md#esp_fo_cleanup_parameters) | The structure `ESP_FO_CLEANUP_PARAMETERS` contains the parameters associated with a file object cleanup event notification. |
| [`ESP_FO_CREATE_CONFIG`](wesp-file-object-events.md#esp_fo_create_config) | The structure `ESP_FO_CREATE_CONFIG` is used to configure a file object create event. |
| [`ESP_FO_CREATE_MODIFY`](wesp-file-object-events.md#esp_fo_create_modify) | The structure `ESP_FO_CREATE_MODIFY` is used to modify event data for the file object create event. |
| [`ESP_FO_CREATE_PARAMETERS`](wesp-file-object-events.md#esp_fo_create_parameters) | The structure `ESP_FO_CREATE_PARAMETERS` contains the parameters associated with a file object create event notification. |
| [`ESP_FO_OPEN_CONFIG`](wesp-file-object-events.md#esp_fo_open_config) | The structure `ESP_FO_OPEN_CONFIG` is used to configure a file object open event. |
| [`ESP_FO_OPEN_PARAMETERS`](wesp-file-object-events.md#esp_fo_open_parameters) | The structure `ESP_FO_OPEN_PARAMETERS` contains the parameters associated with a file object open event notification. |
| [`ESP_FO_READ_CONFIG`](wesp-file-object-events.md#esp_fo_read_config) | The structure `ESP_FO_READ_CONFIG` is used to configure a file object read event. |
| [`ESP_FO_READ_PARAMETERS`](wesp-file-object-events.md#esp_fo_read_parameters) | The structure `ESP_FO_READ_PARAMETERS` contains the parameters associated with a file object read event notification. |
| [`ESP_FO_TARGET_OBJECT_CONFIG`](wesp-file-objects.md#esp_fo_target_object_config) | The union `ESP_FO_TARGET_OBJECT_CONFIG` specifies configuration for the file object's target object. |
| [`ESP_FO_TARGET_OBJECT_INFO`](wesp-file-objects.md#esp_fo_target_object_info) | The union `ESP_FO_TARGET_OBJECT_INFO` specifies information for the file object's target object. |
| [`ESP_FO_WRITE_CONFIG`](wesp-file-object-events.md#esp_fo_write_config) | The structure `ESP_FO_WRITE_CONFIG` is used to configure a file object write event. |
| [`ESP_FO_WRITE_PARAMETERS`](wesp-file-object-events.md#esp_fo_write_parameters) | The structure `ESP_FO_WRITE_PARAMETERS` contains the parameters associated with a file object write event notification. |
| [`ESP_FS_CREATE_FILE_SECTION_CONFIG`](wesp-file-system-events.md#esp_fs_create_file_section_config) | The structure `ESP_FS_CREATE_FILE_SECTION_CONFIG` is used to configure a create file section event. |
| [`ESP_FS_CREATE_FILE_SECTION_PARAMETERS`](wesp-file-system-events.md#esp_fs_create_file_section_parameters) | The structure `ESP_FS_CREATE_FILE_SECTION_PARAMETERS` contains the parameters associated with a create file section event notification. |
| [`ESP_FS_FSCTL_FILE_CONFIG`](wesp-file-system-events.md#esp_fs_fsctl_file_config) | The structure `ESP_FS_FSCTL_FILE_CONFIG` is used to configure a file FSCTL event. |
| [`ESP_FS_FSCTL_FILE_PARAMETERS`](wesp-file-system-events.md#esp_fs_fsctl_file_parameters) | The structure `ESP_FS_FSCTL_FILE_PARAMETERS` contains the parameters associated with a file FSCTL event notification. |
| [`ESP_FS_LOCK_FILE_CONFIG`](wesp-file-system-events.md#esp_fs_lock_file_config) | The structure `ESP_FS_LOCK_FILE_CONFIG` is used to configure a lock file event. |
| [`ESP_FS_LOCK_FILE_PARAMETERS`](wesp-file-system-events.md#esp_fs_lock_file_parameters) | The structure `ESP_FS_LOCK_FILE_PARAMETERS` contains the parameters associated with a lock file event notification. |
| [`ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG`](wesp-file-system-events.md#esp_fs_query_directory_information_config) | The structure `ESP_FS_QUERY_DIRECTORY_INFORMATION_CONFIG` is used to configure a query directory information event. |
| [`ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS`](wesp-file-system-events.md#esp_fs_query_directory_information_parameters) | The structure `ESP_FS_QUERY_DIRECTORY_INFORMATION_PARAMETERS` contains the parameters associated with a query directory information event notification. |
| [`ESP_FS_QUERY_FILE_INFORMATION_CONFIG`](wesp-file-system-events.md#esp_fs_query_file_information_config) | The structure `ESP_FS_QUERY_FILE_INFORMATION_CONFIG` is used to configure a query file information event. |
| [`ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS`](wesp-file-system-events.md#esp_fs_query_file_information_parameters) | The structure `ESP_FS_QUERY_FILE_INFORMATION_PARAMETERS` contains the parameters associated with a query file information event notification. |
| [`ESP_FS_QUERY_OPEN_FILE_CONFIG`](wesp-file-system-events.md#esp_fs_query_open_file_config) | The structure `ESP_FS_QUERY_OPEN_FILE_CONFIG` is used to configure a query open file event. |
| [`ESP_FS_QUERY_OPEN_FILE_MODIFY`](wesp-file-system-events.md#esp_fs_query_open_file_modify) | The structure `ESP_FS_QUERY_OPEN_FILE_MODIFY` is used to modify event data for the query file open event. |
| [`ESP_FS_QUERY_OPEN_FILE_PARAMETERS`](wesp-file-system-events.md#esp_fs_query_open_file_parameters) | The structure `ESP_FS_QUERY_OPEN_FILE_PARAMETERS` contains the parameters associated with a query open file event notification. |
| [`ESP_FS_SET_EA_CONFIG`](wesp-file-system-events.md#esp_fs_set_ea_config) | The structure `ESP_FS_SET_EA_CONFIG` is used to configure a set EA event. |
| [`ESP_FS_SET_EA_PARAMETERS`](wesp-file-system-events.md#esp_fs_set_ea_parameters) | The structure `ESP_FS_SET_EA_PARAMETERS` contains the parameters associated with a set EA event notification. |
| [`ESP_FS_SET_FILE_INFORMATION_CONFIG`](wesp-file-system-events.md#esp_fs_set_file_information_config) | The structure `ESP_FS_SET_FILE_INFORMATION_CONFIG` is used to configure a set file information event. |
| [`ESP_FS_SET_FILE_INFORMATION_PARAMETERS`](wesp-file-system-events.md#esp_fs_set_file_information_parameters) | The structure `ESP_FS_SET_FILE_INFORMATION_PARAMETERS` contains the parameters associated with a set file information event notification. |
| [`ESP_FS_SET_FILE_SECURITY_CONFIG`](wesp-file-system-events.md#esp_fs_set_file_security_config) | The structure `ESP_FS_SET_FILE_SECURITY_CONFIG` is used to configure a set file security event. |
| [`ESP_FS_SET_FILE_SECURITY_PARAMETERS`](wesp-file-system-events.md#esp_fs_set_file_security_parameters) | The structure `ESP_FS_SET_FILE_SECURITY_PARAMETERS` contains the parameters associated with a set file security event notification. |
| [`ESP_FS_UNLOCK_FILE_CONFIG`](wesp-file-system-events.md#esp_fs_unlock_file_config) | The structure `ESP_FS_UNLOCK_FILE_CONFIG` is used to configure an unlock file event. |
| [`ESP_FS_UNLOCK_FILE_PARAMETERS`](wesp-file-system-events.md#esp_fs_unlock_file_parameters) | The structure `ESP_FS_UNLOCK_FILE_PARAMETERS` contains the parameters associated with an unlock file event notification. |
| [`ESP_INTEGER_COMPARISON`](wesp-filter-scalar-comparisons.md#esp_integer_comparison) | The structure `ESP_INTEGER_COMPARISON` is used to compare an integer value. |
| [`ESP_INTEGER_CONFIG`](wesp-rule-value-configuration.md#esp_integer_config) | The structure `ESP_INTEGER_CONFIG` is used to configure an integer value. |
| [`ESP_INTEGER_VALUE_SOURCE`](wesp-filter-scalar-comparisons.md#esp_integer_value_source) | The structure `ESP_INTEGER_VALUE_SOURCE` specifies the source of an integer value. |
| [`ESP_IO_OPERATION`](wesp-event-shared-types.md#esp_io_operation) | The structure `ESP_IO_OPERATION` represents an IO operation. |
| [`ESP_IO_OPERATION_CONFIG`](wesp-event-shared-types.md#esp_io_operation_config) | The structure `ESP_IO_OPERATION_CONFIG` is used to configure an IO operation value. |
| [`ESP_KTM_TRANSACTION_COMMIT_CONFIG`](wesp-transaction-events.md#esp_ktm_transaction_commit_config) | The structure `ESP_KTM_TRANSACTION_COMMIT_CONFIG` is used to configure a KTM transaction commit event. |
| [`ESP_KTM_TRANSACTION_COMMIT_PARAMETERS`](wesp-transaction-events.md#esp_ktm_transaction_commit_parameters) | The structure `ESP_KTM_TRANSACTION_COMMIT_PARAMETERS` contains the parameters associated with a KTM transaction commit event notification. |
| [`ESP_KTM_TRANSACTION_CONFIG`](wesp-other-event-objects.md#esp_ktm_transaction_config) | The configuration structure for a KTM transaction event object is `ESP_KTM_TRANSACTION_CONFIG`. |
| [`ESP_KTM_TRANSACTION_INFO`](wesp-other-event-objects.md#esp_ktm_transaction_info) | The structure `ESP_KTM_TRANSACTION_INFO` specifies information for a KTM transaction. |
| [`ESP_KTM_TRANSACTION_ROLLBACK_CONFIG`](wesp-transaction-events.md#esp_ktm_transaction_rollback_config) | The structure `ESP_KTM_TRANSACTION_ROLLBACK_CONFIG` is used to configure a KTM transaction rollback event. |
| [`ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS`](wesp-transaction-events.md#esp_ktm_transaction_rollback_parameters) | The structure `ESP_KTM_TRANSACTION_ROLLBACK_PARAMETERS` contains the parameters associated with a KTM transaction rollback event notification. |
| [`ESP_MAILSLOT_CONFIG`](wesp-other-event-objects.md#esp_mailslot_config) | The configuration structure for a mailslot event object is `ESP_MAILSLOT_CONFIG`. |
| [`ESP_MAILSLOT_CREATE_CONFIG`](wesp-mailslot-events.md#esp_mailslot_create_config) | The structure `ESP_MAILSLOT_CREATE_CONFIG` is used to configure a mailslot create event. |
| [`ESP_MAILSLOT_CREATE_PARAMETERS`](wesp-mailslot-events.md#esp_mailslot_create_parameters) | The structure `ESP_MAILSLOT_CREATE_PARAMETERS` contains the parameters associated with a mailslot create event notification. |
| [`ESP_MAILSLOT_INFO`](wesp-other-event-objects.md#esp_mailslot_info) | The structure `ESP_MAILSLOT_INFO` specifies information for a mailslot. |
| [`ESP_MEMORY_ADDRESS_BASIC`](wesp-common-value-types.md#esp_memory_address_basic) | The structure `ESP_MEMORY_ADDRESS_BASIC_QUERY` specifies information for a basic memory address query. |
| [`ESP_MEMORY_ADDRESS_BASIC_COMPARISON`](wesp-filter-domain-comparisons.md#esp_memory_address_basic_comparison) | The `ESP_MEMORY_ADDRESS_BASIC_COMPARISON` structure defines comparisons for a basic memory address query. |
| [`ESP_MEMORY_ADDRESS_BASIC_CONFIG`](wesp-rule-value-configuration.md#esp_memory_address_basic_config) | The structure `ESP_MEMORY_ADDRESS_BASIC_CONFIG` is used to configure a memory address basic query. |
| [`ESP_NETWORK_IP_ADDRESS`](wesp-common-value-types.md#esp_network_ip_address) | The structure `ESP_NETWORK_IP_ADDRESS` represents an IP address. |
| [`ESP_NETWORK_IP_ADDRESS_COMPARISON`](wesp-filter-domain-comparisons.md#esp_network_ip_address_comparison) | The structure `ESP_NETWORK_IP_ADDRESS_COMPARISON` is used to compare an IP address value. |
| [`ESP_NETWORK_IP_ADDRESS_CONFIG`](wesp-rule-value-configuration.md#esp_network_ip_address_config) | The structure `ESP_NETWORK_IP_ADDRESS_CONFIG` specifies configuration for a network IP address. |
| [`ESP_NETWORK_IP_ADDRESS_RANGE`](wesp-common-value-types.md#esp_network_ip_address_range) | The structure `ESP_NETWORK_IP_ADDRESS_RANGE` represents a range of IP addresses. |
| [`ESP_NETWORK_PORT_COMPARISON`](wesp-filter-domain-comparisons.md#esp_network_port_comparison) | The structure `ESP_NETWORK_PORT_COMPARISON` is used to compare a socket's network port. |
| [`ESP_NETWORK_PORT_CONFIG`](wesp-rule-value-configuration.md#esp_network_port_config) | The structure `ESP_NETWORK_PORT_CONFIG` specifies configuration for a network port. |
| [`ESP_NUMERICAL_TRANSFORM`](wesp-filter-comparison-types.md#esp_numerical_transform) | The structure `ESP_NUMERICAL_TRANSFORM` is used to represent a numerical transformation. |
| [`ESP_NUMERICAL_TRANSFORM_LIST`](wesp-filter-comparison-types.md#esp_numerical_transform_list) | The structure `ESP_NUMERICAL_TRANSFORM_LIST` is used to represent a numerical transform list. |
| [`ESP_OB_CREATE_HANDLE_CONFIG`](wesp-object-handle-events.md#esp_ob_create_handle_config) | The structure `ESP_OB_CREATE_HANDLE_CONFIG` is used to configure a create handle event. |
| [`ESP_OB_CREATE_HANDLE_MODIFY`](wesp-object-handle-events.md#esp_ob_create_handle_modify) | The structure `ESP_OB_CREATE_HANDLE_MODIFY` is used to modify event data for the OB create handle event. |
| [`ESP_OB_CREATE_HANDLE_PARAMETERS`](wesp-object-handle-events.md#esp_ob_create_handle_parameters) | The `ESP_OB_CREATE_HANDLE_PARAMETERS` struct is supplied as part of a create handle event notification. |
| [`ESP_OB_DUPLICATE_HANDLE_CONFIG`](wesp-object-handle-events.md#esp_ob_duplicate_handle_config) | The structure `ESP_OB_DUPLICATE_HANDLE_CONFIG` is used to configure a duplicate handle event. |
| [`ESP_OB_DUPLICATE_HANDLE_MODIFY`](wesp-object-handle-events.md#esp_ob_duplicate_handle_modify) | The structure `ESP_OB_DUPLICATE_HANDLE_MODIFY` is used to modify event data for the OB duplicate handle event. |
| [`ESP_OB_DUPLICATE_HANDLE_PARAMETERS`](wesp-object-handle-events.md#esp_ob_duplicate_handle_parameters) | The `ESP_OB_DUPLICATE_HANDLE_PARAMETERS` struct is supplied as part of a duplicate handle event notification. |
| [`ESP_PATH`](wesp-common-utilities.md#esp_path) | The structure `ESP_PATH` represents a path. |
| [`ESP_PATH_COMPARISON`](wesp-filter-string-comparisons.md#esp_path_comparison) | The structure `ESP_PATH_COMPARISON` is used to compare a path value. |
| [`ESP_PATH_CONFIG`](wesp-rule-value-configuration.md#esp_path_config) | The structure `ESP_PATH_CONFIG` is used to configure a path value. |
| [`ESP_PIPE_CONFIG`](wesp-other-event-objects.md#esp_pipe_config) | The configuration structure for a pipe event object is `ESP_PIPE_CONFIG`. |
| [`ESP_PIPE_CREATE_CONFIG`](wesp-pipe-events.md#esp_pipe_create_config) | The structure `ESP_PIPE_CREATE_CONFIG` is used to configure a pipe create event. |
| [`ESP_PIPE_CREATE_PARAMETERS`](wesp-pipe-events.md#esp_pipe_create_parameters) | The structure `ESP_PIPE_CREATE_PARAMETERS` contains the parameters associated with a pipe create event notification. |
| [`ESP_PIPE_INFO`](wesp-other-event-objects.md#esp_pipe_info) | The structure `ESP_PIPE_INFO` specifies information for a pipe. |
| [`ESP_PROCESS_CONFIG`](wesp-execution-objects.md#esp_process_config) | The configuration structure for a process event object is `ESP_PROCESS_CONFIG`. |
| [`ESP_PROCESS_CREATE_CONFIG`](wesp-process-events.md#esp_process_create_config) | The structure `ESP_PROCESS_CREATE_CONFIG` is used to configure a process create event. |
| [`ESP_PROCESS_CREATE_PARAMETERS`](wesp-process-events.md#esp_process_create_parameters) | The structure `ESP_PROCESS_CREATE_PARAMETERS` contains the parameters associated with a process create event notification. |
| [`ESP_PROCESS_INFO`](wesp-execution-objects.md#esp_process_info) | The structure `ESP_PROCESS_INFO` specifies information for a process. |
| [`ESP_PROCESS_LOAD_IMAGE_CONFIG`](wesp-process-events.md#esp_process_load_image_config) | The structure `ESP_PROCESS_LOAD_IMAGE_CONFIG` is used to configure a process load image event. |
| [`ESP_PROCESS_LOAD_IMAGE_PARAMETERS`](wesp-process-events.md#esp_process_load_image_parameters) | The structure `ESP_PROCESS_LOAD_IMAGE_PARAMETERS` contains the parameters associated with a process load image event notification. |
| [`ESP_PROCESS_TERMINATE_CONFIG`](wesp-process-events.md#esp_process_terminate_config) | The structure `ESP_PROCESS_TERMINATE_CONFIG` is used to configure a process terminate event. |
| [`ESP_PROCESS_TERMINATE_PARAMETERS`](wesp-process-events.md#esp_process_terminate_parameters) | The structure `ESP_PROCESS_TERMINATE_PARAMETERS` contains the parameters associated with a process terminate event notification. |
| [`ESP_PROPERTY`](wesp-property-queries.md#esp_property) | The structure `ESP_PROPERTY` stores the result of a property query. |
| [`ESP_PROPERTY_BINDING`](wesp-rule-configuration.md#esp_property_binding) | The structure `ESP_PROPERTY_BINDING` stores a binding key configuration for a property. |
| [`ESP_PROPERTY_QUERY`](wesp-property-queries.md#esp_property_query) | The structure `ESP_PROPERTY_QUERY` stores an array of queried properties. |
| [`ESP_REG_CREATE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_create_key_config) | The structure `ESP_REG_CREATE_KEY_CONFIG` is used to configure a registry create key event. |
| [`ESP_REG_CREATE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_create_key_parameters) | The structure `ESP_REG_CREATE_KEY_PARAMETERS` contains the parameters associated with a create key event notification. |
| [`ESP_REG_DATA_COMPARISON`](wesp-filter-domain-comparisons.md#esp_reg_data_comparison) | The structure `ESP_REG_DATA_COMPARISON` is used to compare registry data. |
| [`ESP_REG_DATA_CONFIG`](wesp-rule-value-configuration.md#esp_reg_data_config) | The structure `ESP_REG_DATA_CONFIG` is used to configure a registry data value. |
| [`ESP_REG_DELETE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_delete_key_config) | The structure `ESP_REG_DELETE_KEY_CONFIG` is used to configure a registry delete key event. |
| [`ESP_REG_DELETE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_delete_key_parameters) | The structure `ESP_REG_DELETE_KEY_PARAMETERS` contains the parameters associated with a delete key event notification. |
| [`ESP_REG_DELETE_VALUE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_delete_value_key_config) | The structure `ESP_REG_DELETE_VALUE_KEY_CONFIG` is used to configure a registry delete value key event. |
| [`ESP_REG_DELETE_VALUE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_delete_value_key_parameters) | The structure `ESP_REG_DELETE_VALUE_KEY_PARAMETERS` contains the parameters associated with a delete value key event notification. |
| [`ESP_REG_ENUM_KEY_CONFIG`](wesp-registry-events.md#esp_reg_enum_key_config) | The structure `ESP_REG_ENUM_KEY_CONFIG` is used to configure a registry enum key event. |
| [`ESP_REG_ENUM_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_enum_key_parameters) | The structure `ESP_REG_ENUM_KEY_PARAMETERS` contains the parameters associated with an enum key event notification. |
| [`ESP_REG_ENUM_VALUE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_enum_value_key_config) | The structure `ESP_REG_ENUM_VALUE_KEY_CONFIG` is used to configure a registry enum value key event. |
| [`ESP_REG_ENUM_VALUE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_enum_value_key_parameters) | The structure `ESP_REG_ENUM_VALUE_KEY_PARAMETERS` contains the parameters associated with an enum value key event notification. |
| [`ESP_REG_LOAD_KEY_CONFIG`](wesp-registry-events.md#esp_reg_load_key_config) | The structure `ESP_REG_LOAD_KEY_CONFIG` is used to configure a registry load key event. |
| [`ESP_REG_LOAD_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_load_key_parameters) | The structure `ESP_REG_LOAD_KEY_PARAMETERS` contains the parameters associated with a load key event notification. |
| [`ESP_REG_OPEN_KEY_CONFIG`](wesp-registry-events.md#esp_reg_open_key_config) | The structure `ESP_REG_OPEN_KEY_CONFIG` is used to configure a registry open key event. |
| [`ESP_REG_OPEN_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_open_key_parameters) | The structure `ESP_REG_OPEN_KEY_PARAMETERS` contains the parameters associated with an open key event notification. |
| [`ESP_REG_QUERY_KEY_CONFIG`](wesp-registry-events.md#esp_reg_query_key_config) | The structure `ESP_REG_QUERY_KEY_CONFIG` is used to configure a registry query key event. |
| [`ESP_REG_QUERY_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_query_key_parameters) | The structure `ESP_REG_QUERY_KEY_PARAMETERS` contains the parameters associated with a query key event notification. |
| [`ESP_REG_QUERY_VALUE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_query_value_key_config) | The structure `ESP_REG_QUERY_VALUE_KEY_CONFIG` is used to configure a registry query value key event. |
| [`ESP_REG_QUERY_VALUE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_query_value_key_parameters) | The structure `ESP_REG_QUERY_VALUE_KEY_PARAMETERS` contains the parameters associated with a query value key event notification. |
| [`ESP_REG_RENAME_KEY_CONFIG`](wesp-registry-events.md#esp_reg_rename_key_config) | The structure `ESP_REG_RENAME_KEY_CONFIG` is used to configure a registry rename key event. |
| [`ESP_REG_RENAME_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_rename_key_parameters) | The structure `ESP_REG_RENAME_KEY_PARAMETERS` contains the parameters associated with a rename key event notification. |
| [`ESP_REG_REPLACE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_replace_key_config) | The structure `ESP_REG_REPLACE_KEY_CONFIG` is used to configure a registry replace key event. |
| [`ESP_REG_REPLACE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_replace_key_parameters) | The structure `ESP_REG_REPLACE_KEY_PARAMETERS` contains the parameters associated with a replace key event notification. |
| [`ESP_REG_RESTORE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_restore_key_config) | The structure `ESP_REG_RESTORE_KEY_CONFIG` is used to configure a registry restore key event. |
| [`ESP_REG_RESTORE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_restore_key_parameters) | The structure `ESP_REG_RESTORE_KEY_PARAMETERS` contains the parameters associated with a restore key event notification. |
| [`ESP_REG_SAVE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_save_key_config) | The structure `ESP_REG_SAVE_KEY_CONFIG` is used to configure a registry save key event. |
| [`ESP_REG_SAVE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_save_key_parameters) | The structure `ESP_REG_SAVE_KEY_PARAMETERS` contains the parameters associated with a save key event notification. |
| [`ESP_REG_SET_KEY_SECURITY_CONFIG`](wesp-registry-events.md#esp_reg_set_key_security_config) | The structure `ESP_REG_SET_KEY_SECURITY_CONFIG` is used to configure a registry set key security event. |
| [`ESP_REG_SET_KEY_SECURITY_PARAMETERS`](wesp-registry-events.md#esp_reg_set_key_security_parameters) | The structure `ESP_REG_SET_KEY_SECURITY_PARAMETERS` contains the parameters associated with a set key security event notification. |
| [`ESP_REG_SET_VALUE_KEY_CONFIG`](wesp-registry-events.md#esp_reg_set_value_key_config) | The structure `ESP_REG_SET_VALUE_KEY_CONFIG` is used to configure a registry set value key event. |
| [`ESP_REG_SET_VALUE_KEY_PARAMETERS`](wesp-registry-events.md#esp_reg_set_value_key_parameters) | The structure `ESP_REG_SET_VALUE_KEY_PARAMETERS` contains the parameters associated with a set value key event notification. |
| [`ESP_REG_VALUE_QUERY`](wesp-registry-events.md#esp_reg_value_query) | The structure `ESP_REG_VALUE_QUERY` is used to represent a registry value query. |
| [`ESP_REG_VALUE_QUERY_CONFIG`](wesp-rule-value-configuration.md#esp_reg_value_query_config) | The structure `ESP_REG_VALUE_QUERY_CONFIG` is used to configure a `ESP_REG_VALUE_QUERY` value. |
| [`ESP_REGISTRY_KEY_CONFIG`](wesp-other-event-objects.md#esp_registry_key_config) | The configuration structure for a registry key event object is `ESP_REGISTRY_KEY_CONFIG`. |
| [`ESP_REGISTRY_KEY_INFO`](wesp-other-event-objects.md#esp_registry_key_info) | The structure `ESP_REGISTRY_KEY_INFO` specifies information for a registry key. |
| [`ESP_REGISTRY_KEY_OBJECT_CONFIG`](wesp-other-event-objects.md#esp_registry_key_object_config) | The configuration structure for a registry key object event object is `ESP_REGISTRY_KEY_OBJECT_CONFIG`. |
| [`ESP_REGISTRY_KEY_OBJECT_INFO`](wesp-other-event-objects.md#esp_registry_key_object_info) | The structure `ESP_REGISTRY_KEY_OBJECT_INFO` specifies information for a registry key object. |
| [`ESP_REMOTE_CLIENT`](wesp-event-shared-types.md#esp_remote_client) | The structure `ESP_REMOTE_CLIENT` is used to represent a remote client. |
| [`ESP_REMOTE_CLIENT_CONFIG`](wesp-rule-value-configuration.md#esp_remote_client_config) | The structure `ESP_REMOTE_CLIENT_CONFIG` is used to configure a remote client structure. |
| [`ESP_RULE_CONFIG`](wesp-rule-configuration.md#esp_rule_config) | The structure `ESP_RULE_CONFIG` describes configuration for a rule. |
| [`ESP_RULE_CONFIG_EXTENSION`](wesp-rule-configuration.md#esp_rule_config_extension) | Describes an extension to a WESP rule configuration. |
| [`ESP_RULE_DESCRIPTOR`](wesp-rule-management.md#esp_rule_descriptor) | The structure `ESP_RULE_DESCRIPTOR` describes a rule. |
| [`ESP_RULE_UPDATE_ENTRY`](wesp-rule-management.md#esp_rule_update_entry) | The structure `ESP_RULE_UPDATE_ENTRY` represents an update to a rule. |
| [`ESP_SECURITY_DESCRIPTOR_COMPARISON`](wesp-filter-security-comparisons.md#esp_security_descriptor_comparison) | The structure `ESP_SECURITY_DESCRIPTOR_COMPARISON` performs a security descriptor comparison. |
| [`ESP_SECURITY_DESCRIPTOR_CONFIG`](wesp-rule-value-configuration.md#esp_security_descriptor_config) | The structure `ESP_SECURITY_DESCRIPTOR_CONFIG` is used to configure a security descriptor value. |
| [`ESP_SID_COMPARISON`](wesp-filter-security-comparisons.md#esp_sid_comparison) | The structure `ESP_SID_COMPARISON` is used to compare against a SID value. |
| [`ESP_SID_CONFIG`](wesp-rule-value-configuration.md#esp_sid_config) | The structure `ESP_SID_CONFIG` is used to configure a SID value. |
| [`ESP_STRING_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_comparison) | The structure `ESP_STRING_COMPARISON` is used to compare a string value. |
| [`ESP_STRING_CONFIG`](wesp-rule-value-configuration.md#esp_string_config) | The structure `ESP_STRING_CONFIG` is used to configure a string value. |
| [`ESP_STRING_LIST`](wesp-common-utilities.md#esp_string_list) | The structure `ESP_STRING_LIST` represents a list of strings. |
| [`ESP_STRING_LIST_COMPARISON`](wesp-filter-string-comparisons.md#esp_string_list_comparison) | The structure `ESP_STRING_LIST_COMPARISON` is used to compare against a list of strings. |
| [`ESP_STRING_VALUE_SOURCE`](wesp-filter-string-comparisons.md#esp_string_value_source) | The structure `ESP_STRING_VALUE_SOURCE` specifies the source of a string value. |
| [`ESP_THREAD_CONFIG`](wesp-execution-objects.md#esp_thread_config) | The configuration structure for a thread event object is `ESP_THREAD_CONFIG`. |
| [`ESP_THREAD_CREATE_CONFIG`](wesp-thread-events.md#esp_thread_create_config) | The structure `ESP_THREAD_CREATE_CONFIG` is used to configure a thread create event. |
| [`ESP_THREAD_CREATE_PARAMETERS`](wesp-thread-events.md#esp_thread_create_parameters) | The structure `ESP_THREAD_CREATE_PARAMETERS` contains the parameters associated with a thread create event notification. |
| [`ESP_THREAD_INFO`](wesp-execution-objects.md#esp_thread_info) | The structure `ESP_THREAD_INFO` specifies information for a thread. |
| [`ESP_THREAD_START_CONFIG`](wesp-thread-events.md#esp_thread_start_config) | The structure `ESP_THREAD_START_CONFIG` is used to configure a thread start event. |
| [`ESP_THREAD_START_PARAMETERS`](wesp-thread-events.md#esp_thread_start_parameters) | The structure `ESP_THREAD_START_PARAMETERS` contains the parameters associated with a thread start event notification. |
| [`ESP_THREAD_TERMINATE_CONFIG`](wesp-thread-events.md#esp_thread_terminate_config) | The structure `ESP_THREAD_TERMINATE_CONFIG` is used to configure a thread terminate event. |
| [`ESP_THREAD_TERMINATE_PARAMETERS`](wesp-thread-events.md#esp_thread_terminate_parameters) | The structure `ESP_THREAD_TERMINATE_PARAMETERS` contains the parameters associated with a thread terminate event notification. |
| [`ESP_TOKEN_CONFIG`](wesp-execution-objects.md#esp_token_config) | The configuration structure for a token event object is `ESP_TOKEN_CONFIG`. |
| [`ESP_TOKEN_GROUPS_COMPARISON`](wesp-filter-security-comparisons.md#esp_token_groups_comparison) | The structure `ESP_TOKEN_GROUPS_COMPARISON` is used to compare against token groups. |
| [`ESP_TOKEN_INFO`](wesp-execution-objects.md#esp_token_info) | The structure `ESP_TOKEN_INFO` specifies information for a token. |
| [`ESP_TOKEN_PRIVILEGES_COMPARISON`](wesp-filter-security-comparisons.md#esp_token_privileges_comparison) | The structure `ESP_TOKEN_PRIVILEGES_COMPARISON` is used to compare against token privileges. |
| [`ESP_UNICODE_STRING`](wesp-common-utilities.md#esp_unicode_string) | The structure `ESP_UNICODE_STRING` represents a counted unicode string. |
| [`ESP_VARIANT_VALUE`](wesp-property-queries.md#esp_variant_value) | `ESP_VARIANT_VALUE` contains a property value. |
| [`ESP_VOLUME_CONFIG`](wesp-storage-objects.md#esp_volume_config) | The configuration structure for a volume event object is `ESP_VOLUME_CONFIG`. |
| [`ESP_VOLUME_DISMOUNT_CONFIG`](wesp-volume-events.md#esp_volume_dismount_config) | The structure `ESP_VOLUME_DISMOUNT_CONFIG` is used to configure a volume dismount event. |
| [`ESP_VOLUME_DISMOUNT_PARAMETERS`](wesp-volume-events.md#esp_volume_dismount_parameters) | The structure `ESP_VOLUME_DISMOUNT_PARAMETERS` contains the parameters associated with a volume dismount event notification. |
| [`ESP_VOLUME_FSCTL_CONFIG`](wesp-volume-events.md#esp_volume_fsctl_config) | The structure `ESP_VOLUME_FSCTL_CONFIG` is used to configure a volume FSCTL event. |
| [`ESP_VOLUME_FSCTL_PARAMETERS`](wesp-volume-events.md#esp_volume_fsctl_parameters) | The structure `ESP_VOLUME_FSCTL_PARAMETERS` contains the parameters associated with a volume FSCTL event notification. |
| [`ESP_VOLUME_INFO`](wesp-storage-objects.md#esp_volume_info) | The structure `ESP_VOLUME_INFO` specifies information for a volume. |
| [`ESP_VOLUME_MOUNT_CONFIG`](wesp-volume-events.md#esp_volume_mount_config) | The structure `ESP_VOLUME_MOUNT_CONFIG` is used to configure a volume mount event. |
| [`ESP_VOLUME_MOUNT_PARAMETERS`](wesp-volume-events.md#esp_volume_mount_parameters) | The structure `ESP_VOLUME_MOUNT_PARAMETERS` contains the parameters associated with a volume mount event notification. |

### Constants and handles

| API | Description |
| --- | --- |
| [`ESP_CLIENT`](wesp-clients.md#esp_client) | Identifies a connection to a registered WESP client. |
| [`ESP_CLIENT_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_client_property_id_context_key) | Builds a context-key property ID for the client property namespace. |
| [`ESP_COLLECTION`](wesp-collection-management.md#esp_collection) | Identifies a WESP collection. |
| [`ESP_CONSTANT_UNICODE_STRING`](wesp-common-utilities.md#esp_constant_unicode_string) | The macro `ESP_CONSTANT_UNICODE_STRING` declares an `ESP_UNICODE_STRING` from a constant string. |
| [`ESP_DESKTOP_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_desktop_property_id_context_key) | Builds a context-key property ID for the desktop property namespace. |
| [`ESP_DISK_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_disk_property_id_context_key) | Builds a context-key property ID for the disk property namespace. |
| [`ESP_EVENT_OBJECT`](wesp-event-object-references.md#esp_event_object) | Identifies a WESP event object. |
| [`ESP_EVENT_OBJECT_REF`](wesp-event-object-references.md#esp_event_object_ref) | Identifies a reference to a WESP event object. |
| [`ESP_EVENT_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_event_property_id_context_key) | Builds a context-key property ID for the event property namespace. |
| [`ESP_EVENT_QUEUE`](wesp-event-queue-management.md#esp_event_queue) | Identifies a WESP event queue. |
| [`ESP_FILE_OBJECT_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_file_object_property_id_context_key) | Builds a context-key property ID for the file object property namespace. |
| [`ESP_FILE_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_file_property_id_context_key) | Builds a context-key property ID for the file property namespace. |
| [`ESP_FILE_STREAM_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_file_stream_property_id_context_key) | Builds a context-key property ID for the file stream property namespace. |
| [`ESP_FILTER`](wesp-filter-creation.md#esp_filter) | Identifies a WESP filter. |
| [`ESP_KTM_TRANSACTION_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_ktm_transaction_property_id_context_key) | Builds a context-key property ID for the ktm transaction property namespace. |
| [`ESP_MAILSLOT_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_mailslot_property_id_context_key) | Builds a context-key property ID for the mailslot property namespace. |
| [`ESP_PIPE_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_pipe_property_id_context_key) | Builds a context-key property ID for the pipe property namespace. |
| [`ESP_PROCESS_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_process_property_id_context_key) | Builds a context-key property ID for the process property namespace. |
| [`ESP_REGISTRY_KEY_OBJECT_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_registry_key_object_property_id_context_key) | Builds a context-key property ID for the registry key object property namespace. |
| [`ESP_REGISTRY_KEY_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_registry_key_property_id_context_key) | Builds a context-key property ID for the registry key property namespace. |
| [`ESP_RULE`](wesp-rule-management.md#esp_rule) | Identifies a WESP rule. |
| [`ESP_THREAD_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_thread_property_id_context_key) | Builds a context-key property ID for the thread property namespace. |
| [`ESP_TOKEN_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_token_property_id_context_key) | Builds a context-key property ID for the token property namespace. |
| [`ESP_VOLUME_PROPERTY_ID_CONTEXT_KEY`](wesp-context-key-property-macros.md#esp_volume_property_id_context_key) | Builds a context-key property ID for the volume property namespace. |
