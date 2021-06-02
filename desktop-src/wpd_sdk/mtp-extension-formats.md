---
description: MTP Extension Formats
ms.assetid: 318b7267-f4ba-43ad-aa24-8cfacf056558
title: MTP Extension Formats
ms.topic: article
ms.date: 05/31/2018
---

# MTP Extension Formats

The format of a file on a device can be described by a GUID value. This value is specified by the WPD\_OBJECT\_FORMAT property.

## Vendor-Extended Formats

When a device manufacturer supports a vendor-extended format, their driver combines the vendor's format code (UINT16) with the highest 16 bits of the **WPD\_OBJECT\_FORMAT\_UNSPECIFIED** GUID.

For example, if the vendor-extended code is 0xB001, the resulting GUID would be as shown in the following example:


```C++
{B0010000-AE6C-4804-98BA-C57B46965FE7}
```



## Related topics

<dl> <dt>

[Supporting MTP Extensions](supporting-mtp-extensions.md)
</dt> </dl>

 

 



