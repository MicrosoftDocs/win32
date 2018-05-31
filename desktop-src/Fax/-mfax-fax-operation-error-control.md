---
Description: The fax service calls the FaxDevStartJob function to signal the beginning of a fax operation to the fax service provider (FSP).
ms.assetid: eb015448-f61e-431b-9533-47523d3896fc
title: Fax Operation Error Control
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Operation Error Control

The fax service calls the [**FaxDevStartJob**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevstartjob) function to signal the beginning of a fax operation to the fax service provider (FSP). If a fax operation starts, but the FSP cannot gain access to the line that the fax service indicates, the FSP should take both of the following steps.

-   Return a value of zero from the [**FaxDevSend**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevsend) or the [**FaxDevReceive**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevreceive) function call.
-   Set the **StatusId** member of the [**FAX\_DEV\_STATUS**](/previous-versions/windows/desktop/api/FaxDev/ns-faxdev-_fax_dev_status) structure to an **FS\_LINE\_UNAVAILABLE** status.

When the fax service calls the [**FaxDevReportStatus**](/previous-versions/windows/desktop/api/FaxDev/nf-faxdev-faxdevreportstatus) function it will detect that the line is not available. The fax service will select another line and call the fax operation again.

 

 



