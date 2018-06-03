---
title: MSFT\_StorageEvent class
description: Base class for representing storage events.
ms.assetid: 77338A5C-7AF6-4C78-80E1-AF557B60CA46
keywords:
- MSFT_StorageEvent class Windows Storage Management API
- MSFT_StorageEvent class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageEvent
- MSFT_StorageEvent.SourceObjectId
- MSFT_StorageEvent.SourceClassName
- MSFT_StorageEvent.SourceNamespace
- MSFT_StorageEvent.SourceServer
- MSFT_StorageEvent.Description
- MSFT_StorageEvent.EventTime
- MSFT_StorageEvent.PerceivedSeverity
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageEvent class

Base class for representing storage events.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Indication, Abstract]
class MSFT_StorageEvent
{
  String   SourceObjectId;
  String   SourceClassName;
  String   SourceNamespace;
  String   SourceServer;
  String   Description;
  Datetime EventTime;
  UInt16   PerceivedSeverity;
};
```

## Members

The **MSFT\_StorageEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageEvent** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A brief description of the event, provided by the storage subsystem.

</dd> <dt>

**EventTime**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time in which the event that triggered this event occurred.

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The perceived severity of the event from the notifier's point of view.

One of the following values.



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                     | The severity is unknown or indeterminate. <br/>                        |
| <span id="Information"></span><span id="information"></span><span id="INFORMATION"></span><dl> <dt>**Information**</dt> <dt>2</dt> </dl>                                     | The event is for informative purposes.<br/>                            |
| <span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span><dl> <dt>**Degraded/Warning**</dt> <dt>3</dt> </dl>                 | Action may be required by the user. <br/>                              |
| <span id="Minor"></span><span id="minor"></span><span id="MINOR"></span><dl> <dt>**Minor**</dt> <dt>4</dt> </dl>                                                             | Action is needed, but the situation is not serious at this time.<br/>  |
| <span id="Major"></span><span id="major"></span><span id="MAJOR"></span><dl> <dt>**Major**</dt> <dt>5</dt> </dl>                                                             | Immediate action is needed.<br/>                                       |
| <span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span><dl> <dt>**Critical**</dt> <dt>6</dt> </dl>                                                 | Immediate action is needed and the scope of the issue is broad.<br/>   |
| <span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span><dl> <dt>**Fatal/NonRecoverable**</dt> <dt>7</dt> </dl> | An error has occured, but it is too late to take remedial action.<br/> |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl>        | This value is reserved for system use.<br/>                            |



 

</dd> <dt>

**SourceClassName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The class of the object that caused the event. For example, if the object causing the event is a storage pool, this property should be set to "MSFT\_StoragePool" (not the vendor-derived class).

</dd> <dt>

**SourceNamespace**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source namespace of the object that caused the event.

</dd> <dt>

**SourceObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**ModelCorrespondence {"MSFT\_StorageObject.ObjectId"}**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The object that caused the event.

</dd> <dt>

**SourceServer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source server of the object that caused the event.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageAlertEvent**](msft-storagealertevent.md)
</dt> <dt>

[**MSFT\_StorageArrivalEvent**](msft-storagearrivalevent.md)
</dt> <dt>

[**MSFT\_StorageDepartureEvent**](msft-storagedepartureevent.md)
</dt> <dt>

[**MSFT\_StorageModificationEvent**](msft-storagemodificationevent.md)
</dt> </dl>

 

 





