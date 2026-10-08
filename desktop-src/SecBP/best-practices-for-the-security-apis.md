---
description: Suggestions for application security assessments for app development of Windows security software and secure software development, including application security testing.
ms.assetid: bb0ddae2-f559-4785-97c7-182fc204fa60
title: Best Practices for the Security APIs
ms.topic: best-practice
ms.date: 07/14/2025
---

# Best Practices for the Security APIs

To help develop secure software, we recommend that you use the following best practices when developing applications. For more information, see [Microsoft Security Development Lifecycle](https://www.microsoft.com/securityengineering/sdl).

## Security Development Life Cycle

The [Security Development Life Cycle](/previous-versions/ms995349(v=msdn.10)) (SDL) is a process that aligns a series of security-focused activities and deliverables to each phase of software development. These activities and deliverables include:

-   Developing threat models
-   Using code-scanning tools
-   Conducting code reviews and security testing

For more information about the SDL, see the [Microsoft Security Development Lifecycle](https://www.microsoft.com/securityengineering/sdl).

## Threat Models

Conducting a threat model analysis can help you discover potential points of attack in your code. For more information about threat model analysis, see Howard, Michael and LeBlanc, David \[2003\], *Writing Secure Code*, 2d ed., ISBN 0-7356-1722-8, Microsoft Press, Redmond, Washington. (This resource may not be available in some languages and countries.)

## Service Packs and Security Updates

Build and test environments should mirror the same levels of service packs and security updates of the targeted user base. We recommend that you install the latest service packs and security updates for any Microsoft platform or application that is part of your build and test environment and encourage your users to do the same for the finished application environment. For more information about service packs and security updates, see [Update Windows](https://support.microsoft.com/windows/update-windows-3c5ae7fc-9fb6-9af1-1984-b5e0412c556a) and [Microsoft Security](https://www.microsoft.com/security).

## Authorization

You should create applications that require the least possible privilege. Using the least possible privilege reduces the risk of malicious code compromising your computer system. For more information about running code in least possible privilege level, see [Running with Special Privileges](running-with-special-privileges.md).

## Cryptographic Best Practices

When implementing cryptography in Windows applications:

- **Use [Cryptography API: Next Generation (CNG)](/windows/win32/seccng/cng-portal)** for all new development. CryptoAPI is maintained for backward compatibility only.
- **Design for crypto agility, and plan for post-quantum.** Don't scatter hardcoded algorithm identifiers or key sizes throughout your code — isolate them so algorithms can be swapped without a rewrite. The platform is moving to NIST post-quantum standards, ML-KEM (FIPS 203) for key establishment and ML-DSA (FIPS 204) for signatures, so favor agile designs now — especially for data with a long confidentiality lifetime, to resist "harvest-now, decrypt-later" attacks.
- **Prefer authenticated encryption (AEAD).** Use AES-GCM so that encryption also detects tampering. If you must use an unauthenticated mode such as CBC, pair it with a separate integrity check (encrypt-then-MAC) — confidentiality alone does not protect against modification.
- **Never reuse a nonce (IV) with the same key in AES-GCM.** Nonce reuse in GCM is catastrophic: it can expose the authentication key and enable message forgery. Generate a unique nonce for every encryption operation — for example, an incrementing counter or a fresh random 96-bit value.
- **Never use ECB block cipher mode.** ECB encrypts blocks independently, leaking patterns in plaintext data.
- **Never hardcode cryptographic keys** in source code. Use [DPAPI](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) for local key protection or the [CNG Key Storage Provider](/windows/win32/seccertenroll/cng-key-storage-providers) for persistent keys.
- **Clear secrets from memory when you are done with them.** Overwrite key material, passwords, and other sensitive buffers with [SecureZeroMemory](/windows/win32/api/winbase/nf-winbase-securezeromemory). Unlike `memset`, it is not optimized away by the compiler.
- **Use key lengths of 256 bits for AES**, 2048+ bits for RSA (3072+ preferred), and 256+ bits for ECDSA.
- **Use SHA-256 or stronger** for hashing. Do not use MD5 or SHA-1 for security purposes.
- **Always check return values** from cryptographic functions. A silently failed encryption call may leave data stored in plaintext.
- **Generate random numbers** using [BCryptGenRandom](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) (CNG) — not `rand()` or other non-cryptographic PRNGs. Pass `BCRYPT_USE_SYSTEM_PREFERRED_RNG` to use the system-preferred generator without managing an algorithm handle.


## More Information

For more information about best practices, see the following topics.



| Topic                                                                                                                        | Description                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Running with Special Privileges](running-with-special-privileges.md)<br/>                                            | Discusses security implications of privileges.<br/>                                                                                                                                  |
| [Avoiding Buffer Overruns](avoiding-buffer-overruns.md)<br/>                                                          | Provides information about avoiding buffer overruns.<br/>                                                                                                                            |
| [Control Flow Guard (CFG)](control-flow-guard.md)<br/>                                                                | Discusses memory corruption vulnerabilities.<br/>                                                                                                                                    |
| [Creating a DACL](creating-a-dacl.md)<br/>                                                                            | Shows how to create a discretionary access control list (DACL) by using the [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-definition-language) (SDDL).<br/> |
| [Handling Passwords](handling-passwords.md)<br/>                                                                      | Discusses security implications of using passwords.<br/>                                                                                                                             |
| [Dynamic Access Control developer extensibility](/previous-versions/windows/desktop/dacx/dynamic-access-control-developer-extensibility-roadmap)<br/> | Basic orientation to some of the developer extensibility points for the new Dynamic Access Control solutions.<br/>                                                                   |



 

 

