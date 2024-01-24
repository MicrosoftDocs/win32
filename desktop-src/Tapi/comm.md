---
description: The comm device class consists of communications ports. You access these devices by using the file and communications functions.
ms.assetid: c1cf4998-b752-4cfd-9dd7-c9872b62c44b
title: comm
ms.topic: article
ms.date: 05/31/2018
---

# comm

The comm device class consists of communications ports. You access these devices by using the [file](/windows/desktop/FileIO/file-management-functions) and [communications functions](/windows/desktop/DevIO/communications-functions).

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_ASCII value and appending a null-terminated string that specifies the name of the communication device (such as the modem name).

 

 
