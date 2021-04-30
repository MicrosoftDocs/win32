---
title: Authentication (BITS)
description: BITS supports Basic authentication, Passport authentication, and several challenge/response authentication schemes.
ms.assetid: cfd4aec3-79d0-4971-93f8-df797e5c0f75
ms.topic: article
ms.date: 10/09/2018
---

# Authentication (BITS)

BITS supports Basic authentication, Passport authentication, and several challenge/response authentication schemes. If the server or proxy requires user authentication, use the [**IBackgroundCopyJob2::SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) function to specify the user's credentials. BITS uses the [CryptoAPI](/windows/desktop/SecCrypto/cryptography-portal) to protect the credentials.

To set credentials for Basic authentication use the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) function to specify the user name and password. You should only use Basic authentication with https:// protected secure websites; otherwise the username and password will be visible to users. 

It's possible to embed the user name and password in the URL. This is not considered a good security practice, and is deprecated in RFC 3986 (section 3.2.1).

For [Passport](/windows/desktop/WinHttp/passport-authentication-in-winhttp) authentication, BITS supports explicit credentials only, not implicit credentials tied to the account.

For challenge/response authentication, BITS impersonates the user and uses [Snego](../com/snego.md) to determine which challenge/response authentication to use, such as NTLM or the Kerberos protocol. For a list of challenge/response schemes that BITS supports, see [**BG\_AUTH\_SCHEME**](/windows/desktop/api/Bits1_5/ne-bits1_5-bg_auth_scheme).

BITS jobs can fail if the virtual directory on the server has anonymous authentication and another authentication scheme enabled and if ACLs protect the virtual directory or download files. For example, a job fails with "access denied" if the virtual directory has anonymous and integrated authentication enabled and the file contains an ACL that allows only Ben to read the file. This occurs because the virtual directory allows anonymous access, so IIS does not explicitly authenticate Ben (Ben's credentials are not used to access the file and access is denied).

## Using implicit credentials

To use the user's implicit (logon) credentials for NTLM or Kerberos authentication, call the [**IBackgroundCopyJob2::SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method and set the **UserName** and **Password** members of the [**BG\_BASIC\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-bg_basic_credentials) structure to **NULL**. If you specify implicit credentials for a proxy, BITS will also use the implicit credentials for server authentication unless you specify explicit server credentials.

For additional information for services, see [Service Accounts and BITS](service-accounts-and-bits.md).

You could also change the **LMCompatibilityLevel** or **UseLMCompat** registry value; however, you should change these values only if you have an existing application that cannot be changed to call the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method.

BITS will use implicit credentials for authentication if the **LMCompatibilityLevel** registry value is two or greater, and you have not called the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method. The full path to the **LMCompatibilityLevel** registry value is **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**LSA**\\**LmCompatibilityLevel**.

Note that changing the **LMCompatibilityLevel** registry value can affect other applications and services running on the computer. For more information about using the **LMCompatibilityLevel** registry value, see [KB147706](https://support.microsoft.com/kb/147706).

If setting the **LMCompatibilityLevel** registry value is an issue, you can create the **UseLMCompat** registry value under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**BITS**. The registry value is a DWORD. The following table lists the possible values for **UseLMCompat**:

|Value|Description|
|-|-|
| 0     | BITS will send implicit credentials whenever the server prompts for NTLM or Kerberos credentials.                                                                                           |
| 1     | BITS will send implicit credentials only if the client computer's **LMCompatibilityLevel** registry value is greater than or equal to 2.<br/>     |
| 2     | BITS will send implicit credentials only if the application called the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method.<br/> |

BITS will use a default value of "2" for the **UseLMCompat** registry value if the registry value does not exist.

## Using certificates for client/server authentication

In secure client/server communication, clients and servers can use digital certificates to mutually authenticate each other. BITS automatically supports certificate-based server authentication for secure HTTP transports. To provide BITS the client certificate needed for mutual authentication, call either the [**IBackgroundCopyJobHttpOptions::SetClientCertificateByID**](/windows/desktop/api/Bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setclientcertificatebyid) or [**IBackgroundCopyJobHttpOptions::SetClientCertificateByName**](/windows/desktop/api/Bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setclientcertificatebyname) method.

When a website accepts but does not require an SSL client certificate, and the BITS job does not specify a client certificate, the job will fail with **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED** (0x80072f0c).

## How to handle authenticated proxy scenarios that require user-specific settings

If you are using BITS in an environment that requires proxy authentication while running as an account without usable NTLM or Kerberos credentials in the machine's network domain, you must take extra steps to authenticate properly by using the credentials of another user account that does have credentials on the domain. This is a typical scenario when your BITS code is running as a system service such as LocalService, NetworkService, or LocalSystem, as those accounts do not have usable NTLM or Kerberos credentials.

The proxy detection logic used in BITS does the following when a network helper token (BG\_TOKEN\_NETWORK) is set:

-   If [**IBackgroundCopyJob::SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) was called with **BG\_JOB\_PROXY\_USAGE\_PRECONFIG**, then read local IE proxy settings using job owner token context impersonation via [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser). Starting in Windows 10, version 1809 (10.0; Build 17763), the helper token identity is used for this step.
-   If [**IBackgroundCopyJob::SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) was called with **BG\_PROXY\_USAGE\_AUTODETECT** or if the IE settings from the **BG\_JOB\_PROXY\_USAGE\_PRECONFIG** case specify auto-detect or an auto-config URL, then conduct auto-proxy detection, or Web Proxy Autodiscovery Protocol (WPAD), using helper token impersonation via [**WinHttpGetProxyForUrl**](/windows/desktop/api/winhttp/nf-winhttp-winhttpgetproxyforurl).

After that, helper token impersonation is used for proxy or server authentication throughout.

Starting in Windows 10, version 1809 (10.0; Build 17763), the authenticated proxy scenario with user-specific credentials is simplified.

1.  Call the BITS job's [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method with **BG\_AUTH\_SCHEME\_NEGOTIATE**, *UserName* set to **NULL**, *Password* set to **NULL**, and *Target* set to **BG\_AUTH\_TARGET\_PROXY**. This causes the user account's implicit credentials to be used for NTLM and Kerberos authentication with the proxy and server.
2.  Call [**IBackgroundCopyJob::SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) with **BG\_JOB\_PROXY\_USAGE\_PRECONFIG**.
3.  QueryInterface for [**IBitsTokenOptions**](/windows/desktop/api/Bits4_0/nn-bits4_0-ibitstokenoptions).
4.  Impersonate the user account you're using for NTLM/Kerberos credentials.
5.  Call [**SetHelperToken**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertoken).
6. Call [**SetHelperTokenFlags**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertokenflags) with **BG\_TOKEN\_NETWORK**.
7. Revert impersonation.
8. Continue job setup.
9. Call [**Resume**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume) on the job.

Before Windows 10, version 1809 (10.0; Build 17763), the correct user identity (the helper token's identity) is used for network-based proxy detection (WPAD) and for proxy authentication, but the actual detection of local (IE) proxy settings is always done using the job owner's token, even when a helper token is configured. To work around this shortcoming, you can follow these steps.

1.  Impersonate the user account you're using for NTLM/Kerberos credentials.
2.  Retrieve the user account's IE proxy settings by calling [**WinHttpGetIEProxyConfigForCurrentUser**](/windows/desktop/api/winhttp/nf-winhttp-winhttpgetieproxyconfigforcurrentuser).
3.  Revert impersonation.
4.  Call the BITS job's [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method with **BG\_AUTH\_SCHEME\_NEGOTIATE**, *UserName* set to **NULL**, *Password* set to **NULL**, and *Target* set to **BG\_AUTH\_TARGET\_PROXY**. This causes the user account's implicit credentials to be used for NTLM and Kerberos authentication with the proxy and server.
5.  If step 2 yielded any user-specific proxy settings (i.e. *lpszProxy* or *lpszProxyBypass* are not **NULL**), set the corresponding job settings manually, using [**SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) with the **BG\_JOB\_PROXY\_USAGE\_OVERRIDE** setting.
6.  If step 2 did not yield any user-specific proxy settings, call [**SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) with **BG\_JOB\_USAGE\_PRECONFIG**.
7.  QueryInterface for [**IBitsTokenOptions**](/windows/desktop/api/Bits4_0/nn-bits4_0-ibitstokenoptions).
8.  Impersonate the user account again.
9.  Call [**SetHelperToken**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertoken).
10. Call [**SetHelperTokenFlags**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertokenflags) with **BG\_TOKEN\_NETWORK**.
11. Revert impersonation.
12. Continue job setup.
13. Call [**Resume**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume) on the job.
