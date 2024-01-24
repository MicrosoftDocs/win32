---
title: Creating a Virtual Function Table for a Stream Handler
description: Creating a Virtual Function Table for a Stream Handler
ms.assetid: 8f43b0d4-6710-4175-8da0-aafd6b6d753a
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating a Virtual Function Table for a Stream Handler

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following example (written in C) shows how an application (AVIBall) creates the virtual function table used to reference its services.


```C++
HRESULT STDMETHODCALLTYPE AVIBallQueryInterface (PAVISTREAM ps, 
    REFIID riid, LPVOID FAR* ppvObj); 
HRESULT STDMETHODCALLTYPE AVIBallCreate (PAVISTREAM ps, 
    LONG lParam1, LONG lParam2); 
ULONG STDMETHODCALLTYPE AVIBallAddRef (PAVISTREAM ps); 
ULONG STDMETHODCALLTYPE AVIBallRelease (PAVISTREAM ps); 
HRESULT STDMETHODCALLTYPE AVIBallInfo (PAVISTREAM ps, 
    AVIStreamHeader FAR * psi, LONG lSize); 
LONG STDMETHODCALLTYPE AVIBallFindSample (PAVISTREAM ps, 
    LONG lPos, LONG lFlags); 
HRESULT STDMETHODCALLTYPE AVIBallReadFormat (PAVISTREAM ps, 
    LONG lPos, LPVOID lpFormat, LONG FAR *lpcbFormat); 
HRESULT STDMETHODCALLTYPE AVIBallSetFormat (PAVISTREAM ps, 
    LONG lPos, LPVOID lpFormat, LONG cbFormat); 
HRESULT STDMETHODCALLTYPE AVIBallRead (PAVISTREAM ps, 
    LONG lStart, LONG lSamples, LPVOID lpBuffer, LONG cbBuffer, 
    LONG FAR * plBytes,LONG FAR * plSamples); 
HRESULT STDMETHODCALLTYPE AVIBallWrite (PAVISTREAM ps, LONG lStart, 
    LONG lSamples, LPVOID lpBuffer, LONG cbBuffer, DWORD dwFlags); 
HRESULT STDMETHODCALLTYPE AVIBallDelete (PAVISTREAM ps, 
    LONG lStart, LONG lSamples); 
HRESULT STDMETHODCALLTYPE AVIBallReadData (PAVISTREAM ps, 
    DWORD fcc, LPVOID lp,LONG FAR *lpcb); 
HRESULT STDMETHODCALLTYPE AVIBallWriteData (PAVISTREAM ps, 
    DWORD fcc, LPVOID lp,LONG cb); 
 
IAVIStreamVtbl AVIBallHandler = { 
    AVIBallQueryInterface,  // Function pointer for ::QueryInterface 
    AVIBallAddRef,          // Function pointer for ::AddRef 
    AVIBallRelease,         // Function pointer for ::Release 
    AVIBallCreate,          // Function pointer for ::Create 
    AVIBallInfo,            // Function pointer for ::Info 
    AVIBallFindSample,      // Function pointer for ::FindSample 
    AVIBallReadFormat,      // Function pointer for ::ReadFormat 
    AVIBallSetFormat,       // Function pointer for ::SetFormat 
    AVIBallRead,            // Function pointer for ::Read 
    AVIBallWrite,           // Function pointer for ::Write 
    AVIBallDelete,          // Function pointer for ::Delete 
    AVIBallReadData,        // Function pointer for ::ReadData 
    AVIBallWriteData        // Function pointer for ::WriteData 
}; 
```



File handlers use a similar procedure, except they use a different definition for the virtual function table.

 

 




