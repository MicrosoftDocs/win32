---
Description: 'To use the HTTP or HTTPS transport, you must ensure that the transport is enabled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5e37ac64-1ff2-4132-9b15-2f9c0d3551d7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Configuring the Broker to Listen for HTTP Requests
---

# Configuring the Broker to Listen for HTTP Requests

To use the HTTP or HTTPS transport, you must ensure that the transport is enabled.

The following procedure shows how to enable the HTTP transport.

**To enable the HTTP transport**

1.  Open the HpcWcfBroker.exe.config file located in the "Microsoft Hpc Pack\\Bin\\" folder.
2.  In the **brokerServiceAddresses** section, ensure that the following **add** element is removed from comments.

    `<add baseAddress="http://localhost/Broker"/>`

3.  Use the following command to reserve the HTTP URI for the users who are going to create the session.

    `netsh http add urlacl`

4.  Open the port in the firewall.

When you create the session, you must set the [SessionStartInfo.Secure](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.secure.aspx) property to false.

The following procedure shows how to enable the HTTPS transport.

**To enable the HTTPS transport**

1.  Open the HpcWcfBroker.exe.config file located in the "Microsoft Hpc Pack\\Bin\\" folder.
2.  In the **brokerServiceAddresses** section, uncomment the following **add** element.

    `<add baseAddress="https://localhost/Broker"/>`

    Update the URI as shown if the URI does not include the port number.

    `<add baseAddress="https://localhost:8080/Broker"/>`

3.  Use the following command to reserve the HTTP URI for the users who are going to create the session.

    `netsh http add urlacl`

4.  Open the port in the firewall.
5.  Use the following command to register the certificate with the HTTP listener.

    `netsh http add sslcert`

 

 



