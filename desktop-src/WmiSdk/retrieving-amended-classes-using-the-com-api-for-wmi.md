---
Description: 'If you are using the COM API for WMI to retrieve or store localized class information, specify the locale in the strLocale parameter to the IWbemLocator::ConnectServer interface.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '940a7bd9-c2ea-4deb-b5d8-207a0ce7a616'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Retrieving Amended Classes Using the COM API for WMI
---

# Retrieving Amended Classes Using the COM API for WMI

If you are using the COM API for WMI to retrieve or store localized class information, specify the locale in the *strLocale* parameter to the [**IWbemLocator::ConnectServer**](iwbemlocator-connectserver.md) interface. When reading or writing amended classes, indicate that you want to use localized class definitions by specifying WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS as a flag for the *iFlags* parameter.

The following table lists the synchronous and asynchronous versions of the methods that use the WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS flag.



| Synchronous Method                                                            | Asynchronous Method                                                                     |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**IWbemServices::CreateClassEnum**](iwbemservices-createclassenum.md)       | [**IWbemServices::CreateClassEnumAsync**](iwbemservices-createclassenumasync.md)       |
| [**IWbemServices::CreateInstanceEnum**](iwbemservices-createinstanceenum.md) | [**IWbemServices::CreateInstanceEnumAsync**](iwbemservices-createinstanceenumasync.md) |
| [**IWbemServices::ExecQuery**](iwbemservices-execquery.md)                   | [**IWbemServices::ExecQueryAsync**](iwbemservices-execqueryasync.md)                   |
| [**IWbemServices::GetObject**](iwbemservices-getobject.md)                   | [**IWbemServices::GetObjectAsync**](iwbemservices-getobjectasync.md)                   |
| [**IWbemServices::PutClass**](iwbemservices-putclass.md)                     | [**IWbemServices::PutClassAsync**](iwbemservices-putclassasync.md)                     |
| [**IWbemServices::PutInstance**](iwbemservices-putinstance.md)               | [**IWbemServices::PutInstanceAsync**](iwbemservices-putinstanceasync.md)               |



 

 

 



