---
title: Load Method - CPapFile
description: When these operations are successful, the obtained IStorage interface is released. This closes the file and indicates that the file is not held open during other client operations. It will be reopened when required.
ms.assetid: 40f79adb-87f3-4b0e-9cfe-927a4bc9ada5
keywords:
- Load Method - CPapFile
ms.topic: article
ms.date: 05/31/2018
---

# Load Method - CPapFile

When these operations are successful, the obtained [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface is released. This closes the file and indicates that the file is not held open during other client operations. It will be reopened when required.

This example is the **CPapFile** **Load** method from Papfile.cpp.


```C++
HRESULT CPapFile::Load(
                      SHORT nLockKey,
                      TCHAR* pszFileName)
  {
    HRESULT hr = E_FAIL;
    BOOL bNewFile = (NULL != pszFileName);
    TCHAR* pszFile;

    // If null file name passed then use current file name.
    pszFile = bNewFile ? pszFileName : m_szCurFileName;

    // Verify that the file is using the APPUTIL function.
    if (FileExist(pszFile))
    {
      // Use the COM service to verify that the file is actually a 
      // valid compound file.
      hr = StgIsStorageFile(pszFile);
      if (SUCCEEDED(hr))
      {
        // Use the COM service to open the compound file and
        // obtain an IStorage interface.
        hr = StgOpenStorage(
               pszFile,
               NULL,
               STGM_DIRECT | STGM_READ | STGM_SHARE_EXCLUSIVE,
               NULL,
               0,
               &m_pIStorage);
        if (SUCCEEDED(hr))
        {
          // An IStorage interface has been obtained. Now, request 
          // the COPaper object on the server side to load into  
          // itself the file's paper data using IStorage for our 
          // client-provided compound file.
          hr = m_pIPaper->Load(nLockKey, m_pIStorage);
          if (SUCCEEDED(hr))
          {
            // The paper data was loaded and a current compound
            // file name exists. Copy it for later use in a saves 
            // and loads.
            if (bNewFile)
              StringCchCopy(m_szCurFileName, sizeof(m_szCurFileName), pszFileName);
          }

          // The Storage object is not required now. Do not hold the 
          // file open. Re-obtain the IStorage again later, when 
          // required (and thus re-open the compound file) for
          // another save or load.
          RELEASE_INTERFACE(m_pIStorage);
        }
      }
    }

    return (hr);
  }
  
```



### Remarks

As with the [**Save**](save-method---cpapfile.md) method, if **NULL** is passed for the *pszFileName* parameter, the stored content of member **m\_szCurFileName** is used for the file name. Because an existing file may be opened, the APPUTIL **FileExist** function is first used to verify that the file exists. If it exists, the standard [**StgIsStorageFile**](/windows/desktop/api/coml2api/nf-coml2api-stgisstoragefile) service function is called to verify the format of the file to determine if it is a valid compound file.

If the file is valid, the standard [**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage) service function is called to open the file and return a pointer to an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface for it.

The first parameter is the name of the compound file to open. As with the [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) call, this string is expected in the Unicode form, and during ANSI compilation an APPUTIL macro is used to ensure the ANSI parameter is converted to the expected Unicode.

The second priority storage parameter is **NULL**, indicating it is not used in this sample.

The access mode flags are passed as the third parameter to specify what access modes are permitted on the opened file. [**STGM\_READ**](stgm-constants.md) opens the file with read-only permission. [**STGM\_DIRECT**](stgm-constants.md) opens the file for direct access, as opposed to transacted access. [**STGM\_SHARE\_EXCLUSIVE**](stgm-constants.md) opens the file for exclusive, non-shared use by the caller.

The fourth element exclusion parameter in **NULL**, indicating it is not used in this sample.

The fifth parameter is reserved for future use and must be zero.

The address of pointer variable **m\_pIStorage** is passed as the sixth parameter. When the call successfully returns, **m\_pIStorage** contains a pointer to an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface. This is the interface that is used for any subsequent operations on the opened file.

The important operation in this case is to have the COPaper object load its drawing data from the file. This is done above using the **Load** method of COPaper's [**IPaper**](ipaper-methods.md) interface. If COPaper succeeds in loading its data using the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) provided, the name of the compound file is copied into **m\_szCurFileName** as the new current file name.

When these operations are successfully completed, the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface that was obtained is released. This closes the file and means that the file is not held open during other client operations. It will be reopened when required.

 

 




