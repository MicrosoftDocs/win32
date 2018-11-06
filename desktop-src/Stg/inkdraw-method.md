---
title: InkDraw Method
description: CGuiPaper also keeps an m\_bInking flag. InkStart sets it to TRUE to signal that a drawing sequence is in process. For example, the InkDraw method uses this flag to determine whether it should paint and save ink data.
ms.assetid: 0fe9d029-1522-4caf-8efb-0a4eb2b59958
keywords:
- InkDraw
ms.topic: article
ms.date: 05/31/2018
---

# InkDraw Method

CGuiPaper also keeps an m\_bInking flag. [InkStart](inkstart-method.md) sets it to **TRUE** to signal that a drawing sequence is in process. For example, the InkDraw method uses this flag to determine whether it should paint and save ink data.

The following is the InkDraw method from GUIPAPER.CPP.


```C++
HRESULT CGuiPaper::InkDraw(
                       SHORT nX,
                       SHORT nY)
  {
    if (m_bInking)
    {
      // Start this ink line at previous old position.
      MoveToEx(m_hDC, m_OldPos.x, m_OldPos.y, NULL);

      // Assign new old position and draw the new line.
      LineTo(m_hDC, m_OldPos.x = nX, m_OldPos.y = nY);

      // Ask the Paper object to save this data.
      if (m_bInkSaving)
        m_pIPaper->InkDraw(m_nLockKey, nX, nY);
    }

    return NOERROR;
  }
```



This method does nothing if m\_bInking is **FALSE**. This is the condition when the user is simply moving the mouse over the client window without pressing the left mouse button.

InkDraw clearly has a dual responsibility. The Win32 MoveToEx and LineTo calls are made to draw line images on the GUI screen (using the device context handle kept in m\_hDC). The ink data is also passed to the COPaper object for recording using the [IPaper](ipaper-methods.md) interface's InkDraw method. When m\_bInkSaving is **FALSE**, InkDraw paints the line image but does not store the data in COPaper. This condition is used during repainting.

 

 




