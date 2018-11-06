---
title: Structure of the Sample Desktop Application
description: Structure of the Sample Desktop Application
ms.assetid: e042470d-dc78-488c-bcad-2e8d34714d5d
keywords:
- Windows Media Device Manager,samples
- Device Manager,samples
- desktop applications,samples
- Windows Media Device Manager,desktop application sample
- Device Manager,desktop application sample
- samples,desktop applications
ms.topic: article
ms.date: 05/31/2018
---

# Structure of the Sample Desktop Application

The sample desktop application consists of two main pieces:

-   The wmdapp project contains most of the classes that display the user interface, handle dragging and dropping, and perform all the required functionality of the program.
-   The proghelp project is a helper application that contains nonessential classes to handle status notifications and manual file transfers from the desktop to the application.

The executable uses the helper project only when the user selects **Use Operation Interface** on the **Options** menu to handle manual file transfer to the device, and to increment the status bar in the download progress form. All the rest of the application is handled in the wmdapp project.



| Class                | File                    | Description                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| —                    | wmdmapp.cpp             | The class that handles the parent window of the user interface. The code in this file also handles some user input not handled by CDevFiles, such as creating a playlist or album on a device, deleting files, and registering menu choices.                                                                                                                                                    |
| CDevices             | Devices.cpp             | The class that handles the left-hand pane of the main application window, where the available devices are listed. This class manages the messaging loop, which handles user input such as selecting a device and notifying the CDevFiles pane to load the appropriate files when the device selection has changed.                                                                              |
| CDevFiles            | Devfiles.cpp            | The class that handles the right-hand pane of the main application window, where the files on the selected device are listed. This class manages the messaging loop, and handles user input such as dragging files onto the device and deleting files from the device.                                                                                                                          |
| CStatus              | Status.cpp              | The class that handles the bottom status bar in the main window, where the number of devices and files is listed, along with the amount of free and used memory on the selected device.                                                                                                                                                                                                         |
| CWMDM                | Wmdevmgr.cpp            | The top-level interface for Windows Media Device Manager. This class handles authentication, retrieves the top-level **IWMDeviceManager** interface, and registers for notifications with the **IWMDMNotification** interface.                                                                                                                                                                  |
| CProgress            | Progress.cpp            | The class in the main application project that creates and manages the dialog box showing the progress of an event.                                                                                                                                                                                                                                                                             |
| CItemData            | ItemData.cpp            | A wrapper class that holds a pointer to a storage (if representing a file or folder on the device) or a device (if representing a device), as well as a variety of information about the object including size and attributes.                                                                                                                                                                  |
| CNotificationHandler | Notificationhandler.cpp | Handles device arrival and removal notifications by alerting the CDevices window.                                                                                                                                                                                                                                                                                                               |
| CProgressHelper      | ProgressHelper.cpp      | Created by CDevFiles in local functions to receive notifications from Windows Media Device Manager by implementing **IWMDMProgress**. It is used by the CProgress class to determine the amount of bars in the progress bar, and when an action is finished. This class is defined as a COM object that exposes the SDK interface **IWMDMProgress** and a custom interface IWMDMProgressHelper. |
| COperationHelper     | Operationhelper.cpp     | This class implements **IWMDMOperation** to handle manual transfer of files. It is multi-threaded to allow it to occur asynchronously, and is defined as a COM object that exposes a custom interface, IWMDMOperationHelper, to instantiate and initialize the class. This class is only used if the user selects "Use Operation Interface" in the **Options** menu.                            |



 

The following lists outline the basic steps that occur for various user actions:

**On startup**

The following main steps occur when the sample application is started.

1.  The global CWMDM variable is instantiated and authenticated, and registers to receive notifications
2.  A global CDevices is instantiated, and CDevices::Create is called to create and fill the devices pane.
3.  A global CDevFiles is instantiated, and CDevFiles::Create is called to create the files pane (which is not filled until the user selects a device).
4.  A global CStatus is instantiated, and CStatus::Create is called to instantiate the status bar.
5.  \_OnViewRefresh enumerates through all devices and initializes and adds all devices (CItemData) to CDevices and updates the status bar to show the number of devices.
6.  CDevices::AddItem adds the item to the treeview representing the devices, with a pointer to itself as the TVITEM.lparam. All CDevice (devices) and CDevFiles (file) objects are stored in this member of the treeview node in the appropriate window.

**On selecting a device**

The following main steps occur when the user selects a device in the left-hand pane of the application window.

1.  The CDevices window traps a click and posts a WM\_DRM\_UPDATEDEVICE message, to itself.
2.  CDevices receives its own message and calls UpdateSelection, which tells the global CDevFiles object to clear everything, enumerate all the top-level items in the device, and calls CDevFiles::AddItem to add each to the files pane.
3.  Finally, CDevices calls CDevFiles::UpdateStatusBar to update the status bar with the correct device and file information.

**On creating a playlist**

After clicking "Create Playlist" on the **Containers** menu, the application calls the local function \_OnCreatePlaylist, which performs the following actions:

1.  Get the number of selected items from the global CDevFiles variable.
2.  Call the local function DlgNamePlaylist to open a dialog box to get a name for the playlist.
3.  Call the CProgress::Create to create a dialog window showing the progress of the action, and set parameters on the CProgress class, such as the title text, range, current value, and so on.
4.  Loop through all the selected items in the CDevFiles tree view object, and request the CItemData object associated with each selected file in the tree view, incrementing the progress dialog bar with each file. The files are added to an array of [**IWMDMStorage**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstorage) interfaces.
5.  Get a handle to the currently selected item and query it for an [**IWMDMStorageControl3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstoragecontrol3) interface, which will be used later to create the new playlist on the device.
6.  Query the selected object for [**IWMDMStorage3**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstorage3), and call [**CreateEmptyMetadataObject**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage3-createemptymetadataobject) to create a new [**IWMDMMetaData**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmmetadata)interface.
7.  Add the WMDM\_FORMATCODE\_ABSTRACTAUDIOVIDEOPLAYLIST format code to the new **IWMDMMetadata** interface and create a playlist on the device by calling [**IWMDMStorageControl3::Insert3**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstoragecontrol3-insert3), passing in the metadata interface. The method retrieves a pointer to the new **IWMDMStorage** on the device.
8.  Fill the playlist by querying the new storage for [**IWMDMStorage4**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmstorage4), and calling [**IWMDMStorage4::SetReferences**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmstorage4-setreferences), passing in the array of **IWMDMStorage** pointers collected in step 4.
9.  Finally, create a new CItemData object to hold the new playlist on the device, initialize it with the new storage, and call CDevFiles::AddItem to add it to the CDevFiles pane.

## Related topics

<dl> <dt>

[**Sample Desktop Application**](sample-desktop-application.md)
</dt> </dl>

 

 




