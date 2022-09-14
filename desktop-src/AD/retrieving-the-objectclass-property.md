---
title: Retrieving the objectClass Attribute
description: The objectClass attribute contains the class of which the object is an instance, as well as all classes from which that class is derived.
ms.assetid: 6066d9c3-f97b-482a-88c7-0fde1dc2f4c4
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the objectClass Attribute

The **objectClass** attribute contains the class of which the object is an instance, as well as all classes from which that class is derived. For example, the **user** class inherits from **top**, **person**, and **organizationalPerson**; therefore, the **objectClass** attribute contains the names of those classes, as well as user. So, how do you find out what class the object is an instance of? The **objectClass** attribute is the only attribute with multiple values that has ordered values. The first value is the top of the class hierarchy, which is the top class, and the last value is the most derived class, which is the class that the object is an instance of.

The following function takes a pointer to a column containing an **objectClass** attribute and returns the instantiated **objectClass** of the object.


```C++
HRESULT GetClass(ADS_SEARCH_COLUMN *pcol, LPOLESTR *ppClass)
{
  if (!pcol)
    return E_POINTER;
 
  HRESULT hr = E_FAIL;
  if (ppClass)
  {
    LPOLESTR szClass = new OLECHAR[MAX_PATH];
    wcscpy_s(szClass, L"");
    if ( _wcsicmp(pcol->pszAttrName,L"objectClass") == 0 )
    {
      for (DWORD x = 0; x< pcol->dwNumValues; x++)
      {
        wcscpy_s(szClass, pcol->pADsValues[x].CaseIgnoreString);
      }
    }
    if (0==wcscmp(L"", szClass))
    {
      hr = E_FAIL;
    }
    else
    {
      //Allocate memory for string.
      //Caller must free using CoTaskMemFree.
      *ppClass = (OLECHAR *)CoTaskMemAlloc (
                             sizeof(OLECHAR)*(wcslen(szClass)+1));
      if (*ppClass)
      {
        wcscpy_s(*ppClass, szClass);
        hr = S_OK;
      }
      else
      hr=E_FAIL;
    }
  }
  return hr;
}
```



 

 




