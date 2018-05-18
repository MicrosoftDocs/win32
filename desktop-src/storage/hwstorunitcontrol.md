---
title: HW\_UNIT\_CONTROL routine
description: A miniport driver's HwStorUnitControl routine is called to perform synchronous operations to control the state of storage unit device. The miniport driver is notified to start a unit or handle a power state transition for a unit device.
ms.assetid: '33534C7A-C88D-4980-98A7-2B94488D3550'
keywords: ["HwStorUnitControl routine Storage Devices", "HW_UNIT_CONTROL"]
topic_type:
- apiref
api_name:
- HwStorUnitControl
api_location:
- Storport.h
api_type:
- UserDefined
---

# HW\_UNIT\_CONTROL routine

A miniport driver's **HwStorUnitControl** routine is called to perform synchronous operations to control the state of storage unit device. The miniport driver is notified to start a unit or handle a power state transition for a unit device.

## Syntax


```C++
HW_UNIT_CONTROL HwStorUnitControl;

SCSI_UNIT_CONTROL_STATUS HwStorUnitControl(
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

A pointer to the miniport driver's per-unit storage area.

</dd> <dt>

*ControlType* \[in\]
</dt> <dd>

Specifies an unit control operation. Each control type initiates an action by the miniport driver. The following are the control types and their meanings.



| Control Type                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | IRQL                       | Spinlock        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|-----------------|
| **ScsiQuerySupportedUnitControlTypes**<br/> | Reports the unit-control operations implemented by the miniport driver. The Storport driver calls **HwStorUnitControl** with this control type after the HBA has been initialized but before the first I/O. The miniport driver fills in the SCSI\_SUPPORTED\_CONTROL\_TYPE\_LIST structure at *Parameters* with the operations it supports. After **HwStorUnitControl** returns from this call, the Storport driver calls the miniport driver's **HwStorUnitControl** only for supported operations.<br/> | PASSIVE\_LEVEL<br/>  | None<br/> |
| **ScsiUnitUsage**<br/>                      | Notifies the miniport if the logical unit is used for any supported usage types. Storport driver will call **HwStorUnitControl** separately for each usage type supported.<br/>                                                                                                                                                                                                                                                                                                                            | PASSIVE\_LEVEL<br/>  | None<br/> |
| **ScsiUnitStart**<br/>                      | Notifies the miniport to start a unit device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                         | PASSIVE\_LEVEL<br/>  | None<br/> |
| **ScsiUnitPower**<br/>                      | Reports the unit power on or power off states. If the miniport supports this control type, it will not receive a storage request block with SRB\_FUNCTION\_POWER.<br/>                                                                                                                                                                                                                                                                                                                                     | DISPATCH\_LEVEL<br/> | None<br/> |
| **ScsiUnitPoFxPowerInfo**<br/>              | Notifies the miniport if idle power management is enabled or disabled on the unit component. The miniport should call [**StorPortInitializePoFxPower**](storportinitializepofxpower.md) within this unit control if idle power management was enabled and it if supports runtime power management for the unit device.<br/>                                                                                                                                                                               | PASSIVE\_LEVEL<br/>  | None<br/> |
| **ScsiUnitPoFxPowerRequired**<br/>          | Notifies the miniport whether power is required or not for the unit component.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                        | DISPATCH\_LEVEL<br/> | None<br/> |
| **ScsiUnitPoFxPowerActive**<br/>            | Notifies the miniport that the unit component is either active or idle.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                               | DISPATCH\_LEVEL<br/> | None<br/> |
| **ScsiUnitPoFxPowerSetFState**<br/>         | Notifies the miniport to set the unit component to the given functional power state (F-state). The miniport must support this control type if is specifies more than one F-state in the call to [**StorPortInitializePoFxPower**](storportinitializepofxpower.md).<br/>                                                                                                                                                                                                                                   | DISPATCH\_LEVEL<br/> | None<br/> |
| **ScsiUnitPoFxPowerControl**<br/>           | Requests a power engine plug-in (PEP) initiated private power control operation for the miniport to execute for the unit.<br/>                                                                                                                                                                                                                                                                                                                                                                             | DISPATCH\_LEVEL<br/> | None<br/> |
| **ScsiUnitRemove**<br/>                     | Notifies the miniport that the unit has been removed.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                 | PASSIVE\_LEVEL<br/>  | None<br/> |
| **ScsiUnitSurpriseRemoval**<br/>            | Notifies the miniport that the unit has been surprise-removed.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                        | PASSIVE\_LEVEL<br/>  | None<br/> |
| **ScsiUnitRichDescription**<br/>            | The miniport can choose to support this if the device reports a longer vendor ID, model number, or firmware revision than is defined in the SCSI spec. <br/>                                                                                                                                                                                                                                                                                                                                               | PASSIVE\_LEVEL<br/>  | None<br/> |



 

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
<td><strong>ScsiQuerySupportedUnitControlTypes</strong><br/></td>
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
<p>Points to a caller-allocated array of <strong>BOOLEAN</strong> values that indicate the control types implemented by the miniport driver. The port driver initializes each element to <strong>FALSE</strong>.</p>
<p>The miniport driver sets the corresponding array element to <strong>TRUE</strong> for each operation it supports:</p>
<p><dl> <dt>SupportedTypeList[ScsiQuerySupportedControlTypes]</dt> <dt>SupportedTypeList[ScsiUnitUsage]</dt> <dt>SupportedTypeList[ScsiUnitStart]</dt> <dt>SupportedTypeList[ScsiUnitPower]</dt> <dt>SupportedTypeList[ScsiUnitPoFxPowerInfo] </dt> <dt>SupportedTypeList[ScsiUnitPoFxPowerRequired]</dt> <dt>SupportedTypeList[ScsiUintPoFxPowerActive]</dt> <dt>SupportedTypeList[ScsiUnitPoFxPowerSetFState]</dt> <dt>SupportedTypeList[ScsiUnitPoFxPowerControl]</dt> <dt>SupportedTypeList[ScsiUnitRemove]</dt> <dt>SupportedTypeList[ScsiUnitSurpriseRemoval]</dt> <dt>SupportedTypeList[ScsiUnitRichDescription]</dt> </dl></p>
<p>The miniport driver must not set any element beyond <strong>SupportedTypeList</strong>[<strong>MaxControlType</strong> - 1].</p>
</dd> </dl></td>
</tr>
<tr class="even">
<td><p><strong>ScsiUnitUsage</strong></p></td>
<td><p>Caller-allocated STOR_UC_DEVICE_USAGE structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_UC_DEVICE_USAGE {
    PSTOR_ADDRESS   Address;
    SCSI_UC_DEVICE_USAGE_TYPE   UsageType;
    BOOLEAN InUse;
} STOR_UC_DEVICE_USAGE, *PSTOR_UC_DEVICE_USAGE;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Address"></span><span id="address"></span><span id="ADDRESS"></span><strong>Address</strong></dt> <dd>
<p>The device address for the usage notification.</p>
</dd> <dt><span id="UsageType"></span><span id="usagetype"></span><span id="USAGETYPE"></span><strong>UsageType</strong></dt> <dd>
<p>The usage type from a PnP device usage notification.</p>
</dd> <dt><span id="InUse"></span><span id="inuse"></span><span id="INUSE"></span><strong>InUse</strong></dt> <dd>
<p><strong>TRUE</strong> if the unit is used for the type in <strong>UsageType</strong>. Otherwise, <strong>FALSE</strong>.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiUnitStart</strong></p></td>
<td><p>The <strong>STOR_ADDR_BTL8</strong> address of the unit to start.</p></td>
</tr>
<tr class="even">
<td><p><strong>ScsiUnitPower</strong></p></td>
<td><p>Caller-allocated STOR_UNIT_CONTROL_POWER structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_UNIT_CONTROL_POWER {
    PSTOR_ADDRESS               Address;
    STOR_POWER_ACTION           PowerAction;
    STOR_DEVICE_POWER_STATE     PowerState;
} STOR_UNIT_CONTROL_POWER, *PSTOR_UNIT_CONTROL_POWER;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Address"></span><span id="address"></span><span id="ADDRESS"></span><strong>Address</strong></dt> <dd>
<p>The device address for the power notification.</p>
</dd> <dt><span id="PowerAction"></span><span id="poweraction"></span><span id="POWERACTION"></span><strong>PowerAction</strong></dt> <dd>
<p>The power action indicator. For a runtime power transition, <strong>PowerAction</strong> set to <strong>StorPowerActionNone</strong>.</p>
</dd> <dt><span id="PowerState"></span><span id="powerstate"></span><span id="POWERSTATE"></span><strong>PowerState</strong></dt> <dd>
<p>The current unit power state. This is either <strong>StorPowerDeviceD0</strong> or <strong>StorPowerDeviceD3</strong> for the power on or power of states respectively.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiUnitPoFxPowerInfo</strong></p></td>
<td><p>Caller-allocated STOR_POFX_UNIT_POWER_INFO structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_POFX_UNIT_POWER_INFO {
    STOR_POWER_CONTROL_HEADER   Header;
    BOOLEAN                     IdlePowerEnabled;
} STOR_POFX_UNIT_POWER_INFO, *PSTOR_POFX_UNIT_POWER_INFO;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Header"></span><span id="header"></span><span id="HEADER"></span><strong>Header</strong></dt> <dd>
<p>The power control header structure.</p>
</dd> <dt><span id="IdlePowerEnabled"></span><span id="idlepowerenabled"></span><span id="IDLEPOWERENABLED"></span><strong>IdlePowerEnabled</strong></dt> <dd>
<p><strong>TRUE</strong> if idle power management is enabled for the unit. Otherwise, <strong>FALSE</strong>.</p>
</dd> </dl></td>
</tr>
<tr class="even">
<td><p><strong>ScsiUnitPoFxPowerRequired</strong></p></td>
<td><p>Caller-allocated STOR_POFX_POWER_REQUIRED_CONTEXT structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>typedef struct _STOR_POFX_POWER_REQUIRED_CONTEXT {
    STOR_POWER_CONTROL_HEADER Header;
    BOOLEAN                   PowerRequired;ScsiUnitRichDescription
} STOR_POFX_POWER_REQUIRED_CONTEXT, *PSTOR_POFX_POWER_REQUIRED_CONTEXT;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Header"></span><span id="header"></span><span id="HEADER"></span><strong>Header</strong></dt> <dd>
<p>The power control header structure.</p>
</dd> <dt><span id="PowerRequired"></span><span id="powerrequired"></span><span id="POWERREQUIRED"></span><strong>PowerRequired</strong></dt> <dd>
<p><strong>TRUE</strong> if the unit component requires power. Otherwise, <strong>FALSE.</strong></p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiUintPoFxPowerActive</strong></p></td>
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
<p>Index of the device component with the active status. The component index is always 0 for a unit device.</p>
</dd> <dt><span id="Active"></span><span id="active"></span><span id="ACTIVE"></span><strong>Active</strong></dt> <dd>
<p>The active status of the component. <strong>Active</strong> is set to <strong>TRUE</strong> if the unit is active. Otherwise, <strong>FALSE</strong> if idle.</p>
</dd> </dl></td>
</tr>
<tr class="even">
<td><p><strong>ScsiUnitPoFxPowerSetFState</strong></p></td>
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
<p>Index of the device component with the active status. The component index is always 0 for a unit device.</p>
</dd> <dt><span id="FState"></span><span id="fstate"></span><span id="FSTATE"></span><strong>FState</strong></dt> <dd>
<p>The F-state to set for the unit component.</p>
</dd> </dl></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiUnitPoFxPowerControl</strong></p></td>
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
<p>A power control code GUID identifying the private control private control operation to execute for the unit.</p>
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
<tr class="even">
<td><p><strong>ScsiUnitRemove</strong></p></td>
<td><p>The <strong>STOR_ADDR_BTL8</strong> address of the unit being removed.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ScsiUnitSurpriseRemoval</strong></p></td>
<td><p>The <strong>STOR_ADDR_BTL8</strong> address of the unit being surprise-removed.</p></td>
</tr>
<tr class="even">
<td><p><strong>ScsiUnitRichDescription</strong></p></td>
<td><p>Caller-allocated <strong>STOR_RICH_DEVICE_DESCRIPTION</strong> structure.</p>
<div class="code">
<span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>#define STOR_RICH_DEVICE_DESCRIPTION_STRUCTURE_VERSION_V2   0x2

typedef struct _STOR_RICH_DEVICE_DESCRIPTION_V2 {

    ULONG   Version;
    ULONG   Size;

    CHAR    VendorId[STOR_VENDOR_ID_LENGTH + 1];
    CHAR    ModelNumber[STOR_MODEL_NUMBER_LENGTH + 1];
    CHAR    FirmwareRevision[STOR_FIRMWARE_REVISION_LENGTH + 1];

    PSTOR_ADDRESS Address;

} STOR_RICH_DEVICE_DESCRIPTION_V2, *PSTOR_RICH_DEVICE_DESCRIPTION_V2;</code></pre></td>
</tr>
</tbody>
</table>

</div>
<dl> <dt><span id="Version"></span><span id="version"></span><span id="VERSION"></span><strong>Version</strong></dt> <dd>
<p>The version of the structure. Should be <em>STOR_RICH_DEVICE_DESCRIPTION_STRUCTURE_VERSION_V2</em>.</p>
</dd> <dt><span id="Size"></span><span id="size"></span><span id="SIZE"></span><strong>Size</strong></dt> <dd>
<p>The size of the structure. Should be <em>sizeof(STOR_RICH_DEVICE_DESCRIPTION_V2)</em>.</p>
</dd> <dt><span id="VendorId"></span><span id="vendorid"></span><span id="VENDORID"></span><strong>VendorId</strong></dt> <dd>
<p>A string representing the device’s vendor ID. May be an empty string if <em>ModelNumber</em> is provided. The miniport should fill this in.</p>
</dd> <dt><span id="ModelNumber"></span><span id="modelnumber"></span><span id="MODELNUMBER"></span><strong>ModelNumber</strong></dt> <dd>
<p>A string representing the device’s model. The miniport should fill this in.</p>
</dd> <dt><span id="FirmwareRevision"></span><span id="firmwarerevision"></span><span id="FIRMWAREREVISION"></span><strong>FirmwareRevision</strong></dt> <dd>
<p>A string representing the device’s currently active firmware revision. The miniport should fill this in.</p>
</dd> <dt><span id="Address"></span><span id="address"></span><span id="ADDRESS"></span><strong>Address</strong></dt> <dd>
<p>The address of the device for which the rich device description is desired. This is provided by Storport.</p>
</dd> </dl></td>
</tr>
</tbody>
</table>



 

For the structures that contain the STOR\_POWER\_CONTROL\_HEADER header, it has the following definition in *storport.h*.


```
typedef struct _STOR_POWER_CONTROL_HEADER {
    ULONG Version;
    ULONG Size;
    PSTOR_ADDRESS Address;
} STOR_POWER_CONTROL_HEADER, *PSTOR_POWER_CONTROL_HEADER;
```



<dl> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

The version of the parent structure.

</dd> <dt>

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size
</dt> <dd>

The size, in bytes, of the parent structure.

</dd> <dt>

<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address
</dt> <dd>

The address of the unit the control operation is specified for.

</dd> </dl> </dd> </dl>

## Return value

Depending on the control type, **HwStorUnitControl** returns one of the following SCSI\_UNIT\_CONTROL\_STATUS values:



| Return code                                                                                                 | Description                                                                    |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt> **ScsiUnitControlSuccess**</dt> </dl>      | The miniport driver completed the requested operation successfully.<br/> |
| <dl> <dt> **ScsiUnitControlUnsuccessful**</dt> </dl> | The unit control operation was not successful.<br/>                      |



 

## Remarks

The name **HwStorUnitControl** is just a placeholder. The actual prototype of this routine is defined in *storport.h* as follows:


```
typedef
SCSI_UNIT_CONTROL_STATUS
HW_UNIT_CONTROL (
  _In_ PVOID  DeviceExtension,
  _In_ SCSI_UNIT_CONTROL_TYPE  ControlType,
  _In_ PVOID  Parameters
  );
```



## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_UNIT_CONTROL%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






