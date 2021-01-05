---
description: Manual Conversion from MTS
ms.assetid: 7ecc64a8-783d-4238-8b63-8e9c76382723
title: Manual Conversion from MTS
ms.topic: article
ms.date: 05/31/2018
---

# Manual Conversion from MTS

You might want to isolate conversion of MTS packages to COM+ applications so that it is outside the Windows setup process. The following procedure offers an alternate approach:

1.  Export the MTS packages using the MTS 2.0 Package Export feature (resulting in an MTS package file and a collection of other files).
2.  Delete the MTS packages and upgrade Windows, or perform a clean installation of Windows.
3.  Install the MTS package (.pak) files on a Windows 2000 or later system by using the Component Services administrative tool's Application Install wizard. You will also need to reset the application's "Run As" identity in the system registry under **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\APPID\\RunAs**.

> [!Note]  
> Only the automatic conversion procedure (through Windows setup or by running the MTSTOCOM utility) generates the MTSTOCOM log file. This file is not generated when following the manual conversion procedure.

 

## Related topics

<dl> <dt>

[Automatic Conversion from MTS](automatic-conversion-from-mts.md)
</dt> <dt>

[COM+ Conversion Results and Issues](com--conversion-results-and-issues.md)
</dt> <dt>

[MTS Administration Library](mts-administration-library.md)
</dt> </dl>

 

 



