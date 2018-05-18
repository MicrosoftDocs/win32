---
title: StorPortSetPowerSettingNotificationGuids routine
description: The StorPortSetPowerSettingNotificationGuids routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for.
ms.assetid: 'FB74E774-8CDE-4DE4-942E-10AF4BEFF63C'
keywords: ["StorPortSetPowerSettingNotificationGuids routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortSetPowerSettingNotificationGuids
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortSetPowerSettingNotificationGuids routine

The **StorPortSetPowerSettingNotificationGuids** routine enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for.

## Syntax


```C++
ULONG StorPortSetPowerSettingNotificationGuids(
  _In_ PVOID  HwDeviceExtension,
  _In_ ULONG  GuidCount,
  _In_ LPGUID Guid
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*GuidCount* \[in\]
</dt> <dd>

The number of GUIDs in the *Guid* array.

</dd> <dt>

*Guid* \[in\]
</dt> <dd>

An array of power setting GUIDs to register for notification. A typical use for registering these GUIDs is for SATA miniports to receive notifications for AHCI Link Power Management setting changes. The AHCI Link Power Management settings defined by the Microsoft AHCI StorPort miniport driver are the following.

<dt>

<span id="HIPM_DIPM_Setting"></span><span id="hipm_dipm_setting"></span><span id="HIPM_DIPM_SETTING"></span>

<span id="HIPM_DIPM_Setting"></span><span id="hipm_dipm_setting"></span><span id="HIPM_DIPM_SETTING"></span>**HIPM/DIPM Setting** (0b2d69d7-a2a1-449c-9680-f91c70521c60)


</dt> <dd>

Configures the link power management mode for disk and storage devices that are attached to the system through an AHCI interface.



| Index | Name          | Description                                                 |
|-------|---------------|-------------------------------------------------------------|
| 0     | Active        | Link power management is not used.                          |
| 1     | HIPM          | Host-Initiated Power Management (HIPM) is used.             |
| 2     | HIPM and DIPM | HIPM and Device-Initiated Power Management (DIPM) are used. |



 

</dd> <dt>

<span id="Adaptive_Setting"></span><span id="adaptive_setting"></span><span id="ADAPTIVE_SETTING"></span>

<span id="Adaptive_Setting"></span><span id="adaptive_setting"></span><span id="ADAPTIVE_SETTING"></span>**Adaptive Setting** (dab60367-53fe-4fbc-825e-521d069d2456)


</dt> <dd>

The period of AHCI link idle time before the link is put into a slumber state when HIPM or DIPM is enabled.



| Value  | Description                                             |
|--------|---------------------------------------------------------|
| 0      | Minimum value in milliseconds (only use Partial state). |
| ...    | Any intermediate value.                                 |
| 300000 | Maximum value in milliseconds (5 minutes).              |



 

</dd> </dl>

Other miniports may define and register their own power setting GUIDs.

</dd> </dl>

## Return value

The **StorPortSetPowerSettingNotificationGuids** routine returns one of these status codes:



| Return code                                                                                                          | Description                                                                    |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Insufficient resources are available to register for notifications.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The notification GUIDs were registered successfully.<br/>                |



 

## Remarks

A miniport calls **StorPortSetPowerSettingNotificationGuids** in its [**HwStorFindAdapter**](hwstorfindadapter.md) routine to register the GUIDs it requests to receive notifications for.

When a power state change occurs for a registered notification, the miniport is notified in its [**HwStorAdapterControl**](hwstoradaptercontrol.md) routine. The control type of **ScsiPowerSettingNotification** is set in the *ControlType* parameter.

The AHCI Link Power management settings are part of the Disk Settings subgroup (0012ee47-9041-4b5d-9b77-535fba8b1442) in the power policy configuration. These are managed under the SUB\_DISK configuration alias with *powercfg.exe*.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortSetPowerSettingNotificationGuids%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






