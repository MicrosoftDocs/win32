---
title: Init Method - CPapFile
description: The following code example shows how CPapFile is initialized.
ms.assetid: 8312a6b2-6f3f-4a24-8aeb-9461f3b1a905
keywords:
- Init Method - CPapFile
ms.topic: article
ms.date: 05/31/2018
---

# Init Method - CPapFile

The following code example shows how **CPapFile** is initialized.

This example is the **CPapFile** **Init** method from Papfile.cpp.


```C++
HRESULT CPapFile::Init(
                      TCHAR* pszAppFileName,
                      IPaper* pIPaper)
  {
    HRESULT hr = E_FAIL;

    if (NULL != pIPaper)
    {
      // Keep CPapFile copy of pIPaper. Thus AddRef it.
      // Released in Destructor.
      m_pIPaper = pIPaper;
      m_pIPaper->AddRef();

      if (NULL != pszAppFileName)
      {
        // Set the default current file name.
        StringCchCopy(m_szCurFileName, sizeof(m_szCurFileName), pszAppFileName);

        hr = NOERROR;
      }
    }

    return (hr);
  }
  
```



The *pszAppFileName* parameter is used to initialize CPapFile with a default file name for any subsequent load or save operations. A copy is kept in member **m\_szCurFileName** for the first load. In **StoClien**, such a load is attempted when the application first starts after CPapFile has been initialized with *pszAppFileName* assigned "STOCLIEN.PAP". This file name was constructed in a CGuiPaper constructor by obtaining the current executing module name. (The Win32 [**GetModuleFileName**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) function is called).

The *pIPaper* parameter is required by CPapFile, because it uses this interface on the COPaper object to perform its load and save operations. **AddRef** is called on this stored copy of *pIPaper*, in accordance with COM rules. The matching **Release** is called in the CPapFile destructor.

 

 