---
title: CMainWindow
description: The following example code illustrates this procedure.
ms.assetid: a2998232-db71-48ce-b14b-5e17de147172
keywords:
- CMainWindow
ms.topic: article
ms.date: 05/31/2018
---

# CMainWindow

The Microsoft Windows operating system translates the following user actions into standard window messages and sends them to the main procedure in the **StoClien** application:

-   The user clicks the left mouse button, or the pen tip switch in tablet devices, to initiate a line drawing sequence.
-   The user clicks and holds the button and moves the mouse to draw a line.
-   The sequence is ended when the left mouse button is released.

The following example code illustrates this procedure.

## CMainWindow::WindowProc (STOCLIEN.CPP)


```C++
LRESULT CMainWindow::WindowProc(
            UINT uMsg,
            WPARAM wParam,
            LPARAM lParam)
  {
    LRESULT lResult = FALSE;

    switch (uMsg)
    {
      case WM_CREATE:
        break;

      case WM_ACTIVATE:
        // A mouse click reactivates the paint procedure.
        // This is used to paint a new window when a user
        // selects a portion of the STOCLIEN window that is 
        // visible beneath another window. This message is  
        // sent in the WindowProc handle.
        if (WA_CLICKACTIVE == LOWORD(wParam))
          m_pGuiPaper->PaintWin();
        lResult = ::DefWindowProc(m_hWnd, uMsg, wParam, lParam);
        break;

      case WM_SIZE:
        // Handle a resize of this window.
        m_wWidth = LOWORD(lParam);
        m_wHeight = HIWORD(lParam);
        // Inform CGuiPaper of the change.
        m_pGuiPaper->Resize(m_wWidth, m_wHeight);
        break;

      case WM_PAINT:
        // This is a message to repaint the window.
        {
          PAINTSTRUCT ps;

          if(BeginPaint(m_hWnd, &ps))
            EndPaint(m_hWnd, &ps);

          m_pGuiPaper->PaintWin();
        }
        break;

      case WM_LBUTTONDOWN:
        // Start sequence of ink drawing to the paper.
        m_pGuiPaper->InkStart(LOWORD(lParam), HIWORD(lParam));
        break;

      case WM_MOUSEMOVE:
        // Draw inking sequence data.
        m_pGuiPaper->InkDraw(LOWORD(lParam), HIWORD(lParam));
        break;

      case WM_LBUTTONUP:
        // Stop an ink drawing sequence.
        m_pGuiPaper->InkStop(LOWORD(lParam), HIWORD(lParam));
        break;

      case WM_COMMAND:
        // Dispatch and handle any Menu command messages received.
        lResult = DoMenu(wParam, lParam);
        break;

      case WM_CHAR:
        if (wParam == 0x1b)
        {
          // Exit this application if user presses the ESC key.
          ::PostMessage(m_hWnd, WM_CLOSE, 0, 0);
        }
        break;

      case WM_CLOSE:
        // The user selected Close on the main window System menu
        // or Exit on the File menu.
        // If there is unsaved ink data, then prompt
        // the user. If the user cancels, do not close the window.
        if (IDCANCEL == m_pGuiPaper->AskSave())
          break;
      case WM_QUIT:
        // When exiting the application, close any associated help
        // windows.
        // ::WinHelp(m_hWnd, m_szHelpFile, HELP_QUIT, 0);
      default:
        // If there are any messages that have not been handled,
        // send them to the default window procedure.
        lResult = ::DefWindowProc(m_hWnd, uMsg, wParam, lParam);
        break;
    }

    return(lResult);
  }
```



A line drawing sequence starts when the WM\_LBUTTONDOWN message delivers mouse position data.

CMainWindow has a pointer to the CGuiPaper object and calls the [**CGuiPaper::InkStart**](cguipaper-methods.md) method to start the line drawing sequence.

As the mouse is moved to draw, a sequence of separate **WM\_MOUSEMOVE** messages that contain mouse position data are provided to the [CGuiPaper::InkDraw](cguipaper-methods.md) method.

When the left mouse button is released, the **WM\_LBUTTONUP** message is received. The [CGuiPaper::InkStop](cguipaper-methods.md) method stops the line drawing sequence.

 

 




