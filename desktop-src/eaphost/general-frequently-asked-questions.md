---
title: General Frequently Asked Questions
description: "Read answers to commonly-asked questions about the EAPHost APIs, such as 'What is the lifetime of an authentication?'."
ms.assetid: 4025e8da-8cb1-477b-86bb-7756d9636224
ms.topic: article
ms.date: 05/31/2018
---

# General Frequently Asked Questions

The following topic provides answers to commonly-asked questions about the EAPHost APIs.

### General Frequently Asked Questions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Question</th>
<th>Answer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>What is a supplicant?</td>
<td>The supplicant is the entity to be authenticated using EAPHost. Typical supplicants are [802.1X](/previous-versions/windows/embedded/ms890287(v=msdn.10)) clients, 802.3 clients, and Routing and Remote Access Service (RRAS), Point-to-Point (PPP) clients.</td>
</tr>
<tr class="even">
<td>What is a peer?</td>
<td>The peer is the client side of an EAP authentication.</td>
</tr>
<tr class="odd">
<td>How does a peer differ from a supplicant?</td>
<td>The supplicant transports packets, whereas a peer does not. Nonetheless, the terms peer, supplicant and client are largely synonymous.</td>
</tr>
<tr class="even">
<td>What is an authenticator?</td>
<td>The authenticator is the wireless access point, network access server (NAS), or network access device (NAD) that authenticates the supplicant. The authenticator is also known as the EAP server.</td>
</tr>
<tr class="odd">
<td>What is the lifetime of an authentication?</td>
<td>The lifetime of a single authentication session on the client side is everything that occurs between the [<strong>EapHostPeerBeginSession</strong>](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession) and [<strong>EapHostPeerEndSession</strong>](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerendsession) functions being called. The lifetime on the authenticator side is everything that occurs between the [<strong>EapPeerBeginSession</strong>](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerbeginsession) and [<strong>EapPeerEndSession</strong>](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeerendsession) functions.</td>
</tr>
<tr class="even">
<td>What is a BLOB? Why would I convert a configuration (binary) BLOB to XML?</td>
<td>A BLOB is a binary large object. XML has several advantages over a binary configuration BLOB. Configuration data that is stored in XML is human-readable, human-editable, and cross-platform.</td>
</tr>
<tr class="odd">
<td>When do I convert a stored XML BLOB back to a binary BLOB?</td>
<td>It's possible to store a binary BLOB or XML BLOB, but you must always convert the XML BLOB back to a binary BLOB before use with run-time APIs; the run-time APIs cannot accept an XML directory.</td>
</tr>
<tr class="even">
<td>What are native methods?</td>
<td>Native EAP methods use the new EAPHost API.</td>
</tr>
<tr class="odd">
<td>What are legacy methods?</td>
<td>Legacy EAP methods are defined in the [Extensible Authentication Protocol Reference](/previous-versions/windows/desktop/eap/extensible-authentication-protocol-reference). The legacy EAP methods are available for use in Windows Vista and Windows Server 2008. These methods may not be available for use in subsequent versions of the operating system.</td>
</tr>
<tr class="even">
<td>What's the difference between legacy and native methods?</td>
<td>The native APIs are simpler and have fewer features. All new EAP methods should be written using the EAPHost API.</td>
</tr>
<tr class="odd">
<td>What is &quot;group policy&quot;?</td>
<td>For a description of group policy, see [Group Policy Collection](/previous-versions/windows/it-pro/windows-server-2003/cc779838(v=ws.10)).</td>
</tr>
<tr class="even">
<td>Can EAPHost functions override configuration policy specified by group policy?</td>
<td>No, never. If group policy is in use, group policy settings will always override EAPHost configuration settings.</td>
</tr>
<tr class="odd">
<td>What is Single-Sign-On (SSO)?</td>
<td>[802.1X](/previous-versions/windows/embedded/ms890287(v=msdn.10)) is a layer 2 authentication mechanism. Depending on the SSO configuration, SSO enables users to authenticate to the network using [802.1X](/previous-versions/windows/embedded/ms890287(v=msdn.10)) authentication before or immediately after logging on to Windows. SSO can be configured to use Windows credentials for network authentication (in which case users enter their credentials only once) or use different credentials for Windows and network authentication. For more information, see [SSO and PLAP](understanding-sso-and-plap.md).<br/></td>
</tr>
<tr class="even">
<td>What is Pre-Logon Access Provider (PLAP)</td>
<td>For more information, see [SSO and PLAP](understanding-sso-and-plap.md).</td>
</tr>
<tr class="odd">
<td>What is Protected Extensible Authentication Protocol (PEAP)?</td>
<td>For more information, see [PEAP](/previous-versions/windows/it-pro/windows-server-2003/cc757996(v=ws.10)) and [About Extensible Authentication Protocol](/previous-versions/windows/desktop/eap/about-extensible-authentication-protocol).</td>
</tr>
<tr class="even">
<td>How does PEAP deal with session resumption and re-authentication?</td>
<td>Session resumption and re-authentication typically occurs while roaming on a wireless network. Windows Data Protection API (DPAPI) provides a way to protect and bind data to a user and optionally the logon session. The caller gives [<strong>CryptProtectMemory</strong>](/windows/desktop/api/dpapi/nf-dpapi-cryptprotectmemory) an unencrypted buffer and DPAPI will encrypt the memory in place. Later, the caller can pass in the encrypted buffer to [<strong>CryptUnprotectMemory</strong>](/windows/desktop/api/dpapi/nf-dpapi-cryptunprotectmemory) and DPAPI will decrypt the memory, once again in place. For more information, see [TLS Inner Application Extension (TSL/IA)](https://go.microsoft.com/fwlink/p/?linkid=84011) and [PEAP](/previous-versions/windows/it-pro/windows-server-2003/cc757996(v=ws.10)).<br/></td>
</tr>
<tr class="odd">
<td>What is EAP-Transport Level Security (EAP-TLS)?</td>
<td>EAP-TLS is a client-server protocol in which distinct certificate profiles are typically used for the client and server.For more information, see [IETF RTC 2716](/previous-versions/windows/embedded/ms885336(v=msdn.10)).<br/></td>
</tr>
<tr class="even">
<td>How do I implement a password change using the Local Security Authority (LSA) API?</td>
<td>Use the [<strong>LsaCallAuthenticationPackage</strong>](/windows/desktop/api/ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) function to implement a password change.</td>
</tr>
<tr class="odd">
<td>Why would I want to enable tracing in EAPHost?</td>
<td>The trace logs contain debugging information (available in English only) that may assist Microsoft developers and partners in finding the root causes of any issues being experienced with the authentication process. For more information, see [Enabling Tracing](enabling-tracing.md).<br/></td>
</tr>
<tr class="even">
<td>Why do I encounter the error code, NTE_BAD_KEY_STATE (0x8009000BL) when I use the [Cryptography](/windows/desktop/SecCrypto/cryptography-portal) API to sign into the EAP-TLS exchange?</td>
<td>In Winerror.h NTE_BAD_KEY_STATE (0x8009000BL) is defined as a &quot;key not valid for use in specified state&quot;. This error is typically returned in the following scenarios.
<ul>
<li>When attempting to export a non-exportable private key BLOB</li>
<li>When unsuccessfully attempting to generate a pseudo-random function (PRF) hash handle using [<strong>CryptCreateHash</strong>](/windows/desktop/api/wincrypt/nf-wincrypt-cryptcreatehash)</li>
</ul>
For more information, see [Finish Messages in the TLS 1.0 Protocol](/windows/desktop/SecCrypto/finish-messages-in-the-tls-1-0-protocol).</td>
</tr>
<tr class="odd">
<td>What is a pseudo-random function (PRF)?</td>
<td>A function that takes a key, label, and seed as input, then produces an output of arbitrary length. For more information, see [Finish Messages in the TLS 1.0 Protocol](/windows/desktop/SecCrypto/finish-messages-in-the-tls-1-0-protocol).<br/></td>
</tr>
<tr class="even">
<td>How does EAPHost bind to network adapters?</td>
<td>EAPHost allows multiple supplicants to operate simultaneously, and each supplicant can bind to multiple network adapters. EAPHost supplicants provide binding to the network layers and drive the authentication process. Supplicants contain authentication configuration. Supplicants also save the state and provide subsequent connection security. Because EAPHost doesn't directly bind to any network mechanism, supplicant extensibility is possible.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[EAPHost Supplicant FAQs](eaphost-supplicant-frequently-asked-questions.md)
</dt> <dt>

[EAPHost Method FAQs](eap-method-frequently-asked-questions.md)
</dt> <dt>

[EAPHost Development FAQs](eaphost-development-frequently-asked-questions.md)
</dt> </dl>

