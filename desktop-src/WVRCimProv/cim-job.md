---
title: CIM\_Job class
description: Represents an executing unit of work, such as a script or a print job. A Job is distinct from a Process in that a Job can be scheduled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 113f66fa-eeed-480b-912f-73b66b6a4807
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Job class
- CIM_Job class, described
topic_type:
- apiref
api_name:
- CIM_Job
- CIM_Job.InstanceID
- CIM_Job.Caption
- CIM_Job.Description
- CIM_Job.ElementName
- CIM_Job.InstallDate
- CIM_Job.Name
- CIM_Job.OperationalStatus
- CIM_Job.StatusDescriptions
- CIM_Job.Status
- CIM_Job.HealthState
- CIM_Job.CommunicationStatus
- CIM_Job.DetailedStatus
- CIM_Job.OperatingStatus
- CIM_Job.PrimaryStatus
- CIM_Job.JobStatus
- CIM_Job.TimeSubmitted
- CIM_Job.ScheduledStartTime
- CIM_Job.StartTime
- CIM_Job.ElapsedTime
- CIM_Job.JobRunTimes
- CIM_Job.RunMonth
- CIM_Job.RunDay
- CIM_Job.RunDayOfWeek
- CIM_Job.RunStartInterval
- CIM_Job.LocalOrUtcTime
- CIM_Job.UntilTime
- CIM_Job.Notify
- CIM_Job.Owner
- CIM_Job.Priority
- CIM_Job.PercentComplete
- CIM_Job.DeleteOnCompletion
- CIM_Job.ErrorCode
- CIM_Job.ErrorDescription
- CIM_Job.RecoveryAction
- CIM_Job.OtherRecoveryAction
api_location:
- WvrCimProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Job class

Represents an executing unit of work, such as a script or a print job. A Job is distinct from a Process in that a Job can be scheduled.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), Abstract, Version("2.10.0"), AMENDMENT]
class CIM_Job : CIM_LogicalElement
{
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  string   Name;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   JobStatus;
  datetime TimeSubmitted;
  datetime ScheduledStartTime;
  datetime StartTime;
  datetime ElapsedTime;
  uint32   JobRunTimes = 1;
  uint8    RunMonth;
  sint8    RunDay;
  sint8    RunDayOfWeek;
  datetime RunStartInterval;
  uint16   LocalOrUtcTime;
  datetime UntilTime;
  string   Notify;
  string   Owner;
  uint32   Priority;
  uint16   PercentComplete;
  boolean  DeleteOnCompletion;
  uint16   ErrorCode;
  string   ErrorDescription;
  uint16   RecoveryAction;
  string   OtherRecoveryAction;
};
```

## Members

The **CIM\_Job** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_Job** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                              |
|:-----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**KillJob**](cim-job-killjob.md) | Kills this job and any underlying processes, and removes any associations containing this job. This method is deprecated, instead use the **RequestStateChange** method to distinguish between an orderly shutdown and an immediate shutdown without cleanup.<br/> |



 

### Properties

The **CIM\_Job** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Contains a short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the ability of the instrumentation to communicate with this element. A **NULL** value indicates that instrumentation does not support this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Indicates that the instrumentation cannot report on the **CommunicationStatus** property at this time.

</dd> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)


</dt> <dd>

Indicates that the instrumentation is capable of reporting this property, but intentionally does not for this element.

</dd> <dt>

<span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span>

<span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span>**Communication OK** (2)


</dt> <dd>

Indicates only that communication is established with the element.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (3)


</dt> <dd>

Indicates that the element has been contacted in the past, but is currently unreachable.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (4)


</dt> <dd>

Indicates that the instrumentation has contact information for this element, but has never been able to communicate with it.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**DeleteOnCompletion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether or not the job should be automatically deleted upon completion. Note that the completion of a recurring job is defined by its **JobRunTimes** or **UntilTime** properties, or by manual termination. If this property is set to **FALSE** before the job completes, setting it to **TRUE** after the job completes will not delete the job. Instead, to manually delete the job you must use the [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx).[**DeleteInstance**](Overload:Microsoft.Management.Infrastructure.CimSession.DeleteInstance) method.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063).**PrimaryStatus**", "[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**HealthState**")
</dt> </dl>

Indicates additional status details that complement the **PrimaryStatus** property. A **NULL** value indicates that the instrumentation does not support this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (0)


</dt> <dd>

Indicates that the instrumentation is capable of reporting this property, but intentionally does not report it for this element.

</dd> <dt>

<span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span>

<span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span>**No Additional Information** (1)


</dt> <dd>

Indicates that no details have to be added to the **PrimaryStatus** property, for example when the **PrimaryStatus** is set to **OK**.

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (2)


</dt> <dd>

Indicates that the element functions, but requires attention. Overload and overheated are examples of **Stressed** states.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (3)


</dt> <dd>

Indicates that an element functions nominally, but predicts a failure in the near future.

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (4)


</dt> <dd>

Indicates that this element is in an error condition that requires human intervention.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (5)


</dt> <dd>

Indicates that an element on which this element depends is in error. This element might be **OK** but cannot function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how long the job has been executing or the total execution time if the job is complete.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**ErrorDescription**")
</dt> </dl>

Contains a vendor-specific error code. The value must be set to zero if the job completed without error.

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**ErrorCode**")
</dt> </dl>

Contains a vendor-supplied description of the **ErrorCode** property.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its sub-components.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The implementation cannot report on **HealthState** at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

The element is fully functional and is operating within normal operational parameters and without error.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (10)


</dt> <dd>

The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors

</dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>**Minor failure** (15)


</dt> <dd>

All functionality is available but some might be degraded.

</dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>**Major failure** (20)


</dt> <dd>

The element is failing. It is possible that some or all of the functionality of this component is degraded or not working.

</dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>**Critical failure** (25)


</dt> <dd>

The element is non-functional and recovery might not be possible.

</dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-recoverable error** (30)


</dt> <dd>

The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF has reserved the unused portion of the continuum for additional **HealthStates** values in the future.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the object was installed. The lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing Namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the Namespace, the value of **InstanceID** should be constructed in the following pattern:
>
> *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity defining the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This is similar to the structure of Schema class names. In addition, to ensure uniqueness the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the preceding pattern is not used, the defining entity must assure that the resultant **InstanceID** is not re-used across any **InstanceID**s produced by this or other providers for this Namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**JobRunTimes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies how many times the job should be run. A value of 1 indicates that the job is not recurring, while any nonzero value specifies a limit to the number of times that the job will recur. Zero specifies that there is no limit to the number of times that the job can be processed, in which case it is terminated either after the **UntilTime** or by manual intervention.

</dd> <dt>

**JobStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Contains a free-form string that represents the status of the job. The primary status is reflected in the **OperationalStatus** property. **JobStatus** provides additional, implementation-specific details.

</dd> <dt>

**LocalOrUtcTime**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the times represented in the **RunStartInterval** and **UntilTime** properties represent local times or Coordinated Universal Time (UTC) times. Time values are synchronized worldwide by using the **UTC Time** enumeration value.

The possible values are.

<dt>

<span id="Local_Time"></span><span id="local_time"></span><span id="LOCAL_TIME"></span>

**Local Time** (1)


</dt> <dd></dd> <dt>

<span id="UTC_Time"></span><span id="utc_time"></span><span id="UTC_TIME"></span>

**UTC Time** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

Indicates the user-friendly name for this instance of a job. In addition, the user-friendly name can be used as a property for a search or query.

> \[!Tip\]  
> **Name** does not have to be unique within a namespace.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The User who is to be notified upon the Job completion or failure.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063).**EnabledState**")
</dt> </dl>

Indicates the current operational condition of the element. This property can be used to provide more detail about the current state of the element. It can also indicate transitional states. A **NULL** value indicates that the instrumentation does not support this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Indicates that the instrumentation cannot report on the **OperatingStatus** property at this time.

</dd> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)


</dt> <dd>

Indicates that the instrumentation is capable of reporting this property, but intentionally does not report it for this element.

</dd> <dt>

<span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span>

<span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span>**Servicing** (2)


</dt> <dd>

Indicates that the element is in process to be configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (3)


</dt> <dd>

Indicates that the element is being initialized.

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (4)


</dt> <dd>

Indicates that the element is being brought to an orderly stop.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (5)


</dt> <dd>

Indicates that the element is intentionally stopped.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (6)


</dt> <dd>

Indicates that the element stopped in an unexpected way.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (7)


</dt> <dd>

Indicates that the element is inactive or quiesced.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (8)


</dt> <dd>

Indicates that the element completed its operation. We recommend using a **PrimaryStatus** property value of **OK**, **Error**, or **Degraded** to indicate success or failure of the operation.

</dd> <dt>

<span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span>

<span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span>**Migrating** (9)


</dt> <dd>

Indicates that the element is being moved between host elements.

</dd> <dt>

<span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span>

<span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span>**Emigrating** (10)


</dt> <dd>

Indicates that the element is being moved away from the host element.

</dd> <dt>

<span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span>

<span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span>**Immigrating** (11)


</dt> <dd>

Indicates that the element is being moved to a new host element.

</dd> <dt>

<span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span>

<span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span>**Snapshotting** (12)


</dt> <dd>

Indicates that a snapshot copy of the element is being created.

</dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (13)


</dt> <dd>

Indicates that the element is being brought to an abrupt stop.

</dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (14)


</dt> <dd>

Indicates that the element is performing test functions.

</dd> <dt>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>**Transitioning** (15)


</dt> <dd>

Indicates that the element is between states and is not fully available in either state. Use another value that indicates a more specific transition if one is available.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (16)


</dt> <dd>

Indicates that the element is in service and operational.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Reserved.

</dd> </dl>

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**StatusDescriptions**")
</dt> </dl>

Contains indicators of the current status of the element. The first value of **OperationalStatus** should contain the primary status for the element.

> [!Note]  
> **OperationalStatus** replaces the deprecated **Status** property. Due to the widespread use of the existing **Status** property in management applications, Microsoft strongly recommends that providers or instrumentation provide both the **Status** and **OperationalStatus** properties. When instrumented, **Status** (because it is single-valued) should also provide the primary status of the element.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

Indicates the implementation cannot report on **OperationalStatus** at this time.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Indicates an undefined state.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

Indicates full functionality without errors.

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd>

Indicates the element is working and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)


</dt> <dd>

Indicates that the element is functioning, but needs attention. Overload and overheated are examples of **Stressed** states.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)


</dt> <dd>

Indicates that an element is functioning nominally but predicting a failure in the near future.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)


</dt> <dd>

Indicates that an error has occurred.

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd>

A nonrecoverable error has occurred.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)


</dt> <dd>

The job is starting.

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)


</dt> <dd>

The job is stopping.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)


</dt> <dd>

The element has been intentionally stopped.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

Indicates the element is being configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd>

Indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd>

Indicates that the job is known to exist and has been contacted successfully in the past, but is currently unreachable.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)


</dt> <dd>

Indicates the job stopped in an unexpected way. The state and configuration of the job might need to be updated.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)


</dt> <dd>

Indicates that the job is inactive.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

Indicates that an element on which this job depends is in error. This element may be **OK** but is unable to function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)


</dt> <dd>

Indicates that the job has completed its operation. This value should be combined with either **OK**, **Error**Error, or **Degraded** so that a client can tell if the complete operation **Completed** with **OK** (passed), Completed with **Error** (failed), or Completed with **Degraded** (the operation finished, but it did not complete OK or did not report an error).

</dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)


</dt> <dd>

"Power Mode" indicates that the element has additional power model information contained in the associated PowerManagementService association.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF has reserved this portion of the range for additional *OperationalStatus* values in the future.

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

Microsoft has reserved the unused portion of the range for additional *OperationalStatus* values in the future.

</dd> </dl>

</dd> <dt>

**OtherRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RecoveryAction**")
</dt> </dl>

Describes the recovery action to take when the **RecoveryAction** property is set to **Other**.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_OwningJobElement")
</dt> </dl>

The User that submitted the Job, or the Service or method name that caused the job to be created.

</dd> <dt>

**PercentComplete**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("0"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("101"), **PUnit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percent")
</dt> </dl>

Indicates the percentage of the job that has completed at the time that this value is requested.

> [!Note]  
> Note that the value 101 is undefined and will be not be allowed in the next major revision of the specification.

 

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**DetailedStatus**", "**CIM\_ManagedSystemElement**.**HealthState**")
</dt> </dl>

Indicates a high-level status value.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (1)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (2)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 = *value* </dd> </dl>

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the urgency or importance of execution of the job. The lower the number, the higher the priority.

</dd> <dt>

**RecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**OtherRecoveryAction**")
</dt> </dl>

Describes the recovery action to take when a job runs unsuccessfully.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

The recovery action to take is unknown.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

The recovery action is specified in the **OtherRecoveryAction** property.

</dd> <dt>

<span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span>

<span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span>**Do Not Continue** (2)


</dt> <dd>

Stop the execution of the job and appropriately update its status.

</dd> <dt>

<span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span>

<span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span>**Continue With Next Job** (3)


</dt> <dd>

Continue with the next job in the queue.

</dd> <dt>

<span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span>

<span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span>**Re-run Job** (4)


</dt> <dd>

Re-run the job.

</dd> <dt>

<span id="Run_Recovery_Job"></span><span id="run_recovery_job"></span><span id="RUN_RECOVERY_JOB"></span>

<span id="Run_Recovery_Job"></span><span id="run_recovery_job"></span><span id="RUN_RECOVERY_JOB"></span>**Run Recovery Job** (5)


</dt> <dd>

Run the job associated using a recovery job relationship. The recovery job must already be in the queue from which it will run.

</dd> </dl>

</dd> <dt>

**RunDay**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("-31"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("31"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

Specifies a day in the **RunMonth**, which in combination with **RunDayOfWeek** determines the day on which the job should be processed.

A positive or negative integer indicates whether the **RunDay** is counted from the beginning or end of the month. For example, 5 indicates the fifth day in the **RunMonth** and -1 indicates the last day in the **RunMonth**. The indicated day of the month may be offset to a specified day of the week by the **RunDayOfWeek** parameter.

</dd> <dt>

**RunDayOfWeek**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

Specifies a day of the week relative to the day of the month specified in the **RunDay** property.

A value of 0 indicates no offset, that is use the exact day of the month specified in the **RunDay** property. A positive value specifies the the day of week found on or after the specified **RunDay**. A negative value specifies the the day of week found on or before the specified **RunDay**.

For example, if **RunDay** is 15 and **RunDayOfWeek** is Saturday, then the job is processed on the first Saturday on or after the 15th day in the **RunMonth**, in this case the third Saturday in the month. If **RunDay** is 20 and **RunDayOfWeek** is -Saturday, then this indicates the Saturday on or before the 20th day in the **RunMonth**. If **RunDay** is -1 and **RunDayOfWeek** is -Sunday, then this indicates the last Sunday in the **RunMonth.**

The possible values are.

<dt>

<span id="-Saturday"></span><span id="-saturday"></span><span id="-SATURDAY"></span>

**-Saturday** (-7)


</dt> <dd></dd> <dt>

<span id="-Friday"></span><span id="-friday"></span><span id="-FRIDAY"></span>

**-Friday** (-6)


</dt> <dd></dd> <dt>

<span id="-Thursday"></span><span id="-thursday"></span><span id="-THURSDAY"></span>

**-Thursday** (-5)


</dt> <dd></dd> <dt>

<span id="-Wednesday"></span><span id="-wednesday"></span><span id="-WEDNESDAY"></span>

**-Wednesday** (-4)


</dt> <dd></dd> <dt>

<span id="-Tuesday"></span><span id="-tuesday"></span><span id="-TUESDAY"></span>

**-Tuesday** (-3)


</dt> <dd></dd> <dt>

<span id="-Monday"></span><span id="-monday"></span><span id="-MONDAY"></span>

**-Monday** (-2)


</dt> <dd></dd> <dt>

<span id="-Sunday"></span><span id="-sunday"></span><span id="-SUNDAY"></span>

**-Sunday** (-1)


</dt> <dd></dd> <dt>

<span id="ExactDayOfMonth"></span><span id="exactdayofmonth"></span><span id="EXACTDAYOFMONTH"></span>

**ExactDayOfMonth** (0)


</dt> <dd></dd> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

**Sunday** (1)


</dt> <dd></dd> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

**Monday** (2)


</dt> <dd></dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

**Tuesday** (3)


</dt> <dd></dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

**Wednesday** (4)


</dt> <dd></dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

**Thursday** (5)


</dt> <dd></dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

**Friday** (6)


</dt> <dd></dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

**Saturday** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**RunMonth**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

Specifies the zero-based index of the month during which the job should be processed.

The possible values are.

<dt>

<span id="January"></span><span id="january"></span><span id="JANUARY"></span>

**January** (0)


</dt> <dd></dd> <dt>

<span id="February"></span><span id="february"></span><span id="FEBRUARY"></span>

**February** (1)


</dt> <dd></dd> <dt>

<span id="March"></span><span id="march"></span><span id="MARCH"></span>

**March** (2)


</dt> <dd></dd> <dt>

<span id="April"></span><span id="april"></span><span id="APRIL"></span>

**April** (3)


</dt> <dd></dd> <dt>

<span id="May"></span><span id="may"></span><span id="MAY"></span>

**May** (4)


</dt> <dd></dd> <dt>

<span id="June"></span><span id="june"></span><span id="JUNE"></span>

**June** (5)


</dt> <dd></dd> <dt>

<span id="July"></span><span id="july"></span><span id="JULY"></span>

**July** (6)


</dt> <dd></dd> <dt>

<span id="August"></span><span id="august"></span><span id="AUGUST"></span>

**August** (7)


</dt> <dd></dd> <dt>

<span id="September"></span><span id="september"></span><span id="SEPTEMBER"></span>

**September** (8)


</dt> <dd></dd> <dt>

<span id="October"></span><span id="october"></span><span id="OCTOBER"></span>

**October** (9)


</dt> <dd></dd> <dt>

<span id="November"></span><span id="november"></span><span id="NOVEMBER"></span>

**November** (10)


</dt> <dd></dd> <dt>

<span id="December"></span><span id="december"></span><span id="DECEMBER"></span>

**December** (11)


</dt> <dd></dd> </dl>

</dd> <dt>

**RunStartInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

Specifies the start time as an interval after midnight when the job should be processed. For example, "00000000020000.000000:000" indicates that the job should be run on or after two o'clock, either local time or UTC time depending on the value of the **LocalOrUtcTime** property.

</dd> <dt>

**ScheduledStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("**CIM\_Job**.**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

Specifies the time that the current job is scheduled to start. This time can be represented by the actual date and time, or an interval relative to the time that this property is requested. A value of all zeros indicates that the job is already executing. The property is deprecated. Instead, use the more expressive scheduling properties, **RunMonth**, **RunDay**, **RunDayOfWeek**, and **RunStartInterval**.

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates when the job was actually started. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Contains a string indicating the primary status of the object.

> [!Note]  
> This property is deprecated and replaced by the **OperationalStatus** property. If you choose to use the **Status** property for backward compatibility it should be secondary to the **OperationalStatus** property.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The possible values are.

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> <dt>



 ("No Contact")


</dt> <dd></dd> <dt>



 ("Lost Comm")


</dt> <dd></dd> <dt>



 ("Stopped")


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

Indicates descriptions of the corresponding values in the **OperationalStatus** array. For example, if an element in the **OperationalStatus** property contains the value **Stopping**, then the element at the same array index in this property might contain an explanation as to why an object is being stopped.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**TimeSubmitted**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the time that the job was submitted to execute. A value of all zeros indicates that the owning element is not capable of reporting a date and time. Therefore, the **ScheduledStartTime** and **StartTime** are reported as intervals relative to the time their values are requested.

</dd> <dt>

**UntilTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_Job**.**LocalOrUtcTime**")
</dt> </dl>

The time after which the Job is invalid or should be stopped. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. A value of all nines indicates that the Job can run indefinitely.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> </dl>

 

 





