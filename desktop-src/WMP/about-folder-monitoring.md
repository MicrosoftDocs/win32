---
title: About Folder Monitoring
description: About Folder Monitoring
ms.assetid: d3d83e60-ecc7-4501-a6dd-15f7680a6ec9
keywords:
- Windows Media Player,folder monitoring
- Windows Media Player object model,folder monitoring
- object model,folder monitoring
- Windows Media Player ActiveX control,folder monitoring
- ActiveX control,folder monitoring
- Windows Media Player Mobile ActiveX control,folder monitoring
- Windows Media Player Mobile,folder monitoring
- folder monitoring
- monitoring folders
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Folder Monitoring

Windows Media Player can monitor folders that contain digital media files and update the library when files are added or removed. This folder monitoring functionality is provided by the [IWMPFolderMonitorServices](/windows/win32/wmp/nn-wmp-iwmpfoldermonitorservices?branch=master) interface.

To use the folder monitoring services, you must create the Player object in a remote state. For more information about remoting, see [Remoting the Windows Media Player Control](remoting-the-windows-media-player-control.md). After you have created a remoted instance of the player, obtain a pointer to the **IWMPFolderMonitorServices** interface by calling **QueryInterface** on the [IWMPPlayer](/windows/win32/wmp/nn-wmp-iwmpplayer?branch=master) interface.

Windows Media Player keeps a list of folders that are being monitored. To get a list of monitored folders, use the [IWMPFolderMonitorServices::get\_count](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-get_count?branch=master) and [IWMPFolderMonitorServices::item](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-item?branch=master) methods. To add folders to the list or remove them from the list, use the [IWMPFolderMonitorServices::add](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-add?branch=master) and [remove](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-remove?branch=master) methods, respectively.

**Starting a Scan**

Monitoring of folders is normally a background process that does not need to be called explicitly. If you want to actively scan a folder, call [IWMPFolderMonitorServices::startScan](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-startscan?branch=master). You can stop a scan in progress with the [IWMPFolderMonitorServices::stopScan](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-stopscan?branch=master) method.

**Retrieving the Folder Monitoring Status**

**IWMPFolderMonitorServices** provides functionality for retrieving the status of the folder monitoring process.

Folder scanning is done in two passes. In the first pass, the Player scans the folders named in the monitored folders list one by one and builds a list of files to be added to the library. In the second pass, it goes through the list of files and adds the files to the library, and also removes any media items from the library whose corresponding physical files have been deleted from the file system.

The [FolderScanStateChange](/windows/win32/wmp/nf-wmp-iwmpevents3-folderscanstatechange?branch=master) event is used to notify your program whenever the Player switches to a new state. You can also retrieve the current state by calling [get\_scanState](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-get_scanstate?branch=master). When the first pass starts, the current state value is wmpfssScanning. During the second pass, the state switches to wmpfssUpdating. After the process is finished, the state changes to wmpfssStopped.

While the Player is scanning the monitored folders on the first pass, call [get\_scannedFilesCount](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-get_scannedfilescount?branch=master) to check how many files have been scanned. The [get\_currentFolder](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-get_currentfolder?branch=master) method will tell you which folder is currently being scanned.

After the second pass starts, call [get\_addedFilesCount](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-get_addedfilescount?branch=master) to check how many files have been added to the library. The [get\_updateProgress](/windows/win32/wmp/nf-wmp-iwmpfoldermonitorservices-get_updateprogress?branch=master) method will tell you the progress of the second pass, as a percentage from 0 to 100.

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**IWMPFolderMonitorServices Interface**](/windows/win32/wmp/nn-wmp-iwmpfoldermonitorservices?branch=master)
</dt> </dl>

 

 




