---
description: Provides access to the context of a CAPICOM Chain object. This context allows the CAPICOM certificate trust chain to be used in other derivations of CryptoAPI.
ms.assetid: ee258586-028e-486e-8129-07f43b6cc468
title: IChainContext interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IChainContext
api_type: 
- COM
api_location: 
- Capicom.dll
---

# IChainContext interface

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP.\]

The **IChainContext** interface provides access to the context of a CAPICOM [**Chain**](chain.md) object. This context allows the CAPICOM certificate trust chain to be used in other derivations of CryptoAPI.

## When to use

Use this interface when you need to use a CAPICOM [**Chain**](chain.md) object in another derivation of CryptoAPI.

## Members

The **IChainContext** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IChainContext** interface has these methods.



| Method                                           | Description                                                                                                                    |
|:-------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**FreeContext**](ichaincontext-freecontext.md) | Releases a PCCERT\_CHAIN\_CONTEXT acquired through the [**ChainContext**](ichaincontext-chaincontext.md) property.<br/> |



 

### Properties

The **IChainContext** interface has these properties.



| Property                                                      | Access type           | Description                                                               |
|:--------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------|
| [**ChainContext**](ichaincontext-chaincontext.md)<br/> | Read/write<br/> | Sets or retrieves the PCCERT\_CHAIN\_CONTEXT of a certificate.<br/> |



 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




