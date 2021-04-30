---
description: The Security Service Provider Interface (SSPI) provides a universal, industry-standard interface for secure distributed applications.
ms.assetid: c3cebb9d-9094-493f-96d3-763a0c282dfb
title: Security Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Security Service Providers

The Security Service Provider Interface (SSPI) provides a universal, industry-standard interface for secure distributed applications. The Peer Graphing API provides a way for applications to secure links in a graph by specifying a Security Service Provider (SSP), which is a DLL that implements an SSPI interface. An application specifies an SSP when it creates a graph by using [**PeerGraphCreate**](/windows/desktop/api/P2P/nf-p2p-peergraphcreate).

For more information about creating your own SSP, see the SSPI documentation link in the list of [Graphing Reference Links](graphing-reference-links.md).

## Programming Considerations for Implementing an SSP

Use caution when calling into an application from within an SSP. The following considerations apply to SSP callbacks:

-   Callbacks should not take a long time to return, because they are called during connection negotiation. If it takes too long for a connection to be established, the connection can be dropped.
-   The Peer Graphing API dynamically adjusts connection timeout values, based on the actual load of a system. The lowest timeout value is 20 seconds.
-   To avoid potential deadlock situations, an application must not access the peer graphing database from a callback. If an application requires information from the graphing database, the application can cache the necessary information, and then refer to the cache from within the callback. Caching can also help decrease connection time.

When calling the SSPI entry points, the Peer Graphing Infrastructure requires specific values for specific parameters of five (5) functions. You cannot change these parameter values provided to SSP, and the SSP can either ignore the values for the five parameters or handle them gracefully. The following list identifies these specific parameters and required values:

-   [**AcquireCredentialsHandle**](graphing-reference-links.md)

    Specify one (1) for the *pvGetKeyArgument* parameter. Specifies **NULL** for the *pszPrincipal*, *pvLogonID*, and *pGetKeyFn* parameters.

-   [**InitializeSecurityContext**](graphing-reference-links.md)

    Specify the following flags for the *fContextReq* parameter: **ISC\_REQ\_MUTUAL\_AUTH \| ISC\_REQ\_CONFIDENTIALITY \| ISC\_REQ\_INTEGRITY \| ISC\_REQ\_SEQUENCE\_DETECT \| ISC\_REQ\_STREAM \| ISC\_REQ\_ALLOCATE\_MEMORY**.

-   [**AcceptSecurityContext**](graphing-reference-links.md)

    Specify the following flags for the *fContextReq* parameter: **ASC\_REQ\_MUTUAL\_AUTH \| ASC\_REQ\_CONFIDENTIALITY \| ASC\_REQ\_INTEGRITY \| ASC\_REQ\_SEQUENCE\_DETECT \| ASC\_REQ\_STREAM \| ASC\_REQ\_ALLOCATE\_MEMORY**.

-   [**EncryptMessage**](graphing-reference-links.md)

    Specify zero (0) for the *fQOP* and *MessageSeqNo* parameters.

-   [**DecryptMessage**](graphing-reference-links.md)

    Specify zero (0) for the *MessageSeqNo* parameter and **NULL** for the *pfQOP* parameter.

When calling [**EncryptMessage**](graphing-reference-links.md), four buffers are passed in the **SecBufferDesc** structure. The following table identifies the order to pass the buffers.

| SSP-specific structure         | Description                                                                                                                                                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SECBUFFER\_STREAM\_HEADER**  | Contains the security header data. The size of the header buffer is obtained by calling [**QueryContextAttributes**](graphing-reference-links.md) and specifying the **SECPKG\_ATTR\_STREAM\_SIZES** attribute.  |
| **SECBUFFER\_DATA**            | Contains the plain-text message to be encrypted.                                                                                                                                                                  |
| **SECBUFFER\_STREAM\_TRAILER** | Contains the security trailer data. The size of the header buffer is obtained by calling [**QueryContextAttributes**](graphing-reference-links.md) and specifying the **SECPKG\_ATTR\_STREAM\_SIZES** attribute. |
| **SECBUFFER\_EMPTY**           | Not initialized. The size of this buffer is zero (0).                                                                                                                                                             |



 

When calling [**DecryptMessage**](graphing-reference-links.md), the Peer Graphing API passes exactly four **SecBuffer** structures. The first buffer is **SECBUFFER\_DATA**, and contains an encrypted message. The remaining buffers are used for output, and are of type **SECBUFFER\_EMPTY**.

The SSP needs to support encrypting and decrypting user data buffers with sizes of 16K and greater in one call.

 

 



