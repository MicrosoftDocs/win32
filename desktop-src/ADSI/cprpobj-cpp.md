---
title: CPRPOBJ.CPP
description: In the example provider component, property object methods, in cprpobj.cpp, are listed in the following table.
ms.assetid: 88628b9b-12e6-4d64-9a21-b30f7392a5f2
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
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
| Standard [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) methods.                 |                                                                                                                                                |
| Standard [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty) methods. |                                                                                                                                                |
| **MapSyntaxIdtoADsSyntax**                             | Set the correspondence between the syntax ID and the ADS syntax.                                                                               |
| **MapSyntaxIdtoSampleDSSyntax**                        | Set the correspondence between the syntax ID and the provider syntax.                                                                          |



 

 

 




