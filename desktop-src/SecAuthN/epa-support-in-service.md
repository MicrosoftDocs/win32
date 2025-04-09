---
description: EPA cryptographically binds the TLS session key to the session key of the authentication protocol, allowing TLS to provide the same client authentication as the authentication protocol’s key.
ms.assetid: 97c616aa-1a8a-45a5-9b31-8813dd679e48
title: Supporting Extended Protection for Authentication (EPA) in a service
ms.topic: how-to
ms.date: 07/14/2023
---

# Supporting Extended Protection for Authentication (EPA) in a service

| Feature | Applies to |
|--------|--------|
| EPA | all supported Windows OS |
| EPA Audit Mode | Windows Server 2019<br/>Windows Server 2022<br/>Windows Server 23H2 |

## What is the problem?

There’s a class of attacks on authenticated services called forwarding attacks. These attacks allow adversaries to bypass authentication and act as another user. Because these are attacks on the service and not the authentication protocol itself, it’s up to the authenticated service to thwart forwarding attacks.

## How do forwarding attacks work?

When a service or application calls the API [AcceptSecurityContext](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) to authenticate a client, it passes a blob of data received from the client’s call to [InitializeSecurityContext](/windows/win32/api/sspi/nf-sspi-initializesecuritycontextw). The authentication protocol is responsible for verifying that the provided blob originated from the indicated user. AcceptSecurityContext can make no assertions about the authenticity of the remainder of the application message which it did not see.  

A common security mistake in applications is treating the application traffic as authenticated after a successful authentication of the inner authentication protocol blob. This most commonly occurs with applications that use TLS for their wire protocol. TLS commonly does not use client certificates; it provides the server with integrity and confidentiality guarantees, but not authentication.  The inner authentication provides client authentication, but only for its blob.  It does not authenticate the TLS channel or the remainder of the application protocol contained therein.

An attacker executes a forwarding attack by inserting an authentication blob from one source with an attacker crafted request. For example, an attacker can observe authentication traffic on the network and insert this into its own request to the server. This allows the attacker to gain access to the server as the client from the captured authentication traffic.

The key concept here is that SSPI authentication messages are designed to be exposed on the wire; they are not expected to be kept secret.  This differs from many web-based authentication schemes that use bearer tokens that are always kept confidential inside TLS channels.

## What is the solution?

The preferred solution is to use the authentication protocol’s session key to sign or encrypt ([MakeSignature](/windows/win32/api/sspi/nf-sspi-makesignature), [EncryptMessage](/windows/win32/api/sspi/nf-sspi-encryptmessage)) other traffic. Because the session key is cryptographically derived during the authentication protocol exchange, its authenticated data, and any traffic protected by that key is guaranteed to come from the authenticated client.

This is not always an option. In some cases, the format of the application protocol message is fixed by standards designed for bearer tokens. In this case, Extended Protection for Authentication (EPA), also known as Channel Binding, can protect against forwarding over a TLS/SSL channel.  

## What is EPA?

EPA cryptographically binds the TLS session key to the session key of the authentication protocol, allowing TLS to provide the same client authentication as the authentication protocol’s key. See [Extended Protection for Authentication Overview](/dotnet/framework/wcf/feature-details/extended-protection-for-authentication-overview) for more information.

### Service Binding

The second part of EPA is called Service Binding.  Unlike Channel Binding, this does not provide the service with cryptographic guarantees and serves as a defense of last resort where channel binding is not possible.  This mechanism allows the server to call [QueryContextAttributes](querycontextattributes--general.md) to retrieve the attribute **SECPKG_ATTR_CLIENT_SPECIFIED_TARGET** which contains the name the authenticated client passed to **InitializeSecurityContext**.

For example, imagine a service residing behind a TLS terminating load balancer. It doesn’t have access to the TLS session key and can only determine from the channel binding that the client’s authentication was intended for a TLS protected service. The name supplied by the client should be the same name as it used to validate the TLS server certificate. By verifying that the client was authenticating to a name matching the server TLS certificate from the load balancer, the service gains high confidence that the authentication came from the same client as the TLS channel.

This article will not discuss how to support service binding. See [How to: Specify a Service Binding in Configuration](/dotnet/framework/wcf/how-to-specify-a-service-binding-in-configuration) for more information.

## How do you support EPA?

When enforcing EPA, services may notice clients failing to authenticate due to compatibility issues. Therefore, we have created an EPA audit mode where services can enable auditing, giving admins controls to observe how clients respond before enforcing EPA.

Microsoft services supporting audit mode include:  

- [LDAP](/windows/security/threat-protection/security-policy-settings/domain-controller-ldap-server-signing-requirements)

>[!NOTE]
>Below you will find optional steps to enable EPA audit functionality. Please note, enabling EPA audit functionality without enforcing EPA does not protect against relay attacks. We recommend that services who choose to first enable EPA in audit mode only, later take steps to remediate incompatible clients and eventually strictly enforce EPA to avoid any potential relay attacks.  

>[!NOTE]
>The channel bindings passed into [AcceptSecurityContext](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) do not need to be audit-only bindings to get the auditing results. Services can run audit mode while still enforcing EPA.  

### Client

1. Use [QueryContextAttributes](querycontextattributes--general.md)(TLS) to get channel bindings (fill in unique vs endpoint)
1. Call [InitializeSecurityContext](initializesecuritycontext--general.md), and pass channel bindings in [SECBUFFER_CHANNEL_BINDINGS](/windows/win32/api/sspi/ns-sspi-sec_channel_bindings)

### Server

1. Use [QueryContextAttributes](querycontextattributes--general.md)(TLS), as on the client
1. (Optionally) Makes into audit-only by calling [SspiSetChannelBindingFlags](sspi-sspisetchannelbindingflags.md)
1. (Optionally) Add channel binding result buffer to output buffers for ASC.
1. Specify the EPA level and other configurations by calling [AcceptSecurityContext](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) with [SECBUFFER_CHANNEL_BINDINGS](/windows/win32/api/sspi/ns-sspi-sec_channel_bindings)
1. (Optionally) Use flags to control behavior in corner cases:
    - **ASC_REQ_ALLOW_MISSING_BINDINGS** - Don't fail clients that said nothing at all, like old third-party devices. Enlightened clients that didn't get **SECBUFFER_CHANNEL_BINDINGS** will send an empty binding rather than nothing.
    - **ASC_REQ_PROXY_BINDINGS** - A rare case for TLS terminating load balancers. We don't have a **SECBUFFER_CHANNEL_BINDINGS** to pass, but still want to enforce that clients put request into a TLS channel. This is most useful with service bindings to ensure that the client was also putting into a TLS channel for which the server cert matched our name.

## How do you enforce EPA?

Once a service supports EPA, admins can control EPA state all the way from audit to full enforcement. This gives services the tools to evaluate their ecosystem’s readiness for EPA, remediate incompatible devices, and progressively enforce EPA to protect their environment.

The following attributes and values can be used to enforce various levels of EPA in your environment:

| Name | Description |
|--------|--------|
| None | No channel binding validation is performed. This is the behavior of all servers that have not been updated. |
| Allow | All clients that have been updated must provide channel binding information to the server. Clients that have not been updated do not have to do so. This is an intermediate option that allows for application compatibility. |
| Require | All clients must provide channel binding information. The server rejects authentication requests from clients that do not do so. |

These attributes can be coupled with audit functionality to gather information on device compatibility at various levels of EPA enforcement. You will pass your desired configuration into [SspiSetChannelBindingFlags](sspi-sspisetchannelbindingflags.md).

- **Audit** - Audit mode can be used in conjunction with any of the above EPA enforcement levels.

## How do you interpret EPA audit results?

Audit results are a set of bit flags:

| Flag | Description |
|--------|--------|
| SEC_CHANNEL_BINDINGS_RESULT_CLIENT_SUPPORT | The client indicated that it's capable of channel bindings. |
| SEC_CHANNEL_BINDINGS_RESULT_ABSENT | The client did not provide binding to an outer channel. |
| SEC_CHANNEL_BINDINGS_RESULT_NOTVALID_MISMATCH | The client bindings indicate a different channel than the server. |
| SEC_CHANNEL_BINDINGS_RESULT_NOTVALID_MISSING | Channel binding failed due to **SEC_CHANNEL_BINDINGS_RESULT_ABSENT**. |
| SEC_CHANNEL_BINDINGS_RESULT_VALID_MATCHED | The channels were successfully bound. |
| SEC_CHANNEL_BINDINGS_RESULT_VALID_PROXY | The client indicated binding to an outer channel, which passed due to **ASC_REQ_PROXY_BINDINGS**. |
| SEC_CHANNEL_BINDINGS_RESULT_VALID_MISSING | Channel binding passed due to **ASC_REQ_ALLOW_MISSING_BINDINGS**. |

There are also definitions for sets of bits:

| Flag | Description |
|--------|--------|
| SEC_CHANNEL_BINDINGS_RESULT_VALID | Used to test for all **SEC_CHANNEL_BINDINGS_VALID_**\* cases. |
| SEC_CHANNEL_BINDINGS_RESULT_NOTVALID | Used to test for all **SEC_CHANNEL_BINDINGS_NOTVALID_**\* cases. |

### Audit flow

Any OS that supports the results will always set at least one bit out of **SEC_CHANNEL_BINDINGS_RESULT_VALID** and **SEC_CHANNEL_BINDINGS_RESULT_NOTVALID**.

**Channel binding failed:** Test for any bits from **SEC_CHANNEL_BINDINGS_RESULT_NOTVALID**. For bindings that are not audit-only, this corresponds to ASC failing with **STATUS_BAD_BINDINGS** or **SEC_E_BAD_BINDINGS**.

- **SEC_CHANNEL_BINDINGS_RESULT_NOTVALID_MISMATCH:** The client and server both know about channel bindings but don't agree about the channel. This is the attack case or an improper security configuration that is indistinguishable from an attack because the configuration has compromised HTTPS to inspect traffic (e.g. Fiddler). It also could be the client and server disagreeing about unique versus endpoint bindings.
- **SEC_CHANNEL_BINDINGS_RESULT_NOTVALID_MISSING** splits into two cases:
  - With **SEC_CHANNEL_BINDINGS_RESULT_CLIENT_SUPPORT**, it means that the client attests that it knows about channel bindings and said there was no channel. This can be a forwarding attack from a non-TLS service, but it's likely to be an unenlightened application running on the client that's doing TLS but not telling the inner authentication about it.
  - Without **SEC_CHANNEL_BINDINGS_RESULT_CLIENT_SUPPORT**, it's a client that's not capable of channel bindings. All supported Windows versions are capable of channel binding, so this is either third-party or a system that's had the registry value SuppressExtendedProtection set. This is the case that's turned into **SEC_CHANNEL_BINDINGS_RESULT_VALID_MISSING** if you pass **ASC_REQ_ALLOW_MISSING_BINDINGS**.

**Channel binding succeeded:** This is the inverse of the check for failure, or test for **SEC_CHANNEL_BINDINGS_RESULT_VALID**.

- **SEC_CHANNEL_BINDINGS_RESULT_VALID_MATCHED** is the success case. The security protection is working (or would work if EPA is enabled as audit-only).
- **SEC_CHANNEL_BINDINGS_RESULT_VALID_MISSING** means that **ASC_REQ_ALLOW_MISSING_BINDINGS** was passed, so we allowed a client that did not claim support for channel binding. Clients that are hitting this case are not protected and should be investigated to see what's wrong. They either need to be updated to support channel binding, or the SuppressExtendedProtection registry value should be cleared once the broken applications are updated.
- **SEC_CHANNEL_BINDINGS_RESULT_VALID_PROXY** is a special case associated with the flag **ASC_REQ_PROXY_BINDINGS** that's used when TLS is terminated at a load balancer instead of reaching the server. It's not possible for the server to verify that the client is using the same TLS connection as is terminated at the load balancer. For auditing purposes, this is treated the same as **SEC_CHANNEL_BINDINGS_RESULT_VALID_MATCHED**.

## See also

[AcceptSecurityContext](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext)

[InitializeSecurityContext](/windows/win32/api/sspi/nf-sspi-initializesecuritycontextw)

[MakeSignature](/windows/win32/api/sspi/nf-sspi-makesignature)

[EncryptMessage](/windows/win32/api/sspi/nf-sspi-encryptmessage)

[QueryContextAttributes](querycontextattributes--general.md)

[Extended Protection for Authentication Overview](/dotnet/framework/wcf/feature-details/extended-protection-for-authentication-overview)

[How to: Specify a Service Binding in Configuration](/dotnet/framework/wcf/how-to-specify-a-service-binding-in-configuration)
