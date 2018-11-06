---
title: Peripheral hardware guidelines
description: If their hardware device is not designed to work over a remote session, vendors must ensure that the device driver software forces disabling the redirection of the device by using a system policy or group policy.
ms.assetid: f033d469-a860-4968-b289-bc4eab23bd46
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Peripheral hardware guidelines

To a Remote Desktop Connection (RDC) client, the Remote Desktop Session Host (RD Session Host) server is the local computer. Consequently, devices such as disk drives and printers attached to the server appear as local devices to a client. In contrast, drives and printers attached to a client terminal can appear to be remote devices, depending on the options selected for the connection, the server used, and the version of the client software used.

While the initial release of Remote Desktop Services did not support applications that send output directly to serial, parallel, and sound ports attached to the client terminal, the current versions do allow these devices to appear as local devices to applications running in the Remote Desktop Services session.

If their hardware device is not designed to work over a remote session, vendors must ensure that the device driver software forces disabling the redirection of the device by using a system policy or group policy.

 

 




