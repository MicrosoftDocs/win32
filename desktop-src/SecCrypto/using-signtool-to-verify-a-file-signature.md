---
description: Explains how to use SignTool to verify a file signature.
ms.assetid: 9c40a397-19ea-4600-97ee-987dd10f4ef8
title: Using SignTool to Verify a File Signature
ms.topic: article
ms.date: 05/31/2018
---

# Using SignTool to Verify a File Signature

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

For more information about [SignTool](signtool.md), see [SignTool](signtool.md).

 

 



