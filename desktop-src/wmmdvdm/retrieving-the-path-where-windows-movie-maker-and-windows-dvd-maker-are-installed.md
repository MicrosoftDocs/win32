---
title: Retrieving the Path Where Windows Movie Maker and Windows DVD Maker are Installed
description: Retrieving the Path Where Windows Movie Maker and Windows DVD Maker are Installed
ms.assetid: '2e59756c-3ac3-4ab0-a744-7aa7c83d3e86'
keywords: ["Windows Movie Maker,installation path", "Movie Maker,installation path", "Windows DVD Maker,installation path", "DVD Maker,installation path", "programming guide,Windows Movie Maker installation path", "programming guide,Windows DVD Maker installation path", "Windows Vista,Windows Movie Maker installation path", "Windows VIsta,Windows DVD Maker installation path"]
---

# Retrieving the Path Where Windows Movie Maker and Windows DVD Maker are Installed

You can retrieve the path where Windows Movie Maker and Windows DVD Maker are installed on Windows Vista by querying the **InprocServer32** registry entry under the following subkey:

**HKEY\_CLASSES\_ROOT\\CLSID\\{0f230444-825c-4d1f-b5fd-f315186a4ac0}\\InprocServer32**

The **InprocServer32** registry entry has the form shown in the following table.



| Name           | Type                | Data                                                              |
|----------------|---------------------|-------------------------------------------------------------------|
| (Default)      | **REG\_EXPAND\_SZ** | A string that specifies the path to the location of WMM2FILT.dll. |
| ThreadingModel | **REG\_SZ**         | A string value. (for example, "Both")                             |



 

A typical value for this key is "%ProgramFiles%\\Movie Maker\\WMM2FILT.dll", indicating that "%ProgramFiles%\\Movie Maker\\" is the path to the location where both Windows Movie Maker and Windows DVD Maker are installed.

## Related topics

<dl> <dt>

[**Getting Information from Windows Vista About Windows Movie Maker and Windows DVD Maker**](getting-information-from-windows-vista-about-windows-movie-maker-and-windows-dvd-maker.md)
</dt> </dl>

 

 




