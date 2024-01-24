---
title: Backing Up and Restoring Licenses
description: Backing Up and Restoring Licenses
ms.assetid: 59be02fe-f207-4161-8765-9a88a8050248
keywords:
- Windows Media Format SDK,backing up licenses
- Windows Media Format SDK,restoring licenses
- Windows Media Format SDK,license backup and restore
- Advanced Systems Format (ASF),backing up licenses
- ASF (Advanced Systems Format),backing up licenses
- Advanced Systems Format (ASF),restoring licenses
- ASF (Advanced Systems Format),restoring licenses
- Advanced Systems Format (ASF),license backup and restore
- ASF (Advanced Systems Format),license backup and restore
- digital rights management (DRM),backing up licenses
- DRM (digital rights management),backing up licenses
- digital rights management (DRM),restoring licenses
- DRM (digital rights management),restoring licenses
- digital rights management (DRM),license backup and restore
- DRM (digital rights management),license backup and restore
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Backing Up and Restoring Licenses

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The backup and restore processes are asynchronous. They are triggered when the user selects a menu command or option in the application to back up or restore licenses. You should allow the user to specify the locations where licenses must be backed up to and restored from.

To back up licenses:

1.  Use the [**WMCreateBackupRestorer**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatebackuprestorer) function to create the backup restorer object.
2.  Call the [**IWMBackupRestoreProps::SetProp**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmbackuprestoreprops-setprop) method to set the backup path (the location where you will write the files, such as A:\\ or D:\\Licenses).
3.  Call the [**IWMLicenseBackup::BackupLicenses**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlicensebackup-backuplicenses) method to back up the licenses to the specified path.

The following events are sent to the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method:

-   **WMT\_BACKUPRESTORE\_BEGIN** indicates the backup process has started.
-   **WMT\_BACKUPRESTORE\_END** indicates the backup process has been completed.
-   **WMT\_RESTRICTED\_LICENSE** indicates that one or more licenses cannot be backed up because the right has been disallowed by the content owner.

The key ID is also included in this message. If you have implemented a database for protected files that includes the key ID and metadata, you can display a message to the user with the specific title (such as a song title) for which the license cannot be backed up. Otherwise, the message must be generic and inform the user that some licenses cannot be backed up.

To restore licenses:

1.  Use the **WMCreateBackupRestorer** function to create the backup restorer object.
2.  Call the **IWMBackupRestoreProps::SetProp** method to set the restore path to the location where licenses are backed up.
3.  Call the [**IWMLicenseRestore::RestoreLicenses**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmlicenserestore-restorelicenses) method to restore licenses from that location.

The following events are sent to the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method:

-   **WMT\_BACKUPRESTORE\_CONNECTING** indicates that the application is connecting to the License Management Service.
-   **WMT\_BACKUPRESTORE\_DISCONNECTING** indicates that the application is disconnecting from the License Management Service.
-   **WMT\_BACKUPRESTORE\_BEGIN** indicates the restore process has started.
-   **WMT\_BACKUPRESTORE\_END** indicates the restore process has been completed.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Digital Rights Management Features**](digital-rights-management-features.md)
</dt> <dt>

[**IWMBackupRestoreProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmbackuprestoreprops)
</dt> <dt>

[**IWMLicenseBackup Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicensebackup)
</dt> <dt>

[**IWMLicenseRestore Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmlicenserestore)
</dt> </dl>

 

 




