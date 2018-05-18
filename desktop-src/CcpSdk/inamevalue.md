---
Description: 'Represents a name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4504ef48-f181-4ae5-a3fe-080a80d96d36'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INameValue interface
---

# INameValue interface

Represents a name/value pair.

To get this interface, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection-getenumerator.md) method to get an [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface pointer. Use the **IEnumVARIANT::Next** method to enumerate the items of the collection. Each item in the collection is a variant whose type is VT\_DISPATCH. Query the **pdispVal** member of the variant to get the **INameValue** interface.

## Members

The **INameValue** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INameValue** also has these types of members:

-   [Methods](#methods)

### Methods

The **INameValue** interface has these methods.



| Method                                     | Description                     |
|:-------------------------------------------|:--------------------------------|
| [**get\_Name**](inamevalue-get-name.md)   | Retrieves the name.<br/>  |
| [**get\_Value**](inamevalue-get-value.md) | Retrieves the value.<br/> |



 

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INameValueCollection**](inamevaluecollection.md)
</dt> <dt>

[CCP Interfaces](interfaces.md)
</dt> </dl>

 

 




