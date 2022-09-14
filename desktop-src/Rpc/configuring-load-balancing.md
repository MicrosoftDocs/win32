---
title: Configuring Load Balancing
description: Configuring Load Balancing
ms.assetid: c78ffde1-1811-4065-941f-c24692eb144c
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Load Balancing

Each RPC Proxy machine that is to act as a Load Balancing Server (LBS) service must be configured as an LBS service with knowledge of the servers in the server farm. Optionally, the default resource can be set and the security of Proxy to LBS and LBS to LBS RPC calls can be set. These settings are configured by a set of **Required Registry Keys** and **Optional Registry Keys** as described below.

## Required Registry Keys

Several registry keys and values are required to configure an LBS server. If any keys are missing or are entered in error, a Windows Event is logged. See the description of each key and value for information on the event logged.

To configure the server farm, a registry key must be created **HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy** called **LBSConfiguration**. Under the **LBSConfiguration** key, a key is created for each resource in the server farm. The key name is the string representation of the GUID for the resource. At least one resource key must exist, and this resource is identical to the [**UUID**](./rpcdce/ns-rpcdce-uuid.md) set by clients on the binding handle, [**RPC\_BINDING\_HANDLE**](rpc-binding-handle.md), when they create the RPC/HTTP binding (For more information please see [**RpcBindingSetObject**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetobject)). Under each Resource UUID key, there must exist a DWORD value named **ConfigurationType** which describes the configuration used. There must also exist a **REG\_SZ** of semicolon delimited server identifiers called **ServerFarm**. The servers identified in the **ServerFarm** key are the servers which are members of the load balancing server farm.

The following is a detailed breakdown of the required registry keys and values:

**HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration**

Registry Key. The **LBSConfiguration** key is the registry key that holds the LBS configuration. This includes the Resource [**UUIDs**](./rpcdce/ns-rpcdce-uuid.md) that are to be load balanced, the configuration type for each resource and the servers in the server farms which participate in load balancing. If this key is missing or invalid, LBS will not be considered to be configured and the LBS service will not run.

\-

**HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration\\XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX**

Registry Key. The **Resource UUID** key identifies the resource UUID to be load balanced. This resource UUID is the same as the [**UUID**](./rpcdce/ns-rpcdce-uuid.md) that clients set on the binding handle, [**RPC\_BINDING\_HANDLE**](rpc-binding-handle.md). There must be at least one resource UUID to be load balanced, there may be multiple resource UUIDs. There can be only one server farm and all endpoints must be on all servers within the server farm. If this key cannot be parsed to a valid UUID, the event **RPCPROXY\_EVENTLOG\_LB\_INVALID\_KEY (0xC0000006)** will be logged to the Windows Event Log.

\-

**HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration\\XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX\\ConfigurationType**

DWORD. The **ConfigurationType** DWORD is stored under the **Resource UUID** key. The only allowed value is 1. If this value is anything other than 1, the event **RPCPROXY\_EVENTLOG\_LB\_UNKNOWN\_CFG\_TYPE (0xC0000007)** will be logged to the Windows Event Log.

\-

**HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration\\XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX\\ServerFarm**

REG\_SZ. The **ServerFarm** registry value contains a semicolon delimitated list of server identifiers. The format for the server identifiers is:

"ServerID1,ServerPort1,LBSPort1,\[LBSPort2, …LBSPortN\];"

Multiple server identifiers should be listed in the **ServerFarm** registry key. They must be delimited by a semicolon. The fields which are part of the server identifier are described in the following table. If this field cannot be parsed correctly, the event **RPCPROXY\_EVENTLOG\_LB\_BAD\_CONFIG\_ENTRY (0xC0000008)** will be logged to the Windows Event Log.



| Identifier Field | Requirement | Description                                                                                                                                                                                                                                                                        |
|------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ServerID         | Required    | A resolvable network name for the server. This can be a DNS name, a netbios name, or an IP address.                                                                                                                                                                                |
| ServerPort       | Optional    | If specified, the port on which the server listens for RPC/HTTP connections. If not specified, the End point mapper on the server machine is used to find the server port.                                                                                                         |
| LBSPort          | Optional    | If specified, the port the on which the server listens for LBS. To use this key, the LBS interfaces must be set to a static endpoint using a netsh RPC firewall command. See [Load Balancing Best Practices](load-balancing-best-practices.md) for examples of the netsh command. |



 

## Optional Registry Keys

There are three optional registry values to configure an LBS server. The keys primarily control the level of security for calls to and from the LBS service, and also control the default resource UUID to be used. The following are optional values:

The following is a detailed breakdown of the required registry keys and values:

**HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration\\NoSecurity**

DWORD. When the **NoSecurity** DWORD is not present or set to 0, incoming non-secure calls to the LBS service are rejected. When present and not 0, incoming non-secure calls to the LBS service are not rejected. This key is read once on startup of the LBS service.

\-

**HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration\\AssumeResourceUUID**

DWORD. When the **AssumeResourceUUID** DWORD is not present no change in the LBS service occurs. When present, it must be set with a valid [**UUID**](./rpcdce/ns-rpcdce-uuid.md). This **UUID** will be used as the resource UUID for all connections which do not specify a resource UUID. This is commonly used in cases where clients do not specify a Resource UUID when they create the RPC/HTTP binding, but an administrator wishes to load balance the RPC/HTTP traffic to a server farm. If this key cannot be parsed to a UUID, an internal RPC error is lodged, generating [**RPC\_EXTENDED\_ERROR\_INFO**](/windows/win32/api/rpcasync/ns-rpcasync-rpc_extended_error_info) if it is enabled.

\-

**HKLM\\Software\\Microsoft\\Rpc\\RPCHTTPLBSServer\\NoSecurity**

DWORD. When the **NoSecurity** DWORD is not presented or set to 0, all outgoing calls made to LBS services will have security. If present and not set to 0, all outgoing calls made to LBS services will not have security. Ensure this setting matches the **HKLM\\SOFTWARE\\Microsoft\\Rpc\\RpcProxy\\LBSConfiguration\\NoSecurity** setting.

 

 