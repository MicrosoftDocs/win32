---
title: Getting a List of Specified Objects
description: To search Active Directory Lightweight Directory Services (AD LDS) for specific objects, specify a filter that limits the type of objects selected.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '6c08543e-5d7a-4c1d-a3a1-c26c87e2fe65'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["AD LDS examples ADAM , getting a list of specified objects"]
---

# Getting a List of Specified Objects

To search Active Directory Lightweight Directory Services (AD LDS) for specific objects, specify a filter that limits the type of objects selected.

For more information about filtering in a query, see [Creating a Query Filter](https://msdn.microsoft.com/library/ms675768).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organizationalUnit** object, uses the **Filter** property to select **group** objects, and outputs the name of each **group** present in the **organizationalUnit**.


```VB
' Enumerate filtered AD LDS objects.

Option Explicit

Dim objADAM    ' Binding object.
Dim objFilter  ' Filter object.
Dim strFilter  ' Filter to select objects.
Dim strPath    ' Binding path.

' Construct the binding string.
strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify filtered object type.
strFilter = "group"

WScript.Echo "Filter:  " & strFilter

On Error Resume Next

' Bind to object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

' Enumerate filtered objects.
objADAM.Filter = Array(strFilter)
For Each objFilter in objADAM
    WScript.Echo objFilter.Name
Next

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Filtered enumeration failed."
Else
    WScript.Echo "Success: Filtered enumeration complete."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Filter** property of a **DirectorySearcher** object to select **group** objects, and outputs the name of each **group** present in the **organizationalUnit**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class FilterObjects

        '/ <summary>
        '/ Enumerate filtered AD LDS objects.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry                   ' Binding object.
            Dim objEntry As DirectoryEntry                  ' DirectoryEntry in Results.
            Dim objSearchADAM As DirectorySearcher          ' Search object.
            Dim objSearchResults As SearchResultCollection  ' Results collection.
            Dim strFilter As String                         ' Filter to select objects.
            Dim strPath As String                           ' Binding path.

            ' Construct the binding string.
            strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US"
            Console.WriteLine("Bind to: {0}", strPath)

            ' Specify filter.
            strFilter = "(&amp;(objectClass=group))"
            Console.WriteLine("Filter:  {0}", strFilter)

            ' Get AD LDS object.
            Try
                objADAM = New DirectoryEntry(strPath)
                objADAM.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Get search object,
            '  specify filter and scope,
            '  perform search.
            Try
                objSearchADAM = New DirectorySearcher(objADAM)
                objSearchADAM.Filter = strFilter
                objSearchADAM.SearchScope = SearchScope.Subtree
                objSearchResults = objSearchADAM.FindAll()
            Catch e As Exception
                Console.WriteLine("Error:   Search failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Enumerate filtered objects.
            Try
                If objSearchResults.Count <> 0 Then
                    Console.WriteLine("Results: Following objects found.")
                    Dim objResult As SearchResult
                    For Each objResult In  objSearchResults
                        objEntry = objResult.GetDirectoryEntry()
                        Console.WriteLine("         {0}", objEntry.Name)
                    Next objResult
                Else
                    Console.WriteLine("Results: No objects found.")
                End If
            Catch e As Exception
                Console.WriteLine("Error:   Enumerate failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            Console.WriteLine("Success: Filtered enumeration complete.")
            Return

        End Sub 'Main
    End Class 'FilterObjects
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to bind to an **organizationalUnit** object, uses the **Filter** property of a **DirectorySearcher** object to select **group** objects, and outputs the name of each **group** present in the **organizationalUnit**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class FilterObjects
    {
        /// <summary>
        /// Enumerate filtered AD LDS objects.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;                   // Binding object.
            DirectoryEntry objEntry;                  // DirectoryEntry in Results.
            DirectorySearcher objSearchADAM;          // Search object.
            SearchResultCollection objSearchResults;  // Results collection.
            string strFilter;                         // Filter to select objects.
            string strPath;                           // Binding path.

            // Construct the binding string.
            strPath = "LDAP://localhost:389/OU=TestOU,O=Fabrikam,C=US";
            Console.WriteLine("Bind to: {0}", strPath);

            // Specify filter.
            strFilter = "(&amp;(objectClass=group))";
            Console.WriteLine("Filter:  {0}", strFilter);

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

            // Get search object,
            //  specify filter and scope,
            //  perform search.
            try
            {
                objSearchADAM = new DirectorySearcher(objADAM);
                objSearchADAM.Filter = strFilter;
                objSearchADAM.SearchScope = SearchScope.Subtree;
                objSearchResults = objSearchADAM.FindAll();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Search failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Enumerate filtered objects.
            try
            {
                if (objSearchResults.Count != 0)
                {
                    Console.WriteLine(
                        "Results: Following objects found.");
                    foreach(SearchResult objResult in objSearchResults)
                    {
                        objEntry = objResult.GetDirectoryEntry();
                        Console.WriteLine("         {0}", objEntry.Name);
                    }
                }
                else
                {
                    Console.WriteLine("Results: No objects found.");
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Enumerate failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            Console.WriteLine("Success: Filtered enumeration complete.");
            return;
        }
    }
}
```



The Platform Software Development Kit (SDK) includes a code example topic, DsSrch, that provides a command-prompt application written in C++ that uses the [**IDirectorySearch**](https://msdn.microsoft.com/library/aa746362) interface to query an AD LDS instance. The complete code example is included in the Platform SDK in the **Samples\\NetDs\\ADSI\\Samples\\General\\DsSrch** directory. For more information about using the **IDirectorySearch** interface, see [Searching with the IDirectorySearch Interface](https://msdn.microsoft.com/library/aa746472).

 

 




