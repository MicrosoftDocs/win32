---
title: Creating Users with Active Directory Lightweight Directory Services
description: To create an AD LDS user, bind to the object that will contain the user, create a user object, set its properties, and save the object to the directory store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 08f3b66e-9e17-449c-ab6f-bbfcb3c8d4bd
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , creating users
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Users with Active Directory Lightweight Directory Services

To create an AD LDS user, bind to the object that will contain the user, create a **user** object, set its properties, and save the object to the directory store.

To delete an object created with the following code example in [Deleting Users](deleting-users.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organization** object, uses the **Create** method to create a **user** object in that **organization**, and sets some properties of the **user**.


```VB
' Create AD LDS User.

Option Explicit

Dim objADAM               ' Binding object.
Dim objUser               ' User object.
Dim strDisplayName        ' Display name of user.
Dim strPath               ' Binding path.
Dim strUser               ' User to create.
Dim strUserPrincipalName  ' Principal name of user.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify User.
strUser = "CN=TestUser"
strDisplayName = "Test User"
strUserPrincipalName = "TestUser@Fabrikam.Us"

WScript.Echo "Create:  " & strUser
WScript.Echo "         " & strDisplayName
WScript.Echo "         " & strUserPrincipalName

On Error Resume Next

' Bind to object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

' Create User.
Set objUser = objADAM.Create("user", strUser)
objUser.Put "displayName", strDisplayName
objUser.Put "userPrincipalName", strUserPrincipalName
objUser.SetInfo

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Create failed."
Else
    WScript.Echo "Success:   User created."
    WScript.Echo "UserName:  " & objUser.user
    WScript.Echo "Display:   " & objUser.displayName
    WScript.Echo "Principal: " & objUser.userPrincipalName
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organization** object, uses the **Add** method to create a **user** object in that **organization**, and sets some properties of the **user**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class CreateUser

        '/ <summary>
        '/ Create AD LDS User.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry       ' Binding object.
            Dim objUser As DirectoryEntry       ' User object.
            Dim strDisplayName As String        ' Display name of user.
            Dim strPath As String               ' Binding path.
            Dim strUser As String               ' User to create.
            Dim strUserPrincipalName As String  ' Principal name of user.

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

            ' Specify User.
            strUser = "CN=TestUser"
            strDisplayName = "Test User"
            strUserPrincipalName = "TestUser@Fabrikam.Us"
            Console.WriteLine("Create:  {0}", strUser)

            ' Create User.
            Try
                objUser = objADAM.Children.Add(strUser, "user")
                objUser.Properties("displayName").Add(strDisplayName)
                objUser.Properties("userPrincipalName").Add( _
                    strUserPrincipalName)
                objUser.CommitChanges()
            Catch e As Exception
                Console.WriteLine("Error:   Create failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output User attributes.
            Console.WriteLine("Success: Create succeeded.")
            Console.WriteLine("Name:    {0}", objUser.Name)
            Console.WriteLine("         {0}", _
                objUser.Properties("displayName").Value)
            Console.WriteLine("         {0}", _
                objUser.Properties("userPrincipalName").Value)
            Return

        End Sub 'Main
    End Class 'CreateUser
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to bind to an **organization** object, uses the **Add** method to create a **user** object in that **organization**, and sets some properties of the **user**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class CreateUser
    {
        /// <summary>
        /// Create AD LSD User.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;       // Binding object.
            DirectoryEntry objUser;       // User object.
            string strDisplayName;        // Display name of user.
            string strPath;               // Binding path.
            string strUser;               // User to create.
            string strUserPrincipalName;  // Principal name of user.

            // Construct the binding string.
            strPath = "LDAP://localhost:389/O=Fabrikam,C=US";

            Console.WriteLine("Bind to: {0}", strPath);

            // Get AD LDS object.
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

            // Specify User.
            strUser = "CN=TestUser";
            strDisplayName = "Test User";
            strUserPrincipalName = "TestUser@Fabrikam.Us";
            Console.WriteLine("Create:  {0}", strUser);

            // Create User.
            try
            {
                objUser = objADAM.Children.Add(strUser, "user");
                objUser.Properties["displayName"].Add(strDisplayName);
                objUser.Properties[
                    "userPrincipalName"].Add(strUserPrincipalName);
                objUser.CommitChanges();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Create failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output User attributes.
            Console.WriteLine("Success: Create succeeded.");
            Console.WriteLine("Name:    {0}", objUser.Name);
            Console.WriteLine("         {0}",
                objUser.Properties["displayName"].Value);
            Console.WriteLine("         {0}",
                objUser.Properties["userPrincipalName"].Value);
            return;
        }
    }
}
```



 

 




