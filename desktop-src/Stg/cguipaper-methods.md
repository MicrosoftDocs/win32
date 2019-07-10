---
title: CGuiPaper Methods
description: CGuiPaper's methods are summarized as follows. These methods are all implemented in GUIPAPER.CPP.
ms.assetid: 965a60d4-2737-4a2d-8790-bee70bceaeeb
ms.topic: reference
ms.date: 05/31/2018
---

# CGuiPaper Methods

CGuiPaper's methods are summarized as follows. These methods are all implemented in GUIPAPER.CPP.



| Method                                                         | Description                                                                                                           |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| BOOL Init(HINSTANCE hInst, HWND hWnd, TCHAR\* pszCmdLineFile); | Initializes the GuiPaper. Asks server to create a COPaper object.                                                     |
| HRESULT DrawOn(void);                                          | Locks paper for drawing exclusively by this client.                                                                   |
| HRESULT DrawOff(void);                                         | Unlocks paper to allow other clients to draw.                                                                         |
| HRESULT ClearWin(void);                                        | Clears display window but retains ink data.                                                                           |
| HRESULT PaintWin(void);                                        | Clears window and repaints with current ink data.                                                                     |
| HRESULT Erase(void);                                           | Erases current drawing content and clears display window.                                                             |
| HRESULT Resize(WORD wWidth, WORD wHeight);                     | Resizes the display window.                                                                                           |
| HRESULT InkWidth(SHORT nInkWidth);                             | Sets current ink width for drawing.                                                                                   |
| HRESULT InkColor(COLORREF crInkColor);                         | Sets current ink color for drawing.                                                                                   |
| HRESULT InkSaving(BOOL bInkSaving);                            | Turns ink data saving in COPaper on and off.                                                                          |
| HRESULT InkStart(SHORT nX, SHORT nY);                          | Starts ink drawing sequence.                                                                                          |
| HRESULT InkDraw(SHORT nX, SHORT nY);                           | Draws ink sequence data.                                                                                              |
| HRESULT InkStop(SHORT nX, SHORT nY);                           | Stops ink drawing sequence.                                                                                           |
| HRESULT ConnectPaperSink(void);                                | Connects the client PaperSink object to the server COPaper source.                                                    |
| HRESULT DisconnectPaperSink(void);                             | Disconnect the client PaperSink object from the server COPaper source.                                                |
| HRESULT Load(void);                                            | Loads ink data from current compound file.                                                                            |
| HRESULT Save(void);                                            | Saves existing ink data to current compound file.                                                                     |
| HRESULT AskSave(void);                                         | Checks if drawing changed. If so, displays dialog box asking user whether to save changes and responds appropriately. |
| HRESULT Open(void);                                            | Shows Win32 common dialog box. Opens existing paper data compound file.                                               |
| HRESULT SaveAs(void);                                          | Shows Win32 common dialog box. Saves current paper data in renamed file.                                              |
| COLORREF PickColor(void);                                      | Shows Win32 ommon dialog box. Asks user to choose new pen color.                                                      |



 

The **Init** method creates the server-based COPaper object and assigns CGuiPaper's m\_pIPaper member.

The **AskSave**, **Open**, **SaveAs**, and **PickColor** methods provide familiar GUI behavior using Win32 common dialogs. For example, the **Open** method uses the Win32 Open File Name dialog box to ask the user to specify a file name for opening.

The **Load** and **Save** methods will be covered in detail later in this tour.

**InkSaving**, **InkStart**, **InkDraw**, and **InkStop** are the central methods for the drawing functionality of the **StoClien** application. **StoClien** uses these CGuiPaper methods to capture, display, and store the interactive drawing data as it occurs under user control. They perform a dual role of painting the drawn image to the client window as well as passing the drawing data to COPaper in the server. COPaper translates the drawing data into ink data packets for storage.

 

 




