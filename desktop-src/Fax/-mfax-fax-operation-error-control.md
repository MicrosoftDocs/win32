---
Description: 'The fax service calls the FaxDevStartJob function to signal the beginning of a fax operation to the fax service provider (FSP).'
ms.assetid: 'eb015448-f61e-431b-9533-47523d3896fc'
title: Fax Operation Error Control
---

# Fax Operation Error Control

The fax service calls the [**FaxDevStartJob**](-mfax-faxdevstartjob.md) function to signal the beginning of a fax operation to the fax service provider (FSP). If a fax operation starts, but the FSP cannot gain access to the line that the fax service indicates, the FSP should take both of the following steps.

-   Return a value of zero from the [**FaxDevSend**](-mfax-faxdevsend.md) or the [**FaxDevReceive**](-mfax-faxdevreceive.md) function call.
-   Set the **StatusId** member of the [**FAX\_DEV\_STATUS**](-mfax-fax-dev-status-str.md) structure to an **FS\_LINE\_UNAVAILABLE** status.

When the fax service calls the [**FaxDevReportStatus**](-mfax-faxdevreportstatus.md) function it will detect that the line is not available. The fax service will select another line and call the fax operation again.

 

 



