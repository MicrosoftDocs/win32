---
title: What's New in Windows Server 2008
description: Windows Server 2008 introduces the following new programming elements for Terminal Services.
ms.assetid: a2299b03-5e06-4984-a33f-b44c7cded513
ms.tgt_platform: multiple
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
<li><a href="dynamic-virtual-channels">Dynamic Virtual Channels</a></li>
<li><a href="dynamic-virtual-channels-reference">Dynamic Virtual Channels Reference</a></li>
</ul></td>
</tr>
<tr class="even">
<td>Remote Desktop Web Connection Reference<br/></td>
<td>The following interfaces (and their associated methods and properties) were added to <a href="remote-desktop-web-connection-reference">Remote Desktop Web Connection Reference</a>:<br/>
<ul>
<li><a href="imsrdpclient5"><strong>IMsRdpClient5 Interface</strong></a></li>
<li><a href="imsrdpclient6"><strong>IMsRdpClient6 Interface</strong></a></li>
<li><a href="imsrdpclientadvancedsettings5"><strong>IMsRdpClientAdvancedSettings5 Interface</strong></a></li>
<li><a href="imsrdpclientadvancedsettings6"><strong>IMsRdpClientAdvancedSettings6 Interface</strong></a></li>
<li><a href="imsrdpclientnonscriptable3"><strong>IMsRdpClientNonScriptable3 Interface</strong></a></li>
<li><a href="imsrdpclientshell"><strong>IMsRdpClientShell Interface</strong></a></li>
<li><a href="imsrdpclienttransportsettings"><strong>IMsRdpClientTransportSettings Interface</strong></a></li>
<li><a href="imsrdpclienttransportsettings2"><strong>IMsRdpClientTransportSettings2 Interface</strong></a></li>
<li><a href="imsrdpdevice"><strong>IMsRdpDevice Interface</strong></a></li>
<li><a href="imsrdpdevicecollection"><strong>IMsRdpDeviceCollection Interface</strong></a></li>
<li><a href="imsrdpdrive"><strong>IMsRdpDrive Interface</strong></a></li>
<li><a href="imsrdpdrivecollection"><strong>IMsRdpDriveCollection Interface</strong></a></li>
<li><a href="itsremoteprogram"><strong>ITSRemoteProgram Interface</strong></a></li>
</ul></td>
</tr>
<tr class="odd">
<td>Terminal Services API Reference<br/></td>
<td>The following functions were added to <a href="terminal-services-api-reference">Terminal Services API Reference</a>:<br/>
<ul>
<li><a href="/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsconnectsessiona"><strong>WTSConnectSession Function</strong></a></li>
<li><a href="/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsregistersessionnotificationex"><strong>WTSRegisterSessionNotificationEx Function</strong></a></li>
<li><a href="/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsstartremotecontrolsessiona"><strong>WTSStartRemoteControlSession Function</strong></a></li>
<li><a href="/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsstopremotecontrolsession"><strong>WTSStopRemoteControlSession Function</strong></a></li>
<li><a href="/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsunregistersessionnotificationex"><strong>WTSUnRegisterSessionNotificationEx Function</strong></a></li>
<li><a href="/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopenex"><strong>WTSVirtualChannelOpenEx Function</strong></a></li>
</ul>
The following structures were added:<br/>
<ul>
<li><a href="/windows/desktop/api/Wtsapi32/ns-wtsapi32-_wtsclienta"><strong>WTSCLIENT Structure</strong></a></li>
<li><a href="/windows/desktop/api/Wtsapi32/ns-wtsapi32-_wtsinfoa"><strong>WTSINFO Structure</strong></a></li>
</ul></td>
</tr>
<tr class="even">
<td>Terminal Services WMI Provider<br/></td>
<td>The following classes and methods were added to the <a href="terminal-services-wmi-provider">Terminal Services WMI Provider</a>.<br/>
<ul>
<li><a href="terminal-services-gateway-classes">Terminal Services Gateway Classes (and associated methods)</a></li>
<li><a href="terminal-services-license-server-classes">Terminal Services License Server Classes (and associated methods)</a></li>
<li><a href="terminal-services-remoteapp-classes">RemoteApp Classes (and associated methods)</a></li>
<li><a href="win32-tsdiscoveredlicenseserver"><strong>Win32_TSDiscoveredLicenseServer Class</strong></a></li>
<li><a href="create-win32-terminal"><strong>Create Method of the Win32_Terminal Class</strong></a></li>
<li><a href="delete-win32-terminal"><strong>Delete Method of the Win32_Terminal Class</strong></a></li>
<li><a href="canaccesslicenseserver-win32-terminalservicesetting"><strong>CanAccessLicenseServer Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="findlicenseservers-win32-terminalservicesetting"><strong>FindLicenseServers Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="getdomain-win32-terminalservicesetting"><strong>GetDomain Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="getgraceperioddays-win32-terminalservicesetting"><strong>GetGracePeriodDays Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="getwinstationdrivernames-win32-terminalservicesetting"><strong>GetWinstationDriverNames Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="pinglicenseserver-win32-terminalservicesetting"><strong>PingLicenseServer Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="updatedirectconnectlicenseserver-win32-terminalservicesetting"><strong>UpdateDirectConnectLicenseServer Method of the Win32_TerminalServiceSetting Class</strong></a></li>
<li><a href="setuserauthenticationrequired-win32-tsgeneralsetting"><strong>SetUserAuthenticationRequired Method of the Win32_TSGeneralSetting Class</strong></a></li>
<li><a href="getcurrentredirectableaddresses-win32-tssessiondirectory"><strong>GetCurrentRedirectableAddresses Method of the Win32_TSSessionDirectory Class</strong></a></li>
<li><a href="setcurrentredirectableaddresses-win32-tssessiondirectory"><strong>SetCurrentRedirectableAddresses Method of the Win32_TSSessionDirectory Class</strong></a></li>
<li><a href="getredirectableaddresses-win32-tssessiondirectory"><strong>GetRedirectableAddresses Method of the Win32_TSSessionDirectory Class</strong></a></li>
<li><a href="pingsessiondirectory-win32-tssessiondirectory"><strong>PingSessionDirectory Method of the Win32_TSSessionDirectory Class</strong></a></li>
<li><a href="setloadbalancingstate-win32-tssessiondirectory"><strong>SetLoadBalancingState Method of the Win32_TSSessionDirectory Class</strong></a></li>
<li><a href="setserverweight-win32-tssessiondirectory"><strong>SetServerWeight Method of the Win32_TSSessionDirectory Class</strong></a></li>
</ul></td>
</tr>
<tr class="odd">
<td>Terminal Services Session Broker Plug-in Reference<br/></td>
<td>The Terminal Services Session Broker (TS Session Broker) plug-in is used to extend the capabilities of TS Session Broker.<br/>
<ul>
<li><a href="https://docs.microsoft.com/windows/desktop/TermServ/terminal-services-virtualization-api-reference">Terminal Services Session Broker Plug-in Reference</a></li>
</ul></td>
</tr>
</tbody>
</table>



 

 

 





