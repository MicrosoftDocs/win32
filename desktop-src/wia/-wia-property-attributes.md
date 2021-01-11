---
description: All item objects have properties.
ms.assetid: 00e04790-e319-41b3-b88f-8064912b91b1
title: Property Attributes (WIA)
ms.topic: article
ms.date: 05/31/2018
---

# Property Attributes (WIA)

All item objects have properties. The properties have attributes. For instance, property attributes indicate whether a property is read from, written to, or deleted. They also indicate the valid property values. The following constants are valid property attributes: 

| Property Attribute        | Meaning                                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------------------|
| WIA\_PROP\_CACHEABLE      | The device can cache the property's value.                                                               |
| WIA\_PROP\_FLAG           | The property has a list of legal flag values. Flag values are combined using a bitwise **OR** operation. |
| WIA\_PROP\_LIST           | The property has a list of legal values.                                                                 |
| WIA\_PROP\_NONE           | The property does not have any valid values associated with it.                                          |
| WIA\_PROP\_RANGE          | The property has a range of valid values.                                                                |
| WIA\_PROP\_READ           | The application can read the property's value.                                                           |
| WIA\_PROP\_RW             | The application can read and write the property's value.                                                 |
| WIA\_PROP\_SYNC\_REQUIRED | Do not use.                                                                                              |
| WIA\_PROP\_WRITE          | The application can write the property's value.                                                          |



 

 

 



