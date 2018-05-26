---
title: Removing Members from Groups
description: To remove an AD LDS user object from an AD LDS group object, bind to the group and the user, and use the Remove method on the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e5e05034-9236-47b5-9775-c0aad0e9aac9
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , removing members from groups
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Removing Members from Groups

To remove an AD LDS **user** object from an AD LDS **group** object, bind to the **group** and the **user**, and use the **Remove** method on the **group**.

You can add the object you remove with the following code example by [Adding Members to Groups](adding-members-to-groups.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organization** object, uses the **GetObject** function to bind to a **group** object in an **organizationalUnit** object of the **organization** and a **user** object in the **organization**, and uses the **Remove** method to remove the **user** from the **group**.


```VB
' Remove AD LDS User from AD LDS Group.

Option Explicit

Dim objADAM   ' Binding object.
Dim objGroup  ' Group object.
Dim objUser   ' User object.
Dim strGroup  ' Group.
Dim strPath   ' Binding path.
Dim strOU     ' Organizational unit.
Dim strUser   ' User.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify User.
strUser = "CN=TestUser"

' Specify Group.
strGroup = "CN=TestGroup,OU=TestOU"

WScript.Echo "Remove:  " & strUser
WScript.Echo "          from"
WScript.Echo "         " & strGroup

On Error Resume Next

' Bind to root.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

' Remove User from Group.
Set objGroup = objADAM.GetObject("group", strGroup)
Set objUser  = objADAM.GetObject("user", strUser)
objGroup.Remove objUser.AdsPath

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Remove failed."
Else
    WScript.Echo "Success: User removed from group."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organization** object, uses the **Find** method to bind to a **group** object in an **organizationalUnit** object of the **organization** and a **user** object in the **organization**, and uses the **Remove** method to remove the **user** from the **group**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class RemoveUserFromGroup

        '/ <summary>
        '/ Remove AD LDS User from AD LDS Group.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry   ' Binding object.
            Dim objGroup As DirectoryEntry  ' Group object.
            Dim objUser As DirectoryEntry   ' User object.
            Dim strGroup As String          ' Group.
            Dim strPath As String           ' Binding path.
            Dim strUser As String           ' User.

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

            ' Specify Group.
            strGroup = "CN=TestGroup,OU=TestOU"

            Console.WriteLine("Remove:  {0}", strUser)
            Console.WriteLine("           from")
            Console.WriteLine("         {0}", strGroup)

            ' Remove User from Group.
            Try
                objGroup = objADAM.Children.Find(strGroup, "group")
                objUser = objADAM.Children.Find(strUser, "user")
                objGroup.Properties("member").Remove(objUser.Properties( _
                    "distinguishedName").Value)
                objGroup.CommitChanges()
            Catch e As Exception
                Console.WriteLine("Error:   Remove failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output success.
            Console.WriteLine("Success: User removed from group.")
            Return

        End Sub 'Main
    End Class 'RemoveUserFromGroup
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to bind to an **organization** object, uses the **Find** method to bind to a **group** object in an **organizationalUnit** object of the **organization** and a **user** object in the **organization**, and uses the **Remove** method to remove the **user** from the **group**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class RemoveUserFromGroup
    {
        /// <summary>
        /// Remove AD LDS User from AD LDS Group.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;   // Binding object.
            DirectoryEntry objGroup;  // Group object.
            DirectoryEntry objUser;   // User object.
            string strGroup;          // Group.
            string strPath;           // Binding path.
            string strUser;           // User.

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

            // Specify Group.
            strGroup = "CN=TestGroup,OU=TestOU";

            Console.WriteLine("Remove:  {0}", strUser);
            Console.WriteLine("           from");
            Console.WriteLine("         {0}", strGroup);

            // Remove User from Group.
            try
            {
                objGroup = objADAM.Children.Find(strGroup, "group");
                objUser  = objADAM.Children.Find(strUser, "user");
                objGroup.Properties["member"].Remove(
                    objUser.Properties["distinguishedName"].Value);
                objGroup.CommitChanges();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Remove failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output success.
            Console.WriteLine("Success: User removed from group.");
            return;
        }
    }
}
```



 

 




