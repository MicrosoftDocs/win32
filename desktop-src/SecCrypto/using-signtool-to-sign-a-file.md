---
Description: Explains how to use SignTool to sign a file.
ms.assetid: fa8ee4d3-8927-4f7d-a09e-dbcf75a164d3
title: Using SignTool to Sign a File
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using SignTool to Sign a File

The following command signs the file named MyControl.exe using a [*certificate*](https://www.bing.com/search?q=*certificate*) stored in a Personal Information Exchange (PFX) file:

**SignTool sign /f***MyCert***.pfx MyControl.exe**

The following command signs the file using a certificate stored in a password-protected PFX file:

**SignTool sign /f***MyCert***.pfx /p***MyPassword* **MyControl.exe**

> [!Note]  
> Ensure that you properly protect the password.

 

The following command signs and time stamps the file:

**SignTool sign /f***MyCert***.pfx /t http://timestamp.verisign.com/scripts/timstamp.dll MyControl.exe**

> [!Note]  
> For information about time stamping a file after it has already been signed, see [Adding Time Stamps to Previously Signed Files](adding-time-stamps-to-previously-signed-files.md).

 

The following command signs the file using a certificate located in the My store with a subject name of My Company Publisher:

**SignTool sign /n "My Company Publisher" MyControl.exe**

The following command signs an ActiveX control and provides information that is displayed by Internet Explorer when the user is prompted to install the control:

**SignTool sign /f MyCert.pfx /d "***My Product Name***" /du "http://www.***example***.com/***my\_product***/info.html" MyControl.exe**

The following command signs the file using a certificate whose [*private key*](https://www.bing.com/search?q=*private key*) information is protected by a hardware cryptography module. For example purposes, assume that the certificate called "My High-Value Certificate," has a private key installed in a hardware cryptography module, and the certificate is properly installed.

**SignTool sign /n "My High-Value Certificate" MyControl.exe**

The following command signs the file using a certificate whose [*private key*](https://www.bing.com/search?q=*private key*) information is protected by a hardware cryptography module. A computer store is specified for the [*certification authority*](https://www.bing.com/search?q=*certification authority*) (CA) store.

**SignTool sign /n "***My High Value Certificate***" /sm /s CA MyControl.exe**

The following command signs the file using a certificate stored in a file. The private key information is protected by a hardware cryptography module, and the [*cryptographic service provider*](https://www.bing.com/search?q=*cryptographic service provider*) (CSP)and [*key container*](https://www.bing.com/search?q=*key container*) are specified by name. This command is useful if the certificate is not properly installed.

**SignTool sign /f***HighValue***.cer /csp "***Hardware Cryptography Module***" /k***HighValueContainer***MyControl.exe**

[SignTool](signtool.md) returns command line text that states the result of the signing operation. Additionally, SignTool returns an exit code of zero for successful execution, one for failed execution, and two for execution that completed with warnings.

For information about verifying a file's signature, see [Using SignTool to Verify a File Signature](using-signtool-to-verify-a-file-signature.md). For information about adding a time stamp if the file has already been signed, see [Adding Time Stamps to Previously Signed Files](adding-time-stamps-to-previously-signed-files.md). For additional information about [SignTool](signtool.md), see [SignTool](signtool.md).

 

 



