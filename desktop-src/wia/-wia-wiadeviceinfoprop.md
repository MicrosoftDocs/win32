---
description: Device Information Property Constants - Device Information Properties are properties that describe the setup and installation of the device.
ms.assetid: ff6771ac-491e-4765-8cfe-11c7efc1c971
title: Device Information Property Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_DIP_DEV_ID
- WIA_DIP_VEND_DESC
- WIA_DIP_DEV_DESC
- WIA_DIP_DEV_TYPE
- WIA_DIP_PORT_NAME
- WIA_DIP_DEV_NAME
- WIA_DIP_SERVER_NAME
- WIA_DIP_REMOTE_DEV_ID
- WIA_DIP_UI_CLSID
- WIA_DIP_HW_CONFIG
- WIA_DIP_BAUDRATE
- WIA_DIP_STI_GEN_CAPABILITIES
- WIA_DIP_WIA_VERSION
- WIA_DIP_DRIVER_VERSION
- WIA_DIP_PNP_ID
- WIA_DIP_STI_DRIVER_VERSION
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Device Information Property Constants

Device Information Properties are properties that describe the setup and installation of the device. These properties are available through the [**IWiaDevMgr**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiadevmgr) or [**IWiaDevMgr2**](-wia-iwiadevmgr2.md) interfaces and also through the root item. Device information properties are prefixed with "WIA\_DIP\_" (Device Information Property) and are supplied by Windows Image Acquisition (WIA). For scripting purposes, these constants use the prefix "DeviceInfo" and are part of the [WiaDeviceInfoPropertyId](-wia-wiadeviceinfopropertyid.md) enumerated type. The corresponding member name from that script enumeration appears in parentheses next to the C/C++ constant name in the following list.



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
<td style="text-align: left;"><span id="WIA_DIP_DEV_ID"></span><span id="wia_dip_dev_id"></span><dl> <dt><strong>WIA_DIP_DEV_ID</strong></dt> <dt>DeviceInfoDevId</dt> </dl></td>
<td style="text-align: left;">The device ID string for the WIA minidriver. The WIA service creates and maintains this property.<br/> Type: VT_BSTR, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_VEND_DESC"></span><span id="wia_dip_vend_desc"></span><dl> <dt><strong>WIA_DIP_VEND_DESC</strong></dt> <dt>DeviceInfoVendDesc</dt> </dl></td>
<td style="text-align: left;">The vendor description string for the WIA minidriver. The vendor description is obtained from the INF file. An application reads this property to get a description of the device vendor. The WIA service creates and maintains this property.<br/> Type: VT_BSTR, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_DEV_DESC"></span><span id="wia_dip_dev_desc"></span><dl> <dt><strong>WIA_DIP_DEV_DESC</strong></dt> <dt>DeviceInfoDevDesc</dt> </dl></td>
<td style="text-align: left;">The device description string for the WIA minidriver. The WIA service creates and maintains this property. The device description string this property contains is obtained from the INF file. An application reads this property to get a description of the device.<br/> Type: VT_BSTR, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_DEV_TYPE"></span><span id="wia_dip_dev_type"></span><dl> <dt><strong>WIA_DIP_DEV_TYPE</strong></dt> <dt>DeviceInfoDevType</dt> </dl></td>
<td style="text-align: left;">The device type and device subtype. The WIA service creates and maintains this property. Use the GET_STIDEVICE_TYPE macro to get the device type. The device type and subtype are obtained from the INF file. An application reads this property to determine whether it is using a scanner, camera, or video device.<br/> Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/> Currently, device types are defined as follows. The asterisk * indicates that the device type is not supported by Windows Vista and later. The double asterisk ** indicates that the device type is not supported by either Windows Server 2003, Windows Vista, or later. <br/> 
<table>
<thead>
<tr class="header">
<th>Type</th>
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>StiDeviceTypeDefault</td>
<td>0x0000</td>
<td>Default device</td>
</tr>
<tr class="even">
<td>StiDeviceTypeScanner</td>
<td>0x0001</td>
<td>Scanner device (See the <a href="-wia-wiaitempropscannerdevice.md"><strong>WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES</strong></a> to determine if the scanner is flatbed or sheet-fed.)</td>
</tr>
<tr class="odd">
<td>StiDeviceTypeDigitalCamera*</td>
<td>0x0002</td>
<td>Camera device</td>
</tr>
<tr class="even">
<td>StiDeviceTypeStreamingVideo**</td>
<td>0x0003</td>
<td>Video device</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_PORT_NAME"></span><span id="wia_dip_port_name"></span><dl> <dt><strong>WIA_DIP_PORT_NAME</strong></dt> <dt>DeviceInfoPortName</dt> </dl></td>
<td style="text-align: left;"><p>The installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property. An application reads this property to determine the port name.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_DEV_NAME"></span><span id="wia_dip_dev_name"></span><dl> <dt><strong>WIA_DIP_DEV_NAME</strong></dt> <dt>DeviceInfoDevName</dt> </dl></td>
<td style="text-align: left;"><p>The name of the device. The WIA service creates and maintains this property. The device name contained in this property is obtained from the INF file. An application reads this property to obtain the name of the device.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_SERVER_NAME"></span><span id="wia_dip_server_name"></span><dl> <dt><strong>WIA_DIP_SERVER_NAME</strong></dt> <dt>DeviceInfoServerName</dt> </dl></td>
<td style="text-align: left;"><p>The name of the server that the WIA minidriver is running on. This property is optional for Windows XP and later.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_REMOTE_DEV_ID"></span><span id="wia_dip_remote_dev_id"></span><dl> <dt><strong>WIA_DIP_REMOTE_DEV_ID</strong></dt> <dt>DeviceInfoRemoteDevId</dt> </dl></td>
<td style="text-align: left;"><p>The device ID of the WIA device that is installed on a remote computer. The WIA service creates and maintains this property. It is only used internally by the WIA service.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_UI_CLSID"></span><span id="wia_dip_ui_clsid"></span><dl> <dt><strong>WIA_DIP_UI_CLSID</strong></dt> <dt>DeviceInfoUIClsid</dt> </dl></td>
<td style="text-align: left;"><p>The vendor-supplied CLSID for any UI extension COM object that is installed with the WIA minidriver. The WIA service creates and maintains this property. The UI CLSID value contained in this property is obtained from the INF file. If no UI CLSID is specified, the WIA service supplies a default value. This property is only used internally by the WIA service when UI is being displayed.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_HW_CONFIG"></span><span id="wia_dip_hw_config"></span><dl> <dt><strong>WIA_DIP_HW_CONFIG</strong></dt> <dt>DeviceInfoHwConfig</dt> </dl></td>
<td style="text-align: left;"><p>The type of connection that the device is using. The WIA service creates and maintains this property, and only the WIA service can change it.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The property can have the following possible values.</p>

<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Generic WDM device</td>
</tr>
<tr class="even">
<td>2</td>
<td>SCSI device</td>
</tr>
<tr class="odd">
<td>4</td>
<td>USB device</td>
</tr>
<tr class="even">
<td>8</td>
<td>Serial device</td>
</tr>
<tr class="odd">
<td>16</td>
<td>Parallel device</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_BAUDRATE"></span><span id="wia_dip_baudrate"></span><dl> <dt><strong>WIA_DIP_BAUDRATE</strong></dt> <dt>DeviceInfoBaudRate</dt> </dl></td>
<td style="text-align: left;"><p>The current baud rate setting for the device. The WIA service creates and maintains this property. The value should be &quot;Empty&quot; if the device is not connected by a serial cable.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_STI_GEN_CAPABILITIES"></span><span id="wia_dip_sti_gen_capabilities"></span><dl> <dt><strong>WIA_DIP_STI_GEN_CAPABILITIES</strong></dt> <dt>DeviceInfoStiGenCapabilities</dt> </dl></td>
<td style="text-align: left;"><p>The generic STI capabilities for the device as obtained from the INF file. The WIA service creates and maintains this property. An application reads this property to determine the generic STI capabilities of the device.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_WIA_VERSION"></span><span id="wia_dip_wia_version"></span><dl> <dt><strong>WIA_DIP_WIA_VERSION</strong></dt> <dt>DeviceInfoWiaVersion</dt> </dl></td>
<td style="text-align: left;"><p>The number (as a string) of the current WIA version that is installed on the system. An application reads this property to determine the version of WIA that is installed on the system. The WIA service creates and maintains this property. This property is available in Windows XP and later.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_DRIVER_VERSION"></span><span id="wia_dip_driver_version"></span><dl> <dt><strong>WIA_DIP_DRIVER_VERSION</strong></dt> <dt>DeviceInfoDriverVersion</dt> </dl></td>
<td style="text-align: left;"><p>The current DLL version of the WIA minidriver. The WIA service creates and maintains this property. This property is available in Windows XP and later.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DIP_PNP_ID"></span><span id="wia_dip_pnp_id"></span><dl> <dt><strong>WIA_DIP_PNP_ID</strong></dt> <dt>DeviceInfoPNPID</dt> </dl></td>
<td style="text-align: left;"><p>The current PnP id for the device. The WIA service creates and maintains this property. This property is available in Windows Vista and later.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DIP_STI_DRIVER_VERSION"></span><span id="wia_dip_sti_driver_version"></span><dl> <dt><strong>WIA_DIP_STI_DRIVER_VERSION</strong></dt> <dt>DeviceInfoStiDriverVersion</dt> </dl></td>
<td style="text-align: left;"><p>The generic STI driver version. The WIA service creates and maintains this property. An application reads this property to determine the generic STI driver version. This property is available in Windows Vista and later.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




