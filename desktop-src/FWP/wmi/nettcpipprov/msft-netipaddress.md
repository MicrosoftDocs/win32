---
description: The representation of IPv4 address and IPv6 address.
ms.assetid: 5c4657fd-9cf6-4538-90ee-5aaa881e945b
title: MSFT\_NetIPAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPAddress
- MSFT_NetIPAddress.InstanceID
- MSFT_NetIPAddress.Caption
- MSFT_NetIPAddress.ElementName
- MSFT_NetIPAddress.InstallDate
- MSFT_NetIPAddress.StatusDescriptions
- MSFT_NetIPAddress.Status
- MSFT_NetIPAddress.HealthState
- MSFT_NetIPAddress.CommunicationStatus
- MSFT_NetIPAddress.DetailedStatus
- MSFT_NetIPAddress.OperatingStatus
- MSFT_NetIPAddress.PrimaryStatus
- MSFT_NetIPAddress.OtherEnabledState
- MSFT_NetIPAddress.RequestedState
- MSFT_NetIPAddress.EnabledDefault
- MSFT_NetIPAddress.TransitioningToState
- MSFT_NetIPAddress.AvailableRequestedStates
- MSFT_NetIPAddress.SystemCreationClassName
- MSFT_NetIPAddress.SystemName
- MSFT_NetIPAddress.CreationClassName
- MSFT_NetIPAddress.Description
- MSFT_NetIPAddress.Name
- MSFT_NetIPAddress.OperationalStatus
- MSFT_NetIPAddress.EnabledState
- MSFT_NetIPAddress.TimeOfLastStateChange
- MSFT_NetIPAddress.NameFormat
- MSFT_NetIPAddress.ProtocolType
- MSFT_NetIPAddress.OtherTypeDescription
- MSFT_NetIPAddress.ProtocolIFType
- MSFT_NetIPAddress.IPv4Address
- MSFT_NetIPAddress.IPv6Address
- MSFT_NetIPAddress.Address
- MSFT_NetIPAddress.SubnetMask
- MSFT_NetIPAddress.PrefixLength
- MSFT_NetIPAddress.AddressType
- MSFT_NetIPAddress.IPVersionSupport
- MSFT_NetIPAddress.AddressOrigin
- MSFT_NetIPAddress.InterfaceIndex
- MSFT_NetIPAddress.InterfaceAlias
- MSFT_NetIPAddress.IPAddress
- MSFT_NetIPAddress.AddressFamily
- MSFT_NetIPAddress.Type
- MSFT_NetIPAddress.Store
- MSFT_NetIPAddress.PrefixOrigin
- MSFT_NetIPAddress.SuffixOrigin
- MSFT_NetIPAddress.AddressState
- MSFT_NetIPAddress.ValidLifetime
- MSFT_NetIPAddress.PreferredLifetime
- MSFT_NetIPAddress.SkipAsSource
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPAddress class

The representation of IPv4 address and IPv6 address.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::ProtocolEndpoints"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetIPAddress : CIM_IPProtocolEndpoint
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
  string   OtherTypeDescription;
  uint16   ProtocolIFType = 4096;
  string   IPv4Address;
  string   IPv6Address;
  string   Address;
  string   SubnetMask;
  uint8    PrefixLength;
  uint16   AddressType;
  uint16   IPVersionSupport;
  uint16   AddressOrigin = 0;
  uint32   InterfaceIndex;
  string   InterfaceAlias;
  string   IPAddress;
  uint16   AddressFamily;
  uint8    Type;
  uint8    Store;
  uint16   PrefixOrigin;
  uint16   SuffixOrigin;
  uint16   AddressState;
  datetime ValidLifetime;
  datetime PreferredLifetime;
  boolean  SkipAsSource;
};
```

## Members

The **MSFT\_NetIPAddress** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetIPAddress** class has these methods.



| Method                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Create**](create-msft-netipaddress.md)                         | Creates the IP address.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**RequestStateChange**](msft-netipaddress-requeststatechange.md) | Requests that the state of the element be changed to the value specified in the *RequestedState* parameter. When the requested state change takes place, the enabled state and requested state of the element will be the same. Invoking the **RequestChangeState** method multiple times could result in earlier requests being overwritten or lost. If 0 is returned, then the task completed successfully and the use of [**CIM\_ConcreteJob**](cim-concretejob.md) was not required. If 4096 (0x1000) is returned, then the task will take some time to complete, **CIM\_ConcreteJob** will be created, and its reference returned in the output parameter *Job*. Any other return code indicates an error condition.<br/> This method is inherited from [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).<br/> |



 

### Properties

The **MSFT\_NetIPAddress** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/win32/wmisdk/standard-wmi-qualifiers) ("CIM\_IPProtocolEndpoint.IPv4Address", "CIM\_IPProtocolEndpoint.IPv6Address")
</dt> </dl>

The IP address that this protocol endpoint represents, formatted according to the appropriate convention as defined in the **AddressType** property of this class (e.g., 171.79.6.40). This single property is deprecated to replace it by specific IPv4 and v6 addresses.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

</dd> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the address family for this IP address is v4 or v6.



| Value                                                                                                                                                                                                            | Meaning                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span><dl> <dt>**IPv4**</dt> <dt>2</dt> </dl>  | The address family is IPv4<br/> |
| <span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span><dl> <dt>**IPv6**</dt> <dt>23</dt> </dl> | The address family is IPv6<br/> |



 

</dd> <dt>

**AddressOrigin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).



| Value                                                                                                                                                                                                                                                                 | Meaning                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                           |                                                                                                                   |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                   |                                                                                                                   |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>2</dt> </dl>               |                                                                                                                   |
| <span id="Static"></span><span id="static"></span><span id="STATIC"></span><dl> <dt>**Static**</dt> <dt>3</dt> </dl>                                               | The values were assigned manually. <br/>                                                                    |
| <span id="DHCP"></span><span id="dhcp"></span><dl> <dt>**DHCP**</dt> <dt>4</dt> </dl>                                                                              | The values were assigned utilizing the Dynamic Host Configuration Protocol. See RFC 2131 and related. <br/> |
| <span id="BOOTP"></span><span id="bootp"></span><dl> <dt>**BOOTP**</dt> <dt>5</dt> </dl>                                                                           | The values were assigned utilizing BOOTP. See RFC 951 and related. <br/>                                    |
| <span id="IPv4_Link_Local"></span><span id="ipv4_link_local"></span><span id="IPV4_LINK_LOCAL"></span><dl> <dt>**IPv4 Link Local**</dt> <dt>6</dt> </dl>           | The values were assigned using the IPv4 Link Local protocol. See RFC 3927.<br/>                             |
| <span id="DHCPv6"></span><span id="dhcpv6"></span><span id="DHCPV6"></span><dl> <dt>**DHCPv6**</dt> <dt>7</dt> </dl>                                               | The values were assigned using DHCPv6. See RFC 3315. <br/>                                                  |
| <span id="IPv6AutoConfig"></span><span id="ipv6autoconfig"></span><span id="IPV6AUTOCONFIG"></span><dl> <dt>**IPv6AutoConfig**</dt> <dt>8</dt> </dl>               | The values were assigned using the IPv6 AutoConfig Protocol. See RFC 4862.<br/>                             |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>9 32767</dt> </dl>             |                                                                                                                   |
| <span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span><dl> <dt>**Vendor Reserved**</dt> <dt>32768 65535</dt> </dl> |                                                                                                                   |



 

</dd> <dt>

**AddressState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address lifetime state.

<dl> <dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>**Invalid** (0)
</dt> <dt>

<span id="Tentative"></span><span id="tentative"></span><span id="TENTATIVE"></span>**Tentative** (1)
</dt> <dt>

<span id="Duplicate"></span><span id="duplicate"></span><span id="DUPLICATE"></span>**Duplicate** (2)
</dt> <dt>

<span id="Deprecated"></span><span id="deprecated"></span><span id="DEPRECATED"></span>**Deprecated** (3)
</dt> <dt>

<span id="Preferred"></span><span id="preferred"></span><span id="PREFERRED"></span>**Preferred** (4)
</dt> </dl>

</dd> <dt>

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/win32/wmisdk/standard-wmi-qualifiers) ("No value")
</dt> </dl>

An enumeration that describes the format of the Address property. It is deprecated since it is not needed, as the class contains both IPv4 and v6 addresses).

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (1)
</dt> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (2)
</dt> </dl>

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

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly interface name.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly interface index.

</dd> <dt>

**IPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address.

</dd> <dt>

**IPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPv4 address that this ProtocolEndpoint represents.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

</dd> <dt>

**IPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPv6 address that this ProtocolEndpoint represents.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

</dd> <dt>

**IPVersionSupport**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/win32/wmisdk/standard-wmi-qualifiers) ("CIM\_ProtocolEndpoint.ProtocolIFType")
</dt> </dl>

This property explicitly defines support for different versions of the IP protocol, for this Endpoint. It is deprecated since the ProtocolIFType also provides this functionality by describing an endpoint as IPv4 only (value=4096), IPv6 only (value=4097), or IPv4/v6 (value=4098).

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="IPv4_Only"></span><span id="ipv4_only"></span><span id="IPV4_ONLY"></span>**IPv4 Only** (1)
</dt> <dt>

<span id="IPv6_Only"></span><span id="ipv6_only"></span><span id="IPV6_ONLY"></span>**IPv6 Only** (2)
</dt> <dt>

<span id="Both_IPv4_and_IPv6"></span><span id="both_ipv4_and_ipv6"></span><span id="BOTH_IPV4_AND_IPV6"></span>**Both IPv4 and IPv6** (3)
</dt> </dl>

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

**PreferredLifetime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime over which the address is preferred. The default value is infinite.

</dd> <dt>

**PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The prefix length for the IPv6 address of this Protocol Endpoint, if one is defined.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

</dd> <dt>

**PrefixOrigin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Prefix origin of this address.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (0)
</dt> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>**Manual** (1)
</dt> <dt>

<span id="WellKnown"></span><span id="wellknown"></span><span id="WELLKNOWN"></span>**WellKnown** (2)
</dt> <dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>**Dhcp** (3)
</dt> <dt>

<span id="RouterAdvertisement"></span><span id="routeradvertisement"></span><span id="ROUTERADVERTISEMENT"></span>**RouterAdvertisement** (4)
</dt> </dl>

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

ProtocolIFType's enumeration is limited to IP-related and reserved values for this subclass of ProtocolEndpoint.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="IANA_Reserved"></span><span id="iana_reserved"></span><span id="IANA_RESERVED"></span>**IANA Reserved** (225 4095)
</dt> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (4096)
</dt> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (4097)
</dt> <dt>

<span id="IPv4_v6"></span><span id="ipv4_v6"></span><span id="IPV4_V6"></span>**IPv4/v6** (4098)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (4301 32767)
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

**SkipAsSource**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

true to not use the address as source address for any outgoing packet unless explicitly asked to.

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

Describes if the set is active or persistent.



| Value                                                                                                                                                                                                                                   | Meaning                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="Persistent"></span><span id="persistent"></span><span id="PERSISTENT"></span><dl> <dt>**Persistent**</dt> <dt>0</dt> </dl> | Set is persistent (default).<br/>     |
| <span id="Active"></span><span id="active"></span><span id="ACTIVE"></span><dl> <dt>**Active**</dt> <dt>1</dt> </dl>                 | Set only lasts until next boot. <br/> |



 

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The mask for the IPv4 address of this protocol endpoint, if one is defined.

This property is inherited from [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md).

</dd> <dt>

**SuffixOrigin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Suffix origin of this address.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (0)
</dt> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>**Manual** (1)
</dt> <dt>

<span id="WellKnown"></span><span id="wellknown"></span><span id="WELLKNOWN"></span>**WellKnown** (2)
</dt> <dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>**Dhcp** (3)
</dt> <dt>

<span id="Link"></span><span id="link"></span><span id="LINK"></span>**Link** (4)
</dt> <dt>

<span id="Random"></span><span id="random"></span><span id="RANDOM"></span>**Random** (5)
</dt> </dl>

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

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of address.



| Value                                                                                                                                                                                                                       | Meaning                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="Unicast"></span><span id="unicast"></span><span id="UNICAST"></span><dl> <dt>**Unicast**</dt> <dt>1</dt> </dl> | Marks the address as a unicast address. This is the default<br/> |
| <span id="Anycast"></span><span id="anycast"></span><span id="ANYCAST"></span><dl> <dt>**Anycast**</dt> <dt>2</dt> </dl> | Marks the address as an anycast address<br/>                     |



 

</dd> <dt>

**ValidLifetime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime over which the address is valid. The default value is infinite.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



 

