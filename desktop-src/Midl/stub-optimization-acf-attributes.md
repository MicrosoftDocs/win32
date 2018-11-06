---
title: Stub Optimization ACF Attributes
description: These attributes enable you to optimize the size and speed of your stub code.
ms.assetid: 8c98b9ff-d91c-4a17-90c9-298f588e46c5
keywords:
- ACF MIDL , attributes, stub-optimization
ms.topic: article
ms.date: 05/31/2018
---

# Stub Optimization ACF Attributes

These attributes enable you to optimize the size and speed of your stub code.



| Attribute                                    | Usage                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**code**](code.md)[**nocode**](nocode.md) | Use the [**code**](code.md) and [**nocode**](nocode.md) attributes together to avoid generating stub code for unused functions. Apply the **nocode** attribute to the interface header, and apply the **code** attribute to those procedures that the client application will implement. Client stub code will be generated only for the selected procedures.                                                                |
| [**optimize**](optimize.md)                 | Lets you fine-tune the level of optimization that the MIDL compiler performs when generating stub code, by specifying that data is to be marshaled by either the mixed-mode or interpreted method. You can apply the [**optimize**](optimize.md) attribute to an interface or to selected functions within the interface. In either case, its use will override the command-line optimizations and any pre-existing defaults. |



 

 

 




