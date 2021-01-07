---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 50397050-3b5c-4683-972c-95d9f661b365
ms.tgt_platform: multiple
title: D (WMI)
ms.topic: article
ms.date: 05/31/2018
---

# D (WMI)

[A](gloss-a.md) B [C](gloss-c.md) D [E](gloss-e.md) [F](gloss-f.md) G [H](gloss-h.md) [I](gloss-i.md) J [K](gloss-k.md) [L](gloss-l.md) [M](gloss-m.md) [N](gloss-n.md) [O](gloss-o.md) [P](gloss-p.md) [Q](gloss-q.md) [R](gloss-r.md) [S](gloss-s.md) [T](gloss-t.md) U V [W](gloss-w.md) X Y Z

<dl> <dt>

<span id="wmi.gloss_datetime"></span><span id="WMI.GLOSS_DATETIME"></span>**datetime**
</dt> <dd>

See [*CIM datetime*](gloss-c.md).

</dd> <dt>

<span id="wmi.gloss_decoupled_provider"></span><span id="WMI.GLOSS_DECOUPLED_PROVIDER"></span>**decoupled provider**
</dt> <dd>

A provider hosted in a separate process from WMI. Decoupled providers are the recommended way to instrument an application, because the provider can control its own lifetime instead of being started each time a user accesses the provider through WMI.

</dd> <dt>

<span id="wmi.gloss_direct_access"></span><span id="WMI.GLOSS_DIRECT_ACCESS"></span>**direct access**
</dt> <dd>

A way to access properties and methods supplied by WMI in a script as if they were automation properties and methods of [**SWbemObject**](swbemobject.md).

Nondirect access: `VolumeName = MyDisk.Properties_("VolumeName")`

Direct access: `VolumeName = MyDisk.VolumeName`

</dd> <dt>

<span id="wmi.gloss_distributed_management_task_force"></span><span id="WMI.GLOSS_DISTRIBUTED_MANAGEMENT_TASK_FORCE"></span>**Distributed Management Task Force (DMTF)**
</dt> <dd>

An international standards organization that works with key technology vendors, including Microsoft, to lead the development, adoption, and unification of management standards and initiatives for desktop, enterprise, and Internet environments.

</dd> <dt>

<span id="wmi.gloss_dmtf"></span><span id="WMI.GLOSS_DMTF"></span>**DMTF**
</dt> <dd>

See *Distributed Management Task Force (DMTF)*.

</dd> <dt>

<span id="wmi.gloss_dynamic_class"></span><span id="WMI.GLOSS_DYNAMIC_CLASS"></span>**dynamic class**
</dt> <dd>

A CIM class whose definition is supplied by a [*provider*](gloss-p.md) at run time, as required. Dynamic classes represent provider-specific [*managed objects*](gloss-m.md) and are not stored in the [*CIM repository*](gloss-c.md). Dynamic classes support only *dynamic instances*.

</dd> <dt>

<span id="wmi.gloss_dynamic_instance"></span><span id="WMI.GLOSS_DYNAMIC_INSTANCE"></span>**dynamic instance**
</dt> <dd>

An instance of a CIM class that is supplied by a [*provider*](gloss-p.md) when required. It is not stored in the [*CIM repository*](gloss-c.md). Dynamic instances can be provided for either static or dynamic classes. Dynamically supporting instances of a class enables a provider to supply up-to-the-minute [*property*](gloss-p.md) values.

</dd> </dl>

 

 



