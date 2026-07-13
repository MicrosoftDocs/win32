---
description: Explains how to use SignTool to sign a file.
ms.assetid: fa8ee4d3-8927-4f7d-a09e-dbcf75a164d3
title: Use SignTool to Sign a File
ms.topic: how-to
ms.date: 07/09/2025
# customer intent: As a Windows developer, I want to learn how to use SignTool to sign files so that I can ensure their authenticity and integrity.
---

# Use SignTool to sign a file

The [SignTool](signtool.md) utility is a command-line tool that you can use to sign files, verify file signatures, and time stamp files. Signing a file provides a way to ensure the authenticity and integrity of the file. This is particularly important for executable files, such as applications and ActiveX controls, which users download from the Internet.

## Sign a file

The following command signs the file named MyControl.exe using a [certificate](../secgloss/c-gly.md) stored in a Personal Information Exchange (PFX) file:

<pre>SignTool sign /f <b>MyCert</b>.pfx MyControl.exe</pre>

The following command signs the file using a certificate stored in a password-protected PFX file:

<pre>SignTool sign /f <b>MyCert</b>.pfx /p <b>MyPassword</b> MyControl.exe</pre>

> [!NOTE]  
> Ensure that you properly protect the password.

The following command signs and time stamps the file:

<pre>SignTool sign /f <b>MyCert</b>.pfx /t http://timestamp.digicert.com MyControl.exe</pre>

> [!NOTE]  
> For information about time stamping a file after it has already been signed, see [Adding Time Stamps to Previously Signed Files](adding-time-stamps-to-previously-signed-files.md).

The following command signs the file using a certificate located in the My store with a subject name of My Company Publisher:

<pre>SignTool sign /n "<b>My Company Publisher</b>" MyControl.exe</pre>

The following command signs an ActiveX control and provides information that is displayed by Internet Explorer when the user is prompted to install the control:

<pre>SignTool sign /f <b>MyCert</b>.pfx /d "<b>My Product Name</b>" /du <b>"https://www.example.com/myproductinfo.html"</b> MyControl.exe</pre>

The following command signs the file using a certificate whose [private key](../secgloss/p-gly.md) information is protected by a hardware cryptography module. For example purposes, assume that the certificate called "My High-Value Certificate," has a private key installed in a hardware cryptography module, and the certificate is properly installed.

<pre>SignTool sign /n "<b>My High-Value Certificate</b>" MyControl.exe</pre>

The following command signs the file using a certificate whose [private key](../secgloss/p-gly.md) information is protected by a hardware cryptography module. A computer store is specified for the [certification authority](../secgloss/c-gly.md) (CA) store.

<pre>SignTool sign /n "<b>My High Value Certificate</b>" /sm /s CA MyControl.exe</pre>

The following command signs the file using a certificate stored in a file. The private key information is protected by a hardware cryptography module, and the [cryptographic service provider](../secgloss/c-gly.md) (CSP) and [key container](../secgloss/k-gly.md) are specified by name. This command is useful if the certificate is not properly installed.

<pre>SignTool sign /f <b>HighValue</b>.cer /csp "<b>Hardware Cryptography Module</b>" /k <b>HighValueContainer</b> MyControl.exe</pre>

[SignTool](signtool.md) returns command line text that states the result of the signing operation. Additionally, SignTool returns an exit code of zero for successful execution, one for failed execution, and two for execution that completed with warnings.

## Verifying a file signature

For information about verifying a file's signature, see [Using SignTool to Verify a File Signature](using-signtool-to-verify-a-file-signature.md). For information about adding a time stamp if the file has already been signed, see [Adding Time Stamps to Previously Signed Files](adding-time-stamps-to-previously-signed-files.md). For additional information about SignTool, see [SignTool](signtool.md).

## Related content

[SignTool](signtool.md)

[Using SignTool to Verify a File Signature](using-signtool-to-verify-a-file-signature.md)
