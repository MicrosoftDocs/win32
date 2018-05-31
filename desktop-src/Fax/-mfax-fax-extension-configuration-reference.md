---
Description: The fax service extension configuration mechanism includes the function and callback functions listed in this topic.
ms.assetid: ded5e212-a770-4673-abe5-7238c26a7dfd
title: Fax Extension Configuration Reference
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Extension Configuration Reference

The fax service extension configuration mechanism includes the function and callback functions listed in this topic.

If you plan to implement the fax extension configuration mechanism, you must include the appropriate fax extension configuration header in your source code files. If you are programming on Windows XP, you must include FaxExt.h.

Each fax extension DLL must export the following function to implement the fax extension configuration mechanism.

-   [**FaxExtInitializeConfig**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextinitializeconfig)

The fax service provides the following callback functions to allow an extension to retrieve and set fax device configuration data, and to receive notifications from the fax service about changes in device configuration data.

-   [**FaxExtFreeBuffer**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextfreebuffer)
-   [**FaxExtGetData**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextgetdata)
-   [**FaxExtRegisterForEvents**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextregisterforevents)
-   [**FaxExtSetData**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextsetdata)
-   [**FaxExtUnregisterForEvents**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextunregisterforevents)

The following callback function name is a placeholder for a function defined by the fax extension DLL.

-   [**FaxExtConfigChange**](/previous-versions/windows/desktop/api/FaxExt/nf-faxext-faxextconfigchange)

 

 



