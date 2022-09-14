---
title: Creating Hardware Event Subscriptions
description: On computers that have a Baseboard Management Controller (BMC) installed, hardware events are raised and logged in the System event log (SEL), which is the BMC event store that is stored in nonvolatile memory.
ms.assetid: 646ab546-500e-44ee-8b08-2f835e57e3e6
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Creating Hardware Event Subscriptions

On computers that have a Baseboard Management Controller (BMC) installed, hardware events are raised and logged in the System event log (SEL), which is the BMC event store that is stored in nonvolatile memory. To read these hardware events on Windows Server 2008 using the Event Viewer, you must create a subscription to the events. The hardware event subscriptions will only work on Windows Server 2008.

The following procedure defines how to create the SEL event subscription to retrieve the hardware events:

1.  Save the following XML in an .xml file (in this example the file is named Wsmanselrg.xml). This XML defines the subscription.

    ```XML
    <Subscription xmlns="http://schemas.microsoft.com/2006/03/windows/events/subscription">
        <Description>A subscription for the HardwareEvents</Description>
        <SubscriptionId>WSManSelRg</SubscriptionId>
        <Uri>http://schemas.microsoft.com/wbem/wsman/1/logrecord/sel</Uri>
        <EventSources>
            <EventSource>
                <Address>LOCALHOST</Address>
            </EventSource>
        </EventSources>
        <LogFile>HardwareEvents</LogFile>
        <Delivery Mode="pull">
            <PushSettings>
                <Heartbeat Interval="10000"/>
            </PushSettings>
        </Delivery>
    </Subscription>
    ```

    

2.  Create an event subscription by executing the following command in a command prompt window (the Wecutil.exe program is located in the %SYSTEMROOT%\\System32 directory.):

    **Wecutil cs** *&lt;path&gt;\\wsmanselrg.xml*

3.  Ensure that the subscription is active by executing the following command in a command prompt window:

    **Wecutil gr** *wsmanselrg*

The BMC is a microcontroller attached locally to a server. BMCs have sensors that monitor the physical state of the server and a separate network connection that can communicate over the network, even if the server is offline. You have access to BMC data through the Intelligent Platform Management Interface (IPMI) WMI Provider. For more information about the IPMI provider, see [IPMI Provider](/previous-versions/windows/desktop/ipmiprv/ipmi-provider).

The computer must have the BMC and the IPMI provider installed for the event subscription to work. For computers running on Windows Server 2008, the IPMI provider is installed by default. If the BMC is not available, then IPMI driver cannot be installed and the subscription runtime status will always display an error (0x8004001 - WMI Generic Failure).

 

 
