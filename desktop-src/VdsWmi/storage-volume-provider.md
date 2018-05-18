---
title: Storage Volume Provider
description: The Storage Volume provider supplies volume management functions.
ms.assetid: '7a32bcb0-f4b0-4e48-aea0-865be93d48c7'
---

# Storage Volume Provider

The Storage Volume provider supplies volume management functions. The provider enumerates all existing volumes that the Windows Mount Manager recognizes, and volumes enumerated in the [**FindFirstVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364425) or [**FindNextVolume**](https://msdn.microsoft.com/library/windows/desktop/aa364431) Windows APIs.

You can use this provider to manage volume drive letters, mount points, and for storage quotas. The Storage Volume provider also has methods to defragment, check, mount, dismount, and format a volume. This provider does not manage mapped network or diskette drives. No direct relationship exists between [**Win32\_Volume**](win32-volume.md) and [**Win32\_DiskDrive**](https://msdn.microsoft.com/library/aa394132). The name of the [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name is "MSVDS\_PROVIDER".

**Windows XP:** The Storage Volume Provider is not available.

The Storage Volume provider can modify and enumerate disk volume objects. This provider is implemented through the instance of [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) named "MSVDS\_PROVIDER". **PutInstance** is supported for classes that belong to this provider.

The Storage Volume provider is an instance and method provider that implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)

The Storage Volume provider supports the following classes:

-   [**Win32\_Volume**](win32-volume.md)
-   [**Win32\_DefragAnalysis**](win32-defraganalysis.md)

The Storage Volume provider supports the following association classes in the root\\cimv2 namespace:

-   [**Win32\_MountPoint**](win32-mountpoint.md)
-   [**Win32\_VolumeQuota**](win32-volumequota.md)
-   [**Win32\_VolumeUserQuota**](win32-volumeuserquota.md)
-   

The [**Win32\_Volume**](win32-volume.md) class defines the following methods to manage volumes:

-   [**AddMountPoint**](addmountpoint-method-in-class-win32-volume.md)
-   [**Chkdsk**](chkdsk-method-in-class-win32-volume.md)
-   [**ExcludeFromAutoChk**](excludefromautochk-method-in-class-win32-volume.md)
-   [**Format**](format-method-in-class-win32-volume.md)
-   [**Defrag**](defrag-method-in-class-win32-volume.md)
-   [**DefragAnalysis**](defraganalysis-method-in-class-win32-volume.md)
-   [**Dismount**](dismount-method-in-class-win32-volume.md)
-   [**Mount**](mount-method-in-class-win32-volume.md)
-   [**ScheduleAutoChk**](scheduleautochk-method-in-class-win32-volume.md)

 

 




