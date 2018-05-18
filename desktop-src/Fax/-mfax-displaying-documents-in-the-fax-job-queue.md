---
Description: 'This topic describes how to display documents in the fax job queue in the Microsoft Win32 environment.'
ms.assetid: 'afd808c9-a402-444f-9167-1864337a30e4'
title: Displaying Documents in the Fax Job Queue
---

# Displaying Documents in the Fax Job Queue

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

An application can call the [**FaxGetPageData**](-mfax-faxgetpagedata.md) function for administrative purposes, to display a thumbnail sketch of a fax document in the fax queue. The function returns the first page of data for a fax job in the Tagged Image File Format Class F (TIFF Class F). The calling application must decode the data stream.

Call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate the resources allocated by the [**FaxGetPageData**](-mfax-faxgetpagedata.md) function.

For more information about TIFF Class F files, see [Fax Image Format](-mfax-fax-image-format.md).

 

 



