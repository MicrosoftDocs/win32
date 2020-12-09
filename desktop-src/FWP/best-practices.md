---
title: Best Practices (Windows Filtering Platform)
description: The following list contains best practices for developing applications using the Windows Filtering Platform (WFP) API.
ms.assetid: 017ff210-8666-466e-8424-c95e750fd5ac
ms.topic: article
ms.date: 05/31/2018
---

# Best Practices (Windows Filtering Platform)

The following list contains best practices for developing applications using the Windows Filtering Platform (WFP) API.

-   Use dynamic sessions.

    Many applications add filtering policy objects at start, and then delete these objects at stop. By using a dynamic session, you guarantee that these objects are deleted even if the application crashes. Furthermore, simply closing the engine handle at stop is more efficient than making individual calls to delete each object.

-   Either handle transaction timeouts gracefully or set the session **txnWaitTimeoutInMSec** to infinite to prevent timeouts.

    Even if you do not use explicit transactions, most calls are still executed under an implicit transaction and thus can timeout.

-   Use explicit transactions to combine related add or delete operations into a single transaction.

    This is more efficient and makes it easy to clean up partial results in error paths.

-   Use MUI compliant strings.

    All the localizable strings are stored in a common data structure: [**FWPM\_DISPLAY\_DATA0**](/windows/desktop/api/Fwptypes/ns-fwptypes-fwpm_display_data0). The strings within this structure can be indirect strings of the type supported by [**SHLoadIndirectString**](/windows/win32/api/shlwapi/nf-shlwapi-shloadindirectstring). Before an **FWPM\_DISPLAY\_DATA0** structure is returned by any of the functions, the indirect strings are resolved to the specified string resource using the caller's locale.

-   Associate all objects to a provider.

    When multiple providers are installed on the system, this makes it is easier for diagnostic tools to determine who added what.

-   Add filters to your own sublayer.

    Once a terminating filter in a sublayer is hit, no more filters in that sublayer are evaluated. Thus, if you add your filters to the same sublayer as another provider, you may prevent each other's filters from being invoked, resulting in unexpected results.

-   Use Application Layer Enforcement (ALE) rather than packet-oriented filtering.

    Filtering at the packet layer is slow.

-   Filter ICMP errors and RST events before they are generated.

    This is more efficient that filtering these events after they are generated.

-   Perform packet inspection at Stream/Datagram Data layer rather than at the Transport layer.

    This applies to developing callouts. For more information, see [Callout Driver Programming Considerations](/windows-hardware/drivers/network/callout-driver-programming-considerations) in the Windows Driver Kit (WDK).

-   Consider performance implications when using complex filters.

    Starting in Windows 7 and Windows Server 2008 R2, filters can be created with multiple conditions which use the same field key. This allows complex policies to be created with fewer filters. However such complex filters might incur a slower performance for the WFP filter engine to classify. An evaluation should be made to determine whether use of such filters causes an adverse effect on the overall performance of your solution.

 

 
