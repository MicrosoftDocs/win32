---
title: Kernel Mode SSL
description: Kernel Mode SSL
ms.assetid: ada82704-cb7d-4e98-8c87-76c7bfbd098b
keywords:
- Kernel Mode SSL
ms.topic: article
ms.date: 05/31/2018
---

# Kernel Mode SSL

Kernel mode SSL was introduced in Windows Server 2003 with Service Pack 1 (SP1) with limited support. For computers running on Windows Server 2003 with SP1 a registry key must be set to enable kernel SSL. For computers running on Windows Server 2008 and Windows Vista, full kernel mode support for SSL is provided.

The following sections describe kernel mode SSL support:

-   Kernel Modes SSL in Windows Server 2003 with SP1
-   Kernel Mode SSL in Windows Server 2008 and Windows Vista

## Kernel Modes SSL in Windows Server 2003 with SP1

In Windows Server 2003 with SP1, HTTP Server API provides the option of running SSL security in kernel mode (user mode SSL is the default). The kernel mode feature improves SSL performance by moving encryption and decryption operations to the kernel, thus reducing the number of transitions between kernel mode and user mode.

The following features are not supported when SSL is run in kernel mode:

-   Client certificates
-   RC2 ciphers
-   The PCT 1.0 protocol
-   Server certificate configuration changes require a restart of the HTTP service
-   Bulk encryption and offload support

## Configuring Kernel Mode SSL

Kernel mode SSL is controlled by the **EnableKernelSSL** registry value and is enabled by setting the value to 1. Enabling kernel mode SSL will disable user mode SSL and requires the HTTP service to be restarted to take effect. The **EnableKernelSSL** registry key is located at:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**HTTP**\\**Parameters**\\**EnableKernelSSL**

## Kernel Mode SSL in Windows Server 2008 and Windows Vista

For computers running on Windows Server 2008 and Windows Vista, the HTTP Server API features enhanced SSL functionality.

The following new features are supported:

-   Full client certificate support in kernel mode SSL
-   Kernel mode SSL for all HTTP SSL transactions
-   Bulk encryption and offload support
-   The PCT 1.0 protocol
-   RC2 ciphers
-   Increased performance over user mode SSL

## Configuration

Kernel mode SSL is configurable through two registry values under the HTTP Parameters key located at:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            HTTP
               Parameters
                  EnableSslCloseNotify
                  DisableSslCertChainCacheOnlyUrlRetrieval
```

A user must have Administrator/Local System privileges to modify the registry values and view, or modify, the log files and the folder that contains them.

Configuration information in the registry values is read when the HTTP Server API driver is started. As a result, if the settings are changed the driver must be stopped and restarted to read the new values. This can be accomplished by using the following console commands:

**net stop http**

**net start http**

The following table lists registry configuration values.




| Registry Value | Description | 
|----------------|-------------|
| EnableKernelSSL | <strong>Windows Server 2008 and Windows Vista:</strong> This registry value is obsolete.<br /> | 
| EnableSslCloseNotify | A <strong>DWORD</strong> value that is set to <strong>TRUE</strong> to enable close-notify, or <strong>FALSE</strong> to disable the close-notify requirement. Close-notify is disabled by default.<br /> When close-notify is enabled, the client application is required to send a close-notify message before closing TCP connections. The HTTP Server API also sends a close-notify before closing the connection.<br /> When close-notify is enabled, and the client sends a close-notify message, the HTTP Server API will reuse the SSL session on future connections to the client. If the client does not send a close-notify, the HTTP Server API will not reuse the same SSL session on future connections. Thus, a full SSL handshake is triggered on the new connection thereby reducing performance. <br /><blockquote>[!Note]<br />Enabling close-notify helps mitigate truncation attacks against the HTTPS requests and responses.</blockquote><br /><br /> When close-notify is disabled, the HTTP Server API reuses the SSL session for future connections.<br /> | 
| DisableSslCertChainCacheOnlyUrlRetrieval | A <strong>DWORD</strong> value that is set to <strong>TRUE</strong> to enable the HTTP Server API to retrieve intermediate certificates from either the Internet, or the local store, or <strong>FALSE</strong> to retrieve intermediate certificates from the local store only. The default registry value is <strong>FALSE</strong>.<br /> By default, the HTTP Server API builds a client certificate chain by retrieving the intermediate certificates from the Intermediate Certificate Authority store under the local machine account. Setting this value to <strong>TRUE</strong> enables the HTTP Server API to retrieve the intermediate certificates not only from the local store, but also from the Intermediate Certificate Authority on the Internet.<br /> | 




 

 

 





