---
title: D
description: A C E F H I K L M N O P Q R S T W
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47011004-c0f4-4e49-80e8-ba25a402a73c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# D

[A](gloss-a.md) [C](gloss-c.md) [E](gloss-e.md) [F](gloss-f.md) [H](gloss-h.md) [I](gloss-i.md) [K](gloss-k.md) [L](gloss-l.md) [M](gloss-m.md) [N](gloss-n.md) [O](gloss-o.md) [P](gloss-p.md) [Q](gloss-q.md) [R](gloss-r.md) [S](gloss-s.md) [T](gloss-t.md) [W](gloss-w.md)

<dl> <dt>

<span id="wmi_v2.gloss_datetime"></span><span id="WMI_V2.GLOSS_DATETIME"></span>**datetime**
</dt> <dd>

See [*CIM datetime*](gloss-c.md#wmi-v2-gloss-cim-datetime).

</dd> <dt>

<span id="wmi_v2.gloss_decoupled_provider"></span><span id="WMI_V2.GLOSS_DECOUPLED_PROVIDER"></span>**decoupled provider**
</dt> <dd>

A provider hosted in a separate process from WMI. Decoupled providers are the recommended way to instrument an application, because the provider can control its own lifetime instead of being started each time a user accesses the provider through WMI.

</dd> <dt>

<span id="wmi_v2.gloss_direct_access"></span><span id="WMI_V2.GLOSS_DIRECT_ACCESS"></span>**direct access**
</dt> <dd>

A way to access properties and methods supplied by WMI in a script as if they were automation properties and methods of [**SWbemObject**](https://msdn.microsoft.com/library/aa393741).

Nondirect access: `VolumeName = MyDisk.Properties_("VolumeName")`

Direct access: `VolumeName = MyDisk.VolumeName`

</dd> <dt>

<span id="wmi_v2.gloss_distributed_management_task_force"></span><span id="WMI_V2.GLOSS_DISTRIBUTED_MANAGEMENT_TASK_FORCE"></span>**Distributed Management Task Force (DMTF)**
</dt> <dd>

An international standards organization that works with key technology vendors, including Microsoft, to lead the development, adoption, and unification of management standards and initiatives for desktop, enterprise, and Internet environments.

</dd> <dt>

<span id="wmi_v2.gloss_dmtf"></span><span id="WMI_V2.GLOSS_DMTF"></span>**DMTF**
</dt> <dd>

See *Distributed Management Task Force (DMTF)*.

</dd> <dt>

<span id="wmi_v2.gloss_dynamic_class"></span><span id="WMI_V2.GLOSS_DYNAMIC_CLASS"></span>**dynamic class**
</dt> <dd>

A CIM class whose definition is supplied by a [*provider*](gloss-p.md#wmi-v2-gloss-provider) at run time, as required. Dynamic classes represent provider-specific [*managed objects*](gloss-m.md#wmi-v2-gloss-managed-object) and are not stored in the [*CIM repository*](gloss-c.md#wmi-v2-gloss-cim-repository). Dynamic classes support only *dynamic instances*.

</dd> <dt>

<span id="wmi_v2.gloss_dynamic_instance"></span><span id="WMI_V2.GLOSS_DYNAMIC_INSTANCE"></span>**dynamic instance**
</dt> <dd>

An instance of a CIM class that is supplied by a [*provider*](gloss-p.md#wmi-v2-gloss-provider) when required. It is not stored in the [*CIM repository*](gloss-c.md#wmi-v2-gloss-cim-repository). Dynamic instances can be provided for either static or dynamic classes. Dynamically supporting instances of a class enables a provider to supply up-to-the-minute [*property*](gloss-p.md#wmi-v2-gloss-property) values.

</dd> </dl>

 

 




