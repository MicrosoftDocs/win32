---
Description: The InitializeEmbeddedUI function prototype defines a user-defined initialization function exported by the embedded user interface DLL that is defined in the MsiEmbeddedUI table.
ms.assetid: 1bc2fb8e-cbdc-4f2d-aca5-bbc59a07c93e
title: InitializeEmbeddedUI callback function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InitializeEmbeddedUI callback function

The *InitializeEmbeddedUI* function prototype defines a user-defined initialization function exported by the embedded user interface DLL that is defined in the [MsiEmbeddedUI table](msiembeddedui-table.md).

## Syntax


```C++
UINT CALLBACK InitializeEmbeddedUI(
  _In_    MSIHANDLE hInstall,
  _In_    LPCWSTR   wzResourcePath,
  _Inout_ LPDWORD   pdwInternalUILevel
);
```



## Parameters

<dl> <dt>

*hInstall* \[in\]
</dt> <dd>

A handle to the installer that performs the installation. This handle is valid only for the duration of the *InitializeEmbeddedUI* function.

</dd> <dt>

*wzResourcePath* \[in\]
</dt> <dd>

Pointer to a null-terminated string that contains the full path to the directory that contains all the files from the [MsiEmbeddedUI table](msiembeddedui-table.md). The user interface DLL can use this path to load resources stored in the Windows Installer package.

</dd> <dt>

*pdwInternalUILevel* \[in, out\]
</dt> <dd>

Pointer to a location that contains the internal UI level.

On entry to the *InitializeEmbeddedUI* function, this parameter receives a value that indicates the current UI level for the installation. The value is a combination of INSTALLUILEVEL flags that notifies the UI handler whether the installation is at the full, reduced, or basic [user interface levels](user-interface-levels.md).

The *InitializeEmbeddedUI* function should modify the value to one or more of the following flags. The installer resets the internal user interface level after the function returns.



| Value                                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INSTALLUILEVEL_FULL"></span><span id="installuilevel_full"></span><dl> <dt>**INSTALLUILEVEL\_FULL**</dt> </dl>                            | The embedded UI will handle some messages by using the internal Windows Installer UI set at the full [user interface level](user-interface-levels.md).<br/>                                                                                                                                                                                                                                                                                                            |
| <span id="INSTALLUILEVEL_REDUCED"></span><span id="installuilevel_reduced"></span><dl> <dt>**INSTALLUILEVEL\_REDUCED**</dt> </dl>                   | The embedded UI will handle some messages by using the internal Windows Installer UI set at the reduced [user interface level](user-interface-levels.md). <br/>                                                                                                                                                                                                                                                                                                        |
| <span id="INSTALLUILEVEL_BASIC"></span><span id="installuilevel_basic"></span><dl> <dt>**INSTALLUILEVEL\_BASIC**</dt> </dl>                         | The dialog boxes of the internal Windows Installer basic user interface are displayed together with dialog boxes of the embedded UI. The **INSTALLUILEVEL\_BASIC** value also disables the **Cancel** button on the basic internal UI dialog boxes.<br/>                                                                                                                                                                                                                |
| <span id="INSTALLUILEVEL_NONE"></span><span id="installuilevel_none"></span><dl> <dt>**INSTALLUILEVEL\_NONE**</dt> </dl>                            | The embedded UI will handle all messages. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="INSTALLUILEVEL_SOURCERESONLY"></span><span id="installuilevel_sourceresonly"></span><dl> <dt>**INSTALLUILEVEL\_SOURCERESONLY**</dt> </dl> | The embedded UI will handle all messages. If this value is combined with the **INSTALLUILEVEL\_NONE** value, the installer displays only the dialog boxes used for source resolution. No other dialog boxes are shown. This value has no effect if the UI level is not **INSTALLUILEVEL\_NONE**. It is used with an embedded user interface designed to handle all of the UI except for source resolution. In this case, the installer handles source resolution. <br/> |



 

</dd> </dl>

## Return value

The *InitializeEmbeddedUI* function returns the following values.



| Return code                                                                                            | Description                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_SUCCESS**</dt> </dl>          | The embedded UI DLL initialized successfully. Messages are sent to this DLL.<br/>                                                               |
| <dl> <dt>**INSTALLUILEVEL\_NONE**</dt> </dl>    | The embedded UI DLL did not initialize, and the installation continues with no user interface. <br/>                                            |
| <dl> <dt>**INSTALLUILEVEL\_BASIC**</dt> </dl>   | The embedded UI DLL did not initialize, and the installation continues using the internal basic user interface of the Windows Installer. <br/>  |
| <dl> <dt>**INSTALLUILEVEL\_REDUCED**</dt> </dl> | The embedded UI DLL did not initialize, and the installation continues using the internal reduced user interface of the Windows Installer.<br/> |
| <dl> <dt>**INSTALLUILEVEL\_FULL**</dt> </dl>    | The embedded UI DLL did not initialize, and the installation continues using the internal full user interface of the Windows Installer. <br/>   |
| <dl> <dt>**ERROR\_INSTALL\_FAILURE**</dt> </dl> | The embedded UI DLL did not initialize. The installation returns ERROR\_INSTALL\_FAILURE. <br/>                                                 |



 

## Remarks

The *InitializeEmbeddedUI* function should not increase the internal UI level to a level above the existing internal UI level. If the function attempts to do so, the installer caps the UI level at the existing level and the installer writes a message to the log file.

For an example of the *InitializeEmbeddedUI* function see [Using an Embedded UI](using-an-embedded-ui.md).

## Requirements



|                    |                                                                                                                                                                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.5 on Windows Vista, Windows XP, Windows Server 2003, and Windows Server 2008<br/> |
| Header<br/>  | <dl> <dt>Msi.h</dt> </dl>                                                                                                                          |



 

 




