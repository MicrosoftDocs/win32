---
title: Interpreting Arguments and Strings Based on the Locale ID
description: Some methods or properties need to interpret arguments based on the LCID.
ms.assetid: 59ac04d3-d898-4af8-8f6c-c94791cf1c3d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interpreting Arguments and Strings Based on the Locale ID

Some methods or properties need to interpret arguments based on the LCID. These methods or properties can require that an LCID be passed as an argument. Therefore, properties should be designed to have an LCID parameter.

The following object description language example implements a property that takes a LCID.


```C++
[
   uuid(83219430-CB36-11cd-B774-00DD01103DE1),
   helpstring("Bank Account object."),
   oleautomation,
   dual
   ]
   interface IBankAccount : IDispatch
   {
[propget, helpstring("Returns account balance formatted for the country/region described by localeID.")]
HRESULT CheckingBalance([in, lcid] long localeID, [out, retval] BSTR* retval);
      :
   }
 
```



In the following example, get\_CheckingBalance returns a currency string that contains the balance in the checking account. The currency string should be correctly formatted depending on the locale that is passed in. ConvertCurrency is a private function that converts the checking balance to the currency of the country/region described by the LCID. The string form of converted currency is placed in m\_szBalance. [**GetCurrencyFormat**](https://msdn.microsoft.com/library/windows/desktop/dd318083) is a function that formats a currency string for the given locale.

The following information is contained in a header file:


```C++
class CBankAccount : public IBankAccount
{
   public:
   // IUnknown methods (omitted).
      :

   // IDispatch methods (omitted).
      :

   // IBankAccount methods.
   STDMETHOD(get_CheckingBalance)(long llcid, BSTR * pbstr);
      :
}
 
```



The following information is contained in a .cpp file. Error checking is omitted for brevity:


```C++
STDMETHODIMP
CBankAccount::get_CheckingBalance(long llcid, BSTR * pbstr)
{
   TCHAR ach[100];
   ConvertCurrency(llcid);
      GetCurrencyFormat(llcid, 0, m_szBalance, NULL, ach,
      sizeof(ach));
      *pbstr = SysAllocString(ach);       
     // Return currency string formatted according to locale ID. 

      return NOERROR;
}
 
```



The LCID is commonly used to parse strings that contain locale-dependent information. For example, a function that takes a string such as 6/11/96 needs the LCID to determine whether the month is June (6) or November (11). You should not use the LCID for output strings, including error strings. These strings should always be displayed in the current system language.

For more information on locale identifiers, primary and secondary language identifiers and sublanguage identifiers see [Locales](https://msdn.microsoft.com/library/windows/desktop/dd318716) and [Language Identifier Constants and Strings](https://msdn.microsoft.com/library/windows/desktop/dd318693).

 

 




