---
Description: 'To secure the session, set the SessionStartInfo.Secure property to True.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e6b3eb5c-ac38-4cfe-b126-98eeab2ca341'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Securing the HPC Session
---

# Securing the HPC Session

To secure the session, set the [SessionStartInfo.Secure](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.secure.aspx) property to **True**. The authentication that is used depends on the binding that you specified when you set the [SessionStartInfo.TransportScheme](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.transportscheme.aspx) property.

If you specify NetTcp:

-   The broker uses [NetTcpBinding](https://msdn.microsoft.com/library/system.servicemodel.nettcpbinding.aspx) with Transport security when establishing the endpoints.
-   The broker authenticates the clients using Windows integrated security (Kerberos or NTLM) and the messages are signed and encrypted.

If you specify Http:

-   The broker uses [BasicHttpBinding](https://msdn.microsoft.com/library/system.servicemodel.basichttpbinding.aspx) with TransportWithMessageCredential security when establishing the endpoints.
-   The broker uses SSL (HTTPS) to secure messages.
-   The broker authenticates the clients using the user name and password embedded in the message headers.

If the session is secure, the client, broker, and service must all run as the same user; you cannot set the [SessionStartInfo.UserName](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.username.aspx) property to a user that is different from what the client will run as.

If the credentials that you specify are from a different domain, the domain to which the cluster belongs must have a full-trust relationship with that domain. If not, you will receive a Kerberos validation error.

 

 



