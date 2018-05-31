---
title: Controlling Playback
description: Controlling Playback
ms.assetid: 17384658-77f0-4e64-9e80-8e18571e9b59
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Playback

This topic applies to Windows XP Service Pack 1 or later.

In general, the **MSVidCtl** object controls the larger tasks, such as acquiring the DVD player, handling display, and controlling the graph, while the **MSVidWebDVD** object typically handles specific DVD control, such as disc navigation and playback. However, certain methods exist in both objects. Such methods should only be accessed through the **MSVidCtl** object. Accessing these duplicate methods using the **MSVidWebDVD** object will cause an error:

-   **View**
-   **Stop**
-   **Run**
-   **Pause**

Playback speed, on the other hand, is controlled using the **Rate** property on the **MSVidWebDVD** object.

Because DVD authoring design is not enforced, you may find that your application will not work perfectly with all discs. For example, some discs have a single title that holds a complete movie made of chapters, while others may have a single movie broken across several titles. Discs are designed to work specifically with their own menu screens, not to make navigation or control easy for the Video Control. However, most **MSVidWebDVD** actions, such as navigating through titles, chapters, menu buttons, or screens, will work with most discs.

In addition, you cannot depend on a DVD to include text strings or parental levels appropriately, it is not possible to determine programmatically if a method or property can be used at any particular time, and there can be a lag between UOP setting changes and UOP messages. Therefore, rigorous error trapping is essential to designing a robust application. Ideally, applications will derive the most benefit from using the **MSVidWebDVD** object with custom-designed DVDs, such as educational or reference discs, where you can predict or control the disc design. For these discs, **MSVidWebDVD** presents a simple-to-use, full-featured object that allows you to quickly and easily design a complex interface for your DVDs.

## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




