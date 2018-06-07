---
Description: This section describes the individual Shell samples included in the Windows Software Development Kit (SDK) and, in most cases, downloadable from the MSDN Code Gallery.
title: Shell SDK Samples
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell SDK Samples

This section describes the individual Shell samples included in the Windows Software Development Kit (SDK) and, in most cases, downloadable from the [MSDN Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=154617).

-   [Windows SDK Locations](#windows-sdk-locations)
-   [MSDN Code Gallery Locations](#msdn-code-gallery-locations)
-   [Shell Samples](#shell-samples)

## Windows SDK Locations

When you download and install the Windows 7 SDK, samples are included in that installation. Use of the default SDK installation path results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`. Using the default installation path, the Shell samples listed below are found in the following folders:

-   C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\WinUI\\Shell\\AppPlatform
-   C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\WinUI\\Shell\\AppShellIntegration
-   C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\WinUI\\Shell\\LegacySamples
-   C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\WinUI\\Shell\\ShellExtensibility

## MSDN Code Gallery Locations

Shell samples can also be individually downloaded through the [MSDN Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=154617). Most Shell samples listed below can be found on the following pages:

-   [Windows Shell Application Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155655)
-   [Windows Shell Extensibility Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155658)
-   [Windows Shell Integration Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155659)

## Shell Samples



| Topic                                                                                                         | Contents                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Aero Wizards Sample](samples-aerowizards.md)                                                                | Demonstrates how to migrate Wizard 97 software to the Aero Wizard.                                                                                                                                                            |
| [Application User Model ID (AppUserModelID) Window Property Sample](samples-appusermodelidwindowproperty.md) | Demonstrates how to control the taskbar grouping behavior of an application's windows through the [System.AppUserModel.ID](https://msdn.microsoft.com/07858b3c-e601-40ec-a87a-d66612d5473a) property.                                                 |
| [Automatic Jump List Sample](samples-automaticjumplist.md)                                                   | Demonstrates how to add items to the automatic Jump List for an application, including switching between the display of the Frequent and Recent categories.                                                                   |
| [Change Notify Watcher Sample](samples-changenotifywatcher.md)                                               | Demonstrates how to listen to Shell change notifications on a folder or item in the Windows Explorer namespace.                                                                                                               |
| [Common File Dialog Modes Sample](samples-commonfiledialogmodes.md)                                          | Demonstrates how to use the Common File Dialog in different modes to pick files, containers (folders) or both files and folders (basket mode) without dismissing the dialog.                                                  |
| [Common File Dialog Sample](samples-commonfiledialog.md)                                                     | Demonstrates how to create a custom file open/save dialog by using different Common File Dialog APIs.                                                                                                                         |
| [CreateProcess Verb Sample](samples-createprocessverb.md)                                                    | Demonstrates how to implement a Shell verb using the CreateProcess method.                                                                                                                                                    |
| [Custom Jump List Sample](samples-customjumplist.md)                                                         | Demonstrates how to create a custom Jump List for an application, including adding a custom category and tasks.                                                                                                               |
| [Drag-and-Drop Visuals Sample](samples-dragdropvisuals.md)                                                   | Demonstrates how to use the Shell drag-and-drop services to get the presentation features that Shell drag-and-drop supports for both targets and sources.                                                                     |
| [DropTarget Verb Sample](samples-droptargetverb.md)                                                          | Demonstrates how to implement a Shell verb using the DropTarget method.                                                                                                                                                       |
| [Execute Command Verb Sample](samples-executecommandverb.md)                                                 | Demonstrates how to implement a Shell verb using the ExecuteCommand method.                                                                                                                                                   |
| [Execute In Explorer Sample](samples-execinexplorer.md)                                                      | Demonstrates how to call the [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) function from the Windows Explorer process.                                                                                                                 |
| [Explorer Browser Custom Contents Sample](samples-explorerbrowsercustomcontents.md)                          | Demonstrates how to implement a custom Explorer Browser contol for your application.                                                                                                                                          |
| [Explorer Browser Search Sample](samples-explorerbrowsersearch.md)                                           | Demonstrates how to use the Windows Explorer Browser control to embed Windows Explorer in an application and how to implement search functionality with an in-memory search folder.                                           |
| [Explorer Command Verb Sample](samples-explorercommandverb.md)                                               | Demonstrates how to implement a Shell verb using the ExplorerCommand and ExplorerCommandState methods.                                                                                                                        |
| [Explorer Data Provider Sample](samples-explorerdataprovider.md)                                             | Demonstrates how to implement a Shell namespace extension, including context menu behavior and custom tasks in the browser.                                                                                                   |
| [File Is In Use Sample](samples-fileinuse.md)                                                                | Demonstrates how to customize the **File In Use** dialog to display additional information and options for files that are currently opened in the application.                                                                |
| [File Operation Progress Sink](samples-fileoperationprogresssink.md)                                         | Demonstrates how to use the [**IFileOperationProgressSink**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperationprogresssink) interface methods for monitoring the details of [**IFileOperation**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ifileoperation) interface actions.                      |
| [File Operations Sample](samples-fileoperations.md)                                                          | Demonstrates how to copy, move, delete, and rename file system objects.                                                                                                                                                       |
| [HomeGroup Sample](samples-homegroup.md)                                                                     | Demonstrates how to determine HomeGroup membership status, enumerate top-level items in the **HomeGroup** Shell folder, and launch the **HomeGroup Sharing Wizard**.                                                          |
| [Known Folders Sample](samples-knownfolders.md)                                                              | Demonstrates how to define, register, enumerate and find the path for all known folders on the current system.                                                                                                                |
| [NameSpace Tree Control Sample](samples-namespacetreecontrol.md)                                             | Demonstrates how to implement a custom namespace tree control for an application.                                                                                                                                             |
| [NonDefaultDropMenuVerb Sample](samples-nondefaultdropmenuverb.md)                                           | Demonstrates how to extend the drag-and-drop shortcut menu (sometimes referred to as a context menu).                                                                                                                         |
| [NotificationIcon Sample](samples-notificationicon.md)                                                       | Demonstrates how to use the [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) and [**Shell\_NotifyIconGetRect**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicongetrect) APIs to display a notification icon.                                                |
| [Parsing With Parameters Sample](samples-parsingwithparameters.md)                                           | Demonstrates how to take advantage of Shell helpers that use the parsing name to interact with items through the Shell programming model.                                                                                     |
| [Player Verb Sample](samples-playerverbsample.md)                                                            | Demonstrates how to create a verb that operates on Shell items and containers which plays items or adds items to a queue.                                                                                                     |
| [Playlist Creator Sample](samples-playlistcreator.md)                                                        | Demonstrates how to create a verb that operates on a selected Shell item or container to create a playlist.                                                                                                                   |
| [Recipe Preview Handler Sample](samples-recipepreviewhandler.md)                                             | Demonstrates how to write a handler used to display a file preview inside the Windows Explorer preview pane or other preview handler hosts.                                                                                   |
| [Recipe Thumbnail Provider Sample](samples-recipethumbnailprovider.md)                                       | Demonstrates how to create a thumbnail handler by file type and extends Windows Explorer.                                                                                                                                     |
| [Search Folder Sample](samples-searchfolder.md)                                                              | Demonstrates how to create a search with query constraints using the Shell programming model.                                                                                                                                 |
| [Shell Library Backup Sample](samples-shelllibrarybackup.md)                                                 | Demonstrates how to enumerate libraries as containers.                                                                                                                                                                        |
| [Shell Library Command Line Sample](samples-shelllibrarycommandline.md)                                      | Demonstrates how to use the [**IShellLibrary**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishelllibrary) interface to create a command-line application that provides programmatic access for inspecting and manipulating libraries and library files.              |
| [Shell Storage Sample](samples-shellstorage.md)                                                              | Demonstrates how to create files and folders in Shell containers. Also shows how to save to the Shell item that is returned from the file dialog.                                                                             |
| [Sync and Share Verbs](samples-syncandshareverbs.md)                                                         | Demonstrates how to register a verb that extends the "Sync" and "Share" verbs in the Windows Explorer Command Bar.                                                                                                            |
| [TabThumbnails Sample](samples-tabthumbnails.md)                                                             | Demonstrates how an application can expose multiple switch targets (as for tabs) on a taskband and how to provide their thumbnails.                                                                                           |
| [Taskbar Peripheral Status Sample](samples-taskbarperipheralstatus.md)                                       | Demonstrates taskbar icon overlays and progress bars.                                                                                                                                                                         |
| [Taskbar Thumbnail Toolbar Sample](samples-taskbarthumbnailtoolbar.md)                                       | Demonstrates a thumbnail toolbar, an active toolbar control embedded in a window's thumbnail preview, used to provide access to a window's key commands without making the user restore or activate the application's window. |
| [Using Image Factory Sample](samples-usingimagefactory.md)                                                   | Demonstrates how to use the [**IShellItemImageFactory**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitemimagefactory) interface to get the best possible image for an item.                                                                                    |
| [Using Thumbnail Providers Sample](samples-usingthumbnailproviders.md)                                       | Demonstrates how to use the [**IThumbnailProvider**](/windows/desktop/api/Thumbcache/nn-thumbcache-ithumbnailprovider) interface to extract the thumbnail for an item from the Windows thumbnail cache system.                                                          |



 

 

 



