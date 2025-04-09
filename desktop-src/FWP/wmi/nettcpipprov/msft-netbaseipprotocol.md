---
description: The base class for the MSFT\_NetIPv4Protocol and MSFT\_NetIPv6Protocol classes for the Microsoft TCP/IP WMI v. 2 provider.
ms.assetid: c1f6cfc8-56dc-4b9a-a955-da4638bb2e95
title: MSFT\_NetBaseIPProtocol class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetBaseIPProtocol
- MSFT_NetBaseIPProtocol.InstanceID
- MSFT_NetBaseIPProtocol.Caption
- MSFT_NetBaseIPProtocol.ElementName
- MSFT_NetBaseIPProtocol.InstallDate
- MSFT_NetBaseIPProtocol.StatusDescriptions
- MSFT_NetBaseIPProtocol.Status
- MSFT_NetBaseIPProtocol.HealthState
- MSFT_NetBaseIPProtocol.CommunicationStatus
- MSFT_NetBaseIPProtocol.DetailedStatus
- MSFT_NetBaseIPProtocol.OperatingStatus
- MSFT_NetBaseIPProtocol.PrimaryStatus
- MSFT_NetBaseIPProtocol.OtherEnabledState
- MSFT_NetBaseIPProtocol.RequestedState
- MSFT_NetBaseIPProtocol.EnabledDefault
- MSFT_NetBaseIPProtocol.TransitioningToState
- MSFT_NetBaseIPProtocol.AvailableRequestedStates
- MSFT_NetBaseIPProtocol.SystemCreationClassName
- MSFT_NetBaseIPProtocol.SystemName
- MSFT_NetBaseIPProtocol.CreationClassName
- MSFT_NetBaseIPProtocol.Description
- MSFT_NetBaseIPProtocol.Name
- MSFT_NetBaseIPProtocol.OperationalStatus
- MSFT_NetBaseIPProtocol.EnabledState
- MSFT_NetBaseIPProtocol.TimeOfLastStateChange
- MSFT_NetBaseIPProtocol.NameFormat
- MSFT_NetBaseIPProtocol.ProtocolType
- MSFT_NetBaseIPProtocol.ProtocolIFType
- MSFT_NetBaseIPProtocol.OtherTypeDescription
- MSFT_NetBaseIPProtocol.DefaultHopLimit
- MSFT_NetBaseIPProtocol.NeighborCacheLimit
- MSFT_NetBaseIPProtocol.RouteCacheLimit
- MSFT_NetBaseIPProtocol.ReassemblyLimit
- MSFT_NetBaseIPProtocol.IcmpRedirects
- MSFT_NetBaseIPProtocol.SourceRoutingBehavior
- MSFT_NetBaseIPProtocol.DhcpMediaSense
- MSFT_NetBaseIPProtocol.MediaSenseEventLog
- MSFT_NetBaseIPProtocol.MldLevel
- MSFT_NetBaseIPProtocol.MldVersion
- MSFT_NetBaseIPProtocol.MulticastForwarding
- MSFT_NetBaseIPProtocol.GroupForwardedFragments
- MSFT_NetBaseIPProtocol.RandomizeIdentifiers
- MSFT_NetBaseIPProtocol.AddressMaskReply
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetBaseIPProtocol class

The base class for the [**MSFT\_NetIPv4Protocol**](msft-netipv4protocol.md) and [**MSFT\_NetIPv6Protocol**](msft-netipv6protocol.md) classes for the Microsoft TCP/IP WMI v. 2 provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::Service"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetBaseIPProtocol : CIM_ProtocolEndpoint
{
  string   InstanceID;
  string   Caption;
  string   ElementName;
  datetime InstallDate;
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  uint16   TransitioningToState = 12;
  uint16   AvailableRequestedStates[];
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  string   Description;
  string   Name;
  uint16   OperationalStatus[];
  uint16   EnabledState;
  datetime TimeOfLastStateChange;
  string   NameFormat;
  uint16   ProtocolType;
  uint16   ProtocolIFType;
  string   OtherTypeDescription;
  uint32   DefaultHopLimit;
  uint32   NeighborCacheLimit;
  uint32   RouteCacheLimit;
  uint32   ReassemblyLimit;
  uint8    IcmpRedirects;
  uint32   SourceRoutingBehavior;
  uint8    DhcpMediaSense;
  uint8    MediaSenseEventLog;
  uint32   MldLevel;
  uint32   MldVersion;
  uint8    MulticastForwarding;
  uint8    GroupForwardedFragments;
  uint8    RandomizeIdentifiers;
  uint8    AddressMaskReply;
};
```

## Members

The **MSFT\_NetBaseIPProtocol** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetBaseIPProtocol** class has these methods.



| Method                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RequestStateChange**](msft-netbaseipprotocol-requeststatechange.md) | Requests that the state of the element be changed to the value specified in the *RequestedState* parameter. When the requested state change takes place, the enabled state and requested state of the element will be the same. Invoking the **RequestChangeState** method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully and the use of [**CIM\_ConcreteJob**](cim-concretejob.md) was not required. If 4096 (0x1000) is returned, then the task will take some time to complete, **CIM\_ConcreteJob** will be created, and its reference returned in the output parameter *Job*. Any other return code indicates an error condition.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/> |



 

### Properties

The **MSFT\_NetBaseIPProtocol** class has these properties.

<dl> <dt>

**AddressMaskReply**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the computer should respond to ICMP address mask packets.



| Value                                                                                                                                                                                                                           | Meaning                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | The computer should not respond to ICMP address mask packets.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | The computer should not respond to ICMP address mask packets.<br/> |



 

</dd> <dt>

**AvailableRequestedStates**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.RequestStateChange", "CIM\_EnabledLogicalElementCapabilities.RequestedStatesSupported")
</dt> </dl>

AvailableRequestedStates indicates the possible values for the RequestedState parameter of the method RequestStateChange, used to initiate a state change. The values listed shall be a subset of the values contained in the RequestedStatesSupported property of the associated instance of CIM\_EnabledLogicalElementCapabilities where the values selected are a function of the current state of the CIM\_EnabledLogicalElement. This property may be non-null if an implementation is able to advertise the set of possible values as a function of the current state. This property shall be null if an implementation is unable to determine the set of possible values as a function of the current state.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dl> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)
</dt> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>**Shut Down** (4)
</dt> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (6)
</dt> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test** (7)
</dt> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>**Defer** (8)
</dt> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (9)
</dt> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>**Reboot** (10)
</dt> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>**Reset** (11)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (12 65535)
</dt> </dl>

</dd> <dt>

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

Indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**DefaultHopLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The default hop limit for packets sent.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

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

**DhcpMediaSense**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on the media sensing capability of the TCP/IP stack.



| Value                                                                                                                                                                                                                           | Meaning                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Turns on the media sensing capability of the TCP/IP stack.<br/>  |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Turns off the media sensing capability of the TCP/IP stack.<br/> |



 

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

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dl> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (5)
</dt> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>**Enabled but Offline** (6)
</dt> <dt>

<span id="No_Default"></span><span id="no_default"></span><span id="NO_DEFAULT"></span>**No Default** (7)
</dt> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (9)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (10 32767)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768 65535)
</dt> </dl>

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.OtherEnabledState")
</dt> </dl>

EnabledState is an integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).



| Value                                                                                                                                                                                                                                                                       | Meaning                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                 | The element state is unknown.<br/>                                                                              |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                         | The element is in a state other than one listed here.<br/>                                                      |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>2</dt> </dl>                                                 | The element is or could be executing commands, will process any queued commands, and queues new requests. <br/> |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>3</dt> </dl>                                             | The element will not execute commands and will drop any new requests. <br/>                                     |
| <span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span><dl> <dt>**Shutting Down**</dt> <dt>4</dt> </dl>                         | The element is in the process of going to a Disabled state. <br/>                                               |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>5</dt> </dl>                     | The element does not support being enabled or disabled. <br/>                                                   |
| <span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span><dl> <dt>**Enabled but Offline**</dt> <dt>6</dt> </dl> | The element might be completing commands, and will drop any new requests. <br/>                                 |
| <span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span><dl> <dt>**In Test**</dt> <dt>7</dt> </dl>                                                 | The element is in a test state. <br/>                                                                           |
| <span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span><dl> <dt>**Deferred**</dt> <dt>8</dt> </dl>                                             | The element might be completing commands, but will queue any new requests. <br/>                                |
| <span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span><dl> <dt>**Quiesce**</dt> <dt>9</dt> </dl>                                                 | The element is enabled but in a restricted mode.<br/>                                                           |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>10</dt> </dl>                                            | The element is in the process of going to an Enabled state. New requests are queued.<br/>                       |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>11 32767</dt> </dl>                  |                                                                                                                       |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 65535</dt> </dl>       |                                                                                                                       |



 

</dd> <dt>

**GroupForwardedFragments**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to group fragments before forwarding them.



| Value                                                                                                                                                                                                                           | Meaning                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Fragments are not grouped before forwarding.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Fragments are grouped before forwarding.<br/>     |



 

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

**IcmpRedirects**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to update the path cache in response to Internet Control Message Protocol (ICMP) redirect packets.



| Value                                                                                                                                                                                                                           | Meaning                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | The path cache is not updated in response to ICMP redirect packets.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | The path cache is updated in response to ICMP redirect packets.<br/>     |



 

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

**MediaSenseEventLog**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to turn on logging for the media sensing capability.



| Value                                                                                                                                                                                                                           | Meaning                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Turns on logging for the media sensing capability.<br/>  |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Turns off logging for the media sensing capability.<br/> |



 

</dd> <dt>

**MldLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The level of multicast support.



| Value                                                                                                                                                                                                                           | Meaning                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="None"></span><span id="none"></span><span id="NONE"></span><dl> <dt>**None**</dt> <dt>0</dt> </dl>                 | Multicast packets can neither be sent nor received.<br/> |
| <span id="SendOnly"></span><span id="sendonly"></span><span id="SENDONLY"></span><dl> <dt>**SendOnly**</dt> <dt>1</dt> </dl> | Multicast packets can be sent but not received.<br/>     |
| <span id="All"></span><span id="all"></span><span id="ALL"></span><dl> <dt>**All**</dt> <dt>2</dt> </dl>                     | Multicast packets can be sent as well as received.<br/>  |



 

</dd> <dt>

**MldVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum version of Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) that the host supports.

<dl> <dt>

<span id="Version1"></span><span id="version1"></span><span id="VERSION1"></span>**Version1** (2)
</dt> <dt>

<span id="Version2"></span><span id="version2"></span><span id="VERSION2"></span>**Version2** (3)
</dt> <dt>

<span id="Version3"></span><span id="version3"></span><span id="VERSION3"></span>**Version3** (4)
</dt> </dl>

</dd> <dt>

**MulticastForwarding**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to forward multicast packets.



| Value                                                                                                                                                                                                                           | Meaning                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Multicast packets are not forwarded.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Multicast packets are forwarded.<br/>     |



 

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

A string that identifies this protocol endpoint with either a port or an interface on a device. To ensure uniqueness, the Name property should be prepended or appended with information from the Type or OtherTypeDescription properties. The method selected is described in the NameFormat property of this class.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256)
</dt> </dl>

NameFormat contains the naming heuristic that is selected to ensure that the value of the Name property is unique. For example, you might choose to prepend the name of the port or interface with the Type of ProtocolEndpoint (for example, IPv4) of this instance followed by an underscore.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**NeighborCacheLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of entries in the neighbor cache.

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

 

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).



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

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

A string that describes the enabled or disabled state of the element when the **EnabledState** property is set to 1 ("Other"). This property must be set to null when **EnabledState** is any value other than 1.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

</dd> <dt>

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ProtocolEndpoint.ProtocolType", "CIM\_ProtocolEndpoint.ProtocolIFType")
</dt> </dl>

Describes the type of Protocol Endpoint when the Type property of this class (or any of its subclasses) is set to 1 (Other). This property should be set to null when the Type property is any value other than 1.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

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

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ProtocolEndpoint.OtherTypeDescription")
</dt> </dl>

An enumeration that is synchronized with the IANA ifType MIB. The ifType MIB is maintained at the URL, http://www.iana.org/assignments/ianaiftype-mib. Also, additional values defined by the DMTF are included. The property is used to categorize and classify instances of the ProtocolEndpoint class. Note that if the ProtocolIFType is set to 1 (Other), then the type information should be provided in the OtherTypeDescription string property.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Regular_1822"></span><span id="regular_1822"></span><span id="REGULAR_1822"></span>**Regular 1822** (2)
</dt> <dt>

<span id="HDH_1822"></span><span id="hdh_1822"></span>**HDH 1822** (3)
</dt> <dt>

<span id="DDN_X.25"></span><span id="ddn_x.25"></span>**DDN X.25** (4)
</dt> <dt>

<span id="RFC877_X.25"></span><span id="rfc877_x.25"></span>**RFC877 X.25** (5)
</dt> <dt>

<span id="Ethernet_CSMA_CD"></span><span id="ethernet_csma_cd"></span><span id="ETHERNET_CSMA_CD"></span>**Ethernet CSMA/CD** (6)
</dt> <dt>

<span id="ISO_802.3_CSMA_CD"></span><span id="iso_802.3_csma_cd"></span>**ISO 802.3 CSMA/CD** (7)
</dt> <dt>

<span id="ISO_802.4_Token_Bus"></span><span id="iso_802.4_token_bus"></span><span id="ISO_802.4_TOKEN_BUS"></span>**ISO 802.4 Token Bus** (8)
</dt> <dt>

<span id="ISO_802.5_Token_Ring"></span><span id="iso_802.5_token_ring"></span><span id="ISO_802.5_TOKEN_RING"></span>**ISO 802.5 Token Ring** (9)
</dt> <dt>

<span id="ISO_802.6_MAN"></span><span id="iso_802.6_man"></span>**ISO 802.6 MAN** (10)
</dt> <dt>

<span id="StarLAN"></span><span id="starlan"></span><span id="STARLAN"></span>**StarLAN** (11)
</dt> <dt>

<span id="Proteon_10Mbit"></span><span id="proteon_10mbit"></span><span id="PROTEON_10MBIT"></span>**Proteon 10Mbit** (12)
</dt> <dt>

<span id="Proteon_80Mbit"></span><span id="proteon_80mbit"></span><span id="PROTEON_80MBIT"></span>**Proteon 80Mbit** (13)
</dt> <dt>

<span id="HyperChannel"></span><span id="hyperchannel"></span><span id="HYPERCHANNEL"></span>**HyperChannel** (14)
</dt> <dt>

<span id="FDDI"></span><span id="fddi"></span>**FDDI** (15)
</dt> <dt>

<span id="LAP-B"></span><span id="lap-b"></span>**LAP-B** (16)
</dt> <dt>

<span id="SDLC"></span><span id="sdlc"></span>**SDLC** (17)
</dt> <dt>

<span id="DS1"></span><span id="ds1"></span>**DS1** (18)
</dt> <dt>

<span id="E1"></span><span id="e1"></span>**E1** (19)
</dt> <dt>

<span id="Basic_ISDN"></span><span id="basic_isdn"></span><span id="BASIC_ISDN"></span>**Basic ISDN** (20)
</dt> <dt>

<span id="Primary_ISDN"></span><span id="primary_isdn"></span><span id="PRIMARY_ISDN"></span>**Primary ISDN** (21)
</dt> <dt>

<span id="Proprietary_Point-to-Point_Serial"></span><span id="proprietary_point-to-point_serial"></span><span id="PROPRIETARY_POINT-TO-POINT_SERIAL"></span>**Proprietary Point-to-Point Serial** (22)
</dt> <dt>

<span id="PPP"></span><span id="ppp"></span>**PPP** (23)
</dt> <dt>

<span id="Software_Loopback"></span><span id="software_loopback"></span><span id="SOFTWARE_LOOPBACK"></span>**Software Loopback** (24)
</dt> <dt>

<span id="EON"></span><span id="eon"></span>**EON** (25)
</dt> <dt>

<span id="Ethernet_3Mbit"></span><span id="ethernet_3mbit"></span><span id="ETHERNET_3MBIT"></span>**Ethernet 3Mbit** (26)
</dt> <dt>

<span id="NSIP"></span><span id="nsip"></span>**NSIP** (27)
</dt> <dt>

<span id="SLIP"></span><span id="slip"></span>**SLIP** (28)
</dt> <dt>

<span id="Ultra"></span><span id="ultra"></span><span id="ULTRA"></span>**Ultra** (29)
</dt> <dt>

<span id="DS3"></span><span id="ds3"></span>**DS3** (30)
</dt> <dt>

<span id="SIP"></span><span id="sip"></span>**SIP** (31)
</dt> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>**Frame Relay** (32)
</dt> <dt>

<span id="RS-232"></span><span id="rs-232"></span>**RS-232** (33)
</dt> <dt>

<span id="Parallel"></span><span id="parallel"></span><span id="PARALLEL"></span>**Parallel** (34)
</dt> <dt>

<span id="ARCNet"></span><span id="arcnet"></span><span id="ARCNET"></span>**ARCNet** (35)
</dt> <dt>

<span id="ARCNet_Plus"></span><span id="arcnet_plus"></span><span id="ARCNET_PLUS"></span>**ARCNet Plus** (36)
</dt> <dt>

<span id="ATM"></span><span id="atm"></span>**ATM** (37)
</dt> <dt>

<span id="MIO_X.25"></span><span id="mio_x.25"></span>**MIO X.25** (38)
</dt> <dt>

<span id="SONET"></span><span id="sonet"></span>**SONET** (39)
</dt> <dt>

<span id="X.25_PLE"></span><span id="x.25_ple"></span>**X.25 PLE** (40)
</dt> <dt>

<span id="ISO_802.211c"></span><span id="iso_802.211c"></span><span id="ISO_802.211C"></span>**ISO 802.211c** (41)
</dt> <dt>

<span id="LocalTalk"></span><span id="localtalk"></span><span id="LOCALTALK"></span>**LocalTalk** (42)
</dt> <dt>

<span id="SMDS_DXI"></span><span id="smds_dxi"></span>**SMDS DXI** (43)
</dt> <dt>

<span id="Frame_Relay_Service"></span><span id="frame_relay_service"></span><span id="FRAME_RELAY_SERVICE"></span>**Frame Relay Service** (44)
</dt> <dt>

<span id="V.35"></span><span id="v.35"></span>**V.35** (45)
</dt> <dt>

<span id="HSSI"></span><span id="hssi"></span>**HSSI** (46)
</dt> <dt>

<span id="HIPPI"></span><span id="hippi"></span>**HIPPI** (47)
</dt> <dt>

<span id="Modem"></span><span id="modem"></span><span id="MODEM"></span>**Modem** (48)
</dt> <dt>

<span id="AAL5"></span><span id="aal5"></span>**AAL5** (49)
</dt> <dt>

<span id="SONET_Path"></span><span id="sonet_path"></span><span id="SONET_PATH"></span>**SONET Path** (50)
</dt> <dt>

<span id="SONET_VT"></span><span id="sonet_vt"></span>**SONET VT** (51)
</dt> <dt>

<span id="SMDS_ICIP"></span><span id="smds_icip"></span>**SMDS ICIP** (52)
</dt> <dt>

<span id="Proprietary_Virtual_Internal"></span><span id="proprietary_virtual_internal"></span><span id="PROPRIETARY_VIRTUAL_INTERNAL"></span>**Proprietary Virtual/Internal** (53)
</dt> <dt>

<span id="Proprietary_Multiplexor"></span><span id="proprietary_multiplexor"></span><span id="PROPRIETARY_MULTIPLEXOR"></span>**Proprietary Multiplexor** (54)
</dt> <dt>

<span id="IEEE_802.12"></span><span id="ieee_802.12"></span>**IEEE 802.12** (55)
</dt> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>**Fibre Channel** (56)
</dt> <dt>

<span id="HIPPI_Interface"></span><span id="hippi_interface"></span><span id="HIPPI_INTERFACE"></span>**HIPPI Interface** (57)
</dt> <dt>

<span id="Frame_Relay_Interconnect"></span><span id="frame_relay_interconnect"></span><span id="FRAME_RELAY_INTERCONNECT"></span>**Frame Relay Interconnect** (58)
</dt> <dt>

<span id="ATM_Emulated_LAN_for_802.3"></span><span id="atm_emulated_lan_for_802.3"></span><span id="ATM_EMULATED_LAN_FOR_802.3"></span>**ATM Emulated LAN for 802.3** (59)
</dt> <dt>

<span id="ATM_Emulated_LAN_for_802.5"></span><span id="atm_emulated_lan_for_802.5"></span><span id="ATM_EMULATED_LAN_FOR_802.5"></span>**ATM Emulated LAN for 802.5** (60)
</dt> <dt>

<span id="ATM_Emulated_Circuit"></span><span id="atm_emulated_circuit"></span><span id="ATM_EMULATED_CIRCUIT"></span>**ATM Emulated Circuit** (61)
</dt> <dt>

<span id="Fast_Ethernet__100BaseT_"></span><span id="fast_ethernet__100baset_"></span><span id="FAST_ETHERNET__100BASET_"></span>**Fast Ethernet (100BaseT)** (62)
</dt> <dt>

<span id="ISDN"></span><span id="isdn"></span>**ISDN** (63)
</dt> <dt>

<span id="V.11"></span><span id="v.11"></span>**V.11** (64)
</dt> <dt>

<span id="V.36"></span><span id="v.36"></span>**V.36** (65)
</dt> <dt>

<span id="G703_at_64K"></span><span id="g703_at_64k"></span><span id="G703_AT_64K"></span>**G703 at 64K** (66)
</dt> <dt>

<span id="G703_at_2Mb"></span><span id="g703_at_2mb"></span><span id="G703_AT_2MB"></span>**G703 at 2Mb** (67)
</dt> <dt>

<span id="QLLC"></span><span id="qllc"></span>**QLLC** (68)
</dt> <dt>

<span id="Fast_Ethernet_100BaseFX"></span><span id="fast_ethernet_100basefx"></span><span id="FAST_ETHERNET_100BASEFX"></span>**Fast Ethernet 100BaseFX** (69)
</dt> <dt>

<span id="Channel"></span><span id="channel"></span><span id="CHANNEL"></span>**Channel** (70)
</dt> <dt>

<span id="IEEE_802.11"></span><span id="ieee_802.11"></span>**IEEE 802.11** (71)
</dt> <dt>

<span id="IBM_260_370_OEMI_Channel"></span><span id="ibm_260_370_oemi_channel"></span><span id="IBM_260_370_OEMI_CHANNEL"></span>**IBM 260/370 OEMI Channel** (72)
</dt> <dt>

<span id="ESCON"></span><span id="escon"></span>**ESCON** (73)
</dt> <dt>

<span id="Data_Link_Switching"></span><span id="data_link_switching"></span><span id="DATA_LINK_SWITCHING"></span>**Data Link Switching** (74)
</dt> <dt>

<span id="ISDN_S_T_Interface"></span><span id="isdn_s_t_interface"></span><span id="ISDN_S_T_INTERFACE"></span>**ISDN S/T Interface** (75)
</dt> <dt>

<span id="ISDN_U_Interface"></span><span id="isdn_u_interface"></span><span id="ISDN_U_INTERFACE"></span>**ISDN U Interface** (76)
</dt> <dt>

<span id="LAP-D"></span><span id="lap-d"></span>**LAP-D** (77)
</dt> <dt>

<span id="IP_Switch"></span><span id="ip_switch"></span><span id="IP_SWITCH"></span>**IP Switch** (78)
</dt> <dt>

<span id="Remote_Source_Route_Bridging"></span><span id="remote_source_route_bridging"></span><span id="REMOTE_SOURCE_ROUTE_BRIDGING"></span>**Remote Source Route Bridging** (79)
</dt> <dt>

<span id="ATM_Logical"></span><span id="atm_logical"></span><span id="ATM_LOGICAL"></span>**ATM Logical** (80)
</dt> <dt>

<span id="DS0"></span><span id="ds0"></span>**DS0** (81)
</dt> <dt>

<span id="DS0_Bundle"></span><span id="ds0_bundle"></span><span id="DS0_BUNDLE"></span>**DS0 Bundle** (82)
</dt> <dt>

<span id="BSC"></span><span id="bsc"></span>**BSC** (83)
</dt> <dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>**Async** (84)
</dt> <dt>

<span id="Combat_Net_Radio"></span><span id="combat_net_radio"></span><span id="COMBAT_NET_RADIO"></span>**Combat Net Radio** (85)
</dt> <dt>

<span id="ISO_802.5r_DTR"></span><span id="iso_802.5r_dtr"></span><span id="ISO_802.5R_DTR"></span>**ISO 802.5r DTR** (86)
</dt> <dt>

<span id="Ext_Pos_Loc_Report_System"></span><span id="ext_pos_loc_report_system"></span><span id="EXT_POS_LOC_REPORT_SYSTEM"></span>**Ext Pos Loc Report System** (87)
</dt> <dt>

<span id="AppleTalk_Remote_Access_Protocol"></span><span id="appletalk_remote_access_protocol"></span><span id="APPLETALK_REMOTE_ACCESS_PROTOCOL"></span>**AppleTalk Remote Access Protocol** (88)
</dt> <dt>

<span id="Proprietary_Connectionless"></span><span id="proprietary_connectionless"></span><span id="PROPRIETARY_CONNECTIONLESS"></span>**Proprietary Connectionless** (89)
</dt> <dt>

<span id="ITU_X.29_Host_PAD"></span><span id="itu_x.29_host_pad"></span><span id="ITU_X.29_HOST_PAD"></span>**ITU X.29 Host PAD** (90)
</dt> <dt>

<span id="ITU_X.3_Terminal_PAD"></span><span id="itu_x.3_terminal_pad"></span><span id="ITU_X.3_TERMINAL_PAD"></span>**ITU X.3 Terminal PAD** (91)
</dt> <dt>

<span id="Frame_Relay_MPI"></span><span id="frame_relay_mpi"></span><span id="FRAME_RELAY_MPI"></span>**Frame Relay MPI** (92)
</dt> <dt>

<span id="ITU_X.213"></span><span id="itu_x.213"></span>**ITU X.213** (93)
</dt> <dt>

<span id="ADSL"></span><span id="adsl"></span>**ADSL** (94)
</dt> <dt>

<span id="RADSL"></span><span id="radsl"></span>**RADSL** (95)
</dt> <dt>

<span id="SDSL"></span><span id="sdsl"></span>**SDSL** (96)
</dt> <dt>

<span id="VDSL"></span><span id="vdsl"></span>**VDSL** (97)
</dt> <dt>

<span id="ISO_802.5_CRFP"></span><span id="iso_802.5_crfp"></span>**ISO 802.5 CRFP** (98)
</dt> <dt>

<span id="Myrinet"></span><span id="myrinet"></span><span id="MYRINET"></span>**Myrinet** (99)
</dt> <dt>

<span id="Voice_Receive_and_Transmit"></span><span id="voice_receive_and_transmit"></span><span id="VOICE_RECEIVE_AND_TRANSMIT"></span>**Voice Receive and Transmit** (100)
</dt> <dt>

<span id="Voice_Foreign_Exchange_Office"></span><span id="voice_foreign_exchange_office"></span><span id="VOICE_FOREIGN_EXCHANGE_OFFICE"></span>**Voice Foreign Exchange Office** (101)
</dt> <dt>

<span id="Voice_Foreign_Exchange_Service"></span><span id="voice_foreign_exchange_service"></span><span id="VOICE_FOREIGN_EXCHANGE_SERVICE"></span>**Voice Foreign Exchange Service** (102)
</dt> <dt>

<span id="Voice_Encapsulation"></span><span id="voice_encapsulation"></span><span id="VOICE_ENCAPSULATION"></span>**Voice Encapsulation** (103)
</dt> <dt>

<span id="Voice_over_IP"></span><span id="voice_over_ip"></span><span id="VOICE_OVER_IP"></span>**Voice over IP** (104)
</dt> <dt>

<span id="ATM_DXI"></span><span id="atm_dxi"></span>**ATM DXI** (105)
</dt> <dt>

<span id="ATM_FUNI"></span><span id="atm_funi"></span>**ATM FUNI** (106)
</dt> <dt>

<span id="ATM_IMA"></span><span id="atm_ima"></span>**ATM IMA** (107)
</dt> <dt>

<span id="PPP_Multilink_Bundle"></span><span id="ppp_multilink_bundle"></span><span id="PPP_MULTILINK_BUNDLE"></span>**PPP Multilink Bundle** (108)
</dt> <dt>

<span id="IP_over_CDLC"></span><span id="ip_over_cdlc"></span><span id="IP_OVER_CDLC"></span>**IP over CDLC** (109)
</dt> <dt>

<span id="IP_over_CLAW"></span><span id="ip_over_claw"></span><span id="IP_OVER_CLAW"></span>**IP over CLAW** (110)
</dt> <dt>

<span id="Stack_to_Stack"></span><span id="stack_to_stack"></span><span id="STACK_TO_STACK"></span>**Stack to Stack** (111)
</dt> <dt>

<span id="Virtual_IP_Address"></span><span id="virtual_ip_address"></span><span id="VIRTUAL_IP_ADDRESS"></span>**Virtual IP Address** (112)
</dt> <dt>

<span id="MPC"></span><span id="mpc"></span>**MPC** (113)
</dt> <dt>

<span id="IP_over_ATM"></span><span id="ip_over_atm"></span><span id="IP_OVER_ATM"></span>**IP over ATM** (114)
</dt> <dt>

<span id="ISO_802.5j_Fibre_Token_Ring"></span><span id="iso_802.5j_fibre_token_ring"></span><span id="ISO_802.5J_FIBRE_TOKEN_RING"></span>**ISO 802.5j Fibre Token Ring** (115)
</dt> <dt>

<span id="TDLC"></span><span id="tdlc"></span>**TDLC** (116)
</dt> <dt>

<span id="Gigabit_Ethernet"></span><span id="gigabit_ethernet"></span><span id="GIGABIT_ETHERNET"></span>**Gigabit Ethernet** (117)
</dt> <dt>

<span id="HDLC"></span><span id="hdlc"></span>**HDLC** (118)
</dt> <dt>

<span id="LAP-F"></span><span id="lap-f"></span>**LAP-F** (119)
</dt> <dt>

<span id="V.37"></span><span id="v.37"></span>**V.37** (120)
</dt> <dt>

<span id="X.25_MLP"></span><span id="x.25_mlp"></span>**X.25 MLP** (121)
</dt> <dt>

<span id="X.25_Hunt_Group"></span><span id="x.25_hunt_group"></span><span id="X.25_HUNT_GROUP"></span>**X.25 Hunt Group** (122)
</dt> <dt>

<span id="Transp_HDLC"></span><span id="transp_hdlc"></span><span id="TRANSP_HDLC"></span>**Transp HDLC** (123)
</dt> <dt>

<span id="Interleave_Channel"></span><span id="interleave_channel"></span><span id="INTERLEAVE_CHANNEL"></span>**Interleave Channel** (124)
</dt> <dt>

<span id="FAST_Channel"></span><span id="fast_channel"></span><span id="FAST_CHANNEL"></span>**FAST Channel** (125)
</dt> <dt>

<span id="IP__for_APPN_HPR_in_IP_Networks_"></span><span id="ip__for_appn_hpr_in_ip_networks_"></span><span id="IP__FOR_APPN_HPR_IN_IP_NETWORKS_"></span>**IP (for APPN HPR in IP Networks)** (126)
</dt> <dt>

<span id="CATV_MAC_Layer"></span><span id="catv_mac_layer"></span><span id="CATV_MAC_LAYER"></span>**CATV MAC Layer** (127)
</dt> <dt>

<span id="CATV_Downstream"></span><span id="catv_downstream"></span><span id="CATV_DOWNSTREAM"></span>**CATV Downstream** (128)
</dt> <dt>

<span id="CATV_Upstream"></span><span id="catv_upstream"></span><span id="CATV_UPSTREAM"></span>**CATV Upstream** (129)
</dt> <dt>

<span id="Avalon_12MPP_Switch"></span><span id="avalon_12mpp_switch"></span><span id="AVALON_12MPP_SWITCH"></span>**Avalon 12MPP Switch** (130)
</dt> <dt>

<span id="Tunnel"></span><span id="tunnel"></span><span id="TUNNEL"></span>**Tunnel** (131)
</dt> <dt>

<span id="Coffee"></span><span id="coffee"></span><span id="COFFEE"></span>**Coffee** (132)
</dt> <dt>

<span id="Circuit_Emulation_Service"></span><span id="circuit_emulation_service"></span><span id="CIRCUIT_EMULATION_SERVICE"></span>**Circuit Emulation Service** (133)
</dt> <dt>

<span id="ATM_SubInterface"></span><span id="atm_subinterface"></span><span id="ATM_SUBINTERFACE"></span>**ATM SubInterface** (134)
</dt> <dt>

<span id="Layer_2_VLAN_using_802.1Q"></span><span id="layer_2_vlan_using_802.1q"></span><span id="LAYER_2_VLAN_USING_802.1Q"></span>**Layer 2 VLAN using 802.1Q** (135)
</dt> <dt>

<span id="Layer_3_VLAN_using_IP"></span><span id="layer_3_vlan_using_ip"></span><span id="LAYER_3_VLAN_USING_IP"></span>**Layer 3 VLAN using IP** (136)
</dt> <dt>

<span id="Layer_3_VLAN_using_IPX"></span><span id="layer_3_vlan_using_ipx"></span><span id="LAYER_3_VLAN_USING_IPX"></span>**Layer 3 VLAN using IPX** (137)
</dt> <dt>

<span id="Digital_Power_Line"></span><span id="digital_power_line"></span><span id="DIGITAL_POWER_LINE"></span>**Digital Power Line** (138)
</dt> <dt>

<span id="Multimedia_Mail_over_IP"></span><span id="multimedia_mail_over_ip"></span><span id="MULTIMEDIA_MAIL_OVER_IP"></span>**Multimedia Mail over IP** (139)
</dt> <dt>

<span id="DTM"></span><span id="dtm"></span>**DTM** (140)
</dt> <dt>

<span id="DCN"></span><span id="dcn"></span>**DCN** (141)
</dt> <dt>

<span id="IP_Forwarding"></span><span id="ip_forwarding"></span><span id="IP_FORWARDING"></span>**IP Forwarding** (142)
</dt> <dt>

<span id="MSDSL"></span><span id="msdsl"></span>**MSDSL** (143)
</dt> <dt>

<span id="IEEE_1394"></span><span id="ieee_1394"></span>**IEEE 1394** (144)
</dt> <dt>

<span id="IF-GSN_HIPPI-6400"></span><span id="if-gsn_hippi-6400"></span>**IF-GSN/HIPPI-6400** (145)
</dt> <dt>

<span id="DVB-RCC_MAC_Layer"></span><span id="dvb-rcc_mac_layer"></span><span id="DVB-RCC_MAC_LAYER"></span>**DVB-RCC MAC Layer** (146)
</dt> <dt>

<span id="DVB-RCC_Downstream"></span><span id="dvb-rcc_downstream"></span><span id="DVB-RCC_DOWNSTREAM"></span>**DVB-RCC Downstream** (147)
</dt> <dt>

<span id="DVB-RCC_Upstream"></span><span id="dvb-rcc_upstream"></span><span id="DVB-RCC_UPSTREAM"></span>**DVB-RCC Upstream** (148)
</dt> <dt>

<span id="ATM_Virtual"></span><span id="atm_virtual"></span><span id="ATM_VIRTUAL"></span>**ATM Virtual** (149)
</dt> <dt>

<span id="MPLS_Tunnel"></span><span id="mpls_tunnel"></span><span id="MPLS_TUNNEL"></span>**MPLS Tunnel** (150)
</dt> <dt>

<span id="SRP"></span><span id="srp"></span>**SRP** (151)
</dt> <dt>

<span id="Voice_over_ATM"></span><span id="voice_over_atm"></span><span id="VOICE_OVER_ATM"></span>**Voice over ATM** (152)
</dt> <dt>

<span id="Voice_over_Frame_Relay"></span><span id="voice_over_frame_relay"></span><span id="VOICE_OVER_FRAME_RELAY"></span>**Voice over Frame Relay** (153)
</dt> <dt>

<span id="ISDL"></span><span id="isdl"></span>**ISDL** (154)
</dt> <dt>

<span id="Composite_Link"></span><span id="composite_link"></span><span id="COMPOSITE_LINK"></span>**Composite Link** (155)
</dt> <dt>

<span id="SS7_Signaling_Link"></span><span id="ss7_signaling_link"></span><span id="SS7_SIGNALING_LINK"></span>**SS7 Signaling Link** (156)
</dt> <dt>

<span id="Proprietary_P2P_Wireless"></span><span id="proprietary_p2p_wireless"></span><span id="PROPRIETARY_P2P_WIRELESS"></span>**Proprietary P2P Wireless** (157)
</dt> <dt>

<span id="Frame_Forward"></span><span id="frame_forward"></span><span id="FRAME_FORWARD"></span>**Frame Forward** (158)
</dt> <dt>

<span id="RFC1483_Multiprotocol_over_ATM"></span><span id="rfc1483_multiprotocol_over_atm"></span><span id="RFC1483_MULTIPROTOCOL_OVER_ATM"></span>**RFC1483 Multiprotocol over ATM** (159)
</dt> <dt>

<span id="USB"></span><span id="usb"></span>**USB** (160)
</dt> <dt>

<span id="IEEE_802.3ad_Link_Aggregate"></span><span id="ieee_802.3ad_link_aggregate"></span><span id="IEEE_802.3AD_LINK_AGGREGATE"></span>**IEEE 802.3ad Link Aggregate** (161)
</dt> <dt>

<span id="BGP_Policy_Accounting"></span><span id="bgp_policy_accounting"></span><span id="BGP_POLICY_ACCOUNTING"></span>**BGP Policy Accounting** (162)
</dt> <dt>

<span id="FRF_.16_Multilink_FR"></span><span id="frf_.16_multilink_fr"></span><span id="FRF_.16_MULTILINK_FR"></span>**FRF .16 Multilink FR** (163)
</dt> <dt>

<span id="H.323_Gatekeeper"></span><span id="h.323_gatekeeper"></span><span id="H.323_GATEKEEPER"></span>**H.323 Gatekeeper** (164)
</dt> <dt>

<span id="H.323_Proxy"></span><span id="h.323_proxy"></span><span id="H.323_PROXY"></span>**H.323 Proxy** (165)
</dt> <dt>

<span id="MPLS"></span><span id="mpls"></span>**MPLS** (166)
</dt> <dt>

<span id="Multi-Frequency_Signaling_Link"></span><span id="multi-frequency_signaling_link"></span><span id="MULTI-FREQUENCY_SIGNALING_LINK"></span>**Multi-Frequency Signaling Link** (167)
</dt> <dt>

<span id="HDSL-2"></span><span id="hdsl-2"></span>**HDSL-2** (168)
</dt> <dt>

<span id="S-HDSL"></span><span id="s-hdsl"></span>**S-HDSL** (169)
</dt> <dt>

<span id="DS1_Facility_Data_Link"></span><span id="ds1_facility_data_link"></span><span id="DS1_FACILITY_DATA_LINK"></span>**DS1 Facility Data Link** (170)
</dt> <dt>

<span id="Packet_over_SONET_SDH"></span><span id="packet_over_sonet_sdh"></span><span id="PACKET_OVER_SONET_SDH"></span>**Packet over SONET/SDH** (171)
</dt> <dt>

<span id="DVB-ASI_Input"></span><span id="dvb-asi_input"></span><span id="DVB-ASI_INPUT"></span>**DVB-ASI Input** (172)
</dt> <dt>

<span id="DVB-ASI_Output"></span><span id="dvb-asi_output"></span><span id="DVB-ASI_OUTPUT"></span>**DVB-ASI Output** (173)
</dt> <dt>

<span id="Power_Line"></span><span id="power_line"></span><span id="POWER_LINE"></span>**Power Line** (174)
</dt> <dt>

<span id="Non_Facility_Associated_Signaling"></span><span id="non_facility_associated_signaling"></span><span id="NON_FACILITY_ASSOCIATED_SIGNALING"></span>**Non Facility Associated Signaling** (175)
</dt> <dt>

<span id="TR008"></span><span id="tr008"></span>**TR008** (176)
</dt> <dt>

<span id="GR303_RDT"></span><span id="gr303_rdt"></span>**GR303 RDT** (177)
</dt> <dt>

<span id="GR303_IDT"></span><span id="gr303_idt"></span>**GR303 IDT** (178)
</dt> <dt>

<span id="ISUP"></span><span id="isup"></span>**ISUP** (179)
</dt> <dt>

<span id="Proprietary_Wireless_MAC_Layer"></span><span id="proprietary_wireless_mac_layer"></span><span id="PROPRIETARY_WIRELESS_MAC_LAYER"></span>**Proprietary Wireless MAC Layer** (180)
</dt> <dt>

<span id="Proprietary_Wireless_Downstream"></span><span id="proprietary_wireless_downstream"></span><span id="PROPRIETARY_WIRELESS_DOWNSTREAM"></span>**Proprietary Wireless Downstream** (181)
</dt> <dt>

<span id="Proprietary_Wireless_Upstream"></span><span id="proprietary_wireless_upstream"></span><span id="PROPRIETARY_WIRELESS_UPSTREAM"></span>**Proprietary Wireless Upstream** (182)
</dt> <dt>

<span id="HIPERLAN_Type_2"></span><span id="hiperlan_type_2"></span><span id="HIPERLAN_TYPE_2"></span>**HIPERLAN Type 2** (183)
</dt> <dt>

<span id="Proprietary_Broadband_Wireless_Access_Point_to_Mulipoint"></span><span id="proprietary_broadband_wireless_access_point_to_mulipoint"></span><span id="PROPRIETARY_BROADBAND_WIRELESS_ACCESS_POINT_TO_MULIPOINT"></span>**Proprietary Broadband Wireless Access Point to Mulipoint** (184)
</dt> <dt>

<span id="SONET_Overhead_Channel"></span><span id="sonet_overhead_channel"></span><span id="SONET_OVERHEAD_CHANNEL"></span>**SONET Overhead Channel** (185)
</dt> <dt>

<span id="Digital_Wrapper_Overhead_Channel"></span><span id="digital_wrapper_overhead_channel"></span><span id="DIGITAL_WRAPPER_OVERHEAD_CHANNEL"></span>**Digital Wrapper Overhead Channel** (186)
</dt> <dt>

<span id="ATM_Adaptation_Layer_2"></span><span id="atm_adaptation_layer_2"></span><span id="ATM_ADAPTATION_LAYER_2"></span>**ATM Adaptation Layer 2** (187)
</dt> <dt>

<span id="Radio_MAC"></span><span id="radio_mac"></span><span id="RADIO_MAC"></span>**Radio MAC** (188)
</dt> <dt>

<span id="ATM_Radio"></span><span id="atm_radio"></span><span id="ATM_RADIO"></span>**ATM Radio** (189)
</dt> <dt>

<span id="Inter_Machine_Trunk"></span><span id="inter_machine_trunk"></span><span id="INTER_MACHINE_TRUNK"></span>**Inter Machine Trunk** (190)
</dt> <dt>

<span id="MVL_DSL"></span><span id="mvl_dsl"></span>**MVL DSL** (191)
</dt> <dt>

<span id="Long_Read_DSL"></span><span id="long_read_dsl"></span><span id="LONG_READ_DSL"></span>**Long Read DSL** (192)
</dt> <dt>

<span id="Frame_Relay_DLCI_Endpoint"></span><span id="frame_relay_dlci_endpoint"></span><span id="FRAME_RELAY_DLCI_ENDPOINT"></span>**Frame Relay DLCI Endpoint** (193)
</dt> <dt>

<span id="ATM_VCI_Endpoint"></span><span id="atm_vci_endpoint"></span><span id="ATM_VCI_ENDPOINT"></span>**ATM VCI Endpoint** (194)
</dt> <dt>

<span id="Optical_Channel"></span><span id="optical_channel"></span><span id="OPTICAL_CHANNEL"></span>**Optical Channel** (195)
</dt> <dt>

<span id="Optical_Transport"></span><span id="optical_transport"></span><span id="OPTICAL_TRANSPORT"></span>**Optical Transport** (196)
</dt> <dt>

<span id="Proprietary_ATM"></span><span id="proprietary_atm"></span><span id="PROPRIETARY_ATM"></span>**Proprietary ATM** (197)
</dt> <dt>

<span id="Voice_over_Cable"></span><span id="voice_over_cable"></span><span id="VOICE_OVER_CABLE"></span>**Voice over Cable** (198)
</dt> <dt>

<span id="Infiniband"></span><span id="infiniband"></span><span id="INFINIBAND"></span>**Infiniband** (199)
</dt> <dt>

<span id="TE_Link"></span><span id="te_link"></span><span id="TE_LINK"></span>**TE Link** (200)
</dt> <dt>

<span id="Q.2931"></span><span id="q.2931"></span>**Q.2931** (201)
</dt> <dt>

<span id="Virtual_Trunk_Group"></span><span id="virtual_trunk_group"></span><span id="VIRTUAL_TRUNK_GROUP"></span>**Virtual Trunk Group** (202)
</dt> <dt>

<span id="SIP_Trunk_Group"></span><span id="sip_trunk_group"></span><span id="SIP_TRUNK_GROUP"></span>**SIP Trunk Group** (203)
</dt> <dt>

<span id="SIP_Signaling"></span><span id="sip_signaling"></span><span id="SIP_SIGNALING"></span>**SIP Signaling** (204)
</dt> <dt>

<span id="CATV_Upstream_Channel"></span><span id="catv_upstream_channel"></span><span id="CATV_UPSTREAM_CHANNEL"></span>**CATV Upstream Channel** (205)
</dt> <dt>

<span id="Econet"></span><span id="econet"></span><span id="ECONET"></span>**Econet** (206)
</dt> <dt>

<span id="FSAN_155Mb_PON"></span><span id="fsan_155mb_pon"></span><span id="FSAN_155MB_PON"></span>**FSAN 155Mb PON** (207)
</dt> <dt>

<span id="FSAN_622Mb_PON"></span><span id="fsan_622mb_pon"></span><span id="FSAN_622MB_PON"></span>**FSAN 622Mb PON** (208)
</dt> <dt>

<span id="Transparent_Bridge"></span><span id="transparent_bridge"></span><span id="TRANSPARENT_BRIDGE"></span>**Transparent Bridge** (209)
</dt> <dt>

<span id="Line_Group"></span><span id="line_group"></span><span id="LINE_GROUP"></span>**Line Group** (210)
</dt> <dt>

<span id="Voice_E_M_Feature_Group"></span><span id="voice_e_m_feature_group"></span><span id="VOICE_E_M_FEATURE_GROUP"></span>**Voice E&M Feature Group** (211)
</dt> <dt>

<span id="Voice_FGD_EANA"></span><span id="voice_fgd_eana"></span><span id="VOICE_FGD_EANA"></span>**Voice FGD EANA** (212)
</dt> <dt>

<span id="Voice_DID"></span><span id="voice_did"></span><span id="VOICE_DID"></span>**Voice DID** (213)
</dt> <dt>

<span id="MPEG_Transport"></span><span id="mpeg_transport"></span><span id="MPEG_TRANSPORT"></span>**MPEG Transport** (214)
</dt> <dt>

<span id="6To4"></span><span id="6to4"></span><span id="6TO4"></span>**6To4** (215)
</dt> <dt>

<span id="GTP"></span><span id="gtp"></span>**GTP** (216)
</dt> <dt>

<span id="Paradyne_EtherLoop_1"></span><span id="paradyne_etherloop_1"></span><span id="PARADYNE_ETHERLOOP_1"></span>**Paradyne EtherLoop 1** (217)
</dt> <dt>

<span id="Paradyne_EtherLoop_2"></span><span id="paradyne_etherloop_2"></span><span id="PARADYNE_ETHERLOOP_2"></span>**Paradyne EtherLoop 2** (218)
</dt> <dt>

<span id="Optical_Channel_Group"></span><span id="optical_channel_group"></span><span id="OPTICAL_CHANNEL_GROUP"></span>**Optical Channel Group** (219)
</dt> <dt>

<span id="HomePNA"></span><span id="homepna"></span><span id="HOMEPNA"></span>**HomePNA** (220)
</dt> <dt>

<span id="GFP"></span><span id="gfp"></span>**GFP** (221)
</dt> <dt>

<span id="ciscoISLvlan"></span><span id="ciscoislvlan"></span><span id="CISCOISLVLAN"></span>**ciscoISLvlan** (222)
</dt> <dt>

<span id="actelisMetaLOOP"></span><span id="actelismetaloop"></span><span id="ACTELISMETALOOP"></span>**actelisMetaLOOP** (223)
</dt> <dt>

<span id="Fcip"></span><span id="fcip"></span><span id="FCIP"></span>**Fcip** (224)
</dt> <dt>

<span id="IANA_Reserved"></span><span id="iana_reserved"></span><span id="IANA_RESERVED"></span>**IANA Reserved** (225 4095)
</dt> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (4096)
</dt> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (4097)
</dt> <dt>

<span id="IPv4_v6"></span><span id="ipv4_v6"></span><span id="IPV4_V6"></span>**IPv4/v6** (4098)
</dt> <dt>

<span id="IPX"></span><span id="ipx"></span>**IPX** (4099)
</dt> <dt>

<span id="DECnet"></span><span id="decnet"></span><span id="DECNET"></span>**DECnet** (4100)
</dt> <dt>

<span id="SNA"></span><span id="sna"></span>**SNA** (4101)
</dt> <dt>

<span id="CONP"></span><span id="conp"></span>**CONP** (4102)
</dt> <dt>

<span id="CLNP"></span><span id="clnp"></span>**CLNP** (4103)
</dt> <dt>

<span id="VINES"></span><span id="vines"></span>**VINES** (4104)
</dt> <dt>

<span id="XNS"></span><span id="xns"></span>**XNS** (4105)
</dt> <dt>

<span id="ISDN_B_Channel_Endpoint"></span><span id="isdn_b_channel_endpoint"></span><span id="ISDN_B_CHANNEL_ENDPOINT"></span>**ISDN B Channel Endpoint** (4106)
</dt> <dt>

<span id="ISDN_D_Channel_Endpoint"></span><span id="isdn_d_channel_endpoint"></span><span id="ISDN_D_CHANNEL_ENDPOINT"></span>**ISDN D Channel Endpoint** (4107)
</dt> <dt>

<span id="BGP"></span><span id="bgp"></span>**BGP** (4108)
</dt> <dt>

<span id="OSPF"></span><span id="ospf"></span>**OSPF** (4109)
</dt> <dt>

<span id="UDP"></span><span id="udp"></span>**UDP** (4110)
</dt> <dt>

<span id="TCP"></span><span id="tcp"></span>**TCP** (4111)
</dt> <dt>

<span id="802.11a"></span><span id="802.11A"></span>**802.11a** (4112)
</dt> <dt>

<span id="802.11b"></span><span id="802.11B"></span>**802.11b** (4113)
</dt> <dt>

<span id="802.11g"></span><span id="802.11G"></span>**802.11g** (4114)
</dt> <dt>

<span id="802.11h"></span><span id="802.11H"></span>**802.11h** (4115)
</dt> <dt>

<span id="NFS"></span><span id="nfs"></span>**NFS** (4200)
</dt> <dt>

<span id="CIFS"></span><span id="cifs"></span>**CIFS** (4201)
</dt> <dt>

<span id="DAFS"></span><span id="dafs"></span>**DAFS** (4202)
</dt> <dt>

<span id="WebDAV"></span><span id="webdav"></span><span id="WEBDAV"></span>**WebDAV** (4203)
</dt> <dt>

<span id="HTTP"></span><span id="http"></span>**HTTP** (4204)
</dt> <dt>

<span id="FTP"></span><span id="ftp"></span>**FTP** (4205)
</dt> <dt>

<span id="NDMP"></span><span id="ndmp"></span>**NDMP** (4300)
</dt> <dt>

<span id="Telnet"></span><span id="telnet"></span><span id="TELNET"></span>**Telnet** (4400)
</dt> <dt>

<span id="SSH"></span><span id="ssh"></span>**SSH** (4401)
</dt> <dt>

<span id="SM_CLP"></span><span id="sm_clp"></span>**SM CLP** (4402)
</dt> <dt>

<span id="SMTP"></span><span id="smtp"></span>**SMTP** (4403)
</dt> <dt>

<span id="LDAP"></span><span id="ldap"></span>**LDAP** (4404)
</dt> <dt>

<span id="RDP"></span><span id="rdp"></span>**RDP** (4405)
</dt> <dt>

<span id="HTTPS"></span><span id="https"></span>**HTTPS** (4406)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (4407 32767)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768 65535)
</dt> </dl>

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/win32/wmisdk/standard-wmi-qualifiers) ("CIM\_ProtocolEndpoint.ProtocolIFType"), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_ProtocolEndpoint.OtherTypeDescription")
</dt> </dl>

Note: This property is deprecated in lieu of the ProtocolIFType enumeration. This deprecation was done to have better alignment between the IF-MIB of the IETF and this CIM class.

Deprecated description: ProtocolType is an enumeration that provides information to categorize and classify different instances of this class. For most instances, information in this enumeration and the definition of the subclass overlap. However, there are several cases where a specific subclass of ProtocolEndpoint is not required (for example, there is no Fibre Channel subclass of ProtocolEndpoint). Therefore, this property is needed to define the type of Endpoint.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (2)
</dt> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (3)
</dt> <dt>

<span id="IPX"></span><span id="ipx"></span>**IPX** (4)
</dt> <dt>

<span id="AppleTalk"></span><span id="appletalk"></span><span id="APPLETALK"></span>**AppleTalk** (5)
</dt> <dt>

<span id="DECnet"></span><span id="decnet"></span><span id="DECNET"></span>**DECnet** (6)
</dt> <dt>

<span id="SNA"></span><span id="sna"></span>**SNA** (7)
</dt> <dt>

<span id="CONP"></span><span id="conp"></span>**CONP** (8)
</dt> <dt>

<span id="CLNP"></span><span id="clnp"></span>**CLNP** (9)
</dt> <dt>

<span id="VINES"></span><span id="vines"></span>**VINES** (10)
</dt> <dt>

<span id="XNS"></span><span id="xns"></span>**XNS** (11)
</dt> <dt>

<span id="ATM"></span><span id="atm"></span>**ATM** (12)
</dt> <dt>

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>**Frame Relay** (13)
</dt> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>**Ethernet** (14)
</dt> <dt>

<span id="TokenRing"></span><span id="tokenring"></span><span id="TOKENRING"></span>**TokenRing** (15)
</dt> <dt>

<span id="FDDI"></span><span id="fddi"></span>**FDDI** (16)
</dt> <dt>

<span id="Infiniband"></span><span id="infiniband"></span><span id="INFINIBAND"></span>**Infiniband** (17)
</dt> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>**Fibre Channel** (18)
</dt> <dt>

<span id="ISDN_BRI_Endpoint"></span><span id="isdn_bri_endpoint"></span><span id="ISDN_BRI_ENDPOINT"></span>**ISDN BRI Endpoint** (19)
</dt> <dt>

<span id="ISDN_B_Channel_Endpoint"></span><span id="isdn_b_channel_endpoint"></span><span id="ISDN_B_CHANNEL_ENDPOINT"></span>**ISDN B Channel Endpoint** (20)
</dt> <dt>

<span id="ISDN_D_Channel_Endpoint"></span><span id="isdn_d_channel_endpoint"></span><span id="ISDN_D_CHANNEL_ENDPOINT"></span>**ISDN D Channel Endpoint** (21)
</dt> <dt>

<span id="IPv4_v6"></span><span id="ipv4_v6"></span><span id="IPV4_V6"></span>**IPv4/v6** (22)
</dt> <dt>

<span id="BGP"></span><span id="bgp"></span>**BGP** (23)
</dt> <dt>

<span id="OSPF"></span><span id="ospf"></span>**OSPF** (24)
</dt> <dt>

<span id="MPLS"></span><span id="mpls"></span>**MPLS** (25)
</dt> <dt>

<span id="UDP"></span><span id="udp"></span>**UDP** (26)
</dt> <dt>

<span id="TCP"></span><span id="tcp"></span>**TCP** (27)
</dt> </dl>

</dd> <dt>

**RandomizeIdentifiers**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to randomize interface identifiers.



| Value                                                                                                                                                                                                                           | Meaning                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | Interface identifiers are not randomized.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | Interface identifiers are randomized.<br/>     |



 

</dd> <dt>

**ReassemblyLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum size of the reassembly buffer, in bytes.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

**RequestedState** is an integer enumeration that indicates the last requested or desired state for the element. The actual state of the element is represented by **EnabledState**. This property is provided to compare the last requested and current enabled or disabled states. Note that when **EnabledState** is set to 5 ("Not Applicable"), then this property has no meaning. By default, the **RequestedState** of the element is 5 ("No Change"). Refer to the **EnabledState** property description for explanations of the values in the **RequestedState** enumeration. It should be noted that there are two new values in **RequestedState** that build on the statuses of **EnabledState**. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. This property is set as the result of a method invocation (such as [**StartService**](/windows/win32/cimwin32prov/startservice-method-in-class-cim-service) or [**StopService**](/windows/win32/cimwin32prov/stopservice-method-in-class-cim-service) on [**CIM\_Service**](/windows/win32/cimwin32prov/cim-service)), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. A particular instance of [**CIM\_EnabledLogicalElement**](./cim-enabledlogicalelement.md) might not support [**RequestStateChange**](/previous-versions//cc137002(v=vs.85)). If this occurs, the value 12 ("Not Applicable") is used.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)
</dt> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>**Shut Down** (4)
</dt> <dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>**No Change** (5)
</dt> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (6)
</dt> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test** (7)
</dt> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>**Deferred** (8)
</dt> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (9)
</dt> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>**Reboot** (10)
</dt> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>**Reset** (11)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (13 32767)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768 65535)
</dt> </dl>

</dd> <dt>

**RouteCacheLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum number of entries in the route cache.

</dd> <dt>

**SourceRoutingBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The behavior for source-routed packets. Per RFC 5095, support for forwarding of source-routed IPv6 packets was removed, and a value for **Forward** has the same effect as **DontForward**.

<dl> <dt>

<span id="Forward"></span><span id="forward"></span><span id="FORWARD"></span>**Forward** (0)
</dt> <dt>

<span id="DontForward"></span><span id="dontforward"></span><span id="DONTFORWARD"></span>**DontForward** (1)
</dt> <dt>

<span id="Drop"></span><span id="drop"></span><span id="DROP"></span>**Drop** (2)
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

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**Propagated**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_System.CreationClassName")
</dt> </dl>

The CreationClassName of the scoping System.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**Propagated**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_System.Name")
</dt> </dl>

The Name of the scoping System.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date or time when the EnabledState of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md).

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_EnabledLogicalElement.RequestStateChange", "CIM\_EnabledLogicalElement.RequestedState", "CIM\_EnabledLogicalElement.EnabledState")
</dt> </dl>

TransitioningToState indicates the target state to which the instance is transitioning.

A value of 5 "No Change" shall indicate that no transition is in progress.A value of 12 "Not Applicable" shall indicate the implementation does not support representing ongoing transitions.

A value other than 5 or 12 shall identify the state to which the element is in the process of transitioning.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)
</dt> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)
</dt> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>**Shut Down** (4)
</dt> <dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>**No Change** (5)
</dt> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (6)
</dt> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test** (7)
</dt> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>**Defer** (8)
</dt> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (9)
</dt> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>**Reboot** (10)
</dt> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>**Reset** (11)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (12)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (13 65535)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



 

