---
description: Starting with Windows Vista, the service control manager (SCM) supports remote procedure calls over both Transmission Control Protocol (RPC/TCP) and named pipes (RPC/NP).
ms.assetid: c51732f6-c22f-4726-afaa-13a8948ac44f
title: Services and RPC/TCP
ms.topic: article
ms.date: 05/31/2018
---

# Services and RPC/TCP

Starting with Windows Vista, the service control manager (SCM) supports remote procedure calls over both Transmission Control Protocol (RPC/TCP) and named pipes (RPC/NP). Client-side SCM functions use RPC/TCP by default.

RPC/TCP is appropriate for most applications that use SCM functions remotely, such as remote administration or monitoring tools. However, for compatibility and performance, some applications might need to disable RPC/TCP by setting the registry values described in this topic.

When a service calls a remote SCM function, the client-side SCM first attempts to use RPC/TCP to communicate with the server-side SCM. If the server is running a version of Windows that supports RPC/TCP and allows RPC/TCP traffic, the RPC/TCPP connection will succeed. If the server is running a version of Windows that does not support RPC/TCP, or supports RPC/TCP but is operating behind a firewall which allows only named pipe traffic, the RPC/TCP connection times out and the SCM retries the connection with RPC/NP. This will succeed eventually but can take some time (typically more than 20 seconds), causing the [**OpenSCManager**](/windows/desktop/api/Winsvc/nf-winsvc-openscmanagera) function to appear blocked.

TCP does not carry user credentials specified with a **net use** command. Therefore, if RPC/TCP is enabled and **sc.exe** is used to attempt to access the specified service, the command could fail with access denied. Disabling RPC/TCP on the client side causes the **sc.exe** command to use a named pipe that does carry user credentials, so the command will succeed. For information about sc.exe, see [Controlling a Service Using SC](controlling-a-service-using-sc.md).

> [!Note]  
> A service should not provide explicit credentials to a **net use** command, because those credentials might be inadvertently shared outside of the service boundaries. Instead, the service should use [client impersonation](/windows/desktop/SecAuthZ/client-impersonation) to impersonate the user.

 

### RPC/TCP Registry Values

RPC/TCP is controlled by the **SCMApiConnectionParam**, **DisableRPCOverTCP**, and **DisableRemoteScmEndpoints** registry values, which are all under the **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control** key. All of these values have a REG\_DWORD data type. The following procedures show how to use these registry values to control RPC/TCP.

The following procedure describes how to disable RPC/TCP on the client side.

**To disable RPC/TCP on the client side**

1.  Combine the **SCMApiConnectionParam** registry value with the mask value 0x80000000.
2.  Restart the application that calls the [**OpenSCManager**](/windows/desktop/api/Winsvc/nf-winsvc-openscmanagera) function.

The following procedure describes how to disable TCP on the server side.

**To disable TCP on the server side**

1.  Set the **DisableRPCOverTCP** registry value to 1.
2.  Restart the server.

The following procedure describes how to disable both RPC/TCP and RPC/NP on the server (for example, to reduce the attack surface).

**To disable both RPC/TCP and RPC/NP on the server**

1.  Set the **DisableRemoteScmEndpoints** registry value to 1.
2.  Restart the server.

The **SCMApiConnectionParam** registry value can also be used to specify the RPC/TCP time-out interval, in milliseconds. For example, a value of 30,000 specifies a time-out interval of 30 seconds. The default is 21,000 (21 seconds).

 

 
