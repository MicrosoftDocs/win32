---
title: Disk Quota Provider
description: The Windows Disk Quota provider allows administrators to control the amount of data that each user stores on an NTFS file system.
ms.assetid: '0d22c376-0fbf-4e16-ac91-612933bf5d17'
keywords: ["providers Windows Management Instrumentation , Disk Quota", "Disk Quota provider Windows Management Instrumentation"]
---

# Disk Quota Provider

The Windows Disk Quota provider allows administrators to control the amount of data that each user stores on an NTFS file system. The provider can log events when users are near their quota, and deny further disk space to users who exceed their quota. The [Event Log provider](https://msdn.microsoft.com/library/aa390413) can be used with the Disk Quota provider to track quota issues. The [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name is "DskQuotaProvider".

**Windows XP:** The Disk Quota provider is not available.

As an instance, method, and event provider, the Disk Quota provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The Disk Quota provider also implements the following provider framework interface:

-   [**Provider::EnumerateInstances**](https://msdn.microsoft.com/library/aa392767)

The Wmipdskq.mof file contains the Disk Quota provider, and association and registration classes. You can access the Disk Quota provider classes only in the root\\cimv2 namespace.

The Disk Quota provider supports the following classes:

-   [**Win32\_DiskQuota**](win32-diskquota.md)
-   [**Win32\_QuotaSetting**](win32-quotasetting.md)
-   [**Win32\_VolumeQuotaSetting**](win32-volumequotasetting.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




