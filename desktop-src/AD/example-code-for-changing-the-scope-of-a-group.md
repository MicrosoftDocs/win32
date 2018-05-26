---
title: Example Code for Changing the Scope of a Group
description: This topic contains example code for changing the scope of a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4ae61101-f123-44bd-8bec-bade51d22217
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , changing the scope of a group
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Example Code for Changing the Scope of a Group

The following C++ code example changes the scope of a group.


```C++

    WCHAR *pwszLDAPPath = 
        L"LDAP://CN=mygroup,OU=myou,DC=Fabrikam,DC=com";
 
    HRESULT hr;
    IADsGroup * pGroup = NULL;
 
    // Initialize COM.
    CoInitialize(0);
 
    // Bind to the passed container. 
    hr = ADsGetObject( pwszLDAPPath, IID_IADsGroup,(void **)&amp;pGroup);
 
    if (SUCCEEDED(hr))
    {
        VARIANT vValue;
        BSTR    bsValue = SysAllocString(L"groupType");
        VariantInit(&amp;vValue);
    // Set a new GroupType Value.
        vValue.vt = VT_I4;
        vValue.lVal = ADS_GROUP_TYPE_GLOBAL_GROUP ;
 
        hr = pGroup->Put(bsValue,vValue);
        hr = pGroup->SetInfo();
        pGroup->Release();
        pGroup= NULL;
        SysFreeString(bsValue);
    }
 
    CoUninitialize();
```



The following Visual Basic code example changes the scope of a group.


```VB
Dim x as IADs
On Error GoTo CleanUp
Set x = GetObject("LDAP://CN=mygroup,OU=myou,DC=Fabrikam,DC=com")
x.Put "groupType", 
    ADS_GROUP_TYPE_UNIVERSAL_GROUP|ADS_GROUP_TYPE_SECURITY_ENABLED
Exit Sub

CleanUp:
    MsgBox("An error has occurred.")
    x = Nothing
```



 

 




