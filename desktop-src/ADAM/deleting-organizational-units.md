---
title: Deleting Organizational Units
description: To delete an organizational unit (OU), bind to the object that contains the OU and delete the organizationalUnit object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9fe6be75-dd91-4abc-86a3-07c33883572b
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , deleting organizational units
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Deleting Organizational Units

To delete an organizational unit (OU), bind to the object that contains the OU and delete the **organizationalUnit** object.

Create the object you delete with the following code example by [Creating Organizational Units](creating-organizational-units.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organization** object and uses the **Delete** method to delete a selected **organizationalUnit** object in that **organization**.


```VB
' Delete the AD LDS Organizational Unit.

Option Explicit

Dim objADAM  ' Binding object.
Dim strOU    ' Organizational unit to delete.
Dim strPath  ' Binding path.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify the Organizational Unit.
strOU = "OU=TestOU"

On Error Resume Next

' Bind to the object.
Set objADAM = GetObject(strPath)

' If bind fails, output error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

WScript.Echo "Delete:  " & strOU

' Delete the Organizational Unit.
objADAM.Delete "organizationalUnit", strOU

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Delete failed."
Else
    WScript.Echo "Success: Organizational Unit deleted."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** method to bind to an **organization** object, uses the **Find** method to bind a selected **organizationalUnit** object, and uses the **Remove** method to delete the selected **organizationalUnit** from that **organization**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class DeleteOU

        '/ <summary>
        '/ Delete AD LDS Organizational Unit.
        '/ </summary>

        <STAThread()>  Shared Sub Main()
            Dim objADAM As DirectoryEntry  ' Binding object.
            Dim objOU As DirectoryEntry    ' Organizational unit.
            Dim strOU As String            ' Organiztional unit.
            Dim strPath As String          ' Binding path.

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

            ' Specify the Organizational Unit.
            strOU = "OU=TestOU"

            Console.WriteLine("Delete:  {0}", strOU)

            ' Delete the Organizational Unit.
            Try
                objOU = objADAM.Children.Find(strOU, "OrganizationalUnit")
                objADAM.Children.Remove(objOU)
            Catch e As Exception
                Console.WriteLine("Error:   Delete failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output success.
            Console.WriteLine("Success: Organizational Unit deleted.")
            Return

        End Sub 'Main
    End Class 'DeleteOU
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** method to bind to an **organization** object, uses the **Find** method to bind a selected **organizationalUnit** object, and uses the **Remove** method to delete the selected **organizationalUnit** from that **organization**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class DeleteOU
    {
        /// <summary>
        /// Delete AD LDS Organizational Unit.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;  // Binding object.
            DirectoryEntry objOU;    // Organizational unit.
            string strOU;            // Organiztional unit.
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

            // Specify the Organizational Unit.
            strOU = "OU=TestOU";

            Console.WriteLine("Delete:  {0}", strOU);

            // Delete the Organizational Unit.
            try
            {
                objOU = objADAM.Children.Find(strOU,
                    "OrganizationalUnit");
                objADAM.Children.Remove(objOU);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Delete failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output success.
            Console.WriteLine("Success: Organizational Unit deleted.");
            return;
        }
    }
}
```



 

 




