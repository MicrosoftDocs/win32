---
Description: 'Each fax service provider (FSP) must register with the fax service during installation to provide information about the provider. An FSP can only be installed directly on a fax server (local installation).'
ms.assetid: '86dbd53b-79f8-49e2-8b41-02849891b413'
title: Fax Service Provider Registration
---

# Fax Service Provider Registration

Each fax service provider (FSP) must register with the fax service during installation to provide information about the provider. An FSP can only be installed directly on a fax server (local installation).

Only an administrator can register or unregister an FSP. Registration and unregistration will only take place after you restart the fax service.

To register an FSP locally with the fax service, use the [**IFaxServer::RegisterDeviceProvider**](-mfax-faxserver-cpp-mfax-faxserver-registerdeviceprovider-cpp.md) method. To unregister an FSP, use the [**IFaxServer::UnregisterDeviceProvider**](-mfax-faxserver-cpp-mfax-faxserver-unregisterdeviceprovider-cpp.md) method.

 

 



