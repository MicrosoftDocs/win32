---
title: Remote Control Persistent Virtual Channels
description: A remote control persistent virtual channel is not closed when a remote control connects or disconnects for the session connected to the client. Data will continue to be transmitted and received through this channel.
ms.assetid: 0c3d5429-250e-4272-8cdd-69097acfaff4
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Control Persistent Virtual Channels

On Windows XP, a DLL can specify one or more virtual channels as *remote control persistent*. A remote control persistent virtual channel is not closed when a remote control connects or disconnects for the session connected to the client. Data will continue to be transmitted and received through this channel. Virtual channels that the DLL does not specify as remote control persistent will close in this scenario.

Remote control persistent virtual channels are specified during the call to **VirtualChannelInit**. Refer to the reference page for [**VirtualChannelInit**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelinit) for specific information about this.

 

 




