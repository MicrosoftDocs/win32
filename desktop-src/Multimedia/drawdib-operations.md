---
title: DrawDib Operations
description: DrawDib Operations
ms.assetid: 785ad42e-0c77-44a4-b4ef-be2a0ee2b563
keywords:
- DrawDib,about
- DrawDib,accessing
- DrawDib,opening
- DrawDib,operations
- DrawDib,device context (DC)
- DC (device context)
- DrawDibOpen function
- DrawDibClose function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DrawDib Operations

\[The feature associated with this page, [DrawDib](/windows/win32/multimedia/drawdib), is a legacy feature. It has been superseded by [MediaComposition class](/uwp/api/Windows.Media.Editing.MediaComposition). **MediaComposition class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaComposition class** instead of **DrawDib**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can access the entire group of DrawDib functions by using the [**DrawDibOpen**](/windows/desktop/api/Vfw/nf-vfw-drawdibopen) function. This function loads the dynamic-link library (DLL), allocates memory resources, creates a DrawDib device context (DC), and maintains a reference count of the number of DCs that are initialized. **DrawDibOpen** also returns a handle of the new DC that you use with the other DrawDib functions.

You can release a DrawDib DC when you finish using it by using the [**DrawDibClose**](/windows/desktop/api/Vfw/nf-vfw-drawdibclose) function. **DrawDibClose** also decrements the reference count of the applications accessing the DLL. The call to **DrawDibClose** should be the last DrawDib function in your application.

You can create as many DrawDib DCs as you want. You can use multiple DrawDib DCs to draw several bitmaps simultaneously. You can also create multiple DrawDib DCs, each with unique characteristics, so your application can choose and then use the DC with the most appropriate settings. For example, you can create two DrawDib DCs in an application: one that displays an image at its normal resolution, and the other that displays an enlarged portion of the image.

To run efficiently, DrawDib functions require information about the display adapter and its driver. The display profile is obtained by running a series of tests on the display adapter the first time the DLL containing the DrawDib functions is accessed. The DrawDib functions use this information for all applications. You can repeat these tests when necessary by using the [**DrawDibProfileDisplay**](/windows/desktop/api/Vfw/nf-vfw-drawdibprofiledisplay) function.

> [!Note]  
> Retrieving and storing the display profile is typically a one-time occurrence. If, however, the profile information is deleted or another display driver is installed in the system, DrawDib reruns the tests.

 

## Related topics

<dl> <dt>

[About the DrawDib Functions](about-the-drawdib-functions.md)
</dt> </dl>

 

 




