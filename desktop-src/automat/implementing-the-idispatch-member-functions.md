---
title: Implementing the IDispatch Member Functions
description: The IDispatch member functions must be implemented in such a way as to take into account any language-specific features.
ms.assetid: 'a6315b63-0139-4a5d-a65b-2660740889c4'
---

# Implementing the IDispatch Member Functions

The following example code from the Hello sample implements language-sensitive versions of [**GetTypeInfoCount**](idispatch-gettypeinfocount.md), [**GetIDsOfNames**](idispatch-getidsofnames.md), and [**Invoke**](idispatch-invoke.md). Note that **Invoke** does not check the LCID, but merely passes it to [DispInvoke](69B89E5C-2A04-4A6A-BEB0-18E68F8866AC). **GetTypeInfoCount** does not contain any language-specific information; however, [**GetTypeInfo**](idispatch-gettypeinfo.md) does.

The [**IDispatch**](idispatch.md) member functions must be implemented in such a way as to take into account any language-specific features. [**DispInvoke**](dispinvoke.md) is passed only the U.S. English type information pointer.


```C++
STDMETHODIMP
CHello::GetTypeInfoCount(UINT * pctinfo)
{
   if (pctinfo == NULL)
      return E_INVALIDARG;

   *pctinfo = 1;
   return NOERROR;
}

STDMETHODIMP
CHello::GetTypeInfo(
      UINT itinfo,
      LCID lcid,
      ITypeInfo ** pptinfo)
{
   LPTYPEINFO ptinfo;

   if (pptinfo == NULL)
      return E_INVALIDARG;

   *pptinfo = NULL;

   if(itinfo != 0)
      return DISP_E_BADINDEX;

   if(lcid == LOCALE_SYSTEM_DEFAULT || lcid == 0)
      lcid = GetSystemDefaultLCID();

   if(lcid == LOCALE_USER_DEFAULT)
      lcid = GetUserDefaultLCID();

   switch(lcid)
   {
      case LCID_GERMAN:
         ptinfo = m_ptinfoGerman;
         break;

      case LCID_ENGLISH:
         ptinfo = m_ptinfoEnglish;
         break;

      default:
         return DISP_E_UNKNOWNLCID;
   }

   ptinfo->AddRef();
   *pptinfo = ptinfo;
   return NOERROR;
}

STDMETHODIMP
CHello::GetIDsOfNames(
      REFIID riid,
      OLECHAR ** rgszNames,
      UINT cNames,
      LCID lcid,
      DISPID * rgdispid)
{
   LPTYPEINFO ptinfo;

   if(lcid == LOCALE_SYSTEM_DEFAULT || lcid == 0)
      lcid = GetSystemDefaultLCID();

   if(lcid == LOCALE_USER_DEFAULT)
      lcid = GetUserDefaultLCID();

   switch(lcid)
   {
      case LCID_GERMAN:
         ptinfo = m_ptinfoGerman;
         break;

      case LCID_ENGLISH:
         ptinfo = m_ptinfoEnglish;
         break;

      default:
         return DISP_E_UNKNOWNLCID;
   }
// We are delegating input validation to DispGetIDsOfNames.
// Real-world applications may require additional validation.

   return DispGetIDsOfNames(ptinfo, rgszNames, cNames, rgdispid);
}

STDMETHODIMP
CHello::Invoke(
   DISPID dispidMember,
   REFIID riid,
   LCID lcid,
   WORD wFlags,
   DISPPARAMS * pdispparams,
   VARIANT * pvarResult,
   EXCEPINFO * pexcepinfo,
   UINT * puArgErr)
{ 
// We are delegating input validation to DispInvoke.
// Real-world applications may require additional validation.

   return DispInvoke(
   this, m_ptinfoEnglish,
   dispidMember, wFlags, pdispparams,
   pvarResult, pexcepinfo, puArgErr); 
}
 
```



 

 




