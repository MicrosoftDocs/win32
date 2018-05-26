---
Description: The default behavior for the InkEdit control is to recognize and convert ink into text after a brief timeout has expired.
ms.assetid: d141bcec-e9a8-48b8-86cf-9476a2cc6f9f
title: Displaying Ink as Ink
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Displaying Ink as Ink

The default behavior for the [InkEdit](inkedit-control-reference.md) control is to recognize and convert ink into text after a brief timeout has expired. Because the control is a superclass of [RichEdit](_win32_Rich_Edit_Controls), it is also possible to embed and display ink within the control. Each word is inserted into the control as an [**InkDisp**](/windows/win32/msinkaut/?branch=master) object. The **InkDisp** object contains the ink and its recognition alternates.

When inserted, the ink is scaled to the current font size and other ambient properties, such as italics or bold, are applied. If the user chooses to edit the text of an [**InkDisp**](/windows/win32/msinkaut/?branch=master) object, he or she must first convert the ink to text.

> [!Note]  
> All ink and recognition alternate data is lost during the conversion.

 

This feature is available only on computers that run Microsoft Windows XP Tablet PC Edition, Windows Vista, or later.

 

 



