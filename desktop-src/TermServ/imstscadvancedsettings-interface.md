---
title: IMsTscAdvancedSettings interface
description: Includes methods to retrieve and set properties that enable bitmap caching, compression, and printer and clipboard redirection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3385e843-be05-4801-8d59-6395d95686b1
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- IMsTscAdvancedSettings interface Remote Desktop Services
- IMsTscAdvancedSettings interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsTscAdvancedSettings
api_location:
- MsTscAx.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMsTscAdvancedSettings interface

Includes methods to retrieve and set properties that enable bitmap caching, compression, and printer and clipboard redirection. You can also specify names of virtual channel client DLLs.

You obtain an instance of this interface by using the [**IMsTscAx::AdvancedSettings**](imstscax-advancedsettings.md) property.

## Members

The **IMsTscAdvancedSettings** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface. **IMsTscAdvancedSettings** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsTscAdvancedSettings** interface has these properties.



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
<td style="text-align: left;">[<strong>allowBackgroundInput</strong>](imstscadvancedsettings-allowbackgroundinput.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether background input mode is enabled.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>BitmapPeristence</strong>](imstscadvancedsettings-bitmapperistence.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether bitmap caching is enabled.<br/>
<blockquote>
[!Note]<br />
The spelling error in the name of the property is in the released version of the control.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Compress</strong>](imstscadvancedsettings-compress.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether compression is enabled.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ContainerHandledFullScreen</strong>](imstscadvancedsettings-containerhandledfullscreen.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the container-handled full-screen mode is enabled.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>DisableRdpdr</strong>](imstscadvancedsettings-disablerdpdr.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether printer and clipboard redirection is enabled.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>IconFile</strong>](imstscadvancedsettings-iconfile.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">Specifies the name of the file containing icon data that will be accessed when displaying the client in full-screen mode.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>IconIndex</strong>](imstscadvancedsettings-iconindex.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">Specifies the index of the icon within the current icon file.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>KeyBoardLayoutStr</strong>](imstscadvancedsettings-keyboardlayoutstr.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">Specifies the name of the active input locale identifier (formerly called the keyboard layout) to use for the connection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>PluginDlls</strong>](imstscadvancedsettings-plugindlls.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">Specifies the names of virtual channel client DLLs to be loaded.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

This interface has been extended by the following interfaces, with each new interface inheriting all the methods and properties of the previous interfaces:

-   [**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
-   [**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
-   [**IMsRdpClientAdvancedSettings3**](imsrdpclientadvancedsettings3.md)
-   [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md)
-   [**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
-   [**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
-   [**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| IID<br/>                      | IID\_IMsTscAdvancedSettings is defined as 809945cc-4b3b-4a92-a6b0-dbf9b5f2ef2d<br/> |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

 





