---
title: Name Service Entry Cleanup
description: A name service entry should contain information that does not change frequently.
ms.assetid: b581bc10-e537-4714-b89a-d998fec23360
ms.topic: article
ms.date: 05/31/2018
---

# Name Service Entry Cleanup

A name service entry should contain information that does not change frequently. For this reason, do not include dynamic endpoints in your exported binding handles because they will change at each invocation of the server and will clutter up your name service entry. To remove these binding handles, use [**RpcBindingReset**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingreset).

For example, a reasonable sequence of server operations would be:

For more than one transport:

``` syntax
RpcServerUseProtseq();
RpcServerUseProtseq();
```

To place bindings in the endpoint mapper:

``` syntax
RpcServerInqBindings(&Vector);
RpcEpRegister(Interface, Vector);
```

To remove endpoints from bindings:

``` syntax
for (i=0; i < Vector- > Count; + + i)
{
    RpcBindingReset(Vector->BindingH[i];
}
```

To add bindings to the name service:

``` syntax
RpcNsBindingExport(RPC_C_NS_SYNTAX_DEFAULT, EntryName, Interface
                   Vector);
RpcServerListen();
```

 

 




