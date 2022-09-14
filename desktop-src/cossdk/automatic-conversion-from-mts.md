---
description: Automatic Conversion from MTS
ms.assetid: 0848639a-26ce-47ad-8384-8969a7c3bcde
title: Automatic Conversion from MTS
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Conversion from MTS

Automatic conversion occurs in two steps, as follows:

1.  During Windows setup. The conversion is handled by the Windows setup process through the MTSTOCOM utility.
    > [!Note]  
    > If step 1 fails, some or all of the MTS packages may actually have been converted but may be missing certain properties. In this case, use the Component Services administrative tool to verify all attributes. The MTS attributes will still be present on the computer (in the system registry at HKEY\_LOCAL\_MACHINE\\Microsoft\\Transaction Server) but will be accessible only through the regedit.exe utility.

     

2.  After the last reboot before the Windows logon dialog box is displayed. Step 2 handles those conversion actions that require network access (primarily role member creation).
    > [!Note]  
    > If step 2 fails (due to temporary network or domain controller failures), it is possible to rerun the MTSTOCOM conversion utility any number of times. To do this, at the command prompt or after selecting **Run** from the **Start** menu, type the following: **%windir%\\system32\\mtstocom.exe**.

     

## MTSTOCOM Log File

The MTSTOCOM utility generates a log file (Mtstocom.log) in the Windows directory. This log file keeps a record of the conversion from MTS packages to COM+ applications. If there were any errors during the conversion process, it is always a good idea to check the log file for further information. The log file catches common problems, such as invalid user or password.

## Related topics

<dl> <dt>

[COM+ Conversion Results and Issues](com--conversion-results-and-issues.md)
</dt> <dt>

[Manual Conversion from MTS](manual-conversion-from-mts.md)
</dt> <dt>

[MTS Administration Library](mts-administration-library.md)
</dt> </dl>

 

 



