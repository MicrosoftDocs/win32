---
Description: 'Each fax routing extension must register with the fax service during installation to provide information about the extension and its fax routing methods. A fax routing extension can only be installed directly on a fax server (local installation).'
ms.assetid: 'ed27d558-1c8f-496b-830f-a8c4675ff56f'
title: Fax Routing Extension Registration
---

# Fax Routing Extension Registration

Each fax routing extension must register with the fax service during installation to provide information about the extension and its fax routing methods. A fax routing extension can only be installed directly on a fax server (local installation).

Only an administrator can register or unregister a routing extension. Registration and unregistration will only take place after you restart the fax service.

To register a fax routing extension locally with the fax service, use the [**IFaxServer::RegisterInboundRoutingExtension**](-mfax-faxserver-cpp-mfax-faxserver-registerinboundroutingextension-cpp.md) method. To unregister a fax routing extensions, use the [**IFaxServer::UnregisterInboundRoutingExtension**](-mfax-faxserver-cpp-mfax-faxserver-unregisterinboundroutingextension-cpp.md) method.

 

 



