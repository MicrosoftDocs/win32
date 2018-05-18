---
Description: 'Represents a name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c25c268c-0266-4f6a-b1cf-5fdead1880e2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: INameValue interface
---

# INameValue interface

Represents a name/value pair.

To get this interface, call the [**INameValueCollection::GetEnumerator**](inamevaluecollection2-getenumerator.md) method to get an [**IEnumVARIANT**](139e3c93-faef-4003-9079-e0e94494db3e) interface pointer. Use the **IEnumVARIANT::Next** method to enumerate the items of the collection. Each item in the collection is a variant of type VT\_DISPATCH. Query the **pdispVal** member of the variant to get the **INameValue** interface.

## Members

The **INameValue** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INameValue** also has these types of members:

-   [Properties](#properties)

### Properties

The **INameValue** interface has these properties.



| Property                                      | Access type          | Description                     |
|:----------------------------------------------|:---------------------|:--------------------------------|
| [**Name**](inamevalue2-name.md)<br/>   | Read-only<br/> | Retrieves the name.<br/>  |
| [**Value**](inamevalue2-value.md)<br/> | Read-only<br/> | Retrieves the value.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Interfaces](hpc-interfaces.md)
</dt> <dt>

[**INameValueCollection**](inamevaluecollection2.md)
</dt> </dl>

 

 




