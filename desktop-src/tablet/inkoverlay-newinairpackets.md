---
description: InkOverlay.NewInAirPackets event - Occurs when an in-air packet is seen.
ms.assetid: 10dc1909-bfbc-4ea0-b77a-e33149205107
title: InkOverlay.NewInAirPackets event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkOverlay.NewInAirPackets event

Occurs when an in-air packet is seen.

## Syntax


```C++
void NewInAirPackets(
  [in]      IInkCursor *Cursor,
  [in]      long       PacketCount,
  [in, out] VARIANT    *PacketData
);
```



## Parameters

<dl> <dt>

*Cursor* \[in\]
</dt> <dd>

The [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object that generated the [**NewInAirPackets**](inkcollector-newinairpackets.md) event.

</dd> <dt>

*PacketCount* \[in\]
</dt> <dd>

The number of in-air packets received.

</dd> <dt>

*PacketData* \[in, out\]
</dt> <dd>

An array that contains the selected data for the packet.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

An in-air packet is created when a user moves a pen near the tablet and the cursor is within the ink collector object's window or the user moves a mouse within the ink collector object's associated window. [**NewInAirPackets**](inkcollector-newinairpackets.md) events are generated rapidly, and the event handler must be fast or performance suffers.

This event method is defined in the \_IInkCollectorEvents, \_IInkOverlayEvents, and \_IInkPictureEvents dispatch-only interfaces (dispinterfaces) with an ID of DISPID\_ICENewInAirPackets.

The [**NewInAirPackets**](inkcollector-newinairpackets.md) event is fired even when in select or erase mode, not just when inserting ink. This requires that you monitor the editing mode (which you are responsible for setting) and be aware of the mode before interpreting the event. The advantage of this requirement is greater freedom to innovate on the platform through greater awareness of platform events.

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

[**InkOverlay Class**](inkoverlay-class.md)
</dt> <dt>

[**DesiredPacketDescription Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_desiredpacketdescription)
</dt> <dt>

[**NewPackets Event**](inkcollector-newpackets.md)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> </dl>

 

 




