---
Description: Cert2SPC
ms.assetid: d05df388-c19d-47a5-9ede-11cf06c29fc8
title: Cert2SPC
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cert2SPC

The Cert2SPC tool creates a test [*Software Publisher Certificate*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SPC) by using existing [*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) [*certificates*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb). Cert2SPC can wrap multiple X.509 certificates into a [*PKCS \#7*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) signed-data object. The tool is installed in the \\Bin folder of the Microsoft Windows Software Development Kit (SDK) installation path.

Cert2SPC is available as part of the Windows SDK, which you can download from <http://go.microsoft.com/fwlink/p/?linkid=84091>.

> [!Note]This tool is for test purposes only. A valid SPC is obtained from a [*certification authority*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb).
>
> **Cert2SPC** *Cert1.cer Cert2.cer* … *Output.spc*

 



|                         |                                                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| *Cert1.cer Cert2.cer* … | Names of the X.509 certificates to include in the SPC. Each certificate name ends with the .cer extension.                         |
| *Output.spc*            | Name of the PKCS \#7 object that contains the X.509 certificates to be created. The output file name ends with the .spc extension. |



 

 

 



