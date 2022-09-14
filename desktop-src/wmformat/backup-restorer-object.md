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
ms.topic: article
ms.date: 05/31/2018
---

# Backup Restorer Object

The backup restorer provides interfaces to handle backing up licenses, typically onto removable media, and then restoring those licenses onto a new computer.

The backup restorer object is created by the [**WMCreateBackupRestorer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer) function, which sets a pointer to an [**IWMLicenseBackup**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicensebackup) interface. The other interfaces of the backup restorer object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the backup restorer object.



| Interface                                              | Description                                                                                                                                               |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMBackupRestoreProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmbackuprestoreprops) | Sets and retrieves properties required by the [**IWMLicenseBackup**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicensebackup) and [**IWMLicenseRestore**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicenserestore) interfaces. |
| [**IWMLicenseBackup**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicensebackup)           | Backs up licenses, typically so that they can be restored onto another computer.                                                                          |
| [**IWMLicenseRestore**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicenserestore)         | Restores licenses.                                                                                                                                        |



 

The following callback interface must be implemented by the application in order to use the backup restorer object.



| Interface                                      | Description                                                                |
|------------------------------------------------|----------------------------------------------------------------------------|
| [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) | Receives status messages from processes that execute in a separate thread. |



 

## Related topics

<dl> <dt>

[**Backing Up and Restoring Licenses**](backing-up-and-restoring-licenses.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> </dl>

 

 




