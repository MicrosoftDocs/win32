---
title: CPRPOBJ.CPP
description: In the example provider component, property object methods, in cprpobj.cpp, are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 88628b9b-12e6-4d64-9a21-b30f7392a5f2
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CPRPOBJ.CPP

In the example provider component, property object methods, in cprpobj.cpp, are listed in the following table.



| Method                                                 | Description                                                                                                                                    |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **CSampleDSProperty::CSampleDSProperty**               | Standard constructor.                                                                                                                          |
| **CSampleDSProperty::~CSampleDSProperty**              | Standard destructor.                                                                                                                           |
| **CSampleDSProperty::CreateProperty**                  | Create an ADS Property object, looking up the attribute definitions by calling **SampleDSGetPropertyDefinition**.                              |
| **CSampleDSProperty::CreateProperty**                  | Given the attribute definition, create a property object, setting the correspondence between supported ADS syntaxes and the provider syntaxes. |
| **CSampleDSProperty::AllocatePropertyObject**          | Create a property object and load its type data.                                                                                               |
| **CSampleDSProperty::QueryInterface**                  | Return the requested interface pointer, if available.                                                                                          |
| Standard [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master) methods.                 |                                                                                                                                                |
| Standard [**IADsProperty**](/windows/win32/Iads/nn-iads-iadsproperty?branch=master) methods. |                                                                                                                                                |
| **MapSyntaxIdtoADsSyntax**                             | Set the correspondence between the syntax ID and the ADS syntax.                                                                               |
| **MapSyntaxIdtoSampleDSSyntax**                        | Set the correspondence between the syntax ID and the provider syntax.                                                                          |



 

 

 




