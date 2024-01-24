---
title: Configuring the Registry for Port Allocations and Selective Binding
description: Starting with Windows 2000, a utility in the Windows Resource Kit called Rpccfg.exe should be used to set bindings. For more information, consult the Windows Resource Kit for the appropriate operating system version.
ms.assetid: a33b51e7-2ded-46bd-aadb-27cbd99e1029
keywords:
- Remote Procedure Call RPC , tasks, configuring registry for port allocations and selective binding
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Registry for Port Allocations and Selective Binding

Starting with Windows 2000, a utility in the Windows Resource Kit called Rpccfg.exe should be used to set bindings. For more information, consult the Windows Resource Kit for the appropriate operating system version.

For versions of windows prior to Windows 2000, the registry keys in the following table specify the system defaults for dynamic port allocation and for binding to NICs on multihomed computers. You must first create these keys and then specify the appropriate settings.

Using the [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex) function affects these settings. Developers should be familiar with the registry settings explained in this section and the **RpcServerUseProtseqEx** function when managing port allocations. An example with three hypothetical applications follows the table below, and illustrates how these settings and the **RpcServerUseProtseqEx** function interoperate.

If a key is missing or if it contains an invalid value, the entire configuration is marked as invalid, and all **RpcServerUseProtseq\*** calls over [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp) or [**ncadg\_ip\_udp**](/windows/desktop/Midl/ncadg-ip-udp) will fail.

> [!Note]  
> Ports allocated to a process remain allocated until that process dies. If all available ports are in use, the function returns RPC\_S\_OUT\_OF\_RESOURCES.

 




| Port key | Data type | Description | 
|----------|-----------|-------------|
| <pre data-space="preserve"><code>HKEY_LOCAL_MACHINE   Software      Microsoft         Rpc            Internet               Ports</code></pre> | <strong>REG_MULTI_SZ</strong> | Specifies a set of IP port ranges consisting of either all the ports available from the Internet or all the ports not available from the Internet. Each string represents a single port or an inclusive set of ports (for example,1000-1050, 1984). If any entries are outside the range 0 to 65535, or if any string cannot be interpreted, the RPC run time will treat the entire configuration as invalid. | 
| <pre data-space="preserve"><code>HKEY_LOCAL_MACHINE   Software      Microsoft         Rpc            Internet               PortsInternetAvailable</code></pre> | <strong>REG_SZ</strong> | Y or N (not case-sensitive). If Y, the ports listed in the Ports key are all the Internet-available ports on that computer. If N, the ports listed in the Ports key are all those ports that are not Internet-available. | 
| <pre data-space="preserve"><code>HKEY_LOCAL_MACHINE   Software      Microsoft         Rpc            Internet               UseInternetPorts</code></pre> | <strong>REG_SZ</strong> | Y or N (not case-sensitive). Specifies the system default policy. If Y, the processes using the default will be assigned ports from the set of Internet-available ports, as defined above. If N, processes using the default will be assigned ports from the set of intranet-only ports. | 
| <pre data-space="preserve"><code>HKEY_LOCAL_MACHINE   System      CurrentControlSet         Services            Rpc               Linkage                  Bind</code></pre> | <strong>REG_MULTI_SZ</strong> | Lists the device names of all the NICs on which to bind by default (for example, \Device\AMDPCN1). If the key does not exist, the server will bind to all NICs. If the key does exist, the server will bind to the NICs specified in the key, unless the NICFlags field is set to RPC_C_BIND_TO_ALL_NICS. If the key has a null ("") value, the configuration will be marked as invalid and all calls to <strong>RpcServerUseProtseq*</strong> over <a href="/windows/desktop/Midl/ncacn-ip-tcp"><strong>ncacn_ip_tcp</strong></a> or <a href="/windows/desktop/Midl/ncadg-ip-udp"><strong>ncadg_ip_udp</strong></a> will fail. | 




 

The following table illustrates how three sample applications are affected by the settings defined in the previous table, and how settings applied using the [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex) function are also affected.

In this example, three hypothetical applications are considered:

-   InternetApp: This application is intended for exposure to the Internet, and has specified RPC\_C\_USE\_INTERNET\_PORT in the **EndpointFlags** member of the [**RPC\_POLICY**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_policy) structure passed to the [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex) function.
-   LocalApp: This application is not intended for exposure to the Internet, and has specified RPC\_C\_USE\_INTRANET\_PORT in the **EndpointFlags** member of the [**RPC\_POLICY**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_policy) structure passed to the [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex) function.
-   DefaultApp: This application specifies zero in the **EndpointFlags** member of the [**RPC\_POLICY**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_policy) structure passed to the [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex) function.

The following table explains the impact these settings have based on values specified in the registry entries explained in the previous table. For formatting considerations, the following codes are assigned:

PIA = PortsInternetAvailable Key value

UIP = UseInternetPorts Key value

The value of the Ports key, for sake of this example, is 5000-5100 for each entry.



| Application | PIA | UIP | Result                                  |
|-------------|-----|-----|-----------------------------------------|
| InternetApp | Y   | Y   | Uses ports between 5000 and 5100        |
| LocalApp    | Y   | Y   | Uses a port outside the 5000-5100 range |
| DefaultApp  | Y   | Y   | Uses ports between 5000 and 5100        |
| InternetApp | Y   | N   | Uses ports between 5000 and 5100        |
| LocalApp    | Y   | N   | Uses a port outside the 5000-5100 range |
| DefaultApp  | Y   | N   | Uses a port outside the 5000-5100 range |
| InternetApp | N   | Y   | Uses a port outside the 5000-5100 range |
| LocalApp    | N   | Y   | Uses ports between 5000 and 5100        |
| DefaultApp  | N   | Y   | Uses a port outside the 5000-5100 range |
| InternetApp | N   | N   | Uses a port outside the 5000-5100 range |
| LocalApp    | N   | N   | Uses ports between 5000 and 5100        |
| DefaultApp  | N   | N   | Uses ports between 5000 and 5100        |



 

## Related topics

<dl> <dt>

[**RPC\_POLICY**](/windows/desktop/api/Rpcdce/ns-rpcdce-rpc_policy)
</dt> <dt>

[**RpcServerUseAllProtseqsEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqsex)
</dt> <dt>

[**RpcServerUseAllProtseqsIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqsifex)
</dt> <dt>

[**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex)
</dt> <dt>

[**RpcServerUseProtseqEpEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex)
</dt> <dt>

[**RpcServerUseProtseqIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqifex)
</dt> <dt>

[**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp)
</dt> <dt>

[**ncadg\_ip\_udp**](/windows/desktop/Midl/ncadg-ip-udp)
</dt> </dl>

 

 
