---
title: Data Representation
description: Computing environments can differ significantly, as can network architectures.
ms.assetid: 34ba76ae-644d-4168-886f-0909a65f1abd
keywords:
- Remote Procedure Call RPC , described, data representation
ms.topic: article
ms.date: 05/31/2018
---

# Data Representation

Computing environments can differ significantly, as can network architectures. To accommodate these differences, MIDL enables you to modify the way you represent data. You can sometimes simplify development by converting data into a format that your application can more easily handle. You can alter your application's data format so that it can be more efficiently transmitted over the network.

The **\[**[**transmit\_as**](/windows/desktop/Midl/transmit-as)**\]** and **\[**[**represent\_as**](/windows/desktop/Midl/represent-as)**\]** attributes instruct the compiler to associate a transmissible type that the stub passes between client and server, with a user type that the client and server applications use. You must supply the routines that carry out the conversion between the user type and the transmissible type, and the routines to release the memory that was used to hold the converted data. Using the **\[transmit\_as\]** IDL attribute or the **\[represent\_as\]** ACF attribute instructs the stub to call these conversion routines before and after transmission. The **\[**[**transmit\_as**](/windows/desktop/Midl/transmit-as)**\]** attribute lets you convert one data type to another data type for transmission over the network. The **\[**[**represent\_as**](/windows/desktop/Midl/represent-as)**\]** attribute lets you control the way data from the network is presented to the application.

The **\[**[**wire\_marshal**](/windows/desktop/Midl/wire-marshal)**\]** and **\[**[**user\_marshal**](/windows/desktop/Midl/user-marshal)**\]** attributes are Microsoft extensions to the OSF-DCE IDL. Their syntax and functionality are similar to that of the DCE-specified **\[transmit\_as\]** and **\[represent\_as\]** attributes, respectively. The difference is that, instead of converting the data from one type to another, you marshal the data directly. To do this, you must supply the external routines for sizing the data buffer on the client and server sides, marshaling and unmarshaling the data on the client and server sides, and freeing the data on the server side. The MIDL compiler generates format codes that instruct the NDR engine to call these external routines when needed.

The **\[wire\_marshal\]** and **\[user\_marshal\]** attributes make it possible to marshal data types that otherwise could not be transmitted across process boundaries. Also, because there is less overhead associated with the type conversion, **\[wire\_marshal\]** and **\[user\_marshal\]** provide improved performance at run time, when compared to **\[transmit\_as\]** and **\[represent\_as\]**. The **\[wire\_marshal\]** and **\[user\_marshal\]** attributes are mutually exclusive with respect to each other and with respect to the **\[transmit\_as\]** and **\[represent\_as\]** attributes for a given type.

It is important to note that the implementation of the **\[wire\_marshal\]** and **\[user\_marshal\]** attributes must follow the marshalling rules dictated by OSF-DCE specification. For that reason, the use of these attributes is not recommended if you are not familiar with the wire protocol. More information regarding the NDR Syntax Transfer can be found at [www.opengroup.org](https://pubs.opengroup.org/onlinepubs/9629399/chap14.htm).

This section provides a brief overview of these for MIDL attributes, in the following topics:

-   [**The transmit\_as and represent\_as Attributes**](the-transmit-as-and-represent-as-attributes.md)
-   [**The wire\_marshal and user\_marshal Attributes**](the-wire-marshal-and-user-marshal-attributes.md)

 

 