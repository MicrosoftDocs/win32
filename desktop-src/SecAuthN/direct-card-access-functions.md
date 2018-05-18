---
Description: 'By using the smart card subsystem, you can communicate with cards that may not conform to the ISO 7816 specifications.'
ms.assetid: 'ea6cfa5a-2abf-4b7f-b3f4-99655266f030'
title: Direct Card Access Functions
---

# Direct Card Access Functions

By using the [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) subsystem, you can communicate with cards that may not conform to the ISO 7816 specifications. To do this, the following functions let you control the attributes of the communications between the application and the card by giving you direct, low-level manipulation of the [*reader*](https://msdn.microsoft.com/library/windows/desktop/ms721604#-security-reader-gly).

To use these functions, you have to supply an identifier for the attribute in question. For valid attribute identifiers and values, refer to Table 3-1 in *Requirements for PC-Connected Interface Devices*.



| Topic                                    | Description                           |
|------------------------------------------|---------------------------------------|
| [**SCardControl**](scardcontrol.md)     | Provide direct control of the reader. |
| [**SCardGetAttrib**](scardgetattrib.md) | Get reader attributes.                |
| [**SCardSetAttrib**](scardsetattrib.md) | Set reader attribute.                 |



 

 

 



