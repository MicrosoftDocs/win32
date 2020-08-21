---
title: Users and Network Connections
description: BITS transfers files only when the job owner is logged on and a network connection is established.
ms.assetid: b31fc04f-8fa8-407f-9380-ca6b09589c46
keywords:
- network connections BITS
- transfer job BITS , ownership
- transfer job BITS , ownership, user account
ms.topic: article
ms.date: 10/04/2018
---

# Users and Network Connections

BITS transfers files only when the job owner is logged on and a network connection is established. BITS processes the transfer job using the security context of the job owner. The user who created the job is considered the owner of the job. However, a user with administrator privileges can [**take ownership**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-takeownership) of another user's job.

BITS suspends a job when the owner logs off or if the network connection is lost (BITS will not force a network connection). BITS resumes the job when the owner logs back on and a network connection is established. After the network connection is established, a short delay may occur before BITS begins transferring data.

If the network connection is lost, all jobs whose state is [**BG\_JOB\_STATE\_QUEUED**](/windows/desktop/api/Bits/ne-bits-bg_job_state) or **BG\_JOB\_STATE\_TRANSFERRING** are moved to the **BG\_JOB\_STATE\_TRANSIENT\_ERROR** state with a [BG\_E\_NETWORK\_DISCONNECTED](bits-return-values.md) error code. When a network connection is established, all jobs in a **BG\_JOB\_STATE\_TRANSIENT\_ERROR** state, which may include any error code, are moved to the **BG\_JOB\_STATE\_QUEUED** state.

For BITS to detect that a user is logged on, the user must use one of the following interactive logon options:

-   Log on through the Welcome screen.
-   Log on to a [terminal service](../termserv/terminal-services-portal.md) client.
-   Use [fast user switching](../shell/fast-user-switching.md).
-   Starting with Windows 10, version 1607, log on from another device using Remote Powershell. See [To manage PowerShell Remote sessions](using-windows-powershell-to-create-bits-transfer-jobs.md) for details.

Running an application as another user (by using the **RunAs** command) is not an interactive logon; BITS will not run jobs associated with the specified user.

The LocalSystem, LocalService, and NetworkService system accounts are always logged on; therefore, jobs submitted by a service using these accounts always run. For information and limitations on using service accounts, see [Service Accounts and BITS](service-accounts-and-bits.md).

Job owners can provide a helper token to be used in situations where multiple tokens are needed to complete a transfer, such as for authentication with a remote host. See [Helper Tokens for BITS Transfer Jobs](helper-tokens-for-bits-transfer-jobs.md) for details. In earlier versions of Windows, the job owner effectively had to have administrator privileges to start a job that used a helper token. In Windows 10, version 1607, it is now possible for a BITS job owner to set helper tokens without being an administrator, as long as the helper token does not have administrator capabilities. This reduces the vulnerability footprint of background download or update tools by enabling them to run under the lower-privileged NetworkService account rather than under an account with administrative privileges.

Users with a [restricted token](../secauthz/restricted-tokens.md) (a token that contains restricting SIDs) cannot create or modify jobs.
 

 