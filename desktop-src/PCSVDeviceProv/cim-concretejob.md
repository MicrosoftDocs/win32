---
Description: 'A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '53c9d39b-67a9-409c-80bc-af745be77ce0'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CIM\_ConcreteJob class'
---

# CIM\_ConcreteJob class

A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), Version("2.22.0"), AMENDMENT]
class CIM_ConcreteJob : CIM_Job
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
  string   JobStatus;
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
  uint16   JobState;
  datetime TimeOfLastStateChange;
  datetime TimeBeforeRemoval = 00000000000500.000000:000";
};
```

## Members

The **CIM\_ConcreteJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_ConcreteJob** class has these methods.



| Method                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetError**](geterror-cim-concretejob.md)                     | When the job is executing or has terminated without error, then this method returns no CIM\_Error instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then a CIM\_Error instance is returned.<br/>                                                                                                                                   |
| [**KillJob**](cim-concretejob-killjob.md)                       | KillJob is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. CIM\_ConcreteJob.RequestStateChange() provides 'Terminate' and 'Kill' options to allow this distinction. A method to kill this job and any underlying processes, and to remove any 'dangling' associations.<br/> This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).<br/> |
| [**RequestStateChange**](requeststatechange-cim-concretejob.md) | Requests that the state of the job be changed to the value specified in the RequestedState parameter. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully. Any other return code indicates an error condition.<br/>                                                                       |



 

### Properties

The **CIM\_ConcreteJob** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CommunicationStatus indicates the ability of the instrumentation to communicate with the underlying ManagedElement. CommunicationStatus consists of one of the following values: Unknown, None, Communication OK, Lost Communication, or No Contact. A Null return indicates the implementation (provider) does not implement this property. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. "Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). "Communication OK " indicates communication is established with the element, but does not convey any quality of service. "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. "Lost Communication" indicates that the Managed Element is known to exist and has been contacted successfully in the past, but is currently unreachable.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Not Available

</dd> <dt>

2
</dt> <dd>

Communication OK

</dd> <dt>

3
</dt> <dd>

Lost Communication

</dd> <dt>

4
</dt> <dd>

No Contact

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**DeleteOnCompletion**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether or not the job should be automatically deleted upon completion. Note that the 'completion' of a recurring job is defined by its JobRunTimes or UntilTime properties, or when the Job is terminated by manual intervention. If this property is set to false and the job completes, then the extrinsic method DeleteInstance must be used to delete the job instead of updating this property.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_EnabledLogicalElement.PrimaryStatus), **Model Correspondence** (CIM\_ManagedSystemElement.HealthState)
</dt> </dl>

DetailedStatus compliments PrimaryStatus with additional status detail. It consists of one of the following values: Not Available, No Additional Information, Stressed, Predictive Failure, Error, Non-Recoverable Error, SupportingEntityInError. Detailed status is used to expand upon the PrimaryStatus of the element. A Null return indicates the implementation (provider) does not implement this property. "Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). "No Additional Information" indicates that the element is functioning normally as indicated by PrimaryStatus = "OK". "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. "Predictive Failure" indicates that an element is functioning normally but a failure is predicted in the near future. "Non-Recoverable Error " indicates that this element is in an error condition that requires human intervention. "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

0
</dt> <dd>

Not Available

</dd> <dt>

1
</dt> <dd>

No Additional Information

</dd> <dt>

2
</dt> <dd>

Stressed

</dd> <dt>

3
</dt> <dd>

Predictive Failure

</dd> <dt>

4
</dt> <dd>

Non-Recoverable Error

</dd> <dt>

5
</dt> <dd>

Supporting Entity in Error

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**ElapsedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval that the Job has been executing or the total execution time if the Job is complete. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM\_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**ErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.ErrorDescription)
</dt> </dl>

A vendor-specific error code. The value must be set to zero if the Job completed without error. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.ErrorCode)
</dt> </dl>

A free-form string that contains the vendor error description. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. The following continuum is defined: "Non-recoverable Error" (30) - The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost. "Critical Failure" (25) - The element is non-functional and recovery might not be possible. "Major Failure" (20) - The element is failing. It is possible that some or all of the functionality of this component is degraded or not working. "Minor Failure" (15) - All functionality is available but some might be degraded. "Degraded/Warning" (10) - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors. "OK" (5) - The element is fully functional and is operating within normal operational parameters and without error. "Unknown" (0) - The implementation cannot report on HealthState at this time. DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

5
</dt> <dd>

OK

</dd> <dt>

10
</dt> <dd>

Degraded/Warning

</dd> <dt>

15
</dt> <dd>

Minor failure

</dd> <dt>

20
</dt> <dd>

Major failure

</dd> <dt>

25
</dt> <dd>

Critical failure

</dd> <dt>

30
</dt> <dd>

Non-recoverable error

</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A datetime value that indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID, or that is a registered ID that is assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; must not contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and should not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity must assure that the resulting InstanceID is not re-used across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF defined instances, the 'preferred' algorithm must be used with the &lt;OrgID&gt; set to 'CIM'.

</dd> <dt>

**JobRunTimes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of times that the Job should be run. A value of 1 indicates that the Job is not recurring, while any non-zero value indicates a limit to the number of times that the Job will recur. Zero indicates that there is no limit to the number of times that the Job can be processed, but that it is terminated either after the UntilTime or by manual intervention. By default, a Job is processed once.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**JobState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

JobState is an integer enumeration that indicates the operational state of a Job. It can also indicate transitions between these states, for example, 'Shutting Down' and 'Starting'. Following is a brief description of the states: New (2) indicates that the job has never been started. Starting (3) indicates that the job is moving from the 'New', 'Suspended', or 'Service' states into the 'Running' state. Running (4) indicates that the Job is running. Suspended (5) indicates that the Job is stopped, but can be restarted in a seamless manner. Shutting Down (6) indicates that the job is moving to a 'Completed', 'Terminated', or 'Killed' state. Completed (7) indicates that the job has completed normally. Terminated (8) indicates that the job has been stopped by a 'Terminate' state change request. The job and all its underlying processes are ended and can be restarted (this is job-specific) only as a new job. Killed (9) indicates that the job has been stopped by a 'Kill' state change request. Underlying processes might have been left running, and cleanup might be required to free up resources. Exception (10) indicates that the Job is in an abnormal state that might be indicative of an error condition. Actual status might be displayed though job-specific objects. Service (11) indicates that the Job is in a vendor-specific state that supports problem discovery, or resolution, or both.Query pending (12) waiting for a client to resolve a query

<dt>

<span id="New"></span><span id="new"></span><span id="NEW"></span>

<span id="New"></span><span id="new"></span><span id="NEW"></span>**New** (2)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (3)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (4)


</dt> <dd></dd> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>**Suspended** (5)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>**Shutting Down** (6)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (7)


</dt> <dd></dd> <dt>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>

<span id="Terminated"></span><span id="terminated"></span><span id="TERMINATED"></span>**Terminated** (8)


</dt> <dd></dd> <dt>

<span id="Killed"></span><span id="killed"></span><span id="KILLED"></span>

<span id="Killed"></span><span id="killed"></span><span id="KILLED"></span>**Killed** (9)


</dt> <dd></dd> <dt>

<span id="Exception"></span><span id="exception"></span><span id="EXCEPTION"></span>

<span id="Exception"></span><span id="exception"></span><span id="EXCEPTION"></span>**Exception** (10)


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>**Service** (11)


</dt> <dd></dd> <dt>

<span id="Query_Pending"></span><span id="query_pending"></span><span id="QUERY_PENDING"></span>

<span id="Query_Pending"></span><span id="query_pending"></span><span id="QUERY_PENDING"></span>**Query Pending** (12)


</dt> <dd></dd> <dt>

13–32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768–65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

</dd> <dt>

**JobStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_ManagedSystemElement.OperationalStatus)
</dt> </dl>

A free-form string that represents the status of the job. The primary status is reflected in the inherited OperationalStatus property. JobStatus provides additional, implementation-specific details.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**LocalOrUtcTime**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property indicates whether the times represented in the RunStartInterval and UntilTime properties represent local times or UTC times. Time values are synchronized worldwide by using the enumeration value 2, "UTC Time".

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

<dt>

1
</dt> <dd>

Local Time

</dd> <dt>

2
</dt> <dd>

UTC Time

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

</dd> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The User who is to be notified upon the Job completion or failure.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_EnabledLogicalElement.EnabledState)
</dt> </dl>

OperatingStatus provides a current status value for the operational condition of the element and can be used for providing more detail with respect to the value of EnabledState. It can also provide the transitional states when an element is transitioning from one state to another, such as when an element is transitioning between EnabledState and RequestedState, as well as other transitional conditions.OperatingStatus consists of one of the following values: Unknown, Not Available, In Service, Starting, Stopping, Stopped, Aborted, Dormant, Completed, Migrating, Emmigrating, Immigrating, Snapshotting. Shutting Down, In Test A Null return indicates the implementation (provider) does not implement this property. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. "None" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). "Servicing" describes an element being configured, maintained, cleaned, or otherwise administered. "Starting" describes an element being initialized. "Stopping" describes an element being brought to an orderly stop. "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. "Dormant" indicates that the element is inactive or quiesced. "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded in the PrimaryStatus so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). "Migrating" element is being moved between host elements. "Immigrating" element is being moved to new host element. "Emigrating" element is being moved away from host element. "Shutting Down" describes an element being brought to an abrupt stop. "In Test" element is performing test functions. "Transitioning" describes an element that is between states, that is, it is not fully available in either its previous state or its next state. This value should be used if other values indicating a transition to a specific state are not applicable."In Service" describes an element that is in service and operational.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Not Available

</dd> <dt>

2
</dt> <dd>

Servicing

</dd> <dt>

3
</dt> <dd>

Starting

</dd> <dt>

4
</dt> <dd>

Stopping

</dd> <dt>

5
</dt> <dd>

Stopped

</dd> <dt>

6
</dt> <dd>

Aborted

</dd> <dt>

7
</dt> <dd>

Dormant

</dd> <dt>

8
</dt> <dd>

Completed

</dd> <dt>

9
</dt> <dd>

Migrating

</dd> <dt>

10
</dt> <dd>

Emigrating

</dd> <dt>

11
</dt> <dd>

Immigrating

</dd> <dt>

12
</dt> <dd>

Snapshotting

</dd> <dt>

13
</dt> <dd>

Shutting Down

</dd> <dt>

14
</dt> <dd>

In Test

</dd> <dt>

15
</dt> <dd>

Transitioning

</dd> <dt>

16
</dt> <dd>

In Service

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_ManagedSystemElement.StatusDescriptions), **Override**, **ArrayType** ("Indexed")
</dt> </dl>

Indicates the current statuses of the element. Various operational statuses are defined. Many of the enumeration's values are self-explanatory. However, a few are not and are described here in more detail. "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. "Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future. "In Service" describes an element being configured, maintained, cleaned, or otherwise administered. "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. "Lost Communication" indicates that the ManagedSystem Element is known to exist and has been contacted successfully in the past, but is currently unreachable. "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. "Dormant" indicates that the element is inactive or quiesced. "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems. "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). "Power Mode" indicates that the element has additional power model information contained in the Associated PowerManagementService association. OperationalStatus replaces the Status property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the Status and OperationalStatus properties. Further, the first value of OperationalStatus should contain the primary status for the element. When instrumented, Status (because it is single-valued) should also provide the primary status of the element.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Other

</dd> <dt>

2
</dt> <dd>

OK

</dd> <dt>

3
</dt> <dd>

Degraded

</dd> <dt>

4
</dt> <dd>

Stressed

</dd> <dt>

5
</dt> <dd>

Predictive Failure

</dd> <dt>

6
</dt> <dd>

Error

</dd> <dt>

7
</dt> <dd>

Non-Recoverable Error

</dd> <dt>

8
</dt> <dd>

Starting

</dd> <dt>

9
</dt> <dd>

Stopping

</dd> <dt>

10
</dt> <dd>

Stopped

</dd> <dt>

11
</dt> <dd>

In Service

</dd> <dt>

12
</dt> <dd>

No Contact

</dd> <dt>

13
</dt> <dd>

Lost Communication

</dd> <dt>

14
</dt> <dd>

Aborted

</dd> <dt>

15
</dt> <dd>

Dormant

</dd> <dt>

16
</dt> <dd>

Supporting Entity in Error

</dd> <dt>

17
</dt> <dd>

Completed

</dd> <dt>

18
</dt> <dd>

Power Mode

</dd> <dt>

..–..
</dt> <dd>

DMTF Reserved

</dd> <dt>

0x8000..–0x8000..
</dt> <dd>

Vendor Reserved

</dd> </dl>

</dd> <dt>

**OtherRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.RecoveryAction)
</dt> </dl>

A string describing the recovery action when the RecoveryAction property of the instance is 1 ("Other").

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_OwningJobElement)
</dt> </dl>

The User that submitted the Job, or the Service or method name that caused the job to be created.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**PercentComplete**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MinValue** ("0"), **MaxValue** ("101"), **Units** ("percent")
</dt> </dl>

The percentage of the job that has completed at the time that this value is requested. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run data can be stored in this single-valued property. Note that the value 101 is undefined and will be not be allowed in the next major revision of the specification.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_ManagedSystemElement.DetailedStatus), **Model Correspondence** (CIM\_ManagedSystemElement.HealthState)
</dt> </dl>

PrimaryStatus provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with DetailedStatus to provide high level and detailed health status of the ManagedElement and its subcomponents. PrimaryStatus consists of one of the following values: Unknown, OK, Degraded or Error. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. "OK" indicates the ManagedElement is functioning normally. "Degraded" indicates the ManagedElement is functioning below normal. "Error" indicates the ManagedElement is in an Error condition.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

OK

</dd> <dt>

2
</dt> <dd>

Degraded

</dd> <dt>

3
</dt> <dd>

Error

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved**


</dt> <dd></dd> </dl>

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the urgency or importance of execution of the Job. The lower the number, the higher the priority. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the setting information that would influence the results of a job.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**RecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.OtherRecoveryAction)
</dt> </dl>

Describes the recovery action to be taken for an unsuccessfully run Job. The possible values are: 0 = "Unknown", meaning it is unknown as to what recovery action to take 1 = "Other", indicating that the recovery action will be specified in the OtherRecoveryAction property 2 = "Do Not Continue", meaning stop the execution of the job and appropriately update its status 3 = "Continue With Next Job", meaning continue with the next job in the queue 4 = "Re-run Job", indicating that the job should be re-run 5 = "Run Recovery Job", meaning run the Job associated using the RecoveryJob relationship. Note that the recovery Job must already be in the queue from which it will run.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

<dt>

0
</dt> <dd>

Unknown

</dd> <dt>

1
</dt> <dd>

Other

</dd> <dt>

2
</dt> <dd>

Do Not Continue

</dd> <dt>

3
</dt> <dd>

Continue With Next Job

</dd> <dt>

4
</dt> <dd>

Re-run Job

</dd> <dt>

5
</dt> <dd>

Run Recovery Job

</dd> </dl>

</dd> <dt>

**RunDay**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MinValue** ("-31"), **MaxValue** ("31"), **Model Correspondence** (CIM\_Job.RunMonth), **Model Correspondence** (CIM\_Job.RunDayOfWeek), **Model Correspondence** (CIM\_Job.RunStartInterval)
</dt> </dl>

The day in the month on which the Job should be processed. There are two different interpretations for this property, depending on the value of DayOfWeek. In one case, RunDay defines the day-in-month on which the Job is processed. This interpretation is used when the DayOfWeek is 0. A positive or negative integer indicates whether the RunDay should be calculated from the beginning or end of the month. For example, 5 indicates the fifth day in the RunMonth and -1 indicates the last day in the RunMonth. When RunDayOfWeek is not 0, RunDay is the day-in-month on which the Job is processed, defined in conjunction with RunDayOfWeek. For example, if RunDay is 15 and RunDayOfWeek is Saturday, then the Job is processed on the first Saturday on or after the 15th day in the RunMonth (for example, the third Saturday in the month). If RunDay is 20 and RunDayOfWeek is -Saturday, then this indicates the first Saturday on or before the 20th day in the RunMonth. If RunDay is -1 and RunDayOfWeek is -Sunday, then this indicates the last Sunday in the RunMonth.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**RunDayOfWeek**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.RunMonth), **Model Correspondence** (CIM\_Job.RunDay), **Model Correspondence** (CIM\_Job.RunStartInterval)
</dt> </dl>

A positive or negative integer used in conjunction with RunDay to indicate the day of the week on which the Job is processed. RunDayOfWeek is set to 0 to indicate an exact day of the month, such as March 1. A positive integer (representing Sunday, Monday, ..., Saturday) means that the day of week is found on or after the specified RunDay. A negative integer (representing -Sunday, -Monday, ..., -Saturday) means that the day of week is found on or BEFORE the RunDay.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

<dt>

-7
</dt> <dd>

-Saturday

</dd> <dt>

-6
</dt> <dd>

-Friday

</dd> <dt>

-5
</dt> <dd>

-Thursday

</dd> <dt>

-4
</dt> <dd>

-Wednesday

</dd> <dt>

-3
</dt> <dd>

-Tuesday

</dd> <dt>

-2
</dt> <dd>

-Monday

</dd> <dt>

-1
</dt> <dd>

-Sunday

</dd> <dt>

0
</dt> <dd>

ExactDayOfMonth

</dd> <dt>

1
</dt> <dd>

Sunday

</dd> <dt>

2
</dt> <dd>

Monday

</dd> <dt>

3
</dt> <dd>

Tuesday

</dd> <dt>

4
</dt> <dd>

Wednesday

</dd> <dt>

5
</dt> <dd>

Thursday

</dd> <dt>

6
</dt> <dd>

Friday

</dd> <dt>

7
</dt> <dd>

Saturday

</dd> </dl>

</dd> <dt>

**RunMonth**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.RunDay), **Model Correspondence** (CIM\_Job.RunDayOfWeek), **Model Correspondence** (CIM\_Job.RunStartInterval)
</dt> </dl>

The month during which the Job should be processed. Specify 0 for January, 1 for February, and so on.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

<dt>

0
</dt> <dd>

January

</dd> <dt>

1
</dt> <dd>

February

</dd> <dt>

2
</dt> <dd>

March

</dd> <dt>

3
</dt> <dd>

April

</dd> <dt>

4
</dt> <dd>

May

</dd> <dt>

5
</dt> <dd>

June

</dd> <dt>

6
</dt> <dd>

July

</dd> <dt>

7
</dt> <dd>

August

</dd> <dt>

8
</dt> <dd>

September

</dd> <dt>

9
</dt> <dd>

October

</dd> <dt>

10
</dt> <dd>

November

</dd> <dt>

11
</dt> <dd>

December

</dd> </dl>

</dd> <dt>

**RunStartInterval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.RunMonth), **Model Correspondence** (CIM\_Job.RunDay), **Model Correspondence** (CIM\_Job.RunDayOfWeek), **Model Correspondence** (CIM\_Job.RunStartInterval)
</dt> </dl>

The time interval after midnight when the Job should be processed. For example, 00000000020000.000000:000 indicates that the Job should be run on or after two o'clock, local time or UTC time (distinguished using the LocalOrUtcTime property.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**ScheduledStartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Deprecated** (CIM\_Job.RunMonth), **Deprecated** (CIM\_Job.RunDay), **Deprecated** (CIM\_Job.RunDayOfWeek), **Deprecated** (CIM\_Job.RunStartInterval)
</dt> </dl>

The time that the current Job is scheduled to start. This time can be represented by the actual date and time, or an interval relative to the time that this property is requested. A value of all zeroes indicates that the Job is already executing. The property is deprecated in lieu of the more expressive scheduling properties, RunMonth, RunDay, RunDayOfWeek, and RunStartInterval.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time that the Job was actually started. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (10), **Deprecated** (CIM\_ManagedSystemElement.OperationalStatus)
</dt> </dl>

A string indicating the current status of the object. Various operational and non-operational statuses are defined. This property is deprecated in lieu of OperationalStatus, which includes the same semantics in its enumeration. This change is made for 3 reasons: 1) Status is more correctly defined as an array. This definition overcomes the limitation of describing status using a single value, when it is really a multi-valued property (for example, an element might be OK AND Stopped. 2) A MaxLen of 10 is too restrictive and leads to unclear enumerated values. 3) The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property and did not want to modify their code. Therefore, Status was grandfathered into the Schema. Use of the deprecated qualifier allows the maintenance of the existing property, but also permits an improved definition using OperationalStatus.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

<dt>

OK
</dt> <dd></dd> <dt>

Error
</dt> <dd></dd> <dt>

Degraded
</dt> <dd></dd> <dt>

Unknown
</dt> <dd></dd> <dt>

Pred Fail
</dt> <dd></dd> <dt>

Starting
</dt> <dd></dd> <dt>

Stopping
</dt> <dd></dd> <dt>

Service
</dt> <dd></dd> <dt>

Stressed
</dt> <dd></dd> <dt>

NonRecover
</dt> <dd></dd> <dt>

No Contact
</dt> <dd></dd> <dt>

Lost Comm
</dt> <dd></dd> <dt>

Stopped
</dt> <dd></dd> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_ManagedSystemElement.OperationalStatus), **Override**, **ArrayType** ("Indexed")
</dt> </dl>

Strings describing the various OperationalStatus array values. For example, if "Stopping" is the value assigned to OperationalStatus, then this property may contain an explanation as to why an object is being stopped. Note that entries in this array are correlated with those at the same array index in OperationalStatus.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**TimeBeforeRemoval**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The amount of time that the Job is retained after it has finished executing, either succeeding or failing in that execution. The job must remain in existence for some period of time regardless of the value of the DeleteOnCompletion property. The default is five minutes.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the state of the Job last changed. If the state of the Job has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

</dd> <dt>

**TimeSubmitted**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time that the Job was submitted to execute. A value of all zeroes indicates that the owning element is not capable of reporting a date and time. Therefore, the ScheduledStartTime and StartTime are reported as intervals relative to the time their values are requested.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> <dt>

**UntilTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Model Correspondence** (CIM\_Job.LocalOrUtcTime)
</dt> </dl>

The time after which the Job is invalid or should be stopped. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. A value of all nines indicates that the Job can run indefinitely.

This member is introduced in [**CIM\_Job**](https://msdn.microsoft.com/library/aa387873).

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



 

 




