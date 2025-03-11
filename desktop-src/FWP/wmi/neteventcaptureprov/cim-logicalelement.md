---
title: CIM\_LogicalElement class
description: CIM\_LogicalElement is a base class for all the components of a System that represent abstract system components, such as Files, Processes, or LogicalDevices.
ms.assetid: 45253bef-63d9-48f8-8f3e-4a9a75191715
keywords:
- CIM_LogicalElement class
- CIM_LogicalElement class, described
topic_type:
- apiref
api_name:
- CIM_LogicalElement
- CIM_LogicalElement.InstanceID
- CIM_LogicalElement.Caption
- CIM_LogicalElement.Description
- CIM_LogicalElement.ElementName
- CIM_LogicalElement.InstallDate
- CIM_LogicalElement.Name
- CIM_LogicalElement.OperationalStatus
- CIM_LogicalElement.StatusDescriptions
- CIM_LogicalElement.Status
- CIM_LogicalElement.HealthState
- CIM_LogicalElement.CommunicationStatus
- CIM_LogicalElement.DetailedStatus
- CIM_LogicalElement.OperatingStatus
- CIM_LogicalElement.PrimaryStatus
api_location:
- NetEventPacketCapture.dll
api_type:
- DllExport


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
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

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64)
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

CommunicationStatus indicates the ability of the instrumentation to communicate with the underlying ManagedElement. CommunicationStatus consists of one of the following values: Unknown, None, Communication OK, Lost Communication, or No Contact.

A Null return indicates the implementation (provider) does not implement this property.

"Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

"Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property).

"Communication OK " indicates communication is established with the element, but does not convey any quality of service.

"No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

"Lost Communication" indicates that the Managed Element is known to exist and has been contacted successfully in the past, but is currently unreachable.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                               | Meaning                       |
|-------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>0</dt> </dl>        | Unknown<br/>            |
| <dl> <dt>1</dt> </dl>        | Not Available<br/>      |
| <dl> <dt>2</dt> </dl>        | Communication OK<br/>   |
| <dl> <dt>3</dt> </dl>        | Lost Communication<br/> |
| <dl> <dt>4</dt> </dl>        | No Contact<br/>         |
| <dl> <dt>..</dt> </dl>       | DMTF Reserved<br/>      |
| <dl> <dt>0x8000..</dt> </dl> | Vendor Reserved<br/>    |



 

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

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.PrimaryStatus", "CIM\_ManagedSystemElement.HealthState")
</dt> </dl>

DetailedStatus compliments PrimaryStatus with additional status detail. It consists of one of the following values: Not Available, No Additional Information, Stressed, Predictive Failure, Error, Non-Recoverable Error, SupportingEntityInError. Detailed status is used to expand upon the PrimaryStatus of the element.

A Null return indicates the implementation (provider) does not implement this property.

"Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property).

"No Additional Information" indicates that the element is functioning normally as indicated by PrimaryStatus = "OK".

"Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on.

"Predictive Failure" indicates that an element is functioning normally but a failure is predicted in the near future.

"Non-Recoverable Error " indicates that this element is in an error condition that requires human intervention.

"Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                               | Meaning                               |
|-------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>0</dt> </dl>        | Not Available<br/>              |
| <dl> <dt>1</dt> </dl>        | No Additional Information<br/>  |
| <dl> <dt>2</dt> </dl>        | Stressed<br/>                   |
| <dl> <dt>3</dt> </dl>        | Predictive Failure<br/>         |
| <dl> <dt>4</dt> </dl>        | Non-Recoverable Error<br/>      |
| <dl> <dt>5</dt> </dl>        | Supporting Entity in Error<br/> |
| <dl> <dt>..</dt> </dl>       | DMTF Reserved<br/>              |
| <dl> <dt>0x8000..</dt> </dl> | Vendor Reserved<br/>            |



 

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM\_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. The following continuum is defined:

"Non-recoverable Error" (30) - The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost.

"Critical Failure" (25) - The element is non-functional and recovery might not be possible.

"Major Failure" (20) - The element is failing. It is possible that some or all of the functionality of this component is degraded or not working.

"Minor Failure" (15) - All functionality is available but some might be degraded.

"Degraded/Warning" (10) - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors.

"OK" (5) - The element is fully functional and is operating within normal operational parameters and without error.

"Unknown" (0) - The implementation cannot report on HealthState at this time.

DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                         | Meaning                          |
|-------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>0</dt> </dl>  | Unknown<br/>               |
| <dl> <dt>5</dt> </dl>  | OK<br/>                    |
| <dl> <dt>10</dt> </dl> | Degraded/Warning<br/>      |
| <dl> <dt>15</dt> </dl> | Minor failure<br/>         |
| <dl> <dt>20</dt> </dl> | Major failure<br/>         |
| <dl> <dt>25</dt> </dl> | Critical failure<br/>      |
| <dl> <dt>30</dt> </dl> | Non-recoverable error<br/> |
| <dl> <dt>..</dt> </dl> | DMTF Reserved<br/>         |



 

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A datetime value that indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (1024)
</dt> </dl>

The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

OperatingStatus provides a current status value for the operational condition of the element and can be used for providing more detail with respect to the value of EnabledState. It can also provide the transitional states when an element is transitioning from one state to another, such as when an element is transitioning between EnabledState and RequestedState, as well as other transitional conditions.

OperatingStatus consists of one of the following values: Unknown, Not Available, In Service, Starting, Stopping, Stopped, Aborted, Dormant, Completed, Migrating, Emmigrating, Immigrating, Snapshotting. Shutting Down, In Test

A Null return indicates the implementation (provider) does not implement this property.

"Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

"None" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property).

"Servicing" describes an element being configured, maintained, cleaned, or otherwise administered.

"Starting" describes an element being initialized.

"Stopping" describes an element being brought to an orderly stop.

"Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated.

"Dormant" indicates that the element is inactive or quiesced.

"Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded in the PrimaryStatus so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error).

"Migrating" element is being moved between host elements.

"Immigrating" element is being moved to new host element.

"Emigrating" element is being moved away from host element.

"Shutting Down" describes an element being brought to an abrupt stop.

"In Test" element is performing test functions.

"Transitioning" describes an element that is between states, that is, it is not fully available in either its previous state or its next state. This value should be used if other values indicating a transition to a specific state are not applicable.

"In Service" describes an element that is in service and operational.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                               | Meaning                    |
|-------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>        | Unknown<br/>         |
| <dl> <dt>1</dt> </dl>        | Not Available<br/>   |
| <dl> <dt>2</dt> </dl>        | Servicing<br/>       |
| <dl> <dt>3</dt> </dl>        | Starting<br/>        |
| <dl> <dt>4</dt> </dl>        | Stopping<br/>        |
| <dl> <dt>5</dt> </dl>        | Stopped<br/>         |
| <dl> <dt>6</dt> </dl>        | Aborted<br/>         |
| <dl> <dt>7</dt> </dl>        | Dormant<br/>         |
| <dl> <dt>8</dt> </dl>        | Completed<br/>       |
| <dl> <dt>9</dt> </dl>        | Migrating<br/>       |
| <dl> <dt>10</dt> </dl>       | Emigrating<br/>      |
| <dl> <dt>11</dt> </dl>       | Immigrating<br/>     |
| <dl> <dt>12</dt> </dl>       | Snapshotting<br/>    |
| <dl> <dt>13</dt> </dl>       | Shutting Down<br/>   |
| <dl> <dt>14</dt> </dl>       | In Test<br/>         |
| <dl> <dt>15</dt> </dl>       | Transitioning<br/>   |
| <dl> <dt>16</dt> </dl>       | In Service<br/>      |
| <dl> <dt>..</dt> </dl>       | DMTF Reserved<br/>   |
| <dl> <dt>0x8000..</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ManagedSystemElement.StatusDescriptions")
</dt> </dl>

Indicates the current statuses of the element. Various operational statuses are defined. Many of the enumeration\\'s values are self-explanatory. However, a few are not and are described here in more detail.

"Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on.

"Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future.

"In Service" describes an element being configured, maintained, cleaned, or otherwise administered.

"No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it.

"Lost Communication" indicates that the ManagedSystem Element is known to exist and has been contacted successfully in the past, but is currently unreachable.

"Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated.

"Dormant" indicates that the element is inactive or quiesced.

"Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

"Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error).

"Power Mode" indicates that the element has additional power model information contained in the Associated PowerManagementService association.

OperationalStatus replaces the Status property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today\\'s environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the Status and OperationalStatus properties. Further, the first value of OperationalStatus should contain the primary status for the element. When instrumented, Status (because it is single-valued) should also provide the primary status of the element.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                               | Meaning                               |
|-------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>0</dt> </dl>        | Unknown<br/>                    |
| <dl> <dt>1</dt> </dl>        | Other<br/>                      |
| <dl> <dt>2</dt> </dl>        | OK<br/>                         |
| <dl> <dt>3</dt> </dl>        | Degraded<br/>                   |
| <dl> <dt>4</dt> </dl>        | Stressed<br/>                   |
| <dl> <dt>5</dt> </dl>        | Predictive Failure<br/>         |
| <dl> <dt>6</dt> </dl>        | Error<br/>                      |
| <dl> <dt>7</dt> </dl>        | Non-Recoverable Error<br/>      |
| <dl> <dt>8</dt> </dl>        | Starting<br/>                   |
| <dl> <dt>9</dt> </dl>        | Stopping<br/>                   |
| <dl> <dt>10</dt> </dl>       | Stopped<br/>                    |
| <dl> <dt>11</dt> </dl>       | In Service<br/>                 |
| <dl> <dt>12</dt> </dl>       | No Contact<br/>                 |
| <dl> <dt>13</dt> </dl>       | Lost Communication<br/>         |
| <dl> <dt>14</dt> </dl>       | Aborted<br/>                    |
| <dl> <dt>15</dt> </dl>       | Dormant<br/>                    |
| <dl> <dt>16</dt> </dl>       | Supporting Entity in Error<br/> |
| <dl> <dt>17</dt> </dl>       | Completed<br/>                  |
| <dl> <dt>18</dt> </dl>       | Power Mode<br/>                 |
| <dl> <dt>..</dt> </dl>       | DMTF Reserved<br/>              |
| <dl> <dt>0x8000..</dt> </dl> | Vendor Reserved<br/>            |



 

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ManagedSystemElement.DetailedStatus", "CIM\_ManagedSystemElement.HealthState")
</dt> </dl>

PrimaryStatus provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with DetailedStatus to provide high level and detailed health status of the ManagedElement and its subcomponents.

PrimaryStatus consists of one of the following values: Unknown, OK, Degraded or Error. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

"OK" indicates the ManagedElement is functioning normally.

"Degraded" indicates the ManagedElement is functioning below normal.

"Error" indicates the ManagedElement is in an Error condition.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                               | Meaning                    |
|-------------------------------------------------------------------------------------|----------------------------|
| <dl> <dt>0</dt> </dl>        | Unknown<br/>         |
| <dl> <dt>1</dt> </dl>        | OK<br/>              |
| <dl> <dt>2</dt> </dl>        | Degraded<br/>        |
| <dl> <dt>3</dt> </dl>        | Error<br/>           |
| <dl> <dt>..</dt> </dl>       | DMTF Reserved<br/>   |
| <dl> <dt>0x8000..</dt> </dl> | Vendor Reserved<br/> |



 

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/win32/wmisdk/standard-wmi-qualifiers) ("CIM\_ManagedSystemElement.OperationalStatus"), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (10)
</dt> </dl>

A string indicating the current status of the object. Various operational and non-operational statuses are defined. This property is deprecated in lieu of OperationalStatus, which includes the same semantics in its enumeration. This change is made for 3 reasons:

1) Status is more correctly defined as an array. This definition overcomes the limitation of describing status using a single value, when it is really a multi-valued property (for example, an element might be OK AND Stopped.

2) A MaxLen of 10 is too restrictive and leads to unclear enumerated values.

3) The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property and did not want to modify their code. Therefore, Status was grandfathered into the Schema. Use of the deprecated qualifier allows the maintenance of the existing property, but also permits an improved definition using OperationalStatus.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                                   | Meaning |
|-----------------------------------------------------------------------------------------|---------|
| <dl> <dt>"OK"</dt> </dl>         |         |
| <dl> <dt>"Error"</dt> </dl>      |         |
| <dl> <dt>"Degraded"</dt> </dl>   |         |
| <dl> <dt>"Unknown"</dt> </dl>    |         |
| <dl> <dt>"Pred Fail"</dt> </dl>  |         |
| <dl> <dt>"Starting"</dt> </dl>   |         |
| <dl> <dt>"Stopping"</dt> </dl>   |         |
| <dl> <dt>"Service"</dt> </dl>    |         |
| <dl> <dt>"Stressed"</dt> </dl>   |         |
| <dl> <dt>"NonRecover"</dt> </dl> |         |
| <dl> <dt>"No Contact"</dt> </dl> |         |
| <dl> <dt>"Lost Comm"</dt> </dl>  |         |
| <dl> <dt>"Stopped"</dt> </dl>    |         |



 

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Strings describing the various OperationalStatus array values. For example, if "Stopping" is the value assigned to OperationalStatus, then this property may contain an explanation as to why an object is being stopped. Note that entries in this array are correlated with those at the same array index in OperationalStatus.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                       |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                                       |
| MOF<br/>                      | <dl> <dt>NetEventPacketCapture.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetEventPacketCapture.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> </dl>

 

