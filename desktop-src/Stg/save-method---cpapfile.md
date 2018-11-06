---
title: Save Method - CPapFile
description: When CPapFile is initialized, it can be used to save the current drawing data held in the COPaper object.
ms.assetid: ceac32e5-7d47-480b-b1cd-5a17ac04dd0c
keywords:
- Save Method - CPapFile
ms.topic: article
ms.date: 05/31/2018
---

# Save Method - CPapFile

When **CPapFile** is initialized, it can be used to save the current drawing data held in the COPaper object.

## Save Method (PAPFILE.CPP)

This example is the **CPapFile** [**Save**](ipaper--save.md) method from Papfile.cpp.


```C++
HRESULT CPapFile::Save(
                      SHORT nLockKey,
                      TCHAR* pszFileName)
  {
    HRESULT hr = E_FAIL;
    BOOL bNewFile = (NULL != pszFileName);
    TCHAR* pszFile;

    // If a null file name is passed, then use current file name.
    pszFile = bNewFile ? pszFileName : m_szCurFileName;

    // Use the COM service to reopen, or create, the compound file.
    hr = StgCreateDocfile(
        pszFile,
    STGM_CREATE | STGM_DIRECT | STGM_READWRITE | STGM_SHARE_EXCLUSIVE,
        0,
        &m_pIStorage);
    if (SUCCEEDED(hr))
    {
      // Obtained the IStorage. The compound file is open.
      // Instruct the COPaper object on the server side to save its
      // paper data into the compound file using the IStorage of our
      // client-provided compound file.
      hr = m_pIPaper->Save(nLockKey, m_pIStorage);
      if (SUCCEEDED(hr))
      {
        // The paper data was saved and obtained a new current 
        // compound file name. Copy it for later use in saves 
        // and loads.
        if (bNewFile)
          StringCchCopy(m_szCurFileName, sizeof(m_szCurFileName), pszFileName);
      }

      // Storage complete. Do not hold the file open.
      // Re-obtain the IStorage again later (and thus re-open
      // the compound file) when required for another save or load.
      RELEASE_INTERFACE(m_pIStorage);
    }

    return (hr);
  }
  
```



If **NULL** is passed for the *pszFileName* parameter, the stored content of member **m\_szCurFileName** is used for the file name. The *nLockKey* is the client lock key obtained in a previous call to the COPaper [**Lock**](ipaper-methods.md) method in the **IPaper** interface.

The COM standard [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) service function is called to create the compound file in which the drawing data will be saved.

The name of the compound file to create is passed as the first parameter. This is expected by [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) as a Unicode string. When **StoClien** is compiled for ANSI strings (UNICODE is not defined, which is the default in the makefile), this call actually reduces to a call to an internal APPUTIL function, **A\_StgCreateDocfile**. This function performs the proper conversion of the ANSI pszFile parameter to a Unicode version before calling **StgCreateDocfile**. For more information, see Apputil.h and Stoserve.htm.

The access mode flags are passed as the second parameter and determine which access modes are permitted on the new file. The [STGM\_CREATE](stgm-constants.md) access mode flag creates a new compound file or overwrites an existing one of the same name. [STGM\_READWRITE](stgm-constants.md) opens the file with read-write permission. [STGM\_DIRECT](stgm-constants.md) opens the file for direct access, as opposed to transacted access. [STGM\_SHARE\_EXCLUSIVE](stgm-constants.md) opens the file for exclusive, non-shared use by the caller.

The third parameter is reserved and must be zero.

The address of pointer variable **m\_pIStorage** is passed to [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) as the fourth parameter. When the call successfully returns, **m\_pIStorage** contains an interface pointer to an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface. This is the interface that is used for any subsequent operations on the file.

The important operation in this case is to have the COPaper object store its drawing data in the file. This is done above using the [**Save**](ipaper--save.md) method of the COPaper [**IPaper**](ipaper-methods.md) interface. If COPaper succeeds in saving its data in the storage object provided, the name of the compound file is copied into **m\_szCurFileName** as the new current file name.

 

 




