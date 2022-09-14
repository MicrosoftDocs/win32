---
description: Defines a method that determines whether the Shell will be allowed to move, copy, delete, or rename a folder in a cloud provider's sync root. 
title: IStorageProviderCopyHook interface
ms.topic: reference
ms.date: 11/11/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStorageProviderCopyHook
api_type: 
- COM
api_location: 
- shobjidl.h
---

# IStorageProviderCopyHook interface

Exposes a method that determines whether the Shell will be allowed to move, copy, delete, or rename a folder in a cloud provider's sync root.

## Members

The **IStorageProviderCopyHook** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IStorageProviderCopyHook** also has these types of members:

- [Methods](#methods)

### Methods

The **IStorageProviderCopyHook** interface has these methods.



| Method                                           | Description                                                                                               |
|:-------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**CopyCallback**](nf-shobjidl-istorageprovidercopyhook-copycallback.md)               |  Determines whether the Shell will be allowed to move, copy, delete, or rename a folder in a cloud provider's sync root.                                                           |


## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 Insider Preview Build 19624                                                |
| Header<br/>                   | shobjidl.h   |
