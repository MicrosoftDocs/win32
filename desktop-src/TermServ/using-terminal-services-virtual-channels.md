---
title: Using Remote Desktop Services virtual channels
description: To implement a virtual channel, you provide the server and client modules of a virtual channel's application.
ms.assetid: 3b378071-ebd6-47b0-8a9c-3e671505011a
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Using Remote Desktop Services virtual channels

To implement a virtual channel, you provide the server and client modules of a virtual channel's application. The server module can be a user-mode application or a kernel-mode driver. The client module must be a DLL.

For descriptions of these modules, see the following topics.

## In this section

<dl> <dt>

[Virtual Channel Server Application](virtual-channel-server-application.md)
</dt> <dd>

The server module of an application that uses virtual channels must be a user-mode application running in a client session on the Remote Desktop Session Host (RD Session Host) server. Note that you must provide a method to start the server application.

</dd> <dt>

[Virtual Channel Client DLL](virtual-channel-client-dll.md)
</dt> <dd>

The client of a virtual channels application is a DLL that is loaded during the Remote Desktop Services initialization on the client computer. The DLL must be registered on the client computer.

</dd> <dt>

[Virtual Channel Client Registration](virtual-channel-client-registration.md)
</dt> <dd>

You must store the name of the client DLL in the registry.

</dd> <dt>

[Remote Control Persistent Virtual Channels](remote-control-persistent-virtual-channels.md)
</dt> <dd>

A remote control persistent virtual channel is not closed when a remote control connects or disconnects for the session connected to the client. Data will continue to be transmitted and received through this channel.

</dd> <dt>

[Dynamic Virtual Channels](dynamic-virtual-channels.md)
</dt> <dd>

Dynamic virtual channel (DVC) APIs extend the existing virtual channel APIs for Remote Desktop Services, known as static virtual channel (SVC) APIs.

</dd> </dl>

If you have enabled a virtual channel's application in your Remote Desktop Services deployment, you can also make the application available to client computers that access the RD Session Host server by means of the Remote Desktop ActiveX control. For more information, see [Using the Remote Desktop ActiveX Control with Virtual Channels](using-the-remote-desktop-activex-control-with-virtual-channels.md).

 

 




