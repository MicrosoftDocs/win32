---
title: IAVIStream and IAVIFile Interfaces
description: IAVIStream and IAVIFile Interfaces
ms.assetid: 3ab602da-239f-44ff-b43d-e0c380619d99
keywords:
- IAVIStream interface
- IAVIFile interface
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IAVIStream and IAVIFile Interfaces

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**IAVIStream**](/windows/desktop/api/Vfw/nn-vfw-iavistream) and [**IAVIFile**](/windows/desktop/api/Vfw/nn-vfw-iavifile) interfaces contain the methods used by file and stream handlers. The **PAVISTREAM** data type is a pointer to an AVI stream object (through the **IAVIStream** interface) and the **PAVIFILE** data type is a pointer to an AVI file object (through the **IAVIFile** interface).

To create an object pointer in C, first allocate space for a structure that is large enough to contain the pointer to the virtual function table and the other data members. Create a virtual function table for the methods for your type of stream, then set the pointer to the virtual function table to the address of the virtual function table.

 

 




