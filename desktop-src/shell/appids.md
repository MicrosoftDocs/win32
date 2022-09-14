---
description: Application User Model IDs (AppUserModelIDs) are used extensively by the taskbar in Windows 7 and later systems to associate processes, files, and windows with a particular application.
ms.assetid: ebce2d99-6f20-4545-9f12-d79cd8d0828f
title: Application User Model IDs (AppUserModelIDs)
ms.topic: article
ms.date: 05/31/2018
---

# Application User Model IDs (AppUserModelIDs)

Application User Model IDs (AppUserModelIDs) are used extensively by the taskbar in Windows 7 and later systems to associate processes, files, and windows with a particular application. In some cases, it is sufficient to rely on the internal AppUserModelID assigned to a process by the system. However, an application that owns multiple processes or an application that is running in a host process might need to explicitly identify itself so that it can group its otherwise disparate windows under a single taskbar button and control the contents of that application's Jump List.

-   [Application-Defined and System-Defined AppUserModelIDs](#application-defined-and-system-defined-appusermodelids)
-   [How to Form an Application-Defined AppUserModelID](#how-to-form-an-application-defined-appusermodelid)
-   [Where to Assign an AppUserModelID](#where-to-assign-an-appusermodelid)
-   [Registering an Application as a Host Process](#registering-an-application-as-a-host-process)
-   [Exclusion Lists for Taskbar Pinning and Recent/Frequent Lists](#exclusion-lists-for-taskbar-pinning-and-recentfrequent-lists)
-   [Related topics](#related-topics)

## Application-Defined and System-Defined AppUserModelIDs

Some applications do not declare an explicit AppUserModelID. They are optional. In that case, the system uses a series of heuristics to assign an internal AppUserModelID. However, there is a performance benefit in avoiding those calculations and an explicit AppUserModelID is the only way to guarantee an exact user experience. Therefore, it is strongly recommended that an explicit ID be set. Applications cannot retrieve a system-assigned AppUserModelID.

If an application uses an explicit AppUserModelID, it must also assign the same AppUserModelID to all running windows or processes, shortcuts, and file associations. It must also use that AppUserModelID when customizing its Jump List through [**ICustomDestinationList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icustomdestinationlist), and in any calls to [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs).

> [!Note]  
> If applications do not have an explicit AppUserModelID, they must call [**IApplicationDestinations**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdestinations), [**IApplicationDocumentLists**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdocumentlists), and [**ICustomDestinationList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icustomdestinationlist) methods as well as [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) from within the application. If those methods are called from another process, such as an installer or uninstaller, the system cannot generate the correct AppUserModelID and those calls will have no effect.

 

The following items describe common scenarios that require an explicit AppUserModelID. They also point out cases where multiple explicit AppUserModelIDs should be used.

-   A single executable file with a UI with multiple modes that appear to the user as separate applications should assign different AppUserModelIDs to each mode. For instance, a portion of an application that users see as an independent experience that they can pin to and launch from the taskbar separately from the rest of the application should have its own AppUserModelID, separate from the main experience.
-   Multiple shortcuts with different arguments that all lead to what the user sees as the same application should use one AppUserModelID for all of the shortcuts. For example, Windows Internet Explorer has different shortcuts for different modes (such as launching without add-ons) but they should all appear to the user as a single Internet Explorer instance.
-   An executable that acts as a host process and runs target content as an application must [register as a host application](#registering-an-application-as-a-host-process), after which it can assign different AppUserModelIDs to each perceived experience that it hosts. Alternately, the host process can allow the hosted program to set its AppUserModelIDs. In either case, the host process must keep a record of the source of the AppUserModelIDs, either itself or the hosted application. In this case, there is no primary user experience of the host process without the target content. Examples are Windows Remote Applications Integrated Locally (RAIL) applications, the Java Runtime, RunDLL32.exe, or DLLHost.exe.

    In the case of existing hosted applications, the system attempts to identify individual experiences, but new applications should use explicit AppUserModelIDs to guarantee the intended user experience.

-   Cooperative or chained processes that to the user are part of the same application should have the same AppUserModelID applied to each process. Examples include games with a launcher process (chained) and Microsoft Windows Media Player, which has a first-run/setup experience running in one process and the main application running in another process (cooperative).
-   A Shell namespace extension that acts as a separate application for more than browsing and managing content in Windows Explorer should assign an AppUserModelID in its folder properties. An example is the Control Panel.
-   In a virtualization environment such as a deployment framework, the virtualization environment should assign different AppUserModelIDs to each application that it manages. In these cases, an application launcher uses an intermediary process to set up the environment and then hands off the operation to a different process to run the application. Note that this causes the system to be unable to relate the running target process back to the shortcut because the shortcut points to the intermediary process.

    If any application has multiple windows, shortcuts, or processes, that application's assigned AppUserModelID should also be applied to each of those pieces by the virtualization environment.

    An example of this situation is the ClickOnce framework, which properly assigns AppUserModelIDs on behalf of the applications that it manages. As in all such environments, applications deployed and managed by ClickOnce should not assign explicit AppUserModelIDs themselves, because doing so will conflict with the AppUserModelIDs assigned by ClickOnce and lead to unexpected results.

## How to Form an Application-Defined AppUserModelID

An application must provide its AppUserModelID in the following form. It can have no more than 128 characters and cannot contain spaces. Each section should be pascal-cased.

`CompanyName.ProductName.SubProduct.VersionInformation`

`CompanyName` and `ProductName` should always be used, while the `SubProduct` and `VersionInformation` portions are optional and depend on the application's requirements. `SubProduct` allows a main application that consists of several subapplications to provide a separate taskbar button for each subapplication and its associated windows. `VersionInformation` allows two versions of an application to coexist while being seen as discrete entities. If an application is not intended to be used in that way, the `VersionInformation` should be omitted so that an upgraded version can use the same AppUserModelID as the version that it replaced.

## Where to Assign an AppUserModelID

When an application uses one or more explicit AppUserModelIDs, it should apply those AppUserModelIDs in the following locations and situations:

-   In the [System.AppUserModel.ID](../properties/props-system-appusermodel-id.md) property of the application's shortcut file. A shortcut (as an [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka), CLSID\_ShellLink, or a .lnk file) supports properties through [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) and other property-setting mechanisms used throughout the Shell. This allows the taskbar to identify the proper shortcut to pin and ensures that windows belonging to the process are appropriately associated with that taskbar button.
    > [!Note]  
    > The [System.AppUserModel.ID](../properties/props-system-appusermodel-id.md) property should be applied to a shortcut when that shortcut is created. When using the Microsoft Windows Installer (MSI) to install the application, the [MsiShortcutProperty](../msi/msishortcutproperty-table.md) table allows the AppUserModelID to be applied to the shortcut when it is created during installation.

     

-   As a property of any of the application's running windows. This can be set in one of two ways:

    1.  If different windows owned by one process require different AppUserModelIDs to control taskbar grouping, use [**SHGetPropertyStoreForWindow**](/windows/win32/api/shellapi/nf-shellapi-shgetpropertystoreforwindow)) to retrieve the window's property store and set the AppUserModelID as a window property.
    2.  If all windows in the process use the same AppUserModelID, set the AppUserModelID on the process though [**SetCurrentProcessExplicitAppUserModelID**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-setcurrentprocessexplicitappusermodelid). An application must call **SetCurrentProcessExplicitAppUserModelID** to set its AppUserModelID during an application's initial startup routine before the application presents any UI, makes any manipulation of its Jump Lists, or makes (or causes the system to make) any call to [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs).

    A window-level AppUserModelID overrides a process-level AppUserModelID.

    When an application sets an explicit AppUserModelID at the window level, the application can provide the specifics of its relaunch command for its taskbar button. To supply that information, the following properties are used:

    -   [System.AppUserModel.RelaunchCommand](../properties/props-system-appusermodel-relaunchcommand.md)
    -   [System.AppUserModel.RelaunchDisplayNameResource](../properties/props-system-appusermodel-relaunchdisplaynameresource.md)
    -   [System.AppUserModel.RelaunchIconResource](../properties/props-system-appusermodel-relaunchiconresource.md)

    > [!Note]  
    > If a shortcut exists to launch the application, an application should apply the AppUserModelID as a property of the shortcut instead of using the relaunch properties. In that case, the command line, icon, and text of the shortcut are used to supply the same information as the relaunch properties.

     

    A window-level explicit AppUserModelID can also use the [System.AppUserModel.PreventPinning](../properties/props-system-appusermodel-preventpinning.md) property to specify that it should not be available for pinning or relaunching.

-   In a call to customize or update ([**ICustomDestinationList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icustomdestinationlist)), retrieve ([**IApplicationDocumentLists**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdocumentlists)), or clear ([**IApplicationDestinations**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdestinations)) the application's Jump List.
-   In file association registration (through its [ProgID](fa-progids.md)) if the application uses the system's automatically generated **Recent** or **Frequent** destination lists. This association information is referenced by [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs). This information is also used when adding [**IShellItem**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) destinations to custom Jump Lists through [**ICustomDestinationList::AppendCategory**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icustomdestinationlist-appendcategory).
-   In any call the application makes directly to [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs). If the application depends on the common file dialog to make calls to **SHAddToRecentDocs** on its behalf, those calls can deduce the explicit AppUserModelID only if the AppUserModelID is set for the entire process. If the application sets AppUserModelIDs on its windows instead of on the process, the application must make all calls to **SHAddToRecentDocs** itself, with its explicit AppUserModelID, as well as preventing the common file dialog from making its own calls. This must be done any time an item is opened, to ensure the **Recent** or **Frequent** sections of the application's Jump List are accurate.

The following items describe common scenarios and where to apply explicit AppUserModelIDs in those scenarios.

-   When a single process contains multiple applications, use [**SHGetPropertyStoreForWindow**](/windows/win32/api/shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store and set the AppUserModelID as a window property.
-   When an application uses multiple processes, apply the AppUserModelID to each process. Whether you use the same AppUserModelID on each process depends on whether you want each process to appear as part of the main application or as individual entities.
-   To separate certain windows from a set in the same process, use the window's property store to apply a single AppUserModelID to those windows you want to separate, and then apply a different AppUserModelID to the process. Any window in that process that was not explicitly labeled with the window-level AppUserModelID inherits the AppUserModelID of the process.
-   If a file type is associated with an application, assign the AppUserModelID in the file type's [ProgID](fa-progids.md) registration. If a single executable file is launched in different modes that appear to the user as distinct applications, a separate AppUserModelID is required for each mode. In that case, there must be multiple ProgID registrations for the file type, each with a different AppUserModelID.
-   When there are multiple shortcut locations from which a user can launch an application (in the **Start** menu, on the desktop, or elsewhere) retrieve the shortcut's property store to apply a single AppUserModelID to all of the shortcuts as shortcut properties.
-   When an explicit call is made to [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) by an application, use the AppUserModelID in the call. When the common file dialog is used to open or save files, **SHAddToRecentDocs** is called by the dialog on behalf of the application. That call can infer the explicit AppUserModelID from the process. However, if an explicit AppUserModelID is applied as a window property, the common file dialog cannot determine the correct AppUserModelID. In that case, the application itself must explicitly call **SHAddToRecentDocs** and provide it with the correct AppUserModelID. Additionally, the application must prevent the common file dialog from calling **SHAddToRecentDocs** on its behalf by setting the FOS\_DONTADDTORECENT flag in the **GetOptions** method of [**IFileOpenDialog**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ifileopendialog) or [**IFileSaveDialog**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ifilesavedialog).

## Registering an Application as a Host Process

An application can set the IsHostApp registry entry to cause that executable's process to be considered a host process by the taskbar. This affects its grouping and default Jump List entries.

The following example shows the required registry entry. Note that the entry is not assigned a value; its presence is all that is required. It is a REG\_NULL value.

```
HKEY_CLASSES_ROOT
   Applications
      example.exe
         IsHostApp
```

If either the process itself or the shortcut file used to launch the process has an explicit AppUserModelID, then the host process list is ignored and the application is treated as a normal application by the taskbar. The application's running windows are grouped together under a single taskbar button and the application can be pinned to the taskbar.

If only the running process' executable name is known, without an explicit AppUserModelID, and that executable is in the host process list, then each instance of the process is treated as a separate entity for taskbar grouping. The taskbar button associated with any specific instance of the process does not display a pin/unpin option or a launch icon for a new instance of the process. The process is also not eligible for inclusion in the **Start** menu's Most Frequently Used (MFU) list. However, if the process was launched through a shortcut that contains launch arguments (usually the target content to host as the "application"), the system can determine identity and the application can be pinned and relaunched.

## Exclusion Lists for Taskbar Pinning and Recent/Frequent Lists

Applications, processes, and windows can choose to make themselves unavailable for pinning to the taskbar or for inclusion in the **Start** menu's MFU list. There are three mechanisms to accomplish this:

1.  Add the NoStartPage entry to the application's registration as shown here:

    ```
    HKEY_CLASSES_ROOT
       Applications
          Example.exe
             NoStartPage
    ```

    The data associated with the NoStartPage entry is ignored. Only the presence of the entry is required. Therefore, the ideal type for NoStartPage is REG\_NONE.

    Note that any use of an explicit AppUserModelID overrides the NoStartPage entry. If an explicit AppUserModelID is applied to a shortcut, process, or window, it becomes pinnable and eligible for the **Start** menu MFU list.

2.  Set the [System.AppUserModel.PreventPinning](../properties/props-system-appusermodel-preventpinning.md) property on windows and shortcuts. This property must be set on a window before the [PKEY\_AppUserModel\_ID](../properties/props-system-appusermodel-id.md) property.
3.  Add an explicit AppUserModelID as a value under the following registry subkey as shown here:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Windows
                CurrentVersion
                   Explorer
                      FileAssociation
                         NoStartPageAppUserModelIDs
                            AppUserModelID1
                            AppUserModelID2
                            AppUserModelID3
    ```

    Each entry is a REG\_NULL value with the name of the AppUserModelID. Any AppUserModelID found in this list is not pinnable and not eligible for inclusion in the **Start** menu MFU list.

Be aware that certain executable files as well as shortcuts that contain certain strings in their name are automatically excluded from pinning and inclusion in the MFU list.

> [!Note]  
> This automatic exclusion can be overridden by applying an explicit AppUserModelID.

 

If any of the following strings, regardless of case, are included in the shortcut name, the program is not pinnable and is not displayed in the most frequently used list (not applicable to Windows 10):

-   Documentation
-   Help
-   Install
-   More Info
-   Read me
-   Read First
-   Readme
-   Remove
-   Setup
-   Support
-   What's New

The following list of programs are not pinnable and are excluded from the most frequently used list.

-   Applaunch.exe
-   Control.exe
-   Dfsvc.exe
-   Dllhost.exe
-   Guestmodemsg.exe
-   Hh.exe
-   Install.exe
-   Isuninst.exe
-   Lnkstub.exe
-   Mmc.exe
-   Mshta.exe
-   Msiexec.exe
-   Msoobe.exe
-   Rundll32.exe
-   Setup.exe
-   St5unst.exe
-   Unwise.exe
-   Unwise32.exe
-   Werfault.exe
-   Winhlp32.exe
-   Wlrmdr.exe
-   Wuapp.exe

The preceding lists are stored in the following registry values.

> [!Note]  
> These lists should not be modified by applications. Use one of the exclusion list methods listed previously for the same experience.

 

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  FileAssociation
                     AddRemoveApps
                     HostApps
```

## Related topics

<dl> <dt>

[**SetCurrentProcessExplicitAppUserModelID**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-setcurrentprocessexplicitappusermodelid)
</dt> <dt>

[**GetCurrentProcessExplicitAppUserModelID**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-getcurrentprocessexplicitappusermodelid)
</dt> <dt>

[Taskbar Extensions](taskbar-extensions.md)
</dt> <dt>

[**ICustomDestinationList::SetAppID**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icustomdestinationlist-setappid)
</dt> <dt>

[**IApplicationDocumentLists::SetAppID**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdocumentlists-setappid)
</dt> <dt>

[**IApplicationDestinations::SetAppID**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdestinations-setappid)
</dt> <dt>

[**SHGetPropertyStoreForWindow**](/windows/win32/api/shellapi/nf-shellapi-shgetpropertystoreforwindow)
</dt> </dl>

 

 
