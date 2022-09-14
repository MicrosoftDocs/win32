---
title: .NET Framework default settings
description: .NET Framework 4.5 is default and .NET Framework 3.5 is optional
ms.assetid: 19B53C82-812A-49AC-87C6-C08E7C199208
ms.topic: article
ms.date: 05/31/2018
---

# .NET Framework 4.5 is default and .NET Framework 3.5 is optional

## Platforms

**Clients**   Windows 8  
**Servers**   Windows Server 2012  

## Description

.NET Framework 4.5 is enabled by default in Windows 8. Windows 8 does not include .NET 3.5 by default, but the files for .NET 3.5 are available on the Windows 8 installation media as an optional feature.

If the user is upgrading from Windows 7 to Windows 8, .NET Framework 3.5 is fully enabled to ensure that any apps on the computer continue to work correctly.

## Manifestation

If the user performs a clean installation of Windows 8, and then installs apps that require .NET Framework 3.5 (or 2.0), they will trigger a request for the necessary .NET 3.5 files. Normally the missing files will be downloaded from Windows Update (after asking the user for permission), but if access to Windows Update is not possible, enabling .NET Framework 3.5 will fail unless an alternate source for the missing files has been specified.

## Mitigation

To enable .NET Framework 3.5 on only test machines with clean installs of Windows 8:

1.  Copy \\sources\\sxs\\ from the mounted operating system build ISO image to dotnet35 or similar folder. For example:
    ```
    xcopy e:\sources\sxs\*.* c:\dotnet35 /s
    ```



2.  Execute this command line using admin privileges:
    ```
    Dism.exe /online /enable-feature /featurename:NetFX3 /All /Source:c:\dotnet35 /LimitAccess

    ```



> [!Note]  
> The sources\\SxS folder must not be used as a redistribution mechanism since this is not a supported mechanism.



## Solution

**For consumers:**

Windows 8 includes a mechanism that automatically enables .NET Framework 3.5 when attempting to install the redistributable package or when an application installer that needs .NET 3.5 invokes the redistributable.

**For App developers (and IT Administrators):**

IT administrators can configure .NET 3.5 apps to run on either .NET 3.5 or .NET 4.5 (depending on what's already installed). In order to run a managed app on either 3.5 or 4.5, just add a section in the application configuration file. This will ensure that if .NET 3.5 is installed, the app will run on .NET 3.5; otherwise the app will run on .NET 4.5. An example of the additional section in the configuration file is provided below:


```
<configuration>
   <startup>
      <supportedRuntime version="v2.0.50727"/>
      <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.5"/>
   </startup>
</configuration>
```



**For enterprise OEMs:**

To enable .NET Framework 3.5 for EEAP builds and for applications that do not have access to Windows Update:

1.  Copy \\sources\\sxs\\ from the mounted OS build ISO image to the dotnet35 or similar folder. For example:
    ```
    xcopy e:\sources\sxs\*.* c:\dotnet35 /s
    ```



2.  Set the regkey:
    ```
    [HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Servicing]
     LocalSourcePath = c:\dotnet35
    ```



**For enterprises:**

For machines that are configured to use WSUS for servicing, you can set a registry entry to allow the machine to use Windows Update for enabling .NET 3.5 instead of WSUS (servicing will still be done from WSUS if you do this).

-   Set the regkey:
    ```
    [HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Servicing]  RepairContentServerSource =DWORD(2)
    ```



This registry entry can also be set via Group Policy (Local Computer Policy -> Computer Configuration -> Administrative Templates -> System. Select the setting  Specify settings for optional component installation and component repair .

If you select  Contact Windows Update directly to download repair content instead of Windows Server Update Services (WSUS) , any attempts to add Windows features (for example, .NET Framework 3.5) or repair features will trigger file downloads from Windows Update. Target computers require Internet and WU access for this option. Normal servicing operations continue to use WSUS if it has been configured as a source.

**A note regarding setting local source location via registry entries**

IT administrators can set local source location(s) for .NET 3.5 files via a registry entry, so that users can use the Add/Remove Windows Features dialog to enable features with missing payload without having to specify a source location. The value of the registry entry can be controlled via group policy.

This registry entry is supported:



<table>
<thead>
<tr class="header">
<th>Entry</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local Source Path</td>
<td>REG_EXPAND_SZ</td>
<td>Local source path(s) to be used by default. Multiple paths can be specified; they should be separated by  ; . Locations will be searched in the order they are specified. <br/> Local source location(s) that are specified on the DISM command line, take precedence over locations specified in this registry entry. Folder locations can be specified in this registry entry. <br/> WIMs can be used, but the path must be to the WIM file; there is no need to mount it, for example: <br/> <dl> wim:\\machine\share\file.wim:1<br />
</dl> Notice the  1  at the end. You must specify the numerical index of the image you want to use in the WIM file. <br/> For a mounted WIM, the source path needs to refer to the windows directory of the mounted image, rather than to the mount point (for example: /source:&lt;mount_point&gt;\windows rather than /source:&lt;mount_point&gt;). <br/></td>
</tr>
</tbody>
</table>





## Resources

<dl>

[Implementing Registry-based Policy](/previous-versions/windows/desktop/Policy/implementing-registry-based-policy)  
</dl>
