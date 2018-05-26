---
Description: Several of the LSA Policy functions use the LSA\_UNICODE\_STRING structure to store string information. This structure stores the string and its length information.
ms.assetid: 8a02cbb4-0b59-4c1e-9831-592a2005905e
title: Using LSA Unicode Strings
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using LSA Unicode Strings

Several of the LSA Policy functions use the [**LSA\_UNICODE\_STRING**](/windows/win32/lsalookup/ns-lsalookup-_lsa_unicode_string?branch=master) structure to store string information. This structure stores the string and its length information.

The following code implements a function that converts **LPWSTR** data to [**LSA\_UNICODE\_STRING**](/windows/win32/lsalookup/ns-lsalookup-_lsa_unicode_string?branch=master) structures:


```C++
#include <windows.h>

bool InitLsaString(
  PLSA_UNICODE_STRING pLsaString,
  LPCWSTR pwszString
)
{
  DWORD dwLen = 0;

  if (NULL == pLsaString)
      return FALSE;

  if (NULL != pwszString) 
  {
      dwLen = wcslen(pwszString);
      if (dwLen > 0x7ffe)   // String is too large
          return FALSE;
  }

  // Store the string.
  pLsaString->Buffer = (WCHAR *)pwszString;
  pLsaString->Length =  (USHORT)dwLen * sizeof(WCHAR);
  pLsaString->MaximumLength= (USHORT)(dwLen+1) * sizeof(WCHAR);

  return TRUE;
}
```



 

 



