---
title: Authentication
description: BITS supports Basic authentication, Passport authentication, and several challenge/response authentication schemes.
ms.assetid: cfd4aec3-79d0-4971-93f8-df797e5c0f75
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Authentication

BITS supports Basic authentication, Passport authentication, and several challenge/response authentication schemes. If the server or proxy requires user authentication, use the [**IBackgroundCopyJob2::SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method to specify the user's credentials. BITS uses the [CryptoAPI](https://msdn.microsoft.com/library/windows/desktop/aa380255) to protect the credentials.

**BITS 1.2 and earlier:** The [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method is not available.

Basic authentication requires the user name and password to be embedded in the URL, for example, HTTP://username:password@server/path/file. Because the user name and password are clear text, an administrator can enumerate the jobs in the transfer queue and see the user name and password. The user name and password can also be seen by a network monitor program that is on the same physical network link as the client and server (unless you use HTTPS).

Instead of embedding the user name and password in the URL, you should use the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method to specify the user name and password for Basic authentication. This prevents others from viewing the credentials. If you specify credentials in both places, BITS uses the user name and password from the URL.

For [Passport](https://msdn.microsoft.com/library/windows/desktop/aa384067) authentication, BITS supports explicit credentials only, not implicit credentials tied to the account.

For challenge/response authentication, BITS impersonates the user and uses [Snego](2087a84c-d302-4511-9f02-2d20ee9e0d8e) to determine which challenge/response authentication to use, such as NTLM or the Kerberos protocol. For a list of challenge/response schemes that BITS supports, see [**BG\_AUTH\_SCHEME**](/windows/desktop/api/Bits1_5/ne-bits1_5-__midl_ibackgroundcopyjob2_0002).

BITS jobs can fail if the virtual directory on the server has anonymous authentication and another authentication scheme enabled and if ACLs protect the virtual directory or download files. For example, a job fails with "access denied" if the virtual directory has anonymous and integrated authentication enabled and the file contains an ACL that allows only Ben to read the file. This occurs because the virtual directory allows anonymous access, so IIS does not explicitly authenticate Ben (Ben's credentials are not used to access the file and access is denied).

## Using implicit credentials

To use the user's implicit (logon) credentials for NTLM or Kerberos authentication, call the [**IBackgroundCopyJob2::SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method and set the **UserName** and **Password** members of the [**BG\_BASIC\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0003) structure to **NULL**. If you specify implicit credentials for a proxy, BITS will also use the implicit credentials for server authentication unless you specify explicit server credentials.

For additional information for services, see [Service Accounts and BITS](service-accounts-and-bits.md).

You could also change the **LMCompatibilityLevel** or **UseLMCompat** registry value; however, you should change these values only if you have an existing application that cannot be changed to call the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method.

BITS will use implicit credentials for authentication if the **LMCompatibilityLevel** registry value is two or greater, and you have not called the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method. The full path to the **LMCompatibilityLevel** registry value is **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**LSA**\\**LmCompatibilityLevel**.

Note that changing the **LMCompatibilityLevel** registry value can affect other applications and services running on the computer. For more information about using the **LMCompatibilityLevel** registry value, see [KB147706](http://go.microsoft.com/fwlink/p/?linkid=83990).

If setting the **LMCompatibilityLevel** registry value is an issue, you can create the **UseLMCompat** registry value under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**BITS**. The registry value is a DWORD. The following table lists the possible values for **UseLMCompat**:

| Value | Description                                                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | BITS will send implicit credentials whenever the server prompts for NTLM or Kerberos credentials.                                                                                           |
| 1     | BITS will send implicit credentials only if the client computer's **LMCompatibilityLevel** registry value is greater than or equal to 2.**Prior to BITS 1.5:** Not supported<br/>     |
| 2     | BITS will send implicit credentials only if the application called the [**SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method. **Prior to BITS 2.0:** Not supported<br/> |



 

BITS will use the following default values for the **UseLMCompat** registry value if the registry value does not exist:

| Operating system                     | Value |
|--------------------------------------|-------|
| Windows XP                           | 0     |
| Windows XP with Service Pack 1 (SP1) | 0     |
| Windows XP with Service Pack 2 (SP2) | 1     |
| Windows XP with Service Pack 3 (SP3) | 1     |
| Windows Server 2003                  | 1     |
| Windows Server 2003 R2               | 1     |
| Windows Vista                        | 2     |
| Windows Server 2008                  | 2     |



 

**BITS 1.2 and earlier:** BITS uses implicit credentials for NTLM or Kerberos authentication. If you wrote an application based on BITS 1.0 or 1.2, the same application may not run using later versions of BITS if the **LMCompatibilityLevel** value is less than two. Note that the default **LMCompatibilityLevel** value for Windows XP is zero.

## Using certificates for client/server authentication

In secure client/server communication, clients and servers can use digital certificates to mutually authenticate each other. BITS automatically supports certificate-based server authentication for secure HTTP transports. To provide BITS the client certificate needed for mutual authentication, call either the [**IBackgroundCopyJobHttpOptions::SetClientCertificateByID**](/windows/desktop/api/Bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setclientcertificatebyid) or [**IBackgroundCopyJobHttpOptions::SetClientCertificateByName**](/windows/desktop/api/Bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setclientcertificatebyname) method.

When a website accepts but does not require an SSL client certificate, and the BITS job does not specify a client certificate, the job will fail with **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED** (0x80072f0c).

**Prior to Windows Vista:** BITS supports certificate-based server authentication for secure HTTP transports, but certificate-based client authentication is not supported.

## How to handle authenticated proxy scenarios that require user-specific settings

If you are using BITS in an environment that requires proxy authentication while running as an account without usable NTLM or Kerberos credentials in the machine's network domain, you must take extra steps to authenticate properly by using the credentials of another user account that does have credentials on the domain. This is a typical scenario when your BITS code is running as a system service such as LocalService, NetworkService, or LocalSystem, as those accounts do not have usable NTLM or Kerberos credentials.

The proxy detection logic used in BITS does the following when a network helper token (BG\_TOKEN\_NETWORK) is set:

-   If [**IBackgroundCopyJob::SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) was called with **BG\_JOB\_PROXY\_USAGE\_PRECONFIG**, then detect local IE proxy settings using job owner token context impersonation via [**WinHttpGetIEProxyConfigForCurrentUser**](https://msdn.microsoft.com/library/windows/desktop/aa384096).
-   If [**IBackgroundCopyJob::SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) was called with **BG\_PROXY\_USAGE\_AUTODETECT** or if the IE settings from the **BG\_JOB\_PROXY\_USAGE\_PRECONFIG** case specify auto-detect or an auto-config URL, then conduct auto-proxy detection, or Web Proxy Autodiscovery Protocol (WPAD), using helper token impersonation via [**WinHttpGetProxyForUrl**](https://msdn.microsoft.com/library/windows/desktop/aa384097).

After that, helper token impersonation is used for proxy or server authentication throughout.

This means that the correct user identity (the helper token's identity) is used for network-based proxy detection (WPAD) and for proxy authentication, but that the actual detection of local (IE) proxy settings is always done using the job owner's token, even when a helper token is configured. This behavior is by design in BITS, but there is a workaround you can use when necessary for your situation.

1.  Impersonate the user account you're using for NTLM/Kerberos credentials.
2.  Retrieve the user account's IE proxy settings by calling [**WinHttpGetIEProxyConfigForCurrentUser**](https://msdn.microsoft.com/library/windows/desktop/aa384096).
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

## Authentication scenarios not supported

The following table shows the authentication requests that BITS does not support.



| Scenario not supported                                                                                   | Windows XP    | Windows Server 2003 |
|----------------------------------------------------------------------------------------------------------|---------------|---------------------|
| Passport authentication on the server when the proxy requires authentication (using the HTTPS protocol). | Not supported | Not supported       |
| Passport authentication when the auto-detect proxy setting is set.                                       | Not supported | Not supported       |
| Any authentication scheme on the server when the proxy requires Digest authentication.                   | Not supported | Not supported       |
| Negotiate authentication on the server when the proxy requires Basic authentication.                     | Not supported |                     |
| Using HTTPS when the proxy requires Digest authentication.                                               | Not supported |                     |



 

 

 





