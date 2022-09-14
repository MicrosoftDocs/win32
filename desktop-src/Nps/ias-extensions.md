---
title: Network Policy Server Extensions
description: The NPS Extensions API enables software developers to write extension DLLs that can be used for authentication, authorization, and accounting. NPS Extensions API supports the Remote Authentication Dial-In User Service (RADIUS) protocol.
ms.assetid: f459025f-fe5e-4ffa-a651-c70a4f8234ae
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Network Policy Server Extensions

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The NPS Extensions API enables software developers to write extension DLLs that can be used for authentication, authorization, and accounting. NPS Extensions API supports the Remote Authentication Dial-In User Service (RADIUS) protocol.

The extension DLLs implemented using the NPS Extensions API can provide enhanced session control and accounting. These DLLs can be used for scenarios such as controlling the number of end-user network sessions, using a state server, and connecting to domain authentication databases and Active Directory services. The extension DLLs can expand the remote access authorizations provided by NPS by adding their own authorizations when sending an Accept response back to an authenticating client.

NPS Extensions API is applicable in any computing environment where it would improve efficiency to authenticate dial-in users through a remote server. This technology is especially useful for Internet Service Providers (ISPs).

## In This Section

[Overview](/windows/desktop/Nps/ias-about-internet-authentication-service)

General information about RADIUS and the NPS Extensions API.

[Using](/windows/desktop/Nps/ias-using-internet-authentication-service)

Sample code that demonstrates how to use the NPS Extensions API.

[Reference](/windows/desktop/Nps/ias-internet-authentication-service-reference)

Documentation of enumerated types, functions, and structures that compose the NPS Extensions API.

## Related topics

<dl> <dt>

[Network Policy Server (Internet Authentication Service)](portal.md)
</dt> <dt>

[Extensible Authentication Protocol (EAP)](../eap/eap-start-page.md)
</dt> </dl>

 

 