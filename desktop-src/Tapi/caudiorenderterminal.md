---
description: The CAudioRenderTerminal terminal is derived from CSingleFilterTerminal and implements a static audio render terminal for wave devices using the DirectShow waveout filter. Most MSPs will not need to override the implementation of this terminal.
ms.assetid: 58cd0765-9430-4333-ae96-4d8ca73727b5
title: CAudioRenderTerminal
ms.topic: article
ms.date: 05/31/2018
---

# CAudioRenderTerminal

The **CAudioRenderTerminal** terminal is derived from [CSingleFilterTerminal](csinglefilterterminal.md) and implements a static audio render terminal for wave devices using the DirectShow waveout filter. Most MSPs will not need to override the implementation of this terminal.

Defined in MSPtrmar.h.

## Remarks

The [**put\_Balance**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasicaudioterminal-put_balance) and [**get\_Balance**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasicaudioterminal-get_balance) methods of **CAudioRenderTerminal** are not implemented and will return E\_NOTIMPL.

 

 



