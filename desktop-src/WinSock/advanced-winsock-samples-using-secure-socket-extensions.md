---
Description: Advanced Winsock Samples Using Secure Socket Extensions
ms.assetid: 9c429363-f9bb-4394-89be-f87507f5cbdd
title: Advanced Winsock Samples Using Secure Socket Extensions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Advanced Winsock Samples Using Secure Socket Extensions

## Secure TCP Client and Server Sample

A more advanced Winsock sample that demonstrates the use of secure socket extensions is included with the Microsoft Windows Software Development Kit (SDK). The sample includes a TCP client and server that connect securely using the Winsock and the secure socket extensions.

By default, the Winsock sample source code is installed in the following directory:

*C:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Samples\\NetDs\\winsock*

A sample is located under the following folder:

*securesocket*

The sample code is split into separate directories as described below:

-   stcpclient - the folder that contains the secure TCP client code.
-   stcpcommon - the folder that contains common library code that is shared between the secure TCP client and server.
-   stcpserver - the folder that contains the secure TCP server code.

It should be noted that the samples are meant to be run on two different computers running Windows Vista or later. Additionally, IPsec credentials must be provisioned on both the computers for the connection to succeed, because the sample uses IPsec for securing its traffic. Please refer to the documentation on [IPsec Configuration](https://msdn.microsoft.com/library/windows/desktop/bb736264) for more information on setting up IPsec credentials.

Building the sample will generate two executable files:

*stcpclient.exe* and *stcpserver.exe*.

Copy *stcpclient.exe* to computer A and copy *stcpserver.exe* to computer B. On computer B, start the TCP server by executing the following in a Command Prompt:

**stcpserver.exe**

Execute the following command for more usage options for the server:

**stcpserver.exe /?**

Then on computer A, start the TCP client by executing the following in a Command Prompt:

**stcpclient.exe <fully-qualified-DNS-name-for-machine-B>**

At this point the connection should get established securely.

Execute the following command for more usage options for the client:

**stcpclient.exe /?**

## Related topics

<dl> <dt>

[About Windows Filtering Platform](https://msdn.microsoft.com/library/windows/desktop/aa363967)
</dt> <dt>

[Application Layer Enforcement (ALE)](https://msdn.microsoft.com/library/windows/desktop/aa363971)
</dt> <dt>

[IPsec Configuration](https://msdn.microsoft.com/library/windows/desktop/bb736264)
</dt> <dt>

[IPsec Functions](https://msdn.microsoft.com/library/windows/desktop/aa364938)
</dt> <dt>

[Using Secure Socket Extensions](using-secure-socket-extensions.md)
</dt> <dt>

[Security Support Provider Interface (SSPI)](https://msdn.microsoft.com/library/windows/desktop/aa378663)
</dt> <dt>

[Windows Filtering Platform](https://msdn.microsoft.com/library/windows/desktop/aa366510)
</dt> <dt>

[Windows Filtering Platform API Functions](https://msdn.microsoft.com/library/windows/desktop/aa364931)
</dt> <dt>

[Winsock Secure Socket Extensions](winsock-secure-socket-extensions.md)
</dt> </dl>

 

 



