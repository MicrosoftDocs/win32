---
Description: Basic Telephony services are a minimal subset of the Telephony specification.
ms.assetid: 997e405f-41fa-4aeb-8700-3f9f61430c88
title: Basic Telephony Services
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Basic Telephony Services

Basic Telephony services are a minimal subset of the Telephony specification. Because all service providers must support the functions of Basic Telephony services, applications that use only these functions will work with any TAPI service provider. The functionality contained in Basic Telephony roughly corresponds to the features of POTS.

Many programmers will use only the services that Basic Telephony provides. Others, such as those writing code for PBX phone systems, will need the functions of Supplementary Telephony.

For a list of the functions of Basic Telephony, see [TAPI Quick Function Reference](https://msdn.microsoft.com/en-us/library/ms737239(v=VS.85).aspx).

Because control of phone devices is not assumed to be offered by all service providers, phone-device services are considered to be optional. That is, they are not a part of Basic Telephony. For a list of phone-device services, see [Supplementary Telephony Services](supplementary-telephony-services.md); for more information on phone devices, see [TAPI Device Classes](https://msdn.microsoft.com/en-us/library/ms737225(v=VS.85).aspx).

 

 



