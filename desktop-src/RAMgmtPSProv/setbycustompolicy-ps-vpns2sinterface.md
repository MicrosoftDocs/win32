---
title: SetByCustomPolicy method of the PS\_VpnS2SInterface class
description: Modifies parameters in a S2S Interface. If the interface is already connected, the changes take effect after disconnection.
audience: developer
ms.assetid: 'f8db5281-03f8-46b5-a6da-4f490552908c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByCustomPolicy method", "SetByCustomPolicy method, PS_VpnS2SInterface class", "PS_VpnS2SInterface class, SetByCustomPolicy method"]
topic_type:
- apiref
api_name:
- PS_VpnS2SInterface.SetByCustomPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# SetByCustomPolicy method of the PS\_VpnS2SInterface class

Modifies parameters in a S2S Interface. If the interface is already connected, the changes take effect after disconnection.

## Syntax


```mof
uint32 SetByCustomPolicy(
  [in]  string             Destination[],
  [in]  boolean            AdminStatus,
  [in]  boolean            PromoteAlternate,
  [in]  string             AuthenticationMethod,
  [in]  string             EapMethod,
  [in]  boolean            InternalIPv4,
  [in]  boolean            Force,
  [in]  string             PostConnectionIPv4Subnet[],
  [in]  string             IPv4TriggerFilter[],
  [in]  uint32             IPv4TriggerFilterAction,
  [in]  string             PostConnectionIPv6Subnet[],
  [in]  string             IPv6TriggerFilter[],
  [in]  uint32             IPv6TriggerFilterAction,
  [in]  string             IPv4Subnet[],
  [in]  string             Name,
  [in]  string             ResponderAuthenticationMethod,
  [in]  boolean            PassThru,
  [in]  boolean            Persistent,
  [in]  boolean            InitiateConfigPayload,
  [in]  string             RadiusAttributeClass,
  [in]  uint32             EnableQoS,
  [in]  uint64             TxBandwidthKbps,
  [in]  uint64             RxBandwidthKbps,
  [in]  uint32             NetworkOutageTimeSeconds,
  [in]  uint32             NumberOfTries,
  [in]  uint32             RetryIntervalSeconds,
  [in]  uint32             SADataSizeForRenegotiationKilobytes,
  [in]  uint32             SALifeTimeSeconds,
  [in]  uint32             MMSALifeTimeSeconds,
  [in]  string             IPv6Subnet[],
  [in]  boolean            InternalIPv6,
  [in]  uint32             IdleDisconnectSeconds,
  [in]  string             UserName,
  [in]  string             Password,
  [in]  uint8              Certificate[],
  [in]  string             SharedSecret,
  [in]  uint32             EncryptionMethod,
  [in]  uint32             IntegrityCheckMethod,
  [in]  uint32             CipherTransformConstants,
  [in]  uint32             DHGroup,
  [in]  uint32             AuthenticationTransformConstants,
  [in]  uint32             PfsGroup,
  [in]  boolean            CustomPolicy,
  [in]  string             SourceIPAddress,
  [in]  VpnTrafficSelector LocalVpnTrafficSelector[],
  [in]  VpnTrafficSelector RemoteVpnTrafficSelector[],
  [out] VpnS2SInterface    cmdletOutput
);
```



## Parameters

<dl> <dt>

*Destination* \[in\]
</dt> <dd>

Specifies the destination end-point of the S2S connection.

</dd> <dt>

*AdminStatus* \[in\]
</dt> <dd>

Specifies the admin status of the cmdlet.

</dd> <dt>

*PromoteAlternate* \[in\]
</dt> <dd>

An alternate IP addresses that connects successfully becomes the primary IP address, and the current primary IP address is moved to the alternate list.

</dd> <dt>

*AuthenticationMethod* \[in\]
</dt> <dd>

Specifies the authentication method to be used by the S2S connection.

</dd> <dt>

*EapMethod* \[in\]
</dt> <dd>

Specifies EAP method if the **AuthenticationMethod** property is "EAP".

</dd> <dt>

*InternalIPv4* \[in\]
</dt> <dd>

Specifies negotiation of IPv4 address.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether this procedure displays the default confirmation prompt to the user. **True** to display the default confirmation prompt; otherwise **false**.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*PostConnectionIPv4Subnet* \[in\]
</dt> <dd>

The IPv4 subnet to route. The routes specified by the subnet do not trigger the S2S connection.

**Windows Server 2012:** This parameter was renamed from *IPv4DontTriggerSubnet* in Windows Server 2012 R2.

</dd> <dt>

*IPv4TriggerFilter* \[in\]
</dt> <dd>

An array that contains the demand dial filters for the IPv4 Transport.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*IPv4TriggerFilterAction* \[in\]
</dt> <dd>

Sets the value that indicates whether the IPv4 trigger filters initiates the S2S connection. This parameter can be set to one of the following values.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

<dt>

0
</dt> <dd>

Allow

</dd> <dt>

1
</dt> <dd>

Block

</dd> </dl> </dd> <dt>

*PostConnectionIPv6Subnet* \[in\]
</dt> <dd>

The IPv6 subnet to route. The routes specified by the subnet do not trigger the S2S connection.

**Windows Server 2012:** This parameter was renamed from *IPv6DontTriggerSubnet* in Windows Server 2012 R2.

</dd> <dt>

*IPv6TriggerFilter* \[in\]
</dt> <dd>

An array that contains the demand dial filters for the IPv6 Transport.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*IPv6TriggerFilterAction* \[in\]
</dt> <dd>

Sets the value that indicates whether the IPv6 trigger filters initiates the S2S connection. This parameter can be set to one of the following values.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

<dt>

0
</dt> <dd>

Allow

</dd> <dt>

1
</dt> <dd>

Block

</dd> </dl> </dd> <dt>

*IPv4Subnet* \[in\]
</dt> <dd>

Specifies the IPv4 subnet that is routed on this connection with metric.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the connection.

</dd> <dt>

*ResponderAuthenticationMethod* \[in\]
</dt> <dd>

Specifies the responder authentication method to be used by the S2S connection.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns an object. **True** to return an object other **false**.

</dd> <dt>

*Persistent* \[in\]
</dt> <dd>

A value that indicates whether the connection is persistent or triggered by network traffic. **True** if the connection is persistent; otherwise **false**.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*InitiateConfigPayload* \[in\]
</dt> <dd>

A value that indicates whether negotiate the configuration with peers. **True** to negotiate the configuration with peers; otherwise **false**.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*RadiusAttributeClass* \[in\]
</dt> <dd>

The Class attribute of the RADIUS server.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*EnableQoS* \[in\]
</dt> <dd>

Indicates whether QoS is enabled on the network interface. 0 to enable QoS; otherwise 1.

**Windows Server 2012:** This parameter was renamed from *QoS* in Windows Server 2012 R2.

</dd> <dt>

*TxBandwidthKbps* \[in\]
</dt> <dd>

The bandwidth limit for incoming traffic from the VPN interface, in kbps.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*RxBandwidthKbps* \[in\]
</dt> <dd>

The bandwidth limit for outgoing traffic to the VPN interface, in kbps.

**Windows Server 2012:** This parameter is unavailable before Windows Server 2012 R2.

</dd> <dt>

*NetworkOutageTimeSeconds* \[in\]
</dt> <dd>

Maximum network outage time after which the connection is disconnected.

</dd> <dt>

*NumberOfTries* \[in\]
</dt> <dd>

The number of times the connection is retried. Specify 0 for an unlimited number of retries.

</dd> <dt>

*RetryIntervalSeconds* \[in\]
</dt> <dd>

Number of seconds between retries.

</dd> <dt>

*SADataSizeForRenegotiationKilobytes* \[in\]
</dt> <dd>

The number of kilobytes that are allowed to transfer using a SA. After the transfer, the SA will be renegotiated.

</dd> <dt>

*SALifeTimeSeconds* \[in\]
</dt> <dd>

Lifetime of a security association (SA) in seconds, after which the SA is no longer valid.

</dd> <dt>

*MMSALifeTimeSeconds* \[in\]
</dt> <dd>

Lifetime of main mode security association (SA) in seconds, after which the MM SA is no longer valid.

**Windows Server 2012 R2 and Windows Server 2012:** This property is not supported before Windows Server 2016.

</dd> <dt>

*IPv6Subnet* \[in\]
</dt> <dd>

Specifies the IPv6 subnet that is routed on this connection with metric.

</dd> <dt>

*InternalIPv6* \[in\]
</dt> <dd>

Specifies negotiation of IPv6 Address.

</dd> <dt>

*IdleDisconnectSeconds* \[in\]
</dt> <dd>

A value that specifies the time, in seconds, after which an idle connection is terminated. Unless the idle time-out is disabled, the entire connection is terminated if the connection is idle for the specified interval.

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

Username to be used for dialing this connection. Applicable only if the authentication method is set to "EAP".

</dd> <dt>

*Password* \[in\]
</dt> <dd>

Password of the username to be used for dialing the connection. Applicable only if the authentication method is set to "EAP".

</dd> <dt>

*Certificate* \[in\]
</dt> <dd>

Subject Name of the certificate to be used in default store. Applicable only if the authentication method is set to "MachineCert".

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Text of the Shared Secret to be used in dialing the connection. Applicable only if the authentication method is set to "PSK".

</dd> <dt>

*EncryptionMethod* \[in\]
</dt> <dd>

Encryption method plumbed in IKE policy.

</dd> <dt>

*IntegrityCheckMethod* \[in\]
</dt> <dd>

Integrity method plumbed in IPsec policy.

</dd> <dt>

*CipherTransformConstants* \[in\]
</dt> <dd>

Cipher plumbed in IPsec policy.

</dd> <dt>

*DHGroup* \[in\]
</dt> <dd>

DH Group plumbed in IPsec policy.

</dd> <dt>

*AuthenticationTransformConstants* \[in\]
</dt> <dd>

Auth transform plumbed in IPsec policy.

</dd> <dt>

*PfsGroup* \[in\]
</dt> <dd>

PFS Group plumbed in IPsec policy.

</dd> <dt>

*CustomPolicy* \[in\]
</dt> <dd>

Specifies custom IKE IPsec policies, must be a separate parameter set.

</dd> <dt>

*SourceIPAddress* \[in\]
</dt> <dd>

The IP address of the interface.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*LocalVpnTrafficSelector* \[in\]
</dt> <dd>

An embedded instance of a local [**VpnTrafficSelector**](vpntrafficselector.md) to be negotiated.

**Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.

</dd> <dt>

*RemoteVpnTrafficSelector* \[in\]
</dt> <dd>

An embedded instance of a remote [**VpnTrafficSelector**](vpntrafficselector.md) to be negotiated.

**Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterface**](ps-vpns2sinterface.md)
</dt> </dl>

 

 





