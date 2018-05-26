---
Description: By using Enumerations, you can obtain a list of all the specific peer entities that match your criteria.
ms.assetid: f72e372a-0d23-47f4-8518-1296ec81ce55
title: Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerations

By using Enumerations, you can obtain a list of all the specific peer entities that match your criteria.

**To obtain an enumeration and retrieve the results**

1.  Obtain a handle to the enumeration. Call a **PeerEnum** function, for example, call the [**PeerGraphEnumRecords**](/windows/win32/P2P/nf-p2p-peergraphenumrecords?branch=master) Peer Graphing function. The **PeerEnum** functions create the enumeration, and return a handle to that enumeration to the calling application. This handle must be used to retrieve the results.
2.  Optionally, obtain the number of entities in the enumeration. Call a **GetItemCount** function, for example, call [**PeerGraphGetItemCount**](/windows/win32/P2P/nf-p2p-peergraphgetitemcount?branch=master) or [**PeerGetItemCount**](/windows/win32/P2P/nf-p2p-peergetitemcount?branch=master).
    > [!Note]  
    > You can use the value returned by the **GetItemCount** function to determine the number of items available to retrieve.

     

3.  Retrieve a group of results. Call a **GetNextItem** function, for example, call [**PeerGraphGetNextItem**](/windows/win32/P2P/nf-p2p-peergraphgetnextitem?branch=master).
    > [!Note]  
    > When an application calls a **GetNextItem** function, it specifies the number of entities to return, and then the function returns a pointer to an array of pointers to the entities, and the number of entities, which is always less than or equal to the number specified. An application might need to call this function many times—until the number of entities returned is less than the number requested.

     

4.  After the data is not needed, free the pointer to the data. Call a **FreeData** function, for example, call [**PeerGraphFreeData**](/windows/win32/P2P/nf-p2p-peergraphfreedata?branch=master) or [**PeerFreeData**](/windows/win32/P2P/nf-p2p-peerfreedata?branch=master).
    > [!Note]  
    > For more information, see [Freeing Peer Data](freeing-peer-data.md).

     

5.  After the application does not need the handle to the enumeration, release it. Call an **EndEnumeration** function, for example, call [**PeerEndEnumeration**](/windows/win32/P2P/nf-p2p-peerendenumeration?branch=master) or [**PeerGraphEndEnumeration**](/windows/win32/P2P/nf-p2p-peergraphendenumeration?branch=master).

## Example of an Enumeration

The following code snippet shows you how to enumerate through available identities.


```C++
#include <p2p.h>
#include <stdio.h>

#pragma comment(lib, "p2p.lib")

//-----------------------------------------------------------------------------
// Function: EnumIdentities
//
// Purpose:  Demonstrate how to enumerate identities.
//
// Returns:  HRESULT
//

HRESULT EnumIdentities(void)
{
    HPEERENUM hPeerEnum = NULL;
    HRESULT hr = PeerEnumIdentities(&amp;hPeerEnum);

    if (SUCCEEDED(hr))
    {
        ULONG cIdentities = 0;
        hr = PeerGetItemCount(hPeerEnum, &amp;cIdentities);

        if (SUCCEEDED(hr))
        {
            ULONG i;

            for (i = 0; i < cIdentities; i++)
            {
                ULONG cItem = 1; // process one result at a time
                PEER_NAME_PAIR ** ppNamePair = NULL; // pointer to an array of pointers

                hr = PeerGetNextItem(hPeerEnum, &amp;cItem, (PVOID**) &amp;ppNamePair);

                if (SUCCEEDED(hr) &amp;&amp; (1 == cItem))
                {
                    wprintf(L"%s [%s]\r\n", (*ppNamePair)->pwzFriendlyName, (*ppNamePair)->pwzPeerName);
                    PeerFreeData(ppNamePair);
                }
            }
        }
        PeerEndEnumeration(hPeerEnum);
    }
 
    return hr;
}
```



 

 



