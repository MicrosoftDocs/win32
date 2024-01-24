---
title: Callbacks (RPC)
description: Often the programming model necessitates a server callback to a client through a remote procedure call (RPC), or client calls into an untrusted server. This introduces many potential pitfalls.
ms.assetid: a4f3ea26-ac4b-41e5-abde-96b4baedf2ae
ms.topic: article
ms.date: 05/31/2018
---

# Callbacks (RPC)

Often the programming model necessitates a server callback to a client through a remote procedure call (RPC), or client calls into an untrusted server. This introduces many potential pitfalls.

First, callback to the client must be made with a sufficiently low impersonation level. If the server is a highly privileged system service, calling back a local client with an impersonation level of impersonate or higher can provide the client with privileges sufficient to take over the system. Calling back a remote client with higher impersonation level than necessary can also lead to undesirable consequences.

Second, if an attacker induces your service to perform a callback, it can launch what is called a *black hole*—denial of service attack. Such attacks are not specific to RPC; in these attacks, a machine induces you to send traffic to it, but it does not respond to your requests. You sink more and more resources into calling the black hole, but they never come back. One generic example of such an attack is a TCP-level attack called a TCP/IP SYN flood attack.

On the RPC level, a simple black-hole attack occurs when an attacker calls an interface, and requests the server to call the interface back. The interface complies, but the attacker never returns the call: one thread on the server is tied up. The attacker does this 100 times, tying 100 threads on the server. Eventually the server runs out of memory. Debugging the server can potentially reveal the identity of the black-hole caller, but often the server will be restarted without suspecting foul play, or there may not be enough expertise available to determine the attacker.

The third pitfall is on the client. Often a client makes a call to the server informing the server how to call it back (usually a string binding), and then waits for a call from the server to arrive, blindly accepting any call on that endpoint that claims to come from the server. The callback protocol from the server to the client should include some verification mechanism to ensure that when the callback comes to the client, it actually originated on the server.

 

 




