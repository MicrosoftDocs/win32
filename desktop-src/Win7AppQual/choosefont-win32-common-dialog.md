---
description: ChooseFont() Win32 Common Dialog
ms.assetid: ee1df9f2-585f-4208-ad49-a0f6ba76f53a
title: ChooseFont() Win32 Common Dialog
ms.topic: article
ms.date: 05/31/2018
---

# ChooseFont() Win32 Common Dialog

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

**Severity** - Low  
**Frequency** - Medium  




## Description

Windows 7 includes several updates to the ChooseFont() Win32 common dialog. These fall into two categories:

-   Visual refresh of the dialog
-   Support for new show/hide fonts feature

The **dialog refresh** updates the standard template to bring the dialog more in line with other dialog layouts in Windows. It introduces WYSIWYG to the font display lists to help users choose fonts. It also includes a link to the Fonts CPL to provide easy access for users wishing to customize their font lists.

**Show/hide fonts** is a new Windows 7 platform feature whereby fonts not appropriate for the current user's language settings (input methods) are not presented by default in font selection lists. Users may customize the fonts that they wish to appear in the Fonts CPL or may disable this feature.

## Manifestation of Impact

**Dialog visual refresh**

We have introduced two new templates in Windows 7 (one for applications that load version 6 or later of comctl32.dll and another for applications loading earlier versions).

-   For application compatibility reasons, these new templates will only be loaded for applications that do not hook the ChooseFont message queue. Applications that hook the message queue will continue to see the old dialog layout.
-   Applications that provide their own templates will continue to be able to use them.

Applications that do not get the new templates will see no dialog layout changes from Vista. They should however still get the new WYSIWYG font preview.

**Show/hide fonts**

For all versions of ChooseFont, the dialog will use the current user's show/hide font settings to determine the font list to display. This will result in the display of fewer font lists in most instances.

## End-user Mitigation

**Show/Hide Fonts:** To disable font hiding, users should go to the Font Settings page in the Fonts CPL and deselect the '

"Hide fonts based on language settings" checkbox

## Developer Mitigation

-   **Visual refresh:** Applications developers who provide their own templates may want to refresh this to be in line with the appropriate new Windows 7 template. The new templates are available in the Font.dlg template file.

    **Note:** The new published template contains an additional SysLink control that provides a shortcut that allows users to launch the Fonts CPL to display more fonts. The link control requires version 6 of the Windows common control library (comctl32.dll). Developers should provide a manifest or directive that specifies the use of version 6 of the DLL if available. Where an application uses an earlier version of the common control library, use the "PUSHBUTTON" control type instead.

-   **Show/Hide Fonts:** Developers may disable this feature by providing an additional flag (CF\_INACTIVEFONTS) in the flags member of the CHOOSEFONT structure. Setting this flag causes all installed fonts to display in the font list.
-   **Show/Hide Fonts:** Applications that provide ChooseFont help content may wish to add content to explain why the font list is reduced and direct users to the Fonts CPL to customize their font lists.

## Compatibility, Performance, Reliability, and Usability Testing

Developers whose applications hook the ChooseFont message queue to customize the dialog should verify that their applications retain all existing functionality.

Applications that heavily trim the font list using flags should ensure that the font list presented remains acceptable.

 

 



