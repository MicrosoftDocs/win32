---
Description: 'An application can use a font to draw text only if that font is either resident on a specified device or installed in the system font table.'
ms.assetid: 'b422b981-8760-4484-9965-f212287c421e'
title: Font Installation and Deletion
---

# Font Installation and Deletion

An application can use a font to draw text only if that font is either resident on a specified device or installed in the system font table. The font table is an internal array that identifies all nondevice fonts that are available to an application. An application can retrieve the names of fonts currently installed on a device or stored in the internal font table by calling the [**EnumFontFamilies**](enumfontfamilies.md) or [**ChooseFont**](_win32_choosefont_cpp) functions.

To temporarily install a font, call [**AddFontResource**](addfontresource.md) or [**AddFontResourceEx**](addfontresourceex.md). These functions load a font that is stored in a font-resource file. However, this is a temporary installation because after a reboot the font will not be present.

To install a font that will remain after the system is rebooted, use one of the following methods:

-   Go to the Control Panel, click the **Fonts** icon, and select **Install New Fonts** from the **File** menu. The font is available to an application even before the reboot. However, in a terminal server situation the font is available for the current session but is not available for other sessions until after a reboot.
-   Copy the font into the %windir%\\fonts folder. Then, either go to the Control Panel and click the **Fonts** icon, or call [**AddFontResource**](gdi.AddFontResource) or [**AddFontResourceEx**](gdi.AddFontResourceEx). The font is available to an application even before the reboot. However, in a terminal server situation the font is available for the current session but is not available for other sessions until after a reboot. If you only copy the font into the %windir%\\fonts folder, the font will be available only after the system is rebooted.

When an application finishes using an installed font, it must remove that font by calling the [**RemoveFontResource**](removefontresource.md) function.

A font installed from a location other than the %windir%\\fonts folder cannot be modified when loaded in any active session, including session 0. Any attempt to change, replace, or delete will, therefore, be blocked. If modification to a font is necessary:

-   *Temporary fonts* get loaded only in the current session. Before attempting any font modifications, call [**RemoveFontResource**](removefontresource.md) to force the current session to unload the font.
-   *Permanent fonts* remain installed after reboot and are loaded by all created sessions. Call [**RemoveFontResource**](removefontresource.md) to force the current session to unload the font. Then, in the font registry key (**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts**) find and remove the registry value associated with the font. Finally, reboot the machine to ensure the font isn't loaded in any session. After reboot, proceed with your font modification/deletion.

Whenever an application calls the functions that add and delete font resources, it should also call the [**SendMessage**](_win32_sendmessage_cpp) function and send a [**WM\_FONTCHANGE**](wm-fontchange.md) message to all top-level windows in the system. This message notifies other applications that the internal font table has been altered by an application that added or removed a font.

 

 



