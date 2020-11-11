---
title: Code Details
description: This section lists the source code for the ADSI example provider component implementation. All source code references in this document are subject to change and are available in the example code directory included in the ADSI SDK.
ms.assetid: 207912e5-ac17-48c7-9536-981a8e92e8cf
ms.tgt_platform: multiple
keywords:
- Code Details ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Code Details

This section lists the source code for the ADSI example provider component implementation. All source code references in this document are subject to change and are available in the example code directory included in the ADSI SDK.

> [!Note]  
> The [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) methods **GetEx** and **PutEx** are not implemented in the ADSI example provider component. That is, code that implements Active Directory objects that inherit from **IADs** do not have **GetEx** and **PutEx** methods. This includes the schema class object that supports [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass), the property object that supports [**IADsProperty**](/windows/desktop/api/Iads/nn-iads-iadsproperty), the generic Active Directory object that supports **IADs**, and any container object that supports [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer). In addition, syntax objects are not present in the example provider component. However, the ADSI architecture requires the syntax objects to be included in the schema container object, just as are the schema class and property objects.

 

The following table lists source code files that are included in the provider example directory in the Active Directory Service Interfaces SDK.



| Source code file                 | Description                                                                                                                                                       |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cclsobj.cpp](cclsobj-cpp.md)   | Schema class object routines.                                                                                                                                     |
| [cdispmgr.cpp](cdispmgr-cpp.md) | Dispatch Manager implementation.                                                                                                                                  |
| [cenumns.cpp](cenumns-cpp.md)   | Namespace enumeration routines.                                                                                                                                   |
| [cenumsch.cpp](cenumsch-cpp.md) | Schema enumeration routines.                                                                                                                                      |
| [cenumobj.cpp](cenumobj-cpp.md) | Generic object enumeration routines.                                                                                                                              |
| [cenumvar.cpp](cenumvar-cpp.md) | Base implementation for xxxEnumVariant derived classes.                                                                                                           |
| [cgenobj.cpp](cgenobj-cpp.md)   | Generic object routines.                                                                                                                                          |
| [cnamcf.cpp](cnamcf-cpp.md)     | Namespace class factory routines.                                                                                                                                 |
| [cnamesp.cpp](cnamesp-cpp.md)   | Namespace object routines.                                                                                                                                        |
| [common.cpp](common-cpp.md)     | Code common to all provider objects.                                                                                                                              |
| [core.cpp](core-cpp.md)         | Implementations for 'core' properties shared by all Active Directory objects.                                                                                     |
| [cprops.cpp](cprops-cpp.md)     | Property cache features.                                                                                                                                          |
| [cprov.cpp](cprov-cpp.md)       | Top-level provider object routines.                                                                                                                               |
| [cprovcf.cpp](cprovcf-cpp.md)   | Top-level provider object class factory routines.                                                                                                                 |
| [cprpobj.cpp](cprpobj-cpp.md)   | Property object routines.                                                                                                                                         |
| [cschobj.cpp](cschobj-cpp.md)   | Schema object routines.                                                                                                                                           |
| [getobj.cpp](getobj-cpp.md)     | GetObject feature.                                                                                                                                                |
| [globals.cpp](globals-cpp.md)   | ADSI example provider component globals.                                                                                                                          |
| [guid.cpp](guid-cpp.md)         | Example provider component CLSIDs and LIBIDs.                                                                                                                     |
| [libmain.cpp](libmain-cpp.md)   | Libmain for adssmp.dll.                                                                                                                                           |
| [memory.cpp](memory-cpp.md)     | Example provider component memory management routines.                                                                                                            |
| [pack.cpp](pack-cpp.md)         | Example provider component pack/unpack data in VARIANTs.                                                                                                          |
| [parse.cpp](parse-cpp.md)       | Path parsing for example provider component namespace.                                                                                                            |
| [property.cpp](property-cpp.md) | Get and Put properties by name.                                                                                                                                   |
| [object.cpp](object-cpp.md)     | Example provider component object type list code for filtering.                                                                                                   |
| [regdsapi.cpp](regdsapi-cpp.md) | Example provider component registry directory service APIs.                                                                                                       |
| smpoper.cpp                      | Data conversion routines.                                                                                                                                         |
| [stdfact.cpp](stdfact-cpp.md)   | Standard [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) implementation.                                                                                                  |
| adssmp.inf                       | Example directory data store registry data. For more information, see [Installing the Example Provider Component](installing-the-example-provider-component.md). |



 

 

 