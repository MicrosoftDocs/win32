---
Description: CIM\_LogicalElement is a base class for all the components of a System that represent abstract system components, such as Files, Processes, or LogicalDevices.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b491b44-ae3e-4ee1-8d99-8d109af1ca0d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_LogicalElement class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_LogicalElement class

CIM\_LogicalElement is a base class for all the components of a System that represent abstract system components, such as Files, Processes, or LogicalDevices.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), Abstract, Version("2.6.0"), AMENDMENT]
class CIM_LogicalElement : CIM_ManagedSystemElement
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
};
```

## Members

The **CIM\_LogicalElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_LogicalElement** class has these properties.

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

5 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

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

6 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

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

31 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

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
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (1024)
</dt> </dl>

The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

This member is introduced in [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

17 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

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

19 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

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

4 32767
</dt> <dd>

DMTF Reserved

</dd> <dt>

32768 65535
</dt> <dd>

Vendor Reserved

</dd> </dl>

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

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



 

 




