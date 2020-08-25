---
title: General programming guidelines
description: Guidelines for developing applications in a Remote Desktop Services environment.
ms.assetid: 95b49db5-ba3c-4638-9087-6ee3972d8972
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# General programming guidelines

The following sections provide general guidelines for developing applications in a Remote Desktop Services environment.

## In this section

<dl> <dt>

[Application compatibility layer](application-compatibility-layer.md)
</dt> <dd>

To run legacy applications in a Remote Desktop Services environment you can use the Remote Desktop Services Application Compatibility layer.

</dd> <dt>

[Client/Server application guidelines](client-server-application-guidelines.md)
</dt> <dd>

Client/server applications must not assume that a single computer connection is equivalent to a single user session.

</dd> <dt>

[Monitoring session connections and disconnections](monitoring-session-connections-and-disconnections.md)
</dt> <dd>

To register an application with Remote Desktop Services, store the name of the virtual channel server application in the registry by adding a subkey.

</dd> <dt>

[Peripheral hardware guidelines](peripheral-hardware-guidelines.md)
</dt> <dd>

If their hardware device is not designed to work over a remote session, vendors must ensure that the device driver software forces disabling the redirection of the device by using a system policy or group policy.

</dd> <dt>

[Run-Time linking to Wtsapi32.dll](run-time-linking-to-wtsapi32-dll.md)
</dt> <dd>

Your application can use the Remote Desktop Services API to dynamically link to the Wtsapi32.dll at run time. To do this, your application should call the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) function to load Wtsapi32.dll.

</dd> </dl>

 

 