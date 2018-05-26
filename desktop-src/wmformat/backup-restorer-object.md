---
title: Backup Restorer Object
description: Backup Restorer Object
ms.assetid: 83ce28c0-fd17-46ff-94c0-d28124a0e56a
keywords:
- Windows Media Format SDK,backup restorer objects
- Advanced Systems Format (ASF),backup restorer objects
- ASF (Advanced Systems Format),backup restorer objects
- objects,backup restorer objects
- backup restorer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Backup Restorer Object

The backup restorer provides interfaces to handle backing up licenses, typically onto removable media, and then restoring those licenses onto a new computer.

The backup restorer object is created by the [**WMCreateBackupRestorer**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer?branch=master) function, which sets a pointer to an [**IWMLicenseBackup**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlicensebackup?branch=master) interface. The other interfaces of the backup restorer object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the backup restorer object.



| Interface                                              | Description                                                                                                                                               |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMBackupRestoreProps**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmbackuprestoreprops?branch=master) | Sets and retrieves properties required by the [**IWMLicenseBackup**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlicensebackup?branch=master) and [**IWMLicenseRestore**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlicenserestore?branch=master) interfaces. |
| [**IWMLicenseBackup**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlicensebackup?branch=master)           | Backs up licenses, typically so that they can be restored onto another computer.                                                                          |
| [**IWMLicenseRestore**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmlicenserestore?branch=master)         | Restores licenses.                                                                                                                                        |



 

The following callback interface must be implemented by the application in order to use the backup restorer object.



| Interface                                      | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**IWMStatusCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstatuscallback?branch=master) | Receives status messages from processes that execute in a separate thread. |



 

## Related topics

<dl> <dt>

[**Backing Up and Restoring Licenses**](backing-up-and-restoring-licenses.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




