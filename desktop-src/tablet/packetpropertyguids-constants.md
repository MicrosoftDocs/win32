---
description: Defines values that specify the packet properties.
ms.assetid: 3e8495f6-0860-4ea8-a258-784eaade85c7
title: PacketPropertyGuids Constants (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PacketPropertyGuids Constants

Defines values that specify the packet properties. The Tablet PCAPI uses globally unique identifiers (GUIDs) to identify packet properties, which in COM are constant strings.

In C++, you can access these constants in the Msinkaut.h header file, which is located in the <systemdrive>:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Include directory if you installed the SDK in the default location. In C++, these constants are WCHARs, not BSTRs. Convert them into BSTRs before use. For more information about the BSTR data type, see [Using the COM Library](using-the-com-library.md).

The following table lists the available packet property globally unique identifier (GUID) fields. Use these GUIDs to specify which properties the packet contains when you create the tablet context. To determine the range and resolution of a property, call the [**GetPropertyMetrics**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktablet-getpropertymetrics) method. The constants in the table below beginning with "STR\_" are string representations of the corresponding binary constants shown in the same table cell.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_X_or_GUID_PACKETPROPERTY_GUID_X"></span><span id="str_guid_x_or_guid_packetproperty_guid_x"></span><span id="STR_GUID_X_OR_GUID_PACKETPROPERTY_GUID_X"></span><dl> <dt><strong>STR_GUID_X or GUID_PACKETPROPERTY_GUID_X</strong></dt> </dl></td>
<td style="text-align: left;">The x-coordinate in the tablet coordinate space. Each packet contains this property by default. The origin (0,0) of the tablet is the upper-left corner.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_Y_or_GUID_PACKETPROPERTY_GUID_Y"></span><span id="str_guid_y_or_guid_packetproperty_guid_y"></span><span id="STR_GUID_Y_OR_GUID_PACKETPROPERTY_GUID_Y"></span><dl> <dt><strong>STR_GUID_Y or GUID_PACKETPROPERTY_GUID_Y</strong></dt> </dl></td>
<td style="text-align: left;">The y-coordinate in the tablet coordinate space. Each packet contains this property by default. The origin (0,0) of the tablet is the upper-left corner.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_Y_or_GUID_PACKETPROPERTY_GUID_Y"></span><span id="str_guid_y_or_guid_packetproperty_guid_y"></span><span id="STR_GUID_Y_OR_GUID_PACKETPROPERTY_GUID_Y"></span><dl> <dt><strong>STR_GUID_Y or GUID_PACKETPROPERTY_GUID_Y</strong></dt> </dl></td>
<td style="text-align: left;">The y-coordinate in the tablet coordinate space. Each packet contains this property by default. The origin (0,0) of the tablet is the upper-left corner.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_Z_or_GUID_PACKETPROPERTY_GUID_Z"></span><span id="str_guid_z_or_guid_packetproperty_guid_z"></span><span id="STR_GUID_Z_OR_GUID_PACKETPROPERTY_GUID_Z"></span><dl> <dt><strong>STR_GUID_Z or GUID_PACKETPROPERTY_GUID_Z</strong></dt> </dl></td>
<td style="text-align: left;">The z-coordinate or distance of the pen tip from the tablet surface. The <a href="/windows/desktop/api/msinkaut/ne-msinkaut-tabletpropertymetricunit"><strong>TabletPropertyMetricUnit</strong></a> enumeration type determines the unit of measurement for this property.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_PAKETSTATUS_or_GUID_PACKETPROPERTY_GUID_PACKET_STATUS"></span><span id="str_guid_paketstatus_or_guid_packetproperty_guid_packet_status"></span><span id="STR_GUID_PAKETSTATUS_OR_GUID_PACKETPROPERTY_GUID_PACKET_STATUS"></span><dl> <dt><strong>STR_GUID_PAKETSTATUS or GUID_PACKETPROPERTY_GUID_PACKET_STATUS</strong></dt> </dl></td>
<td style="text-align: left;">Contains one or more of the following flag values:<br/>
<ul>
<li>The cursor is touching the drawing surface (Value = 1).</li>
<li>The cursor is inverted. For example, the eraser end of the pen is pointing toward the surface (Value = 2).</li>
<li>Not used (Value = 4).</li>
<li>The barrel button is pressed (Value = 8).</li>
</ul></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_TIMERTICK_or_GUID_PACKETPROPERTY_GUID_TIMER_TICK"></span><span id="str_guid_timertick_or_guid_packetproperty_guid_timer_tick"></span><span id="STR_GUID_TIMERTICK_OR_GUID_PACKETPROPERTY_GUID_TIMER_TICK"></span><dl> <dt><strong>STR_GUID_TIMERTICK or GUID_PACKETPROPERTY_GUID_TIMER_TICK</strong></dt> </dl></td>
<td style="text-align: left;">The time the packet was generated.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_TIMERTICK_or_GUID_PACKETPROPERTY_GUID_TIMER_TICK"></span><span id="str_guid_timertick_or_guid_packetproperty_guid_timer_tick"></span><span id="STR_GUID_TIMERTICK_OR_GUID_PACKETPROPERTY_GUID_TIMER_TICK"></span><dl> <dt><strong>STR_GUID_TIMERTICK or GUID_PACKETPROPERTY_GUID_TIMER_TICK</strong></dt> </dl></td>
<td style="text-align: left;">The time the packet was generated.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_SERIALNUMBER_or_GUID_PACKETPROPERTY_GUID_SERIAL_NUMBER"></span><span id="str_guid_serialnumber_or_guid_packetproperty_guid_serial_number"></span><span id="STR_GUID_SERIALNUMBER_OR_GUID_PACKETPROPERTY_GUID_SERIAL_NUMBER"></span><dl> <dt><strong>STR_GUID_SERIALNUMBER or GUID_PACKETPROPERTY_GUID_SERIAL_NUMBER</strong></dt> </dl></td>
<td style="text-align: left;">The packet property for identifying the packet.<br/> This is the same value you use to retrieve the packet from the packet queue.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_NORMALPRESSURE_or_GUID_PACKETPROPERTY_GUID_NORMAL_PRESSURE"></span><span id="str_guid_normalpressure_or_guid_packetproperty_guid_normal_pressure"></span><span id="STR_GUID_NORMALPRESSURE_OR_GUID_PACKETPROPERTY_GUID_NORMAL_PRESSURE"></span><dl> <dt><strong>STR_GUID_NORMALPRESSURE or GUID_PACKETPROPERTY_GUID_NORMAL_PRESSURE</strong></dt> </dl></td>
<td style="text-align: left;">The pressure of the pen tip perpendicular to the tablet surface.<br/> The greater the pressure on the pen tip, the more ink that is drawn.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_TANGENTPRESSURE_or_GUID_PACKETPROPERTY_GUID_TANGENT_PRESSURE"></span><span id="str_guid_tangentpressure_or_guid_packetproperty_guid_tangent_pressure"></span><span id="STR_GUID_TANGENTPRESSURE_OR_GUID_PACKETPROPERTY_GUID_TANGENT_PRESSURE"></span><dl> <dt><strong>STR_GUID_TANGENTPRESSURE or GUID_PACKETPROPERTY_GUID_TANGENT_PRESSURE</strong></dt> </dl></td>
<td style="text-align: left;">The pressure of the pen tip along the plane of the tablet surface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_BUTTONPRESSURE_or_GUID_PACKETPROPERTY_GUID_BUTTON_PRESSURE"></span><span id="str_guid_buttonpressure_or_guid_packetproperty_guid_button_pressure"></span><span id="STR_GUID_BUTTONPRESSURE_OR_GUID_PACKETPROPERTY_GUID_BUTTON_PRESSURE"></span><dl> <dt><strong>STR_GUID_BUTTONPRESSURE or GUID_PACKETPROPERTY_GUID_BUTTON_PRESSURE</strong></dt> </dl></td>
<td style="text-align: left;">The pressure on a pressure sensitive button.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_XTILTORIENTATION_or_GUID_PACKETPROPERTY_GUID_X_TILT_ORIENTATION"></span><span id="str_guid_xtiltorientation_or_guid_packetproperty_guid_x_tilt_orientation"></span><span id="STR_GUID_XTILTORIENTATION_OR_GUID_PACKETPROPERTY_GUID_X_TILT_ORIENTATION"></span><dl> <dt><strong>STR_GUID_XTILTORIENTATION or GUID_PACKETPROPERTY_GUID_X_TILT_ORIENTATION</strong></dt> </dl></td>
<td style="text-align: left;">The angle between the y,z-plane and the pen and y-axis plane.<br/> Applies to a pen cursor.<br/> The value is 0 when the pen is perpendicular to the drawing surface and is positive when the pen is to the right of perpendicular.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_YTILTORIENTATION_or_GUID_PACKETPROPERTY_GUID_Y_TILT_ORIENTATION"></span><span id="str_guid_ytiltorientation_or_guid_packetproperty_guid_y_tilt_orientation"></span><span id="STR_GUID_YTILTORIENTATION_OR_GUID_PACKETPROPERTY_GUID_Y_TILT_ORIENTATION"></span><dl> <dt><strong>STR_GUID_YTILTORIENTATION or GUID_PACKETPROPERTY_GUID_Y_TILT_ORIENTATION</strong></dt> </dl></td>
<td style="text-align: left;">The angle between the x,z-plane and the pen and x-axis plane.<br/> Applies to a pen cursor.<br/> The value is 0 when the pen is perpendicular to the drawing surface and is positive when the pen is upward or away from the user.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_AZIMUTHORIENTATION_or_GUID_PACKETPROPERTY_GUID_AZIMUTH_ORIENTATION"></span><span id="str_guid_azimuthorientation_or_guid_packetproperty_guid_azimuth_orientation"></span><span id="STR_GUID_AZIMUTHORIENTATION_OR_GUID_PACKETPROPERTY_GUID_AZIMUTH_ORIENTATION"></span><dl> <dt><strong>STR_GUID_AZIMUTHORIENTATION or GUID_PACKETPROPERTY_GUID_AZIMUTH_ORIENTATION</strong></dt> </dl></td>
<td style="text-align: left;">The clockwise rotation of the cursor about the z-axis through a full circular range.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_ALTITUDEORIENTATION_or_GUID_PACKETPROPERTY_GUID_ALTITUDE_ORIENTATION"></span><span id="str_guid_altitudeorientation_or_guid_packetproperty_guid_altitude_orientation"></span><span id="STR_GUID_ALTITUDEORIENTATION_OR_GUID_PACKETPROPERTY_GUID_ALTITUDE_ORIENTATION"></span><dl> <dt><strong>STR_GUID_ALTITUDEORIENTATION or GUID_PACKETPROPERTY_GUID_ALTITUDE_ORIENTATION</strong></dt> </dl></td>
<td style="text-align: left;">The angle between the axis of the pen and the surface of the tablet.<br/> The value is 0 when the pen is parallel to the surface and 90 when the pen is perpendicular to the surface.<br/> The values are negative when the pen is inverted.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_TWISTORIENTATION_or_GUID_PACKETPROPERTY_GUID_TWIST_ORIENTATION"></span><span id="str_guid_twistorientation_or_guid_packetproperty_guid_twist_orientation"></span><span id="STR_GUID_TWISTORIENTATION_OR_GUID_PACKETPROPERTY_GUID_TWIST_ORIENTATION"></span><dl> <dt><strong>STR_GUID_TWISTORIENTATION or GUID_PACKETPROPERTY_GUID_TWIST_ORIENTATION</strong></dt> </dl></td>
<td style="text-align: left;">The clockwise rotation of the cursor about its own axis.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_PITCHROTATION_or_GUID_PACKETPROPERTY_GUID_PITCH_ROTATION"></span><span id="str_guid_pitchrotation_or_guid_packetproperty_guid_pitch_rotation"></span><span id="STR_GUID_PITCHROTATION_OR_GUID_PACKETPROPERTY_GUID_PITCH_ROTATION"></span><dl> <dt><strong>STR_GUID_PITCHROTATION or GUID_PACKETPROPERTY_GUID_PITCH_ROTATION</strong></dt> </dl></td>
<td style="text-align: left;">The packet property that indicates whether the tip is above or below a horizontal line that is perpendicular to the writing surface.<br/>
<blockquote>
[!Note]<br />
This requires a 3D digitizer.
</blockquote>
<br/> The value is positive if the tip is above the line and negative if it is below the line. For example, if you hold the pen in front of you and write on an imaginary wall, the pitch is positive if the tip is above a line extending from you to the wall.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_ROLLROTATION_or_GUID_PACKETPROPERTY_GUID_ROLL_ROTATION"></span><span id="str_guid_rollrotation_or_guid_packetproperty_guid_roll_rotation"></span><span id="STR_GUID_ROLLROTATION_OR_GUID_PACKETPROPERTY_GUID_ROLL_ROTATION"></span><dl> <dt><strong>STR_GUID_ROLLROTATION or GUID_PACKETPROPERTY_GUID_ROLL_ROTATION</strong></dt> </dl></td>
<td style="text-align: left;">The clockwise rotation of the pen around its own axis. <br/>
<blockquote>
[!Note]<br />
This requires a 3D digitizer.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_YAWROTATION_or_GUID_PACKETPROPERTY_GUID_YAW_ROTATION"></span><span id="str_guid_yawrotation_or_guid_packetproperty_guid_yaw_rotation"></span><span id="STR_GUID_YAWROTATION_OR_GUID_PACKETPROPERTY_GUID_YAW_ROTATION"></span><dl> <dt><strong>STR_GUID_YAWROTATION or GUID_PACKETPROPERTY_GUID_YAW_ROTATION</strong></dt> </dl></td>
<td style="text-align: left;">The angle of the pen to the left or right around the center of its horizontal axis when the pen is horizontal.<br/>
<blockquote>
[!Note]<br />
This requires a 3D digitizer.
</blockquote>
<br/> If you hold the pen in front of you and write on an imaginary wall, zero yaw indicates that the pen is perpendicular to the wall. The value is negative if the tip is to the left of perpendicular and positive if the tip is to the right of perpendicular.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_YAWROTATION_or_GUID_PACKETPROPERTY_GUID_YAW_ROTATION"></span><span id="str_guid_yawrotation_or_guid_packetproperty_guid_yaw_rotation"></span><span id="STR_GUID_YAWROTATION_OR_GUID_PACKETPROPERTY_GUID_YAW_ROTATION"></span><dl> <dt><strong>STR_GUID_YAWROTATION or GUID_PACKETPROPERTY_GUID_YAW_ROTATION</strong></dt> </dl></td>
<td style="text-align: left;">The angle of the pen to the left or right around the center of its horizontal axis when the pen is horizontal.<br/>
<blockquote>
[!Note]<br />
This requires a 3D digitizer.
</blockquote>
<br/> If you hold the pen in front of you and write on an imaginary wall, zero yaw indicates that the pen is perpendicular to the wall. The value is negative if the tip is to the left of perpendicular and positive if the tip is to the right of perpendicular.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_WIDTH_or_GUID_PACKETPROPERTY_GUID_WIDTH"></span><span id="str_guid_width_or_guid_packetproperty_guid_width"></span><span id="STR_GUID_WIDTH_OR_GUID_PACKETPROPERTY_GUID_WIDTH"></span><dl> <dt><strong>STR_GUID_WIDTH or GUID_PACKETPROPERTY_GUID_WIDTH</strong></dt> </dl></td>
<td style="text-align: left;">The width of the contact area on a touch digitizer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_HEIGHT_or_GUID_PACKETPROPERTY_GUID_HEIGHT"></span><span id="str_guid_height_or_guid_packetproperty_guid_height"></span><span id="STR_GUID_HEIGHT_OR_GUID_PACKETPROPERTY_GUID_HEIGHT"></span><dl> <dt><strong>STR_GUID_HEIGHT or GUID_PACKETPROPERTY_GUID_HEIGHT</strong></dt> </dl></td>
<td style="text-align: left;">The height of the contact area on a touch digitizer.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="STR_GUID_FINGERCONTACTCONFIDENCE_or_GUID_PACKETPROPERTY_GUID_FINGERCONTACTCONFIDENCE"></span><span id="str_guid_fingercontactconfidence_or_guid_packetproperty_guid_fingercontactconfidence"></span><span id="STR_GUID_FINGERCONTACTCONFIDENCE_OR_GUID_PACKETPROPERTY_GUID_FINGERCONTACTCONFIDENCE"></span><dl> <dt><strong>STR_GUID_FINGERCONTACTCONFIDENCE or GUID_PACKETPROPERTY_GUID_FINGERCONTACTCONFIDENCE</strong></dt> </dl></td>
<td style="text-align: left;">The level of confidence that there was finger contact on a touch digitizer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="STR_GUID_DEVICE_CONTACT_ID_or_GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID"></span><span id="str_guid_device_contact_id_or_guid_packetproperty_guid_device_contact_id"></span><span id="STR_GUID_DEVICE_CONTACT_ID_OR_GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID"></span><dl> <dt><strong>STR_GUID_DEVICE_CONTACT_ID or GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID</strong></dt> </dl></td>
<td style="text-align: left;">The device contact identifier for a packet.<br/></td>
</tr>
</tbody>
</table>



## Remarks

> [!Note]  
> All packet values coming from the tablet hardware are 32-bit size integers.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**IsPacketPropertySupported Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktablet-ispacketpropertysupported)
</dt> <dt>

[**GetPropertyMetrics Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktablet-getpropertymetrics)
</dt> <dt>

[**IInkTablet Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet)
</dt> </dl>

 

 




