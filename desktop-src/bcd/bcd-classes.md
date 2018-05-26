---
title: BCD WMI Provider Classes
description: The Boot Configuration Data (BCD) Windows Management Instrumentation (WMI) provider runs under the LocalService account and impersonates the client when handling requests.
ms.assetid: 43130b7a-ede8-4201-93de-8bfcadee06ff
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BCD WMI Provider Classes

The Boot Configuration Data (BCD) Windows Management Instrumentation (WMI) provider runs under the LocalService account and impersonates the client when handling requests. A client must be a member of the Administrators group, have Backup and Restore privileges, and connect to the WMI repository using an impersonation level of Impersonate, as shown in the following example.

`GetObject("winmgmts:{impersonationlevel=Impersonate,(Backup,Restore)}!root/wmi:BcdStore`

For more information, see [**WbemImpersonationLevelEnum**](https://msdn.microsoft.com/library/aa393981) and [**WbemPrivilegeEnum**](https://msdn.microsoft.com/library/aa393983).

The following are the BCD WMI provider classes:

-   [**BcdBooleanElement**](bcdbooleanelement.md)
-   [**BcdDeviceData**](bcddevicedata.md)
-   [**BcdDeviceElement**](bcddeviceelement.md)
-   [**BcdDeviceFileData**](bcddevicefiledata.md)
-   [**BcdDeviceLocateData**](bcddevicelocatedata.md)
-   [**BcdDeviceLocateElementChildData**](bcddevicelocateelementchilddata.md)
-   [**BcdDeviceLocateElementData**](bcddevicelocateelementdata.md)
-   [**BcdDeviceLocateStringData**](bcddevicelocatestringdata.md)
-   [**BcdDevicePartitionData**](bcddevicepartitiondata.md)
-   [**BcdDeviceQualifiedPartitionData**](bcddevicequalifiedpartitiondata.md)
-   [**BcdDeviceUnknownData**](bcddeviceunknowndata.md)
-   [**BcdElement**](bcdelement.md)
-   [**BcdIntegerElement**](bcdintegerelement.md)
-   [**BcdIntegerListElement**](bcdintegerlistelement.md)
-   [**BcdObject**](bcdobject.md)
-   [**BcdObjectElement**](bcdobjectelement.md)
-   [**BcdObjectListElement**](bcdobjectlistelement.md)
-   [**BcdStore**](bcdstore.md)
-   [**BcdStringElement**](bcdstringelement.md)

 

 




