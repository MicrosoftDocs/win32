---
title: How-to Topics (DirectWrite)
description: The following topics provide an overview of the DirectWrite API.
ms.assetid: da4817ee-0bff-433f-b595-4250199bcc14
ms.topic: article
ms.date: 05/31/2018
---

# How-to Topics (DirectWrite)

The following topics provide an overview of the [DirectWrite](direct-write-portal.md) API.

## In this section



| Topic                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [How to Align Text](how-to-align-text.md)<br/>                                                                                                                   | You can align [DirectWrite](direct-write-portal.md) text by using the [**SetTextAlignment**](/windows/win32/api/dwrite/nf-dwrite-idwritetextformat-settextalignment) method of the [**IDWriteTextFormat**](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) interface<br/>                                                                                                                                                                                                               |
| [How to Add Support for Multiple Monitors](how-to-add-support-for-multiple-monitors.md)<br/>                                                                     | [DirectWrite](direct-write-portal.md) includes support for systems with multiple monitors. Different monitors may have different pixel geometry (RGB, BGR, or FLAT) or other attributes. For more information about pixel geometry, see the [**DWRITE\_PIXEL\_GEOMETRY**](/windows/win32/api/dwrite/ne-dwrite-dwrite_pixel_geometry) reference topic. This topic will show you how to add support for multiple monitors to your DirectWrite application. <br/> |
| [How to Ensure That Your Application Displays Properly on High-DPI Displays](how-to-ensure-that-your-application-displays-properly-on-high-dpi-displays.md)<br/> | Describes how to create a window the displays properly on high-DPI displays.<br/>                                                                                                                                                                                                                                                                                                                                               |
| [How to Ensure Text is Displayed with the Correct Reading Direction](how-to-ensure-text-is-displayed-with-the-correct-reading-direction.md)<br/>                 | Some languages, such as Arabic and Hebrew, require a right-to-left reading direction. The for a [DirectWrite](direct-write-portal.md) text format object, the default reading direction is left-to-right. DirectWrite does not automatically infer the reading direction from the locale, so you must do this yourself.<br/>                                                                                                   |
| [How to Enumerate Fonts](font-enumeration.md)<br/>                                                                                                               | This overview will show how to enumerate the fonts in the system font collection, by family name.<br/>                                                                                                                                                                                                                                                                                                                          |
| [How to Perform Hit Testing on a Text Layout](how-to-perform-hit-testing-on-a-text-layout.md)<br/>                                                               | Provides a short tutorial about how to add hit testing to a [DirectWrite](direct-write-portal.md) application that displays text by using the [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) interface. <br/>                                                                                                                                                                                                                  |
| [How to Add Inline Objects to a Text Layout](how-to-add-inline-objects-to-a-text-layout.md)<br/>                                                                 | Provides a short tutorial on adding inline objects to a [DirectWrite](direct-write-portal.md) application that displays text using the [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) interface. <br/>                                                                                                                                                                                                                         |
| [How to Add Client Drawing Effects to a Text Layout](how-to-add-custom-drawing-efffects-to-a-text-layout.md)<br/>                                                | Provides a short tutorial on adding client drawing effects to a [DirectWrite](direct-write-portal.md) application that displays text using the [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) interface and a custom text renderer. <br/>                                                                                                                                                                                      |



 

 

