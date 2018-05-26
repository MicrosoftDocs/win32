---
title: S
description: A C D E F H I K L M N O P Q R T W
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 781d0119-3ced-4f04-ba3f-6e291c04605f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# S

[A](gloss-a.md) [C](gloss-c.md) [D](gloss-d.md) [E](gloss-e.md) [F](gloss-f.md) [H](gloss-h.md) [I](gloss-i.md) [K](gloss-k.md) [L](gloss-l.md) [M](gloss-m.md) [N](gloss-n.md) [O](gloss-o.md) [P](gloss-p.md) [Q](gloss-q.md) [R](gloss-r.md) [T](gloss-t.md) [W](gloss-w.md)

<dl> <dt>

<span id="wmi_v2.gloss_schema"></span><span id="WMI_V2.GLOSS_SCHEMA"></span>**schema**
</dt> <dd>

A collection of class definitions that describe [*managed objects*](gloss-m.md#wmi-v2-gloss-managed-object) in a specific environment.

</dd> <dt>

<span id="wmi_v2.gloss_security_descriptor"></span><span id="WMI_V2.GLOSS_SECURITY_DESCRIPTOR"></span>**security descriptor**
</dt> <dd>

A data structure that contains the security information for a securable object, such as a share, file, sink, or event filter.

</dd> <dt>

<span id="wmi_v2.gloss_security_identifier"></span><span id="WMI_V2.GLOSS_SECURITY_IDENTIFIER"></span>**security identifier (SID)**
</dt> <dd>

A data structure that identifies user, group, and computer accounts.

</dd> <dt>

<span id="wmi_v2.gloss_semi_synchronous"></span><span id="WMI_V2.GLOSS_SEMI_SYNCHRONOUS"></span>**semi synchronous**
</dt> <dd>

See *semisynchronous method*.

</dd> <dt>

<span id="wmi_v2.gloss_semi__synchronous"></span><span id="WMI_V2.GLOSS_SEMI__SYNCHRONOUS"></span>**semi-synchronous**
</dt> <dd>

See *semisynchronous method*.

</dd> <dt>

<span id="wmi_v2.gloss_semisynchronous"></span><span id="WMI_V2.GLOSS_SEMISYNCHRONOUS"></span>**semisynchronous method**
</dt> <dd>

A method call that returns immediately and enables the application or script to enumerate the returned objects as a collection.

</dd> <dt>

<span id="gloss_servicesid"></span><span id="GLOSS_SERVICESID"></span>**Service SID**
</dt> <dd>

A unique *SID* that is created for each security context; that is, one for "LocalService" and one for "NetworkService". Only the *service SID* has permissions to resources, like threads and events, which are created by the WMI Provider Host Process (wmiprvse.exe).

</dd> <dt>

<span id="wmi_v2.gloss_sid"></span><span id="WMI_V2.GLOSS_SID"></span>**SID**
</dt> <dd>

See *security identifier*.

</dd> <dt>

<span id="wmi_v2.gloss_singleton_class"></span><span id="WMI_V2.GLOSS_SINGLETON_CLASS"></span>**singleton class**
</dt> <dd>

A WMI class that supports a single instance.

</dd> <dt>

<span id="wmi_v2.gloss_sink"></span><span id="WMI_V2.GLOSS_SINK"></span>**sink**
</dt> <dd>

A COM object that acts as the physical delivery destination for the results of an asynchronous operation or an event notification. A sink implemented by a [*permanent consumer*](gloss-p.md#wmi-v2-gloss-permanent-consumer) supports the [**IWbemUnboundObjectSink**](https://msdn.microsoft.com/library/aa392125) interface. A sink implemented by a [*temporary consumer*](gloss-t.md#wmi-v2-gloss-temporary-consumer) or applications making asynchronous calls supports the [**IWbemObjectSink**](https://msdn.microsoft.com/library/aa391787) interface.

Scripting clients can use the [**SWbemSink**](https://msdn.microsoft.com/library/aa393877) object and events, such as [**OnObjectReady**](https://msdn.microsoft.com/library/aa393881), to receive callbacks resulting from asynchronous calls.

</dd> <dt>

<span id="wmi_v2.gloss_standard_consumer"></span><span id="WMI_V2.GLOSS_STANDARD_CONSUMER"></span>**standard consumer**
</dt> <dd>

A preinstalled [*permanent consumers*](gloss-p.md#wmi-v2-gloss-permanent-consumer) that performs an action, such as sending an email message or writing to a log when configured by a [*Managed Object Format (MOF)*](gloss-m.md#wmi-v2-gloss-managed-object-format) file or a script.

</dd> <dt>

<span id="wmi_v2.gloss_standard_provider"></span><span id="WMI_V2.GLOSS_STANDARD_PROVIDER"></span>**standard provider**
</dt> <dd>

A [*provider*](gloss-p.md#wmi-v2-gloss-provider) that is built into WMI, which is different from a third-party or custom provider.

</dd> <dt>

<span id="wmi_v2.gloss_standard_qualifier"></span><span id="WMI_V2.GLOSS_STANDARD_QUALIFIER"></span>**standard qualifier**
</dt> <dd>

A [*qualifier*](gloss-q.md#wmi-v2-gloss-qualifier) that the [*CIM Object Manager*](gloss-c.md#wmi-v2-gloss-cim-object-manager) automatically attaches to a class, instance, property, method, or parameter of a method.

</dd> <dt>

<span id="wmi_v2.gloss_standard_schema"></span><span id="WMI_V2.GLOSS_STANDARD_SCHEMA"></span>**standard schema**
</dt> <dd>

A common conceptual framework that organizes and relates the classes that represent the current operational state of a system, network, or application. The [*Distributed Management Task Force (DMTF)*](gloss-d.md#wmi-v2-gloss-distributed-management-task-force) defines the standard schema in the [*Common Information Model (CIM)*](gloss-c.md#wmi-v2-gloss-common-information-model).

</dd> <dt>

<span id="wmi_v2.gloss_static_class"></span><span id="WMI_V2.GLOSS_STATIC_CLASS"></span>**static class**
</dt> <dd>

A CIM class definition that rarely changes, and is stored in the [*CIM repository*](gloss-c.md#wmi-v2-gloss-cim-repository) until it is explicitly deleted. The [*CIM Object Manager*](gloss-c.md#wmi-v2-gloss-cim-object-manager) can provide a definition of a static class without a [*provider*](gloss-p.md#wmi-v2-gloss-provider). A static class can support either *static* or [*dynamic instances*](gloss-d.md#wmi-v2-gloss-dynamic-instance).

</dd> <dt>

<span id="wmi_v2.gloss_static_instance"></span><span id="WMI_V2.GLOSS_STATIC_INSTANCE"></span>**static instance**
</dt> <dd>

An instance of a CIM class that is persistently stored in the [*CIM repository*](gloss-c.md#wmi-v2-gloss-cim-repository) and remains valid until explicitly deleted, even across system restarts.

</dd> <dt>

<span id="wmi_v2.gloss_static_method"></span><span id="WMI_V2.GLOSS_STATIC_METHOD"></span>**static method**
</dt> <dd>

A method defined in a CIM class that is executed by retrieving the class definition instead of retrieving an instance of the class.

</dd> <dt>

<span id="wmi_v2.gloss_subschema"></span><span id="WMI_V2.GLOSS_SUBSCHEMA"></span>**subschema**
</dt> <dd>

A part of a *schema* that is owned by a specific organization. The [*Win32schema*](gloss-w.md#wmi-v2-gloss-win32-schema) is an example of a subschema.

</dd> <dt>

<span id="wmi_v2.gloss_system_class"></span><span id="WMI_V2.GLOSS_SYSTEM_CLASS"></span>**system class**
</dt> <dd>

A class that the [*CIM Object Manager*](gloss-c.md#wmi-v2-gloss-cim-object-manager) defines to support core features such as event notification, security, and localization. A system class is automatically defined in each [*namespace*](gloss-n.md#wmi-v2-gloss-namespace). A system class derives from the abstract base class [**\_\_SystemClass**](https://msdn.microsoft.com/library/aa394675).

</dd> <dt>

<span id="wmi_v2.gloss_system_monitor"></span><span id="WMI_V2.GLOSS_SYSTEM_MONITOR"></span>**System Monitor**
</dt> <dd>

A utility that is the GUI for Performance Monitoring.

</dd> <dt>

<span id="wmi_v2.gloss_system_property"></span><span id="WMI_V2.GLOSS_SYSTEM_PROPERTY"></span>**system property**
</dt> <dd>

A property that the [*CIM Object Manager*](gloss-c.md#wmi-v2-gloss-cim-object-manager) defines to provide information that applies to each class, for example, name, derivation, and [*namespace*](gloss-n.md#wmi-v2-gloss-namespace).

</dd> </dl>

 

 




