---
title: MSFT\_StorageJob class
description: Represents a storage job.
ms.assetid: '71DC2B71-3F39-488F-B9D0-01E65354BF7C'
keywords: ["MSFT_StorageJob class Windows Storage Management API", "MSFT_StorageJob class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageJob
- MSFT_StorageJob.Name
- MSFT_StorageJob.Description
- MSFT_StorageJob.ElapsedTime
- MSFT_StorageJob.ErrorCode
- MSFT_StorageJob.ErrorDescription
- MSFT_StorageJob.JobState
- MSFT_StorageJob.JobStatus
- MSFT_StorageJob.LocalOrUtcTime
- MSFT_StorageJob.OperationalStatus
- MSFT_StorageJob.StatusDescriptions
- MSFT_StorageJob.PercentComplete
- MSFT_StorageJob.StartTime
- MSFT_StorageJob.TimeBeforeRemoval
- MSFT_StorageJob.TimeOfLastStateChange
- MSFT_StorageJob.TimeSubmitted
- MSFT_StorageJob.DeleteOnCompletion
- MSFT_StorageJob.IsBackgroundTask
- MSFT_StorageJob.RecoveryAction
- MSFT_StorageJob.OtherRecoveryAction
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageJob class

Represents a storage job.

The following syntax is simplified from Managed Object Format (MOF) code.

Storage jobs represent long running operations on a storage subsystem. These operations can be initiated in either of the following ways:

-   By users, through the various management interfaces defined by this MOF.
-   Automatically, by intelligent storage subsystems.

## Syntax

``` syntax
class MSFT_StorageJob : MSFT_StorageObject
{
  String   Name;
  String   Description;
  Datetime ElapsedTime;
  UInt16   ErrorCode;
  String   ErrorDescription;
  UInt16   JobState;
  String   JobStatus;
  UInt16   LocalOrUtcTime;
  UInt16   OperationalStatus[];
  String   StatusDescriptions[];
  UInt16   PercentComplete;
  Datetime StartTime;
  Datetime TimeBeforeRemoval;
  Datetime TimeOfLastStateChange;
  Datetime TimeSubmitted;
  Boolean  DeleteOnCompletion;
  Boolean  IsBackgroundTask;
  UInt16   RecoveryAction;
  String   OtherRecoveryAction;
};
```

## Members

The **MSFT\_StorageJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageJob** class has these methods.



| Method                                                           | Description                                                                                                        |
|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**GetExtendedStatus**](msft-storagejob-getextendedstatus.md)   | Retrieves extended status information for an unsuccessful storage job.<br/>                                  |
| [**RequestStateChange**](msft-storagejob-requeststatechange.md) | Requests that the state of the job be changed to the value specified in the *RequestedState* parameter.<br/> |



 

### Properties

The **MSFT\_StorageJob** class has these properties.

<dl> <dt>

**DeleteOnCompletion**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the storage job will be deleted automatically after a short time interval.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the operation that the storage job is tracking.

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the job is still executing, this property indicates how long it has been executing. If the job is complete, it is the total execution time.

</dd> <dt>

**ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the operation that this storage job was tracking has failed, the provider sets this property to an error code defined by the method that invoked the operation. If this storage job was tracking a background task, the error code can be set to any valid storage management error code as defined in the value map below. If there was no error, this property must be set to **Success**. This property should be **NULL** until the operation has completed.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A free-form string that contains the vendor's error description.

</dd> <dt>

**IsBackgroundTask**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, this storage job represents an automated background task initiated by the storage subsystem. For all user- or management-initiated operations, this value should be set to **FALSE**.

</dd> <dt>

**JobState**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The state of the job.

<dl> <dt>

<span id="New"></span><span id="new"></span><span id="NEW"></span>**New** (2)
</dt> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (3)
</dt> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (4)
</dt> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>**Suspended** (5)
</dt> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (6)
</dt> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (7)
</dt> <dt>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>**Terminated** (8)
</dt> <dt>

<span id="Killed"></span><span id="killed"></span><span id="KILLED"></span>**Killed** (9)
</dt> <dt>

<span id="Exception"></span><span id="exception"></span><span id="EXCEPTION"></span>**Exception** (10)
</dt> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>**Service** (11)
</dt> <dt>

<span id="Query_Pending"></span><span id="query_pending"></span><span id="QUERY_PENDING"></span>**Query Pending** (12)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (13..32767)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768..65535)
</dt> </dl>

</dd> <dt>

**JobStatus**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A free-form string that represents the status of the job. The primary status is reflected in the **OperationalStatus** property. **JobStatus** provides additional, implementation-specific details.

</dd> <dt>

**LocalOrUtcTime**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Values** ( "Local Time", "UTC Time" ), **ValueMap** ("1", "2")
</dt> </dl>

Indicates whether the time values in the **RunStartInterval** and **UntilTime** properties represent local time or UTC time. Time values are synchronized worldwide by setting this property to **UTC Time**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A system-defined name for the storage job.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Indicates the current status of each storage subsystem that is participating in the storage job.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                              | The operational status is unknown.<br/>                                                                                                                                                             |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                      | A vendor-specific **OperationalStatus** is specified in the **OtherOperationalStatusDescription** property.<br/>                                                                                    |
| <span id="OK_"></span><span id="ok_"></span><dl> <dt>**OK** </dt> <dt>2 </dt> </dl>                                                                                                                   | The storage subsystem is responding to commands and is in a normal operating state.<br/>                                                                                                            |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                                          | The storage subsystem is responding to commands, but is not running in an optimal operating state.<br/>                                                                                             |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>4</dt> </dl>                                                                          | The storage subsystem is functioning, but needs attention. For example, it may be overloaded or overheated.<br/>                                                                                    |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>5</dt> </dl>                                  | The storage subsystem is functioning, but it is likely to fail in the near future.<br/>                                                                                                             |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                                      | An error has occurred.<br/>                                                                                                                                                                         |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl>                      | A nonrecoverable error has occurred.<br/>                                                                                                                                                           |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>8</dt> </dl>                                                                          | The storage subsystem is in the process of starting.<br/>                                                                                                                                           |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>9</dt> </dl>                                                                          | The storage subsystem is in the process of stopping.<br/>                                                                                                                                           |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>10</dt> </dl>                                                                             | The storage subsystem was stopped or shut down in a clean and orderly fashion.<br/>                                                                                                                 |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>11</dt> </dl>                                                                 | The storage subsystem is being configured, maintained, cleaned, or otherwise administered.<br/>                                                                                                     |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>12</dt> </dl>                                                                 | The storage provider is aware of the storage subsystem, but has never been able to communicate with it.<br/>                                                                                        |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>13</dt> </dl>                                 | The storage provider is aware of the storage subsystem and has communicated with it in the past, but is currently unable to communicate with it.<br/>                                               |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>14</dt> </dl>                                                                             | The storage subsystem was stopped abruptly and might require configuration or maintenance.<br/>                                                                                                     |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>15</dt> </dl>                                                                             | The storage provider is able to contact the storage subsystem, but the storage subsystem is not currently active.<br/>                                                                              |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>16</dt> </dl> | This value indicates that another device or connection that the storage subsystem depends on might need attention. It does not necessarily indicate trouble with the storage subsystem itself.<br/> |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>17</dt> </dl>                                                                     | The storage subsystem has completed an operation. This value should be combined with "OK", "Error", or "Degraded", depending on the outcome of the operation.<br/>                                  |
| <span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span><dl> <dt>**Power Mode**</dt> <dt>18</dt> </dl>                                                                 | This value is reserved for system use.<br/>                                                                                                                                                         |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>..</dt> </dl>                                                     | Values between 18 and 0x8000 (exclusive) are reserved for DMTF.<br/>                                                                                                                                |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>0x8000..</dt> </dl>                                       | Values greater than or equal to 0x8000 are reserved for vendors.<br/>                                                                                                                               |



 

</dd> <dt>

**OtherRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A vendor-specific recovery action to be taken for an unsuccessfully run job. This property should only be set if the **RecoveryAction** is set to **Other**.

</dd> <dt>

**PercentComplete**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Units**](https://msdn.microsoft.com/library/aa393650) (Percentage)
</dt> </dl>

The percentage of the job that has completed at the time that this value is requested.

</dd> <dt>

**RecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the recovery action to be taken for an unsuccessfully run job. One of the following values.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                             | The desired recovery action is unknown.<br/>                                   |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                     | The recovery action is specified in the **OtherRecoveryAction** property.<br/> |
| <span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span><dl> <dt>**Do Not Continue**</dt> <dt>2</dt> </dl>                             | Stop executing the storage job and appropriately update its status.<br/>       |
| <span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span><dl> <dt>**Continue With Next Job**</dt> <dt>3</dt> </dl> | Continue with the next job in the queue.<br/>                                  |
| <span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span><dl> <dt>**Re-run Job**</dt> <dt>4</dt> </dl>                                                 | Rerun the job.<br/>                                                            |



 

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the job was started.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptions of the **OperationalStatus** values. For example, if **Stopping** is a value in **OperationalStatus**, the corresponding array element of **StatusDescriptions** may explain why an object is being stopped.

</dd> <dt>

**TimeBeforeRemoval**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of time, in seconds, that the job is retained after it has finished executing, either succeeding or failing in that execution. The job must remain in existence for some period of time regardless of the value of the **DeleteOnCompletion** property.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the state of the job last changed. If the state of the job has not changed and this property does not have a value, it must be set to zero. If a state change was requested, but it was rejected or has not yet been processed, the value of this property must not be updated.

</dd> <dt>

**TimeSubmitted**
</dt> <dd> <dl> <dt>

Data type: **Datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the job was submitted for execution. A value of all zeros indicates that the owning element is not capable of reporting a date and time. Therefore, the **ScheduledStartTime** and **StartTime** are reported as intervals relative to the time their values are requested.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





