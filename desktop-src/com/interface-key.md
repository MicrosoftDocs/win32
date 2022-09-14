---
title: Interface Key
description: Registers new interfaces by associating an interface name with an interface ID (IID). There must be one IID subkey for each new interface.
ms.assetid: 2b2b7506-ac42-4bc4-bad5-17be57d6b4f5
keywords:
- Interface registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Interface Key

Registers new interfaces by associating an interface name with an interface ID (IID). There must be one IID subkey for each new interface.

## Registry Key

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes\\Interface**\\*{*IID*}*



| Registry value                               | Description                                                                                            |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**BaseInterface**](baseinterface.md)       | Identifies the interface from which the current interface is derived.                                  |
| [**NumMethods**](nummethods.md)             | Contains the number of methods in the associated interface, including methods from derived interfaces. |
| [**ProxyStubClsid**](proxystubclsid.md)     | Maps an IID to a CLSID in 16-bit proxy DLLs.                                                           |
| [**ProxyStubClsid32**](proxystubclsid32.md) | Maps an IID to a CLSID in 32-bit proxy DLLs.                                                           |



 

## Remarks

The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes** key corresponds to the **HKEY\_CLASSES\_ROOT** key, which was retained for compatibility with earlier versions of COM.

## Related topics

<dl> <dt>

[**Interface**](interface.md)
</dt> </dl>

 

 




