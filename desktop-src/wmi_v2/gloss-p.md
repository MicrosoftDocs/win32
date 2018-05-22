---
title: P
description: A C D E F G H I K L M N O Q R S T W
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '25e45993-0d08-46cd-a8b9-e430a3fa242a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# P

[A](gloss-a.md) [C](gloss-c.md) [D](gloss-d.md) [E](gloss-e.md) [F](gloss-f.md) G [H](gloss-h.md) [I](gloss-i.md) [K](gloss-k.md) [L](gloss-l.md) [M](gloss-m.md) [N](gloss-n.md) [O](gloss-o.md) [Q](gloss-q.md) [R](gloss-r.md) [S](gloss-s.md) [T](gloss-t.md) [W](gloss-w.md)

<dl> <dt>

<span id="wmi_v2.gloss_performance_counter"></span><span id="WMI_V2.GLOSS_PERFORMANCE_COUNTER"></span>**performance counter**
</dt> <dd>

A property in a performance class that is derived from [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/aa394299) that stores performance data.

</dd> <dt>

<span id="wmi_v2.gloss_performance_object"></span><span id="WMI_V2.GLOSS_PERFORMANCE_OBJECT"></span>**performance object**
</dt> <dd>

An object in a performance library that stores data in counters. These objects are visible in the [*System Monitor*](gloss-s.md#wmi-v2-gloss-system-monitor) utility. Examples are Cache and Logical Disk objects. When transferred into WMI by the [*ADAP*](gloss-a.md#wmi-v2-gloss-auto-discovery-auto-purge) process, each object becomes two WMI performance classes. One class, containing raw data, derives from [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/aa394299). The other class derives from [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/aa394253) and contains the same data visible in System Monitor as calculated by the Cooked Counter provider.

</dd> <dt>

<span id="wmi_v2.gloss_permanent_consumer"></span><span id="WMI_V2.GLOSS_PERMANENT_CONSUMER"></span>**permanent consumer**
</dt> <dd>

An [*event consumer*](gloss-e.md#wmi-v2-gloss-event-consumer) whose registration lasts until it is explicitly canceled. Also see [*temporary consumer*](gloss-t.md#wmi-v2-gloss-temporary-consumer).

</dd> <dt>

<span id="wmi_v2.gloss_physical_consumer"></span><span id="WMI_V2.GLOSS_PHYSICAL_CONSUMER"></span>**physical consumer**
</dt> <dd>

A COM object that is implemented by an [*event consumer provider*](gloss-e.md#wmi-v2-gloss-event-consumer-provider) that includes a [*sink*](gloss-s.md#wmi-v2-gloss-sink) for receiving event notifications.

</dd> <dt>

<span id="wmi_v2.gloss_property"></span><span id="WMI_V2.GLOSS_PROPERTY"></span>**property**
</dt> <dd>

A name/value pair that describes a unit of data for a class. Property values must have a valid [*Managed Object Format (MOF)*](gloss-m.md#wmi-v2-gloss-managed-object-format) data type. Also see [*reference property*](gloss-r.md#wmi-v2-gloss-reference-property).

</dd> <dt>

<span id="wmi_v2.gloss_property_provider"></span><span id="WMI_V2.GLOSS_PROPERTY_PROVIDER"></span>**property provider**
</dt> <dd>

A COM server that supports the retrieval and modification of WMI properties. Property providers implement the [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) and [**IWbemPropertyProvider**](https://msdn.microsoft.com/library/aa391846) interfaces.

</dd> <dt>

<span id="wmi_v2.gloss_provider"></span><span id="WMI_V2.GLOSS_PROVIDER"></span>**provider**
</dt> <dd>

A COM server that communicates with managed objects to access data and event notifications, such as the registry or an SNMP device. Providers forward this data to the [*CIM Object Manager*](gloss-c.md#wmi-v2-gloss-cim-object-manager) for integration and interpretation.

</dd> <dt>

<span id="wmi_v2.gloss_provider_method"></span><span id="WMI_V2.GLOSS_PROVIDER_METHOD"></span>**provider method**
</dt> <dd>

A method that a WMI *provider* implements.

</dd> </dl>

 

 




