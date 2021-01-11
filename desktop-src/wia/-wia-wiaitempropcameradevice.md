---
description: Windows Image Acquisition (WIA) hardware devices have property values that are stored in the Windows registry. For more information, see Common Device Property Constants.
ms.assetid: 7893137b-194c-4ea1-b15c-59d2f41f972a
title: Camera Device Property Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_DPC_PICTURES_TAKEN
- WIA_DPC_PICTURES_REMAINING
- WIA_DPC_EXPOSURE_MODE
- WIA_DPC_EXPOSURE_COMP
- WIA_DPC_EXPOSURE_TIME
- WIA_DPC_FNUMBER
- WIA_DPC_FLASH_MODE
- WIA_DPC_FOCUS_MODE
- WIA_DPC_FOCUS_MANUAL_DIST
- WIA_DPC_ZOOM_POSITION
- WIA_DPC_PAN_POSITION
- WIA_DPC_TILT_POSITION
- WIA_DPC_TIMER_MODE
- WIA_DPC_TIMER_VALUE
- WIA_DPC_POWER_MODE
- WIA_DPC_BATTERY_STATUS
- WIA_DPC_THUMB_WIDTH
- WIA_DPC_THUMB_HEIGHT
- WIA_DPC_PICT_WIDTH
- WIA_DPC_PICT_HEIGHT
- WIA_DPC_DIMENSION
- WIA_DPC_COMPRESSION_SETTING
- WIA_DPC_FOCUS_METERING
- WIA_DPC_TIMELAPSE_INTERVAL
- WIA_DPC_TIMELAPSE_NUMBER
- WIA_DPC_BURST_INTERVAL
- WIA_DPC_BURST_NUMBER
- WIA_DPC_EFFECT_MODE
- WIA_DPC_DIGITAL_ZOOM
- WIA_DPC_SHARPNESS
- WIA_DPC_CONTRAST
- WIA_DPC_CAPTURE_MODE
- WIA_DPC_CAPTURE_DELAY
- WIA_DPC_EXPOSURE_INDEX
- WIA_DPC_EXPOSURE_METERING_MODE
- WIA_DPC_FOCUS_METERING_MODE
- WIA_DPC_FOCUS_DISTANCE
- WIA_DPC_FOCAL_LENGTH
- WIA_DPC_RGB_GAIN
- WIA_DPC_WHITE_BALANCE
- WIA_DPC_UPLOAD_URL
- WIA_DPC_ARTIST
- WIA_DPC_COPYRIGHT_INFO
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Camera Device Property Constants

Windows Image Acquisition (WIA) hardware devices have property values that are stored in the Windows registry. For more information, see [**Common Device Property Constants**](-wia-wiaitempropcommondevice.md).

The following device property constants, with their associated strings, are specific to digital cameras. The prefix "WIA\_DPC\_" indicates a Device Property for Cameras and is the naming convention used in C/C++. For scripting purposes these constants use the prefix "CameraDevice" and are part of the [WiaItemPropertyId](-wia-wiaitempropertyid.md) enumerated type. The corresponding member name from that script enumeration appears in parentheses next to the C/C++ constant name in the following list.

> [!Note]  
> WIA does not support cameras in Windows Vista or later. For those versions of the Windows, use the Windows Portable Device (WPD) API described in the Windows Driver Development Kit (DDK) to acquire images from cameras.

 



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
<td style="text-align: left;"><span id="WIA_DPC_PICTURES_TAKEN"></span><span id="wia_dpc_pictures_taken"></span><dl> <dt><strong>WIA_DPC_PICTURES_TAKEN</strong></dt> <dt>CameraDevicePicturesTaken</dt> </dl></td>
<td style="text-align: left;">The number of pictures that the camera has taken. The minidriver creates and maintains this property.<br/> Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_PICTURES_REMAINING"></span><span id="wia_dpc_pictures_remaining"></span><dl> <dt><strong>WIA_DPC_PICTURES_REMAINING</strong></dt> <dt>CameraDevicePicturesRemaining</dt> </dl></td>
<td style="text-align: left;">The number of pictures that can be taken, given the current property settings. If these settings change, and the changes affect the size of the images that the camera device produces, the WIA minidriver should update the number of remaining pictures. The minidriver creates and maintains this property.<br/> Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a><br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_EXPOSURE_MODE"></span><span id="wia_dpc_exposure_mode"></span><dl> <dt><strong>WIA_DPC_EXPOSURE_MODE</strong></dt> <dt>CameraDeviceExposureMode</dt> </dl></td>
<td style="text-align: left;">Indicates the camera's current exposure mode. An application changes this property to control the exposure mode of the camera device.<br/> Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a><br/> The following table has the seven constants that are valid with this property.<br/> 
<table>
<thead>
<tr class="header">
<th>Exposure Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EXPOSUREMODE_MANUAL</td>
<td>The shutter speed and aperture are set by the user.</td>
</tr>
<tr class="even">
<td>EXPOSUREMODE_AUTO</td>
<td>The shutter speed and aperture are automatically set by the camera.</td>
</tr>
<tr class="odd">
<td>EXPOSUREMODE_APERTURE_PRIORITY</td>
<td>The aperture is set by the user, and the camera automatically sets the shutter speed.</td>
</tr>
<tr class="even">
<td>EXPOSUREMODE_SHUTTER_PRIORITY</td>
<td>The shutter speed is set by the user, and the camera automatically sets the aperture.</td>
</tr>
<tr class="odd">
<td>EXPOSUREMODE_PROGRAM_CREATIVE</td>
<td>The shutter speed and aperture are automatically set by the camera, optimized for still subject matter.</td>
</tr>
<tr class="even">
<td>EXPOSUREMODE_PROGRAM_ACTION</td>
<td>The shutter speed and aperture are automatically set by the camera, optimized for scenes containing fast motion.</td>
</tr>
<tr class="odd">
<td>EXPOSUREMODE_PORTRAIT</td>
<td>The shutter speed and aperture are automatically set by the camera, optimized for portrait photography.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_EXPOSURE_COMP"></span><span id="wia_dpc_exposure_comp"></span><dl> <dt><strong>WIA_DPC_EXPOSURE_COMP</strong></dt> <dt>CameraDeviceExposureComp</dt> </dl></td>
<td style="text-align: left;"><p>Allows for the adjustment of the set point of the digital camera's auto-exposure control. For example, a setting of zero does not change the factory-set auto-exposure level. The units are in &quot;stops&quot; that are scaled by a factor of 1000, to allow for fractional stop values. A setting of 2000 corresponds to two stops more exposure (four times more energy on the sensor), yielding brighter images. A setting of -1000 corresponds to one stop less exposure (one-half the energy on the sensor) yielding darker images. The setting values are in Additive System of Photographic Exposure (APEX) units. This property may be expressed as either a list or a range of values. This property is typically used only when the device has the <strong>WIA_DPC_EXPOSURE_MODE</strong> property set to EXPOSUREMODE_MANUAL.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> or WIA_PROP_LIST</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_EXPOSURE_TIME"></span><span id="wia_dpc_exposure_time"></span><dl> <dt><strong>WIA_DPC_EXPOSURE_TIME</strong></dt> <dt>CameraDeviceExposureTime</dt> </dl></td>
<td style="text-align: left;"><p>Corresponds to the shutter speed, in seconds that are scaled by 10,000. Typically, the device uses this property only when the <strong>WIA_DPC_EXPOSURE_MODE</strong> property is set to EXPOSUREMODE_MANUAL or EXPOSUREMODE_SHUTTER_PRIORITY.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_RANGE</a> or WIA_PROP_LIST</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_FNUMBER"></span><span id="wia_dpc_fnumber"></span><dl> <dt><strong>WIA_DPC_FNUMBER</strong></dt> <dt>CameraDeviceFNumber</dt> </dl></td>
<td style="text-align: left;"><p>Corresponds to the aperture of the lens, in units of the f-stop number scaled by 100. The setting of this property is typically valid only when the <strong>WIA_DPC_EXPOSURE_MODE</strong> property is set to EXPOSUREMODE_MANUAL or EXPOSUREMODE_APERTURE_PRIORITY.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_FLASH_MODE"></span><span id="wia_dpc_flash_mode"></span><dl> <dt><strong>WIA_DPC_FLASH_MODE</strong></dt> <dt>CameraDeviceFlashMode</dt> </dl></td>
<td style="text-align: left;"><p>Defines the current flash mode setting for the camera device. The device driver enumerates the supported values of this property. An application writes this property to set the flash mode for the camera device.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the six constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Flash Mode</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FLASHMODE_AUTO</td>
<td>The camera device determines the proper flash settings.</td>
</tr>
<tr class="even">
<td>FLASHMODE_FILL</td>
<td>The camera device is configured to flash regardless of current lighting conditions.</td>
</tr>
<tr class="odd">
<td>FLASHMODE_OFF</td>
<td>The camera device is configured <em>not</em> to flash for any picture taken.</td>
</tr>
<tr class="even">
<td>FLASHMODE_REDEYE_AUTO</td>
<td>The camera device determines the proper flash settings using red-eye reduction, regardless of current lighting conditions.</td>
</tr>
<tr class="odd">
<td>FLASHMODE_REDEYE_FILL</td>
<td>The camera device is configured to use red-eye reduction and flash regardless of current lighting conditions.</td>
</tr>
<tr class="even">
<td>FLASHMODE_EXTERNALSYNC</td>
<td>The camera device is configured to synchronize with external flash units.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_FOCUS_MODE"></span><span id="wia_dpc_focus_mode"></span><dl> <dt><strong>WIA_DPC_FOCUS_MODE</strong></dt> <dt>CameraDeviceFocusMode</dt> </dl></td>
<td style="text-align: left;"><p>Defines the current focus mode setting for the camera device. The device driver enumerates the supported values of this property. An application writes this property to set the focus mode for the camera device.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the three constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Focus Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FOCUSMODE_MANUAL</td>
<td>The camera device is configured to allow the user to focus manually.</td>
</tr>
<tr class="even">
<td>FOCUSMODE_AUTO</td>
<td>The camera device is configured to focus automatically.</td>
</tr>
<tr class="odd">
<td>FOCUSMODE_MACROAUTO</td>
<td>The camera device is configured to focus automatically using short-range macro settings.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_FOCUS_MANUAL_DIST"></span><span id="wia_dpc_focus_manual_dist"></span><dl> <dt><strong>WIA_DPC_FOCUS_MANUAL_DIST</strong></dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_ZOOM_POSITION"></span><span id="wia_dpc_zoom_position"></span><dl> <dt><strong>WIA_DPC_ZOOM_POSITION</strong></dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_PAN_POSITION"></span><span id="wia_dpc_pan_position"></span><dl> <dt><strong>WIA_DPC_PAN_POSITION</strong></dt> <dt>CameraDevicePanPosition</dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_TILT_POSITION"></span><span id="wia_dpc_tilt_position"></span><dl> <dt><strong>WIA_DPC_TILT_POSITION</strong></dt> <dt>CameraDeviceTiltPosition</dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_TIMER_MODE"></span><span id="wia_dpc_timer_mode"></span><dl> <dt><strong>WIA_DPC_TIMER_MODE</strong></dt> <dt>CameraDeviceTimerMode</dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_TIMER_VALUE"></span><span id="wia_dpc_timer_value"></span><dl> <dt><strong>WIA_DPC_TIMER_VALUE</strong></dt> <dt>CameraDeviceTimerValue</dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_POWER_MODE"></span><span id="wia_dpc_power_mode"></span><dl> <dt><strong>WIA_DPC_POWER_MODE</strong></dt> <dt>CameraDevicePowerMode</dt> </dl></td>
<td style="text-align: left;"><p>Defines the current power source for the camera device. An application reads this property to determine what power source the camera is using.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p>
<p>The following table has the two constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Power Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>POWERMODE_LINE</td>
<td>The camera device is operating on a power adapter.</td>
</tr>
<tr class="even">
<td>POWERMODE_BATTERY</td>
<td>The camera device is operating on battery power.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_BATTERY_STATUS"></span><span id="wia_dpc_battery_status"></span><dl> <dt><strong>WIA_DPC_BATTERY_STATUS</strong></dt> <dt>CameraDeviceBatteryStatus</dt> </dl></td>
<td style="text-align: left;"><p>The percentage of battery power that is left to operate the camera device. This value should be an integer from 0 through 100. An application reads this property to determine the remaining battery life of the camera device.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_THUMB_WIDTH"></span><span id="wia_dpc_thumb_width"></span><dl> <dt><strong>WIA_DPC_THUMB_WIDTH</strong></dt> <dt>CameraDeviceThumbWidth</dt> </dl></td>
<td style="text-align: left;"><p>The width, in pixels, of a thumbnail image to use for newly captured images. An application reads this value to get an estimated size for displaying thumbnails in its user interface.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write (<a href="-wia-property-attributes.md">WIA_PROP_LIST</a>) or Read Only (WIA_PROP_NONE), Valid values: WIA_PROP_LIST or WIA_PROP_NONE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_THUMB_HEIGHT"></span><span id="wia_dpc_thumb_height"></span><dl> <dt><strong>WIA_DPC_THUMB_HEIGHT</strong></dt> <dt>CameraDeviceThumbHeight</dt> </dl></td>
<td style="text-align: left;"><p>The width, in pixels, of a thumbnail image to use for newly captured images. An application reads this value to get an estimated size for displaying thumbnails in its user interface.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write (<a href="-wia-property-attributes.md">WIA_PROP_LIST</a>) or Read Only (WIA_PROP_NONE), Valid values: WIA_PROP_LIST or WIA_PROP_NONE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_PICT_WIDTH"></span><span id="wia_dpc_pict_width"></span><dl> <dt><strong>WIA_DPC_PICT_WIDTH</strong></dt> <dt>CameraDevicePictWidth</dt> </dl></td>
<td style="text-align: left;"><p>The width in pixels to use for newly captured images. The list of valid values for this property has a one-to-one correspondence to the list of valid values for the <strong>WIA_DPC_PICT_HEIGHT</strong> property. If the individual width and height are linearly settable and orthogonal to each other, they may be expressed as a range.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_PICT_HEIGHT"></span><span id="wia_dpc_pict_height"></span><dl> <dt><strong>WIA_DPC_PICT_HEIGHT</strong></dt> <dt>CameraDevicePictHeight</dt> </dl></td>
<td style="text-align: left;"><p>The height in pixels to use for newly captured images. The list of valid values for this property has a one-to-one correspondence with the list of valid values for the <strong>WIA_DPC_PICT_WIDTH</strong> property. If the individual width and height are linearly settable and orthogonal to each other, they may be expressed as a range.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_DIMENSION"></span><span id="wia_dpc_dimension"></span><dl> <dt><strong>WIA_DPC_DIMENSION</strong></dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_COMPRESSION_SETTING"></span><span id="wia_dpc_compression_setting"></span><dl> <dt><strong>WIA_DPC_COMPRESSION_SETTING</strong></dt> <dt>CameraDeviceCompressionSetting</dt> </dl></td>
<td style="text-align: left;"><p>Intended to be approximately linear with respect to perceived image quality over a broad range of scene content, and it contains either a range or a list of integers. Smaller integers are used to represent lower quality (that is, maximum compression), whereas larger integers are used to represent higher quality (that is, minimum compression). Any available settings on a device are relative only to that device and are therefore device specific.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_FOCUS_METERING"></span><span id="wia_dpc_focus_metering"></span><dl> <dt><strong>WIA_DPC_FOCUS_METERING</strong></dt> </dl></td>
<td style="text-align: left;"><p>Reserved, do not use.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read Only, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_TIMELAPSE_INTERVAL"></span><span id="wia_dpc_timelapse_interval"></span><dl> <dt><strong>WIA_DPC_TIMELAPSE_INTERVAL</strong></dt> <dt>CameraDeviceTimelapseInterval</dt> </dl></td>
<td style="text-align: left;"><p>The time, in milliseconds, between image captures in a time-lapse capture operation.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a>, WIA_PROP_LIST, or WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_TIMELAPSE_NUMBER"></span><span id="wia_dpc_timelapse_number"></span><dl> <dt><strong>WIA_DPC_TIMELAPSE_NUMBER</strong></dt> <dt>CameraDeviceTimelapseNumber</dt> </dl></td>
<td style="text-align: left;"><p>The number of images the device attempts to capture during a time-lapse capture.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a>, WIA_PROP_LIST, or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_BURST_INTERVAL"></span><span id="wia_dpc_burst_interval"></span><dl> <dt><strong>WIA_DPC_BURST_INTERVAL</strong></dt> <dt>CameraDeviceBurstInterval</dt> </dl></td>
<td style="text-align: left;"><p>The time, in milliseconds, between image captures during a burst operation.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a>, WIA_PROP_LIST, or WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_BURST_NUMBER"></span><span id="wia_dpc_burst_number"></span><dl> <dt><strong>WIA_DPC_BURST_NUMBER</strong></dt> <dt>CameraDeviceBurstNumber</dt> </dl></td>
<td style="text-align: left;"><p>The number of images the device attempts to capture during a burst operation.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a>, WIA_PROP_LIST, or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_EFFECT_MODE"></span><span id="wia_dpc_effect_mode"></span><dl> <dt><strong>WIA_DPC_EFFECT_MODE</strong></dt> <dt>CameraDeviceEffectMode</dt> </dl></td>
<td style="text-align: left;"><p>Specifies the special image acquisition mode of the camera.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the three constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Effect Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EFFECTMODE_STANDARD</td>
<td>Capture an image in the standard mode for the camera.</td>
</tr>
<tr class="even">
<td>EFFECTMODE_BW</td>
<td>Capture a grayscale image.</td>
</tr>
<tr class="odd">
<td>EFFECTMODE_SEPIA</td>
<td>Capture a sepia image.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_DIGITAL_ZOOM"></span><span id="wia_dpc_digital_zoom"></span><dl> <dt><strong>WIA_DPC_DIGITAL_ZOOM</strong></dt> <dt>CameraDeviceDigitalZoom</dt> </dl></td>
<td style="text-align: left;"><p>The effective zoom ratio of the digital camera's acquired image, scaled by a factor of 10. A value of 10 corresponds to the absence of digital zoom (1X), which is the standard scene size captured by the camera. A value of 20 corresponds to a 2X zoom, where one-quarter of the standard scene size is captured by the camera.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_SHARPNESS"></span><span id="wia_dpc_sharpness"></span><dl> <dt><strong>WIA_DPC_SHARPNESS</strong></dt> <dt>CameraDeviceSharpness</dt> </dl></td>
<td style="text-align: left;"><p>The perceived sharpness of a captured image. This property can use either a list of values or a range of values. The minimum value represents the least amount of sharpness, whereas the maximum value represents the maximum sharpness. Typically a value in the middle of the range represents normal, or default, sharpness.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_CONTRAST"></span><span id="wia_dpc_contrast"></span><dl> <dt><strong>WIA_DPC_CONTRAST</strong></dt> <dt>CameraDeviceContrast</dt> </dl></td>
<td style="text-align: left;"><p>The perceived contrast of a captured image. This property can contain either a list of values or a range of values. The minimum supported value represents the least amount of contrast, whereas the maximum value represents the most contrast. Typically, a value in the middle of the range represents normal, or default, contrast.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_CAPTURE_MODE"></span><span id="wia_dpc_capture_mode"></span><dl> <dt><strong>WIA_DPC_CAPTURE_MODE</strong></dt> <dt>CameraDeviceCaptureMode</dt> </dl></td>
<td style="text-align: left;"><p>Sets the image capture mode.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the three constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Capture Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CAPTUREMODE_NORMAL</td>
<td>Normal mode for the camera.</td>
</tr>
<tr class="even">
<td>CAPTUREMODE_BURST</td>
<td>Capture more than one image in quick succession as defined by the values of the <strong>WIA_DPC_BURST_NUMBER</strong> and <strong>WIA_DPC_BURST_INTERVAL</strong> properties.</td>
</tr>
<tr class="odd">
<td>CAPTUREMODE_TIMELAPSE</td>
<td>Capture more than one image in succession as defined by the <strong>WIA_DPC_TIMELAPSE_NUMBER</strong> and <strong>WIA_DPC_TIMELAPSE_INTERVAL</strong> properties.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_CAPTURE_DELAY"></span><span id="wia_dpc_capture_delay"></span><dl> <dt><strong>WIA_DPC_CAPTURE_DELAY</strong></dt> <dt>CameraDeviceCaptureDelay</dt> </dl></td>
<td style="text-align: left;"><p>The value representing the amount of time delay, in milliseconds, that should be inserted between the capture trigger and the actual initiation of the data capture. This property is not intended to be used to describe the time between frames for single-initiation, multiple captures such as burst or time lapse, which have separate interval properties <strong>WIA_DPC_BURST_INTERVAL</strong> and <strong>WIA_DPC_TIMELAPSE_INTERVAL</strong>. In those cases, it still serves as an initial delay before the first image in the series is captured, independent of the time between frames. For no precapture delay, this property should be set to zero.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_EXPOSURE_INDEX"></span><span id="wia_dpc_exposure_index"></span><dl> <dt><strong>WIA_DPC_EXPOSURE_INDEX</strong></dt> <dt>CameraDeviceExposureIndex</dt> </dl></td>
<td style="text-align: left;"><p>Allows for the emulation of film speed settings on a digital camera. The settings correspond to the ISO designations (ASA/DIN). Typically, a device supports discrete enumerated values, but continuous control over a range of values is possible. A value of 0xFFFF corresponds to the Automatic ISO setting.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_EXPOSURE_METERING_MODE"></span><span id="wia_dpc_exposure_metering_mode"></span><dl> <dt><strong>WIA_DPC_EXPOSURE_METERING_MODE</strong></dt> <dt>CameraDeviceExposureMeteringMode</dt> </dl></td>
<td style="text-align: left;"><p>Specifies the mode the camera uses to automatically adjust the exposure setting.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>

<table>
<thead>
<tr class="header">
<th>Exposure Metering Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EXPOSUREMETERING_AVERAGE</td>
<td>Set the exposure based on an average of the entire scene.</td>
</tr>
<tr class="even">
<td>EXPOSUREMETERING_CENTERWEIGHT</td>
<td>Set the exposure based on a center-weighted average.</td>
</tr>
<tr class="odd">
<td>EXPOSUREMETERING_MULTISPOT</td>
<td>Set the exposure based on a multispot pattern.</td>
</tr>
<tr class="even">
<td>EXPOSUREMETERING_CENTERSPOT</td>
<td>Set the exposure based on a center spot.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_FOCUS_METERING_MODE"></span><span id="wia_dpc_focus_metering_mode"></span><dl> <dt><strong>WIA_DPC_FOCUS_METERING_MODE</strong></dt> <dt>CameraDeviceFocusMeteringMode</dt> </dl></td>
<td style="text-align: left;"><p>Specifies the mode the camera uses to automatically adjust the focus.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following table has the two constants that are valid with this property.</p>

<table>
<thead>
<tr class="header">
<th>Focus Metering Mode</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FOCUSMETERING_CENTERSPOT</td>
<td>Adjust the focus based on a center spot.</td>
</tr>
<tr class="even">
<td>FOCUSMETERING_MULTISPOT</td>
<td>Adjust the focus based on a multispot pattern.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_FOCUS_DISTANCE"></span><span id="wia_dpc_focus_distance"></span><dl> <dt><strong>WIA_DPC_FOCUS_DISTANCE</strong></dt> <dt>CameraDeviceFocusDistance</dt> </dl></td>
<td style="text-align: left;"><p>The distance, in millimeters, between the image-capturing plane of the digital camera and the point of focus. A value of 0xFFFF corresponds to a setting greater than 655 meters.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a> or WIA_PROP_RANGE</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_FOCAL_LENGTH"></span><span id="wia_dpc_focal_length"></span><dl> <dt><strong>WIA_DPC_FOCAL_LENGTH</strong></dt> <dt>CameraDeviceFocalLength</dt> </dl></td>
<td style="text-align: left;"><p>The 35mm-equivalent focal length. The values of this property correspond to the focal length in millimeters multiplied by 100. The focal length determines the optical zoom.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_RGB_GAIN"></span><span id="wia_dpc_rgb_gain"></span><dl> <dt><strong>WIA_DPC_RGB_GAIN</strong></dt> <dt>CameraDeviceRGBGain</dt> </dl></td>
<td style="text-align: left;"><p>A null-terminated Unicode string that represents the red, green, and blue gain applied to image data, respectively. For example, &quot;4:25:50&quot; represents a red gain of 4, a green gain of 25, and a blue gain of 50.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_WHITE_BALANCE"></span><span id="wia_dpc_white_balance"></span><dl> <dt><strong>WIA_DPC_WHITE_BALANCE</strong></dt> <dt>CameraDeviceWhiteBalance</dt> </dl></td>
<td style="text-align: left;"><p>Specifies how the digital camera weights color channels.</p>
<p>Type: <strong>VT_I4</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_LIST</a></p>
<p>The following is a list of possible values for this property.</p>

<table>
<thead>
<tr class="header">
<th>White Balance</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WHITEBALANCE_MANUAL</td>
<td>The white balance is set directly using the <strong>WIA_DPC_RGB_GAIN</strong> property.</td>
</tr>
<tr class="even">
<td>WHITEBALANCE_AUTO</td>
<td>The camera uses an automatic mechanism to set the white balance.</td>
</tr>
<tr class="odd">
<td>WHITEBALANCE_ONEPUSH_AUTO</td>
<td>The camera determines the white balance setting when a user presses the capture button while pointing the camera at a white surface.</td>
</tr>
<tr class="even">
<td>WHITEBALANCE_DAYLIGHT</td>
<td>The camera sets the white balance to a value appropriate for use in daylight conditions.</td>
</tr>
<tr class="odd">
<td>WHITEBALANCE_FLORESCENT</td>
<td>The camera sets the white balance to a value appropriate for use with a fluorescent light source.</td>
</tr>
<tr class="even">
<td>WHITEBALANCE_TUNGSTEN</td>
<td>The camera sets the white balance to a value appropriate for use with a tungsten light source.</td>
</tr>
<tr class="odd">
<td>WHITEBALANCE_FLASH</td>
<td>The camera sets the white balance to a value appropriate for use with an electronic flash.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_UPLOAD_URL"></span><span id="wia_dpc_upload_url"></span><dl> <dt><strong>WIA_DPC_UPLOAD_URL</strong></dt> <dt>CameraDeviceUploadURL</dt> </dl></td>
<td style="text-align: left;"><p>Describes a URL. The URL described by this proroperty is one that images or objects, after they are acquired from the device, can be uploaded to—according to one of the following scenarios.</p>
<ul>
<li>A WIA application reads this property and allows the user to automatically upload images to the URL.</li>
<li>An application sets the URL, and other devices (kiosks and so forth) use this property.</li>
</ul>
<p>Microsoft Windows does not upload images by itself.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="WIA_DPC_ARTIST"></span><span id="wia_dpc_artist"></span><dl> <dt><strong>WIA_DPC_ARTIST</strong></dt> <dt>CameraDeviceArtist</dt> </dl></td>
<td style="text-align: left;"><p>The name of the owner ( which is the current user) of the device. The device uses this property to populate the Artist field in every EXIF image that it captures.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="WIA_DPC_COPYRIGHT_INFO"></span><span id="wia_dpc_copyright_info"></span><dl> <dt><strong>WIA_DPC_COPYRIGHT_INFO</strong></dt> <dt>CameraDeviceCopyrightInfo</dt> </dl></td>
<td style="text-align: left;"><p>The copyright notification. The device uses this property to populate the Copyright field in every EXIF image that it captures.</p>
<p>Type: <strong>VT_BSTR</strong>, Access: Read/Write, Valid values: <a href="-wia-property-attributes.md">WIA_PROP_NONE</a></p></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




