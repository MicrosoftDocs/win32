---
description: Queued Components Security
ms.assetid: 3fbeb81a-e3e4-495b-b891-896877fab92f
title: Queued Components Security
ms.topic: article
ms.date: 05/31/2018
---

# Queued Components Security

When a client makes a method call to a queued object, the call is actually made to the recorder, which packages it as part of a message to the server. The listener reads the message from the queue and passes it to the player. The player invokes the actual server component and makes the same method call. The server component must observe the security call context of the client (not the player's security call context) when the player makes the method call. The recorder marshals the client's security call context into the message, and the player unmarshals it at the server before making the method call. As far as the server object is concerned, there is no difference in security context between a direct call from the client and an indirect call from the player. In particular, the methods invoked execute with the sender's privileges.

A COM+ queued component supports role-based security semantics just like other components built for use with COM+ applications. Components of a queued application can therefore use programmatic interfaces to discover the role membership of their caller ([**ISecurityCallContext::IsCallerInRole**](/windows/desktop/api/ComSvcs/nf-comsvcs-isecuritycallcontext-iscallerinrole)) or a specific user ([**ISecurityCallContext::IsUserInRole**](/windows/desktop/api/ComSvcs/nf-comsvcs-isecuritycallcontext-isuserinrole)). It is recommended that any queued component with a potential security impact use these interfaces to explicitly check the sender's credentials.

The caller identity is the identity associated with a method call. Caller identity is used by role-based security and is present in the security call context. In queued components, the caller identity is represented as data in the Message Queuing message. Message Queuing authenticates the message sender identity. When the caller identity and the message sender identity are the same, Message Queuing authenticates both the message and the caller. This is the usual case.

> [!Note]  
> COM+ queued components does not support impersonation-style security, which allows a server to obtain an access token corresponding to the client identity and use it either to perform access control checks or to act under the client security context.

 

When the caller of a queued component is interacting with the component through an out-of-process recorder, the identities of the caller and message sender (recorder) can be different. In this case, COM+ queued components verifies that the message sender is a member of the QC Trusted User role on the server. Additionally, the out-of-process recorder requires an authentication certificate because it is being authenticated by Message Queuing.

Members of the QC Trusted User role are allowed to specify an arbitrary identity, which means that a malicious member could execute a queued component call with elevated privileges. It is therefore recommended that the number of such users be kept to an absolute minimum.

Because of the risk of a sophisticated attack associated with any mechanism which propagates identity across a network, as well as the risk of a simple denial of service attack by flooding the queues with unexecutable requests, it is recommended that you deploy the COM+ queued components service only on a network of trusted hosts—for example, on a private network or a virtual private network, or behind an appropriately configured firewall.

COM+ queued components runs over DCOM, so you can help protect the integrity and secrecy of queued method calls by selecting **Packet Privacy** as the **Authentication Level of Calls** setting on the **Security** tab of your queued application's **Properties** sheet.

## Related topics

<dl> <dt>

[COM+ Security](com--security.md)
</dt> <dt>

[Security Limitations in Workgroup Mode](security-limitations-in-workgroup-mode.md)
</dt> <dt>

[Specifying the Authentication Protocol](specifying-the-authentication-protocol.md)
</dt> </dl>

 

 



