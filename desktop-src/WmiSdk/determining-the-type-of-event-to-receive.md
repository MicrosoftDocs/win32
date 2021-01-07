---
description: 'Before you register to receive an event, you must determine the types of events to receive: intrinsic or extrinsic.'
ms.assetid: 46cdfcfa-42c6-4169-bc4d-725867224889
ms.tgt_platform: multiple
title: Determining the Type of Event to Receive
ms.topic: article
ms.date: 05/31/2018
---

# Determining the Type of Event to Receive

Before you register to receive an event, you must determine the types of events to receive: [intrinsic](#intrinsic-events) or [extrinsic](#extrinsic-events). For more information about how to receive events, see [Receiving a WMI Event](receiving-a-wmi-event.md). For more information about providing events, see [Developing a WMI Provider](developing-a-wmi-provider.md) and [Writing an Event Provider](writing-an-event-provider.md). For more information about the security concerns for receiving and providing events, see [Securing WMI Events.](securing-wmi-events.md)

## Intrinsic Events

An intrinsic event is an event that occurs in response to a change in the standard WMI data model. Each intrinsic event class represents a specific type of change and occurs when WMI or a provider creates, deletes, or modifies a namespace, class, or class instance. For example, the creation of a [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) instance would result in an [**\_\_InstanceCreationEvent**](--instancecreationevent.md) instance.

WMI creates intrinsic events for objects stored in the WMI repository. A provider generates intrinsic events for dynamic classes, but WMI can create an instance for a dynamic class if no provider is available. WMI uses polling to detect the changes. The following table lists the system classes that WMI uses to report intrinsic events.



| System class                                                           | Description                                                                                                                                                                                             |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**\_\_ClassCreationEvent**](--classcreationevent.md)                 | Notifies a consumer when a class is created.                                                                                                                                                            |
| [**\_\_ClassDeletionEvent**](--classdeletionevent.md)                 | Notifies a consumer when a class is deleted.                                                                                                                                                            |
| [**\_\_ClassModificationEvent**](--classmodificationevent.md)         | Notifies a consumer when a class is modified.                                                                                                                                                           |
| [**\_\_InstanceCreationEvent**](--instancecreationevent.md)           | Notifies a consumer when a class instance is created.                                                                                                                                                   |
| [**\_\_InstanceOperationEvent**](--instanceoperationevent.md)         | Notifies a consumer when any instance event occurs, such as creation, deletion, or modification of the instance. You can use this class in queries to get all types events associated with an instance. |
| [**\_\_InstanceDeletionEvent**](--instancedeletionevent.md)           | Notifies a consumer when an instance is deleted.                                                                                                                                                        |
| [**\_\_InstanceModificationEvent**](--instancemodificationevent.md)   | Notifies a consumer when an instance is modified.                                                                                                                                                       |
| [**\_\_NamespaceCreationEvent**](--namespacecreationevent.md)         | Notifies a consumer when a namespace is created.                                                                                                                                                        |
| [**\_\_NamespaceDeletionEvent**](--namespacedeletionevent.md)         | Notifies a consumer when a namespace is deleted.                                                                                                                                                        |
| [**\_\_NamespaceModificationEvent**](--namespacemodificationevent.md) | Notifies a consumer when a namespace is modified.                                                                                                                                                       |
| [**\_\_ConsumerFailureEvent**](--consumerfailureevent.md)             | Notifies a consumer when some other event is dropped due to a failure on the part of an event consumer.                                                                                                 |
| [**\_\_EventDroppedEvent**](--eventdroppedevent.md)                   | Notifies a consumer when some other event is dropped instead of being delivered to the requesting event consumer.                                                                                       |
| [**\_\_EventQueueOverflowEvent**](--eventqueueoverflowevent.md)       | Notifies a consumer when an event is dropped as a result of a delivery queue overflow.                                                                                                                  |
| [**\_\_MethodInvocationEvent**](--methodinvocationevent.md)           | Notifies a consumer when a method call event occurs.                                                                                                                                                    |



 

## Extrinsic Events

An extrinsic event is a predefined occurrence that cannot be linked directly to changes in the WMI data model. Therefore, WMI enables an event provider to define an event class that describes the event. For example, an event that describes a computer switching to stand-by mode is an extrinsic event. A provider derives an extrinsic event from the [**\_\_ExtrinsicEvent**](--extrinsicevent.md) system class, which is a subclass of the [**\_\_Event**](--event.md) system class. The [System Registry](/previous-versions/windows/desktop/regprov/system-registry-provider) and [SNMP](snmp-provider.md) providers define extrinsic event classes, such as **RegistryKeyChangeEvent**, which notifies a consumer when a registry key is changed. For more information, see [Registering for System Registry Events](registering-for-system-registry-events.md) and [Writing an Event Provider](writing-an-event-provider.md).

In the following example, an event provider is reporting security violations to one or more buildings. The following class might be defined for the extrinsic event representing a security violation.

``` syntax
class SecurityViolationEvent : __ExtrinsicEvent
{
   string Building;           // building where violation occurred
   sint32 EntranceNumber;     // entrance where violation occurred
   datetime TimeOfDetection;  // date and time of violation
}
```

To receive the security violation notifications, a consumer registers for the SecurityViolationEvent event type. Unless otherwise specified, a consumer receives notification of all security violations during all time periods and in all buildings. The event class also contains information that consumers can use to ask for more specific events.

In the following example, the query registers the consumer for security violation events in building 24 only.

`SELECT * FROM SecurityViolationEvent WHERE Building = 24;`

 

 
