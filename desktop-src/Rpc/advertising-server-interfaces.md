---
title: Advertising Server Interfaces
description: The server side of an application that uses automatic handles must call the function RpcNsBindingExport to make binding information about the server available to clients.
ms.assetid: d15fd8da-3afd-4031-95d1-b76a0ad9a20d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Advertising Server Interfaces

The server side of an application that uses automatic handles must call the function [**RpcNsBindingExport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta?branch=master) to make binding information about the server available to clients. Automatic binding handles require a name service running on a server that is accessible to the client. The Microsoft implementation of the name service, Microsoft Locator, manages automatic handles. Server applications that use implicit and explicit binding handles can also advertise their presence in the name service database.

Typically, the server calls the following run-time functions:

``` syntax
/* auto handle server application (fragment) */
 
//interface header file that the MIDL compiler generates
#include "auto.h" 
 
void main(void)
{
    RpcUseProtseqEp(...);
    RpcServerRegisterIf(...);
    RpcServerInqBindings(...);
    RpcNsBindingExport(...);
    ...
}
```

The calls to the first two functions in this code fragment are similar to the [Hello, World example](tutorial.md). These functions make information about the binding available to the client. The calls to [**RpcServerInqBindings**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverinqbindings?branch=master) and [**RpcNsBindingExport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta?branch=master) put the information in the name service database. The call to [**RpcServerInqBindings**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverinqbindings?branch=master) fills the binding vector with valid binding handles before the handles are exported to the name service. After the server program exports the handles to the database, the client (or client stubs) can call [**RpcNsBindingImportBegin**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina?branch=master) and [**RpcNsBindingImportNext**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingimportnext?branch=master) to obtain this information. For details, see [Finding Server Host Systems](finding-server-host-systems.md).

The calls to [**RpcServerInqBindings**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverinqbindings?branch=master) and [**RpcNsBindingExport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta?branch=master) and their associated data structures look similar to the following:

``` syntax
RPC_BINDING_VECTOR * pBindingVector;
RPCSTATUS status;
 
status = RpcServerInqBindings(&pBindingVector);
 
status = RpcNsBindingExport(
                fNameSyntaxType,      // name syntax type 
                pszAutoEntryName,     // nsi entry name 
                autoh_ServerIfHandle, // if server handle
                pBindingVector,       // set in previous call 
                NULL);                // UUID vector
```

Note that the [**RpcServerInqBindings**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverinqbindings?branch=master) parameter *pBindingVector* is a pointer to a pointer to [**RPC\_BINDING\_VECTOR**](/windows/win32/Rpcdce/ns-rpcdce-_rpc_binding_vector?branch=master). Also remember that each call to [**RpcNsBindingExport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta?branch=master) must be followed by a call to [**RpcBindingVectorFree**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingvectorfree?branch=master).

To remove the exported interface from the name service database, the server calls [**RpcNsBindingUnexport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingunexporta?branch=master) as shown:

``` syntax
status = RpcNsBindingUnexport(
                fNameSyntaxType, 
                pszAutoEntryName,  
                auto_ServerIfHandle,
                NULL);              // unexport handles only
```

The [**RpcNsBindingUnexport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingunexporta?branch=master) function should be used only when the service is being permanently removed. It should not be used when the service is temporarily disabled, such as when the server is shut down for maintenance. A server program can register itself with the name service database, yet be unavailable because the server is temporarily offline. The client application should contain exception-handling code for such a condition.

For more information on the content and format of the name service database, see [The RPC Name Service Database](the-rpc-name-service-database.md).

Applications can utilize the Active Directory service if both the client and server programs are running under Windows 2000. The computers running the client and server programs must both be members of a Windows 2000 domain.

To advertise its presence using the Active Directory service, the server program should run in the security context of a domain administrator. If it is running in the context of domain users, a domain administrator must modify the access control list (ACL) on the RPC Services container. For more information, see the Active Directory documentation.

 

 




