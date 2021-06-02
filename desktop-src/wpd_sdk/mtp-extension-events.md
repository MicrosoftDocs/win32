---
description: MTP Extension Events
ms.assetid: c04554cd-d68d-455e-afa3-29d4186dad65
title: MTP Extension Events
ms.topic: article
ms.date: 05/31/2018
---

# MTP Extension Events

Events notify an application that changes have occurred on, or with, a device. For example, an application can register to receive notfications that a device has been removed .

## Vendor-Extended Event Codes

When a device manufacturer supports a vendor-extended event, their driver combines the vendor's event code (UINT16) with the highest 16 bits of the **WPD\_EVENT\_MTP\_VENDOR\_EXTENDED\_EVENTS** GUID.

For example, if the vendor-extended code is 0xC001, the resulting GUID would be as shown in the following example:


```C++
{C0010000-5738-4ff2-8445-BE3126691059}
```



## Vendor-Extended Event Parameters

The parameters for a vendor-extended event are reported by the **WPD\_EVENT\_PARAMETER\_EVENT\_ID** GUID and the **WPD\_PROPERTY\_MTP\_EXT\_EVENT\_PARAMS**, which is a collection of **PROPVARIANTS**. These **PROPVARIANTS** correspond to the event parameters. If there are no parameters, this collection is empty.


```C++
{C0010000-5738-4ff2-8445-BE3126691059}
```



## Related topics

<dl> <dt>

[Supporting MTP Extensions](supporting-mtp-extensions.md)
</dt> </dl>

 

 



