---
title: Use Wireless Hosted Network, Internet Connection Sharing
description: Using Wireless Hosted Network and Internet Connection Sharing
ms.assetid: 56e86ef8-f759-4e56-a591-74e03430125a
ms.topic: article
ms.date: 05/31/2018
---

# Use Wireless Hosted Network, Internet Connection Sharing

The Wireless Hosted Network is a new WLAN feature supported on Windows 7 and Windows 8. It is also supported on Windows Server 2012 and Windows Server 2008 R2 with the Wireless LAN Service installed. This feature implements two major functions:

-   The virtualization of a physical wireless adapter into more than one virtual wireless adapter sometimes referred to as Virtual Wi-Fi.
-   A software-based wireless access point (AP) sometimes referred to as a SoftAP that uses a designated virtual wireless adapter.

Internet Connection Sharing (ICS) is a feature in Windows provided through the SharedAccess Service. Strictly speaking, SharedAccess enables network sharing through a computer where the shared network access does not necessarily provide access to the Internet. We use the term ICS and SharedAccess interchangeably in this section, since Internet Connection Sharing is a major scenario for the wireless Hosted Network and the ICS term is better known to the user community.

Wireless Hosted Network is closely tied to ICS to enable both the wireless personal area network (PAN) and the Internet sharing scenarios. This section provides general recommendations to application developers on how to integrate wireless Hosted Network and ICS using the public wireless Hosted Network and ICS APIs.

## Internet Connection Sharing

The ICS Service operates in one of the two possible modes:

-   Standalone mode

    Only the DHCPv4 server function is operating when the ICS service is invoked. This is a special operation mode for ICS and is only made available through the wireless Hosted Network. A user or application is not able to directly start and stop standalone ICS through public ICS APIs or **netsh** commands. Starting the wireless Hosted Network typically involves starting ICS in standalone mode to use the DHCPv4 server function to provide private IPv4 addresses for connected devices. Network communication for the connected devices is limited to sending and receiving network packets between a connected device and the local computer hosting the wireless Hosted Network and among the connected devices themselves. This effectively enables the wireless personal area network scenario for the wireless Hosted Network.

-   Full mode

    All the features of ICS are operating when the service is invoked, such as network address translation and DHCP server functions for both IPv4 and IPv6. This is the normal mode of operation for ICS. A user or application may start and stop full ICS mode through public APIs or netshell commands. For example, this service can be stopped using net stop sharedaccess from an elevated command prompt. Combining wireless Hosted Network with full ICS, Network communication for the connected devices is not limited to the wireless PAN. Any connected device has access to network (such as the Internet) through the shared network connection from the computer running the wireless Hosted Network. This effectively enables the Network sharing scenario for the wireless Hosted Network.

In this section, we use the term full ICS to mean the case where all the ICS functions are invoked in ICS Service to provide access to all the full ICS features with the wireless Hosted Network.

The two ICS operation modes are mutually exclusive with full ICS taking higher precedence. The ICS Service may transition from standalone mode to full mode, but not from full mode to standalone mode. The ICS standalone mode was introduced in Windows 7 and on Windows Server 2008 R2 with the Wireless LAN Service installed in conjunction with the wireless Hosted Network feature. It is not available in previous versions of Windows.

Any full ICS operation involves two different network adapters in the system:

-   The public interface. This is the network interface with access to the Internet. It is this interface that the local computer running ICS uses to share the Internet with clients and devices connecting to it via SoftAP.
-   The private interface. This is the network interface that other devices use to connect to the local computer that is running ICS. A DHCPv4 server is running on this private interface to provide private local IP addresses to the other remote computers.

When the public interface does not have Internet access, the DHCP server on the private interface continues to provide local IP addresses to the connected devices. Standalone ICS only involves the private interface on which SoftAP is running; it does not involve any public interface.

At any time, there is at most one instance of full ICS running on the local computer. If full ICS is already running on the local computer, starting another full ICS exhibits the following functional behaviors:

-   If the public and private interfaces of the new full ICS are the same as the existing full ICS, starting the second full ICS is equivalent to a no-op.
-   If the new public interface is different from the old public interface, but the new private interface is the same as the old private interface, starting a second full ICS has little impact on the connected devices on the same private interface. The ability to access the Internet may change with the new public interface.
-   If the new private interface is different than the old private interface, ICS functions will stop working on the old private interface and start applying to the new private interface. Any remote device connecting to the local computer using the old private interface will lose IP connectivity to the local computer.

When full ICS is already running, invoking a second full ICS is disruptive to remotely connected devices using the old private interface as long as the second ICS integration uses a different new private interface.

To manage and use the ICS service to support ICS integration with wireless Hosted Network, a software application must first obtain an [**INetSharingManager**](/windows/win32/api/netcon/nn-netcon-inetsharingmanager) interface. The **INetSharingManager** interface provides access directly or indirectly to all the other COM interfaces in the ICS API. The [**get\_SharingInstalled**](/windows/win32/api/netcon/nf-netcon-inetsharingmanager-get_sharinginstalled) method on the **INetSharingManager** interface reports whether the local computer supports connection sharing. The [**get\_EnumEveryConnection**](/windows/win32/api/netcon/nf-netcon-inetsharingmanager-get_enumeveryconnection) method on the **INetSharingManager** interface retrieves an enumeration interface for all connections in the connections folder. The [**get\_INetSharingConfigurationForINetConnection**](/windows/win32/api/netcon/nf-netcon-inetsharingmanager-get_inetsharingconfigurationforinetconnection) method retrieves an [**INetSharingConfiguration**](/windows/win32/api/netcon/nn-netcon-inetsharingconfiguration) interface for the specified connection. Methods on the **INetSharingConfiguration** interface can be used to query and change ICS settings.

The wireless Hosted Network must be started before calling the [**get\_EnumEveryConnection**](/windows/win32/api/netcon/nf-netcon-inetsharingmanager-get_enumeveryconnection) method on the [**INetSharingManager**](/windows/win32/api/netcon/nn-netcon-inetsharingmanager) interface to enumerate all connections in the connections folder.

For information on ICS and the public interfaces and methods that can be used to query and change ICS settings, please see the documentation on [About Internet Connection Sharing and Internet Connection Firewall](/previous-versions/windows/desktop/ics/about-internet-connection-sharing-and-internet-connection-firewall).

## Hosted Network and ICS Integration

When full ICS is not running, starting a wireless Hosted Network also internally starts the ICS Service in standalone mode with only the DHCPv4 server function to allocate IP addresses for the connected devices on the wireless Hosted Network interface. The subnet address range for the standalone DHCPv4 server is 192.168.173.0/24. This is different from the subnet range of 192.168.137.0/24 that is used with full ICS.

Starting a wireless Hosted Network with full ICS employs the following logic:

-   If full ICS is not already running, starting a wireless Hosted Network also starts the ICS Service with standalone DHCPv4 server.
-   If full ICS is already running and the private interface is the wireless Hosted Network interface, just start the wireless Hosted Network.
-   If full ICS is already running but the private interface is not the wireless Hosted Network interface, the wireless Hosted Network will be started without the DHCPv4 server function on the wireless Hosted Network interface.

The impact of the logic above highlights the following facts:

-   ICS does not transition from full mode to standalone mode.
-   Standalone mode can only be invoked by the wireless Hosted Network when ICS is not running in full mode.
-   If ICS is running in standalone mode, it will be preempted into full mode if a user or application starts ICS in full mode.
-   Transitioning from standalone mode to full mode in ICS will be disruptive to connected devices in the wireless PAN if the private interface of full ICS is not the same as the one for SoftAP.

It takes time to start or stop the ICS Service on the local computer in either full or standalone mode. An application should check the state of ICS Service using the **NotifyServiceStatusChange** function to make sure that the ICS Service is not in the start/stop pending state before starting or stopping the wireless Hosted Network for use with ICS integration.

## Starting and Stopping the Wireless Hosted Network

Windows provides a platform where more than one concurrent application is allowed to manage a wireless Hosted Network at the same time. Specifically each application can start and stop the wireless Hosted Network on its own, without prior knowledge about other applications.

There are two sets of functions to start and stop a Hosted Network.

Multiple applications may require the use of the wireless Hosted Network. The [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing) and [**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing) functions start and stop a wireless Hosted Network in a way that is compatible with other concurrent applications. The **WlanHostedNetworkStartUsing** and **WlanHostedNetworkStopUsing** functions allow an application to have a reference to the wireless Hosted Network. This mechanism keeps the wireless Hosted Network running provided that at least one other application has a current reference to the wireless Hosted Network. Any user can call these functions. Successful calls to **WlanHostedNetworkStartUsing** must be matched by calls to the **WlanHostedNetworkStopUsing** function. Any Hosted Network state change caused by the **WlanHostedNetworkStartUsing** function would be automatically undone if the calling application closes its calling handle (by calling [**WlanCloseHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanclosehandle) with the same *hClientHandle* parameter passed to **WlanHostedNetworkStartUsing**) or if the process ends.

The [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart) and [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) functions force start and stop a wireless Hosted Network. These functions can only be called if the user has the appropriate elevated privilege. Successful calls to **WlanHostedNetworkForceStart** may eventually be matched by a call to the **WlanHostedNetworkForceStop** function, depending on the application design. These functions transition the wireless Hosted Network state without associating the request with the application's calling handle. Any Hosted Network state change caused by the **WlanHostedNetworkForceStart** function would not be automatically undone if the calling application closes its calling handle (by calling [**WlanCloseHandle**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanclosehandle) with the same *hClientHandle* parameter passed to [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing)) or if the process ends. If the application that called the **WlanHostedNetworkForceStart** function closes without calling one of the functions to stop the wireless Hosted Network, then Hosted Network is left running. An application might call the **WlanHostedNetworkForceStart** function after ensuring that an elevated system user accepts the increased power requirements involved in running the wireless Hosted Network for extended periods of time.

The general recommendations on which functions to call to start and stop a wireless Hosted Network are as follows:

-   Use the [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing) and [**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing) functions within an application to start and stop a wireless Hosted Network.
-   Do not use the [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart) function to start a wireless Hosted Network unless it is absolutely required by the application. The **WlanHostedNetworkForceStart** function also requires elevated privileges.
-   Only use the [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function as a recovery method. The **WlanHostedNetworkForceStop** function causes a wireless Hosted Network to stop immediately. Other applications that listen for wireless Hosted Network notifications may need to take recovery actions. For more information, see the discussion below on the recovery sequence for wireless Hosted Network.

## Start Sequence for Wireless Hosted Network

For an application that starts a wireless Hosted Network with full ICS, the recommendation is to start the wireless Hosted Network, then start full ICS. If a wireless Hosted Network is already running, an application should use the [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function to stop the wireless Hosted Network only if full ICS is required but has not been enabled before the Hosted Network was started. This will allow other applications to recover from potential disruptions caused by the start of full ICS. For more information, see the discussion below on the recovery sequence for wireless Hosted Network. The combined operation should succeed and fail as a whole.

> [!Note]  
> The wireless Hosted Network must be started before attempting to enumerate the corresponding adapter using the [**IEnumNetSharingEveryConnection**](/windows/win32/api/netcon/nn-netcon-ienumnetsharingeveryconnection) interface.

 

The following ordered steps are the recommended start sequence in an application using wireless Hosted Network with full ICS:

-   Call the [**WlanHostedNetworkInitSettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings) function to make sure wireless Hosted Network is configured and ready to be used.
-   Call the [**WlanHostedNetworkQueryStatus**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerystatus) and [**WlanHostedNetworkQueryProperty**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkqueryproperty) functions to determine if the wireless Hosted Network is allowed and available. If the wireless Hosted Network is not allowed and not available, return an error.
-   Test to see if the ICS Service used for full ICS is allowed. If the ICS service cannot be started, return an error.
-   Call the [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function to force a stop of the wireless Hosted Network.
-   Call the [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing) function to start the wireless Hosted Network.
-   If the wireless Hosted Network fails to start, return an error.
-   If full ICS is already running and the current public or private interface is different from the new interface to be used, cache the current public and private interfaces. An application may also choose to return an error or prompt the user if ICS integration is already running.
-   Start full ICS with the new settings for the public and private interfaces.
-   If full ICS fails to start with these settings, try to start full ICS service with the cached public and private interfaces if full ICS was running before. Call the [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function to stop the wireless Hosted Network and return an error.
-   Return success that the wireless Hosted Network and full ICS succeed.

## Stop Sequence for Wireless Hosted Network

When using wireless Hosted Network with full ICS, an application that has finished its work may want to stop the wireless Hosted Network and the ICS service used for full ICS. In this case, it is recommended that the [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function be called to stop the Hosted Network rather than calling the [**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing) function. The **WlanHostedNetworkForceStop** function stops the wireless Hosted Network and also serves to allow other applications to recover. For more information, see the discussion below on the recovery sequence for wireless Hosted Network.

The following ordered steps are the recommended stop sequence in an application using wireless Hosted Network and full ICS:

-   Stop full ICS.
-   Call the [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function to stop the wireless Hosted Network.

An application using wireless Hosted Network without full ICS that is finished with its work just needs to call the [**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing) or [**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop) function to stop the wireless Hosted Network. If the [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing) function was called to start the wireless Hosted Network, then the application should call the **WlanHostedNetworkStopUsing** function to stop the wireless Hosted Network. If the wireless Hosted Network was was already started before the application or the application called the [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart) function to force start the wireless Hosted Network, then the application can call the **WlanHostedNetworkForceStop** function to stop the wireless Hosted Network or do nothing (leave wireless Hosted Network started) depending on the scenario.

## Recovery Sequence for Wireless Hosted Network

An application using the wireless Hosted Network may be affected by the actions of other applications. The ICS service and the interfaces for managing ICS provide no method for an application to register for ICS change notifications. If another application calls the [**EnableSharing**](/windows/win32/api/netcon/nf-netcon-inetsharingconfiguration-enablesharing) or the [**DisableSharing**](/windows/win32/api/netcon/nf-netcon-inetsharingconfiguration-disablesharing) methods on the [**INetSharingConfiguration**](/windows/win32/api/netcon/nn-netcon-inetsharingconfiguration) interface to enable or disable sharing on a connection, a message is sent to the user interface (the screen) on the local computer not to other applications. So an application needs to rely on the wireless Hosted Network notifications to perform recovery actions when ICS or wireless Hosted Network changes occur.

An application using the wireless Hosted Network should register for wireless Hosted Network notifications by calling the [**WlanRegisterNotification**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanregisternotification). If notifications for only wireless Hosted Network are needed, then the application should pass **WLAN\_NOTIFICATION\_SOURCE\_HNWK** in the *dwNotifSource* parameter passed to the **WlanRegisterNotification**. If other wireless notications are also needed, then **WLAN\_NOTIFICATION\_SOURCE\_HNWK** should be combined with the notification source constants for other types of wireless notifications desired and pass this value in the *dwNotifSource* parameter.

The recovery sequence is the same for applications with or without full ICS, assuming that applications don’t want to start ICS service again. Upon receiving a wireless Hosted Network notification that the Hosted Network has stopped, do the following:

-   If the application called [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart) to start the wireless Hosted Network, then restart the Hosted Network by calling **WlanHostedNetworkForceStart**. Otherwise, call [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing) to restart the wireless Hosted Network.

## Recovery Sequence for Connected Devices

Remote devices or computers connected to the wireless Hosted Network may be affected by the actions of other applications that impact ICS and the wireless Hosted Network. Fortunately, most devices have built in retry logic in the device application to deal with a temporary loss of signal or roaming.

A possible recovery sequence for devices or computers connected to the wireless Hosted Network that lose contact is the following:

-   The wireless device driver indicates a media disconnect to the upper layers of the network stack on the device.
-   The device application starts periodic checks for the availability of the wireless Hosted Network.
-   Once the device application again detects the wireless Hosted Network, the device initiates a wireless connection.
-   Upon a successful connection with the wireless Hosted Network, the device application updates its IP settings accordingly.

## Related topics

<dl> <dt>

[About the Wireless Hosted Network](about-the-wireless-hosted-network.md)
</dt> <dt>

[Wireless Hosted Network Sample](wireless-hosted-network-sample.md)
</dt> <dt>

[**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart)
</dt> <dt>

[**WlanHostedNetworkInitSettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings)
</dt> <dt>

[**WlanHostedNetworkQueryProperty**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkqueryproperty)
</dt> <dt>

[**WlanHostedNetworkQuerySecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerysecondarykey)
</dt> <dt>

[**WlanHostedNetworkQueryStatus**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerystatus)
</dt> <dt>

[**WlanHostedNetworkRefreshSecuritySettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkrefreshsecuritysettings)
</dt> <dt>

[**WlanHostedNetworkSetProperty**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworksetproperty)
</dt> <dt>

[**WlanHostedNetworkSetSecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworksetsecondarykey)
</dt> <dt>

[**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing)
</dt> <dt>

[**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing)
</dt> <dt>

[**WlanRegisterVirtualStationNotification**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanregistervirtualstationnotification)
</dt> </dl>

 

 
