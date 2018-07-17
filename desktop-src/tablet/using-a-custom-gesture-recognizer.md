---
Description: You can use a custom gesture recognizer independently, or in addition to the GestureRecognizer.Create your custom gesture recognizer as an IStylusSyncPlugin, have it create CustomStylusData, and include the plug-in in the same StylusSyncPluginCollection as the GestureRecognizer. In the IStylusSyncPlugin, combine gesture notifications from both recognizers into notifications to be consumed by an application.
ms.assetid: ed4e8f56-9137-47fd-a8f9-17eebfd06e97
title: Using a Custom Gesture Recognizer
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using a Custom Gesture Recognizer

You can use a custom gesture recognizer independently, or in addition to the [**GestureRecognizer**](gesturerecognizer-class.md).

Create your custom gesture recognizer as an [**IStylusSyncPlugin**](https://msdn.microsoft.com/en-us/library/ms704312(v=VS.85).aspx), have it create [CustomStylusData](frlrfMicrosoftStylusInputPluginDataCustomStylusDataClassTopic), and include the plug-in in the same [StylusSyncPluginCollection](frlrfMicrosoftStylusInputStylusSyncPluginCollectionClassTopic) as the [**GestureRecognizer**](gesturerecognizer-class.md). In the **IStylusSyncPlugin**, combine gesture notifications from both recognizers into notifications to be consumed by an application.

## Related topics

<dl> <dt>

[Accessing and Manipulating Stylus Input](accessing-and-manipulating-stylus-input.md)
</dt> </dl>

 

 



