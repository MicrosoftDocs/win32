---
description: Crypt32.dll is the module that implements many of the CryptoAPI functions.
ms.assetid: b6063c92-5831-4b78-b2cd-812e55194bc9
title: Crypt32.dll Versions
ms.topic: article
ms.date: 05/31/2018
---

# Crypt32.dll Versions

Crypt32.dll is the module that implements many of the Certificate and Cryptographic Messaging functions in the CryptoAPI, such as [**CryptSignMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignmessage). Crypt32.dll is a module that comes with the Windows and Windows Server operating systems, but different versions of this DLL provide different capabilities. There is no API to determine the version of CryptoAPI that is in use, but you can determine the version of Crypt32.dll that is currently in use by using the [**GetFileVersionInfo**](/windows/win32/api/winver/nf-winver-getfileversioninfoa) and [**VerQueryValue**](/windows/win32/api/winver/nf-winver-verqueryvaluea) functions.

In general, the version ranges of Crypt32.dll map to the operating system versions as shown in the following table. However, this table should be used as a guideline only because it is possible, through other update avenues, that the Crypt32.dll version will differ from the one indicated in the table.

| Crypt32.dll version                               | Operating system                                                                                                                                                                |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *version* >= 5.131.3790.0                      | Windows Server 2003                                                                                                                                                             |
| *version* >= 5.131.2600.1243                   | Windows XP with Service Pack 2 (SP2)Windows XP with Service Pack 1 (SP1) with hotfix KB329433<br/> Windows XP<br/> |
| 5.131.2600.0 <= *version* < 5.131.2600.1243 | Windows XP with SP1Windows XP<br/>                                                                                                                                        |



 

 

 
