---
title: User Creation with the ADSI LDAP Provider
description: With the ADSI LDAP provider, you can only create a global user account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'f99f85a8-9ced-4006-b95b-bd5671ba4c60'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["LDAP provider ADSI ,user object,User Creation"]
---

# User Creation with the ADSI LDAP Provider

With the ADSI LDAP provider, you can only create a global user account. Local accounts reside in the SAM database and must be created using the WinNT provider. For more information about creating a user object with the WinNT provider, see [WinNT User Object](winnt-user-object.md).

**To create a user object**

1.  Bind to the container where the user object will reside and obtain either the [**IADsContainer**](iadscontainer.md) or [**IDirectoryObject**](idirectoryobject.md) interface for the container.
2.  Use the [**IADsContainer.Create**](iadscontainer-create.md) or [**IDirectoryObject::CreateDSObject**](idirectoryobject-createdsobject.md) method to create the user object.
3.  The minimum attributes required to create a user object will depend on the directory service used. For more information about creating an Active Directory user, see [Creating a User](https://msdn.microsoft.com/library/ms675773).
4.  If the [**IADsContainer**](iadscontainer.md) interface is used, the new object is not actually created until the [**IADs.SetInfo**](iads-setinfo.md) method is called.

    If the [**IDirectoryObject**](idirectoryobject.md) interface is used, the new object is created when the [**CreateDSObject**](idirectoryobject-createdsobject.md) method is called. The minimum attributes, including the [**objectClass**](https://msdn.microsoft.com/library/ms679012), must be specified in the [**ADS\_ATTR\_INFO**](ads-attr-info.md) array passed to the **CreateDSObject** method.

## Example Code

The following code example creates a user account with the default attributes.


```VB
Dim ou As IADs
Dim usr as IADsUser

On Error GoTo Cleanup

Set ou = GetObject("LDAP://OU=Finance,DC=Fabrikam,DC=COM")
Set usr = ou.Create("user", "cn=Jeff Smith")
usr.Put "samAccountName", "jeffsmith"
usr.SetInfo

Cleanup:
   If (Err.Number <> 0) Then
      MsgBox ("An error has occurred. " &  Err.Number)
   End If
   Set ou = Nothing
   Set usr = Nothing
```



## Example Code

The following code example creates a user account with the default attributes. For brevity, error checking is omitted.


```C++
#include <activeds.h>

int main()
{
   HRESULT hr = CoInitialize(NULL);

   IADsContainer *pCont;
   IADsUser *pUser;

   LPWSTR adsPath = L"LDAP://serv1/CN=Users,dc=Fabrikam,dc=com";
   LPWSTR usrPass = NULL;
   LPWSTR usrName = NULL;

   // Add code to securely get the user name and password or leave
   // as NULL to use the current security context.

   hr = ADsOpenObject(adsPath, 
                      usrName,
                      usrPass,
                      ADS_SECURE_AUTHENTICATION,
                      IID_IADsContainer,
                      (void**)&amp;pCont);

   IDispatch *pDisp;
   hr = pCont->Create(CComBSTR("user"), CComBSTR("cn=Jeff Smith"), &amp;pDisp);
   pCont->Release();

   hr = pDisp->QueryInterface(IID_IADsUser,(void**)&amp;pUser);
   pDisp->Release();

   VARIANT var;
   VariantInit(&amp;var);
   V_BSTR(&amp;var) = L"jeffsmith";
   V_VT(&amp;var)=VT_BSTR;
   hr = pUser->Put(CComBSTR("samAccountName"), var);

   hr = pUser->SetInfo();

   VariantClear(&amp;var);
   pUser->Release();

   CoUninitialize();

   return 0;
}
```



 

 




