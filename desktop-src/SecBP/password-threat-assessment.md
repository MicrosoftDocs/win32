---
description: Before implementing code that protects passwords, analyze your environment for attack vectors including modern credential theft techniques such as phishing, credential stuffing, and pass-the-hash.
ms.assetid: 4ebf7185-0179-4754-80da-63b0002c883f
title: Password Threat Assessment
ms.topic: reference
ms.date: 07/16/2026
---

# Password Threat Assessment

Before implementing code that protects passwords, it is best to analyze your particular environment for ways that an attacker might try to penetrate software defenses.

Start by analyzing your network or system architecture. Here are some examples:

-   The number of passwords that must be protected. Is a password required to log on to the local computer? Is the same password used to log on to the network? Are passwords propagated to more than one server on the network? How many passwords must be accommodated?
-   The kind of network (if any) that will be used. Is the network implemented using a corporate directory system (such as LDAP), and is its password architecture used? Are any objects storing unencrypted passwords?
-   Open versus closed network. Is the network self-contained or is it open to the outside? If so, is it protected by a firewall?
-   Remote access. Will users need to access the network from a remote location?

After you have analyzed your system or network architecture, then you can start to analyze how an attacker might try to attack it. Here are some possibilities:

-   Read an unencrypted password from a computer's registry.
-   Read an unencrypted password that is hard-coded in the software.
-   Read an unencrypted password from a computer's swapped-out code page.
-   Read a password from a program's event log.
-   Read a password from an extended Microsoft Active Directory directory service schema that has objects that contain a plaintext password.
-   Run a debugger on a program that requires a password.
-   Guess a password. Any of several techniques might be used. For example, the attacker might know some personal information about a user and try to guess a password from that information (for example, the name of a spouse/partner or child). Or, a brute-force method might be tried, where all combinations of letters, numbers, and punctuation are tried (only feasible where short passwords are used).

## Modern attack vectors

In addition to the classic threats above, modern attackers use increasingly sophisticated techniques:

- **Credential stuffing.** Attackers use leaked credentials from data breaches on other services, exploiting password reuse. Assume that your users' passwords may already be in public breach databases.
- **Pass-the-hash (PtH).** An attacker who obtains a password hash can authenticate to services that accept NTLM without cracking the password itself. Mitigate by disabling NTLM where possible and enabling Credential Guard.
- **Token theft and replay.** Attackers steal authentication tokens (OAuth tokens, Kerberos tickets, session cookies) from memory or disk, then replay them to impersonate the user without needing the password.
- **Phishing and adversary-in-the-middle (AitM).** Phishing kits can intercept multi-factor authentication codes in real-time. Phishing-resistant authentication (FIDO2, certificate-based) is the strongest countermeasure.
- **Supply chain attacks on credential stores.** Attackers target package managers, development tools, or CI/CD pipelines to inject code that exfiltrates secrets at build time or runtime.
- **Memory scraping.** Malware running in the same session can read process memory to extract plaintext credentials. Clear secrets using [**SecureZeroMemory**](/windows/win32/api/winbase/nf-winbase-securezeromemory) and minimize the time credentials are held in memory.

> [!IMPORTANT]
> When assessing your password threat model, assume that attackers have automated tools and may already possess credentials from other breaches. Defense-in-depth (combining strong authentication, credential isolation, and detection) is essential.

Comparing the possible attack methodologies with system or network architecture will likely reveal security risks. At that point, a risk factor can be established for each risk, and the risk factors can be used to triage fixes.
