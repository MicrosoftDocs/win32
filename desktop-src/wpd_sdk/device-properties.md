---
description: Windows Portable Devices supports the following device properties.
ms.assetid: 1caf4c1a-ceb6-4aa5-b430-df01c9fb22ce
title: Device Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Device
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Device Properties (PortableDevice.h)

Windows Portable Devices supports the following device properties.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>VarType</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="wpd_device_datetime"></span><span id="WPD_DEVICE_DATETIME"></span><strong>WPD_DEVICE_DATETIME</strong></td>
<td><strong>VT_DATE</strong></td>
<td>The current date and time on the device.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_firmware_version"></span><span id="WPD_DEVICE_FIRMWARE_VERSION"></span><strong>WPD_DEVICE_FIRMWARE_VERSION</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>The device's firmware version.</td>
</tr>
<tr class="odd">
<td><span id="wpd_device_functional_unique_id"></span><span id="WPD_DEVICE_FUNCTIONAL_UNIQUE_ID"></span><strong>WPD_DEVICE_FUNCTIONAL_UNIQUE_ID</strong></td>
<td><strong>VT_VECTOR | VT_UI1</strong></td>
<td>A unique 16-byte identifier that is common across multiple transports supported by the device. If a single device supports multiple transports, this property may be used to associate the various transport WPD drivers with that device.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_manufacturer"></span><span id="WPD_DEVICE_MANUFACTURER"></span><strong>WPD_DEVICE_MANUFACTURER</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>A human-readable device manufacturer name.</td>
</tr>
<tr class="odd">
<td><span id="wpd_device_model"></span><span id="WPD_DEVICE_MODEL"></span><strong>WPD_DEVICE_MODEL</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>The device model.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_model_unique_id"></span><span id="WPD_DEVICE_MODEL_UNIQUE_ID"></span><strong>WPD_DEVICE_MODEL_UNIQUE_ID</strong></td>
<td><strong>VT_VECTOR | VT_UI1</strong></td>
<td>A unique 16-byte identifier used to differentiate among different models of a device.</td>
</tr>
<tr class="odd">
<td><strong>WPD_DEVICE_NETWORK_IDENTIFIER</strong></td>
<td><strong>VT_UI8</strong></td>
<td>A value that specifies the EUI-64 network identifier of the device; this property is used for out-of-band network operations.If the device has MAC-48 physical network addresses (typical of IPv4 networks), the MAC-48 address is encoded in the EUI-64 address as the two halves of the MAC-48 address separated by FF-FF. The EUI-64 value is stored in &quot;network&quot; or &quot;big-endian&quot; order, where an EUI-64 address of 01-02-03-FF-FF-04-05-06 would be placed in the VT_UI8 such that the decimal value is 72624942021346566. This property is required on any device that supports Nominal or Secure Authentication. This property is recommended on devices that support only Zero Authentication. The value can be used by the host to automatically establish access to the device without user intervention.<br/></td>
</tr>
<tr class="even">
<td><span id="wpd_device_power_level"></span><span id="WPD_DEVICE_POWER_LEVEL"></span><strong>WPD_DEVICE_POWER_LEVEL</strong></td>
<td><strong>VT_UI4</strong></td>
<td>A value from 0 to 100 that specifies the power level of the device's battery, with 0 being none, and 100 being fully charged.</td>
</tr>
<tr class="odd">
<td><span id="wpd_device_power_source"></span><span id="WPD_DEVICE_POWER_SOURCE"></span><strong>WPD_DEVICE_POWER_SOURCE</strong></td>
<td>VT_UI4</td>
<td>A <a href="wpd-power-sources.md"><strong>WPD_POWER_SOURCES</strong></a> enumeration that specifies the power source of the device.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_protocol"></span><span id="WPD_DEVICE_PROTOCOL"></span><strong>WPD_DEVICE_PROTOCOL</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>The device protocol that is being used.</td>
</tr>
<tr class="odd">
<td><span id="wpd_device_serial_number"></span><span id="WPD_DEVICE_SERIAL_NUMBER"></span><strong>WPD_DEVICE_SERIAL_NUMBER</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>The device's serial number.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_supported_drm_scheme"></span><span id="WPD_DEVICE_SUPPORTED_DRM_SCHEME"></span><strong>WPD_DEVICE_SUPPORTED_DRM_SCHEMES</strong></td>
<td><strong>VT_UNKNOWN</strong></td>
<td>A value that specifies whether the supported formats returned from the device are in a preferred order. The first format in the list is most preferred by the device, while the last is the least preferred.Applications may use this property to determine whether a device's supported formats are listed in a preferred order.<br/></td>
</tr>
<tr class="odd">
<td><span id="wpd_device_supported_formats_are_ordered"></span><span id="WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED"></span><strong>WPD_DEVICE_SUPPORTED_FORMATS_ARE_ORDERED</strong></td>
<td><strong>VT_BOOL</strong></td>
<td>A Boolean value that specifies whether the supported formats returned from the device are in a preferred order; that is, the first returned format is most preferred while the last returned format is least preferred.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_supports_non_consumable"></span><span id="WPD_DEVICE_SUPPORTS_NON_CONSUMABLE"></span><strong>WPD_DEVICE_SUPPORTS_NON_CONSUMABLE</strong></td>
<td><strong>VT_BOOL</strong></td>
<td>A Boolean value that specifies whether the device supports non-consumable objects. These are objects that the device is only meant to store, not play or use in any way.</td>
</tr>
<tr class="odd">
<td><span id="wpd_device_sync_partner"></span><span id="WPD_DEVICE_SYNC_PARTNER"></span><strong>WPD_DEVICE_SYNC_PARTNER</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>A human-readable description of a device's <em>synchronization partner</em>. This is a device, application, or server that the device communicates with to maintain a common state or group of files between both partners. Examples include e-mail programs and music libraries.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_friendly_name"></span><span id="WPD_DEVICE_FRIENDLY_NAME"></span><strong>WPD_DEVICE_FRIENDLY_NAME</strong></td>
<td><strong>VT_LPWSTR</strong></td>
<td>A value that represents the friendly name set by the user on the device.</td>
</tr>
<tr class="odd">
<td><span id="wpd_device_transport"></span><span id="WPD_DEVICE_TRANSPORT"></span><strong>WPD_DEVICE_TRANSPORT</strong></td>
<td><strong>VT_UI4</strong></td>
<td>the transport supported by the device, such as USB, IP, or Bluetooth. Valid values are of the <a href="wpd-device-transports.md"><strong>WPD_DEVICE_TRANSPORTS</strong></a> enumeration type.</td>
</tr>
<tr class="even">
<td><span id="wpd_device_type"></span><span id="WPD_DEVICE_TYPE"></span><strong>WPD_DEVICE_TYPE</strong></td>
<td><strong>VT_UI4</strong></td>
<td>A value that specifies the device type; applications use this property for representation purposes only. Functional characteristics of the device are decided through functional objects.Devices that do not supply a device icon, for example, a <strong>WPD_RESOURCE_ICON</strong> for the device object, will be represented in the WPD Namespace with a generic icon. This icon will depend on the specified device type, for example, if the device type is a mobile phone, the generic phone icon is used. On first install of the device, the WPD Class Installer will query this property value and store it in the device registry under the PORTABLE_DEVICE_TYPE value as a REG_DWORD.<br/> This parameter's possible values are from the <a href="object-properties.md"><strong>WPD_DEVICE_TYPES</strong></a> enumeration defined in PortableDevice.h. Values are:<br/> <dl> <strong>WPD_DEVICE_TYPE_GENERIC</strong><br />
<strong>WPD_DEVICE_TYPE_CAMERA</strong><br />
<strong>WPD_DEVICE_TYPE_MEDIA_PLAYER</strong><br />
<strong>WPD_DEVICE_TYPE_PHONE</strong><br />
<strong>WPD_DEVICE_TYPE_VIDEO</strong><br />
<strong>WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER</strong><br />
<strong>WPD_DEVICE_TYPE_AUDIO_RECORDER</strong><br />
</dl></td>
</tr>
<tr class="odd">
<td><span id="wpd_device_use_device_stage"></span><span id="WPD_DEVICE_USE_DEVICE_STAGE"></span><strong>WPD_DEVICE_USE_DEVICE_STAGE</strong></td>
<td><strong>VT_BOOL</strong></td>
<td>If this property exists and is set to <strong>TRUE</strong>, the device can be used with Device Stage . This is meant for devices that cannot store metadata using the <strong>Device Metadata Service</strong>, but will provide metadata on the Microsoft servers.</td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




