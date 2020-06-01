---
Description: Explains how to use SignTool to sign a file.
ms.assetid: fa8ee4d3-8927-4f7d-a09e-dbcf75a164d3
title: Using SignTool to Sign a File
ms.topic: article
ms.date: 05/31/2018
---

# Using SignTool to Sign a File

The following command signs the file named MyControl.exe using a [*certificate*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) stored in a Personal Information Exchange (PFX) file:

_SignTool sign /f***MyCert***.pfx MyControl.exe_

The following command signs the file using a certificate stored in a password-protected PFX file:

_SignTool sign /f***MyCert***.pfx /p***MyPassword* **MyControl.exe_

> [!Note]  
> Ensure that you properly protect the password.

 

The following command signs and time stamps the file:

_SignTool sign /f***MyCert***.pfx /t https[]()://timestamp.digicert.com MyControl.exe_

> [!Note]  
> For information about time stamping a file after it has already been signed, see [Adding Time Stamps to Previously Signed Files](adding-time-stamps-to-previously-signed-files.md).

 

The following command signs the file using a certificate located in the My store with a subject name of My Company Publisher:

_SignTool sign /n "My Company Publisher" MyControl.exe_

The following command signs an ActiveX control and provides information that is displayed by Internet Explorer when the user is prompted to install the control:

_SignTool sign /f MyCert.pfx /d "***My Product Name***" /du "https://www.***example***.com/***my\_product***/info.html" MyControl.exe_

The following command signs the file using a certificate whose [*private key*](https://msdn.microsoft.com/library/ms721603(v=VS.85).aspx) information is protected by a hardware cryptography module. For example purposes, assume that the certificate called "My High-Value Certificate," has a private key installed in a hardware cryptography module, and the certificate is properly installed.

_SignTool sign /n "My High-Value Certificate" MyControl.exe_

The following command signs the file using a certificate whose [*private key*](https://msdn.microsoft.com/library/ms721603(v=VS.85).aspx) information is protected by a hardware cryptography module. A computer store is specified for the [*certification authority*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) (CA) store.

_SignTool sign /n "***My High Value Certificate***" /sm /s CA MyControl.exe_

The following command signs the file using a certificate stored in a file. The private key information is protected by a hardware cryptography module, and the [*cryptographic service provider*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) (CSP)and [*key container*](https://msdn.microsoft.com/library/ms721590(v=VS.85).aspx) are specified by name. This command is useful if the certificate is not properly installed.

_SignTool sign /f***HighValue***.cer /csp "***Hardware Cryptography Module***" /k***HighValueContainer***MyControl.exe_

[SignTool](signtool.md) returns command line text that states the result of the signing operation. Additionally, SignTool returns an exit code of zero for successful execution, one for failed execution, and two for execution that completed with warnings.

For information about verifying a file's signature, see [Using SignTool to Verify a File Signature](using-signtool-to-verify-a-file-signature.md). For information about adding a time stamp if the file has already been signed, see [Adding Time Stamps to Previously Signed Files](adding-time-stamps-to-previously-signed-files.md). For additional information about [SignTool](signtool.md), see [SignTool](signtool.md).

 

 



