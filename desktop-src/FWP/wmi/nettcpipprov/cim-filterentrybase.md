---
description: Aggregates instances of (subclasses of) FilterEntryBase via the aggregation EntriesInFilterList.
ms.assetid: 2829725a-9061-4753-a4ed-e19b39d6f542
title: CIM\_FilterEntryBase class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_FilterEntryBase
- CIM_FilterEntryBase.InstanceID
- CIM_FilterEntryBase.Caption
- CIM_FilterEntryBase.Description
- CIM_FilterEntryBase.ElementName
- CIM_FilterEntryBase.InstallDate
- CIM_FilterEntryBase.OperationalStatus
- CIM_FilterEntryBase.StatusDescriptions
- CIM_FilterEntryBase.Status
- CIM_FilterEntryBase.HealthState
- CIM_FilterEntryBase.CommunicationStatus
- CIM_FilterEntryBase.DetailedStatus
- CIM_FilterEntryBase.OperatingStatus
- CIM_FilterEntryBase.PrimaryStatus
- CIM_FilterEntryBase.Name
- CIM_FilterEntryBase.SystemCreationClassName
- CIM_FilterEntryBase.SystemName
- CIM_FilterEntryBase.CreationClassName
- CIM_FilterEntryBase.IsNegated
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_FilterEntryBase class

Aggregates instances of (subclasses of) FilterEntryBase via the aggregation EntriesInFilterList.

The filter entries are always ANDed together when grouped by the FilterList. Note that it is possible to aggregate different types of filters into a single FilterList - for example, packet header filters (represented by the IpHeadersFilter class) and IPsec security filters. A FilterList is weak to the network device (e.g., the ComputerSystem) that contains it. Hence, the ComputerSystem keys are propagated to this class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Filtering"), Abstract, Version("2.7.0"), AMENDMENT]
class CIM_FilterEntryBase : CIM_LogicalElement
{
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   Name;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  boolean  IsNegated;
};
```

## Members

The **CIM\_FilterEntryBase** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_FilterEntryBase** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64)
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



| Values                                                                                                                                                                                                                                                                     | Meaning                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                | Indicates that the instrumentation cannot report on the **CommunicationStatus** property at this time.<br/>                       |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>1</dt> </dl>                        | Indicates that the instrumentation is capable of reporting this property, but intentionally does not for this element. <br/>      |
| <span id="Communication_OK"></span><span id="communication_ok"></span><span id="COMMUNICATION_OK"></span><dl> <dt>**Communication OK**</dt> <dt>2</dt> </dl>            | Indicates only that communication is established with the element. <br/>                                                          |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>3</dt> </dl>    | Indicates that the element has been contacted in the past, but is currently unreachable.<br/>                                     |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>4</dt> </dl>                                    | Indicates that the instrumentation has contact information for this element, but has never been able to communicate with it.<br/> |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>5 32767</dt> </dl>                  | Reserved.<br/>                                                                                                                    |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 = *value* </dt> </dl> | Reserved.<br/>                                                                                                                    |



 

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

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

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.PrimaryStatus", "CIM\_ManagedSystemElement.HealthState")
</dt> </dl>

Indicates additional status details that complement the **PrimaryStatus** property. A **NULL** value indicates that the instrumentation does not support this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Values                                                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>0</dt> </dl>                                                     | Indicates that the instrumentation is capable of reporting this property, but intentionally does not report it for this element. <br/>                                                                                                                                           |
| <span id="No_Additional_Information"></span><span id="no_additional_information"></span><span id="NO_ADDITIONAL_INFORMATION"></span><dl> <dt>**No Additional Information**</dt> <dt>1</dt> </dl>     | Indicates that no details have to be added to the **PrimaryStatus** property, for example when the **PrimaryStatus** is set to **OK**.<br/>                                                                                                                                      |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>2</dt> </dl>                                                                         | Indicates that the element functions, but requires attention. Overload and overheated are examples of **Stressed** states.<br/>                                                                                                                                                  |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>3</dt> </dl>                                 | Indicates that an element functions nominally, but predicts a failure in the near future. <br/>                                                                                                                                                                                  |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>4</dt> </dl>                     | Indicates that this element is in an error condition that requires human intervention.<br/>                                                                                                                                                                                      |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>5</dt> </dl> | Indicates that an element on which this element depends is in error. This element might be **OK** but cannot function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.<br/> |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>6 32767</dt> </dl>                                               | Reserved.<br/>                                                                                                                                                                                                                                                                   |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 = *value* </dt> </dl>                              | Reserved.<br/>                                                                                                                                                                                                                                                                   |



 

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

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its sub-components.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Values                                                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                          | The implementation cannot report on **HealthState** at this time.<br/>                                                                                                                                                                                       |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>5</dt> </dl>                                                                                                   | The element is fully functional and is operating within normal operational parameters and without error.<br/>                                                                                                                                                |
| <span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span><dl> <dt>**Degraded/Warning**</dt> <dt>10</dt> </dl>                     | The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors<br/> |
| <span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span><dl> <dt>**Minor failure**</dt> <dt>15</dt> </dl>                                 | All functionality is available but some might be degraded. <br/>                                                                                                                                                                                             |
| <span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span><dl> <dt>**Major failure**</dt> <dt>20</dt> </dl>                                 | The element is failing. It is possible that some or all of the functionality of this component is degraded or not working. <br/>                                                                                                                             |
| <span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span><dl> <dt>**Critical failure**</dt> <dt>25</dt> </dl>                     | The element is non-functional and recovery might not be possible.<br/>                                                                                                                                                                                       |
| <span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-recoverable error**</dt> <dt>30</dt> </dl> | The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost.<br/>                                                                                                                              |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>31 = *value* </dt> </dl>                      | DMTF has reserved the unused portion of the continuum for additional **HealthStates** values in the future.<br/>                                                                                                                                             |



 

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

> \[!Important\]In order to ensure uniqueness within the Namespace, the value of **InstanceID** should be constructed in the following pattern:
>
> *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity defining the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This is similar to the structure of Schema class names. In addition, to ensure uniqueness the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefor the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the preceding pattern is not used, the defining entity must assure that the resultant **InstanceID** is not re-used across any **InstanceID**s produced by this or other providers for this Namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**IsNegated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating that the match condition described in the properties of the FilterEntryBase subclass should be negated. This property is defined for ease of use when filtering on simple negations - for example, to select all source ports except 162. It is not recommended that this Boolean be set to True when filtering on multiple criteria, such as defining an IPHeadersFilter based on source/destination addresses, ports, and DiffServ Code Points.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Name")
</dt> </dl>

Defines the label by which the Filter Entry is known and uniquely identified.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

Indicates the current operational condition of the element. This property can be used to provide more detail about the current state of the element. It can also indicate transitional states. A **NULL** value indicates that the instrumentation does not support this property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Value                                                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                | Indicates that the instrumentation cannot report on the **OperatingStatus** property at this time.<br/>                                                                                               |
| <span id="Not_Available"></span><span id="not_available"></span><span id="NOT_AVAILABLE"></span><dl> <dt>**Not Available**</dt> <dt>1</dt> </dl>                        | Indicates that the instrumentation is capable of reporting this property, but intentionally does not report it for this element. <br/>                                                                |
| <span id="Servicing"></span><span id="servicing"></span><span id="SERVICING"></span><dl> <dt>**Servicing**</dt> <dt>2</dt> </dl>                                        | Indicates that the element is in process to be configured, maintained, cleaned, or otherwise administered. <br/>                                                                                      |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>3</dt> </dl>                                            | Indicates that the element is being initialized.<br/>                                                                                                                                                 |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>4</dt> </dl>                                            | Indicates that the element is being brought to an orderly stop.<br/>                                                                                                                                  |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>5</dt> </dl>                                                | Indicates that the element is intentionally stopped.<br/>                                                                                                                                             |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>6</dt> </dl>                                                | Indicates that the element stopped in an unexpected way. <br/>                                                                                                                                        |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>7</dt> </dl>                                                | Indicates that the element is inactive or quiesced. <br/>                                                                                                                                             |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>8</dt> </dl>                                        | Indicates that the element completed its operation. We recommend using a **PrimaryStatus** property value of **OK**, **Error**, or **Degraded** to indicate success or failure of the operation.<br/> |
| <span id="Migrating"></span><span id="migrating"></span><span id="MIGRATING"></span><dl> <dt>**Migrating**</dt> <dt>9</dt> </dl>                                        | Indicates that the element is being moved between host elements. <br/>                                                                                                                                |
| <span id="Emigrating"></span><span id="emigrating"></span><span id="EMIGRATING"></span><dl> <dt>**Emigrating**</dt> <dt>10</dt> </dl>                                   | Indicates that the element is being moved away from the host element.<br/>                                                                                                                            |
| <span id="Immigrating"></span><span id="immigrating"></span><span id="IMMIGRATING"></span><dl> <dt>**Immigrating**</dt> <dt>11</dt> </dl>                               | Indicates that the element is being moved to a new host element. <br/>                                                                                                                                |
| <span id="Snapshotting"></span><span id="snapshotting"></span><span id="SNAPSHOTTING"></span><dl> <dt>**Snapshotting**</dt> <dt>12</dt> </dl>                           | Indicates that a snapshot copy of the element is being created.<br/>                                                                                                                                  |
| <span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span><dl> <dt>**Shutting Down**</dt> <dt>13</dt> </dl>                       | Indicates that the element is being brought to an abrupt stop.<br/>                                                                                                                                   |
| <span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span><dl> <dt>**In Test**</dt> <dt>14</dt> </dl>                                               | Indicates that the element is performing test functions.<br/>                                                                                                                                         |
| <span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span><dl> <dt>**Transitioning**</dt> <dt>15</dt> </dl>                       | Indicates that the element is between states and is not fully available in either state. Use another value that indicates a more specific transition if one is available.<br/>                        |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>16</dt> </dl>                                   | Indicates that the element is in service and operational.<br/>                                                                                                                                        |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>17 32767</dt> </dl>                 | Reserved.<br/>                                                                                                                                                                                        |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 = *value* </dt> </dl> | Reserved.<br/>                                                                                                                                                                                        |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ManagedSystemElement.StatusDescriptions")
</dt> </dl>

Contains indicators of the current status of the element. The first value of **OperationalStatus** should contain the primary status for the element.

> [!Note]  
> **OperationalStatus** replaces the deprecated **Status** property. Due to the widespread use of the existing **Status** property in management applications, Microsoft strongly recommends that providers or instrumentation provide both the **Status** and **OperationalStatus** properties. When instrumented, **Status** (because it is single-valued) should also provide the primary status of the element.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).



| Values                                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                              | Indicates the implementation cannot report on **OperationalStatus** at this time.<br/>                                                                                                                                                                                                                                                                                                 |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                      | Indicates an undefined state.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                                       | Indicates full functionality without errors.<br/>                                                                                                                                                                                                                                                                                                                                      |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                                          | Indicates the element is working and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors<br/>                                                                                                                          |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>4</dt> </dl>                                                                          | Indicates that the element is functioning, but needs attention. Overload and overheated are examples of **Stressed** states.<br/>                                                                                                                                                                                                                                                      |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>5</dt> </dl>                                  | Indicates that an element is functioning nominally but predicting a failure in the near future. <br/>                                                                                                                                                                                                                                                                                  |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                                      | Indicates that an error has occurred.<br/>                                                                                                                                                                                                                                                                                                                                             |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl>                      | A nonrecoverable error has occurred.<br/>                                                                                                                                                                                                                                                                                                                                              |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>8</dt> </dl>                                                                          | The job is starting.<br/>                                                                                                                                                                                                                                                                                                                                                              |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>9</dt> </dl>                                                                          | The job is stopping.<br/>                                                                                                                                                                                                                                                                                                                                                              |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>10</dt> </dl>                                                                             | The element has been intentionally stopped. <br/>                                                                                                                                                                                                                                                                                                                                      |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>11</dt> </dl>                                                                 | Indicates the element is being configured, maintained, cleaned, or otherwise administered. <br/>                                                                                                                                                                                                                                                                                       |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>12</dt> </dl>                                                                 | Indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. <br/>                                                                                                                                                                                                                                                 |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>13</dt> </dl>                                 | Indicates that the job is known to exist and has been contacted successfully in the past, but is currently unreachable.<br/>                                                                                                                                                                                                                                                           |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>14</dt> </dl>                                                                             | Indicates the job stopped in an unexpected way. The state and configuration of the job might need to be updated. <br/>                                                                                                                                                                                                                                                                 |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>15</dt> </dl>                                                                             | Indicates that the job is inactive.<br/>                                                                                                                                                                                                                                                                                                                                               |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>16</dt> </dl> | Indicates that an element on which this job depends is in error. This element may be **OK** but is unable to function because of the state of a dependent element. An example is a network service or endpoint that cannot function due to lower-layer networking problems.<br/>                                                                                                       |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>17</dt> </dl>                                                                     | Indicates that the job has completed its operation. This value should be combined with either **OK**, **Error**Error, or **Degraded** so that a client can tell if the complete operation **Completed** with **OK** (passed), Completed with **Error** (failed), or Completed with **Degraded** (the operation finished, but it did not complete OK or did not report an error). <br/> |
| <span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span><dl> <dt>**Power Mode**</dt> <dt>18</dt> </dl>                                                                 | "Power Mode" indicates that the element has additional power model information contained in the associated PowerManagementService association.<br/>                                                                                                                                                                                                                                    |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>19 32767</dt> </dl>                                               | DMTF has reserved this portion of the range for additional *OperationalStatus* values in the future.<br/>                                                                                                                                                                                                                                                                              |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 65535</dt> </dl>                                    | Microsoft has reserved the unused portion of the range for additional *OperationalStatus* values in the future.<br/>                                                                                                                                                                                                                                                                   |



 

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ManagedSystemElement.DetailedStatus", "CIM\_ManagedSystemElement.HealthState")
</dt> </dl>

Indicates a high-level status value.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The possible values are.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="OK"></span><span id="ok"></span>**OK** (1)
</dt> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (2)
</dt> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (3)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (4 32767)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768 = *value* )
</dt> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/win32/wmisdk/standard-wmi-qualifiers) ("CIM\_ManagedSystemElement.OperationalStatus"), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (10)
</dt> </dl>

Contains a string indicating the primary status of the object.

> [!Note]  
> This property is deprecated and replaced by the **OperationalStatus** property. If you choose to use the **Status** property for backward compatibility it should be secondary to the **OperationalStatus** property.

 

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

The possible values are.

<dl> <dt>

 ("OK")
</dt> <dt>

 ("Error")
</dt> <dt>

 ("Degraded")
</dt> <dt>

 ("Unknown")
</dt> <dt>

 ("Pred Fail")
</dt> <dt>

 ("Starting")
</dt> <dt>

 ("Stopping")
</dt> <dt>

 ("Service")
</dt> <dt>

 ("Stressed")
</dt> <dt>

 ("NonRecover")
</dt> <dt>

 ("No Contact")
</dt> <dt>

 ("Lost Comm")
</dt> <dt>

 ("Stopped")
</dt> </dl>

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-qualifiers) ("Indexed"), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ManagedSystemElement.OperationalStatus")
</dt> </dl>

Indicates descriptions of the corresponding values in the **OperationalStatus** array. For example, if an element in the **OperationalStatus** property contains the value **Stopping**, then the element at the same array index in this property might contain an explanation as to why an object is being stopped.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**Propagated**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ComputerSystem.CreationClassName")
</dt> </dl>

The scoping computer system's CreationClassName.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**Propagated**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ComputerSystem.Name")
</dt> </dl>

The scoping ComputerSystem's Name.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> </dl>

 

