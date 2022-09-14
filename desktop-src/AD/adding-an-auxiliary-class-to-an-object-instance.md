---
title: Adding an Auxiliary Class to an Object Instance
description: The following code examples show how to use ADSI and LDAP to dynamically add an auxiliary class to an existing object instance.
ms.assetid: 739dd372-3bda-4d94-8daf-f71e3091cfb6
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Adding an Auxiliary Class to an Object Instance

The following code examples show how to use ADSI and LDAP to dynamically add an auxiliary class to an existing object instance. The examples assume that an auxiliary class named **vehicle** is defined in the Active Directory schema, and that the **vehicle** class has a **vin** attribute.

When you dynamically add an auxiliary class to an object instance, you must simultaneously specify values for any mandatory **mustHave** attributes in the class. The following examples show how to do this with the "vin" attribute, which is assumed to be mandatory.

The following C++ example binds to an object, and uses [**IADs.PutEx**](/windows/desktop/api/iads/nf-iads-iads-putex) to append the auxiliary class to the list of classes in the object's **objectClass** property. Then the example uses [**IADs.Put**](/windows/desktop/api/iads/nf-iads-iads-put) to set the value of the **vin** attribute. Finally, it calls [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) to commit the changes to the directory.


```C++
LPWSTR pszAuxClass[]={L"vehicle"};
LPWSTR pszVIN[]={L"df897dsfsa-0"};
VARIANT var;

VariantInit(&var);

ADsOpenObject(L"cn=johnd,cn=users,dc=fabrikam,dc=com", 
    NULL, 
    NULL, 
    ADS_SECURE_AUTHENTICATION, 
    IID_IADs,  
    (VOID**)&pIADs);

ADsBuildVarArrayStr(pszAuxClass, 1, &var);
pIADs->PutEx(ADS_PROPERTY_APPEND, CComBSTR("objectClass"), var);
ADsBuildVarArrayStr( pszVIN, 1, &var);
pIADs->Put(CComBSTR("vin"), var);
pIADs->SetInfo();

if(pIADs)
    pIADs->Release();

VariantClear(&var);
```



 

 