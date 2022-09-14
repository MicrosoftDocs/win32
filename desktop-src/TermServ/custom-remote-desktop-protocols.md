---
title: Remote Desktop Protocol Provider API
description: You use the Remote Desktop Protocol Provider API to create a protocol to provide communication between the Remote Desktop Services service and multiple clients.
ms.assetid: dd14c569-195e-460e-a1c3-2a74d0f49ff5
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Protocol Provider API

You use the Remote Desktop Protocol Provider API to create a protocol to provide communication between the Remote Desktop Services service and multiple clients.

When Windows Server loads, the Remote Desktop Services service (also known as Remote Connection Manager (RCM)) starts. The service also starts listener objects for the Remote Desktop Protocol Providers that in turn listen for client connections. The service and the protocol providers are user-mode objects that communicate by using the APIs discussed in this documentation. The protocol providers can communicate with kernel-mode drivers by using input/output controls (IOCTLs). This is shown in the following illustration.

![custom protocol api architecture](images/protocol-architecture.png)

Microsoft has implemented the Remote Desktop Protocol (RDP) to provide communication between the Remote Desktop Services service and client connections. You can create your own protocol by using the interfaces, structures, unions, and enumeration types that make up the Remote Desktop Protocol Provider API. For more information, see the following topics.

<dl> <dt>

[Creating a Remote Desktop Protocol Provider](creating-a-custom-remote-protocol.md)
</dt> <dd>

Information about creating a Remote Desktop Protocol Provider. The protocol manager is implemented as a COM server and registered in a location searched when the Remote Desktop Services service starts.

</dd> <dt>

[Remote Desktop Protocol Provider reference](custom-remote-protocol-reference.md)
</dt> <dd>

Contains interfaces, structures, unions, and enumeration types that enable you to create a custom Remote Desktop Protocol (RDP).

</dd> </dl>

## Related topics

<dl> <dt>

[About Remote Desktop Services](about-terminal-services.md)
</dt> </dl>

 

 




