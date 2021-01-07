---
description: This topic describes how to render the program data to be printed.
ms.assetid: D1343C53-6F13-49FF-8C7C-25D5A3C31B22
title: 'How To: Render Print Job Data'
ms.topic: article
ms.date: 05/31/2018
---

# How To: Render Print Job Data

This topic describes how to render the program data to be printed. This topic does not explain in detail about how to render specific graphics or text images. Instead, it describes how to manage the program data and render it as an XPS document, which it sends to a printer by using the [XPS Print API](xps-printing.md).

## Overview

Rendering print job data for printing involves taking the program-specific data, such as text, images, and formatting, and converting them into a format that is compatible with the destination printer. The program that sends the data to the printer must send it in the format that the printer driver requires.

Use the [XPS Print API](xps-printing.md) to send the data to the printer and it requires the data to be formatted as an XPS document. To produce the XPS document content that the XPS Print API needs, the sample program uses the [XPS Document API](/previous-versions/windows/desktop/dd316976(v=vs.85)).

If the program content is in a format that is not compatible with a printer, it will need to be rendered before it is sent to the printer. If the program uses the [XPS Document API](/previous-versions/windows/desktop/dd316976(v=vs.85)) to manage its program content, the program content will be in a format that can be sent directly to the [XPS Print API](xps-printing.md) and will not require any additional rendering before you send it to the printer.

## Related topics

<dl> <dt>

[XPS Document API](/previous-versions/windows/desktop/dd316976(v=vs.85))
</dt> <dt>

[XPS Print API](xps-printing.md)
</dt> </dl>

 

 
