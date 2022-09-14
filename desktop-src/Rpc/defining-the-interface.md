---
title: Defining the Interface
description: An interface definition is a formal specification for how a client application and a server application communicate with each other.
ms.assetid: 709ca498-4da3-4e6f-bb12-333a407b74c2
keywords:
- Remote Procedure Call RPC , tasks, defining the interface
ms.topic: article
ms.date: 05/31/2018
---

# Defining the Interface

An interface definition is a formal specification for how a client application and a server application communicate with each other. The interface defines how the client and server recognize each other, the remote procedures that the client application can call, and the data types for those procedures' parameters and return values. It also specifies how the data is transmitted between client and server.

You define this interface in the Microsoft Interface Definition Language (MIDL) which consists of C-language definitions augmented with keywords, called attributes, which describe how the data is transmitted over the network.

The interface definition (IDL) file contains type definitions, attributes and function prototypes that describe how data is transmitted on the network. The application configuration (ACF) file contains attributes that configure your application for a particular operating environment without affecting its network characteristics.

 

 




