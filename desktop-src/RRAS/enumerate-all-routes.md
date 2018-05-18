---
title: Enumerate All Routes
description: The following procedure outlines the steps used to enumerate any of the entities used by the RTMv2 API. The sample code that follows shows how to enumerate all routes.
ms.assetid: '78a50e4a-f3c7-4a0d-a528-18d35b66369d'
---

# Enumerate All Routes

The following procedure outlines the steps used to enumerate any of the entities used by the RTMv2 API. The sample code that follows shows how to enumerate all routes.

**The basic process for each enumeration is as follows**

1.  Start the enumeration by obtaining a handle from the routing table manager. Call [**RtmCreateDestEnum**](rtmcreatedestenum.md), [**RtmCreateRouteEnum**](rtmcreaterouteenum.md) and [**RtmCreateNextHopEnum**](rtmcreatenexthopenum.md) to supply the criteria that specifies the kind of information being enumerated. This criteria includes, but is not limited to a range of destinations, a particular interface, and the views in which the information resides.
2.  Call [**RtmGetEnumDests**](rtmgetenumdests.md), [**RtmGetEnumRoutes**](rtmgetenumroutes.md) and [**RtmGetEnumNextHops**](rtmgetenumnexthops.md) one or more times to retrieve data until the routing table manager returns ERROR\_NO\_MORE\_ITEMS. The route, destination, and next-hop data is returned in order of the address information (and the preference and metric values, if routes are being enumerated).
3.  Call [**RtmReleaseDests**](rtmreleasedests.md), [**RtmReleaseRoutes**](rtmreleaseroutes.md) and [**RtmReleaseNextHops**](rtmreleasenexthops.md) when the handles or information structures associated with the enumeration are no longer required.
4.  Call [**RtmDeleteEnumHandle**](rtmdeleteenumhandle.md) to release the enumeration handle that was returned when the enumeration was created. This function is used to release the handle for all types of enumerations.

> [!Note]  
> Routes that are in the hold-down state are only enumerated when a client requests data from all views using RTM\_VIEW\_MASK\_ANY.

 

The following sample code shows how to enumerate all routes in the routing table.


```C++
MaxHandles = RegnProfile.MaxHandlesInEnum;

RouteHandles = _alloca(MaxHandles * sizeof(HANDLE));

// Do a "route enumeration" over the whole table
// by passing a NULL DestHandle in this function.

DestHandle = NULL; // Give a valid handle to enumerate over a particular destination

Status = RtmCreateRouteEnum(RtmRegHandle,
                            DestHandle,
                            RTM_VIEW_MASK_UCAST|RTM_VIEW_MASK_MCAST,
                            RTM_ENUM_OWN_ROUTES, // Get only your own routes
                            NULL,
                            0,
                            NULL,
                            0,
                            &amp;EnumHandle2);
if (Status == NO_ERROR)
{
    do
    {
        NumHandles = MaxHandles;

        Status = RtmGetEnumRoutes(RtmRegHandle
                                  EnumHandle2,
                                  &amp;NumHandles,
                                  RouteHandles);

        for (k = 0; k < NumHandles; k++)
        {
            wprintf("Route %d: %p\n", l++, RouteHandles[k]);

            // Get route information using the route's handle
            Status = RtmGetRouteInfo(...RouteHandles[k]...);

            if (Status == NO_ERROR)
            {
                // Do whatever you want with the route info
                //...

                // Release the route information once you are done
                RtmReleaseRouteInfo(...);
            }
        }

        RtmReleaseRoutes(RtmRegHandle, NumHandles, RouteHandles);
    }
    while (Status == NO_ERROR)

    // Close the enumeration and release its resources
    RtmDeleteEnumHandle(RtmRegHandle, EnumHandle2);
}
```



 

 




