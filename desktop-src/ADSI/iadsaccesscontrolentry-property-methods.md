---
title: IADsAccessControlEntry Property Methods
description: The property methods of the IADsAccessControlEntry interface get or set the properties described in the following table. For more information, see Interface Property Methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: dce11723-0e30-4baa-8666-0a32f0968ebb
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- IADsAccessControlEntry Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsAccessControlEntry Property Methods
- IADsAccessControlEntry.AccessMask
- IADsAccessControlEntry.get_AccessMask
- IADsAccessControlEntry.put_AccessMask
- IADsAccessControlEntry.AceType
- IADsAccessControlEntry.get_AceType
- IADsAccessControlEntry.put_AceType
- IADsAccessControlEntry.AceFlags
- IADsAccessControlEntry.get_AceFlags
- IADsAccessControlEntry.put_AceFlags
- IADsAccessControlEntry.Flags
- IADsAccessControlEntry.get_Flags
- IADsAccessControlEntry.put_Flags
- IADsAccessControlEntry.ObjectType
- IADsAccessControlEntry.get_ObjectType
- IADsAccessControlEntry.put_ObjectType
- IADsAccessControlEntry.InheritedObjectType
- IADsAccessControlEntry.get_InheritedObjectType
- IADsAccessControlEntry.put_InheritedObjectType
- IADsAccessControlEntry.Trustee
- IADsAccessControlEntry.get_Trustee
- IADsAccessControlEntry.put_Trustee
api_location:
- Activeds.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IADsAccessControlEntry Property Methods

The property methods of the [**IADsAccessControlEntry**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master) interface get or set the properties described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**AccessMask**
</dt> <dd> <dl>

Contains a set of flags that specifies access privileges for the object. Valid values for Active Directory objects are defined in the [**ADS\_RIGHTS\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0001?branch=master) enumeration.

For more information and a list of possible values for file or file share objects, see [File Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/aa364399).

For more information and a list of possible values for registry objects, see [Registry Key Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/ms724878).

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AccessMask(
  [out] LONG* plnAccessMask
);
HRESULT put_AccessMask(
  [in] LONG lnAccessMask
);
```


</dt> </dl> </dd> <dt>

**AceFlags**
</dt> <dd> <dl>

Contains a set of flags that specifies if other containers or objects can inherit the ACE. Valid values for Active Directory object are defined in the [**ADS\_ACEFLAG\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0003?branch=master) enumeration.

For more information and possible values for file, file share, and registry objects, see the **AceFlags** member of the [**ACE\_HEADER**](https://msdn.microsoft.com/library/windows/desktop/aa374919) structure.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AceFlags(
  [out] LONG* plnAceFlags
);
HRESULT put_AceFlags(
  [in] LONG lnAceFlags
);
```


</dt> </dl> </dd> <dt>

**AceType**
</dt> <dd> <dl>

Contains a value that indicates the type of ACE. Valid values for Active Directory objects are defined in the [**ADS\_ACETYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0002?branch=master) enumeration.

For more information and possible values for file, file share, and registry objects, see the **AceType** member of the [**ACE\_HEADER**](https://msdn.microsoft.com/library/windows/desktop/aa374919) structure.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AceType(
  [out] LONG* plAceType
);
HRESULT put_AceType(
  [in] LONG lnAceType
);
```


</dt> </dl> </dd> <dt>

**Flags**
</dt> <dd> <dl>

A flag that indicates if the ACE has an object type or inherited object type. Valid flags are defined in the [**ADS\_FLAGTYPE\_ENUM**](/windows/win32/Iads/ne-iads-__midl___midl_itf_ads_0001_0048_0004?branch=master) enumeration.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Flags(
  [out] LONG* lnflags
);
HRESULT put_Flags(
  [in] LONG lnflags
);
```


</dt> </dl> </dd> <dt>

**InheritedObjectType**
</dt> <dd> <dl>

A flag that indicates the type of a child object of an ADSI object. Its value is a **GUID** to an object in string format. When such a **GUID** is set, the ACE applies only to the object referred to by the **GUID**.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_InheritedObjectType(
  [out] BSTR* bstrInheritedObjectType
);
HRESULT put_InheritedObjectType(
  [in] BSTR bstrInheritedObjectType
);
```


</dt> </dl> </dd> <dt>

**ObjectType**
</dt> <dd> <dl>

A flag that indicates the ADSI object type. Its value is a **GUID** to a property or an object in string format. The **GUID** refers to a property when **ADS\_RIGHT\_DS\_READ\_PROP** and **ADS\_RIGHT\_DS\_WRITE\_PROP** access masks are used. The **GUID** specifies an object when **ADS\_RIGHT\_DS\_CREATE\_CHILD** and **ADS\_RIGHT\_DS\_DELETE\_CHILD** access masks are used.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ObjectType(
  [out] BSTR* bstrObjectType
);
HRESULT put_ObjectType(
  [in] BSTR bstrObjectType
);
```


</dt> </dl> </dd> <dt>

**Trustee**
</dt> <dd> <dl>

Contains the name of the account that the ACE applies to.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Trustee(
  [out] BSTR* pbstrSecurityId
);
HRESULT put_Trustee(
  [in] BSTR bstrSecurityId
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following code example shows how to add entries to a discretionary ACL using the [**IADsAccessControlEntry**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master) property methods.


```VB
Dim x As IADs
Dim sd As IADsSecurityDescriptor
Dim ace As IADsAccessControlEntry
Dim Dacl As IADsAccessControlList
Dim Ace1 As New AccessControlEntry
Dim Ace2 As New AccessControlEntry

On Error GoTo Cleanup
 
Set x = GetObject("LDAP://OU=Sales, DC=Fabrikam,DC=com")
Set sd = x.Get("ntSecurityDescriptor")
Set Dacl = sd.DiscretionaryAcl
 
' Show the existing ACEs.
For Each ace In Dacl
  Debug.Print ace.Trustee
Next
 
 
' Setup the first ACE.
Ace1.AccessMask = -1 'Full Permission (Allowed)
Ace1.AceType = ADS_ACETYPE_ACCESS_ALLOWED
Ace1.AceFlags = ADS_ACEFLAG_INHERIT_ACE
Ace1.Trustee = "ACTIVED\Administrator"
 
' Setup the 2nd ACE.
Ace2.AccessMask = -1 'Full Permission (Denied)
Ace2.AceType = ADS_ACETYPE_ACCESS_DENIED
Ace2.AceFlags = ADS_ACEFLAG_INHERIT_ACE
Ace2.Trustee = "ACTIVED\Andyhar"
 
' Add the ACEs to the Discretionary ACL.
Dacl.AddAce Ace1
Dacl.AddAce Ace2
 
sd.DiscretionaryAcl = Dacl
x.Put "ntSecurityDescriptor", Array(sd)
x.SetInfo

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If

    Set x = Nothing
    Set sd = Nothing
    Set ace = Nothing
    Set Dacl = Nothing
    Set Ace1 = Nothing
    Set Ace2 = Nothing
    Set obj = Nothing
    Set cls = Nothing
```



The following code example displays access-control entries.


```C++
IADs *pADs = NULL;
IDispatch *pDisp = NULL;
IADsSecurityDescriptor *pSD = NULL;
VARIANT var;
HRESULT hr = S_OK;
 
VariantInit(&amp;var);

hr = ADsOpenObject(L"LDAP://OU=Sales, DC=Fabrikam,DC=com",NULL,NULL,
                   ADS_SECURE_AUTHENTICATION, IID_IADs,(void**)&amp;pADs);
if(FAILED(hr)) {goto Cleanup;}

hr = pADs->Get(CComBSTR("ntSecurityDescriptor"),&amp;var);
if(FAILED(hr)) {goto Cleanup;}

pDisp = V_DISPATCH(&amp;var);

hr = pDisp->QueryInterface(IID_IADsSecurityDescriptor,(void**)&amp;pSD);
if(FAILED(hr)) {goto Cleanup;}
pDisp->Release();


pSD->get_DiscretionaryAcl(&amp;pDisp);

hr = pDisp->QueryInterface(IID_IADsAccessControlList,(void**)&amp;pACL);
if(FAILED(hr)) {goto Cleanup;}

hr = DisplayAccessInfo(pSD);
if(FAILED(hr)) {goto Cleanup;}
VariantClear(&amp;var);

Cleanup:
    if(pADs) pADs->Release();
    if(pDisp) pDisp->Release();
    if(pSD) pSD->Release();
    return hr;



HRESULT DisplayAccessInfo(IADsSecurityDescriptor *pSD)
{
    LPWSTR lpszFunction = L"DisplayAccessInfo";
    IDispatch *pDisp = NULL;
    IADsAccessControlList *pACL = NULL;
    IADsAccessControlEntry *pACE = NULL;
    IEnumVARIANT *pEnum = NULL;
    IUnknown *pUnk = NULL;
    HRESULT hr = S_OK;
    ULONG nFetch = 0;
    BSTR bstrValue = NULL;
    VARIANT var;
    LPWSTR lpszOutput = NULL;
    LPWSTR lpszMask = NULL;
    size_t nLength = 0;
    
    VariantInit(&amp;var);
    
    hr = pSD->get_DiscretionaryAcl(&amp;pDisp);
    if(FAILED(hr)){goto Cleanup;}
    hr = pDisp->QueryInterface(IID_IADsAccessControlList,(void**)&amp;pACL);
    if(FAILED(hr)){goto Cleanup;}
    
    hr = pACL->get__NewEnum(&amp;pUnk);
    if(FAILED(hr)){goto Cleanup;}
    
    hr = pUnk->QueryInterface(IID_IEnumVARIANT,(void**)&amp;pEnum);
    
    if(FAILED(hr)){goto Cleanup;}
    hr = pEnum->Next(1,&amp;var,&amp;nFetch);
    
    while(hr == S_OK)
    {
        if(nFetch==1)
        {
            if(VT_DISPATCH != V_VT(&amp;var))
            {
                goto Cleanup;
            }
            
            pDisp = V_DISPATCH(&amp;var);
            hr = pDisp->QueryInterface(IID_IADsAccessControlEntry,(void**)&amp;pACE);
            
            if(SUCCEEDED(hr))
            {
                lpszMask = L"Trustee: %s";
                hr = pACE->get_Trustee(&amp;bstrValue);
                nLength = wcslen(lpszMask) + wcslen(bstrValue) + 1;
                lpszOutput = new WCHAR[nLength];
                swprintf_s(lpszOutput,lpszMask,bstrValue);
                printf(lpszOutput);
                delete [] lpszOutput;
                SysFreeString(bstrValue);
                
                pACE->Release();
                pACE = NULL;
                pDisp->Release();
                pDisp = NULL;
            }       
            
            VariantClear(&amp;var);
        }       
        hr = pEnum->Next(1,&amp;var,&amp;nFetch);
    }
    
Cleanup:
    if(pDisp) pDisp->Release();
    if(pACL) pACL->Release();
    if(pACE) pACE->Release();
    if(pEnum) pEnum->Release();
    if(pUnk) pUnk->Release();
    if(szValue) SysFreeString(szValue);
    return hr;
}
```



## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl>   |
| IID<br/>                      | IID\_IADsAccessControlEntry is defined as B4F3A14C-9BDD-11D0-852C-00C04FD8D503<br/> |



## See also

<dl> <dt>

[**IADsAccessControlEntry**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)
</dt> <dt>

[**IADsAccessControlList**](/windows/win32/Iads/nn-iads-iadsaccesscontrollist?branch=master)
</dt> <dt>

[**IADsSecurityDescriptor**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)
</dt> </dl>

 

 





