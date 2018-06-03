---
title: Creating inetOrgPerson Objects
description: To create an inetOrgPerson object, bind to the object that will contain the object, create an inetOrgPerson object, set its properties, and save the object to the directory store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3a7be148-ba09-449c-b343-a1fb30497c62
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , creating inetOrgPerson objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating inetOrgPerson Objects

To create an **inetOrgPerson** object, bind to the object that will contain the object, create an **inetOrgPerson** object, set its properties, and save the object to the directory store.

The following code example assumes that the schema of the AD LDS instance has been extended by [Adding User Classes](adding-user-classes.md).

The following Visual Basic Scripting Edition example uses the **GetObject** function to bind to an **organization** object and uses the **Create** method to create **inetOrgPerson** objects in that **organization**.


```VB
' Create inetOrgPerson Objects.

Option Explicit

Dim objADAM   ' Binding object.
Dim objUser   ' inetOrgPerson.
Dim strPath   ' Binding path.
Dim strUser   ' Selected user.
Dim strUsers  ' Array users.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

On Error Resume Next

' Bind to object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
Else
    WScript.Echo "Success: Bind succeeded."
End If

' Specify Users.
strUsers = Array("CN=inetuser1", "CN=inetuser2", "CN=inetuser3")

' Loop through and create users.
For Each strUser in strUsers

    ' Create User.
    WScript.Echo "Create:  " & strUser
    Set objUser = objADAM.Create("inetOrgPerson", strUser)
    objUser.SetInfo

    ' Output success or error.
    If Err.Number <> vbEmpty Then
        WScript.Echo "Error:   Create failed with error #" _
                             & Hex(Err.Number) & ", " _
                             & Err.Description & "."
    Else
        WScript.Echo "Success: User created."
        WScript.Echo "   Name:  " & objUser.Name
    End If

    Set objUser = Nothing

Next
```



The following Visual Basic .NET example uses the **DirectoryEntry** constructor to bind to an **organization** object and uses the **Add** method to create **inetOrgPerson** objects in that **organization**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class CreateInetOrgUsers

        '/ <summary>
        '/ Create inetOrgPerson Objects.
        '/ </summary>

        <STAThread()>  Shared Sub Main()
            Dim objADAM As DirectoryEntry  ' Binding object.
            Dim objUser As DirectoryEntry  ' inetOrgPerson object.
            Dim strPath As String          ' Binding path.

            ' Construct the binding string.
            strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

            Console.WriteLine("Bind to: {0}", strPath)

            ' Get AD LDS object.
            Try
                objADAM = New DirectoryEntry(strPath)
                objADAM.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Specify users.
            Dim strUsers As String() = _
                {"CN=inetuser1", "CN=inetuser2", "CN=inetuser3"}

            ' Loop through and create users.
            Dim strUser As String
            For Each strUser In  strUsers
                Console.WriteLine("Create:  {0}", strUser)
                ' Create user.
                Try
                    objUser = objADAM.Children.Add(strUser, "inetOrgPerson")
                    objUser.CommitChanges()
                Catch e As Exception
                    Console.WriteLine("Error:   Create failed.")
                    Console.WriteLine("         {0}", e.Message)
                    Return
                End Try

                ' Output user attribute.
                Console.WriteLine("Success: Create succeeded.")
                Console.WriteLine("Name:    {0}", objUser.Name)
            Next strUser
            Return

        End Sub 'Main
    End Class 'CreateInetOrgUsers
End Namespace 'ADAM_Examples
```



The following C# example uses the **DirectoryEntry** constructor to bind to an **organization** object and uses the **Add** method to create **inetOrgPerson** objects in that **organization**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class CreateInetOrgUsers
    {
        /// <summary>
        /// Create inetOrgPerson Objects.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;  // Binding object.
            DirectoryEntry objUser;  // inetOrgPerson object.
            string strPath;          // Binding path.

            // Construct the binding string.
            strPath = "LDAP://localhost:389/O=Fabrikam,C=US";

            Console.WriteLine("Bind to: {0}", strPath);

            // Get the AD LDS object.
            try
            {
                objADAM = new DirectoryEntry(strPath);
                objADAM.RefreshCache();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Bind failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Specify users.
            string[] strUsers = {"CN=inetuser1",
                "CN=inetuser2", "CN=inetuser3"};

            // Loop through and create users.
            foreach (string strUser in strUsers)
            {
                Console.WriteLine("Create:  {0}", strUser);
                // Create user.
                try
                {
                    objUser = objADAM.Children.Add(strUser,
                        "inetOrgPerson");
                    objUser.CommitChanges();
                }
                catch (Exception e)
                {
                    Console.WriteLine("Error:   Create failed.");
                    Console.WriteLine("         {0}", e.Message);
                    return;
                }

                // Output user attribute.
                Console.WriteLine("Success: Create succeeded.");
                Console.WriteLine("Name:     {0}", objUser.Name);
            }
            return;
        }
    }
}
```



The following C++ example in shows how to add a user to an application partition directory using [Active Directory Service Interfaces (ADSI)](https://msdn.microsoft.com/library/aa772170). The example uses the [**IADsContainer::Create**](https://msdn.microsoft.com/library/aa705987) and the [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354) methods. For more information about adding objects using ADSI, see [Creating and Deleting Objects](https://msdn.microsoft.com/library/aa772364).

The example assumes an application partition called O=fabrikam,c=US and has set up your environment for ADSI development. For more information, see [Setting Up Visual C++ 6.0 for ADSI Development](https://msdn.microsoft.com/library/aa746483).


```C++
#include "stdafx.h"

#include "activeds.h"

#include "atlbase.h"

int _tmain()

{

    HRESULT hr;
    
    IADsContainer *pCont;

     // You must initialize COM before calling any ADSI functions or interfaces.
     CoInitialize(NULL);
     
     CComBSTR sbrstADsPath = "LDAP://localhost:389/O=fabrikam,c=US";

    // Bind to the container.
    hr = ADsGetObject(sbrstADsPath, IID_IADsContainer, (void**) &amp;pCont; );
    
    if ( SUCCEEDED(hr) )
    {
        //----------------------------
        // Creating a user
        //-----------------------------
        IDispatch *pDisp=NULL;
        
        IADs *pUser;
        
        hr = pCont->Create( CComBSTR("user"), CComBSTR("CN=jeffsmith"), &amp;pDisp; );
        
        if ( SUCCEEDED(hr) )
        {
           hr = pDisp->QueryInterface( IID_IADs, (void**) &amp;pUser; );
           
           if ( SUCCEEDED(hr) )
            {
            
                // Commit creation to the directory.
                hr = pUser->SetInfo();
                
                if ( !SUCCEEDED(hr) )
                {
                
                    return 0;
                
                }

                // Release the object.
                pUser->Release();
            }
           
           pDisp->Release();
           
        }
        
        pCont->Release();
        
    }
 
    CoUninitialize();
    
}
```



 

 




