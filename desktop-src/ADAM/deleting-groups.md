---
title: Deleting Groups
description: To delete an AD LDS group, bind to the object that contains the group and delete the group object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '9c3d87ce-bf4b-4408-b88e-8dc1f41f7d7b'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["AD LDS examples ADAM , deleting groups"]
---

# Deleting Groups

To delete an AD LDS group, bind to the object that contains the group and delete the **group** object.

For more information and a code example that can be used to create the object deleted, see [Creating Groups](creating-groups.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organizationalUnit** object and uses the **Delete** method to delete a **group** object in that **organizationalUnit**.


```VB
' Delete the AD LDS Group.

Option Explicit

Dim objADAM   ' Binding object.
Dim strGroup  ' Group to delete.
Dim strPath   ' Binding path.

' Construct the binding string.
strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify the Group.
strGroup = "CN=TestGroup"

On Error Resume Next

' Bind to the object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

WScript.Echo "Delete:  " & strGroup

' Delete Group.
objADAM.Delete "group", strGroup

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Delete failed."
Else
    WScript.Echo "Success: Group deleted."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Find** method to bind to a selected **group** object, and uses the **Remove** method to delete the selected **group** from that **organizationalUnit**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class DeleteGroup

        '/ <summary>
        '/ Delete AD LDS Group.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry   ' Binding object.
            Dim objGroup As DirectoryEntry  ' Group object.
            Dim strGroup As String          ' Group to delete.
            Dim strPath As String           ' Binding path.

            ' Construct the binding string.
            strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"

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

            ' Specify Group.
            strGroup = "CN=TestGroup"
            Console.WriteLine("Delete:  {0}", strGroup)

            ' Delete Group.
            Try
                objGroup = objADAM.Children.Find(strGroup, "group")
                objADAM.Children.Remove(objGroup)
            Catch e As Exception
                Console.WriteLine("Error:   Delete failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output success.
            Console.WriteLine("Success: Group deleted.")
            Return

        End Sub 'Main
    End Class 'DeleteGroup
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Find** method to bind to a selected **group** object, and uses the **Remove** method to delete the selected **group** from that **organizationalUnit**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class DeleteGroup
    {
        /// <summary>
        /// Delete AD LDS Group.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;   // Binding object.
            DirectoryEntry objGroup;  // Group object.
            string strGroup;          // Group to delete.
            string strPath;           // Binding path.

            // Construct the binding string.
            strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US";

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

            // Specify the Group.
            strGroup = "CN=TestGroup";
            Console.WriteLine("Delete:  {0}", strGroup);

            // Delete the Group.
            try
            {
                objGroup = objADAM.Children.Find(strGroup, "group");
                objADAM.Children.Remove(objGroup);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Delete failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output success.
            Console.WriteLine("Success: Group deleted.");
            return;
        }
    }
}
```



 

 




