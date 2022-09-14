---
description: InkCollector.NewPackets event - Occurs when the ink collector receives a packet.
ms.assetid: 2682e7ba-dabd-497e-aea4-6d3f837f4f10
title: InkCollector.NewPackets event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkCollector.NewPackets event

Occurs when the ink collector receives a packet.

## Syntax


```C++
void NewPackets(
  [in]      IInkCursor     *Cursor,
  [in]      IInkStrokeDisp *Stroke,
  [in]      long           PacketCount,
  [in, out] VARIANT        *PacketData
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the [**NewInAirPackets**](inkcollector-newinairpackets.md) event.

</dd> <dt>

*Stroke* \[in\]
</dt> <dd>

Specifies the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object.

</dd> <dt>

*PacketCount* \[in\]
</dt> <dd>

The number of packets received for a [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object.

</dd> <dt>

*PacketData* \[in, out\]
</dt> <dd>

When this method returns, contains an array that contains the selected data for the packet.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Packets are received while a stroke is being collected. Packet events occur rapidly, and a **NewPackets** event handler must be fast or performance suffers.

TThis event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICENewPackets.

This event should be used carefully as it could have an adverse effect on ink performance if too much code is executed in the event handlers.

To set which properties are contained in this array, use the [**DesiredPacketDescription**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_desiredpacketdescription) property of the ink collector object. The array that the *PacketData* parameter returns contains the data for those properties.

> [!Note]  
> Although you can modify the packet data, these modifications are not persisted or used.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkCollector Class**](inkcollector-class.md)
</dt> <dt>

[**NewInAirPackets Event**](inkcollector-newinairpackets.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> <dt>

[**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp)
</dt> </dl>

 

 




