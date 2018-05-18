---
title: Binding to an Instance
description: To bind to an Active Directory Lightweight Directory Services (AD LDS) object, use a binding string that specifies the path to an AD LDS instance and a specified object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '0a5e8a0f-f331-4b6a-9559-a34617f5c43d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["Binding to an Instance ADAM", "AD LDS examples ADAM , binding to an instance"]
---

# Binding to an Instance

To bind to an Active Directory Lightweight Directory Services (AD LDS) object, use a binding string that specifies the path to an AD LDS instance and a specified object.

The binding string uses the LDAP provider and requires the following form:

**LDAP://***host name\[/object name\]*

In this string:

-   **LDAP:** specifies the LDAP provider.
-   *host name* specifies the Domain Name System (DNS) name of the computer with the AD LDS installation and the TCP port to use. The host name is in the format *DNS Name:TCP Port Number*. For example, to bind to an AD LDS installation on a computer with a DNS Name of *fabrikam1* using TCP port 389, specify *LDAP://fabrikam1:389*.

    If the TCP port is not specified, the bind operation uses TCP port 389 for non-SSL connections or port 636 for SSL connections.

    To bind to an AD LDS installation on a local computer, specify *localhost* for the host name.

-   *object name* represents a specific AD LDS object and is optional. The *object name* can be a distinguished name or an object GUID. If absent, the bind operation selects the RootDSE object.

For more information about LDAP binding strings, see [LDAP ADsPath](https://msdn.microsoft.com/library/aa746384).

The following Visual Basic Scripting Edition code example uses the [GetObject](http://go.microsoft.com/fwlink/p/?linkid=139824) function to bind to the application directory partition of an AD LDS instance and outputs some of its attributes.


```VB
' Bind to AD LDS object.

Option Explicit

Dim objADAM    ' Object to bind to.
Dim strObject  ' DN of object to bind to.
Dim strPath    ' Binding path.
Dim strPort    ' TCP port.
Dim strServer  ' DNS Name of the computer with the AD LDS installation.

' In this example, the AD LDS installation is on a local computer
strServer = "localhost"

' Optional TCP port.
strPort = "389"

' Optional object name.
strObject = "O=Fabrikam,C=US"

' Construct the binding string.
strPath = "LDAP://"
If strServer <> "" and strServer <> vbNullString Then
    strPath = strPath & strServer
Else
    WScript.Echo "Error: Invalid hostname specified."
    WScript.Quit
End If
If strPort <> "" and strPort <> vbNullString Then
    strPath = strPath & ":" & strPort
End If
If strObject <> "" and strObject <> vbNullString Then
    strPath = strPath & "/" & strObject
End If
WScript.Echo "Bind to: " & strPath
WScript.Echo

On Error Resume Next

' Get AD LDS object.
Set objADAM = GetObject(strPath)

' Output object attributes or error.
If Err.Number = vbEmpty Then
    WScript.Echo "Success: Bind succeeded."
    WScript.Echo "Name:    " & objADAM.Name
    WScript.Echo "Parent:  " & objADAM.Parent
    WScript.Echo "DN:      " & objADAM.distinguishedName
    WScript.Echo "Created: " & objADAM.whenCreated
    WScript.Quit
Else
    WScript.Echo "Error:   Bind failed."
End If
```



The following Visual Basic .NET code example uses the [DirectoryEntry]( http://go.microsoft.com/fwlink/p/?linkid=139825) constructor function to bind to the application directory partition of an AD LDS instance and outputs some of its properties.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class BindToADAM

        '/ <summary>
        '/ Bind to AD LDS object.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry ' Directory object
            Dim strObject As String       ' DN of object to bind to.
            Dim strPath As String         ' Bind string.
            Dim strPort As String         ' Optional TCP Port.
            Dim strServer As String       ' DNS Name of the computer with
                                          ' the AD LDS installation.

            ' In this example the AD LDS installation is on a local computer.
            strServer = "localhost"

            ' TCP Port to use
            strPort = "389"

            ' Distinguished name of the object.
            strObject = "O=Fabrikam,C=US"

            ' Construct the binding string.
            strPath = "LDAP://"
            If strServer.Equals("") Or _
                strServer.Equals(String.Empty) Then
                Console.WriteLine("Error: Invalid hostname specified.")
                Return
            Else
                strPath = String.Concat(strPath, strServer)
            End If

            If Not strPort.Equals("") And _
                Not strPort.Equals(String.Empty) Then
                strPath = String.Concat(strPath, ":", strPort)
            End If

            If Not strObject.Equals("") And _
                Not strObject.Equals(String.Empty) Then
                strPath = String.Concat(strPath, "/", strObject)
            End If

            Console.WriteLine("Bind to: {0}", strPath)

            ' Get the specified object.
            Try
                objADAM = New DirectoryEntry(strPath)
                objADAM.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}.", e.Message)
                Return
            End Try

            ' Output object attributes.
            Console.WriteLine("Success: Bind succeeded.")
            Console.WriteLine("Name:    {0}", objADAM.Name)
            Console.WriteLine("Path:    {0}", objADAM.Path)
            Return

        End Sub 'Main
    End Class 'BindToADAM
End Namespace 'ADAM_Examples
```



The following C# code example uses the [DirectoryEntry]( http://go.microsoft.com/fwlink/p/?linkid=139825) constructor function to bind to the application directory partition of an AD LDS instance and outputs some of its properties.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class BindToADAM
    {
        /// <summary>
        /// Bind to AD LDS object.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;  // Directory object.
            string strObject;        // DN of object to bind to.
            string strPath;          // Bind path.
            string strPort;          // Optional TCP port.
            string strServer;        // DNS Name of the computer with the
                                     // AD LDS installation

            // In this example, the AD LDS installation is on a local computer
            strServer = "localhost";

            // TCP Port to use
            strPort = "389";

            // Distinguished name of the object.
            strObject = "O=Fabrikam,C=US";

            // Construct the binding string.
            strPath = "LDAP://";
            if (strServer.Equals("") || strServer.Equals(String.Empty))
            {
                Console.WriteLine("Error: Invalid hostname specified.");
                return;
            }
            else
            {
                strPath = String.Concat(strPath, strServer);
            }

            if (!strPort.Equals("") &amp;&amp; !strPort.Equals(String.Empty))
            {
                strPath = String.Concat(strPath, ":", strPort);
            }

            if (!strObject.Equals("") &amp;&amp; !strObject.Equals(String.Empty))
            {
                strPath = String.Concat(strPath, "/", strObject);
            }

            Console.WriteLine("Bind to: {0}", strPath);

            // Get the specified object.
            try
            {
                objADAM = new DirectoryEntry(strPath);
                objADAM.RefreshCache();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Bind failed.");
                Console.WriteLine("         {0}.", e.Message);
                return;
            }

            // Output object attributes.
            Console.WriteLine("Success: Bind succeeded.");
            Console.WriteLine("Name:    {0}", objADAM.Name);
            Console.WriteLine("Path:    {0}", objADAM.Path);
            return;
        }
    }
}
```



Use the [**ADsGetObject**](https://msdn.microsoft.com/library/aa772184) function to bind to an AD LDS instance using C++. For more information, see [Binding With GetObject and ADsGetObject](https://msdn.microsoft.com/library/aa772325).

 

 




