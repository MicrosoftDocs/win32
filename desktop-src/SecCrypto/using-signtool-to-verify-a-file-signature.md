---
description: Explains how to use SignTool to verify a file signature.
ms.assetid: 9c40a397-19ea-4600-97ee-987dd10f4ef8
title: Use SignTool to Verify a File Signature
ms.topic: how-to
ms.date: 07/09/2025
# customer intent: As a Windows developer, I want to learn how to use SignTool to verify file signatures so that I can ensure their authenticity and integrity.
---

# Use SignTool to verify a file signature

SignTool is a command-line utility that you can use to verify file signatures, sign files, and time-stamp files. Verifying a file's signature ensures that the file has not been altered since it was signed and that it comes from a trusted source.

## Verify a file signature

The following command verifies the signature of a file named *MyControl.exe*:

**SignTool verify** *MyControl.exe*

If the preceding example fails, it could be that the signature used a code-signing certificate. [SignTool](signtool.md) defaults to the Windows driver policy for verification.

The following command verifies the signature, using the Default Authentication Verification Policy:

**SignTool verify /pa** *MyControl.exe*

The following command verifies a system file that may be signed in a catalog:

**SignTool verify /a** *SysFile.dll*

The following command verifies a system file that is signed in a catalog named *MyCat.cat*:

**SignTool verify /c** *MyCat.cat* *MyFile.ini*

For any [SignTool](signtool.md) verification, you can retrieve the signer of the certificate. The following command verifies a system file and displays the signer certificate:

**SignTool verify /v** *MyControl.exe*

[SignTool](signtool.md) returns command-line text that states the result of the signature check. Additionally, SignTool returns an exit code of zero for successful execution, one for failed execution, and two for execution that completed with warnings.

## Related content

[SignTool](signtool.md)

[Using SignTool to Sign a File](using-signtool-to-sign-a-file.md)