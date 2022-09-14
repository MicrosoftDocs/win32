---
title: Installing and Registering Protocol Handlers (Legacy Windows Environment Features)
description: Installing protocol handlers involves copying the DLL(s) to an appropriate location in the Program Files directory and registering them.
ms.assetid: 3da32de1-2dc4-46d3-80d0-cc45a36f12f9
ms.topic: article
ms.date: 05/31/2018
---

# Installing and Registering Protocol Handlers (Legacy Windows Environment Features)

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

Installing **protocol handlers** involves copying the DLL(s) to an appropriate location in the Program Files directory and registering them.

This section contains the following topics:

-   [Installation Guidelines](#installation-guidelines)
-   [To Register Protocol Handlers](#to-register-protocol-handlers)
-   [To Register Shell Extensions](#to-register-shell-extensions)

## Installation Guidelines

Protocol handlers should implement self-registration for installation and should follow these guidelines:

-   The installer must use either EXE or MSI installer.
-   Release notes must be provided.
-   An **Add/Remove Programs** entry must be created for each add-in installed.
-   The installer must take over all registry settings for the particular file type or store that the current add-in understands.
-   If a previous add-in is being overwritten, the installer should notify the user.
-   If a newer add-in has overwritten the previous add-in, there should be the ability to restore the previous add-in's functionality and make it the default add-in for that file type again.

## To Register Protocol Handlers

You need to make fourteen entries in the registry to register the protocol handler component, where:

-   *Ver\_Ind\_ProgID* is the version independent ProgID of the protocol handler implementation
-   *Ver\_Dep\_ProgID* is the version dependent ProgID of the protocol handler implementation
-   *CLSID\_1* is the CLSID of the protocol handler implementation

1.  Register the version independent ProgID with the following keys and values:

    ```
    HKEY_CLASSES_ROOT\<Ver_Ind_ProgID>
       (Default) = <Protocol Handler Class Description>
    ```

    ```
    HKEY_CLASSES_ROOT\<Ver_Ind_ProgID>/CLSID
       (Default) = {CLSID_1}
    ```

    ```
    HKEY_CLASSES_ROOT\<Ver_Ind_ProgID>/CurVer
       (Default) = <Ver_Dep_ProgID>
    ```

2.  Register the version dependent ProgID with the following keys and values:

    ```
    HKEY_CLASSES_ROOT\<Ver_Dep_ProgID>
       (Default) = <Protocol Handler Class Description>
    ```

    ```
    HKEY_CLASSES_ROOT\<Ver_Dep_ProgID>/CLSID
       (Default) = {CLSID_1}
    ```

3.  Register the protocol handler's CLSID with the following keys and values:

    ```
    HKEY_CLASSES_ROOT\{CLSID_1}
       (Default) = <Protocol Handler Class Description>
    ```

    ```
    HKEY_CLASSES_ROOT\{CLSID_1}/InprocServer32
       (Default) = <DLL Install Path>
       Threading Model = Both
    ```

    ```
    HKEY_CLASSES_ROOT\{CLSID_1}/ProgID
       (Default) = <Ver_Dep_ProgID>
    ```

    ```
    HKEY_CLASSES_ROOT\{CLSID_1}/ShellFolder
       Attributes = dword:a0180000
    ```

    ```
    HKEY_CLASSES_ROOT\{CLSID_1}/TypeLib
       (Default) = {LIBID of PH Component}
    ```

    ```
    HKEY_CLASSES_ROOT\{CLSID_1}/VersionIndependentProgID
       (Default) = <Ver_Ind_ProgID>"
    ```

4.  Register the protocol handler with Windows Desktop Search:

    ```
    HKEY_LOCAL_MACHINE\Software\Microsoft\RSSearch\ProtocolHandlers
       Protocol Name = <Ver_Dep_ProgID>
    ```

    ```
    HKEY_CURRENT_USER\Software\Microsoft\RSSearch\ProtocolHandlers
       Protocol Name = <Ver_Dep_ProgID>
    ```

    ```
    HKEY_CURRENT_USER\Software\Microsoft\Windows Desktop Search\DS\Index\ProtocolHandlers\<Protocol Name>
       HasRequirements = dword:00000000
       HasStartPage = dword:00000000
    ```

## To Register Shell Extensions

You need to make two entries in the registry to register the protocol handler's Shell extension.

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Desktop\NameSpace\{CLSID of PH Implementation}
   (Default) = <Shell Implementation Description>
```

```
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Extensions\Approved
   {CLSID of PH Implementation} = <Shell Implementation Description>
```

 

 




