---
Description: 'Used to limit the results returned by a function instance collection query or by a function instance query.'
ms.assetid: '245aa40c-b17d-4157-bd20-f19c7461eed3'
title: Constraints
---

# Constraints

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Constraints are used to limit the results returned by a function instance collection query or by a function instance query.

Constraints are applied to a query by calling [**IFunctionInstanceCollectionQuery::AddQueryConstraint**](ifunctioninstancecollectionquery-addqueryconstraint.md). Generally, this method applies to collection queries. There is no similar method on the [**IFunctionInstanceQuery**](ifunctioninstancequery.md) interface, but you can constrain function instance queries using the [**IFunctionInstanceCollectionQuery**](ifunctioninstancecollectionquery.md) interface. To constrain a function instance query, create a **IFunctionInstanceCollectionQuery** object, apply the FD\_QUERYCONSTRAINT\_PROVIDERINSTANCEID constraint with the value set to the provider instance identifier returned by [**IFunctionInstance::GetProviderInstanceID**](ifunctioninstance-getproviderinstanceid-method.md) for the function instance you want to query, and then apply other query constraints as required.

A list of constraints defined in the SDK appears in the topic [Constraint Definitions](constraint-definitions.md). Not all constraints are supported by all Function Discovery providers. For more information about the query constraints supported by a provider, see [Built-in Providers](built-in-providers.md). If a provider does not understand a constraint, the provider will ignore it. For example, a SSDP\_CONSTRAINTVALUE\_TYPE\_DEV\_MDASRVR will be ignored by a query to PnP.

## Related topics

<dl> <dt>

[Constraint Definitions](constraint-definitions.md)
</dt> </dl>

 

 



