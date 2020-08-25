---
title: Obtaining Accounting Properties
description: The accounting object is one of the objects in the Request Handlers collection.
ms.assetid: eb5c8606-d3f0-4c33-9035-7b7b1369cb0d
ms.tgt_platform: multiple
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



To access the accounting properties using C++, first obtain the request handlers collection. The [Retrieving a Collection](/windows/desktop/Nps/sdo-retrieving-a-collection) contains C++ code that demonstrates how to obtain a collection. The enumeration value for the request handlers collection is **PROPERTY\_IAS\_REQUESTHANDLERS\_COLLECTION**. (The values corresponding to the various NPS collections are enumerated by the [**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties) enumeration type.)

The request handlers collection contains an object named "Microsoft Accounting". Retrieve this object from the collection. The section [Retrieving an Object from a Collection](/windows/desktop/Nps/sdo-retrieving-an-object-from-a-collection) contains C++ code that demonstrates how to obtain an object from a collection.

Once you have the Microsoft Accounting object, obtain an [**ISdo**](/windows/desktop/api/sdoias/nn-sdoias-isdo) interface for the object using [**IUnknown::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)). The section [Retrieving a User SDO](/windows/desktop/Nps/sdo-retrieving-a-user-sdo) contains C++ code that demonstrates how obtain an **ISdo** interface for an object. You can then use the [**ISdo::GetProperty**](/windows/desktop/api/sdoias/nf-sdoias-isdo-getproperty) method to obtain property values for the Microsoft Accounting object.

## Related topics

<dl> <dt>

[Retrieving a Collection](/windows/desktop/Nps/sdo-retrieving-a-collection)
</dt> <dt>

[Retrieving an Object from a Collection](/windows/desktop/Nps/sdo-retrieving-an-object-from-a-collection)
</dt> <dt>

[Retrieving a User SDO](/windows/desktop/Nps/sdo-retrieving-a-user-sdo)
</dt> <dt>

[**ISdo**](/windows/desktop/api/sdoias/nn-sdoias-isdo)
</dt> <dt>

[**IUnknown::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q))
</dt> <dt>

[**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)
</dt> </dl>

 

 