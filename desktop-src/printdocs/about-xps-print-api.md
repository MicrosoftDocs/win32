---
description: The XPS&\#160;Print&\#160;API provides an interface to the print spooler that applications can use to print jobs that send XPS documents to a printer.
ms.assetid: d3bf7b1d-df21-4e7b-803b-45b65d46b2ca
title: About the XPS Print API
ms.topic: article
ms.date: 05/31/2018
---

# About the XPS Print API

The [XPS Print API](xps-printing.md) provides an interface to the print spooler that applications can use to print jobs that send XPS documents to a printer.

If the destination printer uses an XPSDrv printer driver, the XPS Print API makes it possible for the XPSDrv printer driver to receive document events as the print spooler processes a print job. For a description of the document events that are sent to the XPSDrv printer driver see [XPS Driver Document Events](/windows-hardware/drivers/print/xps-driver-document-events).

If the destination printer uses a GDI printer driver, the [XPS Print API](xps-printing.md) lets the system handle the necessary conversion of the print job data from XPS format to the Enhanced Metafile (EMF) format that the GDI printer driver uses. For a description of the GDI printer driver document events see [DocumentEvent Function](documentevent.md).

## Related topics

<dl> <dt>

[Using the XPS Print API](using-the-xps-print-api.md)
</dt> <dt>

[XPS Print API Reference](xpsprint-api.md)
</dt> </dl>

 

 
