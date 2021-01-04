---
title: Win32_TSGatewayConnection class
description: Represents a connection from a client computer to a Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 6e76ae25-409d-436a-8eef-8f047194c29c
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayConnection class Remote Desktop Services
- Win32_TSGatewayConnection class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnection
- Win32_TSGatewayConnection.ConnectionKey
- Win32_TSGatewayConnection.TunnelId
- Win32_TSGatewayConnection.ChannelId
- Win32_TSGatewayConnection.UserName
- Win32_TSGatewayConnection.FullUserName
- Win32_TSGatewayConnection.ClientAddress
- Win32_TSGatewayConnection.ConnectedTime
- Win32_TSGatewayConnection.IdleTime
- Win32_TSGatewayConnection.ConnectedResource
- Win32_TSGatewayConnection.ProtocolName
- Win32_TSGatewayConnection.ConnectedPort
- Win32_TSGatewayConnection.NumberOfKilobytesSent
- Win32_TSGatewayConnection.NumberOfKilobytesReceived
- Win32_TSGatewayConnection.ConnectionDuration
- Win32_TSGatewayConnection.TransportProtocol
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSGatewayConnection class

Represents a connection from a client computer to a Remote Desktop Gateway (RD Gateway) server.

## Syntax

``` syntax
[dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayConnection
{
  string ConnectionKey;
  uint64 TunnelId;
  uint32 ChannelId;
  string UserName;
  string FullUserName;
  string ClientAddress;
  string ConnectedTime;
  string IdleTime;
  string ConnectedResource;
  string ProtocolName;
  uint32 ConnectedPort;
  uint64 NumberOfKilobytesSent;
  uint64 NumberOfKilobytesReceived;
  string ConnectionDuration;
  uint32 TransportProtocol;
};
```

## Members

The **Win32\_TSGatewayConnection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSGatewayConnection** class has these methods.



| Method                                                                     | Description                                                                                                                      |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| [**CheckStatus**](checkstatus-win32-tsgatewayconnection.md)               | Checks the status of an RD Gateway server connection, and whether the target server is configured for load balancing.<br/> |
| [**Disconnect**](disconnect-win32-tsgatewayconnection.md)                 | Ends the connection.<br/>                                                                                                  |
| [**DisconnectProtocol**](disconnectprotocol-win32-tsgatewayconnection.md) | Ends all connections that use the specified protocol.<br/>                                                                 |
| [**DisconnectUser**](disconnectuser-win32-tsgatewayconnection.md)         | Ends all connections of the specified user.<br/>                                                                           |



 

### Properties

The **Win32\_TSGatewayConnection** class has these properties.

<dl> <dt>

**ChannelId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Channel identifier.

</dd> <dt>

**ClientAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Client IP address.

</dd> <dt>

**ConnectedPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Port on the connected resource to which the user is connected.

</dd> <dt>

**ConnectedResource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer (or cluster) to which the client is connected.

</dd> <dt>

**ConnectedTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time stamp for when the connection was established. This time is reset when the connection is reset, even if it is automatically reconnected.

</dd> <dt>

**ConnectionDuration**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time that has elapsed since the connected time.

</dd> <dt>

**ConnectionKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Connection identifier in the format "tunnelId:channelID".

</dd> <dt>

**FullUserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full user name of the connected user.

</dd> <dt>

**IdleTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Idle time of the connection.

</dd> <dt>

**NumberOfKilobytesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of kilobytes received from the client computer by the RD Gateway server.

</dd> <dt>

**NumberOfKilobytesSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of kilobytes sent to the client computer by the RD Gateway server.

</dd> <dt>

**ProtocolName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Protocol that is used to connect to the RD Gateway server.

<dt>

"RDP"
</dt> <dd>

The protocol for the RD Gateway server.

</dd> </dl>

</dd> <dt>

**TransportProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the transport type for the connection. This must be one of the following values.

<dt>

0
</dt> <dd>

RPC over HTTP transport.

</dd> <dt>

1
</dt> <dd>

HTTP transport.

</dd> <dt>

2
</dt> <dd>

UDP transport.

</dd> </dl>

</dd> <dt>

**TunnelId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Tunnel identifier.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User name connected to the RD Gateway server.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to use this class.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayLoadBalancer**](win32-tsgatewayloadbalancer.md)
</dt> <dt>

[**Win32\_TSGatewayRADIUSServer**](win32-tsgatewayradiusserver.md)
</dt> <dt>

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayResourceGroup**](win32-tsgatewayresourcegroup.md)
</dt> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

