---
description: A security context is the set of security attributes and rules in effect during a communication session.
ms.assetid: 6c87448b-5b8d-4694-ac3f-be83a258fbb0
title: SSPI Context Semantics
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Context Semantics

A [*security context*](../secgloss/s-gly.md) is the set of security attributes and rules in effect during a communication session. This includes such information as the identities of the principal and information on the keys, ciphers, and algorithms being used. For [*Security Support Provider Interface*](../secgloss/s-gly.md) (SSPI), a security context is an opaque structure that is created through an exchange involving the [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function and the [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) function.

For more information about the context attributes, see [Context Requirements](context-requirements.md).

The SSPI model supports three types of security contexts.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="connection-oriented-contexts.md">Connection</a></td>
<td>A connection-oriented <a href="/windows/desktop/SecGloss/c-gly"><em>context</em></a> is the most common security context, and the simplest to use. The caller is responsible for the overall message format and for the location of the data in the message. The caller is also responsible for the location of the security-relevant fields within a message, such as the location of the signature data.<br/></td>
</tr>
<tr class="even">
<td><a href="datagram-contexts.md">Datagram</a></td>
<td>A <a href="/windows/desktop/SecGloss/d-gly"><em>datagram</em></a>-oriented context has extra support for DCE-style datagram communication. It can also be used generically for a datagram-oriented transport application.<br/>
<blockquote>
<p>[!Important]</p>
<p>The <a href="microsoft-kerberos.md">Microsoft Kerberos</a> package does not support datagram contexts in user-to-user mode.<br/></p>
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="stream-contexts.md">Stream</a></td>
<td>A stream-oriented context is responsible for the blocking and message formatting within the security package. The caller is not interested in formatting, but rather a raw stream of data.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Context Requirements](context-requirements.md)
</dt> <dt>

[Connection-Oriented Contexts](connection-oriented-contexts.md)
</dt> <dt>

[Datagram Contexts](datagram-contexts.md)
</dt> <dt>

[Stream Contexts](stream-contexts.md)
</dt> </dl>

 

 
