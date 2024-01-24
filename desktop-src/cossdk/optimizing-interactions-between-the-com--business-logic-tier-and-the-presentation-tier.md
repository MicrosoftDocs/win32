---
description: Typically, the latency between tiers of a distributed application differs greatly.
ms.assetid: 4780a9fd-5940-4b10-a596-22214b17c033
title: Optimizing Interactions Between the COM+ Business Logic Tier and the Presentation Tier
ms.topic: article
ms.date: 05/31/2018
---

# Optimizing Interactions Between the COM+ Business Logic Tier and the Presentation Tier

Typically, the latency between tiers of a distributed application differs greatly. Calls between the presentation tier and business logic tier are often an order of magnitude slower than calls between the business tier and data tier. As a result, held state is more costly when calling into the business logic tier.

The following topics discuss ways to pass data between the presentation and business logic tiers:

-   [Passing Parameters](#passing-parameters)
-   [Data Passing Options](#data-passing-options)
-   [Using a Factory Pattern to Pass Data](#using-a-factory-pattern-to-pass-data)
-   [Related topics](#related-topics)

## Passing Parameters

For a given set of information to be passed between the presentation tier and the business logic tier, you may have a single row, multiple rows, or a combination of a single row (such as a header) and multiple detail rows of data. The most efficient way to pass this information between tiers is by a single method call. This single call would manage the entire information set to be passed. This is necessary unless you choose to control the transaction from the presentation tier (and make all transaction treatment in the presentation tier identical in function). Microsoft does not recommend conducting transactions from the presentation tier because calls between this tier and the business logic tier are usually the slowest of any calls in a multi-tier application.

One way to create such a method is to pass single rows of information as parameters and pass multiple rows as ADO recordsets. Recordsets are the core of Microsoft's ADO data access methodology, and using ADO recordsets allows you to pass all the information related to a single transaction in one step.

## Data Passing Options

There are other options to consider when passing data. These include using a list of parameters and ADO recordsets (as discussed above), just ADO recordsets, XML encoded strings, or arrays of structures. This section discusses each of these options.

The following table shows areas where extra care needs to be taken when using any of the four different argument-passing possibilities. An "X" represents areas where trade-offs need to be understood and weighed against the needs of each project. Try not to make argument-passing decisions on a per-component basis. The benefits of a consistent programming model throughout a project far outweigh any advantage of optimizing on a per-method or per-component basis in all but the most extreme circumstances. The columns are described in the list that follows the table.



|     &nbsp;                  | Concurrency  | WAN          | Deployment   | Complexity   |
|-----------------------|--------------|--------------|--------------|--------------|
| Entry | Value |
| Recordsets<br/> |              | X<br/> | X<br/> | X<br/> |
| XML<br/>        | X<br/> |              | X<br/> | X<br/> |
| Arrays<br/>     | X<br/> |              | X<br/> | X<br/> |



 

The four columns define areas to watch out for when using that option to pass parameters.

-   **The Concurrency column** represents the need to code or provide a mechanism that manages locking conditions on update operations. Since methods that perform saves can represent updates, concurrency problems can arise. Two types of locking are prevalent optimistic and pessimistic. Pessimistic locks prevent a user from getting data for update while another user has the potential for performing an update. Optimistic locking supports a great many more users by trading against the likelihood that any two users would be updating the same document at the same time. Optimistic locking calls for checking to see that the data that is stored matches the data at the point when a copy of the data was accessed for modification. ADO recordsets provide automatic support for optimistic locking. Update scenarios involving single row parameter lists do not provide sufficient support for concurrency checking. XML suffers from this same problem, in that no locking awareness is present in XML data.
-   **The WAN column** represents conditions where there may be transmission contention on a wide area network (WAN ). When the WAN does not have sufficient capacity to manage all of the data being moved at any one time, application users experience response time delays. To support optimistic concurrency, disconnected ADO recordsets pass two copies of the data from the server to the client. The second copy is used by the client to determine the smallest update rowset to pass back when a change is being committed. While this cuts down on traffic from the presentation tier to the data, the extra load of the second copy can be significant. Using recordsets as the sole means of passing all information therefore causes twice as much data to be passed between tiers as is required, except when the update rowset is being passed back to the data tier from a presentation tier.
-   **The Deployment column** represents issues associated with data passing when special technology is required on both the caller and component side of the network. For example, using ADO recordsets requires ADO components to be present on both client and server. XML parsers must be present on both sides as well, to avoid having to code parsers into your applications.
-   **The Complexity column** is indicated for all four choices, and is a matter of preference or prior programming model experience that may be already established in your development organization. Some people find parameter passing to be cumbersome and feel it adds too much complexity to the programming problem. Keeping track of which parameter you are handling, and getting them all visible in one editing window, can create a logistical complexity that some developers find unmanageable.

The parameter-passing method also can have trade-offs, such as the following:

-   Parameters can involve managing multiple arguments and argument types as well as having to decide when it is appropriate to make a recordset a parameter.
-   ADO recordsets can cut hierarchical relationships in method parameters down to one or two arguments. This simplifies the programming model dramatically and supports adding columns at a later time, but it also hides the information hierarchy. Stuffing information into an ADO recordset and later extracting it involves knowing the names of each column or knowing the column order. This situation can add complexity for other component or application developers on the project.
-   XML is a different spin on the hidden hierarchy complication mentioned above. The programmer needs to understand the use of an XML parser to gain access to the information and often must know the names of each item in the data set before the data set can be found.
-   Arrays of structures introduce the need for a common understanding of the information being passed on the part of both caller and component. This need for a map that is shared between two system elements can lead to difficulties when dealing with different versions of components. While the method signature might not change, changes to the expected information can render calling programs incompatible.

Because the complexity issues associated with all four parameter-passing methods are so similar, it is debatable that there is a significant simplification opportunity associated with any one selection.

## Using a Factory Pattern to Pass Data

One important design point is ease of use. The moment you decided to use ADO recordsets to pass a structured set of details back to the presentation tier, you introduced a complexity problem. Presentation tier programmers need to understand the structure of those recordsets. A greater complexity issue can arise when you require multiple details for a set of data to be passed in a recordset. To simplify matters, you should consider creating a recordset factory method whenever you intend to require data to be passed in structured ADO recordsets.

The recordset factory should return an empty but writable disconnected recordset to the caller. This recordset should have the proper fields (names and data types) already configured so that the calling client does not need to know how to manufacture the recordset. This approach is often referred to as the *factory pattern* and is a common solution pattern that solves the need to create an object of a given complexity without having to know the nuances of creating it.

Simple design choices such as choosing the same parameter name for the same piece of data across every method where that information is passed makes it easy to look at a method and know what is expected. Making sure that the order in which like arguments are passed is consistent across an entire family of methods provides a comfort point that enforces a consistent model.

## Related topics

<dl> <dt>

[Optimizing Interactions Between the COM+ Business Logic Tier and the Data Tier](optimizing-interactions-between-the-com--business-logic-tier-and-the-data-tier.md)
</dt> </dl>

 

 




