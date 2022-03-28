---
description: Discusses methods of opening a Control Panel item for Windows Vista and later systems as well as covering legacy Control Panel commands.
ms.assetid: c17167ab-e9a0-4290-955c-484d038b82af
title: Executing Control Panel Items
ms.topic: article
ms.date: 11/21/2021
---

# Executing Control Panel Items

> [!Note]  
> If you are looking for the list of canonical and module names for Control Panel items, see [Canonical Names of Control Panel Items](controlpanel-canonical-names.md).

 

There are two ways to open a Control Panel item:

-   The user can open Control Panel and then open an item by clicking or double-clicking the item's icon.
-   The user or an application can start a Control Panel item by executing it directly from the command line prompt.

An application can open the Control Panel programmatically by using the [**WinExec**](/windows/win32/api/winbase/nf-winbase-winexec) function.


```
WinExec("c:\windows\system32\control.exe", SW_NORMAL);
```



The following example shows how an application can start the Control Panel item named **MyCpl.cpl** by using the [**WinExec**](/windows/win32/api/winbase/nf-winbase-winexec) function.


```
WinExec("c:\windows\system32\control.exe MyCpl.cpl", SW_NORMAL);
```



When a Control Panel item is opened through a command line, you can instruct it to open to a particular tab in the item. Due to the addition and removal of certain tabs in some Windows Vista Control Panel items, the numbering of the tabs might have changed from that in Windows XP. For instance, the following example launches the fourth tab in the System item on Windows XP and the third tab on Windows Vista.


```
control.exe sysdm.cpl,,3
```



This topic discusses the following:

- [Windows Vista Canonical Names](#windows-vista-canonical-names)
- [New Commands for Windows Vista](#new-commands-for-windows-vista)
- [Legacy Control Panel Commands](#legacy-control-panel-commands)
- [Related topics](#related-topics)

## Windows 11 Canonical Names

> [!note]
> With Windows 10 and later most control panel items were moved into the settings app. Please read [launch settings app documentation](https://docs.microsoft.com/en-us/windows/uwp/launch-resume/launch-settings-app) for more information on this.

In Windows Vista and later, the preferred method of launching a Control Panel item from a command line is to use the Control Panel item's canonical name. A canonical name is a non-localized string that the Control Panel item declares in the registry. The value of using a canonical name is that it abstracts the module name of the Control Panel item. An item can be implemented in a .dll and later be reimplemented as a .exe or change its module name. As long as the canonical name remains the same, then any program that opens it by using that canonical name does not need to be updated.

By convention, the canonical name is formed as "CorporationName.ControlPanelItemName".

The following example shows how an application can start the Control Panel item **Programs and Features** with [**WinExec**](/windows/win32/api/winbase/nf-winbase-winexec).


```
WinExec("%systemroot%\system32\control.exe /name Microsoft.ProgramsAndFeatures", SW_NORMAL);
```



To start a Control Panel item with its canonical name, use: "%systemroot%\\system32\\control.exe /name *canonicalName*"

To open a specific sub-page in an item, or to open it with additional parameters, use: "%systemroot%\\system32\\control.exe /name **canonicalName** /page **pageName**"

An application can also implement the [**IOpenControlPanel::Open**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iopencontrolpanel-open) method to launch Control Panel items, including the ability to open a specific sub-page.

For a complete list of Control Panel item canonical names, see [Canonical Names of Control Panel Items](controlpanel-canonical-names.md).

## Command overview

Windows 11 contains the folowwing control panel items:

### Personalization

-   Screensaver: %windir%\\system32\\control.exe desk.cpl,screensaver,@screensaver

### System

-   Performance: `%windir%\\system32\\SystemPropertiesPerformance.exe`
-   Remote access: `%windir%\\system32\\SystemPropertiesRemote.exe`
-   Computer name: `%windir%\\system32\\SystemPropertiesComputerName.exe`
-   System protection: `%windir%\\system32\\SystemPropertiesProtection.exe`
-   Advanced system properties: `%windir%\\system32\\SystemPropertiesAdvanced.exe`

### Programs and Features

-   Add or remove programs: `%windir%\\system32\\control.exe /name Microsoft.ProgramsAndFeatures`
-   Windows features: `%windir%\\system32\\OptionalFeatures.exe`

### Folder Options

-   View: `%windir%\\system32\\rundll32.exe shell32.dll,Options_RunDLL 7`
-   General: `%windir%\\system32\\rundll32.exe shell32.dll,Options_RunDLL 0`

### Power Options

-   Edit current plan settings: `%windir%\\system32\\control.exe /name Microsoft.PowerOptions /page pagePlanSettings`
-   System settings: `%windir%\\system32\\control.exe /name Microsoft.PowerOptions /page pageGlobalSettings`
-   Create a power plan: `%windir%\\system32\\control.exe /name Microsoft.PowerOptions /page pageCreateNewPlan`
-   Power Options: `%windir%\\system32\\control.exe powercfg.cpl,,3`

## Legacy Control Panel Commands

## Windows Vista Canonical Names

In Windows Vista and later, the preferred method of launching a Control Panel item from a command line is to use the Control Panel item's canonical name. A canonical name is a non-localized string that the Control Panel item declares in the registry. The value of using a canonical name is that it abstracts the module name of the Control Panel item. An item can be implemented in a .dll and later be reimplemented as a .exe or change its module name. As long as the canonical name remains the same, then any program that opens it by using that canonical name does not need to be updated.

By convention, the canonical name is formed as "CorporationName.ControlPanelItemName".

The following example shows how an application can start the Control Panel item **Windows Update** with [**WinExec**](/windows/win32/api/winbase/nf-winbase-winexec).


```
WinExec("%systemroot%\system32\control.exe /name Microsoft.WindowsUpdate", SW_NORMAL);
```



To start a Control Panel item with its canonical name, use: "%systemroot%\\system32\\control.exe /name *canonicalName*"

To open a specific sub-page in an item, or to open it with additional parameters, use: "%systemroot%\\system32\\control.exe /name **canonicalName** /page **pageName**"

An application can also implement the [**IOpenControlPanel::Open**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iopencontrolpanel-open) method to launch Control Panel items, including the ability to open a specific sub-page.

For a complete list of Control Panel item canonical names, see [Canonical Names of Control Panel Items](controlpanel-canonical-names.md).

### Commands for Windows Vista

On Windows Vista, some options that were accessed by a .cpl module on Windows XP are now implemented as .exe files. This provides added security by allowing standard users to be prompted to provide administrator credentials when trying to launch the files. Options that do not require extra security are accessed by the same command lines that were used in Windows XP. The following is a list of commands used in Windows Vista to access specific tabs of Control Panel items:

#### Personalization

-   Font size and DPI: %windir%\\system32\\DpiScaling.exe
-   Screen resolution: %windir%\\system32\\control.exe desk.cpl,Settings,@Settings
-   Display settings: %windir%\\system32\\control.exe desk.cpl,Settings,@Settings
-   Themes: %windir%\\system32\\control.exe desk.cpl,Themes,@Themes
-   Screensaver: %windir%\\system32\\control.exe desk.cpl,screensaver,@screensaver
-   Multi-monitor: %windir%\\system32\\control.exe desk.cpl,Monitor,@Monitor
-   Color Scheme: %windir%\\system32\\control.exe /name Microsoft.Personalization /page pageColorization
-   Desktop background: %windir%\\system32\\control.exe /name Microsoft.Personalization /page pageWallpaper

> [!Note]  
> Starter and Basic Editions do not support control.exe /name Microsoft.Personalization command.

 

#### System

-   Performance: %windir%\\system32\\SystemPropertiesPerformance.exe
-   Remote access: %windir%\\system32\\SystemPropertiesRemote.exe
-   Computer name: %windir%\\system32\\SystemPropertiesComputerName.exe
-   System protection: %windir%\\system32\\SystemPropertiesProtection.exe
-   Advanced system properties: %windir%\\system32\\SystemPropertiesAdvanced.exe

#### Programs and Features

-   Add or remove programs: %windir%\\system32\\control.exe /name Microsoft.ProgramsAndFeatures
-   Windows features: %windir%\\system32\\OptionalFeatures.exe

#### Regional and Language Options

-   Keyboard: %systemroot%\\system32\\control.exe /name Microsoft.RegionalAndLanguageOptions /page /p:"keyboard"
-   Location: %systemroot%\\system32\\control.exe /name Microsoft.RegionalAndLanguageOptions /page /p:"location"
-   Administrative: %systemroot%\\system32\\control.exe /name Microsoft.RegionalAndLanguageOptions /page /p:"administrative"

#### Folder Options

-   Folder searching: %windir%\\system32\\rundll32.exe shell32.dll,Options\_RunDLL 2
-   File associations: %windir%\\system32\\control.exe /name Microsoft.DefaultPrograms /page pageFileAssoc
-   View: %windir%\\system32\\rundll32.exe shell32.dll,Options\_RunDLL 7
-   General: %windir%\\system32\\rundll32.exe shell32.dll,Options\_RunDLL 0

#### Power Options

-   Edit current plan settings: %windir%\\system32\\control.exe /name Microsoft.PowerOptions /page pagePlanSettings
-   System settings: %windir%\\system32\\control.exe /name Microsoft.PowerOptions /page pageGlobalSettings
-   Create a power plan: %windir%\\system32\\control.exe /name Microsoft.PowerOptions /page pageCreateNewPlan
-   There is no canonical command for the Advanced Settings page, it is accessed in the older manner: %windir%\\system32\\control.exe powercfg.cpl,,3

### Other lagacy options:
When you use the [**WinExec**](/windows/win32/api/winbase/nf-winbase-winexec) function, the system can recognize special Control Panel commands. These commands predate Windows 10.



| 
|
| control.exe desktop | Launches the <strong>Display Properties</strong> window.<blockquote>[!Note]<br />Starter and Basic Editions do not support this command.</blockquote><br /> | 
| control.exe color | Launches the <strong>Display Properties</strong> window with the <strong>Appearance</strong> tab preselected. | 
| control.exe date/time | Launches the <strong>Date and Time Properties</strong> window. | 
| control.exe international | Launches the <strong>Regional and Language Options</strong> window. | 
| control.exe mouse | Launches the <strong>Mouse Properties</strong> window. | 
| control.exe keyboard | Launches the <strong>Keyboard Properties</strong> window. | 
| control.exe printers | Displays the <strong>Printers and Faxes</strong> folder. | 
| control.exe fonts | Displays the <strong>Fonts</strong> folder. | 




 

For Windows 2000 and later systems:



| Command                    | Description                                              |
|----------------------------|----------------------------------------------------------|
| control.exe folders        | Launches the **Folder Options** window.                  |
| control.exe netware        | Launches the **Novell NetWare** window (if installed).   |
| control.exe telephony      | Launches the **Phone and Modem Options** window.         |
| control.exe admintools     | Displays the **Administrative Tools** folder.            |
| control.exe schedtasks     | Displays the **Scheduled Tasks** folder.                 |
| control.exe netconnections | Displays the **Network Connections** folder.             |
| control.exe infrared       | Launches the **Infrared Monitor** window (if installed). |
| control.exe userpasswords  | Launches the **User Accounts** window.                   |



 

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[User Experience Guidelines](user-experience-guidelines.md)
</dt> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[Using CPLApplet](using-cplapplet.md)
</dt> <dt>

[Control Panel Message Processing](message-processing.md)
</dt> <dt>

[Extending System Control Panel Items](extending-system-control-panel-items.md)
</dt> <dt>

[Assigning Control Panel Categories](assigning-control-panel-categories.md)
</dt> <dt>

[Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md)
</dt> <dt>

[Accessing the Control Panel in Safe Mode under Windows Vista](accessing-the-cp-in-safe-mode-under-vista.md)
</dt> </dl>

 

 
