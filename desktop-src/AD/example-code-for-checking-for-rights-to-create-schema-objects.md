---
title: Example Code for Checking for Rights to Create Schema Objects
description: The following C/C++ code example shows a function that checks the allowedChildClassesEffective attribute on the schema container (IADs pointer to schema container is passed as a parameter) for the attributeSchema and classSchema classes.
ms.assetid: 3abc2351-a3cf-4a6c-9a13-15dd51723883
ms.tgt_platform: multiple
keywords:
- Example Code for Checking for Rights to Create Schema Objects AD
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Checking for Rights to Create Schema Objects

The following C/C++ code example shows a function that checks the **allowedChildClassesEffective** attribute on the schema container (IADs pointer to schema container is passed as a parameter) for the **attributeSchema** and **classSchema** classes. It returns **S\_OK** if both classes are listed in **allowedChildClassesEffective**. If both are not, it returns **S\_FALSE**.


```C++

// Function takes an IADs pointer to schema container as a parameter.
 
HRESULT HasSchemaAdditionRights(IADs *pSchema)
{
if (!pSchema)
  return E_POINTER;
HRESULT hr = E_FAIL;
VARIANT var;
VARIANT *pVar;
// Check access rights.
BOOL bIsAddAttributeAllowed = FALSE;
BOOL bIsAddClassAllowed = FALSE;
// Get AllowedChildClassesEffective. It is constructed;
// therefore, you must use GetInfoEx to explicitly 
// get it into the cache.
LPOLESTR pwszArray[] = {L"allowedChildClassesEffective"};
DWORD dwArrayItems = sizeof(pwszArray)/sizeof(LPOLESTR);
VARIANT vArray;
VariantInit(&vArray);
// Build a Variant of array type, using the specified string array.
hr = ADsBuildVarArrayStr(pwszArray, dwArrayItems, &vArray);
if (SUCCEEDED(hr))
{
  hr = pSchema->GetInfoEx(vArray,0L);
  if (SUCCEEDED(hr))
  {
    hr = pSchema->GetEx(CComBSTR("allowedChildClassesEffective"), 
                        &var);
    if (SUCCEEDED(hr))
    {
       hr = SafeArrayAccessData((SAFEARRAY*)(var.pparray), 
                                (void HUGEP* FAR*)&pVar);
       long lLBound, lUBound;
       // One-dimensional array. Get the bounds for the array.
       hr = SafeArrayGetLBound((SAFEARRAY*)(var.pparray), 
                               1,
                               &lLBound);
       hr = SafeArrayGetUBound((SAFEARRAY*)(var.pparray), 
                               1, 
                               &lUBound);
       // Get the count of elements
       long cElements = lUBound-lLBound + 1;
       // Get the elements of the array.
       if (SUCCEEDED(hr))
       {
        for (int i = 0; i < cElements; i++ ) 
        {
          // Check each element to verify that attributeSchema 
          // or classSchema is there.
          if (VT_BSTR == pVar[i].vt)
          {
            if (0==_wcsicmp(L"attributeSchema", pVar[i].bstrVal))
              bIsAddAttributeAllowed = TRUE;
            else if (0==_wcsicmp(L"classSchema", pVar[i].bstrVal))
              bIsAddClassAllowed = TRUE;
          }
        }
        if (bIsAddAttributeAllowed && bIsAddClassAllowed)
          hr = S_OK;
        else
          hr = S_FALSE;
       }
    }
    VariantClear(&var);
  }
}
 
return hr;
 
};
```



 

 




