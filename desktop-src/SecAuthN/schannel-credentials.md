---
Description: Schannel protocols require credentials to authenticate servers and optionally, clients.
ms.assetid: '8295b1bd-6ae1-4f7e-926d-a9da7ec6a524'
title: Schannel Credentials
ms.topic: article
ms.date: 05/31/2018
---

# Schannel Credentials

Schannel protocols require credentials to authenticate servers and optionally, clients. Server authentication, where the server provides proof of its identity to the client, is required by the Schannel [*security protocols*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). Client authentication may be requested by the server at any time.

Schannel credentials are [*X.509*](https://msdn.microsoft.com/en-us/library/ms721636(v=VS.85).aspx) certificates. [*Public*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) and [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) information from certificates is used to authenticate the server and optionally, the client. These keys are also used to provide message [*integrity*](https://msdn.microsoft.com/en-us/library/ms721588(v=VS.85).aspx) while client and server exchange the information required to generate and exchange [*session keys*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx).

For programming information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

 

 



