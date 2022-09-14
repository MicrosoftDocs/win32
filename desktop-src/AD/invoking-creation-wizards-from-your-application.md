---
title: Invoking Creation Wizards from Your Application
description: An application or component can use the same directory service object creation wizards used by the Active Directory administrative MMC snap-ins. This is accomplished with the IDsAdminCreateObj interface.
ms.assetid: be4b6101-f795-403b-b93e-960759ac4f14
ms.tgt_platform: multiple
keywords:
- Invoking Creation Wizards from Your Application AD
ms.topic: article
ms.date: 05/31/2018
---

# Invoking Creation Wizards from Your Application

An application or component can use the same directory service object creation wizards used by the Active Directory administrative MMC snap-ins. This is accomplished with the [**IDsAdminCreateObj**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadmincreateobj) interface.

## Using the IDsAdminCreateObj Interface

An application or component (client) creates an instance of the [**IDsAdminCreateObj**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadmincreateobj) interface by calling [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) with the **CLSID\_DsAdminCreateObj** class identifier. COM must be initialized by calling [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) before **CoCreateInstance** is called.

The client then calls [**IDsAdminCreateObj::Initialize**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadmincreateobj-initialize) to initialize the [**IDsAdminCreateObj**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadmincreateobj) object. **IDsAdminCreateObj::Initialize** accepts an [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface pointer that represents the container that the object should be created in, and the class name of the object to be created. When creating user objects, it is also possible to specify an existing object that will be copied to the new object.

When the [**IDsAdminCreateObj**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadmincreateobj) object has been initialized, the client calls [**IDsAdminCreateObj::CreateModal**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadmincreateobj-createmodal) to display the object creation wizard.

Unlike most class and interface identifiers, **CLSID\_DsAdminCreateObj** and **IID\_ADsAdminCreateObj** are not defined in a library file. This means you must define the storage for these identifiers within your application. To do this, you must include the file initguid.h immediately before including dsadmin.h. The initguid.h file must only be included once in an application. The following code example shows how to include these files.


```C++
#include <initguid.h>
#include <dsadmin.h>
```



The following code example shows how the [**IDsAdminCreateObj**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadmincreateobj) interface can be created and used to start the object creation wizard for a user object.


```C++
//  Add activeds.lib to your project
//  Add adsiid.lib to your project

#include "stdafx.h"
#include <atlbase.h>
#include <atlstr.h>
#include "activeds.h"
#include <initguid.h> // Only include this in one source file
#include <dsadmin.h>

//  GetUserContainer() function binds to the user container
IADsContainer* GetUserContainer(void)
{
    IADsContainer *pUsers = NULL;
    HRESULT hr;
    IADs *pRoot;

    //  Bind to the rootDSE.
    hr = ADsGetObject(L"LDAP://rootDSE", IID_IADs, (LPVOID*)&pRoot);

    if(SUCCEEDED(hr))
    {
        VARIANT var;
        VariantInit(&var);
        CComBSTR sbstr(L"defaultNamingContext");

        //  Get the default naming context (domain) DN.
        hr = pRoot->Get(sbstr, &var);
        if(SUCCEEDED(hr) && (VT_BSTR == var.vt))
        {
            CStringW sstr(L"LDAP://CN=Users,");
            sstr += var.bstrVal;

            //  Bind to the User container.
            hr = ADsGetObject(sstr, IID_IADsContainer, (LPVOID*)&pUsers);

            VariantClear(&var);
        }
    }

    return pUsers;
}


//  The LaunchNewUserWizard() function launches the user wizard.
HRESULT LaunchNewUserWizard(IADs** ppAdsOut)
{
    if(NULL == ppAdsOut)
    {
        return E_INVALIDARG;
    }

    HRESULT hr;
    IDsAdminCreateObj* pCreateObj = NULL;

    hr = ::CoCreateInstance(CLSID_DsAdminCreateObj,
                            NULL, 
                            CLSCTX_INPROC_SERVER,
                            IID_IDsAdminCreateObj,
                            (void**)&pCreateObj);

    if(SUCCEEDED(hr))
    {
        IADsContainer *pContainer;

        pContainer = GetUserContainer();

        if(pContainer)
        {
            hr = pCreateObj->Initialize(pContainer, NULL, L"user");
            if(SUCCEEDED(hr))
            {
                HWND    hwndParent;

                hwndParent = GetDesktopWindow();

                hr = pCreateObj->CreateModal(hwndParent, ppAdsOut);
            }

            pContainer->Release();
        }

        pCreateObj->Release();
    }

    return hr;    
}

//  Entry point to the application
int main(void)
{
    HRESULT hr;
    IADs *pAds = NULL;

    CoInitialize(NULL);

    hr = LaunchNewUserWizard(&pAds);
    if((S_OK == hr) && (NULL != pAds))
    {
        pAds->Release();
    }

    CoUninitialize();

    return 0;
}
```



 

 