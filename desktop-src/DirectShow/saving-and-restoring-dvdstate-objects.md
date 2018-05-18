---
Description: Saving and Restoring DvdState Objects
ms.assetid: '65180fe2-0faf-47c0-bccd-728e01056c46'
title: Saving and Restoring DvdState Objects
---

# Saving and Restoring DvdState Objects

[**IDvdState**](idvdstate.md) objects enable applications to save a snapshot of the user session, including information such as the current location on the disc, the parental level of the person who is viewing, the selected audio and subpicture streams, and so on. This means that users can save their place on a DVD-Video disc and watch it at a later time.

Applications cannot create DvdState objects. These objects are created internally by the DVD Navigator when an application calls [**IDvdInfo2::GetState**](idvdinfo2-getstate.md). DvdState objects expose the [**IDvdState**](idvdstate.md) interface to allow applications to query for certain information.

In the DVD sample application, the **CDvdCore::RestoreBookmark** and **CDvdCore::SaveBookmark** functions show how to save and retrieve DvdState objects.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



