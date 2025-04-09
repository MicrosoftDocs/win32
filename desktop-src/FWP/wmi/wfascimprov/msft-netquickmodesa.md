---
description: A Quick Mode SA.
ms.assetid: f85e0547-79d9-4c4a-970d-f0b37453dcb6
title: MSFT\_NetQuickModeSA class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetQuickModeSA
- MSFT_NetQuickModeSA.LocalEndpoint
- MSFT_NetQuickModeSA.RemoteEndpoint
- MSFT_NetQuickModeSA.LocalPort
- MSFT_NetQuickModeSA.RemotePort
- MSFT_NetQuickModeSA.TrafficLuid
- MSFT_NetQuickModeSA.IpProtocol
- MSFT_NetQuickModeSA.InterfaceAlias
- MSFT_NetQuickModeSA.RealIfProfileId
- MSFT_NetQuickModeSA.LocalUdpEncapsulationPort
- MSFT_NetQuickModeSA.RemoteUdpEncapsulationPort
- MSFT_NetQuickModeSA.Flags
- MSFT_NetQuickModeSA.TransportLayerFilterName
- MSFT_NetQuickModeSA.MmSaId
- MSFT_NetQuickModeSA.FirstTransformType
- MSFT_NetQuickModeSA.FirstIntegrityAlgorithm
- MSFT_NetQuickModeSA.FirstCipherAlgorithm
- MSFT_NetQuickModeSA.SecondTransformType
- MSFT_NetQuickModeSA.SecondIntegrityAlgorithm
- MSFT_NetQuickModeSA.SecondCipherAlgorithm
- MSFT_NetQuickModeSA.SecondSPI
- MSFT_NetQuickModeSA.PeerV4PrivateAddress
- MSFT_NetQuickModeSA.PfsGroupId
- MSFT_NetQuickModeSA.QuickModeFilterId
- MSFT_NetQuickModeSA.LifetimePackets
- MSFT_NetQuickModeSA.NdAllowClearTimeoutSeconds
- MSFT_NetQuickModeSA.NapContext
- MSFT_NetQuickModeSA.QmSaId
- MSFT_NetQuickModeSA.VirtualIfTunnelId
- MSFT_NetQuickModeSA.TrafficSelectorId
- MSFT_NetQuickModeSA.MmTargetName
- MSFT_NetQuickModeSA.EmTargetName
- MSFT_NetQuickModeSA.ExplicitCredentials
- MSFT_NetQuickModeSA.DFHandling
- MSFT_NetQuickModeSA.EncapsulationMode
- MSFT_NetQuickModeSA.InboundDirection
- MSFT_NetQuickModeSA.PFSInUse
- MSFT_NetQuickModeSA.SPI
- MSFT_NetQuickModeSA.IdleDurationSeconds
- MSFT_NetQuickModeSA.LifetimeKilobytes
- MSFT_NetQuickModeSA.LifetimeSeconds
- MSFT_NetQuickModeSA.PacketLoggingActive
- MSFT_NetQuickModeSA.RefreshThresholdSecondsPercentage
- MSFT_NetQuickModeSA.RefreshThresholdKbytesPercentage
- MSFT_NetQuickModeSA.NameFormat
- MSFT_NetQuickModeSA.OtherTypeDescription
- MSFT_NetQuickModeSA.ProtocolIFType
- MSFT_NetQuickModeSA.ProtocolType
- MSFT_NetQuickModeSA.SystemCreationClassName
- MSFT_NetQuickModeSA.SystemName
- MSFT_NetQuickModeSA.CreationClassName
- MSFT_NetQuickModeSA.Name
- MSFT_NetQuickModeSA.AvailableRequestedStates
- MSFT_NetQuickModeSA.EnabledDefault
- MSFT_NetQuickModeSA.EnabledState
- MSFT_NetQuickModeSA.OtherEnabledState
- MSFT_NetQuickModeSA.RequestedState
- MSFT_NetQuickModeSA.TimeOfLastStateChange
- MSFT_NetQuickModeSA.TransitioningToState
- MSFT_NetQuickModeSA.InstallDate
- MSFT_NetQuickModeSA.OperationalStatus
- MSFT_NetQuickModeSA.StatusDescriptions
- MSFT_NetQuickModeSA.Status
- MSFT_NetQuickModeSA.HealthState
- MSFT_NetQuickModeSA.CommunicationStatus
- MSFT_NetQuickModeSA.DetailedStatus
- MSFT_NetQuickModeSA.OperatingStatus
- MSFT_NetQuickModeSA.PrimaryStatus
- MSFT_NetQuickModeSA.InstanceID
- MSFT_NetQuickModeSA.Caption
- MSFT_NetQuickModeSA.Description
- MSFT_NetQuickModeSA.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetQuickModeSA class

A Quick Mode SA.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetQuickModeSA : CIM_IPsecSAEndpoint
{
  string   LocalEndpoint;
  string   RemoteEndpoint;
  uint16   LocalPort;
  uint16   RemotePort;
  uint64   TrafficLuid;
  UINT8    IpProtocol;
  string   InterfaceAlias;
  uint64   RealIfProfileId;
  uint16   LocalUdpEncapsulationPort;
  uint16   RemoteUdpEncapsulationPort;
  uint32   Flags;
  string   TransportLayerFilterName;
  uint64   MmSaId;
  uint32   FirstTransformType;
  uint32   FirstIntegrityAlgorithm;
  uint32   FirstCipherAlgorithm;
  uint32   SecondTransformType;
  uint32   SecondIntegrityAlgorithm;
  uint32   SecondCipherAlgorithm;
  uint32   SecondSPI;
  string   PeerV4PrivateAddress;
  uint32   PfsGroupId;
  uint64   QuickModeFilterId;
  uint64   LifetimePackets;
  uint32   NdAllowClearTimeoutSeconds;
  uint32   NapContext;
  uint32   QmSaId;
  uint64   VirtualIfTunnelId;
  uint64   TrafficSelectorId;
  string   MmTargetName;
  string   EmTargetName;
  uint64   ExplicitCredentials;
  uint16   DFHandling;
  uint16   EncapsulationMode;
  boolean  InboundDirection;
  boolean  PFSInUse;
  uint32   SPI;
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

The **MSFT\_NetQuickModeSA** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetQuickModeSA** class has these properties.

<dl> <dt>

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

**DFHandling**
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

**EmTargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Extended Mode target SPN

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

**EncapsulationMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ExplicitCredentials**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Optional handle to explicit credentials

</dd> <dt>

**FirstCipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cipher algorithm for the first operation

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

**FirstIntegrityAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The integrity algorithm for the first operation

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="MD5"></span><span id="md5"></span>**MD5** (2)
</dt> <dt>

<span id="SHA-1"></span><span id="sha-1"></span>**SHA-1** (3)
</dt> <dt>

<span id="SHA-256"></span><span id="sha-256"></span>**SHA-256** (65001)
</dt> <dt>

<span id="AES-GMAC-128"></span><span id="aes-gmac-128"></span>**AES-GMAC-128** (65003)
</dt> <dt>

<span id="AES-GMAC-192"></span><span id="aes-gmac-192"></span>**AES-GMAC-192** (65004)
</dt> <dt>

<span id="AES-GMAC-256_"></span><span id="aes-gmac-256_"></span>**AES-GMAC-256** (65005 )
</dt> </dl>

</dd> <dt>

**FirstTransformType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

First Transform type

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SA Flags

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

**InboundDirection**
</dt> <dd> <dl> <dt>

Data type: **boolean**
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

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Local interface alias

</dd> <dt>

**IpProtocol**
</dt> <dd> <dl> <dt>

Data type: **UINT8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP protocol for this traffic. Only specified if the traffic is more general than the matching filter

</dd> <dt>

**LifetimeKilobytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**LifetimePackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Liftime by number of packets

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

**LocalPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The local machine port the SA applies to, or 0 for all ports.

</dd> <dt>

**LocalUdpEncapsulationPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Local Udp encapsulation port for NAT traversal

</dd> <dt>

**MmSaId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Id of the associated Main Mode

</dd> <dt>

**MmTargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Main Mode target SPN

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

**NapContext**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Network Access Protection context

</dd> <dt>

**NdAllowClearTimeoutSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timeout after which the IPsec SA should stop accepting packets coming in the clear in negotiation discovery mode

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

**OtherEnabledState**
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

**PeerV4PrivateAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Private address of peer behind NAT

</dd> <dt>

**PfsGroupId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Perfect forward secrecy group id

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

<span id="DH_Group_24"></span><span id="dh_group_24"></span><span id="DH_GROUP_24"></span>**DH Group 24** (24)
</dt> <dt>

<span id="Same_as_Main_Mode_"></span><span id="same_as_main_mode_"></span><span id="SAME_AS_MAIN_MODE_"></span>**Same as Main Mode** (65535 )
</dt> </dl>

</dd> <dt>

**PFSInUse**
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

**QmSaId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier for tiebraking simultaneous SAs

</dd> <dt>

**QuickModeFilterId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

LUID of the FWPS\_LAYER\_IPSEC\_XX layer FWPS filter corresponding to this SA

</dd> <dt>

**RealIfProfileId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The profile ID corresponding to the actual interface that the traffic is going out on or coming in from the wire.

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

**RemotePort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The remote machine port the SA applies to, or 0 for all ports.

</dd> <dt>

**RemoteUdpEncapsulationPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote Udp encapsulation port for NAT traversal

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**SecondCipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cipher algorithm for the second operation

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

**SecondIntegrityAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The integrity algorithm for the second operation

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="MD5"></span><span id="md5"></span>**MD5** (2)
</dt> <dt>

<span id="SHA-1"></span><span id="sha-1"></span>**SHA-1** (3)
</dt> <dt>

<span id="SHA-256"></span><span id="sha-256"></span>**SHA-256** (65001)
</dt> <dt>

<span id="AES-GMAC-128"></span><span id="aes-gmac-128"></span>**AES-GMAC-128** (65003)
</dt> <dt>

<span id="AES-GMAC-192"></span><span id="aes-gmac-192"></span>**AES-GMAC-192** (65004)
</dt> <dt>

<span id="AES-GMAC-256_"></span><span id="aes-gmac-256_"></span>**AES-GMAC-256** (65005 )
</dt> </dl>

</dd> <dt>

**SecondSPI**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The spi for the first operation

</dd> <dt>

**SecondTransformType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Second Transform type

</dd> <dt>

**SPI**
</dt> <dd> <dl> <dt>

Data type: **uint32**
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

**TrafficLuid**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If traffic type is transport mode, this is the LUID of the FWPS transport layer filter corresponding to this traffic. If traffic type is tunnel mode, this is the LUID of the associated QM policy. In tunnel mode, this represents the QM traffic selectors for the tunnel

</dd> <dt>

**TrafficSelectorId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID/Handle to Virtual-IF traffic selector(s)

</dd> <dt>

**TransitioningToState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**TransportLayerFilterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the matching transport filter

</dd> <dt>

**VirtualIfTunnelId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID/Handle to Virtual-IF tunnel state

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




