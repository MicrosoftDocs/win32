---
description: Tape Location Search
ms.assetid: 17fb4eba-4b2c-41c2-94e2-e58586f92e53
title: Tape Location Search
ms.topic: article
ms.date: 05/31/2018
---

# Tape Location Search

Although DV devices support a command to search by time code or by absolute track number (ATN), the MSDV driver does not have a standard, device-independent way to access these functions. The only option is to send a raw AV/C command to the driver as described in the topic [Issuing Raw AV/C Commands](issuing-raw-av-c-commands.md).

The UVC driver supports a property set for tape location searches. To send a search command, use the **IKsControl** interface and set the PROPSETID\_EXT\_TRANSPORT property. Using a property set is safer than sending raw AV/C commands to the device, because AV/C commands bypass the filter and go directly to the device driver.

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> <dt>

[External Device Transport Property Set](external-device-transport-property-set.md)
</dt> </dl>

 

 



