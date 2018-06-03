---
title: MSFT\_SMStorageDiagnoseResult class
description: Represents the result of a Diagnose method call on a storage object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0011e1a7-f5ca-43e4-a6f8-fc0ad0681f0d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMStorageDiagnoseResult class
- MSFT_SMStorageDiagnoseResult class, described
topic_type:
- apiref
api_name:
- MSFT_SMStorageDiagnoseResult
- MSFT_SMStorageDiagnoseResult.FaultId
- MSFT_SMStorageDiagnoseResult.FaultType
- MSFT_SMStorageDiagnoseResult.FaultingObjectDescription
- MSFT_SMStorageDiagnoseResult.FaultingObjectLocation
- MSFT_SMStorageDiagnoseResult.FaultingObject
- MSFT_SMStorageDiagnoseResult.Reason
- MSFT_SMStorageDiagnoseResult.RecommendedActions
- MSFT_SMStorageDiagnoseResult.PerceivedSeverity
- MSFT_SMStorageDiagnoseResult.EventTime
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMStorageDiagnoseResult class

Represents the result of a Diagnose method call on a storage object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Indication, provider("WMIStorage"), AMENDMENT]
class MSFT_SMStorageDiagnoseResult
{
  String                   FaultId;
  String                   FaultType;
  String                   FaultingObjectDescription;
  String                   FaultingObjectLocation;
  MSFT_SMStorageObject REF FaultingObject;
  String                   Reason;
  String                   RecommendedActions[];
  UInt16                   PerceivedSeverity;
  Datetime                 EventTime;
};
```

## Members

The **MSFT\_SMStorageDiagnoseResult** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMStorageDiagnoseResult** class has these properties.

<dl> <dt>

**EventTime**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time of the fault. This value is set to **NULL** if the date or time is unknown.

</dd> <dt>

**FaultId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A unique identifier of the fault.

</dd> <dt>

**FaultingObject**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMStorageObject**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the storage object instance that has faulted.

</dd> <dt>

**FaultingObjectDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The description of the object that triggered the fault.

</dd> <dt>

**FaultingObjectLocation**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The location of the object that triggered the fault.

</dd> <dt>

**FaultType**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies the type of the fault.

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The perceived severity of the fault from the notifier's point of view.

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

An error has occured, but it is too late to take remedial action.

</dd> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved**


</dt> <dd>

This value is reserved for system use.

</dd> </dl>

</dd> <dt>

**Reason**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The formatted message that describes the reason for the fault.

</dd> <dt>

**RecommendedActions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains descriptions of the recommended actions to take to resolve the cause of the fault.

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

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





