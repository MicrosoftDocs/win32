---
title: Access the Opaque Pointer in a Destination
description: The following sample code shows how to access the opaque pointer in a destination.
ms.assetid: 9bf420a1-2d9b-4be9-bd96-c92023b0ed41
ms.topic: article
ms.date: 05/31/2018
---

# Access the Opaque Pointer in a Destination

The following sample code shows how to access the opaque pointer in a destination.


```C++
// Opaque Info Blob Defn

typedef struct _OPAQUE_INFO
{
    ULONG  Info1;
    ULONG  Info2;
}
OPAQUE_INFO, *POPAQUE_INFO;

PVOID        OpaqueInfoSlotPointer;  // Pointer to the opaque pointer slot
PVOID        OpaqueInfoSlotInfo;     // Information in the opaque pointer slot
POPAQUE_INFO OpaqueInfoPtr;          // Pointer to opaque information
DWORD Status;

// Lock the destination in exclusive mode to sync opaque pointer access
// If you know that you will only be reading the opaque pointer
// and not modifying it, then you can use a shared lock

Status = RtmLockDestination(RtmRegHandle, DestHandle, TRUE, TRUE);

if (Status != NO_ERROR)
{
   return Status;
}

// You can get a pointer to your opaque pointer slot,
// assuming that you have reserved one during registration.

Status = RtmGetOpaqueInformationPointer(RtmRegHandle,
                                        DestHandle,
                                        &OpaqueInfoSlotPointer);
if (Status == NO_ERROR)
{
    OpaqueInfoSlotInfo = * (PVOID *) OpaqueInfoSlotPointer;

    if (OpaqueInfoSlotInfo == NULL)
    {
        // No information set yet - create private information BLOB (if required)
        OpaqueInfoPtr = (POPAQUE_INFO) malloc(OpaqueInfoSize);

        if (OpaqueInfoPtr)
        {
            // Set certain information in the opaque information BLOB
            OpaqueInfoPtr->Info1 = 1;
            OpaqueInfoPtr->Info2 = 2;

            * (PVOID *) OpaqueInfoSlotPointer = OpaqueInfoPtr;
        }
        else
        {
            // Already exists; do something with the opaque information
            OpaqueInfoPtr = (POPAQUE_INFO) OpaqueInfoSlotInfo;

            // Set certain information in the opaque information BLOB
            OpaqueInfoPtr->Info1 = 3;
            OpaqueInfoPtr->Info2 = 4;       
        }
    }
}

// Unlock destination from exclusive mode that we locked earlier
Status = RtmLockDestination(RtmRegHandle, DestHandle, TRUE, FALSE);

ASSERT(Status == NO_ERROR);
```



 

 




