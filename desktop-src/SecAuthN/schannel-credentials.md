---
Description: 'Schannel protocols require credentials to authenticate servers and optionally, clients.'
ms.assetid: '8f912af8-fd64-467a-b154-28c60cb14929'
title: Schannel Credentials
---

# Schannel Credentials

Schannel protocols require credentials to authenticate servers and optionally, clients. Server authentication, where the server provides proof of its identity to the client, is required by the Schannel [*security protocols*](security.s_gly#-security-security-protocol-gly). Client authentication may be requested by the server at any time.

Schannel credentials are [*X.509*](security.x_gly#-security-x-509-gly) certificates. [*Public*](security.p_gly#-security-public-key-gly) and [*private key*](security.p_gly#-security-private-key-gly) information from certificates is used to authenticate the server and optionally, the client. These keys are also used to provide message [*integrity*](security.i_gly#-security-integrity-gly) while client and server exchange the information required to generate and exchange [*session keys*](security.s_gly#-security-session-key-gly).

For programming information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

 

 



