---
title: IP Listen List
description: The HTTP Server APIs do not bind to any IP address and TCP port pairs until a user registers a UrlPrefix.
ms.assetid: f2f51e6c-9114-4ba9-a37c-1d1d1f0b444f
ms.topic: article
ms.date: 05/31/2018
---

# IP Listen List

The HTTP Server APIs do not bind to any IP address and TCP port pairs until a user registers a UrlPrefix. By default, once a registration is entered in the request queue, the HTTP Server API binds to the port specified in the UrlPrefix (for example port 80) for all IP addresses (INADDR\_ANY or INADDR6\_ANY) available on the machine. Problems arise when third party applications (not using the HTTP Server APIs) bind to IP address and port 80 pairs on the machine. The HTTP Server API provides a way to configure the list of IP addresses that it binds and solves this coexistence issue. The system administrator calls the [**HttpSetServiceConfiguration**](/windows/desktop/api/Http/nf-http-httpsetserviceconfiguration) function with the *ConfigId* parameter set to the HttpServiceConfigIPListenList value to specify the IP listen list. Both IPv4 and IPv6 addresses can be added to the list. The IP addresses entered apply to all applications on the machine using the HTTP Server API and persist across reboots of the machine. However, any changes to the IP listen list configuration do not take place dynamically; in most cases, a system reboot may be necessary.

 

 




