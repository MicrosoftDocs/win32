---
description: The CAudioCaptureTerminal terminal is derived from CSingleFilterTerminal and implements a static audio capture terminal for wave devices using the DirectShow wavein filter. Most MSPs will not need to override the implementation of this terminal.
ms.assetid: 2860bf22-46ae-484a-a47b-0d7057b900a1
title: CAudioCaptureTerminal
ms.topic: article
ms.date: 05/31/2018
---

# CAudioCaptureTerminal

The **CAudioCaptureTerminal** terminal is derived from [CSingleFilterTerminal](csinglefilterterminal.md) and implements a static audio capture terminal for wave devices using the DirectShow wavein filter. Most MSPs will not need to override the implementation of this terminal.

Defined in MSPtmac.h.

## Remarks

The [**put\_Balance**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasicaudioterminal-put_balance) and [**get\_Balance**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasicaudioterminal-get_balance) methods of **CAudioCaptureTerminal** are not implemented and will return E\_NOTIMPL.

 

 



