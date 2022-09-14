---
title: Data Type Attributes
description: You can apply these attributes to data types in a typedef statement to further define the usage or effect of the data type.
ms.assetid: 9a2e7c3d-f18f-4162-877c-5fc48a36b05d
keywords:
- IDL MIDL , attributes, data type
ms.topic: article
ms.date: 05/31/2018
---

# Data Type Attributes

You can apply these attributes to data types in a [**typedef**](typedef.md) statement to further define the usage or effect of the data type.



| Attribute                                 | Usage                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**context\_handle**](context-handle.md) | Identifies a binding handle that maintains state (context) information on a particular server between remote procedure calls from a particular client. Not valid for [**object**](object.md) interface functions.                                                                                                         |
| [**handle**](handle.md)                  | Specifies a custom handle type specific to the application.                                                                                                                                                                                                                                                                |
| [**ms\_union**](-ms-union.md)            | Controls the NDR alignment of nonencapsulated unions. Use on [**typedef**](typedef.md)s for backward compatibility with interfaces built with MIDL 1.0 or 2.0.                                                                                                                                                            |
| [**pipe**](pipe.md)                      | Allows transmission of an open-ended stream of typed data across a remote procedure call. An [**in**](in.md) pipe parameter allows the server to pull the data stream from the client during a remote procedure call. An [**out**](-out.md) pipe parameter allows the server to push the data stream back to the client. |
| [**transmit\_as**](transmit-as.md)       | Specifies how a data type will be transmitted over a network, used for custom marshaling.                                                                                                                                                                                                                                  |
| [**v1\_enum**](v1-enum.md)               | Directs that the specified enumerated type be transmitted as a 32-bit entity, rather than the 16-bit default.                                                                                                                                                                                                              |
| [**wire\_marshal**](wire-marshal.md)     | Similar to [**transmit\_as**](transmit-as.md) but you implement the routines to size, marshal, unmarshal, and free the data.                                                                                                                                                                                              |



 

 

 




