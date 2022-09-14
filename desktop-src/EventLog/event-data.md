---
description: Each event can have event-specific data associated with it.
ms.assetid: fa2f9e71-44c3-4569-bde4-24112a756664
title: Event Data
ms.topic: article
ms.date: 05/31/2018
---

# Event Data

Each event can have event-specific data associated with it. The Event Viewer does not interpret this data; it displays extra data only in a combined hexadecimal and text format. The maximum limit on the size of an event in the even log is 0x3FFFF bytes. Therefore, use event-specific data sparingly, including it only if you are sure it will be useful to someone debugging a problem. For example, many network-related events include network control blocks (NCB) as event-specific data.

When you use event-specific data, the last part of its description string should provide a note about the information provided as event-specific data. For example, the network software could provide a note such as: "(The NCB is the event data.)" As a convention, use parentheses around such remarks, as indicated in this example.

You can also use event-specific data to store information the application can process independently of the Event Viewer. For example, you could write a viewer specifically for your events, or write a program that scans the log and creates a report that includes information from the event-specific data.

 

 



