---
description: A MainMode SA.
ms.assetid: 90b7771a-2460-40cf-802a-7dade1deabe7
title: MSFT\_NetMainModeSA class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetMainModeSA
- MSFT_NetMainModeSA.KeyModule
- MSFT_NetMainModeSA.LocalEndpoint
- MSFT_NetMainModeSA.RemoteEndpoint
- MSFT_NetMainModeSA.MaxQMSAs
- MSFT_NetMainModeSA.LocalFirstId
- MSFT_NetMainModeSA.LocalSecondId
- MSFT_NetMainModeSA.RemoteFirstId
- MSFT_NetMainModeSA.RemoteSecondId
- MSFT_NetMainModeSA.OtherGroupId
- MSFT_NetMainModeSA.ExtendedFilterId
- MSFT_NetMainModeSA.LocalUdpEncapsulationPort
- MSFT_NetMainModeSA.RemoteUdpEncapsulationPort
- MSFT_NetMainModeSA.IkePolicyKey
- MSFT_NetMainModeSA.VirtualIfTunnelId
- MSFT_NetMainModeSA.AuthenticationMethod
- MSFT_NetMainModeSA.CipherAlgorithm
- MSFT_NetMainModeSA.GroupId
- MSFT_NetMainModeSA.HashAlgorithm
- MSFT_NetMainModeSA.InitiatorCookie
- MSFT_NetMainModeSA.OtherAuthenticationMethod
- MSFT_NetMainModeSA.OtherCipherAlgorithm
- MSFT_NetMainModeSA.OtherHashAlgorithm
- MSFT_NetMainModeSA.ResponderCookie
- MSFT_NetMainModeSA.VendorID
- MSFT_NetMainModeSA.IdleDurationSeconds
- MSFT_NetMainModeSA.LifetimeKilobytes
- MSFT_NetMainModeSA.LifetimeSeconds
- MSFT_NetMainModeSA.PacketLoggingActive
- MSFT_NetMainModeSA.RefreshThresholdSecondsPercentage
- MSFT_NetMainModeSA.RefreshThresholdKbytesPercentage
- MSFT_NetMainModeSA.NameFormat
- MSFT_NetMainModeSA.OtherTypeDescription
- MSFT_NetMainModeSA.ProtocolIFType
- MSFT_NetMainModeSA.ProtocolType
- MSFT_NetMainModeSA.SystemCreationClassName
- MSFT_NetMainModeSA.SystemName
- MSFT_NetMainModeSA.CreationClassName
- MSFT_NetMainModeSA.Name
- MSFT_NetMainModeSA.AvailableRequestedStates
- MSFT_NetMainModeSA.EnabledDefault
- MSFT_NetMainModeSA.EnabledState
- MSFT_NetMainModeSA.OtherEnabledState
- MSFT_NetMainModeSA.RequestedState
- MSFT_NetMainModeSA.TimeOfLastStateChange
- MSFT_NetMainModeSA.TransitioningToState
- MSFT_NetMainModeSA.InstallDate
- MSFT_NetMainModeSA.OperationalStatus
- MSFT_NetMainModeSA.StatusDescriptions
- MSFT_NetMainModeSA.Status
- MSFT_NetMainModeSA.HealthState
- MSFT_NetMainModeSA.CommunicationStatus
- MSFT_NetMainModeSA.DetailedStatus
- MSFT_NetMainModeSA.OperatingStatus
- MSFT_NetMainModeSA.PrimaryStatus
- MSFT_NetMainModeSA.InstanceID
- MSFT_NetMainModeSA.Caption
- MSFT_NetMainModeSA.Description
- MSFT_NetMainModeSA.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetMainModeSA class

A MainMode SA.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetMainModeSA : CIM_IKESAEndpoint
{
  uint16   KeyModule;
  string   LocalEndpoint;
  string   RemoteEndpoint;
  uint32   MaxQMSAs;
  string   LocalFirstId;
  string   LocalSecondId;
  string   RemoteFirstId;
  string   RemoteSecondId;
  string   OtherGroupId;
  uint64   ExtendedFilterId;
  uint16   LocalUdpEncapsulationPort;
  uint16   RemoteUdpEncapsulationPort;
  string   IkePolicyKey;
  uint64   VirtualIfTunnelId;
  uint16   AuthenticationMethod;
  uint16   CipherAlgorithm;
  uint16   GroupId;
  uint16   HashAlgorithm;
  uint64   InitiatorCookie;
  string   OtherAuthenticationMethod;
  string   OtherCipherAlgorithm;
  string   OtherHashAlgorithm;
  uint64   ResponderCookie;
  string   VendorID;
  uint64   IdleDurationSeconds;
  uint64   LifetimeKilobytes;
  uint64   LifetimeSeconds;
  boolean  PacketLoggingActive;
  uint8    RefreshThresholdSecondsPercentage;
  uint8    RefreshThresholdKbytesPercentage;
  string   NameFormat;
  string   OtherTypeDescription;
  uint16   ProtocolIFType;
  uint16   ProtocolType;
  string   SystemCreationClassName;
  string   SystemName;
  string   CreationClassName;
  string   Name;
  uint16   AvailableRequestedStates[];
  uint16   EnabledDefault;
  uint16   EnabledState;
  string   OtherEnabledState;
  uint16   RequestedState;
  datetime TimeOfLastStateChange;
  uint16   TransitioningToState;
  datetime InstallDate;
  uint16   OperationalStatus[];
  string   StatusDescriptions[];
  string   Status;
  uint16   HealthState;
  uint16   CommunicationStatus;
  uint16   DetailedStatus;
  uint16   OperatingStatus;
  uint16   PrimaryStatus;
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
};
```

## Members

The **MSFT\_NetMainModeSA** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetMainModeSA** class has these properties.

<dl> <dt>

**AuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**AvailableRequestedStates**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used in CimInstance.ToString(). A short string for describing this instance when debugging.

</dd> <dt>

**CipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The actual encryption algorithm used by the SA.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="DES"></span><span id="des"></span>**DES** (2)
</dt> <dt>

<span id="3DES"></span><span id="3des"></span>**3DES** (6)
</dt> <dt>

<span id="AES-128"></span><span id="aes-128"></span>**AES-128** (65001)
</dt> <dt>

<span id="AES-192"></span><span id="aes-192"></span>**AES-192** (65002)
</dt> <dt>

<span id="AES-256"></span><span id="aes-256"></span>**AES-256** (65003)
</dt> <dt>

<span id="AES-GCM-128"></span><span id="aes-gcm-128"></span>**AES-GCM-128** (65004)
</dt> <dt>

<span id="AES-GCM-192"></span><span id="aes-gcm-192"></span>**AES-GCM-192** (65005)
</dt> <dt>

<span id="AES-GCM-256_"></span><span id="aes-gcm-256_"></span>**AES-GCM-256** (65006 )
</dt> </dl>

</dd> <dt>

**CommunicationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**DetailedStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**EnabledDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ExtendedFilterId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Filter ID from the QM policy matching the extended mode filter

</dd> <dt>

**GroupId**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The property GroupId gives the phase 1 security association key exchange group. Well-known group identifiers from RFC2412, Appendix E, are: Group 1='768 bit prime', Group 2='1024 bit prime', Group 3 ='Elliptic Curve Group with 155 bit field element', Group 4= 'Large Elliptic Curve Group with 185 bit field element', and Group 5='1536 bit prime'. Note that only groups 1, 2, 14, 19, 20, and 24 are acceptable in Windows 8.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="DH_Group_1"></span><span id="dh_group_1"></span><span id="DH_GROUP_1"></span>**DH Group 1** (1)
</dt> <dt>

<span id="DH_Group_2"></span><span id="dh_group_2"></span><span id="DH_GROUP_2"></span>**DH Group 2** (2)
</dt> <dt>

<span id="DH_Group_14"></span><span id="dh_group_14"></span><span id="DH_GROUP_14"></span>**DH Group 14** (14)
</dt> <dt>

<span id="DH_Group_19"></span><span id="dh_group_19"></span><span id="DH_GROUP_19"></span>**DH Group 19** (19)
</dt> <dt>

<span id="DH_Group_20"></span><span id="dh_group_20"></span><span id="DH_GROUP_20"></span>**DH Group 20** (20)
</dt> <dt>

<span id="DH_Group_24_"></span><span id="dh_group_24_"></span><span id="DH_GROUP_24_"></span>**DH Group 24** (24 )
</dt> </dl>

</dd> <dt>

**HashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The actual hash algorithm used by the SA.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="MD5"></span><span id="md5"></span>**MD5** (2)
</dt> <dt>

<span id="SHA-1"></span><span id="sha-1"></span>**SHA-1** (3)
</dt> <dt>

<span id="SHA-256"></span><span id="sha-256"></span>**SHA-256** (65001)
</dt> <dt>

<span id="SHA-384"></span><span id="sha-384"></span>**SHA-384** (65002)
</dt> <dt>

<span id="AES-GMAC-128"></span><span id="aes-gmac-128"></span>**AES-GMAC-128** (65003)
</dt> <dt>

<span id="AES-GMAC-192"></span><span id="aes-gmac-192"></span>**AES-GMAC-192** (65004)
</dt> <dt>

<span id="AES-GMAC-256_"></span><span id="aes-gmac-256_"></span>**AES-GMAC-256** (65005 )
</dt> </dl>

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**IdleDurationSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**IkePolicyKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the main mode policy provider context corresponding to this SA

</dd> <dt>

**InitiatorCookie**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies this instance within the PolicyStore.

</dd> <dt>

**KeyModule**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Key Module used to negotiate the SA and its child SA's.

</dd> <dt>

**LifetimeKilobytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**LifetimeSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**LocalEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the local endpoint the SA applies to.

</dd> <dt>

**LocalFirstId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first authentication local identity

</dd> <dt>

**LocalSecondId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The second authentication local identity

</dd> <dt>

**LocalUdpEncapsulationPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Local UDP encapsulation port for NAT-T

</dd> <dt>

**MaxQMSAs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of Quick Mode SA's that may be established with this SA before it must be renegotiated.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OperatingStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherAuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherCipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherEnabledState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherGroupId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Extensions to GroupId

</dd> <dt>

**OtherHashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PacketLoggingActive**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**PrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ProtocolType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**RefreshThresholdKbytesPercentage**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MinValue** (0), **MaxValue** (100), **Override** ("RefreshThresholdKbytesPercentage")
</dt> </dl>

This property is ignored.

</dd> <dt>

**RefreshThresholdSecondsPercentage**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **MinValue** (0), **MaxValue** (100), **Override** ("RefreshThresholdSecondsPercentage")
</dt> </dl>

This property is ignored.

</dd> <dt>

**RemoteEndpoint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the remote endpoint the SA applies to.

</dd> <dt>

**RemoteFirstId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first authentication remote identity

</dd> <dt>

**RemoteSecondId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The second authentication remote identity

</dd> <dt>

**RemoteUdpEncapsulationPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote UDP encapsulation port for NAT-T

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ResponderCookie**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**StatusDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**TimeOfLastStateChange**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**VendorID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**VirtualIfTunnelId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID/Handle to virtual interface tunneling state

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




