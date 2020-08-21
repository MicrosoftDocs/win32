---
title: Installing an EAP Method
description: Follow the instructions below to install a user-implemented EAP method on a client computer running EAPHost.
ms.assetid: c353550f-73a7-4195-81ea-544f74abc880
ms.topic: article
ms.date: 05/31/2018
---

# Installing an EAP Method

Follow the instructions below to install a user-implemented EAP method on a client computer running EAPHost.

-   Implement [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) and [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) for your EAP Method DLL. These functions add and remove the appropriate registry keys for your EAP method during the installation and (uninstallation) process.

    For information on the specific registry keys associated with the installation of an EAP method, see the [Registry Configuration for EAP Methods](registry-keys-for-eap-methods.md) topic.

-   Install the DLL that contains the EAP method implementation with the following console command.

    **regsvr32.exe** *&lt;DLL name&gt;*

    To uninstall the DLL, use the following console command:

    **regsvr32.exe** **/u** *&lt;DLL name&gt;*

-   Restart the EAPHost service.

## Related topics

<dl> <dt>

[Using EAPHost](using-eap-host.md)
</dt> </dl>

 

 