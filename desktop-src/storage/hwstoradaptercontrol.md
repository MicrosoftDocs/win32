---
title: HW\_ADAPTER\_CONTROL routine
description: A miniport driver's HwStorAdapterControl routine is called to perform synchronous operations to control the state or behavior of an adapter, such as stopping or restarting the HBA for power management.
ms.assetid: 'e1944f1b-97db-4ac2-848e-e69359c09589'
keywords: ["HwStorAdapterControl routine Storage Devices", "HW_ADAPTER_CONTROL"]
topic_type:
- apiref
api_name:
- HwStorAdapterControl
api_location:
- Storport.h
api_type:
- UserDefined
---

# HW\_ADAPTER\_CONTROL routine

A miniport driver's **HwStorAdapterControl** routine is called to perform synchronous operations to control the state or behavior of an adapter, such as stopping or restarting the HBA for power management.

## Syntax


```C++
HW_ADAPTER_CONTROL HwStorAdapterControl;

SCSI_ADAPTER_CONTROL_STATUS HwStorAdapterControl(
  _In_ PVOID                     DeviceExtension,
  _In_ SCSI_ADAPTER_CONTROL_TYPE ControlType,
  _In_ PVOID                     Parameters
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

A pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*ControlType* \[in\]
</dt> <dd>

Specifies an adapter-control operation. Each control type initiates an action by the miniport driver. The following are the control types and their meanings. Also listed, are the current IRQL and the spinlock acquired when the control type issued.



| Control Type                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | IRQL                             | Spinlock                 |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|--------------------------|
| **ScsiQuerySupportedControlTypes**<br/>        | Reports the adapter-control operations implemented by the miniport driver. The Storport driver calls **HwStorAdapterControl** with this control type after the HBA has been initialized but before the first I/O. The miniport driver fills in the SCSI\_SUPPORTED\_CONTROL\_TYPE\_LIST structure at *Parameters* with the operations it supports. After **HwStorAdapterControl** returns from this call, the Storport driver calls the miniport driver's **HwStorAdapterControl** only for supported operations.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | PASSIVE\_LEVEL<br/>        | None<br/>          |
| **ScsiStopAdapter**<br/>                       | Shuts down the HBA. The Storport driver calls **HwStorAdapterControl** with this control type when the HBA has been removed from the system, stopped for resource reconfiguration, shut down for power management, or otherwise reconfigured or disabled. The Storport driver ensures that there are no uncompleted requests and issues an SRB\_FUNCTION\_FLUSH request to the miniport driver before calling this routine. <br/> The miniport driver disables interrupts on its HBA, halts all processing, (including background processing not subject to interrupts or processing of which the Storport driver is unaware, such as reconstructing fault-tolerant volumes), flushes any remaining cached data to persistent storage, and puts the HBA into a state from which it can be reinitialized or restarted. <br/> The miniport driver should not free its resources when stopping its HBA. If the HBA was removed or stopped for PnP resource reconfiguration, the Storport driver releases resources on behalf of the miniport driver. If the HBA is shut down for power management, the miniport driver's resources are preserved so the HBA can be restarted. <br/> After **HwStorAdapterControl** returns from stopping the HBA, any data structures allocated on behalf of the miniport driver for the HBA should be considered invalid until the miniport driver is asked to restart. <br/> Note that the Storport driver might call **HwStorAdapterControl** to stop the adapter after the HBA has already been physically removed from the system, so the miniport driver's **HwStorAdapterControl** routine must not perform any operations that require the HBA to be physically present while it is stopping the HBA.<br/> The miniport driver is not called again for the HBA until either the PnP manager requests that the HBA be started, in which case the Storport driver (re)initializes by calling its **HwStorAdapterControl** and [**HwStorInitialize**](hwstorinitialize.md) routines, or an HBA that was stopped for power management is powered up, in which case the Storport driver calls the miniport driver's **HwStorAdapterControl** routine with **ScsiRestartAdapter** or, if the miniport driver does not implement that control type, repeats the initialization sequence for the HBA. <br/> | DIRQL<br/>                 | InterruptLock<br/> |
| **ScsiRestartAdapter**<br/>                    | Reinitializes an HBA. The Storport driver calls **HwStorAdapterControl** with this control type to power up an HBA that was shut down for power management. All resources previously assigned to the miniport driver are still available, and its device extension and logical unit extensions, if any, are intact.<br/> The miniport driver performs the same operations as in its [**HwStorInitialize**](hwstorinitialize.md) routine, such as setting up the HBA's registers and its initial state, if any.<br/> The miniport driver must not call routines that can only be called from [**HwStorFindAdapter**](hwstorfindadapter.md) or from **HwStorAdapterControl** when the control type is **ScsiSetRunningConfig**, such as [**StorPortGetBusData**](storportgetbusdata.md) and [**StorPortSetBusDataByOffset**](storportsetbusdatabyoffset.md). If the miniport driver must call such routines to restart its HBA, it must also implement **ScsiSetRunningConfig**.<br/> If the miniport driver does not implement **ScsiRestartAdapter**, the Storport driver calls the miniport driver's [**HwStorFindAdapter**](hwstorfindadapter.md) and [**HwStorInitialize**](hwstorinitialize.md) routines. However, because such routines might do detection work unnecessary for restarting the HBA, such a miniport driver will not power up its HBA as quickly as a miniport driver that implements **ScsiRestartAdapter**. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | DIRQL<br/>                 | InterruptLock<br/> |
| **ScsiSetBootConfig**<br/>                     | Restores any settings on an HBA that the BIOS might need to reboot. The Storport driver calls **HwStorAdapterControl** with this control type after calling this routine with **ScsiStopAdapter**. <br/> A miniport driver must implement **ScsiSetBootConfig** if it must call [**StorPortGetBusData**](storportgetbusdata.md) or [**StorPortSetBusDataByOffset**](storportsetbusdatabyoffset.md) before the system will be able to reboot. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | PASSIVE\_LEVEL<br/>        | None<br/>          |
| **ScsiSetRunningConfig**<br/>                  | Restores any settings on an HBA that the miniport driver might need to control the HBA while the system is running. The Storport driver calls **HwStorAdapterControl** with **ScsiSetRunningConfig** before calling this routine with **ScsiRestartAdapter** if the miniport driver implements that control type.<br/> The HBA's interrupt is not yet connected when the Storport driver makes this call, so the miniport driver must take care not to generate an interrupt.<br/> A miniport driver must implement **ScsiSetRunningConfig** if it must call [**StorPortGetBusData**](storportgetbusdata.md) and [**StorPortSetBusDataByOffset**](storportsetbusdatabyoffset.md) to restore the appropriate running configuration to the HBA before it can be restarted.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | PASSIVE\_LEVEL<br/>        | None<br/>          |
| **ScsiPowerSettingNotification**<br/>          | Notification for a registered power setting change. The Storport driver calls **HwStorAdapterControl** with this control type if a power setting change occurs. Miniports register for power setting notifications by calling [**StorPortSetPowerSettingNotificationGuids**](storportsetpowersettingnotificationguids.md) with a list of GUIDs representing the power change events of interest. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | PASSIVE\_LEVEL<br/>        | None<br/>          |
| **ScsiAdapterFilterResourceRequirements**<br/> | Filters the required resources for the adapter. The storport driver calls *HwStorAdapterControl* with this [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](https://msdn.microsoft.com/library/windows/hardware/ff550874) control type when the storport processes the request.<br/> The miniport driver should change or reduce the resources described in the buffer using the **STOR\_FILTER\_RESOURCE\_REQUIREMENTS** structure. This control type is valid in Windows 8.1 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | PASSIVE\_LEVEL<br/>        | None<br/>          |
| **ScsiAdapterPower**<br/>                      | Reports the adapter power on or power off states. If the miniport supports this control type, it will not receive a storage request block with SRB\_FUNCTION\_POWER and **HwStorAdapterControl** is not called with the **ScsiStopAdapter** control type. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | &lt;= DISPATCH\_LEVEL<br/> | None<br/>          |
| **ScsiAdapterPoFxPowerRequired**<br/>          | Notifies the miniport whether power is required or not for the adapter component. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | &lt;= DISPATCH\_LEVEL<br/> | None<br/>          |
| **ScsiAdapterPoFxPowerActive**<br/>            | Notifies the miniport whether the adapter component is active or idle. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | &lt;= DISPATCH\_LEVEL<br/> | None<br/>          |
| **ScsiAdapterPoFxPowerSetFState**<br/>         | Notifies the miniport to set the adapter component to the given F-state. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | &lt;= DISPATCH\_LEVEL<br/> | None<br/>          |
| **ScsiAdapterPoFxPowerControl**<br/>           | Requests a power engine plug-in (PEP) initiated private power control operation for the miniport to execute for the adapter. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | &lt;= DISPATCH\_LEVEL<br/> | None<br/>          |
| **ScsiAdapterPrepareForBusReScan**<br/>        | Notifies the miniport to prepare the adapter for bus enumeration. The miniport should power on the adapter and all connected devices to allow the bus enumeration operation to find the devices. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | PASSIVE\_LEVEL<br/>        | None<br/>          |
| **ScsiAdapterSystemPowerHints**<br/>           | Notifies the miniport system power hints. This control type is valid in Windows 8 and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | PASSIVE\_LEVEL<br/>        | None<br/>          |



 

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Contains information related to the *ControlType*.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Control Type</th>
<th>Parameters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ScsiQuerySupportedControlTypes</strong><br/></td>
<td>Caller-allocated SCSI_SUPPORTED_CONTROL_TYPE_LIST structure.<br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _SCSI_SUPPORTED_CONTROL_TYPE_LIST { 
    IN ULONG MaxControlType;
    OUT BOOLEAN SupportedTypeList[0];
} SCSI_SUPPORTED_CONTROL_TYPE_LIST, *PSCSI_SUPPORTED_CONTROL_TYPE_LIST;</code></pre></td>
</tr>
</tbody>
</table>

<dl> <dt><span id="MaxControlType"></span><span id="maxcontroltype"></span><span id="MAXCONTROLTYPE"></span><strong>MaxControlType</strong></dt> <dd>
<p>Specifies the number of entries in the <strong>SupportedTypeList</strong> array.</p>
</dd> <dt><span id="SupportedTypeList"></span><span id="supportedtypelist"></span><span id="SUPPORTEDTYPELIST"></span><strong>SupportedTypeList</strong></dt> <dd>
<p>Points to a caller-allocated array of BOOLEAN values that indicate the control types implemented by the miniport driver. The port driver initializes each element to <strong>FALSE</strong>.</p>
<p>The miniport driver sets the corresponding array element to <strong>TRUE</strong> for each operation it supports:</p>
<p><dl> <dt>SupportedTypeList[ScsiQuerySupportedControlTypes]</dt> <dt>SupportedTypeList[ScsiStopAdapter]</dt> <dt>SupportedTypeList[ScsiRestartAdapter]</dt> <dt>SupportedTypeList[ScsiSetBootConfig] </dt> <dt>SupportedTypeList[ScsiSetRunningConfig]</dt> <dt>SupportedTypeList[ScsiPowerSettingNotification]</dt> <dt>SupportedTypeList[ScsiAdapterPower]</dt> <dt>SupportedTypeList[ScsiAdapterPoFxPowerRequired]</dt> <dt>SupportedTypeList[ScsiAdapterPoFxPowerActive]</dt> <dt>SupportedTypeList[ScsiAdapterPoFxPowerSetFState]</dt> <dt>SupportedTypeList[ScsiAdapterPoFxPowerControl]</dt> <dt>SupportedTypeList[ScsiAdapterPrepareForBusReScan]</dt> <dt>SupportedTypeList[ScsiAdapterSystemPowerHints]</dt> </dl></p>
<p>The miniport driver must not set any element beyond <strong>SupportedTypeList</strong>[<strong>MaxControlType</strong> - 1].</p>
</dd> </dl></td>
</tr>
<tr class="even">
<td><p><strong>ScsiStopAdapter</strong></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiRestartAdapter</strong></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><strong>ScsiSetBootConfig</strong></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiSetRunningConfig</strong></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><strong>ScsiPowerSettingNotification</strong></p></td>
<td><p>Caller-allocated STOR_POWER_SETTING_INFO structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_POWER_SETTING_INFO {
    GUID  PowerSettingGuid;
    PVOID Value;
    ULONG ValueLength;
} STOR_POWER_SETTING_INFO, *PSTOR_POWER_SETTING_INFO;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="PowerSettingGuid"></span><span id="powersettingguid"></span><span id="POWERSETTINGGUID"></span><strong>PowerSettingGuid</strong></dt> <dd>
<p>The GUID of the power setting that changed.</p>
</dd> <dt><span id="Value"></span><span id="value"></span><span id="VALUE"></span><strong>Value</strong></dt> <dd>
<p>Data representing the new value for the power setting.</p>
</dd> <dt><span id="ValueLength"></span><span id="valuelength"></span><span id="VALUELENGTH"></span><strong>ValueLength</strong></dt> <dd>
<p>Length in bytes of the data pointed to by <strong>Value.</strong></p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiAdapterFilterResourceRequirements</strong></p></td>
<td><p>Caller-allocated STOR_FILTER_RESOURCE_REQUIREMENTS structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_FILTER_RESOURCE_REQUIREMENTS {
    ULONG Version;
    ULONG Size;
    PIO_RESOURCE_REQUIREMENTS_LIST IoResourceRequirementsList;
} STOR_FILTER_RESOURCE_REQUIREMENTS, *PSTOR_FILTER_RESOURCE_REQUIREMENTS;
   
#define STOR_FILTER_RESOURCE_REQUIREMENTS_V1 0x1</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Version"></span><span id="version"></span><span id="VERSION"></span><strong>Version</strong></dt> <dd>
<p>The version of the filter. This is currently set to STOR_FILTER_RESOURCE_REQUIREMENTS_V1.</p>
</dd> <dt><span id="Size"></span><span id="size"></span><span id="SIZE"></span><strong>Size</strong></dt> <dd>
<p>The size of this structure.</p>
</dd> <dt><span id="IoResourceRequirementsList"></span><span id="ioresourcerequirementslist"></span><span id="IORESOURCEREQUIREMENTSLIST"></span><strong>IoResourceRequirementsList</strong></dt> <dd>
<p>The IO resource requirements list. For more information see the [<strong>IO_RESOURCE_REQUIREMENTS_LIST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550609) structure.</p>
</dd> </dl></td>
</tr>
<tr class="even">
<td><p><strong>ScsiAdapterPower</strong></p></td>
<td><p>Caller-allocated STOR_ADAPTER_CONTROL_POWER structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_ADAPTER_CONTROL_POWER {
    STOR_POWER_CONTROL_HEADER   Header;
    STOR_POWER_ACTION           PowerAction;
    STOR_DEVICE_POWER_STATE     PowerState;
} STOR_ADAPTER_CONTROL_POWER, *PSTOR_ADAPTER_CONTROL_POWER;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Header"></span><span id="header"></span><span id="HEADER"></span><strong>Header</strong></dt> <dd>
<p>The power control header structure.</p>
</dd> <dt><span id="PowerAction"></span><span id="poweraction"></span><span id="POWERACTION"></span><strong>PowerAction</strong></dt> <dd>
<p>The power action indicator. For a runtime power transition, <strong>PowerAction</strong> set to <strong>StorPowerActionNone</strong>.</p>
</dd> <dt><span id="PowerState"></span><span id="powerstate"></span><span id="POWERSTATE"></span><strong>PowerState</strong></dt> <dd>
<p>The current adapter power state. This is either <strong>StorPowerDeviceD0</strong> or <strong>StorPowerDeviceD3</strong> for the power on or power of states respectively.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiAdapterPoFxPowerRequired</strong></p></td>
<td><p>A <strong>BOOLEAN</strong> which is <strong>TRUE</strong> if the adapter component requires power. Otherwise, <strong>FALSE.</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>ScsiAdapterPoFxPowerActive</strong></p></td>
<td><p>Caller-allocated STOR_POFX_ACTIVE_CONTEXT structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_POFX_ACTIVE_CONTEXT {
    STOR_POWER_CONTROL_HEADER   Header;
    ULONG                       ComponentIndex;
    BOOLEAN                     Active;
} STOR_POFX_ACTIVE_CONTEXT, *PSTOR_POFX_ACTIVE_CONTEXT;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Header"></span><span id="header"></span><span id="HEADER"></span><strong>Header</strong></dt> <dd>
<p>The power control header structure.</p>
</dd> <dt><span id="ComponentIndex"></span><span id="componentindex"></span><span id="COMPONENTINDEX"></span><strong>ComponentIndex</strong></dt> <dd>
<p>Index of the device component with the active status. The component index is always 0 for an adapter.</p>
</dd> <dt><span id="Active"></span><span id="active"></span><span id="ACTIVE"></span><strong>Active</strong></dt> <dd>
<p>The active status of the component. <strong>Active</strong> is always set to <strong>TRUE</strong>.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiAdapterPoFxPowerSetFState</strong></p></td>
<td><p>Caller-allocated STOR_POFX_FSTATE_CONTEXT structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_POFX_FSTATE_CONTEXT {
    STOR_POWER_CONTROL_HEADER   Header;
    ULONG                       ComponentIndex;
    ULONG                       FState;
} STOR_POFX_FSTATE_CONTEXT, *PSTOR_POFX_FSTATE_CONTEXT;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Header"></span><span id="header"></span><span id="HEADER"></span><strong>Header</strong></dt> <dd>
<p>The power control header structure.</p>
</dd> <dt><span id="ComponentIndex"></span><span id="componentindex"></span><span id="COMPONENTINDEX"></span><strong>ComponentIndex</strong></dt> <dd>
<p>Index of the device component with the active status. The component index is always 0 for an adapter.</p>
</dd> <dt><span id="FState"></span><span id="fstate"></span><span id="FSTATE"></span><strong>FState</strong></dt> <dd>
<p>The F-state to set for the adapter component. The F0 state is the only component power state set for an adapter.</p>
</dd> </dl></td>
</tr>
<tr class="even">
<td><p><strong>ScsiAdapterPoFxPowerControl</strong></p></td>
<td><p>Caller-allocated STOR_POFX_POWER_CONTROL structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_POFX_POWER_CONTROL {
    STOR_POWER_CONTROL_HEADER   Header;
    LPCGUID                     PowerControlCode;
    SIZE_T                      InBufferSize;
    SIZE_T                      OutBufferSize;
    PVOID                       InBuffer;
    PVOID                       OutBuffer;
    PSIZE_T                     BytesReturned;
} STOR_POFX_POWER_CONTROL, *PSTOR_POFX_POWER_CONTROL;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Header"></span><span id="header"></span><span id="HEADER"></span><strong>Header</strong></dt> <dd>
<p>The power control header structure.</p>
</dd> <dt><span id="PowerControlCode"></span><span id="powercontrolcode"></span><span id="POWERCONTROLCODE"></span><strong>PowerControlCode</strong></dt> <dd>
<p>A power control code GUID identifying the private control private control operation to execute for the adapter.</p>
</dd> <dt><span id="InBufferSize"></span><span id="inbuffersize"></span><span id="INBUFFERSIZE"></span><strong>InBufferSize</strong></dt> <dd>
<p>The size, in bytes, of the input buffer at <em>InBuffer</em>.</p>
</dd> <dt><span id="OutBufferSize"></span><span id="outbuffersize"></span><span id="OUTBUFFERSIZE"></span><strong>OutBufferSize</strong></dt> <dd>
<p>The size, in bytes, of the output buffer at <em>OutBuffer</em>.</p>
</dd> <dt><span id="InBuffer"></span><span id="inbuffer"></span><span id="INBUFFER"></span><strong>InBuffer</strong></dt> <dd>
<p>The buffer containing input parameters and data for the private power control call.</p>
</dd> <dt><span id="OutBuffer"></span><span id="outbuffer"></span><span id="OUTBUFFER"></span><strong>OutBuffer</strong></dt> <dd>
<p>The buffer where the resulting output parameters and data are returned for the private power control call.</p>
</dd> <dt><span id="BytesReturned"></span><span id="bytesreturned"></span><span id="BYTESRETURNED"></span><strong>BytesReturned</strong></dt> <dd>
<p>The size, in bytes, of the data returned in <em>OutBuffer</em>.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiAdapterPrepareForBusReScan</strong></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><strong>ScsiAdapterSystemPowerHints</strong></p></td>
<td><p>Caller-allocated STOR_SYSTEM_POWER_HINTS structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_SYSTEM_POWER_HINTS {
    ULONG Version;
    ULONG Size;
    RAID_SYSTEM_POWER SystemPower;
    ULONG ResumeLatencyMSec;
} STOR_SYSTEM_POWER_HINTS, *PSTOR_SYSTEM_POWER_HINTS;</code></pre></td>
</tr>
</tbody>
</table>

</div>

<table>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="Version"></span><span id="version"></span><span id="VERSION"></span><strong>Version</strong><br/></td>
<td>The version of this structure. Currently set to STOR_SYSTEM_POWER_HINTS_V1.<br/></td>
</tr>
<tr class="even">
<td><span id="Size"></span><span id="size"></span><span id="SIZE"></span><strong>Size</strong><br/></td>
<td>The size of this structure. Set to <strong>sizeof</strong>(STOR_SYSTEM_POWER_HINTS).<br/></td>
</tr>
<tr class="odd">
<td><span id="SystemPower"></span><span id="systempower"></span><span id="SYSTEMPOWER"></span><strong>SystemPower</strong><br/></td>
<td>A system power usage indicator. This is one of the following values.<br/> <dl> <dt><span id="RaidSystemPowerUnknown"></span><span id="raidsystempowerunknown"></span><span id="RAIDSYSTEMPOWERUNKNOWN"></span>RaidSystemPowerUnknown</dt> <dd> Unknown power usage.<br/> </dd> <dt><span id="RaidSystemPowerLowest"></span><span id="raidsystempowerlowest"></span><span id="RAIDSYSTEMPOWERLOWEST"></span>RaidSystemPowerLowest</dt> <dd> Lowest power usage.<br/> </dd> <dt><span id="RaidSystemPowerLow"></span><span id="raidsystempowerlow"></span><span id="RAIDSYSTEMPOWERLOW"></span>RaidSystemPowerLow</dt> <dd> Low power usage.<br/> </dd> <dt><span id="RaidSystemPowerMedium"></span><span id="raidsystempowermedium"></span><span id="RAIDSYSTEMPOWERMEDIUM"></span>RaidSystemPowerMedium</dt> <dd> Medium power usage.<br/> </dd> <dt><span id="RaidSystemPowerHigh"></span><span id="raidsystempowerhigh"></span><span id="RAIDSYSTEMPOWERHIGH"></span>RaidSystemPowerHigh</dt> <dd> High power usage.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="ResumeLatencyMSec"></span><span id="resumelatencymsec"></span><span id="RESUMELATENCYMSEC"></span><strong>ResumeLatencyMSec</strong><br/></td>
<td>The resume latency, in milliseconds, of the device.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

</dd> </dl>

## Return value

Depending on the control type, **HwStorAdapterControl** returns one of the following SCSI\_ADAPTER\_CONTROL\_STATUS values:



| Return code                                                                                                    | Description                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **ScsiAdapterControlSuccess**</dt> </dl>      | The miniport driver completed the requested operation successfully. Currently, **HwStorAdapterControl** must return this value for all control types.<br/> |
| <dl> <dt> **ScsiAdapterControlUnsuccessful**</dt> </dl> | The adapter control operation was not successful.<br/>                                                                                                     |



 

## Remarks

Because miniport drivers that work with the Storport driver must support Plug and Play (PnP), this function is required. The control types, **ScsiStopAdapter** and **ScsiRestartAdapter**, must be supported.

The name **HwStorAdapterControl** is just a placeholder. The actual prototype of this routine is defined in *storport.h* as follows:


```
typedef
SCSI_ADAPTER_CONTROL_STATUS
HW_ADAPTER_CONTROL (
  _In_ PVOID  DeviceExtension,
  _In_ SCSI_ADAPTER_CONTROL_TYPE  ControlType,
  _In_ PVOID  Parameters
  );
```



## Examples

To define an **HwStorAdapterControl** callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorAdapterControl** callback routine that is named *MyHwAdapterControl*, use the **HW\_ADAPTER\_CONTROL** type as shown in this code example:


```
HW_ADAPTER_CONTROL MyHwAdapterControl;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
SCSI_ADAPTER_CONTROL_STATUS
MyHwAdapterControl (
  _In_ PVOID  DeviceExtension,
  _In_ SCSI_ADAPTER_CONTROL_TYPE  ControlType,
  _In_ PVOID  Parameters
  );
  {
      ...
  }
```



The **HW\_ADAPTER\_CONTROL** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_ADAPTER\_CONTROL** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> <dt>

[**HwStorInitialize**](hwstorinitialize.md)
</dt> <dt>

[**StorPortGetBusData**](storportgetbusdata.md)
</dt> <dt>

[**StorPortSetBusDataByOffset**](storportsetbusdatabyoffset.md)
</dt> <dt>

[**StorPortSetPowerSettingNotificationGuids**](storportsetpowersettingnotificationguids.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_ADAPTER_CONTROL%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






