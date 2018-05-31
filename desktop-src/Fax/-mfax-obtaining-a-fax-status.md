---
Description: The fax service calls the FaxDevReportStatus function asynchronously to query a fax service provider (FSP) DLL about status information for an active fax operation, or for status information after a failed fax operation.
ms.assetid: 04a2154b-cde5-4c37-97a1-44dd4e12f172
title: Obtaining a Fax Status
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Fax Status

The fax service calls the [**FaxDevReportStatus**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevreportstatus) function asynchronously to query a fax service provider (FSP) DLL about status information for an active fax operation, or for status information after a failed fax operation. The service also calls **FaxDevReportStatus** synchronously at the end of each job. The [**FAX\_DEVICE\_STATUS**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_device_statusa) structure contains a status error code, a Microsoft Win32 error code, and routing information for the fax operation.

The FSP must export the [**FaxDevReportStatus**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevreportstatus) function.

 

 



