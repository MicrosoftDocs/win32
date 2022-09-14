---
title: Virtual Channel Server Application
description: The server module of an application that uses virtual channels must be a user-mode application running in a client session on the Remote Desktop Session Host (RD Session Host) server. Note that you must provide a method to start the server application.
ms.assetid: b593df5d-5e22-46c6-8f59-9e3fdfe765ad
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Channel Server Application

The server module of an application that uses virtual channels must be a user-mode application running in a client session on the Remote Desktop Session Host (RD Session Host) server. Note that you must provide a method to start the server application. You can accomplish this in multiple ways; for example, you can use a logon script, or a program or script in the Startup folder. Users could also launch the application.

You must store the name of the virtual channel server application in the registry by adding a subkey under the following location:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**Terminal Server**\\**Addins**

For more information about the subkey, see [Monitoring Session Connections and Disconnections](monitoring-session-connections-and-disconnections.md).

The server application can call the [**WTSVirtualChannelOpen**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopen) function to open a handle to a virtual channel. The application can then use the handle in any of the following functions.

<dl> <dt>

[**WTSVirtualChannelClose**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelclose)
</dt> <dd>

Closes an open virtual channel handle.

</dd> <dt>

[**WTSVirtualChannelPurgeInput**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelpurgeinput)
</dt> <dd>

Deletes all queued input data sent from the client to the server on a specific virtual channel.

> [!Note]  
> This function currently is not used by Remote Desktop Services.

 

</dd> <dt>

[**WTSVirtualChannelPurgeOutput**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelpurgeoutput)
</dt> <dd>

Deletes all queued output data sent from the server to the client on a specific virtual channel.

> [!Note]  
> This function currently is not used by Remote Desktop Services.

 

</dd> <dt>

[**WTSVirtualChannelQuery**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelquery)
</dt> <dd>

Returns information about a specified virtual channel.

</dd> <dt>

[**WTSVirtualChannelRead**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelread)
</dt> <dd>

Reads data from the server end of a virtual channel.

</dd> <dt>

[**WTSVirtualChannelWrite**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelwrite)
</dt> <dd>

Writes data to the server end of a virtual channel.

</dd> </dl>

 

 




