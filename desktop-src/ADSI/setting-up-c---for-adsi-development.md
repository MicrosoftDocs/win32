---
title: Setting Up Visual C++ 6.0 for ADSI Development
description: This topic shows you how to set up C++ in Visual Studio so you can develop an ADSI application.
ms.assetid: 6f1ab3eb-2e0b-4f3e-b93c-e24c8b3b1a27
ms.tgt_platform: multiple
keywords:
- Setting Up C++ for ADSI Development
ms.topic: article
ms.date: 05/31/2018
---

# Setting Up Visual C++ 6.0 for ADSI Development

The Microsoft Visual C++ 6.0 development system can be used to develop enterprise applications. To set up your Visual C++ 6.0 environment to develop an ADSI application, perform the following steps:

**Setting Up the Microsoft Visual C++ 6.0 Development Environment**

1.  Point to the include and library directory. Select **Tools \| Options**. Click the **Directory** tab, and specify the path to the ADSI header files.
2.  Include the Activeds.h file in your project.
3.  Add the Activeds.lib and Adsiid.lib files to the linker input for your project.
4.  Begin programming with ADSI.

Log on to a Windows domain. You must also have permission to modify data in Active Directory. By default, the Administrator has this privilege. To enter this code example:

**A Sample Visual C++ Application: Creating a User in a Domain**

1.  Start Visual C++ 6.0.
2.  Create a standalone executable project. It can be either an MFC, ATL, or Console Application.
3.  Follow the previous steps to set up your project.
4.  Enter the following code example. Replace the "LDAP://CN=users,DC=fabrikam,DC=com" string with the ADsPath of a container in your domain. You should also replace the user name "jeffsmith" with a user name that is unique in your domain.

    ```C++
    #include "stdafx.h"
    #include "activeds.h"

    int main(int argc, char* argv[])
    {
        HRESULT hr;
        IADsContainer *pCont;
        IDispatch *pDisp=NULL;
        IADs *pUser;

         // Initialize COM before calling any ADSI functions or interfaces.
         CoInitialize(NULL);

        hr = ADsGetObject( L"LDAP://CN=users,DC=fabrikam,DC=com", 
                                   IID_IADsContainer, 
                                   (void**) &pCont );
        
        if ( !SUCCEEDED(hr) )
        {
            return 0;
        }

        //-----------------
        // Create a user
        //-----------------
        
        hr = pCont->Create(CComBSTR("user"), CComBSTR("cn=jeffsmith"), &pDisp );
        
        // Release the container object.    
        pCont->Release();
        
        if ( !SUCCEEDED(hr) )
        {
            return 0;
        }

        hr = pDisp->QueryInterface( IID_IADs, (void**) &pUser );

        // Release the dispatch interface.
        pDisp->Release();

        if ( !SUCCEEDED(hr) )
        {    
            return 0;
        }

        // Commit the object data to the directory.
        pUser->SetInfo();

        // Release the object.
        pUser->Release();

        CoUninitialize();
    }
    ```

    

5.  Build and run the application. To verify that the user has been created, use the Active Directory Users and Computers management tool.

 

 




