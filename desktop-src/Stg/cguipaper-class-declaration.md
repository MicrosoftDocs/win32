---
title: CGuiPaper Class Declaration
description: CGuiPaper Class Declaration
ms.assetid: b772d056-bf89-46a8-9462-21772cf96dfa
ms.topic: article
ms.date: 05/31/2018
---

# CGuiPaper Class Declaration

The following is the **CGuiPaper** class declaration from GUIPAPER.H.


```C++
class CGuiPaper
  {
    public:
      CGuiPaper(void);
      ~CGuiPaper(void);
      BOOL Init(HINSTANCE hInst, HWND hWnd, TCHAR* pszCmdLineFile);
      HRESULT DrawOn(void);
      HRESULT DrawOff(void);
      HRESULT ClearWin(void);
      HRESULT PaintWin(void);
      HRESULT Erase(void);
      HRESULT Resize(WORD wWidth, WORD wHeight);
      HRESULT InkWidth(SHORT nInkWidth);
      HRESULT InkColor(COLORREF crInkColor);
      HRESULT InkSaving(BOOL bInkSaving);
      HRESULT InkStart(SHORT nX, SHORT nY);
      HRESULT InkDraw(SHORT nX, SHORT nY);
      HRESULT InkStop(SHORT nX, SHORT nY);
      HRESULT ConnectPaperSink(void);
      HRESULT DisconnectPaperSink(void);
      HRESULT Load(void);
      HRESULT Save(void);
      int     AskSave(void);
      HRESULT Open(void);
      HRESULT SaveAs(void);
      COLORREF PickColor(void);

    private:
      HINSTANCE  m_hInst;
      HWND       m_hWnd;
      HDC        m_hDC;
      RECT       m_WinRect;
      IPaper*    m_pIPaper;
      SHORT      m_nLockKey;
      HPEN       m_hPen;
      SHORT      m_nInkWidth;
      COLORREF   m_crInkColor;
      BOOL       m_bInkSaving;
      BOOL       m_bInking;
      BOOL       m_bPainting;
      POINT      m_OldPos;
      IUnknown*  m_pCOPaperSink;
      DWORD      m_dwPaperSink;
      BOOL       m_bDirty;
      CPapFile*    m_pPapFile;
      OPENFILENAME m_ofnFile;
      TCHAR        m_szFileFilter[MAX_PATH];
      TCHAR        m_szFileName[MAX_PATH];
      TCHAR        m_szFileTitle[MAX_PATH];
      CHOOSECOLOR  m_ChooseColor;
      COLORREF     m_acrCustColors[16];

      IConnectionPoint* GetConnectionPoint(REFIID riid);
  };
```



**CGuiPaper** maintains the current GUI properties for the drawing paper. Members **m\_crInkColor**, **m\_crInkWidth**, and **m\_WinRect** contain values for the current ink color, ink width, and drawing rectangle. The **m\_hWnd** member stores the handle to the window where painting is done.

The actual painting of images is done using a handle to a device context held in member **m\_hDC**. A handle to the current drawing pen is kept in member **m\_hPen**. The pen is destroyed and recreated when its color or width is changed by the user.

Members **m\_pCOPaperSink** and **m\_dwPaperSink** hold values necessary for connecting with COPaper to receive incoming notifications through the [**IPaperSink**](ipapersink-methods.md) interface. Member **m\_bDirty** holds a flag indicating that the user has changed the drawing and that it no longer reflects the data stored in its file.

Member **m\_pIPaper** holds the main interface pointer to the COPaper object. All of the COPaper functionality is accessed through this pointer.

The **m\_nLockKey** member is used to support a client locking scheme that is used with multiple clients to allow a client exclusive access to a shared COPaper object. COPaper assigns **m\_nLockKey** during an [**IPaper**](ipaper-methods.md)::**Lock** call and is passed as a parameter by the client in subsequent calls to COPaper. COPaper will perform the work in those calls only if the lock key that is passed matches the key last handed out to a client by COPaper.

Member **m\_pPapFile** holds a pointer to a [**CPapFile**](cpapfile-class-and-methods.md) object. It is a C++ object that encapsulates load and save operations on a structured storage compound file. **CPapFile** works with the underlying server-based COPaper object to load and save the COPaper drawing data.

 

 




