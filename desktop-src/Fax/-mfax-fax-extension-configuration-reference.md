---
Description: The fax service extension configuration mechanism includes the function and callback functions listed in this topic.
ms.assetid: ded5e212-a770-4673-abe5-7238c26a7dfd
title: Fax Extension Configuration Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Extension Configuration Reference

The fax service extension configuration mechanism includes the function and callback functions listed in this topic.

If you plan to implement the fax extension configuration mechanism, you must include the appropriate fax extension configuration header in your source code files. If you are programming on Windows XP, you must include FaxExt.h.

Each fax extension DLL must export the following function to implement the fax extension configuration mechanism.

-   [**FaxExtInitializeConfig**](/windows/previous-versions/FaxExt/nf-faxext-faxextinitializeconfig?branch=master)

The fax service provides the following callback functions to allow an extension to retrieve and set fax device configuration data, and to receive notifications from the fax service about changes in device configuration data.

-   [**FaxExtFreeBuffer**](/windows/previous-versions/FaxExt/nf-faxext-faxextfreebuffer?branch=master)
-   [**FaxExtGetData**](/windows/previous-versions/FaxExt/nf-faxext-faxextgetdata?branch=master)
-   [**FaxExtRegisterForEvents**](/windows/previous-versions/FaxExt/nf-faxext-faxextregisterforevents?branch=master)
-   [**FaxExtSetData**](/windows/previous-versions/FaxExt/nf-faxext-faxextsetdata?branch=master)
-   [**FaxExtUnregisterForEvents**](/windows/previous-versions/FaxExt/nf-faxext-faxextunregisterforevents?branch=master)

The following callback function name is a placeholder for a function defined by the fax extension DLL.

-   [**FaxExtConfigChange**](/windows/previous-versions/FaxExt/nf-faxext-faxextconfigchange?branch=master)

 

 



