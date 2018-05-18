---
Description: 'HPC sessions do not support all of the WCF features. The following identifies those WCF features that HPC supports.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '44f14c12-22af-4ae1-9122-9575b6c8dfa0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Supported Windows Communication Foundation Features
---

# Supported Windows Communication Foundation Features

HPC sessions do not support all of the WCF features. The following identifies those WCF features that HPC supports.

## Bindings

HPC supports only BasicHttpBinding and NetTcpBinding bindings.

## Message Exchange Patterns

HPC supports only request-reply patterns; HPC does not support duplex patterns.

## Service Contracts

HPC supports the Name and Namespace attributes; HPC does not support the CallbackContract and SessionMode attributes.

## Operation Contracts

HPC supports the following attributes:

-   Action
-   AsyncPattern
-   Name
-   ReplyAction

HPC does not support the following attributes:

-   IsInitiating
-   IsOneWay
-   IsTerminating

## Message Contracts

HPC supports the features that the following message contract samples demonstrate:

-   Default Message Contract
-   Unwrapped Messages
-   Xml Reader
-   Untyped Request/Reply

HPC does not support the features that the Setting the Use and Style Properties sample demonstrates.

For information about the message contract samples, see [Message Contract Samples](http://go.microsoft.com/fwlink/p/?linkid=153835).

## Service Concurrency Modes

HPC supports the Single, Multiple, and Reentrant concurrency modes.

## Service Instancing Modes

HPC supports the PerCall and Single instancing modes; HPC does not support the PerSession instancing mode.

 

 



