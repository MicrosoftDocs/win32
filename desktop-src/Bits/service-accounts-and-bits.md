---
title: Service Accounts and BITS
description: You can use BITS to transfer files from a service. The service must use the LocalSystem, LocalService, or NetworkService system account. These accounts are always logged on; therefore, jobs submitted by a service using these accounts always run.
ms.assetid: 43fb58d6-3a99-488f-ab43-dbb4a794fc2f
keywords:
- service accounts BITS
- transfer job BITS , ownership, service account
- proxy BITS , service accounts
- credentials to transfer job BITS
ms.topic: article
ms.date: 10/04/2018
---

# Service Accounts and BITS

You can use BITS to transfer files from a service. The service must use the LocalSystem, LocalService, or NetworkService system account. These accounts are always logged on; therefore, jobs submitted by a service using these accounts always run.

If a service running under a system account impersonates the user before calling BITS, BITS responds as it would for any user account (for example, the user needs to be logged on to the computer for the transfer to occur). The service should also use dynamic cloaking with the BITS interface pointers when impersonating the user. Cloaking is not inherited, therefore you must call the [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) function on each interface pointer that you receive from BITS (for example, the job pointer returned from calling the [**IBackgroundCopyManager::CreateJob**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-createjob) method); it is not enough to set cloaking on the manager interface pointer. You can also call the [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) function for the process instead of calling the **CoSetProxyBlanket** function on each interface pointer.

However, if the service does not impersonate the user, the following behaviors apply:

- Jobs created by the service account are owned by that account. Because system accounts are always logged on, BITS transfers the files as long as the computer is running and there is a network connection.
- System accounts should not use mapped network drive letters because the drive letters are specific to a session and the mapping may be lost after a computer restart.
- In the absence of a [Helper Token](helper-tokens-for-bits-transfer-jobs.md), network authentication uses computer credentials for LocalSystem and NetworkService accounts and anonymous credentials for the LocalService account. BITS returns "access denied" if the access control list (ACL) for the source file limits access to a user account.
- For details on how authentication works in the presence of a [Helper Token](helper-tokens-for-bits-transfer-jobs.md), see [Authentication](authentication.md).
- Microsoft Internet Explorer proxy settings are stored per-user and are not set for system accounts. Consider configuring a helper token on your BITS jobs, or explicitly setting the correct proxy settings by calling [**IBackgroundCopyJob::SetProxySettings**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setproxysettings) with **BG\_JOB\_PROXY\_USAGE\_OVERRIDE**. Alternatively, you can use the **/Util /SetIEProxy** switches of BitsAdmin.exe to set Internet Explorer proxy settings for the LocalSystem, LocalService, or NetworkService system account. For details, see [BitsAdmin Tool](bitsadmin-tool.md).

Note that BITS does not recognize the proxy settings that are set using the Proxycfg.exe file.