---
title: MSFT\_StorageDiagnoseResult class
description: Represents the result of a diagnose method call on a storage object.
ms.assetid: '6C164BE2-2B7B-404B-A254-1FBBB9FAE579'
keywords: ["MSFT_StorageDiagnoseResult class Windows Storage Management API", "MSFT_StorageDiagnoseResult class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageDiagnoseResult
- MSFT_StorageDiagnoseResult.FaultId
- MSFT_StorageDiagnoseResult.FaultType
- MSFT_StorageDiagnoseResult.FaultingObjectDescription
- MSFT_StorageDiagnoseResult.FaultingObjectLocation
- MSFT_StorageDiagnoseResult.FaultingObject
- MSFT_StorageDiagnoseResult.Reason
- MSFT_StorageDiagnoseResult.RecommendedActions
- MSFT_StorageDiagnoseResult.PerceivedSeverity
- MSFT_StorageDiagnoseResult.EventTime
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageDiagnoseResult class

Represents the result of a diagnose method call on a storage object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageDiagnoseResult
{
  String                 FaultId;
  String                 FaultType;
  String                 FaultingObjectDescription;
  String                 FaultingObjectLocation;
  MSFT_StorageObject REF FaultingObject;
  String                 Reason;
  String                 RecommendedActions[];
  UInt16                 PerceivedSeverity;
  Datetime               EventTime;
};
```

## Members

The **MSFT\_StorageDiagnoseResult** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageDiagnoseResult** class has these properties.

<dl> <dt>

**EventTime**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Denotes the date and time of the incident. **Null** if the time is unknown.

</dd> <dt>

**FaultId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A unique identifier for the fault.

</dd> <dt>

**FaultingObject**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageObject**](msft-storageobject.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the Storage Management API instance of the object that has faulted.

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

A string that uniquely identifies the type of fault.

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Denotes the perceived severity of the event from the notifier's point of view. One of the following values;



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                     | The severity is unknown or indeterminate.<br/>                          |
| <span id="Information"></span><span id="information"></span><span id="INFORMATION"></span><dl> <dt>**Information**</dt> <dt>2</dt> </dl>                                     | The event is for informative purposes.<br/>                             |
| <span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span><dl> <dt>**Degraded/Warning**</dt> <dt>3</dt> </dl>                 | Action may be required by the user.<br/>                                |
| <span id="Minor"></span><span id="minor"></span><span id="MINOR"></span><dl> <dt>**Minor**</dt> <dt>4</dt> </dl>                                                             | Action is needed, but the situation is not serious at this time.<br/>   |
| <span id="Major"></span><span id="major"></span><span id="MAJOR"></span><dl> <dt>**Major**</dt> <dt>5</dt> </dl>                                                             | Immediate action is needed.<br/>                                        |
| <span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span><dl> <dt>**Critical**</dt> <dt>6</dt> </dl>                                                 | Immediate action is needed and the scope of the issue is broad.<br/>    |
| <span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span><dl> <dt>**Fatal/NonRecoverable**</dt> <dt>7</dt> </dl> | An error has occurred, but it is too late to take remedial action.<br/> |



 

</dd> <dt>

**Reason**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The formatted message describing the reason for the fault.

</dd> <dt>

**RecommendedActions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free form descriptions of the recommended actions to take to resolve the cause of the fault.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





