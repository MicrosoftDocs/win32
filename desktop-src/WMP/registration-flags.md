---
title: Registration Flags
description: Registration Flags
ms.assetid: ba1709c2-0fe5-4168-9aed-613d01eff21f
keywords:
- Windows Media Player plug-ins,registration flags
- plug-ins,registration flags
- user interface plug-ins,registration flags
- UI plug-ins,registration flags
- flags,user interface plug-ins
- registry,UI plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registration Flags

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the Windows Media Player Plug-in Wizard creates a new UI plug-in project, it creates a key in the registry that contains information about the plug-in. This key is created in the following location:


```C++
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MediaPlayer\UIPlugins\{ClassId}
```



*ClassId* is the class id of the plug-in.

This key includes the following values.



| Name                     | Type       | Description                                                                                                                                                                               |
|--------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Capabilities             | REG\_DWORD | A DWORD value that consists of at least one plug-in type flag that may be combined with one or more plug-in capabilities flags by using binary OR operations.                             |
| Description              | REG\_SZ    | A string that contains the description of the plug-in. The plug-in wizard creates a string resource and provides the URL of the resource (using the res protocol) for this value.         |
| FriendlyName             | REG\_SZ    | A string that contains the user-readable name for the plug-in. The plug-in wizard creates a string resource and provides the URL of the resource (using the res protocol) for this value. |
| UninstallPath (optional) | REG\_SZ    | A string that contains the path to an executable file that uninstalls the plug-in.                                                                                                        |



 

For more information about the res protocol, see the Internet Development SDK.

The following table details the plug-in type flags.



| Plug-in Type Flag                | Value | Description                                       |
|----------------------------------|-------|---------------------------------------------------|
| **PLUGIN\_TYPE\_BACKGROUND**     | 0x1   | The UI plug-in does not display a user interface. |
| **PLUGIN\_TYPE\_SEPARATEWINDOW** | 0x2   | The UI plug-in is a separate window plug-in.      |
| **PLUGIN\_TYPE\_DISPLAYAREA**    | 0x3   | The UI plug-in is a display area plug-in.         |
| **PLUGIN\_TYPE\_SETTINGSAREA**   | 0x4   | The UI plug-in is a settings area plug-in.        |
| **PLUGIN\_TYPE\_METADATAAREA**   | 0x5   | The UI plug-in is a metadata area plug-in.        |



 

The following table details the plug-in capabilities flags.



| Plug-in Capabilities Flag             | Value      | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **PLUGIN\_FLAGS\_ACCEPTSMEDIA**       | 0x10000000 | The UI plug-in can accept **Media** object pointer arrays when Windows Media Player calls [**IWMPPluginUI::SetProperty**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-setproperty) .                                                                                                                                                                                                                                                           |
| **PLUGIN\_FLAGS\_ACCEPTSPLAYLISTS**   | 0x8000000  | The UI plug-in can accept **Playlist** object pointer arrays when Windows Media Player calls [**IWMPPluginUI::SetProperty**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-setproperty) .                                                                                                                                                                                                                                                        |
| **PLUGIN\_FLAGS\_HASPRESETS**         | 0x4000000  | The UI plug-in uses presets. If the plug-in specifies this flag, Windows Media Player will query the plug-in for preset information by calling [**IWMPPluginUI::GetProperty**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-getproperty) .                                                                                                                                                                                                      |
| **PLUGIN\_FLAGS\_HASPROPERTYPAGE**    | 0x80000000 | The UI plug-in provides a property page dialog. Windows Media Player will call [**IWMPPluginUI::DisplayPropertyPage**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-displaypropertypage) if this flag is set when the property page is invoked.                                                                                                                                                                                                 |
| **PLUGIN\_FLAGS\_HIDDEN**             | 0x02000000 | The background UI plug-in does not appear on the **Plug-ins** menu that is accessed from the **View** or **Tools** menus or the **Select Now Playing options** button in Now Playing. It does appear on the **Plug-ins** tab of the Options dialog. It does cause the Background Plug-in Running icon to appear in the status bar.This flag has no effect on plug-ins other than background UI plug-ins.<br/> |
| **PLUGIN\_FLAGS\_INSTALLAUTORUN**     | 0x40000000 | Windows Media Player runs the UI plug-in automatically when the plug-in is installed.                                                                                                                                                                                                                                                                                                                               |
| **PLUGIN\_FLAGS\_LAUNCHPROPERTYPAGE** | 0x20000000 | Windows Media Player calls [**IWMPPluginUI::DisplayPropertyPage**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-displaypropertypage) when the UI plug-in runs for the first time.If this flag is specified, **PLUGIN\_FLAGS\_HASPROPERTYPAGE** should be specified also.<br/>                                                                                                                                                             |



 

The following constants are defined in wmpplug.h. Do not change the values associated with these constants.



| Name                                    | Description                               |
|-----------------------------------------|-------------------------------------------|
| **PLUGIN\_INSTALLREGKEY**               | The location of the plug-in registry key. |
| **PLUGIN\_INSTALLREGKEY\_FRIENDLYNAME** | The name of the friendly name value.      |
| **PLUGIN\_INSTALLREGKEY\_DESCRIPTION**  | The name of the description value.        |
| **PLUGIN\_INSTALLREGKEY\_CAPABILITIES** | The name of the capabilities value.       |
| **PLUGIN\_INSTALLREGKEY\_UNINSTALL**    | The name of the uninstall path value.     |



 

## Related topics

<dl> <dt>

[**IWMPPluginUI::DisplayPropertyPage**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-displaypropertypage)
</dt> <dt>

[**IWMPPluginUI::GetProperty**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-getproperty)
</dt> <dt>

[**IWMPPluginUI::SetProperty**](/previous-versions/windows/desktop/api/wmpplug/nf-wmpplug-iwmppluginui-setproperty)
</dt> <dt>

[**User Interface Plug-ins Programming Reference**](user-interface-plug-ins-programming-reference.md)
</dt> </dl>

 

 





