---
title: Implementing and Activating a Handler with Extra Data Supplied by Server
description: Implementing and Activating a Handler with Extra Data Supplied by Server
ms.assetid: 5bbf81bd-430d-4008-b1cc-9ea91bb3b1e7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing and Activating a Handler with Extra Data Supplied by Server

If the server wants to include some extra data in the packet for the handler to use, the server must implement both the [**IMarshal**](/windows/win32/objidlbase/nn-objidl-imarshal?branch=master) and the [**IStdMarshalInfo**](/windows/win32/objidlbase/nn-objidl-istdmarshalinfo?branch=master) interfaces. The server must aggregate the standard marshaler and must delegate the first part of the marshaling to the aggregated standard marshaler, including [**IMarshal::GetUnmarshalClass**](/windows/win32/ObjIdl/nf-objidl-imarshal-getunmarshalclass?branch=master), and must add its own data size to the size returned by the standard marshaler's [**IMarshal::GetMarshalSizeMax**](/windows/win32/ObjIdl/nf-objidl-imarshal-getmarshalsizemax?branch=master). The standard marshaler calls [**IStdMarshalInfo::GetClassForHandler**](/windows/win32/objidlbase/nf-objidl-istdmarshalinfo-getclassforhandler?branch=master) to get the CLSID of the handler to be created. After the standard marshaler has done its marshaling, the server then writes its own extra data into the stream. The resulting structures, with extra data in the stream, are shown in the following illustration:

![](images/4cff306b-bb82-4c05-8e64-7ca73731f265.png)

## Server-Side Structures with Extra Data in Stream

This allows the call from COM to [**CoUnmarshalInterface**](/windows/win32/combaseapi/nf-combaseapi-counmarshalinterface?branch=master) on the client side the ability to skip over any unread data and leave the stream in the appropriate position following all the marshaled interface data if the handler cannot be created.

## Client-Side Structures with Extra Data in Stream

As in the case where there is no extra server data in the stream, the client-side COM call to [**CoUnmarshalInterface**](/windows/win32/combaseapi/nf-combaseapi-counmarshalinterface?branch=master) will create the identity and handler. The handler must implement [**IMarshal**](/windows/win32/objidlbase/nn-objidl-imarshal?branch=master) and must delegate the **IMarshal** calls to the aggregated standard marshaler first and then marshal or unmarshal any extra data that the server provided. The handler's [**UnmarshalInterface**](/windows/win32/objidlbase/nf-objidl-imarshal-unmarshalinterface?branch=master) will be called for every unmarshal, regardless of whether it has unmarshaled the interface before or not. In this case, the server does not call [**CoGetStdMarshalEx**](/windows/win32/combaseapi/nf-combaseapi-cogetstdmarshalex?branch=master) but the handler must. The resulting client-side structure is shown in the following illustration.

![](images/053411c7-9d54-4ae5-bcb6-778454b1d86f.png)

## Related topics

<dl> <dt>

[The Lightweight Client-Side Handler](the-lightweight-client-side-handler.md)
</dt> </dl>

 

 




