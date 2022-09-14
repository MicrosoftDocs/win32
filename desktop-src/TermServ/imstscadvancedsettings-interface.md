---
title: IMsTscAdvancedSettings interface
description: Includes methods to retrieve and set properties that enable bitmap caching, compression, and printer and clipboard redirection.
ms.assetid: 3385e843-be05-4801-8d59-6395d95686b1
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
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAdvancedSettings interface

Includes methods to retrieve and set properties that enable bitmap caching, compression, and printer and clipboard redirection. You can also specify names of virtual channel client DLLs.

You obtain an instance of this interface by using the [**IMsTscAx::AdvancedSettings**](imstscax-advancedsettings.md) property.

## Members

The **IMsTscAdvancedSettings** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IMsTscAdvancedSettings** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsTscAdvancedSettings** interface has these properties.




| Property | Access type | Description | 
|----------|-------------|-------------|
| <a href="imstscadvancedsettings-allowbackgroundinput.md"><strong>allowBackgroundInput</strong></a><br /> | Read/write<br /> | Specifies whether background input mode is enabled.<br /> | 
| <a href="imstscadvancedsettings-bitmapperistence.md"><strong>BitmapPeristence</strong></a><br /> | Read/write<br /> | Specifies whether bitmap caching is enabled.<br /><blockquote>[!Note]<br />The spelling error in the name of the property is in the released version of the control.</blockquote><br /> | 
| <a href="imstscadvancedsettings-compress.md"><strong>Compress</strong></a><br /> | Read/write<br /> | Specifies whether compression is enabled.<br /> | 
| <a href="imstscadvancedsettings-containerhandledfullscreen.md"><strong>ContainerHandledFullScreen</strong></a><br /> | Read/write<br /> | Specifies whether the container-handled full-screen mode is enabled.<br /> | 
| <a href="imstscadvancedsettings-disablerdpdr.md"><strong>DisableRdpdr</strong></a><br /> | Read/write<br /> | Specifies whether printer and clipboard redirection is enabled.<br /> | 
| <a href="imstscadvancedsettings-iconfile.md"><strong>IconFile</strong></a><br /> | Write-only<br /> | Specifies the name of the file containing icon data that will be accessed when displaying the client in full-screen mode.<br /> | 
| <a href="imstscadvancedsettings-iconindex.md"><strong>IconIndex</strong></a><br /> | Write-only<br /> | Specifies the index of the icon within the current icon file.<br /> | 
| <a href="imstscadvancedsettings-keyboardlayoutstr.md"><strong>KeyBoardLayoutStr</strong></a><br /> | Write-only<br /> | Specifies the name of the active input locale identifier (formerly called the keyboard layout) to use for the connection.<br /> | 
| <a href="imstscadvancedsettings-plugindlls.md"><strong>PluginDlls</strong></a><br /> | Write-only<br /> | Specifies the names of virtual channel client DLLs to be loaded.<br /> | 




 

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



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| IID<br/>                      | IID\_IMsTscAdvancedSettings is defined as 809945cc-4b3b-4a92-a6b0-dbf9b5f2ef2d<br/> |



## See also

<dl> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

