---
title: Advanced Winsock sample app using secure socket extensions
description: A more advanced Winsock sample app that demonstrates the use of secure socket extensions is available in the Windows-classic-samples GitHub repo.
ms.date: 05/31/2024
ms.assetid: 9c429363-f9bb-4394-89be-f87507f5cbdd
ms.topic: concept-article
---

# Advanced Winsock sample app using secure socket extensions

## Secure TCP client and server sample app

A more advanced Winsock sample app that demonstrates the use of secure socket extensions is available in the [Windows-classic-samples](https://github.com/microsoft/Windows-classic-samples/tree/main/Samples/Win7Samples/netds/winsock/securesocket) GitHub repo. The sample includes a TCP client and server that connect securely using the Winsock and the secure socket extensions.

The sample code is split into separate directories as described below:

* stcpclient. The folder that contains the secure TCP client code.
* stcpcommon. The folder that contains common library code that is shared between the secure TCP client and server.
* stcpserver. The folder that contains the secure TCP server code.

The samples are meant to be run on two different computers running Windows Vista or later. Additionally, IPsec credentials must be provisioned on both the computers for the connection to succeed, because the sample uses IPsec for securing its traffic. Please refer to the documentation on [IPsec Configuration](/windows/desktop/FWP/ipsec-configuration) for more information on setting up IPsec credentials.

Building the sample will generate two executable files:

*stcpclient.exe* and *stcpserver.exe*.

Copy *stcpclient.exe* to computer A and copy *stcpserver.exe* to computer B. On computer B, start the TCP server by executing the following in a Command Prompt:

**stcpserver.exe**

Execute the following command for more usage options for the server:

**stcpserver.exe /?**

Then on computer A, start the TCP client by executing the following in a Command Prompt:

**stcpclient.exe &lt;fully-qualified-DNS-name-for-machine-B&gt;**

At this point the connection should get established securely.

Execute the following command for more usage options for the client:

**stcpclient.exe /?**

## Related topics

* [About Windows Filtering Platform](/windows/desktop/FWP/about-windows-filtering-platform)
* [Application Layer Enforcement (ALE)](/windows/desktop/FWP/application-layer-enforcement--ale-)
* [IPsec Configuration](/windows/desktop/FWP/ipsec-configuration)
* [IPsec Functions](/windows/desktop/FWP/fwp-ipsec-functions)
* [Using Secure Socket Extensions](using-secure-socket-extensions.md)
* [Security Support Provider Interface (SSPI)](/windows/desktop/Rpc/security-support-provider-interface-sspi-)
* [Windows Filtering Platform](/windows/desktop/FWP/windows-filtering-platform-start-page)
* [Windows Filtering Platform API Functions](/windows/desktop/FWP/fwp-functions)
* [Winsock Secure Socket Extensions](winsock-secure-socket-extensions.md)
