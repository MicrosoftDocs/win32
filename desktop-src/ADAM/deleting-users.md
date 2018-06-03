---
title: Deleting Users with Active Directory Lightweight Directory Services
description: To delete an AD LDS user, bind to the object that contains the user and delete the user object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3fa4711b-8c39-4559-8acc-c435c0829d2b
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , deleting users
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Deleting Users with Active Directory Lightweight Directory Services

To delete an AD LDS user, bind to the object that contains the user and delete the **user** object.

For more information and a code example that can be used to create a deleted object, see [Creating Users](creating-users.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organization** object and uses the **Delete** method to delete a selected **user** object in that **organization**.


```VB
' Delete AD LDS User.

Option Explicit

Dim objADAM  ' Binding object.
Dim strPath  ' Binding path.
Dim strUser  ' User to delete.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify the User.
strUser = "CN=TestUser"

On Error Resume Next

' Bind to the object.
Set objADAM = GetObject(strPath)

' If bind fails, output error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

WScript.Echo "Delete:  " & strUser

' Delete the User.
objADAM.Delete "user", strUser

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Delete failed."
Else
    WScript.Echo "Success: User deleted."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** method to bind to an **organization** object, uses the **Find** method to bind to a selected **user** object, and uses the **Remove** method to remove the selected **user** from that **organization**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class DeleteUser

        '/ <summary>
        '/ Delete AD LDS User.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry  ' Binding object.
            Dim objUser As DirectoryEntry  ' User object.
            Dim strPath As String          ' Binding path.
            Dim strUser As String          ' User to delete.

            ' Construct the binding string.
            strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

            Console.WriteLine("Bind to: {0}", strPath)

            ' Get the AD LDS object.
            Try
                objADAM = New DirectoryEntry(strPath)
                objADAM.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Specify the User.
            strUser = "CN=TestUser"
            Console.WriteLine("Delete:  {0}", strUser)

            ' Delete the User.
            Try
                objUser = objADAM.Children.Find(strUser, "user")
                objADAM.Children.Remove(objUser)
            Catch e As Exception
                Console.WriteLine("Error:   Delete failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output success.
            Console.WriteLine("Success: User deleted.")
            Return

        End Sub 'Main
    End Class 'DeleteUser
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** method to bind to an **organization** object, uses the **Find** method to bind to a selected **user** object, and uses the **Remove** method to remove the selected **user** from that **organization**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class DeleteUser
    {
        /// <summary>
        /// Delete AD LDS User.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;  // Binding object.
            DirectoryEntry objUser;  // User object.
            string strPath;          // Binding path.
            string strUser;          // User to delete.

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

            // Specify the User.
            strUser = "CN=TestUser";
            Console.WriteLine("Delete:  {0}", strUser);

            // Delete the User.
            try
            {
                objUser = objADAM.Children.Find(strUser, "user");
                objADAM.Children.Remove(objUser);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Delete failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output success.
            Console.WriteLine("Success: User deleted.");
            return;
        }
    }
}
```



 

 




