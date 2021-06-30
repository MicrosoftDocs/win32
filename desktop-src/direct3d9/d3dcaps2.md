---
description: See a list of D3DCAPS2 driver capability flags. Includes the definitions, values, and descriptions with links to APIs.
ms.assetid: 0c0c65fc-f953-4379-a6d0-6ce447a0c183
title: D3DCAPS2
ms.topic: article
ms.date: 05/31/2018
---

# D3DCAPS2

Driver capability flags.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td>#define</td>
<td>Value</td>
<td>Description</td>
</tr>
<tr class="even">
<td>D3DCAPS2_CANAUTOGENMIPMAP</td>
<td>0x40000000L</td>
<td>The driver is capable of automatically generating mipmaps. For more information, see <a href="automatic-generation-of-mipmaps.md">Automatic Generation of Mipmaps (Direct3D 9)</a>.</td>
</tr>
<tr class="odd">
<td>D3DCAPS2_CANCALIBRATEGAMMA</td>
<td>0x00100000L</td>
<td>The system has a calibrator installed that can automatically adjust the gamma ramp so that the result is identical on all systems that have a calibrator. To invoke the calibrator when setting new gamma levels, use the D3DSGR_CALIBRATE flag when calling <a href="/windows/desktop/api"><strong>SetGammaRamp</strong></a>. Calibrating gamma ramps incurs some processing overhead and should not be used frequently.</td>
</tr>
<tr class="even">
<td>D3DCAPS2_CANSHARERESOURCE</td>
<td>0x80000000L</td>
<td>The device can create sharable resources. Methods that create resources can set non-NULL values for their <a href="/windows/desktop/api/dxgi/nf-dxgi-idxgiresource-getsharedhandle"><strong>pSharedHandle</strong></a> parameters. 
<table>
<tbody>
<tr class="odd">
<td>Differences between Direct3D 9 and Direct3D 9Ex:<br/> This flag is available in Direct3D 9Ex only.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>D3DCAPS2_CANMANAGERESOURCE</td>
<td>0x10000000L</td>
<td>The driver is capable of managing resources. On such drivers, D3DPOOL_MANAGED resources will be managed by the driver. To have Direct3D override the driver so that Direct3D manages resources, use the D3DCREATE_DISABLE_DRIVER_MANAGEMENT flag when calling <a href="/windows/desktop/api"><strong>CreateDevice</strong></a>.</td>
</tr>
<tr class="even">
<td>D3DCAPS2_DYNAMICTEXTURES</td>
<td>0x20000000L</td>
<td>The driver supports dynamic textures.</td>
</tr>
<tr class="odd">
<td>D3DCAPS2_FULLSCREENGAMMA</td>
<td>0x00020000L</td>
<td>The driver supports dynamic gamma ramp adjustment in full-screen mode.</td>
</tr>
<tr class="even">
<td>D3DCAPS2_RESERVED</td>
<td>0x02000000L</td>
<td>Reserved; not used.</td>
</tr>
</tbody>
</table>



 

These constants are used by the D3CAPS2 member of [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9).

## Constant Information



|  Requirement                        | Value           |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 
