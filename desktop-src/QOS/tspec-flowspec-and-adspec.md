---
title: Tspec, FlowSpec, and Adspec
description: RSVP transmits request information for a QOS-enabled connection with RSVP PATH and RESV messages.
ms.assetid: '67fbdebf-3dd9-4a05-b9a6-8a1e8f965aab'
keywords: ["Tspec QOS", "FlowSpec QOS", "Adspec QOS"]
---

# Tspec, FlowSpec, and Adspec

RSVP transmits request information for a QOS-enabled connection with RSVP PATH and RESV messages. Within such PATH and RESV messages, certain values are used to represent traffic and requested QOS parameters that enable a sender and receiver to establish service quality parameters for a given flow:

-   The sender Tspec (T representing traffic) specifies parameters available for the flow. Both senders and receivers use Tspec (SenderTspec and ReceiverTspec, respectively).
-   The [**FLOWSPEC**](flowspec.md) specifies requested QOS parameters, and is used by the receiver in RESV messages.
-   The Adspec (ad for advertisement) enables QOS-enabled network devices in the path between sender and receiver to advertise their service capabilities, resource availability, and transmission characteristics.

## RSVP Tspec

Both senders and receivers use Tspec, as part of SenderTspec and Receiverflowspec, respectively.

Sender provides the Tspec to describe the traffic it will originate, and the receiver provides the flowspec to describe the reservation it needs.

The RSVP Tspec derives its parameters from the **SendingFlowspec** member of a [**QOS**](qos.md) structure (SendingFlowspec is of type [**FLOWSPEC**](flowspec.md)).

The following table explains how members in **SendingFlowspec** map to Tspec parameters.



| SendingFlowspec Parameter | Tspec              |
|---------------------------|--------------------|
| TokenRate                 | TokenBucketRate    |
| TokenBucketSize           | TokenBucketSize    |
| PeakBandwidth             | PeakRate           |
| MinimumPolicedSize        | MinimumPolicedUnit |
| MaxSduSize                | MaximumPacketSize  |
| DelayVariation            |                    |
| Latency                   |                    |



 

 

## SenderTspec Specifics

The following items are specific to a sender's use of the RSVP Tspec in PATH messages:

-   If MaxSduSize is not specified in the Tspec included in the sender's PATH message, the RSVP SP will default to a value of 1,500 bytes.
-   If MinimumPolicedSize is not specified in the Tspec included in the sender's PATH message, the RSVP SP will default to a value of 128 bytes.

## Receiver Flowspec Specifics

For receivers, the contents of the RSVP flowspec varies depending on requested service type in the following ways:

-   [CONTROLLED LOAD](controlled-load.md) service contains a Tspec.
-   [GUARANTEED](guaranteed.md) service flowspec contains a Tspec and an Rspec.

CONTROLLED LOAD Service

Receivers requesting CONTROLLED LOAD service may decide to specify only (but at least) the ServiceType parameter in ReceivingFlowspec, setting remaining parameters to QOS\_UNSPECIFIED, in which case the RSVP SP copies the SenderTspec from the matching PATH message into the ReceiverFlowspec sent with the corresponding RESV message. In order to specify additional parameters in the ReceiverFlowspec (allowing remaining flow parameters set to QOS\_UNSPECIFIED to be derived from the SenderTspec), an application may provide values for other ReceivingFlowspec parameters.

GUARANTEED Service

When a receiver requests GUARANTEED service, the RSVP SP copies SenderTspec from the matching PATH message into the ReceiverFlowspec sent with the corresponding RESV message.

## RSVP Rspec

The RSVP Rspec specifies requested QOS parameters, and is used by the receiver in RESV messages to transmit requested reservation parameters only when GUARANTEED service is specified by the application. The Rspec derives its parameters from the ReceivingFlowspec member of a [**QOS**](qos.md) structure (ReceivingFlowspec is of type [**FLOWSPEC**](flowspec.md)).

The following table explains how parameters in ReceivingFlowspec map to Rspec parameters.



| ReceivingFlowspec parameter | Rspec          |
|-----------------------------|----------------|
| TokenRate                   | Rate           |
| TokenBucketSize             |                |
| PeakBandwidth               |                |
| MinimumPolicedSize          |                |
| MaxSduSize                  |                |
| DelayVariation              | DelaySlackTerm |
| Latency                     |                |



 

The application specifying GUARANTEED service is expected to provide two of the following three parameters:

-   TokenRate
-   DelayVariation
-   Latency

The two parameters must be provided in the following combinations:

-   TokenRate and DelayVariation
    -   or
-   DelayVariation and Latency

In other words, providing TokenRate and Latency is not acceptable. If an application fails to specify two of the three required parameters, the RSVP SP infers appropriate values based on the corresponding PATH message(s). The following table explains how the provided parameters are used by the RSVP SP to construct the RSVP Rspec.



| Application specifies:       | RSVP SP constructs Rspec:                                                                                                   |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| TokenRate and DelayVariation | Rate is copied from TokenRate DelaySlackTerm is copied from DelayVariation <br/> Latency parameter ignored<br/> |
| DelayVariation and Latency   | Rate parameter of Rspec calculated based on DelayVariation and Latency and other parameters obtained from Adspec            |



 

## RSVP Adspec

Each RSVP PATH message includes an Adspec, which enables QOS-enabled network devices in the path between sender and receiver to advertise the services they support, their resource availability and transmission characteristics. Such information can be useful in helping the receiving application select [**FLOWSPEC**](flowspec.md).

 

 





