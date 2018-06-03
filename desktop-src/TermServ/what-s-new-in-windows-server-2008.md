---
title: What's New in Windows Server 2008
description: Windows Server 2008 introduces the following new programming elements for Terminal Services.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2299b03-5e06-4984-a33f-b44c7cded513
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows Server 2008

Windows Server 2008 introduces the following new programming elements for Terminal Services.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Programming element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Dynamic Virtual Channels Reference<br/></td>
<td>Dynamic virtual channel (DVC) APIs extend the existing virtual channel APIs for Terminal Services, known as static virtual channel (SVC) APIs.<br/>
<ul>
<li>[Dynamic Virtual Channels](dynamic-virtual-channels.md)</li>
<li>[Dynamic Virtual Channels Reference](dynamic-virtual-channels-reference.md)</li>
</ul></td>
</tr>
<tr class="even">
<td>Remote Desktop Web Connection Reference<br/></td>
<td>The following interfaces (and their associated methods and properties) were added to [Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md):<br/>
<ul>
<li>[<strong>IMsRdpClient5 Interface</strong>](imsrdpclient5.md)</li>
<li>[<strong>IMsRdpClient6 Interface</strong>](imsrdpclient6.md)</li>
<li>[<strong>IMsRdpClientAdvancedSettings5 Interface</strong>](imsrdpclientadvancedsettings5.md)</li>
<li>[<strong>IMsRdpClientAdvancedSettings6 Interface</strong>](imsrdpclientadvancedsettings6.md)</li>
<li>[<strong>IMsRdpClientNonScriptable3 Interface</strong>](imsrdpclientnonscriptable3.md)</li>
<li>[<strong>IMsRdpClientShell Interface</strong>](imsrdpclientshell.md)</li>
<li>[<strong>IMsRdpClientTransportSettings Interface</strong>](imsrdpclienttransportsettings.md)</li>
<li>[<strong>IMsRdpClientTransportSettings2 Interface</strong>](imsrdpclienttransportsettings2.md)</li>
<li>[<strong>IMsRdpDevice Interface</strong>](imsrdpdevice.md)</li>
<li>[<strong>IMsRdpDeviceCollection Interface</strong>](imsrdpdevicecollection.md)</li>
<li>[<strong>IMsRdpDrive Interface</strong>](imsrdpdrive.md)</li>
<li>[<strong>IMsRdpDriveCollection Interface</strong>](imsrdpdrivecollection.md)</li>
<li>[<strong>ITSRemoteProgram Interface</strong>](itsremoteprogram.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Terminal Services API Reference<br/></td>
<td>The following functions were added to [Terminal Services API Reference](terminal-services-api-reference.md):<br/>
<ul>
<li>[<strong>WTSConnectSession Function</strong>](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsconnectsessiona)</li>
<li>[<strong>WTSRegisterSessionNotificationEx Function</strong>](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsregistersessionnotificationex)</li>
<li>[<strong>WTSStartRemoteControlSession Function</strong>](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsstartremotecontrolsessiona)</li>
<li>[<strong>WTSStopRemoteControlSession Function</strong>](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsstopremotecontrolsession)</li>
<li>[<strong>WTSUnRegisterSessionNotificationEx Function</strong>](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsunregistersessionnotificationex)</li>
<li>[<strong>WTSVirtualChannelOpenEx Function</strong>](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopenex)</li>
</ul>
The following structures were added:<br/>
<ul>
<li>[<strong>WTSCLIENT Structure</strong>](/windows/desktop/api/Wtsapi32/ns-wtsapi32-_wtsclienta)</li>
<li>[<strong>WTSINFO Structure</strong>](/windows/desktop/api/Wtsapi32/ns-wtsapi32-_wtsinfoa)</li>
</ul></td>
</tr>
<tr class="even">
<td>Terminal Services WMI Provider<br/></td>
<td>The following classes and methods were added to the [Terminal Services WMI Provider](terminal-services-wmi-provider.md).<br/>
<ul>
<li>[Terminal Services Gateway Classes (and associated methods)](terminal-services-gateway-classes.md)</li>
<li>[Terminal Services License Server Classes (and associated methods)](terminal-services-license-server-classes.md)</li>
<li>[RemoteApp Classes (and associated methods)](terminal-services-remoteapp-classes.md)</li>
<li>[<strong>Win32_TSDiscoveredLicenseServer Class</strong>](win32-tsdiscoveredlicenseserver.md)</li>
<li>[<strong>Create Method of the Win32_Terminal Class</strong>](create-win32-terminal.md)</li>
<li>[<strong>Delete Method of the Win32_Terminal Class</strong>](delete-win32-terminal.md)</li>
<li>[<strong>CanAccessLicenseServer Method of the Win32_TerminalServiceSetting Class</strong>](canaccesslicenseserver-win32-terminalservicesetting.md)</li>
<li>[<strong>FindLicenseServers Method of the Win32_TerminalServiceSetting Class</strong>](findlicenseservers-win32-terminalservicesetting.md)</li>
<li>[<strong>GetDomain Method of the Win32_TerminalServiceSetting Class</strong>](getdomain-win32-terminalservicesetting.md)</li>
<li>[<strong>GetGracePeriodDays Method of the Win32_TerminalServiceSetting Class</strong>](getgraceperioddays-win32-terminalservicesetting.md)</li>
<li>[<strong>GetWinstationDriverNames Method of the Win32_TerminalServiceSetting Class</strong>](getwinstationdrivernames-win32-terminalservicesetting.md)</li>
<li>[<strong>PingLicenseServer Method of the Win32_TerminalServiceSetting Class</strong>](pinglicenseserver-win32-terminalservicesetting.md)</li>
<li>[<strong>UpdateDirectConnectLicenseServer Method of the Win32_TerminalServiceSetting Class</strong>](updatedirectconnectlicenseserver-win32-terminalservicesetting.md)</li>
<li>[<strong>SetUserAuthenticationRequired Method of the Win32_TSGeneralSetting Class</strong>](setuserauthenticationrequired-win32-tsgeneralsetting.md)</li>
<li>[<strong>GetCurrentRedirectableAddresses Method of the Win32_TSSessionDirectory Class</strong>](getcurrentredirectableaddresses-win32-tssessiondirectory.md)</li>
<li>[<strong>SetCurrentRedirectableAddresses Method of the Win32_TSSessionDirectory Class</strong>](setcurrentredirectableaddresses-win32-tssessiondirectory.md)</li>
<li>[<strong>GetRedirectableAddresses Method of the Win32_TSSessionDirectory Class</strong>](getredirectableaddresses-win32-tssessiondirectory.md)</li>
<li>[<strong>PingSessionDirectory Method of the Win32_TSSessionDirectory Class</strong>](pingsessiondirectory-win32-tssessiondirectory.md)</li>
<li>[<strong>SetLoadBalancingState Method of the Win32_TSSessionDirectory Class</strong>](setloadbalancingstate-win32-tssessiondirectory.md)</li>
<li>[<strong>SetServerWeight Method of the Win32_TSSessionDirectory Class</strong>](setserverweight-win32-tssessiondirectory.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td>Terminal Services Session Broker Plug-in Reference<br/></td>
<td>The Terminal Services Session Broker (TS Session Broker) plug-in is used to extend the capabilities of TS Session Broker.<br/>
<ul>
<li>[Terminal Services Session Broker Plug-in Reference](https://msdn.microsoft.com/library/dd379710)</li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 





