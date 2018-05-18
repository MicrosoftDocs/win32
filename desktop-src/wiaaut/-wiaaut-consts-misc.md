---
title: Miscellaneous Constants
description: Miscellaneous String constants.
ms.assetid: '603fcb38-93e0-4285-a4f7-af6ce03ccae3'
topic_type:
- apiref
api_name:
- wiaIDUnknown
- wiaAnyDeviceID
api_location:
- Wiaaut.h
api_type:
- HeaderDef
---

# Miscellaneous Constants

Miscellaneous **String** constants.



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
<td style="text-align: left;"><span id="wiaIDUnknown"></span><span id="wiaidunknown"></span><span id="WIAIDUNKNOWN"></span><dl> <dt><strong>wiaIDUnknown</strong></dt> <dt>{00000000-0000-0000-0000-000000000000}</dt> </dl></td>
<td style="text-align: left;">Unknown ID. Default value for the FormatID parameter for the [<strong>Transfer</strong>](-wiaaut-iitem-transfer.md), [<strong>ShowTransfer</strong>](-wiaaut-icommondialog-showtransfer.md), and [<strong>ShowAcquireImage</strong>](-wiaaut-icommondialog-showacquireimage.md) methods. In this context, it implies any FormatID rather than an unknown FormatID, or you might think of it as unknown to the calling application. Any property that represents a GUID can also return this constant as an error result.<br/> The following example shows how to determine if the file returned from [<strong>ShowAcquireImage</strong>](-wiaaut-icommondialog-showacquireimage.md) is in a known format.<br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>Dim Img &#39;As ImageFile

Set Img = CommonDialog1.ShowAcquireImage
If Img.FormatID = wiaIDUnknown Then
    MsgBox &quot;Image format unknown&quot;
End If</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="wiaAnyDeviceID"></span><span id="wiaanydeviceid"></span><span id="WIAANYDEVICEID"></span><dl> <dt><strong>wiaAnyDeviceID</strong></dt> <dt>*</dt> </dl></td>
<td style="text-align: left;"><p>DeviceID for any Device. Default value for the DeviceID parameter for the [<strong>RegisterEvent</strong>](-wiaaut-idevicemanager-registerevent.md), [<strong>UnregisterEvent</strong>](-wiaaut-idevicemanager-unregisterevent.md), [<strong>RegisterPersistentEvent</strong>](-wiaaut-idevicemanager-registerpersistentevent.md), and [<strong>UnregisterPersistentEvent</strong>](-wiaaut-idevicemanager-unregisterpersistentevent.md) methods. This constant is defined here in case you want to explicitly use any device when calling these methods.</p>
<p>For example code, see [Download New Items as They are Created](-wiaaut-shared-samples.md#download-new-items-as-they-are-created) in Shared Samples.</p></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





