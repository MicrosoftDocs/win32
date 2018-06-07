---
Description: This section contains reference topics for the Evntrace.h header.
ms.assetid: E0DCFAB0-8E12-4B6E-90C5-88B25EBDFA4C
title: Evntrace.h
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Evntrace.h

This section contains reference topics for the Evntrace.h header.

## In this section



| Topic                                                         | Description                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EVENT\_TRACE\_HEADER**](event-trace-header.md)<br/> | The **EVENT\_TRACE\_HEADER** structure is used to pass a WMI event to the WMI event logger. It is overlaid on the [**WNODE\_HEADER**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-_wnode_header) portion of the [**WNODE\_EVENT\_ITEM**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-tagwnode_event_item) passed to [**IoWMIWriteEvent**](/windows-hardware/drivers/ddi/content/Wdm/nf-wdm-iowmiwriteevent). Information contained in the **EVENT\_TRACE\_HEADER** is written to the WMI log file.<br/> |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Evntrace.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




