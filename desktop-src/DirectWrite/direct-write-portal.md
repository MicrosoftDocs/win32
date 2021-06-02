---
title: DirectWrite (DWrite)
description: Today's applications must support high-quality text rendering, resolution-independent outline fonts, and full Unicode text and layout support. DirectWrite, a [DirectX](../directx.md) API, provides these features and more.
ms.assetid: 62a8d723-ae1c-4cbc-a9da-3177e80d4a3a
ms.topic: article
ms.date: 05/31/2018
---

# DirectWrite (DWrite)

## Purpose

Today's applications must support high-quality text rendering, resolution-independent outline fonts, and full Unicode text and layout support. DirectWrite, a [DirectX](../directx.md) API, provides these features and more.

- A device-independent text layout system that improves text readability in documents and in UI.
- High-quality, sub-pixel, [Microsoft ClearType](/typography/cleartype/) text rendering that can use [GDI](interoperating-with-gdi.md), [Direct2D](rendering-by-using-direct2d.md), or application-specific rendering technology.
- Hardware-accelerated text, when used with [Direct2D](rendering-by-using-direct2d.md).
- Support for multi-format text.
- Support for the advanced typography features of OpenType fonts.
- Support for the layout and rendering of text in all supported languages.
- [GDI](interoperating-with-gdi.md)-compatible layout and rendering.

The API supports measuring, drawing, and hit-testing of multi-format text. DirectWrite handles text in all supported languages for global and localized applications, building on the key language infrastructure found in Windows 7. DirectWrite also provides a low-level glyph rendering API for developers who want to perform their own layout and Unicode-to-glyph processing.

> [!NOTE]
> [Project Reunion](/windows/apps/project-reunion/) introduces a new version of DirectWrite&mdash;called DWriteCore&mdash;that runs on versions of Windows down to Windows 8, and opens the door for you to use it cross-platform. For more details, see [DWriteCore overview](dwritecore-overview.md).

## Run-time requirements

- Windows 7 or Windows Vista with Service Pack 2 (SP2) and Platform Update for Windows Vista
- Windows Server 2008 R2 or Windows Server 2008 with Service Pack 2 (SP2) and Platform Update for Windows Server 2008

## In this section

| Topic | Description |
|-|-|
| [What's new in DirectWrite](what-s-new-in-directwrite-for-windows-8-consumer-preview.md)<br/> | Here are some of the new additions to DirectWrite. <br/> |
| [Programming Guide](programming-guide.md)<br/> | The following topics provide an overview of the DirectWrite API.<br/> |
| [API Reference](reference.md)<br/> | Describes the DirectWrite API.<br/> |
| [Sample Code](samples.md)<br/> | This section contains information about sample programs for DirectWrite.<br/> |
