---
description: The SafeWia object is a &\#0034;safe for scripting&\#0034; entry point for all Windows Image Acquisition (WIA) scripting functionality.
ms.assetid: 6b10bb8e-8500-4f2c-ae18-5db78ef75f74
title: SafeWia object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SafeWia
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# SafeWia object

The **SafeWia** object is a "safe for scripting" entry point for all Windows Image Acquisition (WIA) scripting functionality. Any application that uses the WIA scripting model must create a **SafeWia** or [**Wia**](-wia-wia.md) object. Use that object to enumerate and create devices and to receive notification of hardware events.

## Members

The **SafeWia** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SafeWia** object has these methods.



| Method                             | Description                                                                                                                                                                                                                |
|:-----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Create**](-wia-iwia-create.md) | The [**Create**](-wia-iwia-create.md) method of the [**Wia**](-wia-wia.md) object makes a connection to the specified WIA device, and returns an [**Item**](-wia-item.md) object that represents the device.<br/> |



 

### Properties

The **SafeWia** object has these properties.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Access type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><a href="-wia-iwia-devices.md"><strong>Devices</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Collection of <a href="-wia-deviceinfo.md"><strong>DeviceInfo</strong></a> objects that represents all of the devices installed on the computer. Read-only. <br/>
<blockquote>
[!Note]<br />
This collection is 0-based.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |
| IID<br/>                      | CLSID\_SafeWia<br/>                                                                                     |



## See also

<dl> <dt>

[**Wia**](-wia-wia.md)
</dt> </dl>

 

 




