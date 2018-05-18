---
title: IMsRdpClientAdvancedSettings5 interface
description: Manages advanced client settings. Derives from the IMsRdpClientAdvancedSettings4 interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a927cd4c-7f70-493e-a4f6-056d0352d56e'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["IMsRdpClientAdvancedSettings5 interface Remote Desktop Services", "IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , described"]
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings5
api_location:
- MsTscAx.dll
api_type:
- COM
---

# IMsRdpClientAdvancedSettings5 interface

Manages advanced client settings. Derives from the [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md) interface.

To obtain an instance of this interface, use the [**IMsTscAx::AdvancedSettings**](imstscax-advancedsettings.md) property to obtain an [**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md) interface pointer. Then call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) on the **IMsTscAdvancedSettings** pointer, and pass **IID\_IMsRdpClientAdvancedSettings5** to **QueryInterface**.

## Members

The **IMsRdpClientAdvancedSettings5** interface inherits from [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md). **IMsRdpClientAdvancedSettings5** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpClientAdvancedSettings5** interface has these properties.



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
<td style="text-align: left;">[<strong>AudioRedirectionMode</strong>](imsrdpclientadvancedsettings5-audioredirectionmode.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The audio redirection mode. The [<strong>AudioRedirectionMode</strong>](imsrdpclientadvancedsettings5-audioredirectionmode.md) property has the following possible values.<br/>
<dt><span id="AUDIO_MODE_REDIRECT___0"></span><span id="audio_mode_redirect___0"></span><strong>AUDIO_MODE_REDIRECT 0</strong> (Audio redirection is enabled and the option for redirection is &quot;Bring to this computer&quot;. This is the default mode.)<br/> </dt> <dd></dd> <dt><span id="AUDIO_MODE_PLAY_ON_SERVER_1"></span><span id="audio_mode_play_on_server_1"></span><strong>AUDIO_MODE_PLAY_ON_SERVER 1</strong> (Audio redirection is enabled and the option is &quot;Leave at remote computer&quot;. The &quot;Leave at remote computer&quot; option is supported only when connecting remotely to a host computer that is running Windows Vista. If the connection is to a host computer that is running Windows Server 2008, the option &quot;Leave at remote computer&quot; is changed to &quot;Do not play&quot;.)<br/> </dt> <dd></dd> <dt><span id="AUDIO_MODE_NONE_2"></span><span id="audio_mode_none_2"></span><strong>AUDIO_MODE_NONE 2</strong> (Audio redirection is enabled and the mode is &quot;Do not play&quot;.)<br/> </dt> <dd></dd> </dl></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>BitmapVirtualCache32BppSize</strong>](imsrdpclientadvancedsettings5-bitmapvirtualcache32bppsize.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies the virtual cache file size for 32 bits per pixel (bpp) bitmaps. The maximum value is 48 megabytes (MB).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ConnectionBarShowPinButton</strong>](imsrdpclientadvancedsettings5-connectionbarshowpinbutton.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the pin button should be shown on the connection bar. By default, the value is <strong>TRUE</strong>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>PublicMode</strong>](imsrdpclientadvancedsettings5-publicmode.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether public mode should be enabled or disabled. By default, public mode is set to <strong>FALSE</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RedirectClipboard</strong>](imsrdpclientadvancedsettings5-redirectclipboard.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether clipboard redirection should be enabled or disabled. By default, clipboard redirection mode is set to <strong>TRUE</strong> (enabled).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RedirectDevices</strong>](imsrdpclientadvancedsettings5-redirectdevices.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether redirected devices should be enabled or disabled. By default, redirected devices mode is set to <strong>FALSE</strong>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RedirectPOSDevices</strong>](imsrdpclientadvancedsettings5-redirectposdevices.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether Point of Service redirected devices should be enabled or disabled. By default, Point of Service redirected devices mode is set to <strong>FALSE</strong>.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

This interface has been extended by the following interfaces, with each new interface inheriting all the methods and properties of the previous interfaces:

-   [**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
-   [**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
-   [**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings5 is defined as FBA7F64E-6783-4405-DA45-FA4A763DABD0<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings3**](imsrdpclientadvancedsettings3.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
</dt> <dt>

[**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

 





