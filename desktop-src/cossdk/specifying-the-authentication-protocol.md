---
description: Specifying the Authentication Protocol
ms.assetid: 2f469332-6b3e-475a-9ec6-782e1e445672
title: Specifying the Authentication Protocol
ms.topic: article
ms.date: 05/31/2018
---

# Specifying the Authentication Protocol

Depending on the security requirements at your site, you can require the queued components service always to verify a client's identity, never to verify a client's identity, or to verify a client's identity only if the component is configured to require authentication even when not accessed through a queue.

> [!Note]  
> In order to use a queued component in workgroup mode, the authentication level must be set to none.

 

## Component Services Administrative Tool

To specify the authentication protocol, use the following steps:

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the **COM+ Applications** folder associated with the computer you wish to manage.

2.  Right-click the queued application for which you want to specify the authentication protocol, and then click **Properties**.

3.  Select the **Queuing** tab in the properties dialog.

4.  Under **MSMQ Message Authentication**, select the radio button associated with the authentication protocol you want to implement.

5.  Click **OK**.

## Visual Basic

Use the *AuthLevel* parameter when activating the queued application as described in the [Using the Queue Moniker](using-the-queue-moniker.md).

## C/C++

Use the *AuthLevel* parameter when activating the queued application as described in the [Using the Queue Moniker](using-the-queue-moniker.md).

## Related topics

<dl> <dt>

[Queued Components Security](queued-components-security.md)
</dt> <dt>

[Security Limitations in Workgroup Mode](security-limitations-in-workgroup-mode.md)
</dt> </dl>

 

 



