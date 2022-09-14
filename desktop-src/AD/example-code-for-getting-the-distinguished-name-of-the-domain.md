---
title: Example Code for Getting the Distinguished Name of the Domain
description: This topic includes a code example that gets the distinguished name of the domain that the local computer is a member of by using serverless binding.
ms.assetid: 2b478c55-4683-48cd-bee9-385eea38d01d
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , getting the distinguished name of the domain
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Getting the Distinguished Name of the Domain

This topic includes a code example that gets the distinguished name of the domain that the local computer is a member of by using serverless binding.

The following Visual Basic code example gets the distinguished name of the domain that the local computer is a member of by using serverless binding.


```VB
Dim rootDSE As IADs
Dim DistinguishedName As String
 
Set rootDSE = GetObject("LDAP://rootDSE")
DistinguishedName = "LDAP://" & rootDSE.Get("defaultNamingContext")
```



The following C# code example gets the distinguished name of the domain that the local computer is a member of by using serverless binding.


```CSharp
DirectoryEntry RootDirEntry = new DirectoryEntry("LDAP://RootDSE");
Object distinguishedName = RootDirEntry.Properties["defaultNamingContext"].Value;
```



The following C/C++ code example gets the distinguished name of the domain that the local computer is a member of by using serverless binding.


```C++
IADs *pads;
hr = ADsGetObject(  L"LDAP://rootDSE",
                    IID_IADs, 
                    (void**)&pads);

if(SUCCEEDED(hr))
{
    VARIANT var;

    VariantInit(&var);
    
    hr = pads->Get(CComBSTR("defaultNamingContext"), &var);
    if(SUCCEEDED(hr))
    {
        if(VT_BSTR == var.vt)
        {
            wprintf(var.bstrVal);
        }
        
        VariantClear(&var);
    }
    
    pads->Release();
}
```



 

 




