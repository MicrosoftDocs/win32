---
description: The following table lists packet property GUIDs used by the PACKET\_PROPERTY structure.
ms.assetid: d3e94b57-3078-4a84-b58a-faa31bdff79e
title: PacketProperty GUIDs
ms.topic: article
ms.date: 05/31/2018
---

# PacketProperty GUIDs

The following table lists packet property GUIDs used by the [**PACKET\_PROPERTY**](/windows/desktop/api/tpcshrd/ns-tpcshrd-packet_property) structure.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>GUID</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GUID_ALTITUDE_ORIENTATION<br/></td>
<td>Angle between the axis of the pen and the surface of the tablet. The value is 0 when the pen is parallel to the surface and 90 when the pen is perpendicular to the surface. The values are negative when the pen is inverted.<br/></td>
</tr>
<tr class="even">
<td>GUID_AZIMUTH_ORIENTATION<br/></td>
<td>Clockwise rotation of the cursor around the z-axis through a full circular range.<br/></td>
</tr>
<tr class="odd">
<td>GUID_BOXNUMBER<br/></td>
<td>The GUID that is used to retrieve the box number for an ink recognition alternate when the recognizer is operating in box mode.<br/></td>
</tr>
<tr class="even">
<td>GUID_BUTTON_PRESSURE<br/></td>
<td>Pressure on a pressure-sensitive button.<br/></td>
</tr>
<tr class="odd">
<td>GUID_NORMAL_PRESSURE<br/></td>
<td>The GUID for the PacketProperty object that represents pressure of the pen tip perpendicular to the tablet surface. The greater the pressure put on the pen tip, the more ink that is drawn.<br/></td>
</tr>
<tr class="even">
<td>GUID_PACKET_STATUS<br/></td>
<td>Contains one or more of the following flag values:<br/>
<ul>
<li>The cursor is touching the drawing surface (Value = 1).</li>
<li>The cursor is inverted. For example, the eraser end of the pen is pointing toward the surface (Value = 2).</li>
<li>Not used (Value = 4).</li>
<li>The barrel button is pressed (Value = 8).</li>
</ul></td>
</tr>
<tr class="odd">
<td>GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID<br/></td>
<td>The device contact identifier for a packet.<br/></td>
</tr>
<tr class="even">
<td>GUID_SERIAL_NUMBER<br/></td>
<td>Identifies the packet. This is the same value you use to retrieve the packet from the packet queue.<br/></td>
</tr>
<tr class="odd">
<td>GUID_TANGENT_PRESSURE<br/></td>
<td>The GUID for the PacketProperty object that represents pressure of the pen tip along the plane of the tablet surface.<br/></td>
</tr>
<tr class="even">
<td>GUID_TIMER_TICK<br/></td>
<td>Time the packet was generated.<br/></td>
</tr>
<tr class="odd">
<td>GUID_TWIST_ORIENTATION<br/></td>
<td>Clockwise rotation of the cursor around its own axis.<br/></td>
</tr>
<tr class="even">
<td>GUID_X<br/></td>
<td>The x-coordinate in the tablet coordinate space. Each packet contains this property by default. The origin (0,0) of the tablet is the upper-left corner.<br/></td>
</tr>
<tr class="odd">
<td>GUID_X_TILT_ORIENTATION<br/></td>
<td>For a pen cursor, the x-tilt orientation is the angle between the y,z-plane and the pen and y-axis plane. The value is 0 when the pen is perpendicular to the drawing surface and is positive when the pen is to the right of perpendicular.<br/></td>
</tr>
<tr class="even">
<td>GUID_Y<br/></td>
<td>The y-coordinate in the tablet coordinate space. Each packet contains this property by default. The origin (0,0) of the tablet is the upper-left corner.<br/></td>
</tr>
<tr class="odd">
<td>GUID_Y_TILT_ORIENTATION<br/></td>
<td>For a pen cursor, the y-tilt orientation is the angle between the x,z-plane and the pen and x-axis plane. The value is 0 when the pen is perpendicular to the drawing surface and is positive when the pen is upward, or away from the user.<br/></td>
</tr>
<tr class="even">
<td>GUID_Z<br/></td>
<td>The z-coordinate or distance of the pen tip from the tablet surface. The <a href="/windows/desktop/api/tpcshrd/ne-tpcshrd-property_units"><strong>PROPERTY_UNITS</strong></a> enumeration type determines the unit of measurement for this property. <br/></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> The TangentPressure field represents pressure along the plane of the tablet surface; the NormalPressure field represents pressure perpendicular to the plane of the tablet surface.

 

 

 




