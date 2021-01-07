---
description: After you create an attachment snap-in extension, you must register it in order for the MMC and the Security Configuration snap-ins to locate and use it.
ms.assetid: 176a658c-b1fd-40c5-a2ac-c9a2b7060c55
title: Registering an Attachment Snap-in Extension
ms.topic: article
ms.date: 05/31/2018
---

# Registering an Attachment Snap-in Extension

After you create an attachment snap-in extension, you must register it in order for the MMC and the Security Configuration snap-ins to locate and use it.

Your attachment snap-in must extend the Security Configuration snap-ins namespace by adding its own node as described in the following procedure.

**To install and register the attachment snap-in extension**

1.  Register the snap-in extension under the following registry key. Do not create a StandAlone key under the snap-in; attachment snap-ins extensions must only be extensions.

    ```
    HKEY_LOCAL_MACHINE
       SOFTWARE
          Microsoft
             MMC
                SnapIns
    ```

2.  Register the attachment snap-in extension under the following subkeys. This can be done as part of your **DllRegisterServer** and **DllUnregisterServer** function implementations.

    [Security Templates](security-templates.md) namespace:

    ```
    HKLM
       SOFTWARE
          Microsoft
             MMC
                NodeTypes
                   24a7f717-1f0c-11d1-affb-00c04fb984f9
                      Extensions
                         NameSpace
    ```

    [Security Configuration and Analysis](security-configuration-and-analysis.md) namespace:

    ```
    HKLM
       SOFTWARE
          Microsoft
             MMC
                NodeTypes
                   678050c7-1ff8-11d1-affb-00c04fb984f9
                      Extensions
                         NameSpace
    ```

 

 



