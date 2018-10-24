---
Description: The comm device class consists of communications ports. You access these devices by using the file and communications functions.
ms.assetid: c1cf4998-b752-4cfd-9dd7-c9872b62c44b
title: comm
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# comm

The comm device class consists of communications ports. You access these devices by using the [file](https://msdn.microsoft.com/library/windows/desktop/aa364232) and [communications functions](https://msdn.microsoft.com/library/windows/desktop/aa363194).

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring_tag) structure, setting the **dwStringFormat** member to the STRINGFORMAT\_ASCII value and appending a null-terminated string that specifies the name of the communication device (such as the modem name).

 

 



