---
description: Best practices for handling passwords and credentials securely in Windows applications, including storage, memory management, and modern alternatives.
ms.assetid: 1d810f71-9bf5-4c5c-a573-c35081f604cf
title: Handling Passwords
ms.topic: concept-article
ms.date: 07/16/2026
---

# Handling Passwords

User name and password credentials remain common for authentication, even as stronger methods like certificates, biometrics, and passkeys become more widespread. Encryption keys and other secrets also require protection. Software systems must handle these credentials securely to resist credential theft, replay attacks, and lateral movement by attackers.

> [!WARNING]
> Never hardcode passwords, API keys, connection strings, or other secrets in source code. Hardcoded secrets are trivially extracted by attackers using decompilers, memory inspection, or source-code leaks. This is one of the most common credential vulnerabilities exploited in the wild.

> [!IMPORTANT]
> When you have finished using passwords or secrets in memory, immediately overwrite the buffer by calling [**SecureZeroMemory**](/windows/win32/api/winbase/nf-winbase-securezeromemory). Unlike `memset`, the compiler cannot optimize away `SecureZeroMemory`, ensuring secrets are actually cleared.

## Modern credential management

For new development on Windows, use these approaches in preference order:

1. **Eliminate passwords where possible.** Use Windows Hello, passkeys (FIDO2/WebAuthn), or certificate-based authentication to avoid handling passwords altogether.
2. **Use the Windows Credential Manager.** Call [**CredWrite**](/windows/win32/api/wincred/nf-wincred-credwritea) and [**CredRead**](/windows/win32/api/wincred/nf-wincred-credreada) to store and retrieve credentials in the OS credential vault, which encrypts them with the user's logon session key.
3. **Use DPAPI for local secret storage.** Call [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) to encrypt secrets that must be persisted locally. DPAPI ties encryption to the user account or machine, providing defense-in-depth.
4. **For service credentials, use managed identities or key vaults.** Services running on Azure should use managed identities. On-premises services should retrieve secrets from a secure vault at runtime rather than storing them in configuration files.

## Password handling principles

When passwords must be handled in code:

- **Collect passwords as late as possible and discard them as early as possible.** Minimize the window during which the secret exists in memory.
- **Never log passwords or secrets.** Ensure diagnostic logging, event logs, and crash dumps do not contain credential material.
- **Never transmit passwords in plaintext.** Always use TLS/HTTPS or an equivalent encrypted channel.
- **Prompt securely.** Use [**CredUIPromptForWindowsCredentials**](/windows/win32/api/wincred/nf-wincred-creduipromptforwindowscredentialsa) to collect credentials through the standard Windows credential dialog, which enforces secure desktop isolation.

For more information about threats and mitigations:

-   [Password Threat Assessment](password-threat-assessment.md)
-   [Threat Mitigation Techniques](threat-mitigation-techniques.md)

 

 

 
