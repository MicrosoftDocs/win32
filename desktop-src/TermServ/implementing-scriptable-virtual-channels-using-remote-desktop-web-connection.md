---
title: Implementing scriptable virtual channels by using Remote Desktop Web Connection
description: Code examples that show the steps for implementing scriptable virtual channels with Remote Desktop Web Connection.
ms.assetid: a482b84d-96b6-4f42-8841-7039a1882789
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Implementing scriptable virtual channels by using Remote Desktop Web Connection

The following procedure and code examples show the steps for implementing scriptable virtual channels with Remote Desktop Web Connection. The examples were written in Visual Basic Scripting Edition and assume that the Remote Desktop ActiveX control is named "MsRdpClient".

**To create and deploy scriptable virtual channels**

1.  Deploy the server side of the application and make sure it is running on the Remote Desktop Session Host (RD Session Host) server. For information about deploying virtual channels applications on the server, see [Virtual Channel Server Application](virtual-channel-server-application.md).
2.  In your client script, call [**IMsTscAx::CreateVirtualChannels**](imstscax-createvirtualchannels.md), passing a string that contains a comma-separated list of virtual channel names.

    ```VB
    MsRdpClient.CreateVirtualChannels("mychan1,mychan2")
    ```

    

    For information about virtual channel naming restrictions, see [Virtual Channel Client Registration](virtual-channel-client-registration.md).

3.  Call [**IMsTscAx::Connect**](imstscax-connect.md) to create your Remote Desktop Services connection.

    ```VB
    MsRdpClient.connect
    ```

    

4.  Use the [**IMsTscAx::SendOnVirtualChannel**](imstscax-sendonvirtualchannel.md) method to send data to the server, passing a string that contains the virtual channel name and a second string that contains the data to be passed.

    ```VB
    MsRdpClient.SendOnVirtualChannel("mychan1","hello from the client")
    ```

    

5.  Receive data from the server on the [**IMsTscAxEvents::OnChannelReceivedData**](imstscaxevents-onchannelreceiveddata.md) event.

    ```VB
    Sub MsRdpClient.OnChannelReceivedData(chanName,data)
    Msgbox("received data:" &data& "on virtual channel:" &chanName)
    End sub
    ```

    

 

 




