---
title: IAVIStream and IAVIFile Interfaces
description: IAVIStream and IAVIFile Interfaces
ms.assetid: 3ab602da-239f-44ff-b43d-e0c380619d99
keywords:
- IAVIStream interface
- IAVIFile interface
ms.topic: article
ms.date: 05/31/2018
---

# IAVIStream and IAVIFile Interfaces

The [**IAVIStream**](/windows/desktop/api/Vfw/nn-vfw-iavistream) and [**IAVIFile**](/windows/desktop/api/Vfw/nn-vfw-iavifile) interfaces contain the methods used by file and stream handlers. The **PAVISTREAM** data type is a pointer to an AVI stream object (through the **IAVIStream** interface) and the **PAVIFILE** data type is a pointer to an AVI file object (through the **IAVIFile** interface).

To create an object pointer in C, first allocate space for a structure that is large enough to contain the pointer to the virtual function table and the other data members. Create a virtual function table for the methods for your type of stream, then set the pointer to the virtual function table to the address of the virtual function table.

 

 




