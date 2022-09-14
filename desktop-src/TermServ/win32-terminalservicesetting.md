---
title: Win32_TerminalServiceSetting class
description: Represents the configuration for a Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 4cd047db-921f-4ccb-946b-d2c7b8d6beea
ms.tgt_platform: multiple
keywords:
- Win32_TerminalServiceSetting class Remote Desktop Services
- Win32_TerminalServiceSetting class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting
- Win32_TerminalServiceSetting.Caption
- Win32_TerminalServiceSetting.Description
- Win32_TerminalServiceSetting.InstallDate
- Win32_TerminalServiceSetting.Name
- Win32_TerminalServiceSetting.Status
- Win32_TerminalServiceSetting.ServerName
- Win32_TerminalServiceSetting.TerminalServerMode
- Win32_TerminalServiceSetting.GetCapabilitiesID
- Win32_TerminalServiceSetting.LicensingType
- Win32_TerminalServiceSetting.PolicySourceLicensingType
- Win32_TerminalServiceSetting.PossibleLicensingTypes
- Win32_TerminalServiceSetting.LicensingName
- Win32_TerminalServiceSetting.LicensingDescription
- Win32_TerminalServiceSetting.ActiveDesktop
- Win32_TerminalServiceSetting.UserPermission
- Win32_TerminalServiceSetting.DeleteTempFolders
- Win32_TerminalServiceSetting.PolicySourceDeleteTempFolders
- Win32_TerminalServiceSetting.UseTempFolders
- Win32_TerminalServiceSetting.PolicySourceUseTempFolders
- Win32_TerminalServiceSetting.AllowTSConnections
- Win32_TerminalServiceSetting.PolicySourceAllowTSConnections
- Win32_TerminalServiceSetting.SingleSession
- Win32_TerminalServiceSetting.PolicySourceSingleSession
- Win32_TerminalServiceSetting.ProfilePath
- Win32_TerminalServiceSetting.PolicySourceProfilePath
- Win32_TerminalServiceSetting.HomeDirectory
- Win32_TerminalServiceSetting.PolicySourceHomeDirectory
- Win32_TerminalServiceSetting.TimeZoneRedirection
- Win32_TerminalServiceSetting.PolicySourceTimeZoneRedirection
- Win32_TerminalServiceSetting.Logons
- Win32_TerminalServiceSetting.DirectConnectLicenseServers
- Win32_TerminalServiceSetting.PolicySourceDirectConnectLicenseServers
- Win32_TerminalServiceSetting.PolicySourceConfiguredLicenseServers
- Win32_TerminalServiceSetting.DisableForcibleLogoff
- Win32_TerminalServiceSetting.PolicySourceDisableForcibleLogoff
- Win32_TerminalServiceSetting.FallbackPrintDriverType
- Win32_TerminalServiceSetting.PolicySourceFallbackPrintDriverType
- Win32_TerminalServiceSetting.SessionBrokerDrainMode
- Win32_TerminalServiceSetting.LimitedUserSessions
- Win32_TerminalServiceSetting.EnableDFSS
- Win32_TerminalServiceSetting.PolicySourceEnableDFSS
- Win32_TerminalServiceSetting.EnableRemoteDesktopMSI
- Win32_TerminalServiceSetting.PolicySourceEnableRemoteDesktopMSI
- Win32_TerminalServiceSetting.EnableAutomaticReconnection
- Win32_TerminalServiceSetting.PolicySourceEnableAutomaticReconnection
- Win32_TerminalServiceSetting.UseRDEasyPrintDriver
- Win32_TerminalServiceSetting.PolicySourceUseRDEasyPrintDriver
- Win32_TerminalServiceSetting.RedirectSmartCards
- Win32_TerminalServiceSetting.PolicySourceRedirectSmartCards
- Win32_TerminalServiceSetting.EnableDiskFSS
- Win32_TerminalServiceSetting.EnableNetworkFSS
- Win32_TerminalServiceSetting.NetworkFSSUserSessionWeight
- Win32_TerminalServiceSetting.NetworkFSSLocalSystemWeight
- Win32_TerminalServiceSetting.NetworkFSSCatchAllWeight
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TerminalServiceSetting class

The **Win32\_TerminalServiceSetting** WMI class represents the configuration for a Remote Desktop Session Host (RD Session Host) server. Settings include capabilities such as RD Session Host server mode, licensing, Active Desktop, permissions, deletion of temporary folders, and temporary directories for sessions.

The following syntax is simplified from MOF code and includes all defined and inherited properties, in alphabetical order. For reference information on methods, see the table of methods later in this topic.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TERMINALSERVICESETTING_Prov"), ClassContext("local|hkey_local_machine\\SYSTEM\\CurrentControlSet\\Control\\TerminalServer"), AMENDMENT]
class Win32_TerminalServiceSetting : CIM_Setting
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   ServerName;
  uint32   TerminalServerMode;
  uint32   GetCapabilitiesID;
  uint32   LicensingType;
  uint32   PolicySourceLicensingType;
  uint32   PossibleLicensingTypes;
  string   LicensingName;
  string   LicensingDescription;
  uint32   ActiveDesktop;
  uint32   UserPermission;
  uint32   DeleteTempFolders;
  uint32   PolicySourceDeleteTempFolders;
  uint32   UseTempFolders;
  uint32   PolicySourceUseTempFolders;
  uint32   AllowTSConnections;
  uint32   PolicySourceAllowTSConnections;
  uint32   SingleSession;
  uint32   PolicySourceSingleSession;
  string   ProfilePath;
  uint32   PolicySourceProfilePath;
  string   HomeDirectory;
  uint32   PolicySourceHomeDirectory;
  uint32   TimeZoneRedirection;
  uint32   PolicySourceTimeZoneRedirection;
  string   Logons;
  string   DirectConnectLicenseServers;
  uint32   PolicySourceDirectConnectLicenseServers;
  uint32   PolicySourceConfiguredLicenseServers;
  uint32   DisableForcibleLogoff;
  uint32   PolicySourceDisableForcibleLogoff;
  uint32   FallbackPrintDriverType;
  uint32   PolicySourceFallbackPrintDriverType;
  uint32   SessionBrokerDrainMode;
  uint32   LimitedUserSessions;
  uint32   EnableDFSS;
  uint32   PolicySourceEnableDFSS;
  uint32   EnableRemoteDesktopMSI;
  uint32   PolicySourceEnableRemoteDesktopMSI;
  uint32   EnableAutomaticReconnection;
  uint32   PolicySourceEnableAutomaticReconnection;
  uint32   UseRDEasyPrintDriver;
  uint32   PolicySourceUseRDEasyPrintDriver;
  uint32   RedirectSmartCards;
  uint32   PolicySourceRedirectSmartCards;
  uint32   EnableDiskFSS;
  uint32   EnableNetworkFSS;
  uint32   NetworkFSSUserSessionWeight;
  uint32   NetworkFSSLocalSystemWeight;
  uint32   NetworkFSSCatchAllWeight;
};
```

## Members

The **Win32\_TerminalServiceSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TerminalServiceSetting** class has these methods.



| Method                                                                                                                | Description                                                                                                                                                                    |
|:----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddDirectConnectLicenseServer**](win32-terminalservicesetting-adddirectconnectlicenseserver.md)                   | Configures a new license server in the enterprise.<br/>                                                                                                                  |
| [**AddLSToSpecifiedLicenseServerList**](addlstospecifiedlicenseserverlist-win32-terminalservicesetting.md)           | Adds the given license server to the end of the list of specified license servers.<br/>                                                                                  |
| [**CanAccessLicenseServer**](canaccesslicenseserver-win32-terminalservicesetting.md)                                 | Determines whether the RD Session Host server is allowed to request Remote Desktop Services client access licenses (RDS CALs) from a Remote Desktop license server.<br/> |
| [**ChangeMode**](win32-terminalservicesetting-changemode.md)                                                         | Sets the licensing type of the Remote Desktop license server.<br/>                                                                                                       |
| [**CreateWinstation**](createwinstation-win32-terminalservicesetting.md)                                             | Creates a new listener stack based on the unique combination of listener name and NIC.<br/>                                                                              |
| [**DeleteDirectConnectLicenseServer**](win32-terminalservicesetting-deletedirectconnectlicenseserver.md)             | Deletes the specified license server from the enterprise.<br/>                                                                                                           |
| [**EmptySpecifiedLicenseServerList**](emptyspecifiedlicenseserverlist-win32-terminalservicesetting.md)               | Removes all license servers from the list of specified license servers.<br/>                                                                                             |
| [**FindLicenseServers**](findlicenseservers-win32-terminalservicesetting.md)                                         | Enumerates all of the Remote Desktop license servers and the method of discovery.<br/>                                                                                   |
| [**GetDomain**](getdomain-win32-terminalservicesetting.md)                                                           | Retrieves the name of the domain that the RD Session Host server is a member of.<br/>                                                                                    |
| [**GetGracePeriodDays**](getgraceperioddays-win32-terminalservicesetting.md)                                         | Retrieves the number of days that are remaining in the RD Licensing grace period for an RD Session Host server.<br/>                                                     |
| [**GetRegisteredLicenseServerList**](getregisteredlicenseserverlist-win32-terminalservicesetting.md)                 | Gets the list of registered license servers.<br/>                                                                                                                        |
| [**GetSpecifiedLicenseServerList**](getspecifiedlicenseserverlist-win32-terminalservicesetting.md)                   | Retrieves the list of specified license servers.<br/>                                                                                                                    |
| [**GetTSLanaIds**](gettslanaids-win32-terminalservicesetting.md)                                                     | Gets the IDs and descriptions of Remote Desktop Services network adapters.<br/>                                                                                          |
| [**GetTStoLSConnectivityStatus**](gettstolsconnectivitystatus-win32-terminalservicesetting.md)                       | Determines the connectivity status between Remote Desktop Services and a license server.<br/>                                                                            |
| [**GetWinstationDriverNames**](getwinstationdrivernames-win32-terminalservicesetting.md)                             | Retrieves a list of Winstation driver names.<br/>                                                                                                                        |
| [**PingLicenseServer**](pinglicenseserver-win32-terminalservicesetting.md)                                           | Pings the license server to determine whether it is a valid license server.<br/>                                                                                         |
| [**RemoveLSFromSpecifiedLicenseServerList**](removelsfromspecifiedlicenseserverlist-win32-terminalservicesetting.md) | Removes the given license server from the list of specified license servers.<br/>                                                                                        |
| [**SetAllowTSConnections**](win32-terminalservicesetting-setallowtsconnections.md)                                   | Sets the **AllowTSConnections** property.<br/>                                                                                                                           |
| [**SetDisableForcibleLogoff**](win32-terminalservicesetting-setdisableforciblelogoff.md)                             | Sets the **DisableForcibleLogoff** property.<br/>                                                                                                                        |
| [**SetFallbackPrintDriverType**](win32-terminalservicesetting-setfallbackprintdrivertype.md)                         | Sets the **FallbackPrintDriverType** property.<br/>                                                                                                                      |
| [**SetHomeDirectory**](win32-terminalservicesetting-sethomedirectory.md)                                             | Sets the **HomeDirectory** property.<br/>                                                                                                                                |
| [**SetPolicyPropertyName**](win32-terminalservicesetting-setpolicypropertyname.md)                                   | Sets one of the following properties: **DeleteTempFolders** or **UseTempFolders**.<br/>                                                                                  |
| [**SetPrimaryLicenseServer**](setprimarylicenseserver-win32-terminalservicesetting.md)                               | Sets the given license server as the first entry in the list of specified license servers.<br/>                                                                          |
| [**SetProfilePath**](win32-terminalservicesetting-setprofilepath.md)                                                 | Sets the **ProfilePath** property.<br/>                                                                                                                                  |
| [**SetSingleSession**](win32-terminalservicesetting-setsinglesession.md)                                             | Sets the **SingleSession** property.<br/>                                                                                                                                |
| [**SetSpecifiedLicenseServerList**](setspecifiedlicenseserverlist-win32-terminalservicesetting.md)                   | Updates the list of specified license servers, replacing any existing specified license servers.<br/>                                                                    |
| [**SetTimeZoneRedirection**](win32-terminalservicesetting-settimezoneredirection.md)                                 | Sets the **TimeZoneRedirection** property.<br/>                                                                                                                          |
| [**UpdateDirectConnectLicenseServer**](updatedirectconnectlicenseserver-win32-terminalservicesetting.md)             | Updates the list of discovery license servers.<br/>                                                                                                                      |



 

### Properties

The **Win32\_TerminalServiceSetting** class has these properties.

<dl> <dt>

**ActiveDesktop**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether Active Desktop is allowed in each user session.

<dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (0)


</dt> <dd>

Active Desktop is not allowed in each user session.

</dd> <dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (1)


</dt> <dd>

Active Desktop is allowed in each user session.

</dd> </dl>

</dd> <dt>

**AllowTSConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether new Remote Desktop Services connections are allowed.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

New connections are not allowed.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

New connections are allowed.

</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**DeleteTempFolders**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether temporary directories are deleted on exit.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Deletion of temporary directories is disabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Deletion of temporary directories is enabled.

</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**DirectConnectLicenseServers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

This property is not available.

**Windows Server 2008:** Enumerates the list of license servers.

</dd> <dt>

**DisableForcibleLogoff**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines whether an administrator that is logged on to the console can be forcibly logged off.

<dt>

0
</dt> <dd>

Administrator can be forcibly logged off.

</dd> <dt>

1
</dt> <dd>

Administrator cannot be forcibly logged off.

</dd> </dl>

</dd> <dt>

**EnableAutomaticReconnection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether to allow Remote Desktop connection clients to automatically reconnect to sessions on an RD Session Host server if the network link is temporarily lost.

<dt>

0 (0x0)
</dt> <dd>

Automatic reconnection is disabled.

</dd> <dt>

1 (0x1)
</dt> <dd>

Automatic reconnection is enabled.

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**EnableDFSS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether dynamic fair-share scheduling (DFSS) is enabled or disabled. This can be one of the following values.

**Windows Server 2008:** This property is unavailable prior to Windows Server 2008 R2.

<dt>

0
</dt> <dd>

DFSS is disabled.

</dd> <dt>

1
</dt> <dd>

DFSS is enabled.

</dd> </dl>

</dd> <dt>

**EnableDiskFSS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies if disk fair share scheduling is enabled.

<dt>

0 (0x0)
</dt> <dd>

Disk fair share scheduling is disabled.

</dd> <dt>

1 (0x1)
</dt> <dd>

Disk fair share scheduling is enabled.

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**EnableNetworkFSS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies if network fair share scheduling is enabled.

<dt>

0 (0x0)
</dt> <dd>

Network fair share scheduling is disabled.

</dd> <dt>

1 (0x1)
</dt> <dd>

Network fair share scheduling is enabled.

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**EnableRemoteDesktopMSI**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the Remote Desktop MSI is enabled or disabled.

<dt>

0 (0x0)
</dt> <dd>

Disabled

</dd> <dt>

1 (0x1)
</dt> <dd>

Enabled

</dd> </dl>

**Windows Server 2008:** This property is unavailable prior to Windows Server 2008 R2.

</dd> <dt>

**FallbackPrintDriverType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies which printer driver to fallback to.

<dt>

<span id="No_fallback_dirvers_0"></span><span id="no_fallback_dirvers_0"></span><span id="NO_FALLBACK_DIRVERS_0"></span>

<span id="No_fallback_dirvers_0"></span><span id="no_fallback_dirvers_0"></span><span id="NO_FALLBACK_DIRVERS_0"></span>**No fallback dirvers=0** (0)


</dt> <dd>

No fallback drivers.

</dd> <dt>

<span id="Best_guess_1"></span><span id="best_guess_1"></span><span id="BEST_GUESS_1"></span>

<span id="Best_guess_1"></span><span id="best_guess_1"></span><span id="BEST_GUESS_1"></span>**Best guess=1** (1)


</dt> <dd>

Best guess.

</dd> <dt>

<span id="Best_guess__if_no_match_is_found_fallback_to_PCL_2"></span><span id="best_guess__if_no_match_is_found_fallback_to_pcl_2"></span><span id="BEST_GUESS__IF_NO_MATCH_IS_FOUND_FALLBACK_TO_PCL_2"></span>

<span id="Best_guess__if_no_match_is_found_fallback_to_PCL_2"></span><span id="best_guess__if_no_match_is_found_fallback_to_pcl_2"></span><span id="BEST_GUESS__IF_NO_MATCH_IS_FOUND_FALLBACK_TO_PCL_2"></span>**Best guess, if no match is found fallback to PCL=2** (2)


</dt> <dd>

Best guess. If no match is found, fallback to Hewlett-Packard Printer Control Language (PCL).

</dd> <dt>

<span id="Best_guess__if_no_match_is_found_fallback_to_PS_3"></span><span id="best_guess__if_no_match_is_found_fallback_to_ps_3"></span><span id="BEST_GUESS__IF_NO_MATCH_IS_FOUND_FALLBACK_TO_PS_3"></span>

<span id="Best_guess__if_no_match_is_found_fallback_to_PS_3"></span><span id="best_guess__if_no_match_is_found_fallback_to_ps_3"></span><span id="BEST_GUESS__IF_NO_MATCH_IS_FOUND_FALLBACK_TO_PS_3"></span>**Best guess, if no match is found fallback to PS=3** (3)


</dt> <dd>

Best guess. If no match is found, fallback to Postscript (PS).

</dd> <dt>

<span id="Best_guess__if_no_match_is_found_show_both_PCL_and_PS_drivers_4"></span><span id="best_guess__if_no_match_is_found_show_both_pcl_and_ps_drivers_4"></span><span id="BEST_GUESS__IF_NO_MATCH_IS_FOUND_SHOW_BOTH_PCL_AND_PS_DRIVERS_4"></span>

<span id="Best_guess__if_no_match_is_found_show_both_PCL_and_PS_drivers_4"></span><span id="best_guess__if_no_match_is_found_show_both_pcl_and_ps_drivers_4"></span><span id="BEST_GUESS__IF_NO_MATCH_IS_FOUND_SHOW_BOTH_PCL_AND_PS_DRIVERS_4"></span>**Best guess, if no match is found show both PCL and PS drivers=4** (4)


</dt> <dd>

Best guess. If no match is found, show both PS and PCL drivers.

</dd> </dl>

</dd> <dt>

**GetCapabilitiesID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Capabilities ID for the provider.

</dd> <dt>

**HomeDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The root directory for the computer.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**LicensingDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A brief description of the licensing mode.

</dd> <dt>

**LicensingName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the licensing mode.

</dd> <dt>

**LicensingType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The licensing type for the specified server mode.

<dt>

<span id="Personal_Terminal_Server"></span><span id="personal_terminal_server"></span><span id="PERSONAL_TERMINAL_SERVER"></span>

<span id="Personal_Terminal_Server"></span><span id="personal_terminal_server"></span><span id="PERSONAL_TERMINAL_SERVER"></span>**Personal Terminal Server** (0)


</dt> <dd>

Personal RD Session Host server.

</dd> <dt>

<span id="Remote_Desktop_for_Administration"></span><span id="remote_desktop_for_administration"></span><span id="REMOTE_DESKTOP_FOR_ADMINISTRATION"></span>

<span id="Remote_Desktop_for_Administration"></span><span id="remote_desktop_for_administration"></span><span id="REMOTE_DESKTOP_FOR_ADMINISTRATION"></span>**Remote Desktop for Administration** (1)


</dt> <dd>

Remote Desktop for Administration.

</dd> <dt>

<span id="Per_Device"></span><span id="per_device"></span><span id="PER_DEVICE"></span>

<span id="Per_Device"></span><span id="per_device"></span><span id="PER_DEVICE"></span>**Per Device** (2)


</dt> <dd>

Per Device. Valid for application servers.

</dd> <dt>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>**Per User** (3)


</dt> <dd>

Per User. Valid for application servers.

</dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>**Not Configured** (4)


</dt> <dd>

Not Configured.

</dd> </dl>

</dd> <dt>

**LimitedUserSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the feature to limit the number of both active and inactive sessions that are allowed on an RD Session Host server is enabled. For example, you may want to set **LimitedUserSessions** to guarantee license compliance for a particular application that is installed on the RD Session Host server. Or, you may want to limit the maximum number of sessions on an RD Session Host server in a load-balanced farm so that the server will not be overloaded if another server in the farm fails.

> [!Note]
>
> The session that is used to connect to the server for administrative purposes is not affected by **LimitedUserSessions**.
>
> In an RD Session Host server farm, if a user exceeds the session limit, the session will be directed to another server by RD Connection Broker load balancing. If the server is a stand-alone server, the user will not be able to connect.
>
> Because of the session that is used to connect to the server for administrative purposes, and the timing of the enforcement of the number of sessions during the logon cycle, it is recommended that you set **LimitedUserSessions** to a value that is slightly lower that the physical limit for the number of sessions on a server.
>
> The **LimitedUserSessions** property is only valid if the RD Session Host role service is installed.

 

<dt>

0
</dt> <dd>

The feature is disabled.

</dd> <dt>

1 or greater
</dt> <dd>

A value of one or greater represents the maximum number of sessions (both active and inactive) that are allowed on the RD Session Host server.

</dd> </dl>

</dd> <dt>

**Logons**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether new sessions are allowed. This setting does not affect existing settings.

<dt>

0
</dt> <dd>

New sessions are allowed.

</dd> <dt>

1
</dt> <dd>

New sessions are not allowed.

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**NetworkFSSCatchAllWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the default network fair share weight for catch-all network traffic. Valid values are 1 to 9.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**NetworkFSSLocalSystemWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the default network fair share weight for a local system processes. Valid values are 1 to 9.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**NetworkFSSUserSessionWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the default network fair share weight for a user session. Valid values are 1 to 9.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**PolicySourceAllowTSConnections**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **AllowTSConnections** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceConfiguredLicenseServers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the license servers returned by the [**GetSpecifiedLicenseServerList**](getspecifiedlicenseserverlist-win32-terminalservicesetting.md) method are configured by the server or by group policy.

**Windows Server 2008:** This property is not available.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceDeleteTempFolders**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **DeleteTempFolders** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceDirectConnectLicenseServers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

This property is not available.

**Windows Server 2008:** Indicates whether the **DirectConnectLicenseServers** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceDisableForcibleLogoff**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2008:** Determines whether the **DisableForcibleLogoff** property is configured by the server or by group policy.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy.

</dd> </dl>

</dd> <dt>

**PolicySourceEnableAutomaticReconnection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **EnableAutomaticReconnection** property is configured by the server or group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**PolicySourceEnableDFSS**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **EnableDFSS** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

**Windows Server 2008:** This property is unavailable prior to Windows Server 2008 R2.

</dd> <dt>

**PolicySourceEnableRemoteDesktopMSI**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **EnableRemoteDesktopMSI** property is configured by the server or group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

**Windows Server 2008:** This property is unavailable prior to Windows Server 2008 R2.

</dd> <dt>

**PolicySourceFallbackPrintDriverType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **FallbackPrintDriverType** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceHomeDirectory**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **HomeDirectory** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceLicensingType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **LicensingType** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceProfilePath**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ProfilePath** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceRedirectSmartCards**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **RedirectSmartCards** property is configured by the server or group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**PolicySourceSingleSession**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the property **SingleSession** is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceTimeZoneRedirection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the property **TimeZoneRedirection** is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PolicySourceUseRDEasyPrintDriver**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **UseRDEasyPrintDriver** property is configured by the server or group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**PolicySourceUseTempFolders**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **UseTempFolders** property is configured by the server or by group policy.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> </dl>

</dd> <dt>

**PossibleLicensingTypes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**BitMap**](/windows/desktop/WmiSdk/standard-qualifiers) ("0", "1", "2", "4", "5"), [**BitValues**](/windows/desktop/WmiSdk/standard-qualifiers) ("Personal Terminal Server", "Remote Desktop for Administration", "Per Device", "Per User", "Not Configured")
</dt> </dl>

A bitmask that specifies the licensing types that are available. This can be a combination of one or more of the following values.

<dt>

1 (0x1)
</dt> <dd>

Personal RD Session Host server licenses are supported.

</dd> <dt>

2 (0x2)
</dt> <dd>

Remote Desktop licenses are supported.

</dd> <dt>

4 (0x4)
</dt> <dd>

Per device licenses are supported.

</dd> <dt>

8 (0x8)
</dt> <dd>

Per user licenses are supported.

</dd> </dl>

</dd> <dt>

**ProfilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Profile path for the computer.

</dd> <dt>

**RedirectSmartCards**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies if redirection of smart card devices is allowed in a remote session.

<dt>

0 (0x0)
</dt> <dd>

Smart card device redirection is not allowed.

</dd> <dt>

1 (0x1)
</dt> <dd>

Smart card device redirection is allowed.

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the RD Session Host server whose properties are of interest.

</dd> <dt>

**SessionBrokerDrainMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The RD Connection Broker user logon mode.

<dt>

0
</dt> <dd>

Allow all connections.

</dd> <dt>

1
</dt> <dd>

Allow reconnections, but prevent new logons until the server is restarted.

</dd> <dt>

2
</dt> <dd>

Allow reconnections, but prevent new logons.

</dd> </dl>

</dd> <dt>

**SingleSession**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether one or more Remote Desktop Services sessions are allowed per user.

<dt>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>

<span id="False"></span><span id="false"></span><span id="FALSE"></span>**False** (0)


</dt> <dd>

More than one session is allowed per user.

</dd> <dt>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>

<span id="True"></span><span id="true"></span><span id="TRUE"></span>**True** (1)


</dt> <dd>

Only one session is allowed per user.

</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> </dl>

</dd> <dt>

**TerminalServerMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The RD Session Host server operating mode of the Remote Desktop Services service. This mode controls the licensing policies that are applicable as well as whether application-compatibility features are enabled.

<dt>

<span id="AppServer"></span><span id="appserver"></span><span id="APPSERVER"></span>

<span id="AppServer"></span><span id="appserver"></span><span id="APPSERVER"></span>**AppServer** (1)


</dt> <dd>

The server operates as an application server.

</dd> <dt>

<span id="RemoteAdmin"></span><span id="remoteadmin"></span><span id="REMOTEADMIN"></span>

<span id="RemoteAdmin"></span><span id="remoteadmin"></span><span id="REMOTEADMIN"></span>**RemoteAdmin** (0)


</dt> <dd>

The session is administered remotely.

</dd> </dl>

</dd> <dt>

**TimeZoneRedirection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the client computer can redirect its time zone settings to the Remote Desktop Services session.

<dt>

0
</dt> <dd>

Redirection is disabled.

</dd> <dt>

1
</dt> <dd>

Redirection is enabled.

</dd> </dl>

</dd> <dt>

**UseRDEasyPrintDriver**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the Remote Desktop Easy Print printer driver is used first to install all client printers.

<dt>

0
</dt> <dd>

The RD Session Host server tries to find a suitable printer driver to install the client printer. If the RD Session Host server does not have a printer driver that matches the client printer, the server tries to use the Remote Desktop Easy Print driver to install the client printer.

</dd> <dt>

1
</dt> <dd>

The RD Session Host server first tries to use the Remote Desktop Easy Print printer driver to install all client printers. If for any reason the Remote Desktop Easy Print printer driver cannot be used, a printer driver on the RD Session Host server that matches the client printer is used.

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:** This property is not available.

</dd> <dt>

**UserPermission**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies if each user session has tight or relaxed security.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Security is tight.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Security is relaxed.

</dd> </dl>

</dd> <dt>

**UseTempFolders**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether temporary directories are created and deleted on a per-session basis.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Temporary directories are not created and deleted for each session. One is created for the first session and never deleted.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Temporary directories are created and deleted for each session.

</dd> </dl>

</dd> </dl>

## Remarks

**Win32\_TerminalServiceSetting** is associated to [**Win32\_TerminalService**](win32-terminalservice.md) as the **Setting** property of the [**Win32\_TerminalServiceToSetting**](win32-terminalservicetosetting.md) association.

[**Win32\_TerminalSetting**](win32-terminalsetting.md) is associated to [**Win32\_Terminal**](win32-terminal.md) as the **Setting** property of the [**Win32\_TerminalTerminalSetting**](win32-terminalterminalsetting.md) association.

To connect to the Root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of six.

The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[**Win32\_Terminal**](win32-terminal.md)
</dt> <dt>

[**Win32\_TerminalService**](win32-terminalservice.md)
</dt> <dt>

[**Win32\_TerminalServiceToSetting**](win32-terminalservicetosetting.md)
</dt> <dt>

[**Win32\_TerminalTerminalSetting**](win32-terminalterminalsetting.md)
</dt> <dt>

[**CIM\_Setting**](/windows/desktop/CIMWin32Prov/cim-setting)
</dt> </dl>

 

