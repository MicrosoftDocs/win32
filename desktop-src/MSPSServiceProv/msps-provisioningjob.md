---
title: Msps\_ProvisioningJob class
description: Represents an active provisioning job for a specific machine. The class provides access to job status, errors, and the fabric policy associated with the machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c750118a-5664-46b4-8232-7dd6b98ec3b3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'shielded-vm-provisioning'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Msps_ProvisioningJob class", "Msps_ProvisioningJob class, described"]
topic_type:
- apiref
api_name:
- Msps_ProvisioningJob
- Msps_ProvisioningJob.Caption
- Msps_ProvisioningJob.Description
- Msps_ProvisioningJob.ElementName
- Msps_ProvisioningJob.InstallDate
- Msps_ProvisioningJob.OperationalStatus
- Msps_ProvisioningJob.StatusDescriptions
- Msps_ProvisioningJob.Status
- Msps_ProvisioningJob.HealthState
- Msps_ProvisioningJob.CommunicationStatus
- Msps_ProvisioningJob.DetailedStatus
- Msps_ProvisioningJob.OperatingStatus
- Msps_ProvisioningJob.PrimaryStatus
- Msps_ProvisioningJob.TimeSubmitted
- Msps_ProvisioningJob.ScheduledStartTime
- Msps_ProvisioningJob.StartTime
- Msps_ProvisioningJob.ElapsedTime
- Msps_ProvisioningJob.JobRunTimes
- Msps_ProvisioningJob.RunMonth
- Msps_ProvisioningJob.RunDay
- Msps_ProvisioningJob.RunDayOfWeek
- Msps_ProvisioningJob.RunStartInterval
- Msps_ProvisioningJob.LocalOrUtcTime
- Msps_ProvisioningJob.UntilTime
- Msps_ProvisioningJob.Notify
- Msps_ProvisioningJob.Owner
- Msps_ProvisioningJob.Priority
- Msps_ProvisioningJob.PercentComplete
- Msps_ProvisioningJob.DeleteOnCompletion
- Msps_ProvisioningJob.ErrorCode
- Msps_ProvisioningJob.ErrorDescription
- Msps_ProvisioningJob.RecoveryAction
- Msps_ProvisioningJob.OtherRecoveryAction
- Msps_ProvisioningJob.InstanceID
- Msps_ProvisioningJob.Name
- Msps_ProvisioningJob.TimeOfLastStateChange
- Msps_ProvisioningJob.TimeBeforeRemoval
- Msps_ProvisioningJob.JobStatus
- Msps_ProvisioningJob.JobState
- Msps_ProvisioningJob.AdditionalIdentifier
api_location:
- MSPSService.dll
api_type:
- DllExport
---

# Msps\_ProvisioningJob class

Represents an active provisioning job for a specific machine. The class provides access to job status, errors, and the fabric policy associated with the machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), ClassVersion("1.0.0"), dynamic, provider("mspsservice"), AMENDMENT]
class Msps_ProvisioningJob : CIM_ConcreteJob
{
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  datetime TimeSubmitted;
  datetime ScheduledStartTime;
  datetime StartTime;
  datetime ElapsedTime;
  uint32   JobRunTimes = 1;
  uint8    RunMonth;
  sint8    RunDay;
  sint8    RunDayOfWeek;
  datetime RunStartInterval;
  uint16   LocalOrUtcTime;
  datetime UntilTime;
  string   Notify;
  string   Owner;
  uint32   Priority;
  uint16   PercentComplete;
  boolean  DeleteOnCompletion;
  uint16   ErrorCode;
  string   ErrorDescription;
  uint16   RecoveryAction;
  string   OtherRecoveryAction;
  string   InstanceID;
  string   Name;
  datetime TimeOfLastStateChange;
  datetime TimeBeforeRemoval = "00000000000500.000000:000";
  string   JobStatus;
  uint16   JobState;
  string   AdditionalIdentifier;
};
```

## Members

The **Msps\_ProvisioningJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Msps\_ProvisioningJob** class has these methods.



| Method                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetError**](msps-provisioningjob-geterror.md)                     | When the job is executing or has terminated without error, then this method returns no **CIM\_Error** instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then a **CIM\_Error** instance is returned.<br/> This method is inherited from [**CIM\_ConcreteJob**](cim-concretejob.md).<br/>                                                                                        |
| [**KillJob**](msps-provisioningjob-killjob.md)                       | [**KillJob**](msps-provisioningjob-killjob.md) is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. **CIM\_ConcreteJob.RequestStateChange()** provides 'Terminate' and 'Kill' options to allow this distinction.<br/> A method to kill this job and any underlying processes, and to remove any 'dangling' associations.<br/> This method is inherited from [**CIM\_Job**](cim-job.md).<br/> |
| [**RequestStateChange**](msps-provisioningjob-requeststatechange.md) | Requests that the state of the job be changed to the value specified in the **RequestedState** parameter. Invoking the **RequestStateChange** method multiple times could result in earlier requests being overwritten or lost.<br/> If 0 is returned, then the task completed successfully. Any other return code indicates an error condition.<br/> This method is inherited from [**CIM\_ConcreteJob**](cim-concretejob.md).<br/>                 |



 

### Properties

The **Msps\_ProvisioningJob** class has these properties.

<dl> <dt>

**AdditionalIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Additional identifier associated with this job instance.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**CommunicationStatus** indicates the ability of the instrumentation to communicate with the underlying **ManagedElement**.

A Null return indicates the implementation (provider) does not implement this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

**Unknown** - indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

</dd> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)


</dt> <dd>

**Not Available** - indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property).

</dd> <dt>

<span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span>

<span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span>**Communication OK** (2)


</dt> <dd>

**Communication OK** - indicates communication is established with the element, but does not convey any quality of service.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (3)


</dt> <dd>

**Lost Communication** - indicates that the Managed Element is known to exist and has been contacted successfully in the past, but is currently unreachable.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (4)


</dt> <dd>

**No Contact** - indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

**DMTF Reserved**

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

**Vendor Reserved**

</dd> </dl>

</dd> <dt>

**DeleteOnCompletion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether or not the job should be automatically deleted upon completion. Note that the 'completion' of a recurring job is defined by its **JobRunTimes** or **UntilTime** properties, or when the Job is terminated by manual intervention. If this property is set to false and the job completes, then the extrinsic method **DeleteInstance** must be used to delete the job instead of updating this property.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.PrimaryStatus", "CIM\_ManagedSystemElement.HealthState")
</dt> </dl>

Compliments **PrimaryStatus** with additional status detail. This property is used to expand upon the **PrimaryStatus** of the element.

A Null return indicates the implementation (provider) does not implement this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (0)


</dt> <dd>

Not Available - indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property).

</dd> <dt>

<span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span>

<span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span>**No Additional Information** (1)


</dt> <dd>

**No Additional Information** - indicates that the element is functioning normally as indicated by **PrimaryStatus** = "OK".

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (2)


</dt> <dd>

**Stressed** - indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (3)


</dt> <dd>

**Predictive Failure** - indicates that an element is functioning normally but a failure is predicted in the near future.

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (4)


</dt> <dd>

**Non-Recoverable Error** - indicates that this element is in an error condition that requires human intervention.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (5)


</dt> <dd>

**Supporting Entity in Error** - indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

**DMTF Reserved**

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

**Vendor Reserved**

</dd> </dl>

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval that the Job has been executing or the total execution time if the Job is complete. Note that this property is also present in the **JobProcessingStatistics** class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

Note that the **Name** property of **CIM\_ManagedSystemElement** is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of **LogicalDevice**), the same information can be present in both the **Name** and **ElementName** properties. Note that if there is an associated instance of **CIM\_EnabledLogicalElementCapabilities,** restrictions on this properties may exist as defined in **ElementNameMask** and **MaxElementNameLen** properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**ErrorDescription**")
</dt> </dl>

A vendor-specific error code. The value must be set to zero if the Job completed without error. Note that this property is also present in the **JobProcessingStatistics** class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**ErrorCode**")
</dt> </dl>

A free-form string that contains the vendor error description. Note that this property is also present in the **JobProcessingStatistics** class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

**Unknown** - The implementation cannot report on **HealthState** at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (5)


</dt> <dd>

**OK** - The element is fully functional and is operating within normal operational parameters and without error.

</dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>**Degraded/Warning** (10)


</dt> <dd>

**Degraded/Warning** - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors.

</dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>**Minor failure** (15)


</dt> <dd>

**Minor failure** - All functionality is available but some might be degraded.

</dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>**Major failure** (20)


</dt> <dd>

**Major failure** - The element is failing. It is possible that some or all of the functionality of this component is degraded or not working.

</dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>**Critical failure** (25)


</dt> <dd>

**Critical failure** - The element is non-functional and recovery might not be possible.

</dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-recoverable error** (30)


</dt> <dd>

**Non-recoverable error** - The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

DMTF Reserved - DMTF has reserved the unused portion of the continuum for additional **HealthStates** in the future.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A **datetime** value that indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following \\'preferred\\' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon \\':\\', and where &lt;OrgID&gt; must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID, or that is a registered ID that is assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; must not contain a colon (\\':\\'). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be re-used to identify different underlying (real-world) elements. If the above \\'preferred\\' algorithm is not used, the defining entity must assure that the resulting InstanceID is not re-used across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

For DMTF defined instances, the \\'preferred\\' algorithm must be used with the &lt;OrgID&gt; set to \\'CIM\\'.

This property is inherited from [**CIM\_ConcreteJob**](cim-concretejob.md).

</dd> <dt>

**JobRunTimes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of times that the Job should be run. A value of 1 indicates that the Job is not recurring, while any non-zero value indicates a limit to the number of times that the Job will recur. Zero indicates that there is no limit to the number of times that the Job can be processed, but that it is terminated either after the **UntilTime** or by manual intervention. By default, a Job is processed once.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**JobState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("JobState")
</dt> </dl>

The current execution state of the provisioning job. **PendingBoot** - The provisioning job is waiting for the machine to boot. **Running** - Provisioning is in progress. **Completed** - The Shielded VM has been successfully provisioned. The job is complete.

<dt>

<span id="New"></span><span id="new"></span><span id="NEW"></span>

**New** (2)


</dt> <dd></dd> <dt>

<span id="PendingBoot"></span><span id="pendingboot"></span><span id="PENDINGBOOT"></span>

**PendingBoot** (3)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (4)


</dt> <dd></dd> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

**Suspended** (5)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (6)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (7)


</dt> <dd></dd> <dt>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>

**Terminated** (8)


</dt> <dd></dd> <dt>

<span id="Killed"></span><span id="killed"></span><span id="KILLED"></span>

**Killed** (9)


</dt> <dd></dd> <dt>

<span id="Exception"></span><span id="exception"></span><span id="EXCEPTION"></span>

**Exception** (10)


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** (11)


</dt> <dd></dd> <dt>

<span id="Query_Pending"></span><span id="query_pending"></span><span id="QUERY_PENDING"></span>

**Query Pending** (12)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>13–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**JobStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**")
</dt> </dl>

The current status of the provisioning job.

This property is inherited from [**CIM\_Job**](cim-job.md).

<dt>


</dt> <dd>

**Complete** - The Shielded VM has been successfully provisioned. The job is complete.

</dd> <dt>


</dt> <dd>

**InProgress** - Provisioning is in progress.

</dd> <dt>


</dt> <dd>

**PendingBoot** - The provisioning job is pending the initial boot sequence.

</dd> <dt>


</dt> <dd>

**Failed** - There was an error while provisioning the machine. [**GetError**](msps-provisioningjob-geterror.md) for more details.

</dd> </dl>

</dd> <dt>

**LocalOrUtcTime**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property indicates whether the times represented in the **RunStartInterval** and **UntilTime** properties represent local times or UTC times. Time values are synchronized worldwide by using the enumeration value 2, "UTC Time".

This property is inherited from [**CIM\_Job**](cim-job.md).

<dt>

<span id="Local_Time"></span><span id="local_time"></span><span id="LOCAL_TIME"></span>

<span id="Local_Time"></span><span id="local_time"></span><span id="LOCAL_TIME"></span>**Local Time** (1)


</dt> <dd>

**Local Time**

</dd> <dt>

<span id="UTC_Time"></span><span id="utc_time"></span><span id="UTC_TIME"></span>

<span id="UTC_Time"></span><span id="utc_time"></span><span id="UTC_TIME"></span>**UTC Time** (2)


</dt> <dd>

**UTC Time**

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024), [**Required**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name")
</dt> </dl>

The user-friendly name for this instance of a Job. In addition, the user-friendly name can be used as a property for a search or query. (Note: Name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_ConcreteJob**](cim-concretejob.md).

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The User who is to be notified upon the Job completion or failure.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

Provides a current status value for the operational condition of the element and can be used for providing more detail with respect to the value of **EnabledState**. It can also provide the transitional states when an element is transitioning from one state to another, such as when an element is transitioning between **EnabledState** and **RequestedState**, as well as other transitional conditions.

A Null return indicates the implementation (provider) does not implement this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

**Unknown** - indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

</dd> <dt>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>

<span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span>**Not Available** (1)


</dt> <dd>

**Not Available** - indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property).

</dd> <dt>

<span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span>

<span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span>**Servicing** (2)


</dt> <dd>

**Servicing** - describes an element being configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (3)


</dt> <dd>

**Starting** - describes an element being initialized.

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (4)


</dt> <dd>

**Stopping** - describes an element being brought to an orderly stop.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (5)


</dt> <dd>

**Stopped** - describes an orderly stop.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (6)


</dt> <dd>

**Aborted** - describes an abrupt stop where the state and configuration of the element might need to be updated.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (7)


</dt> <dd>

**Dormant** - indicates that the element is inactive or quiesced.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (8)


</dt> <dd>

**Completed** - indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded in the **PrimaryStatus** so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error).

</dd> <dt>

<span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span>

<span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span>**Migrating** (9)


</dt> <dd>

**Migrating** - element is being moved between host elements.

</dd> <dt>

<span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span>

<span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span>**Emigrating** (10)


</dt> <dd>

**Emigrating** - element is being moved away from host element.

</dd> <dt>

<span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span>

<span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span>**Immigrating** (11)


</dt> <dd>

**Immigrating** - element is being moved to new host element.

</dd> <dt>

<span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span>

<span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span>**Snapshotting** (12)


</dt> <dd>

**Snapshotting**

</dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (13)


</dt> <dd>

**Shutting Down** - describes an element being brought to an abrupt stop.

</dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (14)


</dt> <dd>

**In Test** - element is performing test functions.

</dd> <dt>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>**Transitioning** (15)


</dt> <dd>

**Transitioning** - describes an element that is between states, that is, it is not fully available in either its previous state or its next state. This value should be used if other values indicating a transition to a specific state are not applicable.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (16)


</dt> <dd>

**In Service** - describes an element that is in service and operational.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

**DMTF Reserved**

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

**Vendor Reserved**

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

Indicates the current statuses of the element.

**OperationalStatus** replaces the **Status** property on **ManagedSystemElement** to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the **Status** and **OperationalStatus** properties. Further, the first value of **OperationalStatus** should contain the primary status for the element. When instrumented, **Status** (because it is single-valued) should also provide the primary status of the element.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

**Unknown**

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

**Other**

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (2)


</dt> <dd>

**OK**

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)


</dt> <dd>

**Degraded**

</dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)


</dt> <dd>

**Stressed** - indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on.

</dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)


</dt> <dd>

**Predictive Failure** - indicates that an element is functioning nominally but predicting a failure in the near future.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)


</dt> <dd>

**Error**

</dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)


</dt> <dd>

**Non-Recoverable Error**

</dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)


</dt> <dd>

**Starting**

</dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)


</dt> <dd>

**Stopping**

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)


</dt> <dd>

**Stopped** - indicates that a clean and orderly stop has occurred.

</dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)


</dt> <dd>

**In Service** - describes an element being configured, maintained, cleaned, or otherwise administered.

</dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)


</dt> <dd>

**No Contact** - indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

</dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)


</dt> <dd>

**Lost Communication** - indicates that the **ManagedSystemElement** is known to exist and has been contacted successfully in the past, but is currently unreachable.

</dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)


</dt> <dd>

**Aborted** - indicates that an abrupt stop has occurred, where the state and configuration of the element might need to be updated.

</dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)


</dt> <dd>

**Dormant** - indicates that the element is inactive or quiesced.

</dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)


</dt> <dd>

**Supporting Entity in Error** - indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

</dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)


</dt> <dd>

**Completed** - indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error).

</dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)


</dt> <dd>

**Power Mode** - indicates that the element has additional power model information contained in the Associated **PowerManagementService** association.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

**DMTF Reserved**

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

**Vendor Reserved**

</dd> </dl>

</dd> <dt>

**OtherRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**RecoveryAction**")
</dt> </dl>

A string describing the recovery action when the **RecoveryAction** property of the instance is 1 ("Other").

This property is inherited from [**CIM\_Job**](cim-job.md).

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

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**PercentComplete**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("0"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("101"), **PUnit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percent")
</dt> </dl>

The percentage of the job that has completed at the time that this value is requested. Note that this property is also present in the **JobProcessingStatistics** class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run data can be stored in this single-valued property.

Note that the value 101 is undefined and will be not be allowed in the next major revision of the specification.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ManagedSystemElement.DetailedStatus", "CIM\_ManagedSystemElement.HealthState")
</dt> </dl>

Provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with **DetailedStatus** to provide high level and detailed health status of the Managed Element and its subcomponents.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

**Unknown** - indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

</dd> <dt>

<span id="OK"></span><span id="ok"></span>

<span id="OK"></span><span id="ok"></span>**OK** (1)


</dt> <dd>

**OK** - indicates the Managed Element is functioning normally.

</dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (2)


</dt> <dd>

**Degraded** - indicates the managed element is functioning below normal.

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)


</dt> <dd>

**Error** - indicates the managed element is in an Error condition.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

**DMTF Reserved**

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd>

**Vendor Reserved**

</dd> </dl>

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the urgency or importance of execution of the Job. The lower the number, the higher the priority. Note that this property is also present in the **JobProcessingStatistics** class. This class is necessary to capture the setting information that would influence the results of a job.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**RecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**OtherRecoveryAction**")
</dt> </dl>

Describes the recovery action to be taken for an unsuccessfully run Job. The possible values are:

This property is inherited from [**CIM\_Job**](cim-job.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd>

**Unknown** - meaning it is unknown as to what recovery action to take.

</dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

**Other** - indicating that the recovery action will be specified in the **OtherRecoveryAction** property.

</dd> <dt>

<span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span>

<span id="Do_Not_Continue"></span><span id="do_not_continue"></span><span id="DO_NOT_CONTINUE"></span>**Do Not Continue** (2)


</dt> <dd>

**Do Not Continue** - meaning stop the execution of the job and appropriately update its status.

</dd> <dt>

<span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span>

<span id="Continue_With_Next_Job"></span><span id="continue_with_next_job"></span><span id="CONTINUE_WITH_NEXT_JOB"></span>**Continue With Next Job** (3)


</dt> <dd>

**Continue With Next Job** - meaning continue with the next job in the queue .

</dd> <dt>

<span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span>

<span id="Re-run_Job"></span><span id="re-run_job"></span><span id="RE-RUN_JOB"></span>**Re-run Job** (4)


</dt> <dd>

**Re-run Job** - indicating that the job should be re-run.

</dd> <dt>

<span id="Run_Recovery_Job"></span><span id="run_recovery_job"></span><span id="RUN_RECOVERY_JOB"></span>

<span id="Run_Recovery_Job"></span><span id="run_recovery_job"></span><span id="RUN_RECOVERY_JOB"></span>**Run Recovery Job** (5)


</dt> <dd>

**Run Recovery Job** - meaning run the Job associated using the RecoveryJob relationship. Note that the recovery Job must already be in the queue from which it will run.

</dd> </dl>

</dd> <dt>

**RunDay**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) ("-31"), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) ("31"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**RunMonth**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

The day in the month on which the Job should be processed. There are two different interpretations for this property, depending on the value of **DayOfWeek**. In one case, **RunDay** defines the day-in-month on which the Job is processed. This interpretation is used when the **DayOfWeek** is 0. A positive or negative integer indicates whether the **RunDay** should be calculated from the beginning or end of the month. For example, 5 indicates the fifth day in the **RunMonth** and -1 indicates the last day in the **RunMonth**.

When **RunDayOfWeek** is not 0, **RunDay** is the day-in-month on which the Job is processed, defined in conjunction with **RunDayOfWeek**. For example, if **RunDay** is 15 and **RunDayOfWeek** is Saturday, then the Job is processed on the first Saturday on or after the 15th day in the **RunMonth** (for example, the third Saturday in the month). If **RunDay** is 20 and **RunDayOfWeek** is -Saturday, then this indicates the first Saturday on or before the 20th day in the **RunMonth**. If **RunDay** is -1 and **RunDayOfWeek** is -Sunday, then this indicates the last Sunday in the **RunMonth.**

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**RunDayOfWeek**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

A positive or negative integer used in conjunction with RunDay to indicate the day of the week on which the Job is processed. **RunDayOfWeek** is set to 0 to indicate an exact day of the month, such as March 1. A positive integer (representing Sunday, Monday, ..., Saturday) means that the day of week is found on or after the specified **RunDay**. A negative integer (representing -Sunday, -Monday, ..., -Saturday) means that the day of week is found on or BEFORE the **RunDay.**

This property is inherited from [**CIM\_Job**](cim-job.md).

<dt>

<span id="-Saturday"></span><span id="-saturday"></span><span id="-SATURDAY"></span>

<span id="-Saturday"></span><span id="-saturday"></span><span id="-SATURDAY"></span>**-Saturday** (-7)


</dt> <dd>

**-Saturday**

</dd> <dt>

<span id="-Friday"></span><span id="-friday"></span><span id="-FRIDAY"></span>

<span id="-Friday"></span><span id="-friday"></span><span id="-FRIDAY"></span>**-Friday** (-6)


</dt> <dd>

**-Friday**

</dd> <dt>

<span id="-Thursday"></span><span id="-thursday"></span><span id="-THURSDAY"></span>

<span id="-Thursday"></span><span id="-thursday"></span><span id="-THURSDAY"></span>**-Thursday** (-5)


</dt> <dd>

**-Thursday**

</dd> <dt>

<span id="-Wednesday"></span><span id="-wednesday"></span><span id="-WEDNESDAY"></span>

<span id="-Wednesday"></span><span id="-wednesday"></span><span id="-WEDNESDAY"></span>**-Wednesday** (-4)


</dt> <dd>

**-Wednesday**

</dd> <dt>

<span id="-Tuesday"></span><span id="-tuesday"></span><span id="-TUESDAY"></span>

<span id="-Tuesday"></span><span id="-tuesday"></span><span id="-TUESDAY"></span>**-Tuesday** (-3)


</dt> <dd>

**-Tuesday**

</dd> <dt>

<span id="-Monday"></span><span id="-monday"></span><span id="-MONDAY"></span>

<span id="-Monday"></span><span id="-monday"></span><span id="-MONDAY"></span>**-Monday** (-2)


</dt> <dd>

**-Monday**

</dd> <dt>

<span id="-Sunday"></span><span id="-sunday"></span><span id="-SUNDAY"></span>

<span id="-Sunday"></span><span id="-sunday"></span><span id="-SUNDAY"></span>**-Sunday** (-1)


</dt> <dd>

**-Sunday**

</dd> <dt>

<span id="ExactDayOfMonth"></span><span id="exactdayofmonth"></span><span id="EXACTDAYOFMONTH"></span>

<span id="ExactDayOfMonth"></span><span id="exactdayofmonth"></span><span id="EXACTDAYOFMONTH"></span>**ExactDayOfMonth** (0)


</dt> <dd>

**ExactDayOfMonth**

</dd> <dt>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>

<span id="Sunday"></span><span id="sunday"></span><span id="SUNDAY"></span>**Sunday** (1)


</dt> <dd>

**Sunday**

</dd> <dt>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>

<span id="Monday"></span><span id="monday"></span><span id="MONDAY"></span>**Monday** (2)


</dt> <dd>

**Monday**

</dd> <dt>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>

<span id="Tuesday"></span><span id="tuesday"></span><span id="TUESDAY"></span>**Tuesday** (3)


</dt> <dd>

**Tuesday**

</dd> <dt>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>

<span id="Wednesday"></span><span id="wednesday"></span><span id="WEDNESDAY"></span>**Wednesday** (4)


</dt> <dd>

**Wednesday**

</dd> <dt>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>

<span id="Thursday"></span><span id="thursday"></span><span id="THURSDAY"></span>**Thursday** (5)


</dt> <dd>

**Thursday**

</dd> <dt>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>

<span id="Friday"></span><span id="friday"></span><span id="FRIDAY"></span>**Friday** (6)


</dt> <dd>

**Friday**

</dd> <dt>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>

<span id="Saturday"></span><span id="saturday"></span><span id="SATURDAY"></span>**Saturday** (7)


</dt> <dd>

**Saturday**

</dd> </dl>

</dd> <dt>

**RunMonth**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Job.RunDay", "CIM\_Job.RunDayOfWeek", "CIM\_Job.RunStartInterval")
</dt> </dl>

The month during which the Job should be processed. Specify 0 for January, 1 for February, and so on.

This property is inherited from [**CIM\_Job**](cim-job.md).

<dt>

<span id="January"></span><span id="january"></span><span id="JANUARY"></span>

<span id="January"></span><span id="january"></span><span id="JANUARY"></span>**January** (0)


</dt> <dd>

**January**

</dd> <dt>

<span id="February"></span><span id="february"></span><span id="FEBRUARY"></span>

<span id="February"></span><span id="february"></span><span id="FEBRUARY"></span>**February** (1)


</dt> <dd>

**February**

</dd> <dt>

<span id="March"></span><span id="march"></span><span id="MARCH"></span>

<span id="March"></span><span id="march"></span><span id="MARCH"></span>**March** (2)


</dt> <dd>

**March**

</dd> <dt>

<span id="April"></span><span id="april"></span><span id="APRIL"></span>

<span id="April"></span><span id="april"></span><span id="APRIL"></span>**April** (3)


</dt> <dd>

**April**

</dd> <dt>

<span id="May"></span><span id="may"></span><span id="MAY"></span>

<span id="May"></span><span id="may"></span><span id="MAY"></span>**May** (4)


</dt> <dd>

**May**

</dd> <dt>

<span id="June"></span><span id="june"></span><span id="JUNE"></span>

<span id="June"></span><span id="june"></span><span id="JUNE"></span>**June** (5)


</dt> <dd>

**June**

</dd> <dt>

<span id="July"></span><span id="july"></span><span id="JULY"></span>

<span id="July"></span><span id="july"></span><span id="JULY"></span>**July** (6)


</dt> <dd>

**July**

</dd> <dt>

<span id="August"></span><span id="august"></span><span id="AUGUST"></span>

<span id="August"></span><span id="august"></span><span id="AUGUST"></span>**August** (7)


</dt> <dd>

**August**

</dd> <dt>

<span id="September"></span><span id="september"></span><span id="SEPTEMBER"></span>

<span id="September"></span><span id="september"></span><span id="SEPTEMBER"></span>**September** (8)


</dt> <dd>

**September**

</dd> <dt>

<span id="October"></span><span id="october"></span><span id="OCTOBER"></span>

<span id="October"></span><span id="october"></span><span id="OCTOBER"></span>**October** (9)


</dt> <dd>

**October**

</dd> <dt>

<span id="November"></span><span id="november"></span><span id="NOVEMBER"></span>

<span id="November"></span><span id="november"></span><span id="NOVEMBER"></span>**November** (10)


</dt> <dd>

**November**

</dd> <dt>

<span id="December"></span><span id="december"></span><span id="DECEMBER"></span>

<span id="December"></span><span id="december"></span><span id="DECEMBER"></span>**December** (11)


</dt> <dd>

**December**

</dd> </dl>

</dd> <dt>

**RunStartInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**RunMonth**", "**CIM\_Job**.**RunDay**", "**CIM\_Job**.**RunDayOfWeek**", "**CIM\_Job**.**RunStartInterval**")
</dt> </dl>

The time interval after midnight when the Job should be processed. For example,

00000000020000.000000:000

indicates that the Job should be run on or after two o'clock, local time or UTC time (distinguished using the **LocalOrUtcTime** property.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**ScheduledStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("CIM\_Job.RunMonth", "CIM\_Job.RunDay", "CIM\_Job.RunDayOfWeek", "CIM\_Job.RunStartInterval")
</dt> </dl>

The time that the current Job is scheduled to start. This time can be represented by the actual date and time, or an interval relative to the time that this property is requested. A value of all zeroes indicates that the Job is already executing. The property is deprecated in lieu of the more expressive scheduling properties, **RunMonth**, **RunDay**, **RunDayOfWeek**, and **RunStartInterval.**

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time that the Job was actually started. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. Note that this property is also present in the **JobProcessingStatistics** class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).**OperationalStatus**"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the object. Various operational and non-operational statuses are defined. This property is deprecated in lieu of **OperationalStatus**, which includes the same semantics in its enumeration. This change is made for 3 reasons:

1) Status is more correctly defined as an array. This definition overcomes the limitation of describing status using a single value, when it is really a multi-valued property (for example, an element might be OK AND Stopped.

2) A MaxLen of 10 is too restrictive and leads to unclear enumerated values.

3) The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property and did not want to modify their code. Therefore, Status was grandfathered into the Schema. Use of the deprecated qualifier allows the maintenance of the existing property, but also permits an improved definition using **OperationalStatus.**

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

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

Strings describing the various **OperationalStatus** array values. For example, if "Stopping" is the value assigned to **OperationalStatus**, then this property may contain an explanation as to why an object is being stopped. Note that entries in this array are correlated with those at the same array index in **OperationalStatus.**

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**TimeBeforeRemoval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The amount of time that the Job is retained after it has finished executing, either succeeding or failing in that execution. The job must remain in existence for some period of time regardless of the value of the DeleteOnCompletion property.

The default is five minutes.

This property is inherited from [**CIM\_ConcreteJob**](cim-concretejob.md).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the state of the Job last changed. If the state of the Job has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_ConcreteJob**](cim-concretejob.md).

</dd> <dt>

**TimeSubmitted**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time that the Job was submitted to execute. A value of all zeroes indicates that the owning element is not capable of reporting a date and time. Therefore, the **ScheduledStartTime** and **StartTime** are reported as intervals relative to the time their values are requested.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> <dt>

**UntilTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_Job**](cim-job.md).**LocalOrUtcTime**")
</dt> </dl>

The time after which the Job is invalid or should be stopped. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. A value of all nines indicates that the Job can run indefinitely.

This property is inherited from [**CIM\_Job**](cim-job.md).

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Namespace<br/>                | Root\\MSPS<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>MSPSService.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MSPSService.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 





