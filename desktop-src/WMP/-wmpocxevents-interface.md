---
title: '_WMPOCXEvents Interface (Wmp.h)'
description: The \_WMPOCXEvents interface provides the same events as the IWMPEvents, IWMPEvents2, IWMPEvents3, and IWMPEvents4 interfaces, but inherits from IDispatch rather than IUnknown.
ms.assetid: 883d538e-19b6-417b-a32d-622c41c24b9c
keywords:
- _WMPOCXEvents Interface Windows Media Player
topic_type:
- apiref
api_name:
- _WMPOCXEvents Interface
api_location:
- wmp.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# \_WMPOCXEvents Interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **\_WMPOCXEvents** interface provides the same events as the **IWMPEvents**, **IWMPEvents2**, **IWMPEvents3**, and **IWMPEvents4** interfaces, but inherits from **IDispatch** rather than **IUnknown**. This enables you to receive Windows Media Player event notifications through an **IDispatch** event sink.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Handling Events in C++**](handling-events-in-c.md)
</dt> <dt>

[**IWMPEvents Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents)
</dt> <dt>

[**IWMPEvents2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents2)
</dt> <dt>

[**IWMPEvents3 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents3)
</dt> <dt>

[**IWMPEvents4 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents4)
</dt> </dl>

 

 





