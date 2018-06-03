---
title: Creating Contact Objects
description: To create a Contact object, bind to the object that will contain the object, create a Contact object, set its properties and save the object to the directory store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 2951c0fe-cc02-4ffc-a14a-e660579899fd
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , creating contact objects
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Contact Objects

To create a **Contact** object, bind to the object that will contain the object, create a **Contact** object, set its properties and save the object to the directory store.

The following code example assumes that the schema of the AD LDS instance has been extended by [Adding Contact Classes](adding-contact-classes.md).

The following Visual Basic Scripting Edition code example defines a function that uses the **Create** method to create **Contact** objects in a selected **organization** object.


```VB
' Create Contacts.

Option Explicit

Dim lngErrNumber  ' Error number.
Dim objADAM       ' Binding object.
Dim strPath       ' Binding path.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

Function lngCreateContact(objADAMPath, _
                          strCN, _
                          strSN, _
                          strTitle, _
                          strTelephoneNumber, _
                          strGivenName, _
                          strMail, _
                          strManager)

    Dim objNewContact  ' New contact to create.

    On Error Resume Next

    ' Create new contact.
    Set objNewContact = objADAMPath.Create("Contact", "CN=" & strCN)

    ' Set attributes.
    If strSN <> "" And strSN <> vbNullString Then
        objNewContact.Put "sn", strSN
    End If
    If strTitle <> "" And strTitle <> vbNullString Then
        objNewContact.Put "title", strTitle
    End If
    If strTelephoneNumber <> "" And _
       strTelephoneNumber <> vbNullString _
    Then
        objNewContact.Put "telephoneNumber", strTelephoneNumber
    End If
    If strGivenName <> "" And strGivenName <> vbNullString Then
        objNewContact.Put "givenName", strGivenName
    End If
    If strMail <> "" And strMail <> vbNullString Then
        objNewContact.Put "mail", strMail
    End If
    If strManager <> "" And strManager <> vbNullString Then
        objNewContact.Put "manager", strManager
    End If
    objNewContact.SetInfo

    ' Return success or error.
    lngCreateContact = Err.Number

    Set objNewContact = Nothing

    On Error Goto 0

End Function

WScript.Echo "Bind to: " & strPath

On Error Resume Next

' Bind to the object.
Set objADAM = GetObject(strPath)

' If bind fails, output error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
Else
    WScript.Echo "Success: Bind succeeded."
End If

On Error Goto 0

' Create first Contact.
' Manager not specified.
lngErrNumber = lngCreateContact(objADAM, _
                                "Jane Clayton", _
                                "Clayton", _
                                "Office Manager", _
                                "+1(206)555-0101", _
                                "Jane", _
                                "janeclayton@fabrikam.us", _
                                "")
' Output success or error.
If lngErrNumber <> vbEmpty Then
    WScript.Echo "Error:   Create failed with error# " _
                         & Hex(lngErrNumber) & "."
Else
    WScript.Echo "Success: User created."
End If

' Create second Contact.
' Change "CN=Jane Clayton,O=Fabrikam,C=US" to appropriate manager.
lngErrNumber = lngCreateContact(objADAM, _
                                "Jeff Smith", _
                                "Smith", _
                                "Office Assistant", _
                                "+1(206)555-0111", _
                                "Jeff", _
                                "jeffsmith@fabrikam.us", _
                                "CN=Jane Clayton,O=Fabrikam,C=US")
' Output success or error.
If lngErrNumber <> vbEmpty Then
    WScript.Echo "Error:   Create failed with error# " _
                         & Hex(lngErrNumber) & "."
Else
    WScript.Echo "Success: User created."
End If
```



The following Visual Basic .NET code example defines a function that uses the **Add** method to create **Contact** objects in a selected **organization** object.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class CreateContacts

        '/ <summary>
        '/ Create a single Contact.
        '/ </summary>

        Private Shared Function CreateContact( _
                                    objADAMPath As DirectoryEntry, _
                                    strCN As String, _
                                    strSN As String, _
                                    strTitle As String, _
                                    strTelephoneNumber As String, _
                                    strGivenName As String, _
                                    strMail As String, _
                                    strManager As String) As Boolean

            Dim objNewContact As DirectoryEntry  ' New Contact to create.

            ' Create new contact and set attributes.
            Try
                objNewContact = objADAMPath.Children.Add(strCN, "Contact")
                If strSN <> "" Or strSN <> String.Empty Then
                    objNewContact.Properties("sn").Add(strSN)
                End If
                If strTitle <> "" Or strTitle <> String.Empty Then
                    objNewContact.Properties("title").Add(strTitle)
                End If
                If strTelephoneNumber <> "" Or _
                    strTelephoneNumber <> String.Empty Then
                    objNewContact.Properties("telephoneNumber").Add( _
                       strTelephoneNumber)
                End If
                If strGivenName <> "" Or strGivenName <> String.Empty Then
                    objNewContact.Properties("givenName").Add(strGivenName)
                End If
                If strMail <> "" Or strMail <> String.Empty Then
                    objNewContact.Properties("mail").Add(strMail)
                End If
                If strManager <> "" Or strManager <> String.Empty Then
                    objNewContact.Properties("manager").Add(strManager)
                End If
                objNewContact.CommitChanges()
            Catch e As Exception
                Console.WriteLine("Error:   {0}", e.ToString())
                Return False
            End Try

            Console.WriteLine("Success:  Contact created.")
            Return True

        End Function 'CreateContact

        '/ <summary>
        '/ Create Contacts.
        '/ </summary>

        <STAThread()>  Shared Sub Main()
            Dim objADAM As DirectoryEntry  ' Binding object.
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

            ' Create first Contact.
            ' Manager not specified.
            If Not CreateContacts.CreateContact( _
                                      objADAM, _
                                      "CN=Jane Clayton", _
                                      "Clayton", _
                                      "Office Manager", _
                                      "+1(206)555-0101", _
                                      "Jane", _
                                      "janeclayton@fabrikam.us", _
                                      "") _
            Then
                Return
            End If

            ' Create second Contact.
            ' Change "CN=Jane Clayton,O=Fabrikam,C=US"
            '  to appropriate manager.
            If Not CreateContacts.CreateContact( _
                                      objADAM, _
                                      "CN=Jeff Smith", _
                                      "Smith", _
                                      "Office Assistant", _
                                      "+1(206)555-0111", _
                                      "Jeff", _
                                      "jeffsmith@fabrikam.us", _
                                      "CN=Jane Clayton,O=Fabrikam,C=US") _
            Then
                Return
            End If

            Return

        End Sub 'Main
    End Class 'CreateContacts
End Namespace 'ADAM_Examples
```



The following C# code example defines a function that uses the **Add** method to create **Contact** objects in a selected **organization** object.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class CreateContacts
    {
        /// <summary>
        /// Create a single Contact.
        /// </summary>

        private static bool CreateContact(
            DirectoryEntry objADAMPath,
            string strCN,
            string strSN,
            string strTitle,
            string strTelephoneNumber,
            string strGivenName,
            string strMail,
            string strManager)
        {
            DirectoryEntry objNewContact;  // New Contact to create.

            // Create new contact and set attributes.
            try
            {
                objNewContact = objADAMPath.Children.Add(
                    strCN, "Contact");
                if (strSN != "" || strSN != String.Empty)
                    objNewContact.Properties["sn"].Add(strSN);
                if (strTitle != "" || strTitle != String.Empty)
                    objNewContact.Properties["title"].Add(strTitle);
                if (strTelephoneNumber != "" ||
                    strTelephoneNumber != String.Empty)
                    objNewContact.Properties[
                        "telephoneNumber"].Add(strTelephoneNumber);
                if (strGivenName != "" || strGivenName != String.Empty)
                    objNewContact.Properties[
                        "givenName"].Add(strGivenName);
                if (strMail != "" || strMail != String.Empty)
                    objNewContact.Properties["mail"].Add(strMail);
                if (strManager != "" || strManager != String.Empty)
                    objNewContact.Properties["manager"].Add(strManager);
                objNewContact.CommitChanges();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   {0}", e.ToString());
                return false;
            }

            Console.WriteLine("Success:  Contact created.");
            return true;
        }

        /// <summary>
        /// Create Contacts.
        /// </summary>

        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;   // Binding object.
            string strPath;           // Binding path.

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

            // Create first Contact.
            // Manager not specified.
            if (!CreateContacts.CreateContact(
                objADAM,
                "CN=Jane Clayton",
                "Clayton",
                "Office Manager",
                "+1(206)555-0101",
                "Jane",
                "janeclayton@fabrikam.us",
                ""))
            {
                return;
            }
 
            // Create second Contact.
            // Change "CN=Jane Clayton,O=Fabrikam,C=US"
            // to appropriate manager.
            if (!CreateContacts.CreateContact(
                objADAM,
                "CN=Jeff Smith",
                "Smith",
                "Office Assistant",
                "+1(206)555-0111",
                "Jeff",
                "jeffsmith@fabrikam.us",
                "CN=Jane Clayton,O=Fabrikam,C=US"))
            {
                return;
            }

            return;
        }
    }
}
```



 

 




