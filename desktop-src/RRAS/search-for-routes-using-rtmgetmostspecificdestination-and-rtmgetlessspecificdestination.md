---
title: Search for Routes Using a Prefix Tree
description: The following sample code shows how to use RtmGetMostSpecificDestination and RtmGetLessSpecificDestination to walk up the prefix tree in the routing table.
ms.assetid: 14e8e87f-c76c-48ad-93b5-0d8a711148d6
ms.topic: article
ms.date: 05/31/2018
---

# Search for Routes Using a Prefix Tree

The following sample code shows how to use [**RtmGetMostSpecificDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetmostspecificdestination) and [**RtmGetLessSpecificDestination**](/windows/desktop/api/Rtmv2/nf-rtmv2-rtmgetlessspecificdestination) to walk up the prefix tree in the routing table.


```C++
// Used to walk up the prefix tree, given the destination and mask

// Search for a best matching route to a network
// given (address,mask) for this destination network

// First get the best matching destination

RTM_IPV4_SET_ADDR_AND_MASK(NetAddress, Addr, Mask);

Status = RtmGetMostSpecificDestination(RtmRegHandle,
                                       &NetAddress,
                                       RTM_BEST_PROTOCOL,   // Determines which route information is returned.
                                       RTM_VIEW_MASK_UCAST, // Give the information for best unicast route
                                       DestInfo1);
// Use RtmGetLessSpecificDestination to go up the
// tree until it returns ERROR_NOT_FOUND. Use two
// RTM_DEST_INFO buffers - DestInfo1 & DestInfo2
// alternately to avoid all unnecessary copying.

while (Status == NO_ERROR)
{
    if (DestInfo1->DestAddress.NumBits == NetAddress.NumBits)
    {
        Print("Exact Match of Destination\n");
    }

    Status = RtmGetLessSpecificDestination(RtmRegHandle,
                                           DestInfo1->DestHandle,
                                           RTM_BEST_PROTOCOL,
                                           RTM_VIEW_MASK_UCAST,
                                           DestInfo2);

    // NOTE that the buffer is DestInfo1 and not DestInfo2
    RtmReleaseDestInfo(RtmRegHandle, DestInfo1);

    if (Status != NO_ERROR) 
    {
        break;
    }
    
    // Use any information you want in DestInfo2
    Print("Mask Len: %d\n", DestInfo2->DestAddress.NumBits);

    Status = RtmGetLessSpecificDestination(RtmRegHandle,
                                           DestInfo2->DestHandle,
                                           RTM_BEST_PROTOCOL,
                                           RTM_VIEW_MASK_UCAST,
                                           DestInfo1);

    // NOTE that the buffer is DestInfo2 and not DestInfo1
    RtmReleaseDestInfo(RtmRegHandle, DestInfo2);

    if (Status != NO_ERROR) 
    {
        break;
    }

    // Use any information you want in DestInfo1
    Print("Mask Len: %d\n", DestInfo1->DestAddress.NumBits);
}
```



 

 




