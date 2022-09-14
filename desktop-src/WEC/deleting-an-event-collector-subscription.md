---
title: Deleting an Event Collector Subscription
description: You can delete an Event Collector subscription from a local computer.
ms.assetid: d3102149-906d-4286-85c8-e5b1eb6dd382
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Deleting an Event Collector Subscription

You can delete an Event Collector subscription from a local computer. You must know the name of the subscription before you can delete it. For more information about how to list the current subscriptions on a local computer, see [Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md), or type the following command at the command prompt:

**wecutil es**

> [!Note]
>
> You can use this example to delete an Event Collector subscription or you can type the following command at the command prompt:
>
> **wecutil ds** *SubscriptionName*

 

After you retrieve the name of the Event Collector subscription to delete, you can provide the name of the subscription as a parameter to [**EcDeleteSubscription**](/windows/desktop/api/Evcoll/nf-evcoll-ecdeletesubscription).

The following C++ code example shows how to delete an Event Collector subscription.


```C++
#include <windows.h>
#include <EvColl.h>
#include <strsafe.h>

#pragma comment(lib, "wecapi.lib")

void __cdecl wmain()
{
    DWORD dwRetVal;
    LPWSTR lpSubname = L"MyTestSubscription";

    // Delete the specified Event Collector subscription.
    if (!EcDeleteSubscription(lpSubname, 0))
    {
        dwRetVal = GetLastError();
        LPVOID lpwszBuffer;

        FormatMessageW( FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
            NULL,
            dwRetVal,
            0,
            (LPWSTR) &lpwszBuffer,
            0,
            NULL);

        if (!lpwszBuffer)
        {
            wprintf(L"Failed to FormatMessage.  Operation Error Code: %u." 
                L"Error Code from FormatMessage: %u\n", dwRetVal, GetLastError());
            return;
        }

        wprintf(L"\nFailed to Perform Operation.\nError Code: %u\n"
            L"Error Message: %s\n", dwRetVal, lpwszBuffer);

        LocalFree(lpwszBuffer);
    }
}
```



## Related topics

<dl> <dt>

[Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md)
</dt> <dt>

[Windows Event Collector Reference](windows-event-collector-reference.md)
</dt> </dl>

 

 




