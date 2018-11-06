---
Description: The ShutdownEmbeddedUI function prototype defines a user-defined shutdown function exported by the embedded UI DLL that is defined in the MsiEmbeddedUI table.
ms.assetid: aee925f7-ea3e-4f5c-94dd-85985548d17b
title: ShutdownEmbeddedUI callback function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShutdownEmbeddedUI
api_type: 
- UserDefined
api_location: 
---

# ShutdownEmbeddedUI callback function

The *ShutdownEmbeddedUI* function prototype defines a user-defined shutdown function exported by the embedded UI DLL that is defined in the [MsiEmbeddedUI table](msiembeddedui-table.md). This function should be called at the end of the installation. After calling this function, the installer sends no additional messages to the embedded UI DLL and you can unload the DLL.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. Available beginning with Windows Installer 4.5.

## Syntax


```C++
DWORD CALLBACK ShutdownEmbeddedUI(void);
```



## Parameters

This callback function has no parameters.

## Return value

The return value from this function prototype is 0 in all cases. If a user-defined function returns a non-zero value, the installer writes a message to the log file.

## Remarks

For an example of the *ShutdownEmbeddedUI* function see [Using an Embedded UI](using-an-embedded-ui.md).

## Requirements



|                    |                                                                                                                                                                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.5 on Windows Vista, Windows XP, Windows Server 2003, and Windows Server 2008<br/> |
| Header<br/>  | <dl> <dt>Msi.h</dt> </dl>                                                                                                                          |



 

 




