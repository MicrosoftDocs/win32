---
title: Creating Groups
description: To create an AD LDS group, bind to the object that will contain the user, create a group object, set its properties, and save the object to the directory store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a82a0f37-4ea2-4e60-9cc5-e0b8db9ba0bd
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , creating groups
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating Groups

To create an AD LDS group, bind to the object that will contain the user, create a **group** object, set its properties, and save the object to the directory store.

To delete the object created with the following code example by [Deleting Groups](deleting-groups.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organizationalUnit** object, uses the **Create** method to create a **group** object in that **organizationalUnit**, and sets properties of the **group**.


```VB
' Create AD LDS Group.

Option Explicit

Dim objADAM         ' Binding object.
Dim objGroup        ' Group object.
Dim strDescription  ' Description of group.
Dim strDisplayName  ' Display name of group.
Dim strGroup        ' Group.
Dim strPath         ' Binding path.
Dim strSAMAccountName ' SAMAccountName

' Construct the binding string.
strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify Group.
strGroup = "CN=TestGroup"
strDisplayName = "Test Group"
strDescription = "AD LDS Test Group"
strSAMAccountName = "test"

WScript.Echo "Create:  " & strGroup
WScript.Echo "         " & strDisplayName
WScript.Echo "         " & strDescription

On Error Resume Next

' Bind to object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

' Create Group.
Set objGroup = objADAM.Create("group", strGroup)
objGroup.Put "displayName", strDisplayName
objGroup.Put "description", strDescription
objGroup.Put "sAMAccountName", strSAMAccountName
objGroup.SetInfo

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Create failed."
Else
    WScript.Echo "Success: Group created."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Add** method to create a **group** object in that **organizationalUnit**, and sets properties of the **group**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class CreateGroup

        '/ <summary>
        '/ Create AD LDS Group.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry   ' Binding object.
            Dim objGroup As DirectoryEntry  ' Group object.
            Dim strDescription As String    ' Description of group.
            Dim strDisplayName As String    ' Display name of user.
            Dim strSAMAccountName As String ' user's SAMAccountName.
            Dim strGroup As String          ' Group to create.
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
            strDisplayName = "Test Group"
            strDescription = "AD LDS Test Group"
            Console.WriteLine("Create:  {0}", strGroup)

            ' Create Group.
            Try
                objGroup = objADAM.Children.Add(strGroup, "group")
                objGroup.Properties("displayName").Add(strDisplayName)
                objGroup.Properties("description").Add(strDescription)
                objGroup.Properties("sAMAccountName").Add(strSAMAccountName)
                objGroup.CommitChanges()
            Catch e As Exception
                Console.WriteLine("Error:   Create failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output Group attributes.
            Console.WriteLine("Success: Create succeeded.")
            Console.WriteLine("Name:    {0}", objGroup.Name)
            Console.WriteLine("         {0}", _
                objGroup.Properties("displayName").Value)
            Console.WriteLine("         {0}", _
                objGroup.Properties("description").Value)
            Return

        End Sub 'Main
    End Class 'CreateGroup
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Add** method to create a **group** object in that **organizationalUnit**, and sets properties of the **group**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class CreateGroup
    {
        /// <summary>
        /// Create AD LDS Group.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;   // Binding object.
            DirectoryEntry objGroup;  // Group object.
            string strDescription;    // Description of group.
            string strDisplayName;    // Display name of user.
            string strSAMAccountName  // User's SAMAccountName
            string strGroup;          // Group to create.
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

            // Specify Group.
            strGroup = "CN=TestGroup";
            strDisplayName = "Test Group";
            strDescription = "AD LDS Test Group";
            strSAMAccountName = "test";
            Console.WriteLine("Create:  {0}", strGroup);

            // Create Group.
            try
            {
                objGroup = objADAM.Children.Add(strGroup, "group");
                objGroup.Properties["displayName"].Add(strDisplayName);
                objGroup.Properties["description"].Add(strDescription);
                objGroup.Propertiew["sAMAccountName"].Add(strSAMAccountName);
                objGroup.CommitChanges();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Create failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output Group attributes.
            Console.WriteLine("Success: Create succeeded.");
            Console.WriteLine("Name:    {0}", objGroup.Name);
            Console.WriteLine("         {0}",
                objGroup.Properties["displayName"].Value);
            Console.WriteLine("         {0}",
                objGroup.Properties["description"].Value);
            return;
        }
    }
}
```



 

 




