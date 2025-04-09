---
description: Represents a TCIP/IP (Internet Protocol Suite) neighbor.
ms.assetid: 31e7a7bd-83b0-4da0-809d-a5ba8940a9fc
title: MSFT\_NetNeighbor class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# MSFT\_NetNeighbor class

Represents a TCIP/IP (Internet Protocol Suite) neighbor.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::Service"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetNeighbor : CIM_RemoteServiceAccessPoint
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
  uint16   EnabledState = 5;
  string   OtherEnabledState;
  uint16   RequestedState = 12;
  uint16   EnabledDefault = 2;
  datetime TimeOfLastStateChange;
  uint16   TransitioningToState = 12;
  uint16   AvailableRequestedStates[];
  string   Name;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  string   AccessInfo;
  uint16   InfoFormat;
  string   OtherInfoFormatDescription;
  uint16   AccessContext = 0;
  string   OtherAccessContext;
  string   IPAddress;
  uint32   InterfaceIndex;
  string   InterfaceAlias;
  string   LinkLayerAddress;
  uint8    Store;
  uint8    State;
  uint16   AddressFamily;
};
```

## Members

The **MSFT\_NetNeighbor** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetNeighbor** class has these methods.



| Method                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Create**](create-msft-netneighbor.md)                         | Creates a TCP/IP neighbor.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**RequestStateChange**](msft-netneighbor-requeststatechange.md) | Requests that the state of the element be changed to the value specified in the *RequestedState* parameter. When the requested state change takes place, the enabled state and requested state of the element will be the same. Invoking the **RequestChangeState** method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully and the use of [**CIM\_ConcreteJob**](cim-concretejob.md) was not required. If 4096 (0x1000) is returned, then the task will take some time to complete, **CIM\_ConcreteJob** will be created, and its reference returned in the output parameter *Job*. Any other return code indicates an error condition.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/> |



 

### Properties

The **MSFT\_NetNeighbor** class has these properties.

<dl> <dt>

**AccessContext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_RemoteServiceAccessPoint.OtherAccessContext")
</dt> </dl>

The AccessContext property identifies the role this RemoteServiceAccessPoint is playing in the hosting system.

This property is inherited from [**CIM\_RemoteServiceAccessPoint**](cim-remoteserviceaccesspoint.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Default_Gateway"></span><span id="default_gateway"></span><span id="DEFAULT_GATEWAY"></span>**Default Gateway** (2)
</dt> <dt>

<span id="DNS_Server"></span><span id="dns_server"></span><span id="DNS_SERVER"></span>**DNS Server** (3)
</dt> <dt>

<span id="SNMP_Trap_Destination"></span><span id="snmp_trap_destination"></span><span id="SNMP_TRAP_DESTINATION"></span>**SNMP Trap Destination** (4)
</dt> <dt>

<span id="MPLS_Tunnel_Destination"></span><span id="mpls_tunnel_destination"></span><span id="MPLS_TUNNEL_DESTINATION"></span>**MPLS Tunnel Destination** (5)
</dt> <dt>

<span id="DHCP_Server"></span><span id="dhcp_server"></span><span id="DHCP_SERVER"></span>**DHCP Server** (6)
</dt> <dt>

<span id="SMTP_Server"></span><span id="smtp_server"></span><span id="SMTP_SERVER"></span>**SMTP Server** (7)
</dt> <dt>

<span id="LDAP_Server"></span><span id="ldap_server"></span><span id="LDAP_SERVER"></span>**LDAP Server** (8)
</dt> <dt>

<span id="Network_Time_Protocol__NTP__Server"></span><span id="network_time_protocol__ntp__server"></span><span id="NETWORK_TIME_PROTOCOL__NTP__SERVER"></span>**Network Time Protocol (NTP) Server** (9)
</dt> <dt>

<span id="Management_Service"></span><span id="management_service"></span><span id="MANAGEMENT_SERVICE"></span>**Management Service** (10)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (11 32767)
</dt> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (32768 65535)
</dt> </dl>

</dd> <dt>

**AccessInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_RemoteServiceAccessPoint.InfoFormat")
</dt> </dl>

Access or addressing information or a combination of this information for a remote connection. This information can be a host name, network address, or similar information.

This property is inherited from [**CIM\_RemoteServiceAccessPoint**](cim-remoteserviceaccesspoint.md).

</dd> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that specifies the address family of the neighbor. This property contains one of the following values.



| Value                                                                                                                                                                                                            | Meaning                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span><dl> <dt>**IPv4**</dt> <dt>2</dt> </dl>  | The address family is IPv4.<br/> |
| <span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span><dl> <dt>**IPv6**</dt> <dt>23</dt> </dl> | The address family is IPv6.<br/> |



 

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

Indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).



| Value                                                                                                                                                                                                                                                                       | Meaning                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                 |                                                                                                                                                                                                                 |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                         |                                                                                                                                                                                                                 |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>2</dt> </dl>                                                 | The element is or could be executing commands, will process any queued commands, and queues new requests.<br/>                                                                                            |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>3</dt> </dl>                                             | The element will not execute commands and will drop any new requests.<br/>                                                                                                                                |
| <span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span><dl> <dt>**Shutting Down**</dt> <dt>4</dt> </dl>                         | The element is in the process of going to a Disabled state.<br/>                                                                                                                                          |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>5</dt> </dl>                     | The element does not support being enabled or disabled.<br/>                                                                                                                                              |
| <span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span><dl> <dt>**Enabled but Offline**</dt> <dt>6</dt> </dl> | The element might be completing commands, and will drop any new requests.<br/>                                                                                                                            |
| <span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span><dl> <dt>**In Test**</dt> <dt>7</dt> </dl>                                                 | The element is in a test state.<br/>                                                                                                                                                                      |
| <span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span><dl> <dt>**Deferred**</dt> <dt>8</dt> </dl>                                             | The element might be completing commands, but will queue any new requests.<br/>                                                                                                                           |
| <span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span><dl> <dt>**Quiesce**</dt> <dt>9</dt> </dl>                                                 | The element is enabled but in a restricted mode. The behavior of the element is similar to the Enabled state (2), but it processes only a restricted set of commands. All other requests are queued.<br/> |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>10</dt> </dl>                                            | The element is in the process of going to an Enabled state (2). New requests are queued.<br/>                                                                                                             |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>11 32767</dt> </dl>                  | Reserved.<br/>                                                                                                                                                                                            |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 65535</dt> </dl>       | Reserved.<br/>                                                                                                                                                                                            |



 

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

**InfoFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_RemoteServiceAccessPoint.OtherInfoFormatDescription")
</dt> </dl>

An enumerated integer that describes the format and interpretation of the AccessInfo property.

206\\'Parameterized URL\\'- a URL containing ${parameterName} strings. Those strings are intended to be replaced in their entirety by the value of the named parameter. The interpretation of such parameters is not defined by this subclass.

As an example use: If a parameter named \\'CompanyURL\\' has a value of 'www.DMTF.org' and the value of AccessInfo was 'http:\\${CompanyURL}', then the resultant URL is intended to be 'http:\\www.dmtf.org'.

This property is inherited from [**CIM\_RemoteServiceAccessPoint**](cim-remoteserviceaccesspoint.md).



| Value                                                                                                                                                                                                                                                                                           | Meaning |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                             |         |
| <span id="Host_Name"></span><span id="host_name"></span><span id="HOST_NAME"></span><dl> <dt>**Host Name**</dt> <dt>2</dt> </dl>                                                             |         |
| <span id="IPv4_Address"></span><span id="ipv4_address"></span><span id="IPV4_ADDRESS"></span><dl> <dt>**IPv4 Address**</dt> <dt>3</dt> </dl>                                                 |         |
| <span id="IPv6_Address"></span><span id="ipv6_address"></span><span id="IPV6_ADDRESS"></span><dl> <dt>**IPv6 Address**</dt> <dt>4</dt> </dl>                                                 |         |
| <span id="IPX_Address"></span><span id="ipx_address"></span><span id="IPX_ADDRESS"></span><dl> <dt>**IPX Address**</dt> <dt>5</dt> </dl>                                                     |         |
| <span id="DECnet_Address"></span><span id="decnet_address"></span><span id="DECNET_ADDRESS"></span><dl> <dt>**DECnet Address**</dt> <dt>6</dt> </dl>                                         |         |
| <span id="SNA_Address"></span><span id="sna_address"></span><span id="SNA_ADDRESS"></span><dl> <dt>**SNA Address**</dt> <dt>7</dt> </dl>                                                     |         |
| <span id="Autonomous_System_Number"></span><span id="autonomous_system_number"></span><span id="AUTONOMOUS_SYSTEM_NUMBER"></span><dl> <dt>**Autonomous System Number**</dt> <dt>8</dt> </dl> |         |
| <span id="MPLS_Label"></span><span id="mpls_label"></span><span id="MPLS_LABEL"></span><dl> <dt>**MPLS Label**</dt> <dt>9</dt> </dl>                                                         |         |
| <span id="IPv4_Subnet_Address"></span><span id="ipv4_subnet_address"></span><span id="IPV4_SUBNET_ADDRESS"></span><dl> <dt>**IPv4 Subnet Address**</dt> <dt>10</dt> </dl>                    |         |
| <span id="IPv6_Subnet_Address"></span><span id="ipv6_subnet_address"></span><span id="IPV6_SUBNET_ADDRESS"></span><dl> <dt>**IPv6 Subnet Address**</dt> <dt>11</dt> </dl>                    |         |
| <span id="IPv4_Address_Range"></span><span id="ipv4_address_range"></span><span id="IPV4_ADDRESS_RANGE"></span><dl> <dt>**IPv4 Address Range**</dt> <dt>12</dt> </dl>                        |         |
| <span id="IPv6_Address_Range"></span><span id="ipv6_address_range"></span><span id="IPV6_ADDRESS_RANGE"></span><dl> <dt>**IPv6 Address Range**</dt> <dt>13</dt> </dl>                        |         |
| <span id="Dial_String"></span><span id="dial_string"></span><span id="DIAL_STRING"></span><dl> <dt>**Dial String**</dt> <dt>100</dt> </dl>                                                   |         |
| <span id="Ethernet_Address"></span><span id="ethernet_address"></span><span id="ETHERNET_ADDRESS"></span><dl> <dt>**Ethernet Address**</dt> <dt>101</dt> </dl>                               |         |
| <span id="Token_Ring_Address"></span><span id="token_ring_address"></span><span id="TOKEN_RING_ADDRESS"></span><dl> <dt>**Token Ring Address**</dt> <dt>102</dt> </dl>                       |         |
| <span id="ATM_Address"></span><span id="atm_address"></span><span id="ATM_ADDRESS"></span><dl> <dt>**ATM Address**</dt> <dt>103</dt> </dl>                                                   |         |
| <span id="Frame_Relay_Address"></span><span id="frame_relay_address"></span><span id="FRAME_RELAY_ADDRESS"></span><dl> <dt>**Frame Relay Address**</dt> <dt>104</dt> </dl>                   |         |
| <span id="URL"></span><span id="url"></span><dl> <dt>**URL**</dt> <dt>200</dt> </dl>                                                                                                         |         |
| <span id="FQDN"></span><span id="fqdn"></span><dl> <dt>**FQDN**</dt> <dt>201</dt> </dl>                                                                                                      |         |
| <span id="User_FQDN"></span><span id="user_fqdn"></span><span id="USER_FQDN"></span><dl> <dt>**User FQDN**</dt> <dt>202</dt> </dl>                                                           |         |
| <span id="DER_ASN1_DN"></span><span id="der_asn1_dn"></span><dl> <dt>**DER ASN1 DN**</dt> <dt>203</dt> </dl>                                                                                 |         |
| <span id="DER_ASN1_GN"></span><span id="der_asn1_gn"></span><dl> <dt>**DER ASN1 GN**</dt> <dt>204</dt> </dl>                                                                                 |         |
| <span id="Key_ID"></span><span id="key_id"></span><span id="KEY_ID"></span><dl> <dt>**Key ID**</dt> <dt>205</dt> </dl>                                                                       |         |
| <span id="Parameterized_URL"></span><span id="parameterized_url"></span><span id="PARAMETERIZED_URL"></span><dl> <dt>**Parameterized URL**</dt> <dt>206</dt> </dl>                           |         |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>207 32767</dt> </dl>                                     |         |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 65535</dt> </dl>                           |         |



 

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

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the interface alias of the neighbor.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the interface index of the neighbor.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the network address of the neighbor.

</dd> <dt>

**LinkLayerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets the link layer address of the neighbor.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (256), [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

Uniquely identifies the service access point (SAP) and provides an indication of the functionality that is managed. This functionality is described in more detail in the Description property of the object.

This property is inherited from [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md).

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

**OtherAccessContext**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_RemoteServiceAccessPoint.AccessContext")
</dt> </dl>

When the AccessContext property contains a value of 1, "Other" then this is a free form string providing more information about the role of RemoteServiceAccessPoint in the hosting system.

This property is inherited from [**CIM\_RemoteServiceAccessPoint**](cim-remoteserviceaccesspoint.md).

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

**OtherInfoFormatDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_RemoteServiceAccessPoint.InfoFormat")
</dt> </dl>

Describes the format when the property InfoFormat is set to 1 (Other).

This property is inherited from [**CIM\_RemoteServiceAccessPoint**](cim-remoteserviceaccesspoint.md).

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

**State**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the discovery state of the neighbor. This property contains one of the following values.



| Value                                                                                                                                                                                                                                       | Meaning        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| <span id="Unreachable"></span><span id="unreachable"></span><span id="UNREACHABLE"></span><dl> <dt>**Unreachable**</dt> <dt>0</dt> </dl> |                |
| <span id="Incomplete"></span><span id="incomplete"></span><span id="INCOMPLETE"></span><dl> <dt>**Incomplete**</dt> <dt>1</dt> </dl>     |                |
| <span id="Probe"></span><span id="probe"></span><span id="PROBE"></span><dl> <dt>**Probe**</dt> <dt>2</dt> </dl>                         |                |
| <span id="Delay"></span><span id="delay"></span><span id="DELAY"></span><dl> <dt>**Delay**</dt> <dt>3</dt> </dl>                         |                |
| <span id="Stale"></span><span id="stale"></span><span id="STALE"></span><dl> <dt>**Stale**</dt> <dt>4</dt> </dl>                         |                |
| <span id="Reachable"></span><span id="reachable"></span><span id="REACHABLE"></span><dl> <dt>**Reachable**</dt> <dt>5</dt> </dl>         |                |
| <span id="Permanent"></span><span id="permanent"></span><span id="PERMANENT"></span><dl> <dt>**Permanent**</dt> <dt>6</dt> </dl>         |                |
| <dl> <dt></dt> <dt>7</dt> </dl>                                                                                                          | TBD<br/> |



 

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

**Store**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the interface store of the neighbor persists after a reboot. This property contains one of the following values.



| Value                                                                                                                                                                                                                                   | Meaning                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <span id="Persistent"></span><span id="persistent"></span><span id="PERSISTENT"></span><dl> <dt>**Persistent**</dt> <dt>0</dt> </dl> | The interface store persists after a reboot.<br/>         |
| <span id="Active"></span><span id="active"></span><span id="ACTIVE"></span><dl> <dt>**Active**</dt> <dt>1</dt> </dl>                 | The interface store does not persist after a reboot.<br/> |



 

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

The date or time when the enabled state of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

This property is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).

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



## See also

<dl> <dt>

[**CIM\_RemoteServiceAccessPoint**](cim-remoteserviceaccesspoint.md)
</dt> <dt>

[NetTCPIP Provider Classes](net-tcpip-classes.md)
</dt> </dl>

 

