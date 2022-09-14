---
title: Virtual Channel Client DLL
description: The client of a virtual channels application is a DLL that is loaded during the Remote Desktop Services initialization on the client computer. The DLL must be registered on the client computer.
ms.assetid: fca0505c-c4a9-4230-aeaa-ff3dfa62f581
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Channel Client DLL

The client of a virtual channels application is a DLL that is loaded during the Remote Desktop Services initialization on the client computer. The DLL must be registered on the client computer. For more information, see [Virtual Channel Client Registration](virtual-channel-client-registration.md).

The client DLL must export a [**VirtualChannelEntry**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelentry) function, which Remote Desktop Services calls during initialization. The **VirtualChannelEntry** entry point receives a pointer to a [**CHANNEL\_ENTRY\_POINTS**](/windows/win32/api/cchannel/ns-cchannel-channel_entry_points) structure. This structure contains pointers to the functions that the client DLL calls to access virtual channels.



| Function                                                      | Description                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VirtualChannelInit**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelinit)<br/>   | Registers the names of the virtual channels to be used by the client and provides a [**VirtualChannelInitEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_init_event_fn) callback function through which Remote Desktop Services notifies the client about events that affect the client connection.<br/> |
| [**VirtualChannelOpen**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelopen)<br/>   | Opens the client end of a specified virtual channel and provides a [**VirtualChannelOpenEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_open_event_fn) callback function through which Remote Desktop Services notifies the client about events that affect the virtual channel.<br/>                    |
| [**VirtualChannelWrite**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelwrite)<br/> | Writes data to a virtual channel. Remote Desktop Services sends this data to the server end of the virtual channel. The server end calls the [**WTSVirtualChannelRead**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelread) function to read the data.<br/>                                             |
| [**VirtualChannelClose**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelclose)<br/> | Closes a virtual channel.<br/>                                                                                                                                                                                                                                                  |



 

Your DLL's [**VirtualChannelEntry**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelentry) function must call the [**VirtualChannelInit**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelinit) function to initialize access to virtual channels. When you call **VirtualChannelInit**, you must pass a pointer to the [**VirtualChannelInitEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_init_event_fn) callback function. Remote Desktop Services calls this callback function when initialization is complete and again when a connection has been established with a Remote Desktop Session Host (RD Session Host) server.

After the connection is established, you can call the [**VirtualChannelOpen**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelopen) function to open the virtual channels registered by the [**VirtualChannelInit**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelinit) call. The **VirtualChannelOpen** call specifies a pointer to your [**VirtualChannelOpenEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_open_event_fn) callback function.

After the [**VirtualChannelOpen**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelopen) call returns, you can call the [**VirtualChannelWrite**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelwrite) function to write to the virtual channel. The write operation is asynchronous, so you must not free or reuse the buffer passed to **VirtualChannelWrite** until Remote Desktop Services calls your [**VirtualChannelOpenEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_open_event_fn) function to indicate that the write operation has been completed. When you call **VirtualChannelWrite**, you can pass a piece of user data that identifies the write operation. Remote Desktop Services passes this user data back when it calls **VirtualChannelOpenEvent** to notify you that the operation has completed. At the server end of the virtual channel, the server add-in calls the [**WTSVirtualChannelRead**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelread) function to read the data.

Remote Desktop Services also calls your [**VirtualChannelOpenEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_open_event_fn) function when data is written to the virtual channel by the server module. The server module calls the [**WTSVirtualChannelWrite**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelwrite) function to write data to the server end of the virtual channel.

The client and server modules can write data blocks of any size to the virtual channel. Before sending the data, however, Remote Desktop Services segments the data into chunks of CHANNEL\_CHUNK\_LENGTH bytes. Remote Desktop Services calls your [**VirtualChannelOpenEvent**](/windows/desktop/api/Cchannel/nc-cchannel-channel_open_event_fn) function once for each chunk of data, rather than rebuilding the data into a block of the original size. Each call to **VirtualChannelOpenEvent** indicates the size of the chunk, the total size written by the server, and whether the data constitutes the beginning, middle, or end of a block written by the server.

You can call the [**VirtualChannelClose**](/windows/desktop/api/Cchannel/nc-cchannel-virtualchannelclose) function to close a channel. However, it is not necessary to call it because Remote Desktop Services closes all channels automatically when the client disconnects from the server.

 

 





