---
title: E
description: A C D F H I K L M N O P Q R S T W
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d2e28e01-645e-442a-8b22-f5450807aca8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# E

[A](gloss-a.md) [C](gloss-c.md) [D](gloss-d.md) [F](gloss-f.md) [H](gloss-h.md) [I](gloss-i.md) [K](gloss-k.md) [L](gloss-l.md) [M](gloss-m.md) [N](gloss-n.md) [O](gloss-o.md) [P](gloss-p.md) [Q](gloss-q.md) [R](gloss-r.md) [S](gloss-s.md) [T](gloss-t.md) [W](gloss-w.md)

<dl> <dt>

<span id="wmi_v2.gloss_event_class"></span><span id="WMI_V2.GLOSS_EVENT_CLASS"></span>**event class**
</dt> <dd>

A WMI class that *event consumers* can subscribe to by an *event query*. The class reports a specific type of occurrence. For example, the [**Win32\_ProcessStopTrace**](https://msdn.microsoft.com/library/aa394376) class reports that a specific process has stopped.

</dd> <dt>

<span id="wmi_v2.gloss_event_consumer"></span><span id="WMI_V2.GLOSS_EVENT_CONSUMER"></span>**event consumer**
</dt> <dd>

A recipient of notifications that report an occurrence of an event. An event consumer is either [*temporary*](https://www.bing.com/search?q=*temporary*) or [*permanent*](https://www.bing.com/search?q=*permanent*).

</dd> <dt>

<span id="wmi_v2.gloss_event_consumer_provider"></span><span id="WMI_V2.GLOSS_EVENT_CONSUMER_PROVIDER"></span>**event consumer provider**
</dt> <dd>

A provider that determines which permanent event consumer handles a given event. An event consumer provider is registered with WMI by an instance of [**\_\_EventConsumerProviderRegistration**](https://msdn.microsoft.com/library/aa394637), which contains a list of the [*logical consumer*](https://www.bing.com/search?q=*logical consumer*) classes that the event consumer provider supports. An event consumer provider is a COM server that maps [*physical consumers*](https://www.bing.com/search?q=*physical consumers*) to *logical consumers*. An event consumer provider supports the [**IWbemEventConsumerProvider**](https://msdn.microsoft.com/library/aa391489) interface and is a component of the permanent consumer architecture.

</dd> <dt>

<span id="wmi_v2.gloss_event_filter"></span><span id="WMI_V2.GLOSS_EVENT_FILTER"></span>**event filter**
</dt> <dd>

An instance of the [**\_\_EventFilter**](https://msdn.microsoft.com/library/aa394639) system class that describes an event type and the conditions for delivering a notification. A consumer uses an event filter to register to receive notification of a specific type of event.

</dd> <dt>

<span id="wmi_v2.gloss_event_provider"></span><span id="WMI_V2.GLOSS_EVENT_PROVIDER"></span>**event provider**
</dt> <dd>

A WMI provider that monitors a source of events and notifies WMI when events occur. An event provider implements the [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) and [**IWbemEventProvider**](https://msdn.microsoft.com/library/aa391504) interfaces, and sometimes [**IWbemEventProviderQuerySink**](https://msdn.microsoft.com/library/aa391736).

</dd> <dt>

<span id="wmi_v2.gloss_event_query"></span><span id="WMI_V2.GLOSS_EVENT_QUERY"></span>**event query**
</dt> <dd>

A [*WMI Query Language*](https://www.bing.com/search?q=*WMI Query Language*) statement that event consumers use to register to receive notification of specific events. An event provider uses an event query to register to generate notifications of specific events.

</dd> <dt>

<span id="wmi_v2.gloss_extension_schema"></span><span id="WMI_V2.GLOSS_EXTENSION_SCHEMA"></span>**extension schema**
</dt> <dd>

The third layer of the [*CIM schema*](https://www.bing.com/search?q=*CIM schema*), which includes platform-specific extensions of the CIM schema such as Windows 2000, UNIX, and Exchange Server. Also see [*common model*](https://www.bing.com/search?q=*common model*) and core model.

</dd> <dt>

<span id="wmi_v2.gloss_extrinsic_event"></span><span id="WMI_V2.GLOSS_EXTRINSIC_EVENT"></span>**extrinsic event**
</dt> <dd>

An event notification from a provider. Most providers create an instance of an event class defined in the provider MOF files. An extrinsic event inherits from [**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646). For example, the [Event Log Provider](https://msdn.microsoft.com/library/aa390413) defines the event class [**Win32\_NTLogEvent**](https://msdn.microsoft.com/library/aa394226). Also see [*intrinsic event*](https://www.bing.com/search?q=*intrinsic event*).

</dd> </dl>

 

 




