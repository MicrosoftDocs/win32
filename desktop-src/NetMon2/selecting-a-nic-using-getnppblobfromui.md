---
description: With Network Monitor, selecting a NIC programmatically is a two-step process. First, create the filter BLOB by calling the CreateBlob method. Then, select the NIC by calling the GetNPPBlobFromUI method.
ms.assetid: 0556b20a-307e-4bc3-a986-cfee96a8655d
title: Selecting a NIC Using GetNPPBlobFromUI
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a NIC Using GetNPPBlobFromUI

With Network Monitor, selecting a NIC programmatically is a two-step process. First, create the filter BLOB by calling the [**CreateBlob**](createblob.md) method. Then, select the NIC by calling the [**GetNPPBlobFromUI**](getnppblobfromui.md) method.

In this example a filter BLOB is used to select the required NIC:


```C++
DWORD rc;

// Call CreateBlob to create a filter blob.
///////////////////////////////////////////
HBLOB hFilterBlob;
rc = CreateBlob(&hFilterBlob);
if (FAILED (rc));
{
  // Failed creating filter BLOB. Add appropriate error handling.
}


// Call GetNPPBlobFromUI to retrieve the NPP Blob.
//////////////////////////////////////////////////
rc = GetNPPBlobFromUI(hwnd,
                      hFilterBlob,
                      &hBlob);
if (FAILED (rc));
{
  // Failed retrieving NPP BLOB. Add appropriate error handling.
}
```



 

 



