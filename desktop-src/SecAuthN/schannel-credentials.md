---
Description: Schannel protocols require credentials to authenticate servers and optionally, clients.
ms.assetid: 8f912af8-fd64-467a-b154-28c60cb14929
title: Schannel Credentials
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Schannel Credentials

Schannel protocols require credentials to authenticate servers and optionally, clients. Server authentication, where the server provides proof of its identity to the client, is required by the Schannel [*security protocols*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50). Client authentication may be requested by the server at any time.

Schannel credentials are [*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) certificates. [*Public*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) and [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) information from certificates is used to authenticate the server and optionally, the client. These keys are also used to provide message [*integrity*](https://msdn.microsoft.com/af511aed-88f5-4b12-ad44-317925297f70) while client and server exchange the information required to generate and exchange [*session keys*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50).

For programming information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

 

 



