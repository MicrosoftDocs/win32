---
title: Security Channel Layer Examples
description: The following examples illustrate security in the Channel Layer.
ms.assetid: ac4f0275-4783-411d-98da-2c5a1a169dcc
keywords:
- security examples
- security examples, setup
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Security Channel Layer Examples

The following examples illustrate security in the [Channel Layer](channel-layer-overview.md)

Windows transport security over TCP: Client: [RequestReplyTcpClientWithWindowsTransportSecurityExample](requestreplytcpclientwithwindowstransportsecurityexample.md), Server: [RequestReplyTcpServerWithWindowsTransportSecurityExample](requestreplytcpserverwithwindowstransportsecurityexample.md).

Windows transport security over named pipes: Client: [RequestReplyNamedPipesClientWithWindowsTransportSecurityExample](requestreplynamedpipesclientwithwindowstransportsecurityexample.md), Server: [RequestReplyNamedPipesServerWithWindowsTransportSecurityExample](requestreplynamedpipesserverwithwindowstransportsecurityexample.md).

SSL transport security: Client: [HttpClientWithSslExample](httpclientwithsslexample.md), Server: [HttpServerWithSslExample](httpserverwithsslexample.md).

Username over SSL mixed-mode security: Client: [HttpClientWithUsernameOverSslExample](httpclientwithusernameoversslexample.md), Server: [HttpServerWithUsernameOverSslExample](httpserverwithusernameoversslexample.md).

Username over SSL mixed-mode security: Client: [HttpClientWithKerberosOverSslExample](httpclientwithkerberosoversslexample.md), Server: [HttpServerWithKerberosOverSslExample](httpserverwithkerberosoversslexample.md).

Username over SSL mixed-mode security: [MetadataImportWithUsernameOverSslExample](metadataimportwithusernameoversslexample.md). Issued token over SSL mixed-mode security: [MetadataImportWithIssuedTokenOverSslExample](metadataimportwithissuedtokenoversslexample.md). X509 certificate over SSL mixed-mode security: [MetadataImportWithX509OverSslExample](metadataimportwithx509oversslexample.md).

## One-Time Setup for Security Samples

To run WWSAPI security examples, you need to set up the client and server certificates for SSL, as well as a local user account for HTTP header authentication. Before you start, you need the following tools:

-   MakeCert.exe (Available in the Windows 7 SDK.)
-   CertUtil.exe or CertMgr.exe (CertUtil.exe is available in the Windows SDKs starting with Windows Server 2003. CertMgr.exe is available in the Windows 7 SDK. You only need one of these tools.)
-   HttpCfg.exe: (You need this only if you are using Windows 2003 or Windows XP. This tool is available in Windows XP SP2 Support Tools and also comes with the Windows Server 2003 Resource Kit Tools CD.)

If you get the WWSAPI examples by installing the Windows 7 SDK, you can find the MakeCert.exe and CertMgr.exe under %ProgramFiles%\\Microsoft SDKs\\Windows\\v7.0\\bin.

Perform the following five-step setup from the command prompt (elevated if you are using Windows Vista and above):

1.  Generate a self-signed certificate to be the certificate authority (CA) or issuer: **MakeCert.exe -ss Root -sr LocalMachine -n "CN=Fake-Test-CA" -cy authority -r -sk "CAKeyContainer"**
2.  Generate a server certificate using the previous certificate as the issuer: **MakeCert.exe -ss My -sr LocalMachine -n "CN=localhost" -sky exchange -is Root -ir LocalMachine -in Fake-Test-CA -sk "ServerKeyContainer"**
3.  Find the thumbprint (a 40-character SHA-1 hash) of the server certificate by running either of the following commands and search for the certificate named localhost with issuer Fake-Test-CA:
    -   **CertUtil.exe -store My localhost**
    -   **CertMgr.exe -s -r LocalMachine My**
4.  Register the server certificate?s thumbprint with no spaces with HTTP.SYS:
    -   On Windows Vista and above (the "appid" option is an arbitrary GUID): **Netsh.exe http add sslcert ipport=0.0.0.0:8443 appid={00112233-4455-6677-8899-AABBCCDDEEFF}** certhash=<40CharacterThumbprint>
    -   On Windows XP or 2003: **HttpCfg.exe set ssl -i 0.0.0.0:8443 -h <40CharacterThumbprint>**
5.  Create a local user: **Net user "TestUserForBasicAuth" "TstPWD@\*4Bsic" /add**

To clean up the certificates, SSL certificate binding and the user account created in the previous steps, run the following commands. Note if there are multiple certificates of the same name, CertMgr.exe will need your input before deleting them.

-   **CertMgr.exe -del -c -n Fake-Test-CA -s -r LocalMachine Root**
-   **CertMgr.exe -del -c -n localhost -s -r LocalMachine My**
-   **Netsh.exe http delete sslcert ipport=0.0.0.0:8443 (or HttpCfg.exe delete ssl -i 0.0.0.0:8443)**
-   **Net user "TestUserForBasicAuth" /delete**

Make sure there is only one root certificate named Fake-Test-CA. If you are unsure, it?s always safe to try to clean up these certificates using the cleanup commands above (and ignore errors) before starting the five-step setup.

 

 




