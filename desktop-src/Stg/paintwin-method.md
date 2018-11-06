---
title: PaintWin Method
description: PaintWin Method
ms.assetid: e89794e6-c059-4531-a1e3-3a4972e0218d
ms.topic: article
ms.date: 05/31/2018
---

# PaintWin Method

The following is CGuiPaper's **PaintWin** method from GUIPAPER.CPP.


```C++
HRESULT CGuiPaper::PaintWin(void)
  {
    HRESULT hr = E_FAIL;
    COLORREF crInkColor;
    SHORT nInkWidth;

    if (m_pIPaper && !m_bPainting && !m_bInking)
    {
      m_bPainting = TRUE;
      // Save and restore ink color and width since redraw otherwise
      // ends up changing these values in CGuiPaper.
      crInkColor = m_crInkColor;
      nInkWidth = m_nInkWidth;
      hr = m_pIPaper->Redraw(m_nLockKey);
      m_nInkWidth = nInkWidth;
      m_crInkColor = crInkColor;
      m_bPainting = FALSE;
    }

    return hr;
  }
```



**PaintWin** essentially calls COPaper's **Redraw** method. In the [StoServe](structured-storage-server-sample--stoserve-.md) sample, the **Redraw** method was shown to broadcast COPaper's entire ink data array to all connected sinks. **PaintWin** calls an object on the server side to send back the drawing data to the client.

 

 




