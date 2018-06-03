---
title: Adding User Classes
description: To extend the AD LDS schema to include object class definitions for four additional user classes (inetOrgPerson, User, Organizational-Person, and Person) use the definitions for these object classes in the MS-\ .ldf files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 855ddc43-76c6-47cb-81b6-42a794044eda
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , adding user classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding User Classes

To extend the AD LDS schema to include object class definitions for four additional user classes (**inetOrgPerson**, **User**, **Organizational-Person**, and **Person**) use the definitions for these object classes in the MS-\*.ldf files.

The MS-\*.ldf files are LDAP Data Interchange Format (LDIF) files. The MS-InetOrgPerson.ldf file contains the definitions for all user classes. The MS-User.ldf file contains the definitions for all user classes excluding the **inetOrgPerson** class. The MS-UserProxy.ldf file contains the definitions for the **UserProxy** class only. The AD LDS installation process installs these LDIF files in the folder that contains the AD LDS program files.

Use the following command to run the LDIFDE utility to load one of the LDIF files.

*ADAMPath***\\ldifde.exe -i -f** *ADAMPath***\\***MSFile* **-s** *servername***:***Port* \[**-b** *Username Domain Password*\] **-k -j . -c "CN=Schema,CN=Configuration,DC=X" \#schemaNamingContext**

In the preceding command:

-   *ADAMPath* is the installation path of AD LDS program files: %windir%\\AD LDS.
-   *MSFile* is the name of the LDIF file to load.
-   *servername* is the name of the computer with the AD LDS installation. Use *localhost* if the AD LDS installation is on a local computer.
-   *Port* is the LDAPport of the AD LDS instance. The default is 389.
-   *Username* is the user name for the account to use to authenticate.
-   *Domain* is the domain of the authentication user.
-   *Password* is the password of the authentication user.

The command uses the credentials of the currently logged on user if you do not specify the **-b** option and its parameters.

For more information about extending the Active Directory schema using the LDIFDE utility, see [LDIF Scripts](https://msdn.microsoft.com/library/ms677268).

After extending the schema with the following code example, create **inetOrgPerson** objects by [Creating inetOrgPerson Objects](creating-inetorgperson-objects.md).

The following Visual Basic Scripting Edition code example creates a command line to run the **ldifde.exe** application to load the MS-InetOrgPerson.ldf file that is installed with AD LDS.


```VB
' Extend Schema with AD LDS User Classes.

' Use ldifde.exe to load MS-*.ldf to an AD LDS instance
' while verifying the file signature with AdamSchema.cat.
' Creates a log file ldif.log in the script directory.

Option Explicit

Const conWindowStyle  =    1
Const conWaitOnReturn = True

Dim objShell        ' Command shell object.
Dim strADAMPath     ' Path to AD LDS installation.
Dim strCommandLine  ' Extend command line.
Dim strFileName     ' LDIF file to load.
Dim strServerPort   ' AD LDS Installation and port.

' Specify LDIF file name.
'  MS-InetOrgPerson.ldf for all user classes
'  including inetOrgPerson, but without UserProxy.
'  MS-User.ldf for user classes
'  without inetOrgPerson and UserProxy.
'  MS-UserProxy.ldf for UserProxy class only.
strFileName = "MS-InetOrgPerson.ldf"

' Construct the binding string.
' The binding string used assumes the following:
'   The AD LDS installation is on a local computer
'   The port used is the default port 389.
' 
' Modify the binding string as appropriate.
strServerPort = "localhost:389"

' Specify the path for the AD LDS installation.
strADAMPath  = "!windir!\AD LDS\"

' Construct the command.
strCommandLine = _
"cmd /v:on /k """"" & strADAMPath   & "ldifde.exe" & """ -i" & _
           " -f """ & strADAMPath   & strFileName & _
           """ -s " & strServerPort & " -k -j ." & _
           " -c ""CN=Schema,CN=Configuration,DC=X""" & _
           " #schemaNamingContext"""

WScript.Echo "Execute:" & vbNewLine & strCommandLine

Set objShell = WScript.CreateObject("WScript.Shell")

objShell.Run strCommandLine, conWindowStyle, conWaitOnReturn
```



The following Visual Basic .NET code example creates a command line to run the **ldifde.exe** application to load the MS-InetOrgPerson.ldf file that is installed with AD LDS.


```VB
Imports System
Imports System.Diagnostics
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class ExtendSchemaADAMUser

        '/ <summary>
        '/ Extend Schema with AD LDS User Classes.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            ' Use ldifde.exe to load MS-*.ldf to an AD LDS instance
            ' while verifying the file signature with AdamSchema.cat.
            ' Creates a log file ldif.log in the script directory.

            Dim strADAMPath As String     ' Path to AD LDS installation.
            Dim strCommandLine As String  ' Extend command line.
            Dim strFileName As String     ' LDIF file to load.
            Dim strServerPort As String   ' AD LDS Installation and port.

            ' Specify LDIF file name.
            ' MS-InetOrgPerson.ldf for all user classes
            ' including inetOrgPerson, but without UserProxy.
            ' MS-User.ldf for user classes
            ' without inetOrgPerson and UserProxy.
            ' MS-UserProxy.ldf for UserProxy class only.
            strFileName = "MS-InetOrgPerson.ldf"

            ' Construct the binding string.
            ' The binding string used assumes the following:
            '   The AD LDS installation is on a local computer.
            '   The port used is the default port 389.
            ' 
            ' Modify the binding string as appropriate.
            strServerPort = "localhost:389"

            ' Specify path for AD LDS installation.
            strADAMPath = "!windir!\AD LDS\"

            ' Construct the command.
            strCommandLine = String.Concat( _
                "/v:on /k """"", strADAMPath, "ldifde.exe"" -i", _
                " -f """, strADAMPath, strFileName, """", " -s ", _
                strServerPort, " -k -j .", _
                " -c ""CN=Schema,CN=Configuration,DC=X""", _
                " #schemaNamingContext""")

            Console.WriteLine("Execute:  \n{0}", strCommandLine)

            ' Execute the command.
            Try
                Process.Start("cmd.exe", strCommandLine)
            Catch e As Exception
                Console.WriteLine("Error:   Extending schema failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            Console.WriteLine("Success: Extending schema completed.")
            Return

        End Sub 'Main
    End Class 'ExtendSchemaADAMUser
End Namespace 'ADAM_Examples
```



The following C# code example creates a command line to run the ldifde.exe application to load the MS-InetOrgPerson.ldf file that is installed with AD LDS.


```CSharp
using System;
using System.Diagnostics;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class ExtendSchemaADAMUser
    {
        /// <summary>
        /// Extend Schema with AD LDS User Classes.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // Use ldifde.exe to load MS-*.ldf to an AD LDS instance
            // while verifying the file signature with AdamSchema.cat.
            // Creates a log file ldif.log in the script directory.

            string strADAMPath;     // Path to AD LDS installation.
            string strCommandLine;  // Extend command line.
            string strFileName;     // LDIF file to load.
            string strServerPort;   // AD LDS Installation and port.

            // Specify LDIF file name.
            // MS-InetOrgPerson.ldf for all user classes
            // including inetOrgPerson, but without UserProxy.
            // MS-User.ldf for user classes
            // without inetOrgPerson and UserProxy.
            // MS-UserProxy.ldf for UserProxy class only.
            strFileName = "MS-InetOrgPerson.ldf";

            // Construct the binding string.
            // The binding string used assumes the following:
            //   The AD LDS installation is on a local computer.
            //   The port used is the default port 389.
            // 
            // Modify the binding string as appropriate.
            strServerPort = "localhost:389";

            // Specify the path for the AD LDS installation.
            strADAMPath  = "!windir!\\AD LDS\\";

            // Construct the command.
            strCommandLine = String.Concat(
                "/v:on /k \"\"", strADAMPath, "ldifde.exe\" -i",
                " -f \"", strADAMPath, strFileName, "\"",
                " -s ", strServerPort, " -k -j .",
                " -c \"CN=Schema,CN=Configuration,DC=X\"",
                " #schemaNamingContext\"");

            Console.WriteLine("Execute:\n{0}", strCommandLine);

            // Execute the command.
            try
            {
                Process.Start("cmd.exe", strCommandLine);
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Extending schema failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            Console.WriteLine("Success: Extending schema completed.");
            return;
        }
    }
}
```



 

 




