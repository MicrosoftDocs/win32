---
description: The process of creating a certificate request involves collecting certain information from the requester.
ms.assetid: b03efa83-e255-4427-a796-63d5841664a9
title: Creating the Certificate Request
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Certificate Request

The process of creating a certificate request involves collecting certain information from the requester. Usually, this is done through some sort of user interface (UI), although the information could be taken directly from a database without the need for a UI. The level of information required is set by the policy of the [*certification authority*](../secgloss/c-gly.md) (CA).

An example of the required information might be as follows:

-   Common Name
-   Unit Name
-   Company Name
-   City
-   State
-   Country/Region

> [!Note]  
> The interface is designed to make a single request for each xenroll instance. A separate xenroll instance must be created to create each [*certificate request*](../secgloss/c-gly.md).

 

For information about how to use the Certificate Enrollment Control to request a certificate in specific programming languages, see the following topics:

-   [Request Sample in C++](request-sample-in-c-.md)
-   [Request Sample in VBScript](request-sample-in-vbscript.md)

 

 
