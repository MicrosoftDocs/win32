---
title: What's New (IMAPI)
description: The following table identifies what is new for each release of the Image Mastering API.
ms.assetid: a90daec2-5916-4c24-b2ad-94199641a2ab
ms.topic: article
ms.date: 05/31/2018
---

# What's New: Image Mastering API

The following table identifies what is new for each release of the Image Mastering API.




| Version | Description of features | 
|---------|-------------------------|
| Version 2.0 | Much of the API has been redesigned. Most of the version 1.0 functionality is still available in version 2.0. Those writing image mastering applications or performing new device and format development are encouraged to use version 2.0 instead of version 1.0.<br /> IMAPI 2.0 is included in Windows Vista. Enabling the same functionality for Windows XP and Windows Server 2003 requires the installation of the <a href="https://support.microsoft.com/kb/932716">KB932716</a> update package.<br /> Point-Release Notes:<br /><ul><li>An update offering multi-boot support via the <a href="/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage2"><strong>IFileSystemImage2</strong></a> interface was introduced in Windows Vista with Service Pack 1 (SP1) and Windows Server 2008.<br /></li><li>A feature update offering mastering support for the BD-R\BD-RE format, RAW CD Disc-at-Once image creation, as well as burn verification was included in the <a href="https://www.microsoft.com/downloads/details.aspx?FamilyID=63ab51ea-99c9-45c0-980a-c556746fcf05">Windows Feature Pack for Storage</a>. This feature update is supported on Windows Vista with SP1, Windows XP with Service Pack 2 (SP2) and later, and Windows Server 2003 with Service Pack 1 (SP1) and later. Additionally, these features are included in Windows 7 and Windows Server 2008.<br /></li><li>IMAPI 2.0 features native to Windows 7 and Windows Server 2008 include 'Gapless Burning' for audio cds and the elimination of 'Double Stashing' during burn operations. Double Stashing is a process, within the larger burn operation, in which every file is stashed before being burned to disc. With the latest version of IMAPI 2.0, files are selectively choosen for stashing, leaving the remaining files (mostly large files) non-stashed. The end result is saved disk space and operation time.<br /></li></ul> | 
| Version 1.0 | Initial release. Lets an application stage and burn a simple audio or data image to CD-R and CD-RW devices. The API supports the Joliet and ISO 9660 format for Redbook audio and data discs. For information on version 1.0, see <a href="imapiv1.md">IMAPIv1 Support</a>.Included in Windows XP.<br /> | 




 

## Version 2.0

-   Allows applications to burn to the DVD-R, DVD+R, DVD-RW, DVD+RW, DVD+DL, DVD-DL, and DVD-RAM, BD-R, and BD-RE media formats.
-   Allows recording to multiple drives at the same time. In version 1.0, only one recorder on the system could be used by IMAPI at one time. If you run a version 1.0 application on Windows Vista, other applications may concurrently use IMAPI 1.0 or 2.0 interfaces on other drives in the system. While this is generally seen as a benefit, applications which relied upon the single system burner behavior may require minor updates.
-   Access to a recorder is denied when the recorder is writing information to the disc. Otherwise, the recorder is available to other clients.
-   Supports more than one stash file on a client computer whereas version 1.0 allowed only one system-wide stash file.
-   On Windows Vista, version 1.0 no longer contains service or kernel-mode components. However, the [**IDiscRecorder2**](/windows/desktop/api/imapi2/nn-imapi2-idiscrecorder2) interface still uses the IOCTL\_CDROM\_EXCLUSIVE\_ACCESS and IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT commands to manage access or communication to specific drive devices.
-   On Windows Vista, the version 1.0 interfaces now call the version 2.0 interfaces.
-   Included with Windows Vista with SP1 and Windows Server 2008, IMAPI vesion 2.0 offers multiboot support via the [**IFileSystemImage2**](/windows/desktop/api/imapi2fs/nn-imapi2fs-ifilesystemimage2) interface.
-   Allows the use of 'Gapless Burning' for audio CDs. With Gapless Burning, the audible gap between audio tracks can be removed.
-   Replaced 'Double Stashing' with a process that specifically selects files for stashing, and leaves the remaining files (mostly large files) non-stashed. The end result is saved disk space and operation time.
-   With the [Windows Feature Pack for Storage](https://www.microsoft.com/downloads/details.aspx?FamilyID=63ab51ea-99c9-45c0-980a-c556746fcf05), burn verification options have been made available with a property accessed via [**IBurnVerification**](/windows/desktop/api/imapi2/nn-imapi2-iburnverification).
