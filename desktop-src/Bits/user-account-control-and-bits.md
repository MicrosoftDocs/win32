---
title: User Account Control and BITS
description: When an administrator user logs onto the computer, two access tokens are created. One is a filtered standard user access token and the other is a full administrator access token.
ms.assetid: 02439ab3-b885-4a2f-b507-0c48d2b30b76
ms.topic: article
ms.date: 7/12/2019
---

# BITS Security, Tokens, and Administrator Accounts

## HTTP Server certificate callbacks
Correctly validating server certificates is a key part of maintaining HTTPS security. BITS helps by always validating server certificates against a list of requirements specified by [**SetSecurityFlags**](/windows/desktop/api/bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setsecurityflags). By default, BITS uses "browser" style certificate validation.

You can also specify a custom function to call in order to further validate the certificate. Set the server certificate callback with the [**SetServerCertificateValidationInterface**](/windows/desktop/api/Bits10_3/nf-bits10_3-ibackgroundcopyjobhttpoptions3-setservercertificatevalidationinterface) method. Your method will only be called after the operating system has validated the certificate based on the [**SetSecurityFlag**s](/windows/desktop/api/bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setsecurityflags) call. 

## HTTP Client certificates
You can set a client certificate on an HTTP job with two different certificate settings methods. You can set a certificate either by [ID](/windows/desktop/api/bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setclientcertificatebyid) or by the certificate [subject name](/windows/desktop/api/bits2_5/nf-bits2_5-ibackgroundcopyjobhttpoptions-setclientcertificatebyname). The client certificate will be used during TLS negotiation (or renegotiation) if the server requires client authentication.

## Write-only HTTP headers
BITS helps you protect HTTP authentication tokens from unwanted access. Often an HTTP server will need some kind of security token or string when downloading or uploading a file to HTTP servers.

BITS protects these authentication tokens in several ways.
* BITS lets you use TLS- and SSL-protected HTTP connections by specifying an HTTPS URL.
* Custom headers are always persisted in an encrypted format on disk.
* You can prevent customer headers from being returned to other programs with the [**IBackgroundCopyJobHttpOptions3::MakeCustomHeadersWriteOnly**](/windows/win32/api/Bits10_3/nf-bits10_3-ibackgroundcopyjobhttpoptions3-makecustomheaderswriteonly) method.


## Standard and Administrator users
A user who is in the administrator group can run a process with standard user access or in an elevated state (with administrator privileges). BITS will run the job in either state as long as the user is logged onto the computer. However, if the user created the job or took ownership of the job in an elevated state, the user must be in the elevated state to retrieve or modify the job (otherwise, the call fails with Access Denied (0x80070005)). To determine the elevated state of a job, call the [**IBackgroundCopyJob4::GetOwnerElevationState**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-getownerelevationstate) method.

A standard user cannot enumerate or modify jobs owned by other users.

## Integrity level
In addition to the elevated state, the integrity level of the token can determine if the user can modify a job. A client cannot modify jobs created by a token with a higher integrity level. In particular, many local-system tokens carry an integrity level higher than the integrity level of an elevated window, and so they cannot be modified by an administrator from an ordinary elevated command window. For example, Windows Update and SMS jobs run as LocalSystem which has a higher integrity level than an elevated token so an administrator cannot modify or delete these jobs. To modify these job, create a Task Scheduler task that runs as local system. The task can execute a console application that uses the BITS API, or the task could execute a script that calls BitsAdmin.exe. To determine the integrity level used, call the [**IBackgroundCopyJob4::GetOwnerIntegrityLevel**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-getownerintegritylevel) method.

## Service identity
Starting in the Windows 10 May 2019 Update (10.0; Build 18362), BITS jobs started from a service will maintain the service identity. This allows for services that wish to use BITS to download files to or upload files from a directory whose permissions are tied to the service SID. Additionally, network traffic will be correctly attributed to the service that requested the BITS job instead of being attributed to BITS.

 




