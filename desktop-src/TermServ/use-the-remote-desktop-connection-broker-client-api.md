---
title: How to use the Remote Desktop Connection Broker client API
description: The Remote Desktop Connection Broker client API allows third party protocol vendors to leverage the Connection Broker to expedite the handling of connections that use their protocol to connect to virtual machines or Remote Desktop servers in a farm.
ms.assetid: 05C2D6CA-C9C5-4783-B196-6A02918046EF
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# How to use the Remote Desktop Connection Broker client API

The Remote Desktop Connection Broker client API allows third party protocol vendors to leverage the Connection Broker to expedite the handling of connections that use their protocol to connect to virtual machines or Remote Desktop servers in a farm.

## Instructions

### Step 1: Obtain the IConnectionBrokerClient interface

When your application or protocol provider is initialized, perform the following steps.

1.  Call the [**CBCreateClientInstance**](cbcreateclientinstance.md) function to obtain the [**IConnectionBrokerClient**](iconnectionbrokerclient.md) interface.
2.  Keep the [**IConnectionBrokerClient**](iconnectionbrokerclient.md) interface as long as you need it.
3.  When the [**IConnectionBrokerClient**](iconnectionbrokerclient.md) interface is no longer needed, call the [**Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) method.

### Step 2: Request the target information

When your protocol provider receives an incoming connection request, perform the following steps to call the [**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) method. This method obtains, from the Connection Broker, the appropriate server to redirect the connection to.

1.  Create an event that can be signaled using the [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa), or similar function, to use for the *hStatusEvent* parameter.
2.  Allocate memory for the *pTargetInfo* and *pResult* parameters. These memory blocks must remain in place until after this entire sequence is complete.
3.  Fill out a [**CB\_CONNECTION\_INFO**](cb-connection-info.md) structure that contains all of the information about the incoming connection.
4.  Call the [**GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) method, passing all of the required parameters. This is an asynchronous method that will return an instance of the [**IConnectionBrokerRequest**](iconnectionbrokerrequest.md) interface.
5.  Wait for the *hStatusEvent* event to become set.
6.  Whenever the *hStatusEvent* event is set, call the [**IConnectionBrokerRequest::CheckStatus**](iconnectionbrokerrequest-checkstatus.md) method to determine the status of the request.
7.  When [**CheckStatus**](iconnectionbrokerrequest-checkstatus.md) returns **CB\_STATUS\_REQUEST\_COMPLETED**, the *pTargetInfo* and *pResult* parameters will contain their information. You can break out of the wait loop because the *hStatusEvent* parameter will no longer be used.
8.  Use the information in the [**CB\_TARGET\_INFO**](cb-target-info.md) structure represented by the *pTargetInfo* parameter to determine where to redirect the incoming connection to.
9.  Release the [**IConnectionBrokerRequest**](iconnectionbrokerrequest.md) interface.
10. Close the *hStatusEvent* event handle, or you can reuse it for subsequent connection requests.

 

 