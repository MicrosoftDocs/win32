---
description: You can write policy modules in the C, C++, or Visual Basic programming language.
ms.assetid: 37a93c67-02f2-4c4e-a000-2bb98e0ca948
title: Writing Custom Modules
ms.topic: article
ms.date: 05/31/2018
---

# Writing Custom Modules

You can write policy modules in the C, C++, or Visual Basic programming language. The required Microsoft compiler is available in Visual C++ version 5.0 or later or in Visual Basic version 5.0 or later. An enterprise [*certification authority*](../secgloss/c-gly.md) (CA) should use only the Microsoft-provided enterprise policy module.

You must implement [**ICertPolicy**](/windows/desktop/api/Certpol/nn-certpol-icertpolicy) when writing a custom policy module. Additionally, you must implement [**ICertManageModule**](/windows/desktop/api/Certmod/nn-certmod-icertmanagemodule) when writing a custom policy module.

Policy modules can call methods from [**ICertServerPolicy**](/windows/desktop/api/Certif/nn-certif-icertserverpolicy) to assist in the processing of a [*certificate request*](../secgloss/c-gly.md); **ICertServerPolicy** allows properties and certificate extensions to be set and retrieved.

For more information, see the following topics.



| Topic                                                                      | Description                             |
|----------------------------------------------------------------------------|-----------------------------------------|
| [Setting Certificate Properties](setting-certificate-properties.md)       | Setting the properties of a certificate |
| [Writing Custom Exit Modules](writing-custom-exit-modules.md)             | Writing custom exit modules             |
| [Writing Custom Extension Handlers](writing-custom-extension-handlers.md) | Writing custom extension handlers       |



 

 

 
