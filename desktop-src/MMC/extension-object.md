---
title: Extension Object object
description: The Extension object encapsulates a single MMC snap-in extension.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '100e73d3-b40b-4c44-99f0-b72c232b9632'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Extension Object object MMC", "Extension Object object MMC , described"]
topic_type:
- apiref
api_name:
- Extension Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# Extension Object object

The **Extension** object encapsulates a single MMC snap-in extension.

## Members

The **Extension Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Extension Object** object has these methods.



| Method                                                       | Description                                                                      |
|:-------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**Enable**](extension-enable.md)                           | Enables or disables this extension.<br/>                                   |
| [**EnableAllExtensions**](extension-enableallextensions.md) | Determines whether or not all extensions for the snap-in are enabled.<br/> |



 

### Properties

The **Extension Object** object has these properties.



| Property                                                | Access type          | Description                                                                                                            |
|:--------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**Extensions**](extension-extensions.md)<br/>   | Read-only<br/> | The [**Extensions**](extensions-collection.md) collection that represents the extensions for this snap-in.<br/> |
| [**Name**](extension-name.md)<br/>               | Read-only<br/> | The name of the extension.<br/>                                                                                  |
| [**SnapinCLSID**](extension-snapinclsid.md)<br/> | Read-only<br/> | The CLSID of the snap-in, in string form.<br/>                                                                   |
| [**Vendor**](extension-vendor.md)<br/>           | Read-only<br/> | The snap-in vendor.<br/>                                                                                         |
| [**Version**](extension-version.md)<br/>         | Read-only<br/> | The vendor-provided version of the snap-in, in string form.<br/>                                                 |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Extension is defined as AD4D6CA6-912F-409b-A26E-7FD234AEF542<br/>            |



 

 





