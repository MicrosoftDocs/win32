---
title: InkStart Method
description: InkStart, InkDraw, and InkStop methods all use Win32 GUI constructs such as device contexts and pen objects.
ms.assetid: a639e1d2-6d81-472b-b639-d237e202020f
ms.topic: article
ms.date: 05/31/2018
---

# InkStart Method

**InkStart**, [**InkDraw**](inkdraw-method.md), and [**InkStop**](cguipaper-methods.md) methods all use Win32 GUI constructs such as device contexts and pen objects. This illustrates why CGuiPaper is needed as a separate level of encapsulation. The GUI aspects of the drawing paper are handled in CGuiPaper. The COPaper object is sent only ink data.

Another design reason for the CGuiPaper level of encapsulation is the dual nature of its **InkStart**, [**InkDraw**](inkdraw-method.md), and [**InkStop**](cguipaper-methods.md) methods. They not only call on COPaper to record the ink data as it occurs, they also paint a visual image of the drawing as it occurs. CGuiPaper keeps an m\_bInkSaving flag to manage this dual nature. When m\_bInkSaving is FALSE, the image is drawn on screen but the data is not sent to COPaper for recording.

This scheme is used in repainting when the user is not moving the mouse but COPaper's ink data is being resent to CGuiPaper for automatic repainting. CGuiPaper can be told to set the m\_bInkSaving flag by calling its [**InkSaving**](cguipaper-methods.md) method.

The following sample code snippets illustrate the **InkStart** methods of GUIPAPER.CPP AND SINK.CPP.

## InkStart Method (GUIPAPER.CPP)


```C++
HRESULT CGuiPaper::InkStart(
                       SHORT nX,
                       SHORT nY)
  {
    HRESULT hr = E_FAIL;

    if (m_nLockKey || (!m_nLockKey && !m_bInkSaving))
    {
      // Start an ink drawing sequence only if one is not in progress.
      if (!m_bInking)
      {
        // Remember start position.
        m_OldPos.x = nX;
        m_OldPos.y = nY;

        // Delete old pen.
        if (m_hPen)
          DeleteObject(m_hPen);

        // Create and select the new drawing pen.
        m_hPen = CreatePen(PS_SOLID, m_nInkWidth, m_crInkColor);
        SelectObject(m_hDC, m_hPen);

        hr = NOERROR;

        // Ask the Paper object to mark the start of the ink drawing
        // sequence in the current ink color.
        if (m_pIPaper && m_bInkSaving)
        {
          hr = m_pIPaper->InkStart(
                            m_nLockKey,
                            nX,
                            nY,
                            m_nInkWidth,
                            m_crInkColor);
          // Capture the Mouse.
          SetCapture(m_hWnd);

          // We've modified the ink data--it is now "dirty" with
          // respect to the compound file image. Set dirty flag.
          m_bDirty = TRUE;
        }

        // Set inking flag to TRUE.
        m_bInking = TRUE;
      }
    }

    return hr;
  }
```



## InkStart Method (SINK.CPP)

**StoClien** receives the drawing data in the form of calls to the connected **IPaperSink** interface in its COPaperSink object. These methods correspond to the similar **InkStart**, [**InkDraw**](inkdraw-method.md), and [**InkStop**](cguipaper-methods.md) methods in CGuiPaper.


```C++
STDMETHODIMP COPaperSink::CImpIPaperSink::InkStart(
                                              SHORT nX,
                                              SHORT nY,
                                              SHORT nWidth,
                                              COLORREF crInkColor)
  {
    // Turn off ink saving to the COPaper object.
    m_pBackObj->m_pGuiPaper->InkSaving(FALSE);

    // Play the data back to the CGuiPaper for display only.
    m_pBackObj->m_pGuiPaper->InkWidth(nWidth);
    m_pBackObj->m_pGuiPaper->InkColor(crInkColor);
    m_pBackObj->m_pGuiPaper->InkStart(nX, nY);

    return NOERROR;
  }
```



When **InkStart** is called in the sink, it calls CGuiPaper to turn off ink saving to COPaper. COPaper does not need to receive an echoed copy of the data it is sending. When [**InkDraw**](inkdraw-method.md) is called in the sink, it simply passes the call on to **CGuiPaper::InkDraw**. When [**InkStop**](cguipaper-methods.md) is called in the sink, CGuiPaper is called to turn ink saving back on. The result is a playback of COPaper's ink data to CGuiPaper for display only.

You can test the behavior of **StoClien** when its **IPaperSink** is disconnected by choosing the Disconnect choice on the Sink menu. As an experiment, after disconnecting the sink, choose About from the Help menu. This will show the About dialog box, which will cover part of the **StoClien**'s drawing. Click OK in the About dialog box. Notice that the portion of the drawing that was covered is now gone. The drawing data is not lost, but part of the image is. The client received the WM\_PAINT message and issued the [**IPaper::Redraw**](ipaper--redraw.md) method. But because the sink was not connected, it did not receive the **IPaperSink** calls to repaint the drawing.

You can also test this behavior by minimizing **StoClien** and then restoring it. In this case, the entire drawing image is lost and needs repainting. To repaint the drawing image after either of these tests, use the Sink menu to reconnect, and then choose [**Redraw**](ipaper--redraw.md) from the Draw menu.

 

 




