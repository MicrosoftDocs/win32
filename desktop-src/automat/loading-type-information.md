---
title: Loading Type Information
description: Demonstrates how to load locale-specific type library information.
ms.assetid: '60c467c6-0449-4269-a0ac-61ac485f33f5'
---

# Loading Type Information

The following example uses the Hello sample code to illustrate the **LoadTypeInfo** function that loads locale-specific type library information when an object is created.


```C++
LoadTypeInfo(&amp;phello->m_ptinfoEnglish, IID_IHello, LCID_ENGLISH);
LoadTypeInfo(&amp;phello->m_ptinfoGerman, IID_IHello, LCID_GERMAN);

// LoadTypeInfo - Gets type information of an object's interface from 
// the type library.
// 
// Parameters:
// pptinfo - Returns type information.
// clsid    - Interface ID of object in type library.
// lcid - Locale ID of type information to be loaded.
// 
// Return Value:
// HRESULT
// 
// 
HRESULT LoadTypeInfo(ITypeInfo ** pptinfo, REFCLSID clsid,
LCID lcid)
{
   HRESULT hr;
   LPTYPELIB ptlib = NULL;
   LPTYPEINFO ptinfo = NULL;

   if (pptinfo == NULL)
      return E_INVALIDARG;

   *pptinfo = NULL;

   // Load type library.
   hr = LoadRegTypeLib(LIBID_Hello, 2, 0, lcid, &amp;ptlib);
   if (FAILED(hr))
      return hr;

   // Get type information for interface of the object.
   hr = ptlib->GetTypeInfoOfGuid(clsid, &amp;ptinfo);
   if (FAILED(hr))
   {
      ptlib->Release();
      return hr;
   }

   ptlib->Release();
   *pptinfo = ptinfo;
   return NOERROR;
}
 
```



 

 




