---
Description: Quality Messages
ms.assetid: ff98cb51-6300-470d-b696-5e27591c6b3f
title: Quality Messages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Quality Messages

Quality messages are defined with the [**Quality**](/windows/win32/strmif/ns-strmif-tagquality?branch=master) structure. This structure contains the following members:

-   **Type:** Defined by the [**QualityMessageType**](/windows/win32/strmif/ne-strmif-tagqualitymessagetype?branch=master) enumeration; either Famine, indicating that the filter is receiving too little data, or Flood, indicating that the filter is receiving too much data.
-   **Proportion:** The requested adjustment in the data rate, from a baseline of 1000. For example, 750 indicates 75% and 1500 indicates 150%.
-   **Late:** Reference time indicating how late the most recent sample arrived. The value is negative if the sample arrived early.
-   **TimeStamp:** The time stamp on the most recent sample.

For example, suppose that a sample with a time stamp of 240 milliseconds (ms) reaches the renderer at 280 ms, stream time. The renderer creates a quality message of type Famine. The sample arrived 40 ms late, so the **Late** member is 400000. (All reference times are in 100-nanosecond units.) The **TimeStamp** member is 2400000.

For the **Proportion** member, the renderer might use a running average to calculate the value. Perhaps samples have been arriving on time, and this sample is an anomaly. In that case the renderer might request only a small correction. On the other hand, if samples are consistently late, the renderer might request a larger correction.

Quality control is handled through the [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master) interface. It contains two methods.

-   [**Notify**](/windows/win32/Strmif/nf-strmif-iqualitycontrol-notify?branch=master): Sends a quality message.
-   [**SetSink**](/windows/win32/Strmif/nf-strmif-iqualitycontrol-setsink?branch=master): Specifies a custom quality manager.

An object that implements **IQualityControl** receives quality messages through its **Notify** method. It can either handle the message or pass the message to another object. If the application calls the object's **SetSink** method, the object should delegate quality control to the specified quality manager.

 

 



