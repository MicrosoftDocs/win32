---
Description: 'The fax service extension configuration mechanism includes the function and callback functions listed in this topic.'
ms.assetid: 'ded5e212-a770-4673-abe5-7238c26a7dfd'
title: Fax Extension Configuration Reference
---

# Fax Extension Configuration Reference

The fax service extension configuration mechanism includes the function and callback functions listed in this topic.

If you plan to implement the fax extension configuration mechanism, you must include the appropriate fax extension configuration header in your source code files. If you are programming on Windows XP, you must include FaxExt.h.

Each fax extension DLL must export the following function to implement the fax extension configuration mechanism.

-   [**FaxExtInitializeConfig**](-mfax-faxextinitializeconfig.md)

The fax service provides the following callback functions to allow an extension to retrieve and set fax device configuration data, and to receive notifications from the fax service about changes in device configuration data.

-   [**FaxExtFreeBuffer**](-mfax-faxextfreebuffer.md)
-   [**FaxExtGetData**](-mfax-faxextgetdata.md)
-   [**FaxExtRegisterForEvents**](-mfax-faxextregisterforevents.md)
-   [**FaxExtSetData**](-mfax-faxextsetdata.md)
-   [**FaxExtUnregisterForEvents**](-mfax-faxextunregisterforevents.md)

The following callback function name is a placeholder for a function defined by the fax extension DLL.

-   [**FaxExtConfigChange**](-mfax-faxextconfigchange.md)

 

 



