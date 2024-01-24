---
title: Firewall Port Registry Settings
description: Firewall Port Registry Settings
ms.assetid: 86995f2c-8794-45da-9dca-9cdd388b2a21
keywords:
- Windows Media Player,firewall port registry settings
- Windows Media Player,port registry settings
- Windows Media Player,registry
- registry,firewall port settings
- registry,port settings
- registry,settings for Windows Media Player
- firewall port registry settings
- port registry settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Firewall Port Registry Settings

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player places entries in the registry so that firewalls can determine whether to open or close the ports that are used by media library sharing.

**AcceptedEULA Registry Entry**

Windows Media Player uses the following registry entry to indicate whether the user has accepted the end user license agreement (EULA).


```C++
[HKEY_LOCAL_MACHINE\Software\Microsoft\MediaPlayer\Preferences]
"AcceptedEULA" = dword:value
```



A value of 1 indicates that the user has accepted the license agreement. A value of 0 indicates that the user has not accepted the license agreement.

**WMPNSSFirewallPortsOpen Registry Entry**

Windows Media Player uses the following registry entry to indicate whether the user has chosen to share his or her media library with other computers on a home network.


```C++
[HKEY_LOCAL_MACHINE\Software\Microsoft\MediaPlayer\Preferences]
"WMPNSSFirewallPortsOpen" = dword:value
```



A value of 1 indicates that the user has chosen to share the library. A value of 0 indicates that the user has chosen not to share the library.

**Ports Related to Media Library Sharing**

On Windows Vista, if the **WMPNSSFirewallPortsOpen** registry entry has a value of 1, the following ports should be open.



| Port          | Protocol                  | Process                         | Direction            |
|---------------|---------------------------|---------------------------------|----------------------|
| 554           | TCP RTSP                  | wmpnetwk.exe                    | inbound and outbound |
| 8554 - 8558   | TCP RTSP                  | wmpnetwk.exe                    | inbound and outbound |
| 5004, 5005    | UDP RTCP/RTP              | wmpnetwk.exe                    | inbound and outbound |
| 50004 - 50013 | UDP RTCP/RTP              | wmpnetwk.exe                    | inbound and outbound |
| 1900          | UDP SSDP                  | SSDPsrv in svchost.exe          | inbound and outbound |
| 2869          | TCP SSDP, UPnP            | SSDPsrv/UPnPHost in svchost.exe | inbound              |
| 10280 - 10284 | UDP WMDRM-ND registration | wmpnetwk.exe                    | inbound and outbound |
| 10243         | TCP HTTP                  | wmpnetwk.exe                    | inbound              |
| 2177          | TCP UDP qWAVE             | svchost.exe                     | inbound and outbound |



 

On Windows Vista, if the **AcceptedEULA** registry entry has a value of 1, the following ports should be open.



| Port          | Protocol       | Process                         | Direction            |
|---------------|----------------|---------------------------------|----------------------|
| All UDP ports | UDP RTP, MSB   | wmplayer.exe, any subnet        | inbound              |
| 1900          | UDP SSDP       | SSDPsrv/UPnPHost in svchost.exe | inbound and outbound |
| 2869          | TCP SSDP, UPnP | SSDPsrv, UPnPHost               | inbound              |



 

On Microsoft Windows XP, if the **WMPNSSFirewallPortsOpen** registry entry has a value of 1, the following ports should be open.



| Port          | Protocol                  | Process                         | Direction            |
|---------------|---------------------------|---------------------------------|----------------------|
| 1900          | UDP SSDP                  | SSDPsrv in svchost.exe          | inbound and outbound |
| 2869          | TCP SSDP, UPnP            | SSDPsrv/UPnPHost in svchost.exe | inbound              |
| 10280 - 10284 | UDP WMDRM-ND registration | wmpnetwk.exe                    | inbound and outbound |
| 10243         | TCP HTTP                  | wmpnetwk.exe                    | inbound              |



 

## Related topics

<dl> <dt>

[**Registry Settings**](registry-settings.md)
</dt> </dl>

 

 




