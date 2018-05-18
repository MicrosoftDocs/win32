---
title: Use a Client-Specific Route List
description: The following procedures outlines the steps to use the client-specific route lists. The sample code that follows shows how to implement the procedure.
ms.assetid: 'aa9b7b2a-259f-4ce1-afb6-c04875e8ffe3'
---

# Use a Client-Specific Route List

The following procedures outlines the steps to use the client-specific route lists. The sample code that follows shows how to implement the procedure.

**To use this feature, a client should take the following steps**

1.  Call [**RtmCreateRouteList**](rtmcreateroutelist.md) to obtain a handle from the routing table manager.
2.  Call [**RtmInsertInRouteList**](rtminsertinroutelist.md) whenever the client must add a route to this list.
3.  When the client no longer requires the list, it should call [**RtmDeleteRouteList**](rtmdeleteroutelist.md) to remove the list.

**If the client must enumerate the routes on the list, the client should take the following steps**

1.  Call [**RtmCreateRouteListEnum**](rtmcreateroutelistenum.md) to obtain an enumeration handle from the routing table manager.
2.  Call [**RtmGetListEnumRoutes**](rtmgetlistenumroutes.md) to obtain the handles to the routes in the list.
3.  Call [**RtmReleaseRoutes**](rtmreleaseroutes.md) to release the handles when no longer required.

The following sample code shows how to create and use a client-specific route list.


```C++
HANDLE RouteListHandle1;
HANDLE RouteListHandle2;

// Create two entity-specific lists to add routes to

Status = RtmCreateRouteList(RtmRegHandle,
                            &amp;RouteListHandle1);
// Check Status
//...

Status = RtmCreateRouteList(RtmRegHandle,
                            &amp;RouteListHandle2);
// Check Status
//...

// Assume you have added a bunch of routes
// by calling RtmAddRouteToDest many times
// with 'RouteListHandle1' specified similar to
// Status = RtmAddRouteToDest(RtmRegHandle,
//                            ...
//                            RouteListHandle1,
//                            ...
//                            &amp;ChangeFlags);

// Enumerate routes in RouteListHandle1 list

// Create an enumeration on the route list

Status = RtmCreateRouteListEnum(RtmRegHandle,
                                RouteListHandle1,
                                &amp;EnumHandle);

if (Status == NO_ERROR)
{
        // Allocate space on the top of the stack
        
    MaxHandles = RegnProfile.MaxHandlesInEnum;

    RouteHandles = _alloca(MaxHandles * sizeof(HANDLE));

    // Note how the termination condition is different
    // from other enumerations - the call to the function
    // RtmGetListEnumRoutes always returns NO_ERROR
    // Quit when you get fewer handles than requested
    
    do
    {
                // Get next set of routes from the list enumeration
        
        NumHandles = MaxHandles;

        Status = RtmGetListEnumRoutes(RtmRegHandle,
                                      EnumHandle,
                                      &amp;NumHandles,
                                      RouteHandles);

        for (i = 0; i < NumHandles; i++)
        {
            Print("Route Handle %5lu: %p\n", i, RouteHandles[i]);
        }

        // Move all these routes to another route list
        // They are automatically removed from the old one
        
        Status = RtmInsertInRouteList(RtmRegHandle,
                                      RouteListHandle2,
                                      NumHandles,
                                      RouteHandles);
        // Check Status...
        
                // Release the routes that have been enumerated
        
        RtmReleaseRoutes(RtmRegHandle, NumHandles, RouteHandles);
    }
    while (NumHandles == MaxHandles);

    RtmDeleteEnumHandle(RtmRegHandle, EnumHandle);
}

// Destroy all the entity-specific route lists 
// after removing all routes from these lists;
// the routes themselves are not deleted

Status = RtmDeleteRouteList(RtmRegHandle, RouteListHandle1);
ASSERT(Status == NO_ERROR);


Status = RtmDeleteRouteList(RtmRegHandle, RouteListHandle2);
ASSERT(Status == NO_ERROR);
```



 

 




