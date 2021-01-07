---
description: The Microsoft.Windows.ActCtx object references manifests and provides a way for scripting engines to access side-by-side assemblies. The Microsoft.Windows.ActCtx object can be used to create an instance of a side-by-side assembly with COM components.
ms.assetid: 818e175e-2c58-4c44-87ce-4e97352fc3f3
title: Microsoft.Windows.ActCtx object
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Microsoft.Windows.ActCtx
api_type: 
- COM
api_location: 
---

# Microsoft.Windows.ActCtx object

The **Microsoft.Windows.ActCtx** object references manifests and provides a way for scripting engines to access side-by-side assemblies. The **Microsoft.Windows.ActCtx** object can be used to create an instance of a side-by-side assembly with COM components.

The **Microsoft.Windows.ActCtx** object comes as an assembly in Windows Server 2003. It can also be installed by applications that use the Windows Installer for setup and include it as a merge module in their installation package.

## Members

The **Microsoft.Windows.ActCtx** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Microsoft.Windows.ActCtx** object has these methods.



| Method                               | Description                                                                     |
|:-------------------------------------|:--------------------------------------------------------------------------------|
| [**CreateObject**](createobject.md) | Creates an object in the context of the current manifest.<br/>            |
| [**GetObject**](getobject.md)       | Gets an instance of an existing **Microsoft.Windows.ActCtx** object.<br/> |



 

### Properties

The **Microsoft.Windows.ActCtx** object has these properties.



| Property                                | Access type          | Description                                    |
|:----------------------------------------|:---------------------|:-----------------------------------------------|
| [**Manifest**](manifest.md)<br/> | Read-only<br/> | Gets the active activation context.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



 

 




