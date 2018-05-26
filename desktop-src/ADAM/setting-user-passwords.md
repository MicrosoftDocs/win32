---
title: Setting User Passwords with Active Directory Lightweight Directory Services
description: To set the password for an AD LDS user, set authentication flags for a non-secure or secure connection, bind to the user, set the port number and method for setting the password, and set the password.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4a8a7c39-eee4-40d1-b0a2-3d2be83c3c2d
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , setting user passwords
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Setting User Passwords with Active Directory Lightweight Directory Services

To set the password for an AD LDS user, set authentication flags for a non-secure or secure connection, bind to the user, set the port number and method for setting the password, and set the password.

The following Visual Basic Scripting Edition code example uses the **GetObject** function to connect to the LDAP provider, uses the **OpenDSObject** method to bind to an AD LDS **user**, uses the **SetOption** method to set the port number and method, and sets the password with the **SetPassword** method.


```VB
' Set Password of User.

Option Explicit

Const ADS_SECURE_AUTHENTICATION =   1
Const ADS_USE_SSL               =   2
Const ADS_USE_SIGNING           =  64
Const ADS_USE_SEALING           = 128

Const ADS_OPTION_PASSWORD_PORTNUMBER = 6
Const ADS_OPTION_PASSWORD_METHOD     = 7

Const ADS_PASSWORD_ENCODE_REQUIRE_SSL = 0
Const ADS_PASSWORD_ENCODE_CLEAR       = 1

Dim intPort    ' Port for instance.
Dim lngAuth    ' Authentication flags.
Dim objLDAP    ' LDAP provider object.
Dim objUser    ' User object.
Dim strPath    ' Binding path.
Dim strPort    ' Port for instance.
Dim strServer  ' DNS Name of the computer with the AD LS installation
Dim strUser    ' User DN.

' Create LDAP provider.
Set objLDAP = GetObject("LDAP:")

' Construct the binding string.
strServer = "localhost"
strPort = "389"
intPort = CInt(strPort)
strUser = "CN=TestUser,O=Fabrikam,C=US"
strPath = "LDAP://" & strServer & ":" & strPort & "/" & strUser
WScript.Echo "Bind to:  " & strPath

' Set authentication flags.
' For non-secure connection, use LDAP port and
'  ADS_USE_SIGNING | ADS_USE_SEALING | ADS_SECURE_AUTHENTICATION
' For secure connection, use SSL port and
'  ADS_USE_SSL | ADS_SECURE_AUTHENTICATION
lngAuth = ADS_USE_SIGNING Or ADS_USE_SEALING Or _
              ADS_SECURE_AUTHENTICATION

' Bind to user object using LDAP port.
Set objUser = objLDAP.OpenDsObject(strPath, _
                                   vbNullString, vbNullString, _
                                   lngAuth)

On Error Resume Next

' Set the password for the user.
objUser.SetOption ADS_OPTION_PASSWORD_PORTNUMBER, intPort
objUser.SetOption ADS_OPTION_PASSWORD_METHOD, _
                      ADS_PASSWORD_ENCODE_CLEAR
' Be aware that, for security, a password should not be entered in code,
' but should be read from a dialog or the console.
objUser.SetPassword "ADAMComplexPassword1234"

If Err.Number <>0 Then
    WScript.Echo "Error:    Set password failed with error " _
                            & Hex(Err.Number)
Else
    WScript.Echo "Success:  Password set for user"
    WScript.Echo "          " & objUser.ADsPath
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to connect to the LDAP provider and bind to an AD LDS **user**, uses the **Invoke** method to set the port number, method, and password.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class SetPassword

        '/ <summary>
        '/ Set Password of User.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Const ADS_OPTION_PASSWORD_PORTNUMBER As Long = 6
            Const ADS_OPTION_PASSWORD_METHOD As Long     = 7

            Const ADS_PASSWORD_ENCODE_REQUIRE_SSL As Integer = 0
            Const ADS_PASSWORD_ENCODE_CLEAR As Integer       = 1

            Dim AuthTypes As AuthenticationTypes  ' Authentication flags.
            Dim intPort As Integer                ' Port for instance.
            Dim objUser As DirectoryEntry         ' User object.
            Dim strPath As String                 ' Binding path.
            Dim strPort As String                 ' Port for instance.
            Dim strServer As String               ' DNS Name of the computer with 
                                                  '  the AD LDS installation.
            Dim strUser As String                 ' User DN.

            ' Construct the binding string.
            strServer = "localhost"
            strPort = "389"
            strUser = "CN=TestUser,O=Fabrikam,C=US"
            strPath = String.Concat("LDAP://", _
                          strServer, ":", strPort, _
                          "/", strUser)
            Console.WriteLine("Bind to:  {0}", strPath)

            ' Set the authentication flags.
            ' For non-secure connection, use LDAP port and
            '  ADS_USE_SIGNING |
            '  ADS_USE_SEALING |
            '  ADS_SECURE_AUTHENTICATION
            ' For secure connection, use SSL port and
            '  ADS_USE_SSL | ADS_SECURE_AUTHENTICATION
            AuthTypes = AuthenticationTypes.Signing Or _
                        AuthenticationTypes.Sealing Or _
                        AuthenticationTypes.Secure

            ' Bind to user object using LDAP port.
            Try
                objUser = New DirectoryEntry( _
                    strPath, Nothing, Nothing, AuthTypes)
                objUser.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}.", e.Message)
                Return
            End Try

            ' Set port number, method, and password.
            intPort = Int32.Parse(strPort)
            Try
                ' Be aware that, for security, a password should
                '  not be entered in code, but should be obtained
                '  from the user interface.
                objUser.Invoke("SetOption", _
                    New Object() {ADS_OPTION_PASSWORD_PORTNUMBER, intPort})
                objUser.Invoke("SetOption", _
                    New Object() {ADS_OPTION_PASSWORD_METHOD, _
                                  ADS_PASSWORD_ENCODE_CLEAR})
                objUser.Invoke("SetPassword", _
                    New Object() {"ADAMComplexPassword1234"})
            Catch e As Exception
                Console.WriteLine("Error:   Set password failed.")
                Console.WriteLine("         {0}.", e.Message)
                Return
            End Try

            Console.WriteLine("Success: Password set.")
            Return

        End Sub 'Main
    End Class 'SetPassword
End Namespace 'ADAM_Examples
```



The following C# code example uses the **DirectoryEntry** constructor to connect to the LDAP provider and bind to an AD LDS **user**, uses the **Invoke** method to set the port number, method, and password.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class SetPassword
    {
        /// <summary>
        /// Set Password of User.
        /// </summary>
        [STAThread]
        static void Main()
        {
            const long ADS_OPTION_PASSWORD_PORTNUMBER = 6;
            const long ADS_OPTION_PASSWORD_METHOD     = 7;

            const int ADS_PASSWORD_ENCODE_REQUIRE_SSL = 0;
            const int ADS_PASSWORD_ENCODE_CLEAR       = 1;

            AuthenticationTypes AuthTypes;  // Authentication flags.
            int intPort;                    // Port for instance.
            DirectoryEntry objUser;         // User object.
            string strPath;                 // Binding path.
            string strPort;                 // Port for instance.
            string strServer;               // DNS name of the computer with
                                            //   the AD LDS installation.
            string strUser;                 // User DN.

            // Construct the binding string.
            strServer = "localhost";
            strPort = "389";
            strUser = "CN=TestUser,O=Fabrikam,C=US";
            strPath = String.Concat("LDAP://", strServer,
                ":", strPort, "/", strUser);
            Console.WriteLine("Bind to:  {0}", strPath);

            // Set authentication flags.
            // For non-secure connection, use LDAP port and
            //  ADS_USE_SIGNING |
            //  ADS_USE_SEALING |
            //  ADS_SECURE_AUTHENTICATION
            // For secure connection, use SSL port and
            //  ADS_USE_SSL | ADS_SECURE_AUTHENTICATION
            AuthTypes = AuthenticationTypes.Signing |
                AuthenticationTypes.Sealing |
                AuthenticationTypes.Secure;

            // Bind to user object using LDAP port.
            try
            {
                objUser = new DirectoryEntry(
                    strPath, null, null, AuthTypes);
                objUser.RefreshCache();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Bind failed.");
                Console.WriteLine("         {0}.", e.Message);
                return;
            }

            // Set port number, method, and password.
            intPort = Int32.Parse(strPort);
            try
            {
                //  Be aware that, for security, a password should
                //  not be entered in code, but should be obtained
                //  from the user interface.
                objUser.Invoke("SetOption", new object[]
                    {ADS_OPTION_PASSWORD_PORTNUMBER, intPort});
                objUser.Invoke("SetOption", new object[]
                    {ADS_OPTION_PASSWORD_METHOD,
                     ADS_PASSWORD_ENCODE_CLEAR});
                objUser.Invoke("SetPassword", new object[]
                    {"ADAMComplexPassword1234"});
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Set password failed.");
                Console.WriteLine("         {0}.", e.Message);
                return;
            }

            Console.WriteLine("Success: Password set.");
            return;
        }
    }
}
```



 

 




