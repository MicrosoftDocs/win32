---
description: The Transport Layer Security (TLS) Handshake Protocol is responsible for the authentication and key exchange necessary to establish or resume secure sessions.
ms.assetid: 65fb4db3-e505-457a-9159-dba0b506ea0b
title: TLS Handshake Protocol
ms.topic: article
ms.date: 05/31/2018
---

# TLS Handshake Protocol

The [*Transport Layer Security*](../secgloss/t-gly.md) (TLS) Handshake Protocol is responsible for the authentication and key exchange necessary to establish or resume secure sessions. When establishing a secure [*session*](../secgloss/s-gly.md), the Handshake Protocol manages the following:

-   Cipher suite negotiation
-   Authentication of the server and optionally, the client
-   Session key information exchange.

## Cipher Suite Negotiation

The client and server make contact and choose the cipher suite that will be used throughout their message exchange.

## Authentication

In TLS, a server proves its identity to the client. The client might also need to prove its identity to the server. PKI, the use of [*public/private key pairs*](../secgloss/p-gly.md), is the basis of this authentication. The exact method used for authentication is determined by the cipher suite negotiated.

## Key Exchange

The client and server exchange random numbers and a special number called the Pre-Master Secret. These numbers are combined with additional data permitting client and server to create their shared secret, called the Master Secret. The Master Secret is used by client and server to generate the write MAC secret, which is the session key used for [*hashing*](../secgloss/h-gly.md), and the write key, which is the [*session key*](../secgloss/s-gly.md) used for encryption.

## Establishing a Secure Session by Using TLS

The TLS Handshake Protocol involves the following steps:

1.  The client sends a "Client hello" message to the server, along with the client's random value and supported cipher suites.
2.  The server responds by sending a "Server hello" message to the client, along with the server's random value.
3.  The server sends its certificate to the client for authentication and may request a certificate from the client. The server sends the "Server hello done" message.
4.  If the server has requested a certificate from the client, the client sends it.
5.  The client creates a random Pre-Master Secret and encrypts it with the [*public key*](../secgloss/p-gly.md) from the server's certificate, sending the encrypted Pre-Master Secret to the server.
6.  The server receives the Pre-Master Secret. The server and client each generate the Master Secret and [*session keys*](../secgloss/s-gly.md) based on the Pre-Master Secret.
7.  The client sends "Change cipher spec" notification to server to indicate that the client will start using the new [*session keys*](../secgloss/s-gly.md) for [*hashing*](../secgloss/h-gly.md) and encrypting messages. Client also sends "Client finished" message.
8.  Server receives "Change cipher spec" and switches its record layer security state to [*symmetric encryption*](../secgloss/s-gly.md) using the [*session keys*](../secgloss/s-gly.md). Server sends "Server finished" message to the client.
9.  Client and server can now exchange application data over the secured channel they have established. All messages sent from client to server and from server to client are encrypted using session key.

## Resuming a Secure Session by Using TLS

1.  The client sends a "Client hello" message using the Session ID of the session to be resumed.
2.  The server checks its session cache for a matching Session ID. If a match is found, and the server is able to resume the session, it sends a "Server hello" message with the Session ID.
    > [!Note]  
    > If a session ID match is not found, the server generates a new session ID and the TLS client and server perform a full handshake.

     

3.  Client and server must exchange "Change cipher spec" messages and send "Client finished" and "Server finished" messages.
4.  Client and server can now resume application data exchange over the secure channel.

 

 
