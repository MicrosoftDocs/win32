---
description: Contains definitions of security terms that begin with the letter I.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: af511aed-88f5-4b12-ad44-317925297f70
title: I (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# I (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) I J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_iis_gly"></span><span id="_SECURITY_IIS_GLY"></span>**IIS**
</dt> <dd>

Software services that support website creation, configuration, and management, along with other Internet functions. Internet Information Services include Network News Transfer Protocol (NNTP), File Transfer Protocol (FTP), and Simple Mail Transfer Protocol (SMTP). IIS incorporates various functions for security, allows for CGI applications, and provides for Gopher and FTP servers.

</dd> <dt>

<span id="_security_impersonation_gly"></span><span id="_SECURITY_IMPERSONATION_GLY"></span>**impersonation**
</dt> <dd>

A mechanism that allows a server process to run by using the security credentials of the client or some other user using the credentials. When the server is impersonating the client, any operations performed by the server are performed by using the client's (impersonating user's) credentials. Impersonation does not allow the server to access remote resources on behalf of the client. This requires delegation.

</dd> <dt>

<span id="_security_impersonation_token_gly"></span><span id="_SECURITY_IMPERSONATION_TOKEN_GLY"></span>**impersonation token**
</dt> <dd>

An access token that has been created to capture the security information of a client process, allowing a server to "impersonate" the client process in security operations.

See also [*access token*](a-gly.md) and [*primary token*](p-gly.md).

</dd> <dt>

<span id="_security_initialization_vector_gly"></span><span id="_SECURITY_INITIALIZATION_VECTOR_GLY"></span>**initialization vector**
</dt> <dd>

(IV) A sequence of random bytes appended to the front of the plaintext before encryption by a block cipher. Adding the initialization vector to the beginning of the plaintext eliminates the possibility of having the initial ciphertext block the same for any two messages. For example, if messages always start with a common header (a letterhead or "From" line) their initial ciphertext would always be the same, assuming that the same cryptographic algorithm and symmetric key was used. Adding a random initialization vector eliminates this from happening.

</dd> <dt>

<span id="_security_inner_data_gly"></span><span id="_SECURITY_INNER_DATA_GLY"></span>**inner data**
</dt> <dd>

Any encoded data used as the message for another encoded message. For example, an enveloped message and its hash value may be the inner data for a second message.

</dd> <dt>

<span id="_security_inner_content_gly"></span><span id="_SECURITY_INNER_CONTENT_GLY"></span>**inner content**
</dt> <dd>

Data that is enhanced, such as with a digital signature. This term is used primarily when discussing enhanced data in a PKCS \#7 message.

</dd> <dt>

<span id="_security_integrity_gly"></span><span id="_SECURITY_INTEGRITY_GLY"></span>**integrity**
</dt> <dd>

The completeness and accuracy of a message after it has been sent or stored.

</dd> <dt>

<span id="_security_integrity_sid_gly"></span><span id="_SECURITY_INTEGRITY_SID_GLY"></span>**integrity SID**
</dt> <dd>

A [*security identifier*](s-gly.md) (SID) that represents an integrity level. An integrity SID in the [*system access control list*](s-gly.md) (SACL) of an object's security descriptor specifies the integrity level of the object. Integrity SIDs in an access token specify the integrity level of the token.

</dd> <dt>

<span id="_security_interrupt_request_level_gly"></span><span id="_SECURITY_INTERRUPT_REQUEST_LEVEL_GLY"></span>**IRQL**
</dt> <dd>

An interrupt request level (IRQL) defines the hardware priority at which a processor operates at any given time. In the Windows Driver Model, a thread running at a low IRQL can be interrupted to run code at a higher IRQL.

</dd> <dt>

<span id="_security_iv_gly"></span><span id="_SECURITY_IV_GLY"></span>**IV**
</dt> <dd>

See *initialization vector*.

</dd> </dl>

 

 



