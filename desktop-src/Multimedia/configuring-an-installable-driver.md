---
title: Configuring an Installable Driver
description: Configuring an Installable Driver
ms.assetid: c81f4bcb-38c6-42f1-a50d-1f700c6a3c37
keywords:
- installable drivers,configuring
- configuring installable drivers
- OpenDriver function
- SendDriverMessage function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configuring an Installable Driver

To direct an installable driver to carry out useful tasks, you must open the driver by using the [OpenDriver](https://msdn.microsoft.com/en-us/library/Dd743639(v=VS.85).aspx) function and send it messages by using the [SendDriverMessage](https://msdn.microsoft.com/en-us/library/Dd798653(v=VS.85).aspx) function. The following example shows how to direct the driver to display its configuration dialog box.


```C++
LONG MyConfigureDriver()
{
    HDRVR hdrvr;
    DRVCONFIGINFO dci;
    LONG lRes;

    // Open the driver (no additional parameters needed this time).
    if ((hdrvr = OpenDriver(L"\\samples\\sample.drv", 0, 0)) == 0) {
        // Can't open the driver
        return DRVCNF_CANCEL;
    }

    // Make sure driver has a configuration dialog box.
    if (SendDriverMessage(hdrvr, DRV_QUERYCONFIGURE, 0, 0) != 0) {
        // Set the DRVCONFIGINFO structure and send the message
        dci.dwDCISize = sizeof (dci);
        dci.lpszDCISectionName = (LPWSTR)0;
        dci.lpszDCIAliasName = (LPWSTR)0;
        lRes = SendDriverMessage(hdrvr, DRV_CONFIGURE, 0, (LONG)&amp;dci);
     }

    // Close the driver (no additional parameters needed this time).
    CloseDriver(hdrvr, 0, 0);

    return lRes;
}
 
```



 

 




