---
title: Unicode Considerations
description: The WriteFmtUserTypeStg service function, used in the IPaper Save method, requires Unicode string parameters.
ms.assetid: 34a1d30e-4401-474e-999e-832b963064bb
ms.topic: article
ms.date: 05/31/2018
---

# Unicode Considerations

The **WriteFmtUserTypeStg** service function, used in the [**IPaper::Save**](ipaper--save.md) method, requires Unicode string parameters. This is the case with COM/OLE service calls that take string parameters. When compiling for ANSI strings, the expected Unicode parameters need conversion from ANSI to Unicode. This process is achieved using some macros in APPUTIL.h that may obscure conversions. For example, see **WriteFmtUserTypeStg**.

The following call appears in the [**Save**](ipaper--save.md) method.


```C++
WriteFmtUserTypeStg(pIStorage, m_ClipBdFmt, TEXT(CLIPBDFMT_STR));
```



When **StoServe** is compiled for ANSI (not for Unicode), this call actually reduces to a call to an internal APPUTIL surrogate function. To support this, the following macro scheme is used in Apputil.h, which is an included file in all code sample .CPP files.


```C++
#if !defined(UNICODE)

  STDAPI A_WriteFmtUserTypeStg(IStorage*, CLIPFORMAT, LPSTR);

  #if !defined(_NOANSIMACROS_)

  #undef WriteFmtUserTypeStg
  #define WriteFmtUserTypeStg(a, b, c) A_WriteFmtUserTypeStg(a, b, c)

  #endif

  #endif
```



The scheme uses surrogate service call functions. The ANSI versions of the calls begin with A\_. These surrogate ANSI functions are implemented in Apputil.cpp. They are used when the code sample is being compiled for ANSI strings (the default in the makefiles). The service functions that the surrogates stand in place of support only Unicode string parameters. This forces some string conversions from ANSI to Unicode before the real COM/OLE service call is made inside the surrogate.

For example, if UNICODE is not defined during compiling, any calls in the samples to the **WriteFmtUserTypeStg** COM service function are actually changed by the macros into calls to an A\_WriteFmtUserTypeStg function that is implemented in APPUTIL.CPP. This function accepts the input ANSI string pointer, converts it to a Unicode copy, and passes that Unicode copy as the string parameter in a call to the actual **WriteFmtUserTypeStg** function.

Here is A\_WriteFmtUserTypeStg from Apputil.cpp.

``` syntax
STDAPI A_WriteFmtUserTypeStg(
           IStorage* pIStorage,
           CLIPFORMAT ClipFmt,
           LPSTR pszUserType)
  {
    HRESULT hr = E_INVALIDARG;
    WCHAR wszUc[MAX_PATH];

    if (NULL != pszUserType)
    {
      // Convert from ANSI in pszUserType to Unicode in wszUc.
      AnsiToUc(pszUserType, wszUc, MAX_PATH);

      // Use the Unicode string in the actual service call.
      hr = WriteFmtUserTypeStg(pIStorage, ClipFmt, wszUc);
    }

    return hr;
  }
```

 

 




