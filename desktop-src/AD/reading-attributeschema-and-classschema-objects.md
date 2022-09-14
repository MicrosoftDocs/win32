---
title: Reading attributeSchema and classSchema Objects
description: This topic provides code examples and guidelines for reading directly from attributeSchema and classSchema objects in the schema container.
ms.assetid: a60558e1-88a1-493c-9340-a90143b11f60
ms.tgt_platform: multiple
keywords:
- Reading attributeSchema and classSchema Objects AD
- objects AD , Reading attributeSchema and classSchema Objects
ms.topic: article
ms.date: 05/31/2018
---

# Reading attributeSchema and classSchema Objects

This topic provides code examples and guidelines for reading directly from **attributeSchema** and **classSchema** objects in the schema container. Be aware that, in most programming situations, when you must read data about a class or attribute definition, it is more effective to read data from the abstract schema as described in [Reading the Abstract Schema](reading-the-abstract-schema.md).

The interfaces and techniques used to read from the schema container are those used to read any object in Active Directory Domain Services. The guidelines include:

-   To bind to the schema container, obtain its distinguished name which can be retrieved by binding to rootDSE and reading the **schemaNamingContext** property, as described in [Serverless Binding and RootDSE](serverless-binding-and-rootdse.md).
-   Use an [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) pointer for the schema container to enumerate the **attributeSchema** and **classSchema** objects.
-   Use the [**IADs**](/windows/desktop/api/iads/nn-iads-iads) or [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) interface to retrieve the properties of an **attributeSchema** and **classSchema** object.
-   Use the [**ADsOpenObject**](/windows/desktop/api/adshlp/nf-adshlp-adsopenobject) or [**ADsGetObject**](/windows/desktop/api/adshlp/nf-adshlp-adsgetobject) functions to bind directly to an **attributeSchema** or **classSchema** object.
-   If you are reading multiple **attributeSchema** or **classSchema** objects, you can increase performance by binding to an [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) pointer on the schema container and using the [**IADsContainer.GetObject**](/windows/desktop/api/iads/nf-iads-iadscontainer-getobject) method to bind to the individual class and attribute objects. This is more efficient than making repeated [**ADsOpenObject**](/windows/desktop/api/adshlp/nf-adshlp-adsopenobject) or [**ADsGetObject**](/windows/desktop/api/adshlp/nf-adshlp-adsgetobject) calls to bind to the individual class and attribute objects. Use the **cn** attribute to build the relative path for the **IADsContainer.GetObject** call (for example, "cn=user" for the **classSchema** object for the user class).
-   Use an [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) pointer for the schema container to query the schema for attributes or classes that match a search filter.

For a code example that demonstrates different methods of searching for schema objects, see [Example Code for Searching for Schema Objects](example-code-for-searching-for-schema-objects.md).

The following C++ code example binds to an [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) pointer on the schema container and then uses the [**ADsBuildEnumerator**](/windows/desktop/api/adshlp/nf-adshlp-adsbuildenumerator) and [**ADsEnumerateNext**](/windows/desktop/api/adshlp/nf-adshlp-adsenumeratenext) functions to enumerate its contents. Be aware that the enumeration includes all **attributeSchema** and **classSchema** objects as well as a single **subSchema** object, which is the abstract schema.

For each enumerated object, the code example uses the [**IADs.Class**](/windows/desktop/ADSI/iads-property-methods) property to determine whether it is an **attributeSchema** or **classSchema** object. The code example shows how to read the properties that are unavailable from the abstract schema.


```C++
//  Add activeds.lib to the project.
//  Add adsiid.lib to the project.

#include "stdafx.h"
#include <windows.h>
#include <stdio.h>
#include <ole2.h>
#include <activeds.h>
#include <atlbase.h>

//  Forward declarations.
void ProcessAttribute(IADs *pChild);
void ProcessClass(IADs *pChild);

//  Entry point for the application.
int wmain(int argc, WCHAR* argv[])
{
    HRESULT hr;

    hr = CoInitialize(NULL);
    if(SUCCEEDED(hr))
    {
        CComBSTR sbstrDSPath;
        CComVariant svar;
        IADs *pRootDSE = NULL;
        IADsContainer *pSchema = NULL;  
        IEnumVARIANT *pEnum = NULL;
        ULONG lFetch;
        CComBSTR sbstrClass; 
        DWORD dwClasses = 0, dwAttributes = 0, dwUnknownClass = 0;

        //  Bind to rootDSE to get the schemaNamingContext property.
        hr = ADsGetObject(L"LDAP://rootDSE", IID_IADs, (void**)&pRootDSE);
        if (FAILED(hr)) 
        {
            wprintf(L"ADsGetObject failed: 0x%x\n", hr);
            goto cleanup;
        }

        hr = pRootDSE->Get(CComBSTR("schemaNamingContext"), &svar);
        sbstrDSPath = "LDAP://";
        sbstrDSPath += svar.bstrVal;

        //  Bind to the actual schema container.
        wprintf(L"Binding to %s\n", sbstrDSPath);
        hr = ADsGetObject(sbstrDSPath, IID_IADsContainer, (void**) &pSchema);
        if (FAILED(hr)) 
        {
            wprintf(L"ADsGetObject to schema failed: 0x%x\n", hr);
            goto cleanup;
        }

        //  Enumerate the attribute and class objects in the schema container.
        hr = ADsBuildEnumerator(pSchema, &pEnum);
        if (FAILED(hr)) 
        {
            wprintf(L"ADsBuildEnumerator failed: 0x%x\n", hr);
            goto cleanup;
        }

        hr = ADsEnumerateNext(pEnum, 1, &svar, &lFetch);
        while(S_OK == hr && 1 == lFetch)
        {
            IADs *pChild = NULL;

            //  Get an IADs pointer on the child object.
            hr = V_DISPATCH(&svar)->QueryInterface(IID_IADs, (void**) &pChild);
            if (SUCCEEDED(hr)) 
            {
                //  Verify that this is a class, attribute, or subSchema object.
                hr = pChild->get_Class(&sbstrClass);
                if (SUCCEEDED(hr)) 
                {
                    //  Get data. This depends on type of schema element.
                    if (_wcsicmp(L"classSchema", sbstrClass) == 0)
                    {
                        dwClasses++;
                        wprintf(L"%s\n", sbstrClass);
                        ProcessClass(pChild);
                        wprintf(L"\n");
                    }
                    else if (_wcsicmp(L"attributeSchema", sbstrClass) == 0)
                    {
                        dwAttributes++;
                        wprintf(L"%s\n", sbstrClass);
                        ProcessAttribute(pChild);
                        wprintf(L"\n");
                    }
                    else if (_wcsicmp(L"subSchema", sbstrClass) == 0) 
                    {
                        wprintf(L"abstract schema");
                        wprintf(L"\n");
                    }
                    else
                    {
                        dwUnknownClass++;
                    }
                }

                pChild->Release();
            }

            hr = ADsEnumerateNext(pEnum, 1, &svar, &lFetch);
        }

        wprintf(L"Classes: %u\nAttributes: %u\nUnknown: %u\n", dwClasses, dwAttributes, dwUnknownClass);

cleanup:
        if (pRootDSE)
        {
            pRootDSE->Release();
        }

        if (pEnum)
        {
            ADsFreeEnumerator(pEnum);
        }

        if (pSchema)
        {
            pSchema->Release();
        }

    }    

    CoUninitialize();

    return 0;
}


//  PrintGUIDFromVariant
//  Prints a GUID in string format.
void PrintGUIDFromVariant(VARIANT varGUID)
{
    HRESULT hr;
    void HUGEP *pArray;
    WCHAR szGUID[40];
    LPGUID pGUID;

    DWORD dwLen = sizeof(GUID);

    hr = SafeArrayAccessData(V_ARRAY(&varGUID), &pArray);
    if(SUCCEEDED(hr))
    {
        pGUID = (LPGUID)pArray;

        //  Convert GUID to string.
        StringFromGUID2(*pGUID, szGUID, 40); 

        //  Print GUID.
        wprintf(L",%s",szGUID);

        SafeArrayUnaccessData(V_ARRAY(&varGUID));
    }
}


// PrintADSPropertyValue
void PrintADSPropertyValue(VARIANT var, BSTR bstrPropName, HRESULT hr) 
{
    if (E_ADS_PROPERTY_NOT_FOUND == hr)
    {
        wprintf(L"-- not set --\n");
    }
    else if (FAILED(hr))
    {
        wprintf(L"get %s failed: 0x%x\n", bstrPropName, hr);
    }
    else 
    {
        switch (var.vt) 
        {
        case VT_BSTR:
            wprintf(L"%s\n", var.bstrVal);
            break;

        case VT_I4:
            wprintf(L"%u\n", var.iVal);
            break;

        case VT_BOOL:
            wprintf(L"%s\n", var.boolVal ? L"TRUE" : L"FALSE");
            break;

        default:
            wprintf(L"-- ??? --\n");
        }
    }
}

//  ProcessAttribute
//  Gets information about an attributeClass object.
void ProcessAttribute(IADs *pChild)
{
    HRESULT hr;
    CComVariant svar;
    CComBSTR sbstrPropName;

    //  Get the attribute Common-Name (cn) property. 
    sbstrPropName = "cn";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the attribute lDAPDisplayName.
    sbstrPropName = "lDAPDisplayName";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class linkID. 
    sbstrPropName = "linkID";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the attribute schemaIDGUID. 
    sbstrPropName = "schemaIDGUID";
    hr = pChild->Get(sbstrPropName, &svar);
    if (E_ADS_PROPERTY_NOT_FOUND == hr)
    {
        wprintf(L"-- not set --\n");
    }
    else if(SUCCEEDED(hr))
    {
        PrintGUIDFromVariant(svar);
    }

    //  Get the attribute attributeSecurityGUID. 
    sbstrPropName = "attributeSecurityGUID";
    hr = pChild->Get(sbstrPropName, &svar);
    if (E_ADS_PROPERTY_NOT_FOUND == hr)
    {
        wprintf(L"-- not set --\n");
    }
    else if (SUCCEEDED(hr))
    {
        PrintGUIDFromVariant(svar);
    }

    //  Get the attribute attributeSyntax property. 
    sbstrPropName = "attributeSyntax";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the attribute's oMSyntax property. 
    sbstrPropName = "oMSyntax";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);
}


//  ProcessClass
//  Gets information about a schema class.
void ProcessClass(IADs *pChild)
{
    HRESULT hr;
    CComVariant svar;
    CComBSTR sbstrPropName;

    //  Get the class cn.
    sbstrPropName = "cn";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class lDAPDisplayName.
    sbstrPropName = "lDAPDisplayName";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class schemaIDGUID. 
    sbstrPropName = "schemaIDGUID";
    hr = pChild->Get(sbstrPropName, &svar);
    if (FAILED(hr))
    {
        wprintf(L",get schemaIDGUID failed: 0x%x", hr);
    }
    else 
    {
        PrintGUIDFromVariant(svar);
    }

    //  Get the class adminDescription property. 
    sbstrPropName = "adminDescription";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class adminDisplayName property. 
    sbstrPropName = "adminDisplayName";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class rDNAttID. 
    sbstrPropName = "rDNAttID";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class defaultHidingValue. 
    sbstrPropName = "defaultHidingValue";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class defaultObjectCategory. 
    sbstrPropName = "defaultObjectCategory";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class systemOnly value.
    sbstrPropName = "systemOnly";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);

    //  Get the class defaultSecurityDescriptor.
    sbstrPropName = "defaultSecurityDescriptor";
    hr = pChild->Get(sbstrPropName, &svar);
    PrintADSPropertyValue(svar, sbstrPropName, hr);
}
```



 

 