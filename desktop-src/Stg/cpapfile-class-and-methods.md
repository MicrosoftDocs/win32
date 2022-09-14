---
title: CPapFile Class and Methods
description: StoClien encapsulates its compound file operations in a CPapFile C++ object.
ms.assetid: 21a3e170-0a73-4744-8cfc-3a04e0571792
ms.topic: reference
ms.date: 05/31/2018
---

# CPapFile Class and Methods

**StoClien** encapsulates its compound file operations in a CPapFile C++ object.

The following is the **CPapFile** class declaration from Papfile.h.


```C++
class CPapFile
  {
    public:
      CPapFile(void);
      ~CPapFile(void);
      HRESULT Init(TCHAR* pszFileName, IPaper* pIPaper);
      HRESULT Load(SHORT nLockKey, TCHAR* pszFileName);
      HRESULT Save(SHORT nLockKey, TCHAR* pszFileName);

    private:
      TCHAR          m_szCurFileName[MAX_PATH];
      IPaper*        m_pIPaper;
      IStorage*      m_pIStorage;
  };
  
```



The CPapFile object keeps a current file name in member **m\_szCurFileName**. This file name is used as a default in the [**Load**](load-method---cpapfile.md) and [**Save**](save-method---cpapfile.md) methods when they do not explicitly receive a file name.

Member **m\_pIPaper** keeps an interface pointer to the COPaper [**IPaper**](ipaper-methods.md) interface. Member **m\_pIStorage** keeps a pointer to the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface for the current compound file that **StoClien** is using for structured storage.

The following is a summary of CPapFile's methods.


```C++
HRESULT Init(TCHAR* pszFileName, IPaper* pIPaper);
    // Initializes CPapFile.

  HRESULT Load(SHORT nLockKey, TCHAR* pszFileName);
    // Loads default or specified paper data file.

  HRESULT Save(SHORT nLockKey, TCHAR* pszFileName);
    // Saves drawing data to the current paper data file or
    // to a specified paper data file.
```



 

 




