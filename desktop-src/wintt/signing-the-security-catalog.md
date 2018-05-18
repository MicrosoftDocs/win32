---
title: Signing the Security Catalog
description: WTP executes only trusted troubleshooting packs that are signed using a security catalog. The security catalog must be code signed by a certificate that chains up to a trusted root authority on the computer.
ms.assetid: '258864d3-4ed2-41b6-8a8e-e02de461c245'
---

# Signing the Security Catalog

WTP executes only trusted troubleshooting packs that are signed using a security catalog. The security catalog must be code signed by a certificate that chains up to a trusted root authority on the computer. The security catalog contains the cryptographic hashes of all files included in the troubleshooting pack. When you run a troubleshooting pack, WTP gets the security catalog from the troubleshooting pack's folder and confirms that the files in the folder match those specified in the security catalog. If any of the files have been modified or if there are any additional unsigned files present, the pack is not run.

To sign the security catalog, use the [**Signtool.exe**](https://msdn.microsoft.com/library/windows/desktop/aa387764) tool included in the \\Bin folder of the Windows SDK. The following shows how to sign a catalog file assuming the code signing certificate is in the MY certificate store.

**signtool sign -a -n "***SubjectName***" -t** *URLPath\\***diagpackage.cat**

**signtool verify -pa -v** *Path\\***diagpackage.cat**

Although using the time stamp option (-t) is not required, you should use it so that when the certificate expires, the pack remains valid and WTP can still run it. The following shows a few of the available time stamp servers:

-   Verisign SHA1 : http://timestamp.verisign.com/scripts/timstamp.dll
-   Geotrust SHA1 : http://www.trustcenter.de/codesigning/timestamp
-   Comodo : http://timestamp.comodoca.com/authenticode

 

 




