---
title: MSFT\_SMStorageHealthStatusChangeEvent class
description: Represents a health status change event for a storage system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f979d5d0-74c8-4001-96ae-397efc1c3109
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMStorageHealthStatusChangeEvent class
- MSFT_SMStorageHealthStatusChangeEvent class, described
topic_type:
- apiref
api_name:
- MSFT_SMStorageHealthStatusChangeEvent
- MSFT_SMStorageHealthStatusChangeEvent.StorageSubsystemObjectId
- MSFT_SMStorageHealthStatusChangeEvent.SourceInstance
- MSFT_SMStorageHealthStatusChangeEvent.Description
- MSFT_SMStorageHealthStatusChangeEvent.EventTime
- MSFT_SMStorageHealthStatusChangeEvent.PerceivedSeverity
- MSFT_SMStorageHealthStatusChangeEvent.SourceClassName
- MSFT_SMStorageHealthStatusChangeEvent.StorageSystem
- MSFT_SMStorageHealthStatusChangeEvent.PreviousHealthStatus
- MSFT_SMStorageHealthStatusChangeEvent.CurrentHealthStatus
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMStorageHealthStatusChangeEvent class

Represents a health status change event for a storage system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Indication, provider("WMIStorage"), AMENDMENT]
class MSFT_SMStorageHealthStatusChangeEvent : MSFT_SMStorageEvent
{
  string               StorageSubsystemObjectId;
  MSFT_SMStorageObject SourceInstance;
  string               Description;
  datetime             EventTime;
  uint16               PerceivedSeverity;
  string               SourceClassName;
  MSFT_SMSystem        StorageSystem;
  UInt16               PreviousHealthStatus;
  UInt16               CurrentHealthStatus;
};
```

## Members

The **MSFT\_SMStorageHealthStatusChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMStorageHealthStatusChangeEvent** class has these properties.

<dl> <dt>

**CurrentHealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the storage system object.

The possible values are:

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A brief description of the event, provided by the storage subsystem.

This property is inherited from [**MSFT\_SMStorageEvent**](msft-smstorageevent.md).

</dd> <dt>

**EventTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time in which the event that triggered this event occurred.

This property is inherited from [**MSFT\_SMStorageEvent**](msft-smstorageevent.md).

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The perceived severity of the event from the notifier's point of view.

This property is inherited from [**MSFT\_SMStorageEvent**](msft-smstorageevent.md).

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The severity is unknown or indeterminate.

</dd> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>**Information** (2)


</dt> <dd>

The event is for informative purposes.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (3)


</dt> <dd>

Action may be required by the user.

</dd> <dt>

<span id="Minor"></span><span id="minor"></span><span id="MINOR"></span>

<span id="Minor"></span><span id="minor"></span><span id="MINOR"></span>**Minor** (4)


</dt> <dd>

Action is needed, but the situation is not serious at this time.

</dd> <dt>

<span id="Major"></span><span id="major"></span><span id="MAJOR"></span>

<span id="Major"></span><span id="major"></span><span id="MAJOR"></span>**Major** (5)


</dt> <dd>

Immediate action is needed.

</dd> <dt>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>

<span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span>**Critical** (6)


</dt> <dd>

Immediate action is needed and the scope of the issue is broad.

</dd> <dt>

<span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span>

<span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span>**Fatal/NonRecoverable** (7)


</dt> <dd>

An error has occurred, but it is too late to take remedial action.

</dd> <dt>




</dt> <dd>

This value is reserved for system use.

</dd> </dl>

</dd> <dt>

**PreviousHealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the storage system object before the event occurred.

The possible values are:

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**SourceClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The class of the object that caused the event. For example, if the object causing the event is a storage pool, this property should be set to "MSFT\_SMStoragePool" (not the vendor-derived class).

This property is inherited from [**MSFT\_SMStorageEvent**](msft-smstorageevent.md).

</dd> <dt>

**SourceInstance**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMStorageObject**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_SMStorageObject**](msft-smstorageobject.md)")
</dt> </dl>

The [**MSFT\_SMStorageObject**](msft-smstorageobject.md) object that caused the event.

This property is inherited from [**MSFT\_SMStorageEvent**](msft-smstorageevent.md).

</dd> <dt>

**StorageSubsystemObjectId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the storage object that caused the event.

This property is inherited from [**MSFT\_SMStorageEvent**](msft-smstorageevent.md).

</dd> <dt>

**StorageSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMSystem**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The storage system object that is associated with the event.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageEvent**](msft-smstorageevent.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





