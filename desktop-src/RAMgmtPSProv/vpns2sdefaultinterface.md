---
title: VpnS2SDefaultInterface class
description: Represents the S2S VPN default interface.
audience: developer
ms.assetid: '65a70302-91bb-47e3-a23a-19d7aa26bc37'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["VpnS2SDefaultInterface class", "VpnS2SDefaultInterface class, described"]
topic_type:
- apiref
api_name:
- VpnS2SDefaultInterface
- VpnS2SDefaultInterface.Protocol
- VpnS2SDefaultInterface.Destination
- VpnS2SDefaultInterface.AdminStatus
- VpnS2SDefaultInterface.InterfaceType
- VpnS2SDefaultInterface.RetryInterval
- VpnS2SDefaultInterface.SADataSizeForRenegotiation
- VpnS2SDefaultInterface.SALifeTime
- VpnS2SDefaultInterface.IPv6Subnet
- VpnS2SDefaultInterface.IPv4Subnet
- VpnS2SDefaultInterface.Name
- VpnS2SDefaultInterface.UserName
- VpnS2SDefaultInterface.Certificate
- VpnS2SDefaultInterface.NetworkOutageTime
- VpnS2SDefaultInterface.NumberOfTries
- VpnS2SDefaultInterface.PromoteAlternate
- VpnS2SDefaultInterface.AuthenticationMethod
- VpnS2SDefaultInterface.ResponderAuthenticationMethod
- VpnS2SDefaultInterface.EapMethod
- VpnS2SDefaultInterface.InternalIPv4
- VpnS2SDefaultInterface.InternalIPv6
- VpnS2SDefaultInterface.IdleDisconnect
- VpnS2SDefaultInterface.LastError
- VpnS2SDefaultInterface.UnReachabilityReasons
- VpnS2SDefaultInterface.ConnectionState
- VpnS2SDefaultInterface.IPv4TriggerFilter
- VpnS2SDefaultInterface.IPv4TriggerFilterAction
- VpnS2SDefaultInterface.PostConnectionIPv4Subnet
- VpnS2SDefaultInterface.IPv6TriggerFilter
- VpnS2SDefaultInterface.IPv6TriggerFilterAction
- VpnS2SDefaultInterface.PostConnectionIPv6Subnet
- VpnS2SDefaultInterface.Persistent
- VpnS2SDefaultInterface.InitiateConfigPayload
- VpnS2SDefaultInterface.EnableQoS
- VpnS2SDefaultInterface.TxBandwidthKbps
- VpnS2SDefaultInterface.RxBandwidthKbps
- VpnS2SDefaultInterface.SourceIpAddress
- VpnS2SDefaultInterface.MMSALifeTime
- VpnS2SDefaultInterface.LocalVpnTrafficSelector
- VpnS2SDefaultInterface.RemoteVpnTrafficSelector
- VpnS2SDefaultInterface.LastDisconnectReason
- VpnS2SDefaultInterface.EncryptionType
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# VpnS2SDefaultInterface class

Represents the S2S VPN default interface.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnS2SDefaultInterface : VpnS2SInterface
{
  string             Protocol;
  string             Destination[];
  boolean            AdminStatus;
  string             InterfaceType;
  uint32             RetryInterval;
  uint32             SADataSizeForRenegotiation;
  uint32             SALifeTime;
  string             IPv6Subnet[];
  string             IPv4Subnet[];
  string             Name;
  string             UserName;
  uint8              Certificate[];
  uint32             NetworkOutageTime;
  uint32             NumberOfTries;
  boolean            PromoteAlternate;
  string             AuthenticationMethod;
  string             ResponderAuthenticationMethod;
  string             EapMethod;
  boolean            InternalIPv4;
  boolean            InternalIPv6;
  uint32             IdleDisconnect;
  uint32             LastError;
  string             UnReachabilityReasons;
  string             ConnectionState;
  string             IPv4TriggerFilter[];
  uint32             IPv4TriggerFilterAction;
  string             PostConnectionIPv4Subnet[];
  string             IPv6TriggerFilter[];
  uint32             IPv6TriggerFilterAction;
  string             PostConnectionIPv6Subnet[];
  boolean            Persistent;
  boolean            InitiateConfigPayload;
  uint32             EnableQoS;
  uint64             TxBandwidthKbps;
  uint64             RxBandwidthKbps;
  string             SourceIpAddress;
  uint32             MMSALifeTime;
  VpnTrafficSelector LocalVpnTrafficSelector[];
  VpnTrafficSelector RemoteVpnTrafficSelector[];
  uint32             LastDisconnectReason;
  string             EncryptionType;
};
```

## Members

The **VpnS2SDefaultInterface** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnS2SDefaultInterface** class has these properties.

<dl> <dt>

**AdminStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The admin status of the cmdlet.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**AuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The authentication method to be used for the S2S connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>

<span id="EAP"></span><span id="eap"></span>

**EAP** ("EAP")


</dt> <dd></dd> <dt>

<span id="MachineCertificates"></span><span id="machinecertificates"></span><span id="MACHINECERTIFICATES"></span>

**MachineCertificates** ("MachineCertificates")


</dt> <dd></dd> <dt>

<span id="PSKOnly"></span><span id="pskonly"></span><span id="PSKONLY"></span>

**PSKOnly** ("PSKOnly")


</dt> <dd></dd> </dl>

</dd> <dt>

**Certificate**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Subject Name of the certificate to be used in default store; applicable only when the authentication method is "MachineCert".

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**ConnectionState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current state of the interface, for example connected, disconnected, or unreachable.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**Destination**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The destination end-point of the S2S connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**EapMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The EAP method when the **AuthenticationMethod** property is "EAP".

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are:

<dt>

<span id="TLS"></span><span id="tls"></span>

**TLS** ("TLS")


</dt> <dd></dd> <dt>

<span id="PEAP"></span><span id="peap"></span>

**PEAP** ("PEAP")


</dt> <dd></dd> <dt>

<span id="MSCHAPv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>

**MSCHAPv2** ("MSCHAPv2")


</dt> <dd></dd> </dl>

</dd> <dt>

**EnableQoS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether QoS is enabled on the interface.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>



 (0)


</dt> <dd>

Enabled

</dd> <dt>



 (1)


</dt> <dd>

Disabled

</dd> </dl>

**Windows Server 2012:** This property was renamed from **QoS** in Windows Server 2012 R2.

</dd> <dt>

**EncryptionType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the type of encryption.

The possible values are.

<dt>

<span id="NoEncryption"></span><span id="noencryption"></span><span id="NOENCRYPTION"></span>

**NoEncryption** ("NoEncryption")


</dt> <dd></dd> <dt>

<span id="RequireEncryption"></span><span id="requireencryption"></span><span id="REQUIREENCRYPTION"></span>

**RequireEncryption** ("RequireEncryption")


</dt> <dd></dd> <dt>

<span id="OptionalEncryption"></span><span id="optionalencryption"></span><span id="OPTIONALENCRYPTION"></span>

**OptionalEncryption** ("OptionalEncryption")


</dt> <dd></dd> <dt>

<span id="MaximumEncryption"></span><span id="maximumencryption"></span><span id="MAXIMUMENCRYPTION"></span>

**MaximumEncryption** ("MaximumEncryption")


</dt> <dd></dd> </dl>

</dd> <dt>

**IdleDisconnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The duration, in seconds, after which an idle connection is terminated.

Unless the idle time-out is disabled, the entire connection is terminated if the connection is idle for the specified interval.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**InitiateConfigPayload**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to negotiate the configuration with peers; otherwise **false**.

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**InterfaceType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>

<span id="HomeRouter"></span><span id="homerouter"></span><span id="HOMEROUTER"></span>

**HomeRouter** ("HomeRouter")


</dt> <dd></dd> <dt>

<span id="FullRouter"></span><span id="fullrouter"></span><span id="FULLROUTER"></span>

**FullRouter** ("FullRouter")


</dt> <dd></dd> </dl>

</dd> <dt>

**InternalIPv4**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to negotiate the IPv4 address.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**InternalIPv6**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to negotiate the IPv6 address.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**IPv4Subnet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4 subnet that is routed on this connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**IPv4TriggerFilter**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the demand dial filters for the IPv4 Transport.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**IPv4TriggerFilterAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the IPv4 trigger filters initiates the S2S connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>



 (0)


</dt> <dd>

Allow

</dd> <dt>



 (1)


</dt> <dd>

Block

</dd> </dl>

**Windows Server 2012:** The data type of this property was changed from a string in Windows Server 2012 R2.

</dd> <dt>

**IPv6Subnet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 subnet that is routed on this connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**IPv6TriggerFilter**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains the demand dial filters for the IPv6 Transport.

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**IPv6TriggerFilterAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the IPv6 trigger filters initiates the S2S connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>



 (0)


</dt> <dd>

Allow

</dd> <dt>



 (1)


</dt> <dd>

Block

</dd> </dl>

**Windows Server 2012:** The data type of this property was changed from a string in Windows Server 2012 R2.

</dd> <dt>

**LastDisconnectReason**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reason for the last interface disconnect.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**LastError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last error value if the interface fails to connect.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**LocalVpnTrafficSelector**
</dt> <dd> <dl> <dt>

Data type: **[**VpnTrafficSelector**](vpntrafficselector.md)** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnTrafficSelector**](vpntrafficselector.md)")
</dt> </dl>

An array of local [**VpnTrafficSelector**](vpntrafficselector.md) embedded instances to be negotiated.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**MMSALifeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of a main mode security association (SA), after which the MM SA is no longer valid, in seconds.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**NetworkOutageTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum network outage time after which the connection is disconnected.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**NumberOfTries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of times the connection is retried.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**Persistent**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** if the connection is persistent; otherwise **false**.

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**PostConnectionIPv4Subnet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv4 subnet to route

The routes specified by the subnet do not trigger the S2S connection.

**Windows Server 2012:** This property was renamed from **IPv4DontTriggerSubnet** in Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**PostConnectionIPv6Subnet**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IPv6 subnet to route

The routes specified by the subnet do not trigger the S2S connection.

**Windows Server 2012:** This property was renamed from **IPv6DontTriggerSubnet** in Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**PromoteAlternate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether an alternate IP address that connects successfully becomes the primary IP address, and the current primary IP address is moved to the alternate list.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The underlying protocol.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>

<span id="L2TP"></span><span id="l2tp"></span>

**L2TP** ("L2TP")


</dt> <dd></dd> <dt>

<span id="IKEv2"></span><span id="ikev2"></span><span id="IKEV2"></span>

**IKEv2** ("IKEv2")


</dt> <dd></dd> <dt>

<span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span>

**Automatic** ("Automatic")


</dt> <dd></dd> <dt>

<span id="GRE"></span><span id="gre"></span>

**GRE** ("GRE")


</dt> <dd></dd> </dl>

**Windows Server 2012 and Windows Server 2012 R2:** The "GRE" value is not supported before Windows Server 2016.

</dd> <dt>

**RemoteVpnTrafficSelector**
</dt> <dd> <dl> <dt>

Data type: **[**VpnTrafficSelector**](vpntrafficselector.md)** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnTrafficSelector**](vpntrafficselector.md)")
</dt> </dl>

An array of remote [**VpnTrafficSelector**](vpntrafficselector.md) embedded instances to be negotiated.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**ResponderAuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The responder authentication method to be used for the S2S connection.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

The possible values are.

<dt>

<span id="MachineCertificates"></span><span id="machinecertificates"></span><span id="MACHINECERTIFICATES"></span>

**MachineCertificates** ("MachineCertificates")


</dt> <dd></dd> <dt>

<span id="PSKOnly"></span><span id="pskonly"></span><span id="PSKONLY"></span>

**PSKOnly** ("PSKOnly")


</dt> <dd></dd> </dl>

</dd> <dt>

**RetryInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of seconds between retries.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**RxBandwidthKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The incoming bandwidth limit of the interface.

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**SADataSizeForRenegotiation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of kilobytes that can be transferred using a security administration (SA). After the transfer, the SA will be renegotiated.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**SALifeTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime of a security association (SA), in seconds, after which the SA is no longer valid.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**SourceIpAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP address of the interface.

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**TxBandwidthKbps**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The outgoing bandwidth limit of the interface.

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**UnReachabilityReasons**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The reason why the interface was unreachable.

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The username to use for dialing this connection when the authentication method is set to "EAP".

This property is inherited from [**VpnS2SInterface**](vpns2sinterface.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





