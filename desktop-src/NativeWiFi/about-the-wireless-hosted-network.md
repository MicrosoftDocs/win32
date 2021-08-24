---
description: About the Wireless Hosted Network
ms.assetid: a6990759-9b84-4644-8f82-75aa63e8197b
title: About the Wireless Hosted Network
ms.topic: article
ms.date: 05/31/2018
---

# About the Wireless Hosted Network

The wireless Hosted Network is a new WLAN feature supported on Windows 7 and on Windows Server 2008 R2 with the Wireless LAN Service installed. This feature implements two major functions:

-   The virtualization of a physical wireless adapter into more than one virtual wireless adapter sometimes referred to as Virtual Wi-Fi.
-   A software-based wireless access point (AP) sometimes referred to as a SoftAP that uses a designated virtual wireless adapter.

These two functions coexist in a Windows system together. Enabling or disabling the wireless Hosted Network enables or disables both virtual Wi-Fi and SoftAP. It is not possible to enable or disable these two functions separately in Windows.

With this feature, a Windows computer can use a single physical wireless adapter to connect as a client to a hardware access point (AP), while at the same time acting as a software AP allowing other wireless-capable devices to connect to it. This feature requires that a Hosted Network capable wireless adapter is installed in the local computer. The driver for the wireless adapter must implement the wireless LAN device driver model defined by Microsoft for use on Windows 7. To receive the Windows 7 logo, a wireless driver must implement the wireless Hosted Network feature.

There is at most one wireless Hosted Network enabled at any time on the local computer and only one wireless adapter will be used by the wireless Hosted Network. If there is more than one Hosted Network capable wireless adapter, Windows will choose one adapter for use with the wireless Hosted Network. When the Hosted Network APIs are used, the Hosted Network capable wireless adapter is virtualized to at most 3 logical adapters:

-   A station adapter (STA) for use by client or ad hoc wireless applications. The STA adapter inherits all the settings of the original physical wireless adapter and exhibits the same behaviors as the physical adapter. Conceptually, one can view the STA adapter as identical to the physical adapter after virtualization. The STA adapter is always in the system as long as the corresponding wireless physical adapter is present.
-   An AP adapter for use by the wireless Hosted Network to host SoftAP. The AP adapter is present in the Windows system only after the wireless Hosted Network is invoked for the first time (when the [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing), [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart), or [**WlanHostedNetworkInitSettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings) function is first called). Once created, the AP adapter will remain in the system until the wireless Hosted Network is disabled. If the wireless Hosted Network is enabled at some later time, the AP adapter will show up in the system again.
-   A virtual station adapter (VSTA) for use by hardware vendors to extend the wireless Hosted Network capability in Windows. The VSTA adapter is optional and can only be created in the system by the corresponding IHV service. Unlike the AP adapter, the VSTA adapter exists in the Windows system only from the time when the IHV service initializes the adapter until the time the IHV service releases the adapter.

Virtual Wi-Fi maps the logical adapters to NDIS ports. The binding of the STA, AP, and VSTA adapters to specific NDIS ports is decided by Windows. The STA adapter is always bound to Port 0. The AP adapter is bound to the next available NDIS port when virtualization starts, and the binding remains the same until virtualization ends when wireless Hosted Network is disabled. The VSTA adapter is bound to the next available NDIS port when it is initialized by the corresponding IHV service and the binding remains the same until it is released by the IHV service.

It is possible for the VSTA adapter to be created for use by IHVs without creating the SoftAP adapter.

The following combinations are valid for a physical adapter with virtualization:

-   STA adapter.
-   STA and AP adapters.
-   STA and VSTA adapters.
-   STA, AP, and VSTA adapters.

Except for the STA adapter case, all other combinations are only valid when the wireless Hosted Network is enabled. As for the single STA adapter case, it is the physical adapter if the wireless Hosted Network is disabled. If the wireless Hosted Network is enabled, it is the STA adapter when the wireless Hosted Network has never been invoked in the system.

Layer 2 bridging is prohibited between the AP adapter and any other adapters in the system. The same restriction applies to the VSTA adapter when it is present in the system.

The wireless Hosted Network feature in Windows implements a SoftAP. However, this SoftAP is not designed to replace hardware-based wireless AP devices. In particular, if the wireless Hosted Network is running when the computer goes to sleep (standby), hibernate, or before the computer restarts, the wireless Hosted Network will be stopped. The wireless Hosted Network will not automatically restart after the computer resumes from sleep, hibernate, or restarts. In addition, SoftAP does not provide the DNS resolution. In the case where an external DNS server is not made available using Internet Connection Sharing (see the discussion of ICS below), fully qualified domain name (FQDN) resolution between any two computers or devices connected with the SoftAP, including the computer hosting the SoftAP, would only work if both entities mark the network type of the SoftAP network as PRIVATE (HOME or WORK in the network category pop-up). Since the machine hosting the SoftAP always marks the SoftAP network type as PRIVATE, only the computers or devices connected to SoftAP need to mark the SoftAP network type as PRIVATE in order for FQDN resolution to work.

SoftAP and ad hoc networking are mutually exclusive on the same physical adapter. If SoftAP is running on the AP adapter and a user or application starts ad hoc networking on the STA adapter, SoftAP will be shut down. Iif ad hoc networking is running on the STA adapter, an attempt to start SoftAP on the AP adapter will fail.

To provide protection for the wireless communications between the computer hosting SoftAP and the devices connecting to the SoftAP, the wireless Hosted Network requires that all devices connected use the WPA2-PSK/AES cipher suite. The shared key is a 63-character value generated by Windows when the wireless Hosted Network is invoked for the first time (when the [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing), [**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart), or [**WlanHostedNetworkInitSettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings) function is first called). A user or application cannot change the value of this shared key, but an application can request the operating system regenerate a new key by calling the [**WlanHostedNetworkRefreshSecuritySettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkrefreshsecuritysettings) function or a user can request the operating system regenerate a new key using **netsh wlan** commands. This shared key is called the primary or system key for the wireless Hosted Network and is persistent across starting and stopping of the wireless Hosted Network. This primary key is called the "system security key" in **netsh wlan** commands.

To allow for ease of use, wireless Hosted Network also supports the concept of a secondary or user security key that is more user-friendly, but could be less secure. This secondary key is called the "user security key" in **netsh wlan** commands. The secondary key is not generated by Windows. The user must supply the value for this key. A user or application may set or change the key value by calling the [**WlanHostedNetworkSetSecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworksetsecondarykey) function or by using the **netsh wlan** commands. The secondary key can be set to be persistent or temporary. For a temporary key, if the wireless Hosted Network is already running, the secondary key will be valid until the wireless Hosted Network stops. For a temporary key, if the wireless Hosted Network is not running, it will be valid only between the next wireless Hosted Network start and stop.

There is exactly one primary key and at most one secondary key for the wireless Hosted Hetwork on any computer. Any device provisioned through Wi-Fi Protected Setup (WPS) will receive the primary key. Other manually configured devices can have use either key. Whenever a key is changed, any device with the old key value will not be able to connect to the wireless Hosted Network without being re-provisioned with the new key. However, devices with the other unchanged key shall continue to be able to connect to the wireless Hosted Network.

An application can register for wireless Hosted Network notifications, so a WLAN notification will be sent to the application callback when properties change on the wireless Hosted Network. An application registers for wireless Hosted Network notifications by calling the [**WlanRegisterNotification**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanregisternotification) with the *dwNotifSource* parameter set to include the WLAN\_NOTIFICATION\_SOURCE\_HNWK bit.

Windows provides two ways for IT administrators to manage the wireless Hosted Network feature. For computers that are members of a domain, administrators can use group policy to disallow the wireless Hosted Network. Using **netsh wlan** commands, an administrator can enable or disable wireless Hosted Network locally on the computer.

## Supported Scenarios for Wireless Hosted Network

The wireless Hosted network enables two major scenarios for Windows computers:

• The ability to provide a wireless Personal Area Network (wireless PAN) for use with various other wireless devices.

• Network connection sharing for use by other computers and devices.

The wireless PAN is the primary scenario enabled by the wireless Hosted Network on its own. Once the wireless Hosted Network is started on a computer, any wireless-capable device supporting WPA2-PSK/AES will be able to connect to the softAP just as if it is connecting to a regular hardware AP. Devices connected to the wireless Hosted Network form a wireless PAN, where they are able to exchange information with the Windows computer hosting the SoftAP as well as among themselves.

Network connection sharing for use by other computers and devices requires the use of Internet Connection Sharing (ICS). In this scenario, the public interface of ICS is the shared connection while the private interface is the virtual adapter hosting the SoftAP. The shared connection can be an Ethernet, wireless LAN, or wireless WAN connection. In the case of a wireless LAN connection, the public interface of ICS can be either from another wireless LAN adapter or the station virtual adapter on the same physical wireless adapter that hosts the SoftAP. The most common use for network sharing is sharing an Internet connection, where the network on the public interface of ICS has access to the Internet.

The wireless Hosted Network interacts with Wi-Fi Protected Setup (WPS) , another important new feature in Windows 7 and Windows Server 2008 R2 with the Wireless LAN Service installed. The wireless Hosted Network and WPS support a scenario that provisions a WPS-capable device for a non-WPS capable hardware AP. In this case, the SoftAP hosted on Windows is invoked in the background to push the hardware AP profile onto the WPS-capable device.

## User and Application Access to Wireless Hosted Network

End users interact with the wireless Hosted Network feature in Windows using third party applications or **netsh** commands. There is currently no native user interface for configuring or managing the wireless Hosted Network on Windows 7 or on Windows Server 2008 R2 with the Wireless LAN Service installed.

Third-party applications and the **netsh** commands are based on using the public wireless Hosted Network functions. This set of functions provides a complete set of capabilities to manage the wireless Hosted Network on Windows 7 and on Windows Server 2008 R2 with the Wireless LAN Service installed.

The following is a list of the wireless Hosted Network functions and the common actions from an end user viewpoint that the function that would be used for:



| Functions used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WlanHostedNetworkForceStart_____WlanHostedNetworkStartUsing"></span><span id="wlanhostednetworkforcestart_____wlanhostednetworkstartusing"></span><span id="WLANHOSTEDNETWORKFORCESTART_____WLANHOSTEDNETWORKSTARTUSING"></span>[**WlanHostedNetworkForceStart**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestart), [**WlanHostedNetworkStartUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstartusing)<br/>                                                                                                                                                                                                                                                       | Start the wireless Hosted Network.<br/>                                                                                                                 |
| <span id="WlanHostedNetworkForceStop__WlanHostedNetworkStopUsing"></span><span id="wlanhostednetworkforcestop__wlanhostednetworkstopusing"></span><span id="WLANHOSTEDNETWORKFORCESTOP__WLANHOSTEDNETWORKSTOPUSING"></span>[**WlanHostedNetworkForceStop**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkforcestop), [**WlanHostedNetworkStopUsing**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkstopusing)<br/>                                                                                                                                                                                                                                                                          | Stop the wireless Hosted Network.<br/>                                                                                                                  |
| <span id="WlanHostedNetworkInitSettings__WlanHostedNetworkSetSecondaryKey__WlanHostedNetworkRefreshSecuritySettings"></span><span id="wlanhostednetworkinitsettings__wlanhostednetworksetsecondarykey__wlanhostednetworkrefreshsecuritysettings"></span><span id="WLANHOSTEDNETWORKINITSETTINGS__WLANHOSTEDNETWORKSETSECONDARYKEY__WLANHOSTEDNETWORKREFRESHSECURITYSETTINGS"></span>[**WlanHostedNetworkInitSettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkinitsettings), [**WlanHostedNetworkSetSecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworksetsecondarykey), [**WlanHostedNetworkRefreshSecuritySettings**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkrefreshsecuritysettings)<br/> | Configure wireless Hosted Network settings (change the SSID, change the secondary key, or request that the primary key is regenerated).<br/>            |
| <span id="WlanHostedNetworkQueryStatus__WlanHostedNetworkQuerySecondaryKey__WlanHostedNetworkQueryProperty"></span><span id="wlanhostednetworkquerystatus__wlanhostednetworkquerysecondarykey__wlanhostednetworkqueryproperty"></span><span id="WLANHOSTEDNETWORKQUERYSTATUS__WLANHOSTEDNETWORKQUERYSECONDARYKEY__WLANHOSTEDNETWORKQUERYPROPERTY"></span>[**WlanHostedNetworkQueryStatus**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerystatus), [**WlanHostedNetworkQuerySecondaryKey**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkquerysecondarykey), [**WlanHostedNetworkQueryProperty**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlanhostednetworkqueryproperty)<br/>                                              | Query the wireless Hosted Network settings and information (status, SSID, secondary key, primary key, or a list the devices currently connected ).<br/> |



 

The **netsh** commands are intended for use by advanced users or administrators.

*Netsh.exe* has many subcommands for wireless LAN. A complete list of options for **netsh** and wireless LAN is available from the command prompt by typing the following:

**netsh wlan /?**

Documentation on all of the Netsh commands for wireless LAN is also available online on Technet. For more information, please see [Netsh commands for Wireless Local Area Network (WLAN)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

The following are a few **netsh** commands commonly used with for wireless LAN and the wireless Hosted Network, although other combinations of commands are supported:



| Command                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="netsh_wlan_start_hostednetwork"></span><span id="NETSH_WLAN_START_HOSTEDNETWORK"></span>**netsh wlan start hostednetwork**<br/>                                                                                                                                                                                                                                                                                                                                     | Start the wireless Hosted Network.<br/>              |
| <span id="netsh_wlan_stop_hostednetwork"></span><span id="NETSH_WLAN_STOP_HOSTEDNETWORK"></span>**netsh wlan stop hostednetwork**<br/>                                                                                                                                                                                                                                                                                                                                        | Stop the wireless Hosted Network.<br/>               |
| <span id="netsh_wlan_set_hostednetwork__mode__allow_disallow"></span><span id="NETSH_WLAN_SET_HOSTEDNETWORK__MODE__ALLOW_DISALLOW"></span>**netsh wlan set hostednetwork \[mode=\]allow\|disallow**<br/>                                                                                                                                                                                                                                                                      | Enable or disable the wireless Hosted Network.<br/>  |
| <span id="netsh_wlan_set_hostednetwork__ssid___ssid___key___passphrase___keyUsage__persistent_temporary_"></span><span id="netsh_wlan_set_hostednetwork__ssid___ssid___key___passphrase___keyusage__persistent_temporary_"></span><span id="NETSH_WLAN_SET_HOSTEDNETWORK__SSID___SSID___KEY___PASSPHRASE___KEYUSAGE__PERSISTENT_TEMPORARY_"></span>**netsh wlan set hostednetwork \[ssid=\]&lt;ssid&gt; \[key=\]&lt;passphrase&gt; \[keyUsage=\]persistent\|temporary** <br/> | Configure the wireless Hosted Network settings.<br/> |
| <span id="netsh_wlan_refresh_hostednetwork___data___key"></span><span id="NETSH_WLAN_REFRESH_HOSTEDNETWORK___DATA___KEY"></span>**netsh wlan refresh hostednetwork \[data=\] key**<br/>                                                                                                                                                                                                                                                                                       | Refresh the wireless Hosted Network key.<br/>        |
| <span id="netsh_wlan_show_hostednetwork___setting__security_"></span><span id="NETSH_WLAN_SHOW_HOSTEDNETWORK___SETTING__SECURITY_"></span>**netsh wlan show hostednetwork \[\[setting=\]security\]**<br/>                                                                                                                                                                                                                                                                     | Display wireless Hosted Network information.<br/>    |
| <span id="netsh_wlan_show_settings"></span><span id="NETSH_WLAN_SHOW_SETTINGS"></span>**netsh wlan show settings**<br/>                                                                                                                                                                                                                                                                                                                                                       | Display wireless LAN global settings.<br/>           |



 

## Related topics

<dl> <dt>

[Using Wireless Hosted Network and Internet Connection Sharing](using-hosted-network-and-internet-connection-sharing.md)
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

 

 
