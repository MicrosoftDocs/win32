---
description: Of the six predefined mapping modes, one is device dependent (MM\_TEXT) and the remaining five (MM\_HIENGLISH, MM\_LOENGLISH, MM\_HIMETRIC, MM\_LOMETRIC, and MM\_TWIPS) are device independent.
ms.assetid: 722df020-edf2-4763-b58c-3e29fa7007db
title: Predefined Mapping Modes
ms.topic: article
ms.date: 05/31/2018
---

# Predefined Mapping Modes

Of the six predefined mapping modes, one is device dependent (MM\_TEXT) and the remaining five (MM\_HIENGLISH, MM\_LOENGLISH, MM\_HIMETRIC, MM\_LOMETRIC, and MM\_TWIPS) are device independent.

The default mapping mode is MM\_TEXT. One logical unit equals one pixel. Positive x is to the right, and positive y is down. This mode maps directly to the device's coordinate system. The logical-to-physical mapping involves only an offset in x and y that is defined by the application-controlled window and viewport origins. The viewport and window extents are all set to 1, creating a one-to-one mapping.

Applications that display geometric shapes (circles, squares, polygons, and so on) make use of one of the device-independent mapping modes. For example, if you are writing an application to provide charting capabilities for a spreadsheet program and want to guarantee that the diameter of each pie chart is 2 inches, use the MM\_LOENGLISH mapping mode and call the appropriate functions to draw and fill the chart. Specifying MM\_LOENGLISH, guarantees that the diameter of the chart is consistent on any display or printer. If MM\_TEXT is used instead of MM\_LOENGLISH, a chart that appears circular on a VGA display would appear elliptical on an EGA display and would appear very small on a 300 dpi (dots per inch) laser printer.

 

 



