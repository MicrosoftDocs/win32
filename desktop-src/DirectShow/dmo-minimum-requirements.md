---
Description: DMO Minimum Requirements
ms.assetid: cd342f0f-a3dc-4623-a18f-c45071795ef4
title: DMO Minimum Requirements
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMO Minimum Requirements

Every DMO should meet the following minimum requirements:

-   It must support aggregation.
-   It must expose the [**IMediaObject**](/windows/win32/Mediaobj/nn-mediaobj-imediaobject?branch=master) interface.
-   The threading model must be 'both'. DMOs must function correctly in a free-threaded environment.

Audio effect DMOs should support the [**IMediaObjectInPlace**](/windows/win32/Mediaobj/nn-mediaobj-imediaobjectinplace?branch=master) interface, for use in DirectMusic and DirectSound.

The following interfaces are documented elsewhere, but are useful for many DMOs. They are not required, however.

-   **ISpecifyPropertyPages**, **IPropertyPage**: These interfaces enable a DMO to provide a property page, for the user to set properties.
-   **IPersistStream**: This interface enables the DMO to save its state to persistent storage.
-   [**IAMStreamConfig**](/windows/win32/Strmif/nn-strmif-iamstreamconfig?branch=master), [**IAMVideoCompression**](/windows/win32/Strmif/nn-strmif-iamvideocompression?branch=master): These interfaces enable a client to configure an encoder's output format and compression settings. (These two interfaces are part of the DirectShow API, but are also recommended for DMOs.)

## Related topics

<dl> <dt>

[Writing a DMO](writing-a-dmo.md)
</dt> </dl>

 

 



