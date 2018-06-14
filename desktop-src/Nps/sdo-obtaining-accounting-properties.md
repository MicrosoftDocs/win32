---
title: Obtaining Accounting Properties
description: The accounting object is one of the objects in the Request Handlers collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: eb5c8606-d3f0-4c33-9035-7b7b1369cb0d
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Accounting Properties

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

The accounting object is one of the objects in the Request Handlers collection. The enumeration value for the request handlers collection is **PROPERTY\_IAS\_REQUESTHANDLERS\_COLLECTION**. The name of the handler for the accounting object is "Microsoft Accounting".

The following Visual Basic code accesses the properties available from the accounting object handler.


```VB
Set sdoRequestHandler = sdoCollRequestHandlers.Item("Microsoft Accounting")
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_ACCOUNTING)
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_ACCOUNTING_INTERIM)
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_AUTHENTICATION)
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_FILE_DIRECTORY)
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_IAS1_FORMAT)
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_OPEN_NEW_FREQUENCY)
vtTemp = sdoRequestHandler.GetProperty(PROPERTY_ACCOUNTING_LOG_OPEN_NEW_SIZE)
```



To access the accounting properties using C++, first obtain the request handlers collection. The [Retrieving a Collection](https://msdn.microsoft.com/library/bb960708) contains C++ code that demonstrates how to obtain a collection. The enumeration value for the request handlers collection is **PROPERTY\_IAS\_REQUESTHANDLERS\_COLLECTION**. (The values corresponding to the various NPS collections are enumerated by the [**IASPROPERTIES**](https://msdn.microsoft.com/library/bb960636) enumeration type.)

The request handlers collection contains an object named "Microsoft Accounting". Retrieve this object from the collection. The section [Retrieving an Object from a Collection](https://msdn.microsoft.com/library/bb960707) contains C++ code that demonstrates how to obtain an object from a collection.

Once you have the Microsoft Accounting object, obtain an [**ISdo**](https://msdn.microsoft.com/library/bb960639) interface for the object using [**IUnknown::QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx). The section [Retrieving a User SDO](https://msdn.microsoft.com/library/bb960710) contains C++ code that demonstrates how obtain an **ISdo** interface for an object. You can then use the [**ISdo::GetProperty**](https://msdn.microsoft.com/library/bb960671) method to obtain property values for the Microsoft Accounting object.

## Related topics

<dl> <dt>

[Retrieving a Collection](https://msdn.microsoft.com/library/bb960708)
</dt> <dt>

[Retrieving an Object from a Collection](https://msdn.microsoft.com/library/bb960707)
</dt> <dt>

[Retrieving a User SDO](https://msdn.microsoft.com/library/bb960710)
</dt> <dt>

[**ISdo**](https://msdn.microsoft.com/library/bb960639)
</dt> <dt>

[**IUnknown::QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx)
</dt> <dt>

[**IASPROPERTIES**](https://msdn.microsoft.com/library/bb960636)
</dt> </dl>

 

 




