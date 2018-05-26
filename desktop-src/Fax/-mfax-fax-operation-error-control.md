---
Description: The fax service calls the FaxDevStartJob function to signal the beginning of a fax operation to the fax service provider (FSP).
ms.assetid: eb015448-f61e-431b-9533-47523d3896fc
title: Fax Operation Error Control
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Operation Error Control

The fax service calls the [**FaxDevStartJob**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevstartjob?branch=master) function to signal the beginning of a fax operation to the fax service provider (FSP). If a fax operation starts, but the FSP cannot gain access to the line that the fax service indicates, the FSP should take both of the following steps.

-   Return a value of zero from the [**FaxDevSend**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevsend?branch=master) or the [**FaxDevReceive**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevreceive?branch=master) function call.
-   Set the **StatusId** member of the [**FAX\_DEV\_STATUS**](/windows/previous-versions/FaxDev/ns-faxdev-_fax_dev_status?branch=master) structure to an **FS\_LINE\_UNAVAILABLE** status.

When the fax service calls the [**FaxDevReportStatus**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevreportstatus?branch=master) function it will detect that the line is not available. The fax service will select another line and call the fax operation again.

 

 



