---
title: Enumerating Users and Groups
description: To enumerate members of a group, search Active Directory Lightweight Directory Services (AD LDS) using a filter to limit the type of object selected and then use the appropriate techniques shown in the following example code.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f667b05c-5eb9-4407-8400-d517ee37a43c
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , enumerating users and groups
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enumerating Users and Groups

To enumerate members of a group, search Active Directory Lightweight Directory Services (AD LDS) using a filter to limit the type of object selected and then use the appropriate techniques shown in the following example code.

For more information about filtering a query, see [Creating a Query Filter](https://msdn.microsoft.com/library/ms675768).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organizationalUnit** object, uses the **Filter** property to select **group** objects, outputs the name of each **group** present, and uses the **Members** method to output each member of each **group**.


```VB
' Enumerate AD LDS groups and group members.

Option Explicit

Dim objADAM    ' Binding object.
Dim objGroup   ' Group object.
Dim objMember  ' Member object.
Dim strPath    ' Binding path.

' Construct the binding string.
strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath
WScript.Echo "Enum:    Groups and members"

On Error Resume Next

' Bind to object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

' Enumerate groups and members.
objADAM.Filter = Array("group")
For Each objGroup in objADAM
    WScript.Echo "Group:   " & objGroup.Name
    For Each objMember in objGroup.Members
        WScript.Echo " Member:  " & objMember.Name
    Next
Next

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Enumeration failed."
Else
    WScript.Echo "Success: Enumeration complete."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Filter** property of a **DirectorySearcher** object to select **group** objects, outputs the name of each **group** present, and uses the **member** property to output each member of each **group**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class EnumMembers

        '/ <summary>
        '/ Enumerate AD LDS groups and group members.
        '/ </summary>

        <STAThread()>  Shared Sub Main()
            Dim objADAM As DirectoryEntry                   ' Binding object.
            Dim objGroupEntry As DirectoryEntry             ' Group Results.
            Dim objSearchADAM As DirectorySearcher          ' Search object.
            Dim objSearchResults As SearchResultCollection  ' Results collection.
            Dim strPath As String                           ' Binding path.

            ' Construct the binding string.
            strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"
            Console.WriteLine("Bind to: {0}", strPath)
            Console.WriteLine("Enum:    Groups and members.")

            ' Get the AD LDS object.
            Try
                objADAM = New DirectoryEntry(strPath)
                objADAM.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Get search object, specify filter and scope,
            ' perform search.
            Try
                objSearchADAM = New DirectorySearcher(objADAM)
                objSearchADAM.Filter = "(&amp;(objectClass=group))"
                objSearchADAM.SearchScope = SearchScope.Subtree
                objSearchResults = objSearchADAM.FindAll()
            Catch e As Exception
                Console.WriteLine("Error:   Search failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Enumerate groups and members.
            Try
                If objSearchResults.Count <> 0 Then
                    Dim objResult As SearchResult
                    For Each objResult In  objSearchResults
                        objGroupEntry = objResult.GetDirectoryEntry()
                        Console.WriteLine("Group    {0}", objGroupEntry.Name)
                        Dim objMember As Object
                        For Each objMember _
                            In objGroupEntry.Properties("member")
                                Console.WriteLine(" Member: {0}", _
                                    objMember.ToString())
                        Next objMember
                    Next objResult
                Else
                    Console.WriteLine("Results: No groups found.")
                End If
            Catch e As Exception
                Console.WriteLine("Error:   Enumerate failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            Console.WriteLine("Success: Enumeration complete.")
            Return

        End Sub 'Main
    End Class 'EnumMembers
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Filter** property of a **DirectorySearcher** object to select **group** objects, outputs the name of each **group** present, and uses the **member** property to output each member of each **group**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class EnumMembers
    {
        /// <summary>
        /// Enumerate AD LDS groups and group members.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;                   // Binding object.
            DirectoryEntry objGroupEntry;             // Group Results.
            DirectorySearcher objSearchADAM;          // Search object.
            SearchResultCollection objSearchResults;  // Results collection.
            string strPath;                           // Binding path.

            // Construct the binding string.
            strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US";
            Console.WriteLine("Bind to: {0}", strPath);
            Console.WriteLine("Enum:    Groups and members.");

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

            // Get search object, specify filter and scope,
            // perform search.
            try
            {
                objSearchADAM = new DirectorySearcher(objADAM);
                objSearchADAM.Filter = "(&amp;(objectClass=group))";
                objSearchADAM.SearchScope = SearchScope.Subtree;
                objSearchResults = objSearchADAM.FindAll();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Search failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Enumerate groups and members.
            try
            {
                if (objSearchResults.Count != 0)
                {
                    foreach(SearchResult objResult in objSearchResults)
                    {
                        objGroupEntry = objResult.GetDirectoryEntry();
                        Console.WriteLine("Group    {0}",
                            objGroupEntry.Name);
                        foreach(object objMember
                            in objGroupEntry.Properties["member"])
                        {
                            Console.WriteLine(" Member: {0}",
                                objMember.ToString());
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Results: No groups found.");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Enumerate failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            Console.WriteLine("Success: Enumeration complete.");
            return;
        }
    }
}
```



The Active Directory Service Interfaces (ADSI) has three enumerator helper functions that you can use from C++ to enumerate objects in AD LDS. For more information, see [Enumeration Helper Functions](https://msdn.microsoft.com/library/aa705909).

 

 




