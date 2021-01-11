---
description: In addition to device information properties, Windows Image Acquisition (WIA) devices have property values stored in the registry that applications read and write.
ms.assetid: 9948318b-7171-45fa-b46f-48f9357fdb32
title: Common Device Property Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_DPA_CONNECT_STATUS
- WIA_DPA_DEVICE_TIME
- WIA_DPA_FIRMWARE_VERSION
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Common Device Property Constants

In addition to device information properties, Windows Image Acquisition (WIA) devices have property values stored in the registry that applications read and write. They are associated with the [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) object or [**IWiaItem2**](-wia-iwiaitem2.md) object. Device properties represent device information such as connection status and device time. Each device property has an associated device property string.

The Device Property Constants listed here are common to most or all WIA hardware devices.

The prefix "WIA\_DPA\_" indicates a Device Property for All devices and is the naming convention used in C/C++. For scripting purposes these constants use the prefix "Device" and are part of the [WiaItemPropertyId](-wia-wiaitempropertyid.md) enumerated type. The corresponding member name from that script enumeration appears in parentheses next to the C/C++ constant name in the following list.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant/value</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPA_CONNECT_STATUS"></span><span id="wia_dpa_connect_status"></span><dl> <dt><strong>WIA_DPA_CONNECT_STATUS</strong></dt> <dt>DeviceConnectStatus</dt> </dl></td>
<td style="text-align: left;">The current connection status for the device. The minidriver creates and maintains this property.<br/> Type: <strong>VT_I4</strong>, Access: Read-only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/> The property can have the following possible values.<br/> 
<table>
<thead>
<tr class="header">
<th>Connect Status</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WIA_DEVICE_NOT_CONNECTED</td>
<td>Device is not connected.</td>
</tr>
<tr class="even">
<td>WIA_DEVICE_CONNECTED</td>
<td>Device is connected and operational.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPA_DEVICE_TIME"></span><span id="wia_dpa_device_time"></span><dl> <dt><strong>WIA_DPA_DEVICE_TIME</strong></dt> <dt>DeviceDeviceTime</dt> </dl></td>
<td style="text-align: left;"><p>The current clock time that is stored on the device. The minidriver creates and maintains this property.</p>
<p>Type: <strong>VT_UI2</strong> | <strong>VT_VECTOR</strong>, Access: Read/Write or Read-only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>This property is supported only by devices that have an internal clock. If the device clock can be set, this property is Read/Write; otherwise, it is Read-only.</p>
<p>WIA devices report time in a <a href="/windows/desktop/api/minwinbase/ns-minwinbase-systemtime">SYSTEMTIME</a> structure.</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPA_FIRMWARE_VERSION"></span><span id="wia_dpa_firmware_version"></span><dl> <dt><strong>WIA_DPA_FIRMWARE_VERSION</strong></dt> <dt>DeviceFirmwareVersion</dt> </dl></td>
<td style="text-align: left;"><p>The device firmware version. This value must be a string value, such as &quot;1.0.4&quot; or &quot;1.0abc&quot;. The minidriver creates and maintains this property. If the WIA minidriver does not supply a version resource, the WIA service supplies the value &quot;0.0.0.0&quot; as a default. An application reads this property to determine the version of the WIA minidriver DLL.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read-only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 
