---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 223cfe51-8b1d-4965-b7b1-acc3cd5619f0
ms.tgt_platform: multiple
title: S (WMI)
ms.topic: article
ms.date: 05/31/2018
---

# S (WMI)

[A](gloss-a.md) B [C](gloss-c.md) [D](gloss-d.md) [E](gloss-e.md) [F](gloss-f.md) G [H](gloss-h.md) [I](gloss-i.md) J [K](gloss-k.md) [L](gloss-l.md) [M](gloss-m.md) [N](gloss-n.md) [O](gloss-o.md) [P](gloss-p.md) [Q](gloss-q.md) [R](gloss-r.md) S [T](gloss-t.md) U V [W](gloss-w.md) X Y Z

<dl> <dt>

<span id="wmi.gloss_schema"></span><span id="WMI.GLOSS_SCHEMA"></span>**schema**
</dt> <dd>

A collection of class definitions that describe [*managed objects*](gloss-m.md) in a specific environment.

</dd> <dt>

<span id="wmi.gloss_security_descriptor"></span><span id="WMI.GLOSS_SECURITY_DESCRIPTOR"></span>**security descriptor**
</dt> <dd>

A data structure that contains the security information for a securable object, such as a share, file, sink, or event filter.

</dd> <dt>

<span id="wmi.gloss_security_identifier"></span><span id="WMI.GLOSS_SECURITY_IDENTIFIER"></span>**security identifier (SID)**
</dt> <dd>

A data structure that identifies user, group, and computer accounts.

</dd> <dt>

<span id="wmi.gloss_semi_synchronous"></span><span id="WMI.GLOSS_SEMI_SYNCHRONOUS"></span>**semi synchronous**
</dt> <dd>

See *semisynchronous method*.

</dd> <dt>

<span id="wmi.gloss_semi__synchronous"></span><span id="WMI.GLOSS_SEMI__SYNCHRONOUS"></span>**semi-synchronous**
</dt> <dd>

See *semisynchronous method*.

</dd> <dt>

<span id="wmi.gloss_semisynchronous"></span><span id="WMI.GLOSS_SEMISYNCHRONOUS"></span>**semisynchronous method**
</dt> <dd>

A method call that returns immediately and enables the application or script to enumerate the returned objects as a collection.

</dd> <dt>

<span id="gloss_servicesid"></span><span id="GLOSS_SERVICESID"></span>**Service SID**
</dt> <dd>

A unique *SID* that is created for each security context; that is, one for "LocalService" and one for "NetworkService". Only the *service SID* has permissions to resources, like threads and events, which are created by the WMI Provider Host Process (wmiprvse.exe).

</dd> <dt>

<span id="wmi.gloss_sid"></span><span id="WMI.GLOSS_SID"></span>**SID**
</dt> <dd>

See *security identifier*.

</dd> <dt>

<span id="wmi.gloss_singleton_class"></span><span id="WMI.GLOSS_SINGLETON_CLASS"></span>**singleton class**
</dt> <dd>

A WMI class that supports a single instance.

</dd> <dt>

<span id="wmi.gloss_sink"></span><span id="WMI.GLOSS_SINK"></span>**sink**
</dt> <dd>

A COM object that acts as the physical delivery destination for the results of an asynchronous operation or an event notification. A sink implemented by a [*permanent consumer*](gloss-p.md) supports the [**IWbemUnboundObjectSink**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemunboundobjectsink) interface. A sink implemented by a [*temporary consumer*](gloss-t.md) or applications making asynchronous calls supports the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

Scripting clients can use the [**SWbemSink**](swbemsink.md) object and events, such as [**OnObjectReady**](swbemsink-onobjectready.md), to receive callbacks resulting from asynchronous calls.

</dd> <dt>

<span id="wmi.gloss_standard_consumer"></span><span id="WMI.GLOSS_STANDARD_CONSUMER"></span>**standard consumer**
</dt> <dd>

A preinstalled [*permanent consumers*](gloss-p.md) that performs an action, such as sending an email message or writing to a log when configured by a [*Managed Object Format (MOF)*](gloss-m.md) file or a script.

</dd> <dt>

<span id="wmi.gloss_standard_provider"></span><span id="WMI.GLOSS_STANDARD_PROVIDER"></span>**standard provider**
</dt> <dd>

A [*provider*](gloss-p.md) that is built into WMI, which is different from a third-party or custom provider.

</dd> <dt>

<span id="wmi.gloss_standard_qualifier"></span><span id="WMI.GLOSS_STANDARD_QUALIFIER"></span>**standard qualifier**
</dt> <dd>

A [*qualifier*](gloss-q.md) that the [*CIM Object Manager*](gloss-c.md) automatically attaches to a class, instance, property, method, or parameter of a method.

</dd> <dt>

<span id="wmi.gloss_standard_schema"></span><span id="WMI.GLOSS_STANDARD_SCHEMA"></span>**standard schema**
</dt> <dd>

A common conceptual framework that organizes and relates the classes that represent the current operational state of a system, network, or application. The [*Distributed Management Task Force (DMTF)*](gloss-d.md) defines the standard schema in the [*Common Information Model (CIM)*](gloss-c.md).

</dd> <dt>

<span id="wmi.gloss_static_class"></span><span id="WMI.GLOSS_STATIC_CLASS"></span>**static class**
</dt> <dd>

A CIM class definition that rarely changes, and is stored in the [*CIM repository*](gloss-c.md) until it is explicitly deleted. The [*CIM Object Manager*](gloss-c.md) can provide a definition of a static class without a [*provider*](gloss-p.md). A static class can support either *static* or [*dynamic instances*](gloss-d.md).

</dd> <dt>

<span id="wmi.gloss_static_instance"></span><span id="WMI.GLOSS_STATIC_INSTANCE"></span>**static instance**
</dt> <dd>

An instance of a CIM class that is persistently stored in the [*CIM repository*](gloss-c.md) and remains valid until explicitly deleted, even across system restarts.

</dd> <dt>

<span id="wmi.gloss_static_method"></span><span id="WMI.GLOSS_STATIC_METHOD"></span>**static method**
</dt> <dd>

A method defined in a CIM class that is executed by retrieving the class definition instead of retrieving an instance of the class.

</dd> <dt>

<span id="wmi.gloss_subschema"></span><span id="WMI.GLOSS_SUBSCHEMA"></span>**subschema**
</dt> <dd>

A part of a *schema* that is owned by a specific organization. The [*Win32schema*](gloss-w.md) is an example of a subschema.

</dd> <dt>

<span id="wmi.gloss_system_class"></span><span id="WMI.GLOSS_SYSTEM_CLASS"></span>**system class**
</dt> <dd>

A class that the [*CIM Object Manager*](gloss-c.md) defines to support core features such as event notification, security, and localization. A system class is automatically defined in each [*namespace*](gloss-n.md). A system class derives from the abstract base class [**\_\_SystemClass**](--systemclass.md).

</dd> <dt>

<span id="wmi.gloss_system_monitor"></span><span id="WMI.GLOSS_SYSTEM_MONITOR"></span>**System Monitor**
</dt> <dd>

A (CIM) utility that is the GUI for Performance Monitoring.

</dd> <dt>

<span id="wmi.gloss_system_property"></span><span id="WMI.GLOSS_SYSTEM_PROPERTY"></span>**system property**
</dt> <dd>

A property that the [*CIM Object Manager*](gloss-c.md) defines to provide information that applies to each class, for example, name, derivation, and [*namespace*](gloss-n.md).

</dd> </dl>

 

 



