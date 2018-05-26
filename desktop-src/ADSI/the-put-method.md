---
title: The Put Method
description: Saves the value for a property for an Active Directory object by name into the property cache.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8534ceba-5fcb-441f-9e76-3060319478af
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Put ADSI ,about
- ADSI ADSI ,example code Visual Basic ,using the Put method
- properties ADSI ,saving a value for a property to property cache
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# The Put Method

The [**IADs::Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) method saves the value for a property for an Active Directory object by name into the property cache. Use [**IADs::PutEx**](/windows/win32/Iads/nf-iads-iads-putex?branch=master) to save multi-valued properties to the property cache, or to remove a property from an object. These values are not persisted to the underlying directory service until [**IADs::SetInfo**](/windows/win32/Iads/nf-iads-iads-setinfo?branch=master) is called.


```VB
Dim Namespace As IADsOpenDSObject
Dim User As IADsUser
Dim NewName As Variant
Dim sUserName As String
Dim sPassword As String

On Error GoTo CleanUp
 
Set Namespace = GetObject("LDAP:")

' Insert code to safely get the user name and password
 
Set User = Namespace.OpenDSObject("LDAP://MyMachine/CN=Administrator,CN=Users,DC=MyDomain,DC=Fabrikam,DC=COM", sUserName, sPassword, ADS_SECURE_AUTHENTICATION)
 
NewName = InputBox("Enter a new name:")
 
' Set using IADs::PutMethod
User.Put "FullName", NewName
User.SetInfo

Exit Sub

CleanUp:
    Set IADsOpenDSObject = Nothing
    Set IADsUser = Nothing

End Sub
```



The following code example shows how to use [**IADs::Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) with a single value:


```VB
Dim x As IADs
Dim sUserName As String
Dim sFull As String

On Error GoTo CleanUp

sUserName = InputBox("Enter your user name:")
 
Set x = GetObject("LDAP://CN="&amp; sUserName &amp;",CN=Users,DC=Fabrikam, DC=Com") 

sFull = InputBox ("Enter your full name:")
x.Put "name", sFull
 
' Commit to the directory.
x.SetInfo

Exit Sub

CleanUp:
    MsgBox ("An error has occurred. " & Err.Description)
    Set x = Nothing
```



The following code example shows how to use [**IADs::Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) with multiple values:


```VB
Dim x As IADs
Dim sFirst As String
Dim sLast As String
Dim sUsername As String

On Error GoTo CleanUp

sUsername = InputBox("User name:")
 
Set x = GetObject("LDAP://CN=" & sUsername & ", CN=Users,DC=Fabrikam, DC=Com")

sFirst = InputBox("Enter your first name:")
sLast = InputBox("Enter your last name:")
 
x.Put "givenName", sFirst
x.Put "sn", sLast
 
'Commit to the directory
x.SetInfo

Exit Sub

CleanUp:
    MsgBox ("An error has occurred. " & Err.Description)
    Set x = Nothing
```



The following code example shows how to use [**IADs::Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) with both multiple and single values:


```C++
int main(int argc, char* argv[], LPWSTR pszADsPath)
{
   HRESULT hr;
   IADs *pADs=NULL;

   CoInitialize(NULL);

   hr = ADsGetObject(pszADsPath,
                     IID_IADs, 
                    (void**) &amp;pADs );

   if (!SUCCEEDED(hr) )
   {
     return hr;
   }

   VARIANT var;
 
   // Using Put with a single value for the first name
   VariantInit(&amp;var);
   V_BSTR(&amp;var) = SysAllocString(L"Janet");
   V_VT(&amp;var) = VT_BSTR;
   hr = pADs->Put( L"givenName", var );

   // Using Put with a single value for the last name
   VariantClear(&amp;var);
   V_BSTR(&amp;var) = SysAllocString(L"Johns");
   V_VT(&amp;var) = VT_BSTR;
   hr = pADs->Put( L"sn", var ); 
   VariantClear(&amp;var);

   // Using Put with multiple values for other telephones
   LPWSTR pszPhones[] = { L"425 844 1234", L"425 924 4321" };
   DWORD dwNumber = sizeof( pszPhones ) /sizeof(LPWSTR);

   hr = ADsBuildVarArrayStr( pszPhones, dwNumber, &amp;var );
   hr = pADs->Put( L"otherTelephone", var ); 
   VariantClear(&amp;var);

   hr = pADs->SetInfo();
   pADs->Release();

   if (!SUCCEEDED(hr) )
   {
     return hr;
   }

 CoUninitialize();
 return 0;
}
```



 

 




