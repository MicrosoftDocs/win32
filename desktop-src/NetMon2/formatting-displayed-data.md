---
description: Network Monitor or your parser DLL can format the data that is displayed in the details pane of the Network Monitor UI.
ms.assetid: 60ab9253-ec0f-4c97-a475-ce2a74d469c4
title: Formatting Displayed Data
ms.topic: article
ms.date: 05/31/2018
---

# Formatting Displayed Data

Network Monitor or your parser DLL can format the data that is displayed in the details pane of the Network Monitor UI.

Network Monitor provides a generic formatter that provides the basic services needed to display most data types that exist within a protocol. However, the generic formatter does not support all data types. For example, the generic formatter does not support the following:

-   Several address types.
-   Source and destination-friendly names.
-   Object identifiers.
-   Large integer data types.
-   Variable length small integer data types.

The following example identifies two formatted strings for the Privilege ID property.

-   The first line of code shows the output of the generic formatter. The output is based on the data type.
-   The second line of code shows the output of a custom formatter with a string to the property data.

``` syntax
Privilege ID (PID) = 0x0029
Privilege ID   (PID) = 0x0029   The Process has privileges
```

> [!Note]  
> When possible, use the generic formatter to display your data because it allows you to control the size of your parser DLL, and provides better cross-platform capabilities for your parser DLL.

 

 

 



