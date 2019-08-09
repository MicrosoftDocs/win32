---
title: Setup Configuration
description: Setup configuration requires administrator privileges and is persistent across restarts.
ms.assetid: 96e9c069-829b-4615-b94b-3761bc541440
ms.topic: article
ms.date: 05/31/2018
---

# Setup Configuration

Setup configuration requires administrator privileges and is persistent across restarts. Typically, a setup application running with administrator privileges performs such persistent configuration during setup so that applications can then run at lower privilege, though persistent configuration may be done at any time. Setup configuration can include any of the following four activities:

-   Creating a URL reservation. The HTTP API enables the setup application to reserve URL prefixes for request queues associated with specific applications. To reserve a URL, the setup application calls the [**HttpSetServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpsetserviceconfiguration) function with *ConfigId* parameter set to **HttpServiceConfigUrlAclInfo** and passes a pointer in the *pConfigInformation* parameter to an [**HTTP\_SERVICE\_CONFIG\_URLACL\_SET**](/windows/desktop/api/Http/ns-http-http_service_config_urlacl_set) structure containing the registration information. For more information, see [Namespace Reservations, Registrations, and Routing](namespace-reservations-registrations-and-routing.md).
-   Configuring SSL. To configure SSL, the administrator calls the [**HttpSetServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpsetserviceconfiguration) function with *ConfigId* parameter set to **HttpServiceConfigSSLCertInfo** and passes a pointer in the *pConfigInformation* parameter to an [**HTTP\_SERVICE\_CONFIG\_SSL\_SET**](/windows/desktop/api/Http/ns-http-http_service_config_ssl_set) structure containing the SSL certificate information.
-   Setting other HTTP server–wide, persistent configurations, such as the IP addresses on which the HTTP server will listen and the server-wide timeout value. See [IP Listen List](ip-listen-list.md) and [**HTTP\_SERVICE\_CONFIG\_TIMEOUT\_SET**](/windows/desktop/api/Http/ns-http-http_service_config_timeout_set).

 

 




