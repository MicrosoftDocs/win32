---
title: Example Code for Using IADsProperty Interfaces to Access the Property Cache
description: The following code example shows how to use the IADsPropertyList, IADsPropertyEntry, and IADsPropertyValue interfaces with C++ and ADSI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d2ac3a1e-642c-451c-a79e-baa38dacb4a2
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Example Code ADSI , Using IADsProperty Interfaces to Access the Property Cache
- Example Code for Using IADsProperty Interfaces to Access the Property Cache ADSI
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Using IADsProperty Interfaces to Access the Property Cache

The following code example shows how to use the [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist), [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry), and [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue) interfaces with C++ and ADSI.


```C++
HRESULT hr;
BSTR    bstr;
VARIANT var;
IDispatch *pDispatch;
IADsPropertyList *pPropList;
IADsPropertyEntry *pEntry;
IADsPropertyValue *pValue;
LONG  lADsType;
IADs *pADs=NULL;
 
//////////////////////////////////////////////////////////
// Be aware that, for brevity, error handling is omitted.
//////////////////////////////////////////////////////////
 
hr = ADsGetObject(L"LDAP://DC=Sales,DC=Fabrikam,DC=Com", IID_IADs, (void**) &amp;pADs);
 
///////////////////////////////////////////////////////////////////
// Retrieve objects prior to calling IADsProperty* methods.
///////////////////////////////////////////////////////////////////
hr = pADs->GetInfo();
hr = pADs->QueryInterface(IID_IADsPropertyList, (void**) &amp;pPropList);
pADs->Release();
 
//////////////////////////////////////////////////
// Get the DC property.
//////////////////////////////////////////////////
hr = pPropList->GetPropertyItem(CComBSTR("dc"), ADSTYPE_CASE_IGNORE_STRING, &amp;var);
 
if (SUCCEEDED(hr))
{
    //////////////////////////////////////////
    // Get the IADsPropertyEntry interface.
    //////////////////////////////////////////
    pDispatch = V_DISPATCH( &amp;var );
    hr = pDispatch->QueryInterface(IID_IADsPropertyEntry, (void**)&amp;pEntry);
    VariantClear(&amp;var);
 
    if (SUCCEEDED(hr))
    {
        VARIANT  varValueArray;
        VARIANT  varValue;
        long   idx=0;
 
        ///////////////////////////////////////////////
        // get_Values return array of VT_DISPATCH.
        ///////////////////////////////////////////////
        hr = pEntry->get_Values(&amp;varValueArray);
        hr = pEntry->get_ADsType(&amp;lADsType);
        hr = SafeArrayGetElement(V_ARRAY(&amp;varValueArray), &amp;idx, &amp;varValue);
        pEntry->Release();  // Release entry.
 
        /////////////////////////////////////
        // IADsPropertyValue
        /////////////////////////////////////
        pDispatch = (IDispatch*) V_DISPATCH(&amp;varValue);
        hr = pDispatch->QueryInterface(IID_IADsPropertyValue, 
                                       (void**) &amp;pValue);
        pDispatch->Release();
 
        /////////////////////////////
        // Display the value.
        /////////////////////////////
        hr = pValue->get_CaseIgnoreString(&amp;bstr);
        printf("%S\n", bstr);
        SysFreeString(bstr);
        pValue->Release();
    } 
}
```



The following code example shows how to use the [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist), [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry), and [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue) interfaces using Visual Basic and ADSI.


```VB
Dim propList As IADsPropertyList
Dim propEntry As IADsPropertyEntry
Dim propVal As IADsPropertyValue
Dim count As Long
 
Set propList = GetObject("LDAP://dc01/DC=Fabrikam,DC=com")
 
propList.GetInfo
count = propList.PropertyCount
Debug.Print "No of Property Found: " & count
 
For i = 0 To count - 1
    ' Each item in the property list has a property entry.
    Set propEntry = propList.Item(i)
    Debug.Print propEntry.Name
    Debug.Print propEntry.ADsType
    
    ' Each value in property entry has property values.
    For Each v In propEntry.Values
        Set propVal = v
        Debug.Print propVal.ADsType
    Next
Next
```



 

 




