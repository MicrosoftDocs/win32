---
description: Learn about TLS 1.0 and TLS 1.1 deprecation in Windows and how to enable compatibility support for legacy TLS.
title: TLS 1.0 and TLS 1.1 deprecation in Windows
ms.author: alalve
ms.topic: article
ms.date: 01/16/2024
ms.contributor: jekrynit
---

# TLS 1.0 and TLS 1.1 deprecation in Windows

The internet standards and regulatory bodies have deprecated or disallowed TLS versions 1.0 and 1.1 due to several security issues. Starting with Windows 11 Insider Preview releases in 2024, they will be disabled by default. This change applies to both server and client devices but won't impact in-market Operating System versions.

TLS 1.0 and TLS 1.1 have already been disabled by Microsoft 365 products as well as WinHTTP and WinINet API surfaces. Most newer versions of applications support TLS 1.2 or higher protocol versions. Therefore, if an application starts failing after this change, the first step is to look for a newer version of the application that has TLS 1.2 or TLS 1.3 support.

To learn more about this deprecation, see [RFC 8996](https://www.ietf.org/rfc/rfc8996.html).

## Reenable TLS 1.0 and TLS 1.1 for legacy compatibility

Best practice is to check for an updated application version before re-enabling legacy TLS versions.

> [!NOTE]
> Re-enabling TLS 1.0 or TLS 1.1 on devices is a temporary solution until incompatible applications can be updated or replaced. Support for these legacy TLS versions may be removed completely in the future.

You can enable TLS 1.0 or TLS 1.1 using the registry editor (regedit.exe), the command prompt (CMD), or PowerShell. When editing the registry, an entry with a value of **0** is the same as **disabled** and a value of **1** is the same as **enabled**. The registry path for these entries are stored in:

```registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client
```

# [Registry Editor](#tab/registry-editor)

To override a system default, follow these steps to enable TLS 1.0 or TLS 1.1 on either the server or client device:

1. On your desktop, select **Start**, type **Registry Editor**, right-click on **Registry Editor** and select **Run as administrator**.
1. In the **Registry Editor**, navigate to the TLS path you want to edit previously referenced.
1. In the top pane, select **Edit** > **New** > **DWORD** > type **Enabled**, then hit **Enter**.
1. Double-click on your **Enabled** registry entry, change the value to **1**, then select **OK**.

# [Command Prompt](#tab/command-promt)

To enable TLS 1.0 for server using the command prompt or Windows Terminal, run the following as admin:

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server" /v "Enabled" /t REG_DWORD /d 1 /f
```

To enable TLS 1.0 for client using the command prompt or Windows Terminal, run the following as admin:

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client" /v "Enabled" /t REG_DWORD /d 1 /f
```

# [PowerShell](#tab/powershell)

To enable TLS 1.0 for server using PowerShell, run the following as admin:

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server" -Name "Enabled" -Value 1
```

To enable TLS 1.0 for client using PowerShell, run the following as admin:

```powershell
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client" -Name "Enabled" -Value 1
```

---

## Known issues

The following Windows applications rely on TLS 1.0 or TLS 1.1 and are expected to fail or lose some functionality.

> [!NOTE]
> The provided list is not exhaustive. If other applications show issues, check with the software vendor for an updated version or leave feedback under "Network and Internet" and "Secure Channel" in the [Windows Feedback Hub](https://aka.ms/WIPFeedbackHub).

|Application|Impacted Version|Fixed Version|
|-|-|-|
| ACDSee Photo Studio | 2018 | 2023 |
| Adguard | 6.4, 7.12 | 7.15 |
| ArcGIS | 10.3 | 11.1 |
| Arma 3 | 3 | 3 |
| Blio e-Reader | 3.4.1 | Not Available |
| BlueStacks 3 (蓝叠3) | 5.10 | 5.13 |
| BlueStacks X | 0.21.0.1063 | 10.4.0.1034 |
| CCB Security Client (中国建设银行E路航网银安全组件) | 3.3.9.7 | Not Available |
| CorelDRAW Graphics Suite X6 | 16 | 24.5.0.731 (2022) |
| Driver Support | 10.1.6.14 | SolveIQ |
| DRUKI Gofin | 3.17.94.0 | Not Available |
| ESET NOD32 Antivirus | 5.0.94.0 | 10.0.390.0 |
| EVault Data Protection | 7.01.6125 | Not Available |
| Jaws for Windows | 2019.1903.47 | 2023.2307.37 |
| K7 Enterprise Security | 4.1.0.116 | 4.5.1.121 |
| LANGuard | 12.7 | 12.10 |
| Microsoft Office 2008 Professional Accounting Express | 2008 | Not Available |
| Project Plan 365 | 23.8.1204.14137 | 23.30.1225.39313 |
| Quick Heal Total Security | 23.00 (14.1.0.10) | Not Available |
| Safari | 5.1.7 | 5.1.7 |
| Splice | 4.0.35686 | 4.3.98750 |
| SQL Server | 2012, 2014, 2016 | 2014, 2016 patched, see [KB3135244](/troubleshoot/sql/database-engine/connect/tls-1-2-support-microsoft-sql-server)|
| Turbo Tax | 2011, 2012, 2014, 2015, 2016, 2017, 2018 | 2022 |
| UltraViewer | 6.6.37 | 6.6.63 |
| UPlay | 22.1 | Ubisoft Connect |
| vWorkspace | 8.6.1 | Not Available |
| WebCompanion | 11.7 | 12.1 |
| Xbox One SmartGlass | 2.2.1702.2004 | Not Available |
| 火萤视频桌面 (Qiffa) | 5.2.5.9 | Not Available |  

## Developer guidance

Additional information for developers and enterprise administrators using Security Support Provider Interface (SSPI) can be found at [TLS 1.0 and TLS 1.1 soon to be disabled in Windows](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/tls-1-0-and-tls-1-1-soon-to-be-disabled-in-windows/ba-p/3887947)
