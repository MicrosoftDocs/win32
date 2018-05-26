---
title: SystemSetting enumeration
description: Specifies the type of system settings to retrieve or set.
ms.assetid: 8EA9EA90-543D-4127-938B-68E2F363BB6A
keywords:
- SystemSetting enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- SystemSetting
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SystemSetting enumeration

Specifies the type of system settings to retrieve or set.

## Syntax


```C++
enum SystemSetting {
  SystemSettingNone                       = 0, 
  SystemSettingFlagGetBool                = 65536,                                                                                          // 0x10000
  SystemSettingFlagSetBoolFalse           = 16777216,                                                                                       // 0x1000000
  SystemSettingFlagSetBoolTrue            = 33554432,                                                                                       // 0x2000000
  SystemSettingBatteryPresent             = 1 | SystemSettingFlagGetBool, 
  SystemSettingOnACPower                  = 2 | SystemSettingFlagGetBool, 
  SystemSettingElevated                   = 3 | SystemSettingFlagGetBool, 
  SystemSettingPioModeOnSystemDrive       = 4 | SystemSettingFlagGetBool, 
  SystemSettingUsingBasicDisplay          = 5 | SystemSettingFlagGetBool, 
  SystemSettingIEPresent                  = 6 | SystemSettingFlagGetBool, 
  SystemSettingAutoLogOnEnabled           = 7 | SystemSettingFlagGetBool, 
  SystemSettingAntivirusActive            = 8 | SystemSettingFlagGetBool, 
  SystemSettingKernelDebuggerEnabled      = 9 | SystemSettingFlagGetBool, 
  SystemSettingDriverVerifierEnabled      = 10 | SystemSettingFlagGetBool, 
  SystemSettingProblemDevicesExist        = 11 | SystemSettingFlagGetBool, 
  SystemSettingPowerProfileMinSavings     = 12 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolTrue, 
  SystemSettingPowerProfileBalanced       = 13 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolTrue, 
  SystemSettingPowerProfileMaxSavings     = 14 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolTrue, 
  SystemSettingLowBatteryAction           = 15 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingScreensaver                = 16 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingCriticalBatteryAction      = 17 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingAutoSleepAC                = 18 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingAutoSleepDC                = 19 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingAutoHibernateAC            = 20 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingAutoHibernateDC            = 21 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingDisplayTimeoutAC           = 22 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingDisplayTimeoutDC           = 23 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingDisplayDimAC               = 24 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingDisplayDimDC               = 25 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingVolumeShadowCopy           = 26 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingWindowsAutoUpdate          = 27 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingWirelessAdaptersConnected  = 28 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingLockOnWakeAC               = 29 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingLockOnWakeDC               = 30 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse, 
  SystemSettingWakeOnTimerAC              = 31 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingWakeOnTimerDC              = 32 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingHibernateOn                = 33 | SystemSettingFlagGetBool, 
  SystemSettingSuspendOn                  = 34 | SystemSettingFlagGetBool, 
  SystemSettingFastStartupOn              = 35 | SystemSettingFlagGetBool, 
  SystemSettingShowExtensions             = 36 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingShowAllObjects             = 37 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingScreenBackground           = 38 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingIEFirstRun                 = 39 | SystemSettingFlagSetBoolFalse, 
  SystemSettingScreensaverSecure          = 40 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingTracingRunning             = 41 | SystemSettingFlagGetBool, 
  SystemSettingAudioRenderDevicePresent   = 42 | SystemSettingFlagGetBool, 
  SystemSettingDisplayBootMenu            = 43 | SystemSettingFlagGetBool, 
  SystemSettingConnectedStandbyOn         = 44 | SystemSettingFlagGetBool, 
  SystemSettingAllowDisplayRequiredAC     = 45 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingAllowDisplayRequiredDC     = 46 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingAllowExecutionRequiredAC   = 47  | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingAllowExecutionRequiredDC   = 48  | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingIEWarnOnIntranet           = 49  | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue, 
  SystemSettingLockScreen                 = 50 | SystemSettingFlagGetBool | SystemSettingFlagSetBoolFalse | SystemSettingFlagSetBoolTrue 

};
```



## Constants

<dl> <dt>

<span id="SystemSettingNone"></span><span id="systemsettingnone"></span><span id="SYSTEMSETTINGNONE"></span>**SystemSettingNone**
</dt> <dd>

No system setting was specified. This value should never occur at runtime.

</dd> <dt>

<span id="SystemSettingFlagGetBool"></span><span id="systemsettingflaggetbool"></span><span id="SYSTEMSETTINGFLAGGETBOOL"></span>**SystemSettingFlagGetBool**
</dt> <dd>

A flag that specifies that a **SystemSetting** enumerator is readable.

</dd> <dt>

<span id="SystemSettingFlagSetBoolFalse"></span><span id="systemsettingflagsetboolfalse"></span><span id="SYSTEMSETTINGFLAGSETBOOLFALSE"></span>**SystemSettingFlagSetBoolFalse**
</dt> <dd>

A flag that indicates that a **SystemSetting** enumerator is writable with the value of false.

</dd> <dt>

<span id="SystemSettingFlagSetBoolTrue"></span><span id="systemsettingflagsetbooltrue"></span><span id="SYSTEMSETTINGFLAGSETBOOLTRUE"></span>**SystemSettingFlagSetBoolTrue**
</dt> <dd>

A flag that indicates that a **SystemSetting** enumerator is writable with the value of true.

</dd> <dt>

<span id="SystemSettingBatteryPresent"></span><span id="systemsettingbatterypresent"></span><span id="SYSTEMSETTINGBATTERYPRESENT"></span>**SystemSettingBatteryPresent**
</dt> <dd>

A battery is present in the system.

</dd> <dt>

<span id="SystemSettingOnACPower"></span><span id="systemsettingonacpower"></span><span id="SYSTEMSETTINGONACPOWER"></span>**SystemSettingOnACPower**
</dt> <dd>

The system is on AC power.

</dd> <dt>

<span id="SystemSettingElevated"></span><span id="systemsettingelevated"></span><span id="SYSTEMSETTINGELEVATED"></span>**SystemSettingElevated**
</dt> <dd>

TThe assessment is running elevated.

</dd> <dt>

<span id="SystemSettingPioModeOnSystemDrive"></span><span id="systemsettingpiomodeonsystemdrive"></span><span id="SYSTEMSETTINGPIOMODEONSYSTEMDRIVE"></span>**SystemSettingPioModeOnSystemDrive**
</dt> <dd>

The system drive is using PIO mode.

</dd> <dt>

<span id="SystemSettingUsingBasicDisplay"></span><span id="systemsettingusingbasicdisplay"></span><span id="SYSTEMSETTINGUSINGBASICDISPLAY"></span>**SystemSettingUsingBasicDisplay**
</dt> <dd>

The system is using the basic display driver.

</dd> <dt>

<span id="SystemSettingIEPresent"></span><span id="systemsettingiepresent"></span><span id="SYSTEMSETTINGIEPRESENT"></span>**SystemSettingIEPresent**
</dt> <dd>

Internet Explorer is present in the installed OS SKU.

</dd> <dt>

<span id="SystemSettingAutoLogOnEnabled"></span><span id="systemsettingautologonenabled"></span><span id="SYSTEMSETTINGAUTOLOGONENABLED"></span>**SystemSettingAutoLogOnEnabled**
</dt> <dd>

Auto Logon is enabled.

</dd> <dt>

<span id="SystemSettingAntivirusActive"></span><span id="systemsettingantivirusactive"></span><span id="SYSTEMSETTINGANTIVIRUSACTIVE"></span>**SystemSettingAntivirusActive**
</dt> <dd>

An anti-virus application is active.

</dd> <dt>

<span id="SystemSettingKernelDebuggerEnabled"></span><span id="systemsettingkerneldebuggerenabled"></span><span id="SYSTEMSETTINGKERNELDEBUGGERENABLED"></span>**SystemSettingKernelDebuggerEnabled**
</dt> <dd>

A kernel debugger is enabled on the system.

</dd> <dt>

<span id="SystemSettingDriverVerifierEnabled"></span><span id="systemsettingdriververifierenabled"></span><span id="SYSTEMSETTINGDRIVERVERIFIERENABLED"></span>**SystemSettingDriverVerifierEnabled**
</dt> <dd>

Driver Verifier is enabled on the system.

</dd> <dt>

<span id="SystemSettingProblemDevicesExist"></span><span id="systemsettingproblemdevicesexist"></span><span id="SYSTEMSETTINGPROBLEMDEVICESEXIST"></span>**SystemSettingProblemDevicesExist**
</dt> <dd>

One or more devices have an issue. In Device Manager, these devices are shown with a yellow bang icon.

</dd> <dt>

<span id="SystemSettingPowerProfileMinSavings"></span><span id="systemsettingpowerprofileminsavings"></span><span id="SYSTEMSETTINGPOWERPROFILEMINSAVINGS"></span>**SystemSettingPowerProfileMinSavings**
</dt> <dd>

The current power profile is set to minimum power savings.

</dd> <dt>

<span id="SystemSettingPowerProfileBalanced"></span><span id="systemsettingpowerprofilebalanced"></span><span id="SYSTEMSETTINGPOWERPROFILEBALANCED"></span>**SystemSettingPowerProfileBalanced**
</dt> <dd>

The current power profile is set to balanced power savings.

</dd> <dt>

<span id="SystemSettingPowerProfileMaxSavings"></span><span id="systemsettingpowerprofilemaxsavings"></span><span id="SYSTEMSETTINGPOWERPROFILEMAXSAVINGS"></span>**SystemSettingPowerProfileMaxSavings**
</dt> <dd>

The current power profile is set to maximum power savings.

</dd> <dt>

<span id="SystemSettingLowBatteryAction"></span><span id="systemsettinglowbatteryaction"></span><span id="SYSTEMSETTINGLOWBATTERYACTION"></span>**SystemSettingLowBatteryAction**
</dt> <dd>

The low battery action is enabled.

</dd> <dt>

<span id="SystemSettingScreensaver"></span><span id="systemsettingscreensaver"></span><span id="SYSTEMSETTINGSCREENSAVER"></span>**SystemSettingScreensaver**
</dt> <dd>

The screen saver has a non-zero timeout and will activate when the timer expires.

</dd> <dt>

<span id="SystemSettingCriticalBatteryAction"></span><span id="systemsettingcriticalbatteryaction"></span><span id="SYSTEMSETTINGCRITICALBATTERYACTION"></span>**SystemSettingCriticalBatteryAction**
</dt> <dd>

The critical battery action is enabled.

</dd> <dt>

<span id="SystemSettingAutoSleepAC"></span><span id="systemsettingautosleepac"></span><span id="SYSTEMSETTINGAUTOSLEEPAC"></span>**SystemSettingAutoSleepAC**
</dt> <dd>

The system has a non-zero timeout value for going to sleep when on AC power.

</dd> <dt>

<span id="SystemSettingAutoSleepDC"></span><span id="systemsettingautosleepdc"></span><span id="SYSTEMSETTINGAUTOSLEEPDC"></span>**SystemSettingAutoSleepDC**
</dt> <dd>

The system has a non-zero timeout value for going to sleep when on DC power.

</dd> <dt>

<span id="SystemSettingAutoHibernateAC"></span><span id="systemsettingautohibernateac"></span><span id="SYSTEMSETTINGAUTOHIBERNATEAC"></span>**SystemSettingAutoHibernateAC**
</dt> <dd>

The system has a non-zero timeout value for hibernating when on AC power.

</dd> <dt>

<span id="SystemSettingAutoHibernateDC"></span><span id="systemsettingautohibernatedc"></span><span id="SYSTEMSETTINGAUTOHIBERNATEDC"></span>**SystemSettingAutoHibernateDC**
</dt> <dd>

The system has a non-zero timeout value for hibernating when on DC power.

</dd> <dt>

<span id="SystemSettingDisplayTimeoutAC"></span><span id="systemsettingdisplaytimeoutac"></span><span id="SYSTEMSETTINGDISPLAYTIMEOUTAC"></span>**SystemSettingDisplayTimeoutAC**
</dt> <dd>

The system has a non-zero timeout for when the display will turn off when on AC power.

</dd> <dt>

<span id="SystemSettingDisplayTimeoutDC"></span><span id="systemsettingdisplaytimeoutdc"></span><span id="SYSTEMSETTINGDISPLAYTIMEOUTDC"></span>**SystemSettingDisplayTimeoutDC**
</dt> <dd>

The system has a non-zero timeout for when the display will turn off when on DC power.

</dd> <dt>

<span id="SystemSettingDisplayDimAC"></span><span id="systemsettingdisplaydimac"></span><span id="SYSTEMSETTINGDISPLAYDIMAC"></span>**SystemSettingDisplayDimAC**
</dt> <dd>

The system has a non-zero timeout for when the display will dim while on AC power.

</dd> <dt>

<span id="SystemSettingDisplayDimDC"></span><span id="systemsettingdisplaydimdc"></span><span id="SYSTEMSETTINGDISPLAYDIMDC"></span>**SystemSettingDisplayDimDC**
</dt> <dd>

The system has a non-zero timeout for when the display will dim while on DC power.

</dd> <dt>

<span id="SystemSettingVolumeShadowCopy"></span><span id="systemsettingvolumeshadowcopy"></span><span id="SYSTEMSETTINGVOLUMESHADOWCOPY"></span>**SystemSettingVolumeShadowCopy**
</dt> <dd>

The Volume Shadow Copy service is enabled.

</dd> <dt>

<span id="SystemSettingWindowsAutoUpdate"></span><span id="systemsettingwindowsautoupdate"></span><span id="SYSTEMSETTINGWINDOWSAUTOUPDATE"></span>**SystemSettingWindowsAutoUpdate**
</dt> <dd>

Windows Update will automatically update the system.

</dd> <dt>

<span id="SystemSettingWirelessAdaptersConnected"></span><span id="systemsettingwirelessadaptersconnected"></span><span id="SYSTEMSETTINGWIRELESSADAPTERSCONNECTED"></span>**SystemSettingWirelessAdaptersConnected**
</dt> <dd>

Wireless networking adapters are enabled and connected to a wireless network.

</dd> <dt>

<span id="SystemSettingLockOnWakeAC"></span><span id="systemsettinglockonwakeac"></span><span id="SYSTEMSETTINGLOCKONWAKEAC"></span>**SystemSettingLockOnWakeAC**
</dt> <dd>

The system will prompt for a password when it wakes from sleep or hibernation while on AC power.

</dd> <dt>

<span id="SystemSettingLockOnWakeDC"></span><span id="systemsettinglockonwakedc"></span><span id="SYSTEMSETTINGLOCKONWAKEDC"></span>**SystemSettingLockOnWakeDC**
</dt> <dd>

The system will prompt for a password when it wakes from sleep or hibernation while on DC power.

</dd> <dt>

<span id="SystemSettingWakeOnTimerAC"></span><span id="systemsettingwakeontimerac"></span><span id="SYSTEMSETTINGWAKEONTIMERAC"></span>**SystemSettingWakeOnTimerAC**
</dt> <dd>

The Wake Timer has a non-zero value while on AC power.

</dd> <dt>

<span id="SystemSettingWakeOnTimerDC"></span><span id="systemsettingwakeontimerdc"></span><span id="SYSTEMSETTINGWAKEONTIMERDC"></span>**SystemSettingWakeOnTimerDC**
</dt> <dd>

The Wake Timer has a non-zero value while on DC power.

</dd> <dt>

<span id="SystemSettingHibernateOn"></span><span id="systemsettinghibernateon"></span><span id="SYSTEMSETTINGHIBERNATEON"></span>**SystemSettingHibernateOn**
</dt> <dd>

The system has a non-zero timeout value for hibernating.

</dd> <dt>

<span id="SystemSettingSuspendOn"></span><span id="systemsettingsuspendon"></span><span id="SYSTEMSETTINGSUSPENDON"></span>**SystemSettingSuspendOn**
</dt> <dd>

The system under assessment is enabled for suspension.

</dd> <dt>

<span id="SystemSettingFastStartupOn"></span><span id="systemsettingfaststartupon"></span><span id="SYSTEMSETTINGFASTSTARTUPON"></span>**SystemSettingFastStartupOn**
</dt> <dd>

The system under assessment is enabled for Fast Startup (hybrid boot).

</dd> <dt>

<span id="SystemSettingShowExtensions"></span><span id="systemsettingshowextensions"></span><span id="SYSTEMSETTINGSHOWEXTENSIONS"></span>**SystemSettingShowExtensions**
</dt> <dd>

The File Explorer option to show extensions is enabled.

</dd> <dt>

<span id="SystemSettingShowAllObjects"></span><span id="systemsettingshowallobjects"></span><span id="SYSTEMSETTINGSHOWALLOBJECTS"></span>**SystemSettingShowAllObjects**
</dt> <dd>

The File Explorer option to show hidden items is enabled.

</dd> <dt>

<span id="SystemSettingScreenBackground"></span><span id="systemsettingscreenbackground"></span><span id="SYSTEMSETTINGSCREENBACKGROUND"></span>**SystemSettingScreenBackground**
</dt> <dd>

The system under assessment is set to display a desktop background.

</dd> <dt>

<span id="SystemSettingIEFirstRun"></span><span id="systemsettingiefirstrun"></span><span id="SYSTEMSETTINGIEFIRSTRUN"></span>**SystemSettingIEFirstRun**
</dt> <dd>

Internet Explorer behaves as it does when it runs for the first time

</dd> <dt>

<span id="SystemSettingScreensaverSecure"></span><span id="systemsettingscreensaversecure"></span><span id="SYSTEMSETTINGSCREENSAVERSECURE"></span>**SystemSettingScreensaverSecure**
</dt> <dd>

The system under assessment displays the logon screen after it returns from a screen saver.

</dd> <dt>

<span id="SystemSettingTracingRunning"></span><span id="systemsettingtracingrunning"></span><span id="SYSTEMSETTINGTRACINGRUNNING"></span>**SystemSettingTracingRunning**
</dt> <dd>

A Windows Performance Record trace is running.

</dd> <dt>

<span id="SystemSettingAudioRenderDevicePresent"></span><span id="systemsettingaudiorenderdevicepresent"></span><span id="SYSTEMSETTINGAUDIORENDERDEVICEPRESENT"></span>**SystemSettingAudioRenderDevicePresent**
</dt> <dd>

An audio rendering device (for example, speakers) is present.

</dd> <dt>

<span id="SystemSettingDisplayBootMenu"></span><span id="systemsettingdisplaybootmenu"></span><span id="SYSTEMSETTINGDISPLAYBOOTMENU"></span>**SystemSettingDisplayBootMenu**
</dt> <dd>

The system displays a menu when it boots, for example when multiple operating systems are installed.

</dd> <dt>

<span id="SystemSettingConnectedStandbyOn"></span><span id="systemsettingconnectedstandbyon"></span><span id="SYSTEMSETTINGCONNECTEDSTANDBYON"></span>**SystemSettingConnectedStandbyOn**
</dt> <dd>

The system supports connected standby mode.

</dd> <dt>

<span id="SystemSettingAllowDisplayRequiredAC"></span><span id="systemsettingallowdisplayrequiredac"></span><span id="SYSTEMSETTINGALLOWDISPLAYREQUIREDAC"></span>**SystemSettingAllowDisplayRequiredAC**
</dt> <dd>

The system when on AC power allows the display to be required (the display won't turn off).

</dd> <dt>

<span id="SystemSettingAllowDisplayRequiredDC"></span><span id="systemsettingallowdisplayrequireddc"></span><span id="SYSTEMSETTINGALLOWDISPLAYREQUIREDDC"></span>**SystemSettingAllowDisplayRequiredDC**
</dt> <dd>

The system when on DC power allows the display to be required (the display won't turn off).

</dd> <dt>

<span id="SystemSettingAllowExecutionRequiredAC"></span><span id="systemsettingallowexecutionrequiredac"></span><span id="SYSTEMSETTINGALLOWEXECUTIONREQUIREDAC"></span>**SystemSettingAllowExecutionRequiredAC**
</dt> <dd>

The system when on AC power allows an execution required request (the system won't suspend if execution required is set).

</dd> <dt>

<span id="SystemSettingAllowExecutionRequiredDC"></span><span id="systemsettingallowexecutionrequireddc"></span><span id="SYSTEMSETTINGALLOWEXECUTIONREQUIREDDC"></span>**SystemSettingAllowExecutionRequiredDC**
</dt> <dd>

The system when on DC power allows an execution required request (the system won't suspend if execution required is set).

</dd> <dt>

<span id="SystemSettingIEWarnOnIntranet"></span><span id="systemsettingiewarnonintranet"></span><span id="SYSTEMSETTINGIEWARNONINTRANET"></span>**SystemSettingIEWarnOnIntranet**
</dt> <dd>

Internet Explorer warns if the Intranet security settings are in effect.

</dd> <dt>

<span id="SystemSettingLockScreen"></span><span id="systemsettinglockscreen"></span><span id="SYSTEMSETTINGLOCKSCREEN"></span>**SystemSettingLockScreen**
</dt> <dd>

The lock screen is displayed after a suspend.

</dd> </dl>

## Remarks

Assessments can query the system for various settings using the [**SystemSettingCheckBoolean**](support-systemsettingcheckboolean.md) API or the [**SystemState**](systemstate.md) interface. Only some of the system settings are writable to false and some are writable to true.

Managed code uses the [**SystemSetting**](axe-systemsetting_om) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





