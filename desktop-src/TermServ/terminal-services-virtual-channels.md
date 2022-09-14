---
title: Remote Desktop Services virtual channels
description: Virtual channels are software extensions that can be used to add functional enhancements to a Remote Desktop Services application.
ms.assetid: f7bdebec-ecc3-4f28-9327-f0d2f169c142
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services virtual channels

*Virtual channels* are software extensions that can be used to add functional enhancements to a Remote Desktop Services application. Examples of functional enhancements might include: support for special types of hardware, audio, or other additions to the core functionality provided by the Remote Desktop Services [Remote Desktop Protocol](remote-desktop-protocol.md) (RDP). The RDP protocol provides multiplexed management of multiple virtual channels.

## In this section

<dl> <dt>

[Using Remote Desktop Services virtual channels](using-terminal-services-virtual-channels.md)
</dt> <dd>

To implement a virtual channel, you provide the server and client modules of a virtual channel's application.

</dd> <dt>

[Dynamic virtual channels reference](dynamic-virtual-channels-reference.md)
</dt> <dd>

Dynamic virtual channel (DVC) client interfaces are supported by Remote Desktop Services.

</dd> <dt>

[Graphics virtual channels reference](graphics-virtual-channels-reference.md)
</dt> <dd>

The graphics virtual channels reference contains programming elements that enable you to create a virtual graphics channel.

</dd> </dl>

A virtual channel application has two parts, a client module and a server module. The server module is an executable program running on the Remote Desktop Session Host (RD Session Host) server. The client module is a DLL that must be loaded into memory on the client computer when the Remote Desktop Connection (RDC) client program runs.

Virtual channels can add functional enhancements to a Remote Desktop Connection (RDC) client, independent of the RDP protocol. With virtual channel support, new features can be added without having to update the client or server software, or the RDP protocol.

Four major classes of users of virtual channels have been identified:

-   General kernel-mode drivers, such as serial or printer drivers.
-   File system redirection (this is just a special case of a general kernel-mode driver).
-   User mode applications, for example remote cut-and-paste.
-   Audio devices.

For more information, see [Using Remote Desktop Services Virtual Channels](using-terminal-services-virtual-channels.md).

If you have enabled a virtual channels application in your Remote Desktop Services deployment, you can make the application available to client computers that access the RD Session Host server by means of the Remote Desktop Microsoft ActiveX control. For more information, see [Scriptable Virtual Channels](scriptable-virtual-channels.md) and [Using the Remote Desktop ActiveX Control with Virtual Channels](using-the-remote-desktop-activex-control-with-virtual-channels.md).

 

 




