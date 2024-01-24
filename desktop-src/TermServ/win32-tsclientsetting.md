---
title: Win32_TSClientSetting class
description: Defines configuration settings for the Win32\_Terminal class related to connection policy.
ms.assetid: 438baf22-adc2-410e-bf9b-4b17a05c5ce4
ms.tgt_platform: multiple
keywords:
- Win32_TSClientSetting class Remote Desktop Services
- Win32_TSClientSetting class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSClientSetting
- Win32_TSClientSetting.Caption
- Win32_TSClientSetting.Description
- Win32_TSClientSetting.InstallDate
- Win32_TSClientSetting.Name
- Win32_TSClientSetting.Status
- Win32_TSClientSetting.TerminalName
- Win32_TSClientSetting.ConnectionPolicy
- Win32_TSClientSetting.ConnectClientDrivesAtLogon
- Win32_TSClientSetting.ConnectPrinterAtLogon
- Win32_TSClientSetting.DefaultToClientPrinter
- Win32_TSClientSetting.PolicySourceDefaultToClientPrinter
- Win32_TSClientSetting.WindowsPrinterMapping
- Win32_TSClientSetting.PolicySourceWindowsPrinterMapping
- Win32_TSClientSetting.LPTPortMapping
- Win32_TSClientSetting.PolicySourceLPTPortMapping
- Win32_TSClientSetting.COMPortMapping
- Win32_TSClientSetting.PolicySourceCOMPortMapping
- Win32_TSClientSetting.DriveMapping
- Win32_TSClientSetting.PolicySourceDriveMapping
- Win32_TSClientSetting.AudioMapping
- Win32_TSClientSetting.PolicySourceAudioMapping
- Win32_TSClientSetting.ClipboardMapping
- Win32_TSClientSetting.PolicySourceClipboardMapping
- Win32_TSClientSetting.ColorDepthPolicy
- Win32_TSClientSetting.PolicySourceColorDepthPolicy
- Win32_TSClientSetting.ColorDepth
- Win32_TSClientSetting.PolicySourceColorDepth
- Win32_TSClientSetting.MaxMonitors
- Win32_TSClientSetting.MaxXResolution
- Win32_TSClientSetting.MaxYResolution
- Win32_TSClientSetting.PolicySourceMaxMonitors
- Win32_TSClientSetting.PolicySourceMaxResolution
- Win32_TSClientSetting.PNPRedirection
- Win32_TSClientSetting.PolicySourcePNPRedirection
- Win32_TSClientSetting.AudioCaptureRedir
- Win32_TSClientSetting.PolicySourceAudioCaptureRedir
- Win32_TSClientSetting.VideoPlaybackRedir
- Win32_TSClientSetting.PolicySourceVideoPlaybackRedir
- Win32_TSClientSetting.AllowDwm
- Win32_TSClientSetting.PolicySourceAllowDwm
- Win32_TSClientSetting.PolicyAdvancedRemoteAppGraphics
- Win32_TSClientSetting.AdvancedRemoteAppGraphics
- Win32_TSClientSetting.RemoteSessionProfile
- Win32_TSClientSetting.PolicySourceRemoteSessionProfile
- Win32_TSClientSetting.AVC444ModePreferred
- Win32_TSClientSetting.PolicySourceAvc444ModePreferred
- Win32_TSClientSetting.EncodeImageQuality
- Win32_TSClientSetting.PolicySourceEncodeImageQuality
- Win32_TSClientSetting.HardwareGraphicsAdapter
- Win32_TSClientSetting.PolicySourceHardwareGraphicsAdapter
- Win32_TSClientSetting.SelectTransport
- Win32_TSClientSetting.PolicySourceSelectTransport
- Win32_TSClientSetting.SelectNetworkDetect
- Win32_TSClientSetting.PolicySourceSelectNetworkDetect
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSClientSetting class

The **Win32\_TSClientSetting** WMI class defines configuration settings for the [**Win32\_Terminal**](win32-terminal.md) class related to connection policy.

The following syntax is simplified from MOF code and includes all defined and inherited properties, in alphabetical order. For reference information on methods, see the table of methods later in this topic.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TSCLIENTSETTING_Prov"), ClassContext("local|hkey_local_machine\\SYSTEM\\CurrentControlSet\\Control\\TerminalServer\\WinStations"), AMENDMENT]
class Win32_TSClientSetting : Win32_TerminalSetting
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   TerminalName;
  uint32   ConnectionPolicy;
  uint32   ConnectClientDrivesAtLogon;
  uint32   ConnectPrinterAtLogon;
  uint32   DefaultToClientPrinter;
  uint32   PolicySourceDefaultToClientPrinter;
  uint32   WindowsPrinterMapping;
  uint32   PolicySourceWindowsPrinterMapping;
  uint32   LPTPortMapping;
  uint32   PolicySourceLPTPortMapping;
  uint32   COMPortMapping;
  uint32   PolicySourceCOMPortMapping;
  uint32   DriveMapping;
  uint32   PolicySourceDriveMapping;
  uint32   AudioMapping;
  uint32   PolicySourceAudioMapping;
  uint32   ClipboardMapping;
  uint32   PolicySourceClipboardMapping;
  uint32   ColorDepthPolicy;
  uint32   PolicySourceColorDepthPolicy;
  uint32   ColorDepth;
  uint32   PolicySourceColorDepth;
  uint32   MaxMonitors;
  uint32   MaxXResolution;
  uint32   MaxYResolution;
  uint32   PolicySourceMaxMonitors;
  uint32   PolicySourceMaxResolution;
  uint32   PNPRedirection;
  uint32   PolicySourcePNPRedirection;
  uint32   AudioCaptureRedir;
  uint32   PolicySourceAudioCaptureRedir;
  uint32   VideoPlaybackRedir;
  uint32   PolicySourceVideoPlaybackRedir;
  uint32   AllowDwm;
  uint32   PolicySourceAllowDwm;
  uint32   PolicyAdvancedRemoteAppGraphics;
  uint32   AdvancedRemoteAppGraphics;
  uint32   RemoteSessionProfile;
  uint32   PolicySourceRemoteSessionProfile;
  uint32   AVC444ModePreferred;
  uint32   PolicySourceAvc444ModePreferred;
  uint32   EncodeImageQuality;
  uint32   PolicySourceEncodeImageQuality;
  uint32   HardwareGraphicsAdapter;
  uint32   PolicySourceHardwareGraphicsAdapter;
  uint32   SelectTransport;
  uint32   PolicySourceSelectTransport;
  uint32   SelectNetworkDetect;
  uint32   PolicySourceSelectNetworkDetect;
};
```

## Members

The **Win32\_TSClientSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSClientSetting** class has these methods.



| Method                                                                   | Description                                                                                                                                                  |
|:-------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConnectionSettings**](win32-tsclientsetting-connectionsettings.md)   | Sets the **ConnectClientDrivesAtLogon**, **ConnectPrinterAtLogon**, and **DefaultToClientPrinter** properties of this class.<br/>                      |
| [**SetAllowDwm**](setallowdwm-win32-tsclientsetting.md)                 | Not supported.<br/> **Windows 7 and Windows Server 2008 R2:** Sets the **AllowDwm** property.<br/>                                               |
| [**SetClientProperty**](win32-tsclientsetting-setclientproperty.md)     | Sets the **LPTPortMapping**, **COMPortMapping**, **AudioMapping**, **ClipboardMapping**, **DriveMapping**, or **WindowsPrinterMapping** property.<br/> |
| [**SetColorDepth**](win32-tsclientsetting-setcolordepth.md)             | Sets the **ColorDepth** property.<br/>                                                                                                                 |
| [**SetColorDepthPolicy**](win32-tsclientsetting-setcolordepthpolicy.md) | Sets the **ColorDepthPolicy** property.<br/>                                                                                                           |
| [**SetMaxMonitors**](setmaxmonitors-win32-tsclientsetting.md)           | Sets the **MaxMonitors** property.<br/>                                                                                                                |
| [**SetMaxXResolution**](setmaxxresolution-win32-tsclientsetting.md)     | Sets the **MaxXResolution** property.<br/>                                                                                                             |
| [**SetMaxYResolution**](setmaxyresolution-win32-tsclientsetting.md)     | Sets the **MaxYResolution** property.<br/>                                                                                                             |



 

### Properties

The **Win32\_TSClientSetting** class has these properties.

<dl> <dt>

**AdvancedRemoteAppGraphics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether to enable advanced RemoteFX graphics for RemoteApp.

**Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2012 R2 and Windows 8.1.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Advanced graphics are disabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Advanced graphics are enabled.

</dd> </dl>

</dd> <dt>

**AllowDwm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not available.

**Windows 7 and Windows Server 2008 R2:  **

Specifies whether to enable or disable remote desktop composition. Zero will disable remote desktop composition and a nonzero value will enable it.

Use the [**SetAllowDwm**](setallowdwm-win32-tsclientsetting.md) method to modify this property.

</dd> <dt>

**AudioCaptureRedir**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether to allow audio capture redirection.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

<dt>

<span id="FALSE"></span><span id="false"></span>

**FALSE** (0)


</dt> <dd></dd> <dt>

<span id="TRUE"></span><span id="true"></span>

**TRUE** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**AudioMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether audio mapping is disabled or enabled.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Audio mapping is enabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Audio mapping is disabled.

</dd> </dl>

</dd> <dt>

**AVC444ModePreferred**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether AVC444 mode is preferred.

**Windows 8.1, Windows Server 2012 R2, Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 10 or Windows Server 2016.

<dt>

<span id="FALSE"></span><span id="false"></span>

**FALSE** (0)


</dt> <dd></dd> <dt>

<span id="TRUE"></span><span id="true"></span>

**TRUE** (1)


</dt> <dd></dd> </dl>

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

**ClipboardMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether clipboard mapping is disabled or enabled.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Clipboard mapping is enabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Clipboard mapping is disabled.

</dd> </dl>

</dd> <dt>

**ColorDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the color depth. For possible values, see the [**SetColorDepth**](win32-tsclientsetting-setcolordepth.md) method.

<dt>

<span id="8_bit"></span><span id="8_BIT"></span>

<span id="8_bit"></span><span id="8_BIT"></span>**8 bit** (1)


</dt> <dd></dd> <dt>

<span id="15_bit"></span><span id="15_BIT"></span>

<span id="15_bit"></span><span id="15_BIT"></span>**15 bit** (2)


</dt> <dd></dd> <dt>

<span id="16_bit"></span><span id="16_BIT"></span>

<span id="16_bit"></span><span id="16_BIT"></span>**16 bit** (3)


</dt> <dd></dd> <dt>

<span id="24_bit"></span><span id="24_BIT"></span>

<span id="24_bit"></span><span id="24_BIT"></span>**24 bit** (4)


</dt> <dd></dd> <dt>

<span id="32_bit"></span><span id="32_BIT"></span>

<span id="32_bit"></span><span id="32_BIT"></span>**32 bit** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**ColorDepthPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether to override the user's maximum color setting.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Do not override the user's policy.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Override the user's policy.

</dd> </dl>

</dd> <dt>

**COMPortMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether COM port mapping is disabled or enabled.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

COM port mapping is enabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

COM port mapping is disabled.

</dd> </dl>

</dd> <dt>

**ConnectClientDrivesAtLogon**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the client's drives will be automatically connected during the logon process.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Drives will not be automatically connected.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Drives will be automatically connected.

</dd> </dl>

</dd> <dt>

**ConnectionPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The policy the server uses to retrieve the user connection settings.

<dt>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>**Per User** (0)


</dt> <dd>

The user's connection settings are in effect.

</dd> <dt>

<span id="Server-Override"></span><span id="server-override"></span><span id="SERVER-OVERRIDE"></span>

<span id="Server-Override"></span><span id="server-override"></span><span id="SERVER-OVERRIDE"></span>**Server-Override** (1)


</dt> <dd>

The user's connection settings are overridden by the server.

</dd> </dl>

</dd> <dt>

**ConnectPrinterAtLogon**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether all mapped local printers of the client will be automatically connected during the logon process.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Local printers will not be automatically connected.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Local printers will be automatically connected.

</dd> </dl>

</dd> <dt>

**DefaultToClientPrinter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether print jobs will be automatically sent to the client's local printer.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Print jobs are not to be automatically sent to the client's local printer.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Print jobs are to be automatically sent to the client's local printer.

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

**DriveMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether drive mapping is disabled or enabled.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Drive mapping is enabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Drive mapping is disabled.

</dd> </dl>

</dd> <dt>

**EncodeImageQuality**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the image quality for RDP experience.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

<span id="lossless"></span><span id="LOSSLESS"></span>

**lossless** (1)


</dt> <dd></dd> <dt>

<span id="high"></span><span id="HIGH"></span>

**high** (2)


</dt> <dd></dd> <dt>

<span id="medium"></span><span id="MEDIUM"></span>

**medium** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**HardwareGraphicsAdapter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether the RD Session Host server uses the hardware graphics renderer as the default adapter.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

<span id="FALSE"></span><span id="false"></span>

**FALSE** (0)


</dt> <dd></dd> <dt>

<span id="TRUE"></span><span id="true"></span>

**TRUE** (1)


</dt> <dd></dd> </dl>

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

**LPTPortMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether LPT port mapping is disabled or enabled.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

LPT port mapping is enabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

LPT port mapping is disabled.

</dd> </dl>

</dd> <dt>

**MaxMonitors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of monitors supported by the server. Use the [**SetMaxMonitors**](setmaxmonitors-win32-tsclientsetting.md) method to modify this property.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

</dd> <dt>

**MaxXResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum X resolution supported by the server. Use the [**SetMaxXResolution**](setmaxxresolution-win32-tsclientsetting.md) method to modify this property.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

</dd> <dt>

**MaxYResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum Y resolution supported by the server. Use the [**SetMaxYResolution**](setmaxyresolution-win32-tsclientsetting.md) method to modify this property.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

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

**PNPRedirection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether to allow Plug and Play redirection.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Allow Plug and Play redirection.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Do not allow Plug and Play redirection.

</dd> </dl>

</dd> <dt>

**PolicyAdvancedRemoteAppGraphics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **AdvancedRemoteAppGraphics** property is configured by the server or group policy.

**Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2012 R2 and Windows 8.1.

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

**PolicySourceAllowDwm**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not available.

**Windows 7 and Windows Server 2008 R2:  **

Indicates whether the **AllowDwm** property is configured by the server or group policy.

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

**PolicySourceAudioCaptureRedir**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **AudioCaptureRedir** property is configured by the server or group policy.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

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

**PolicySourceAudioMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **AudioMapping** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceAvc444ModePreferred**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the **AVC444ModePreferredis** property is configured.

**Windows 8.1, Windows Server 2012 R2, Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 10 or Windows Server 2016.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy

</dd> </dl>

</dd> <dt>

**PolicySourceClipboardMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ClipboardMapping** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceColorDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ColorDepth** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceColorDepthPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ColorDepthPolicy** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceCOMPortMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **COMPortMapping** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceDefaultToClientPrinter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **DefaultToClientPrinter** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceDriveMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **DriveMapping** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceEncodeImageQuality**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the **EncodeImageQualityi** is configured.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy

</dd> </dl>

</dd> <dt>

**PolicySourceHardwareGraphicsAdapter**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the **HardwareGraphicsAdapter** is configured.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy

</dd> </dl>

</dd> <dt>

**PolicySourceLPTPortMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **LPTPortMapping** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceMaxMonitors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **MaxMonitors** property is configured by the server, group policy, or default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

</dd> <dt>

**PolicySourceMaxResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **MaxXResolution** and **MaxYResolution** properties are configured by the server, group policy, or default.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourcePNPRedirection**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **PNPRedirection** property is configured by the server or by group policy.

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

**PolicySourceRemoteSessionProfile**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the **RemoteSessionProfile** is configured.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is unavailable prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy

</dd> </dl>

</dd> <dt>

**PolicySourceSelectNetworkDetect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the property **SelectNetworkDetect** is configured.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy

</dd> </dl>

</dd> <dt>

**PolicySourceSelectTransport**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates how the property **SelectTransport** is configured.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group Policy

</dd> </dl>

</dd> <dt>

**PolicySourceVideoPlaybackRedir**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **VideoPlaybackRedir** property is configured by the server or group policy.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

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

**PolicySourceWindowsPrinterMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **WindowsPrinterMapping** property is configured by the server, group policy, or by default.

<dt>

0 (0x0)
</dt> <dd>

Server

</dd> <dt>

1 (0x1)
</dt> <dd>

Group policy

</dd> <dt>

2 (0x2)
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**RemoteSessionProfile**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the profile for the RDP experience.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

<span id="scale"></span><span id="SCALE"></span>

**scale** (1)


</dt> <dd></dd> <dt>

<span id="experience"></span><span id="EXPERIENCE"></span>

**experience** (2)


</dt> <dd></dd> <dt>

<span id="bandwidth"></span><span id="BANDWIDTH"></span>

**bandwidth** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**SelectNetworkDetect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether network detection is used.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

used at connect time and in steady state.

</dd> <dt>

1
</dt> <dd>

disabled at connect time

</dd> <dt>

2
</dt> <dd>

disabled in steady state

</dd> <dt>

3
</dt> <dd>

disabled at connect time and in steady state.

</dd> </dl>

</dd> <dt>

**SelectTransport**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies which transport protocols can be used for RDP access to server.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available prior to Windows 8 or Windows Server 2012.

<dt>

0
</dt> <dd>

Use both UDP and TCP.

</dd> <dt>

1
</dt> <dd>

Use only TCP.

</dd> <dt>

2
</dt> <dd>

Use either UDP or TCP.

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

**TerminalName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the terminal.

This property is inherited from [**Win32\_TerminalSetting**](win32-terminalsetting.md).

</dd> <dt>

**VideoPlaybackRedir**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether to allow video playback redirection.

**Windows Server 2008 and Windows Vista:** This property is not available before Windows Server 2008 R2 and Windows 7.

<dt>

<span id="FALSE"></span><span id="false"></span>

**FALSE** (0)


</dt> <dd></dd> <dt>

<span id="TRUE"></span><span id="true"></span>

**TRUE** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**WindowsPrinterMapping**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether printer mapping is disabled or enabled for the client's window.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

Printer mapping is enabled.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

Printer mapping is disabled.

</dd> </dl>

</dd> </dl>

## Remarks

Be aware that a window station associated with the console session cannot access the methods and properties of this class. If an attempt is made to do so by specifying "Console" as the value of the **TerminalName** property, methods of this object will return **WBEM\_E\_NOT\_SUPPORTED**. This error code is also returned if a window station attempts to call methods of this object to add or modify the security properties of the LocalSystem, LocalService, or NetworkService accounts.

To connect to the \\root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of six.

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
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Terminal**](win32-terminal.md)
</dt> <dt>

[**Win32\_TerminalSetting**](win32-terminalsetting.md)
</dt> <dt>

[**CIM\_Setting**](/windows/desktop/CIMWin32Prov/cim-setting)
</dt> </dl>

 

