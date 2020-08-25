---
title: Helper Tokens for BITS Transfer Jobs
description: Helper Tokens for BITS Transfer Jobs
ms.assetid: f29f9870-e406-472b-9342-203def7453ae
ms.topic: article
ms.date: 05/31/2018
---

# Helper Tokens for BITS Transfer Jobs

In Windows Vista, the Background Intelligent Transfer Service (BITS) service allows an application to associate a single security token to a BITS transfer job. The BITS transfer job then uses this token for authentication and for access to local and remote resources.

In Windows 7, the BITS service associates an additional token to a BITS transfer job. The BITS transfer job can be configured with an additional security token, which is an impersonation token created by an application calling the BITS COM API. This helper token model allows applications to simultaneously use two different security tokens to access local files, client-side certificates, remote files, and proxies. For example, a BITS transfer job is created that writes the downloaded data to a privileged local directory, and then it presents a low-rights domain identity to the HTTP server and proxy server.

An application, typically a Windows service, specifies a helper token by using the new interface [**IBitsTokenOptions**](/windows/desktop/api/Bits4_0/nn-bits4_0-ibitstokenoptions). This interface is implemented by the BITS job object. The application calls [**IBackgroundCopyJob::QueryInterface**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) to get the interface pointer. The application impersonates the helper identity and calls [**IBitsTokenOptions::SetHelperToken**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertoken) to pass the token to the BITS service. Then the application specifies the resources to which the token applies by passing a set of bit flags using [**IBitsTokenOptions::SetHelperTokenFlags**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertokenflags). The application clears all the flags (using **SetHelperTokenFlags** again) to revert the behavior. The BITS service stores the bit flags and the token in the BITS transfer job.

When the owner of the BITS transfer jobs logs off, the BITS service discards any helper tokens that are associated with the transfer job. If the transfer is not complete, the BITS service places the job in an error state with the **BG\_E\_TOKEN\_REQUIRED** error code and discards the helper token. The client application can refresh the token by calling [**IBitsTokenOptions::SetHelperToken**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertoken) and can then resume the BITS transfer job. Alternatively, the client application can clear the helper token flags using [**IBitsTokenOptions::SetHelperTokenFlags**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertokenflags) and then resume the transfer job without a helper token.

Similarly, when the owner of a terminal services session logs off, the BITS service must discard any helper tokens from that session and place the affected transfer jobs in an error state with the **BG\_E\_TOKEN\_REQUIRED** error code.

The helper token model requires a change to BITS access control policy. Previous versions of BITS implemented access checks on every method call. Starting with Windows 7, the access check must be performed inside the [**IBackgroundCopyJob::QueryInterface**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) call; otherwise, the helper token might not have access to the transfer job.

> [!Note]  
> Older implementations effectively required that BITS users have administrator privileges in order to set helper tokens. Starting with Windows 10, version 1607, non-administrator BITS users can use [**IBitsTokenOptions::SetHelperToken**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertoken) to set non-administrator helper tokens on BITS jobs they own. This change enables non-administrator BITS users (such as background downloader services running under the [NetworkService account](/windows/desktop/Services/networkservice-account)) to set helper tokens.
>
> Specifically, the implementation has been changed to allow users without administrator privileges to set helper tokens, as long as the following conditions are met:
>
> -   during the [**IBackgroundCopyJob::QueryInterface**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) call, the SID of the caller's thread's token is the same as the SID of the job owner's user account, and
> -   when [**IBitsTokenOptions::SetHelperToken**](/windows/desktop/api/Bits4_0/nf-bits4_0-ibitstokenoptions-sethelpertoken) is called, the helper token does not have the administrator SID (**DOMAIN\_ALIAS\_RID\_ADMINS**) enabled.

 

## Related topics

<dl> <dt>

[**IBitsTokenOptions**](/windows/desktop/api/Bits4_0/nn-bits4_0-ibitstokenoptions)
</dt> </dl>

 

 