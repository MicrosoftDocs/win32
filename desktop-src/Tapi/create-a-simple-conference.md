---
description: The following code example demonstrates the creation of a simple conference call. For information on IP multicast multimedia video conferencing, see About Rendezvous IP Telephony Conferencing.
ms.assetid: fb55853d-b882-41c8-99e6-bfa897b2dabf
title: Create a Simple Conference
ms.topic: article
ms.date: 05/31/2018
---

# Create a Simple Conference

The following code example demonstrates the creation of a simple conference call. For information on IP multicast multimedia video conferencing, see [About Rendezvous IP Telephony Conferencing](about-rendezvous-ip-telephony-conferencing.md).

Before using this code example, a call must be in progress, and you must perform the operations in [Make a Call](make-a-call.md) or [Receive a Call](receive-a-call.md) have been performed.

> [!Note]  
> This example does not have the error checking and releases appropriate for production code.

 

``` syntax
// From elsewhere in your code, you have obtained pBasicCall and pCallInfo, 
// which are pointers to the ITBasicCallControl and ITCallInfo interfaces
// of a call currently in progress. pAddress is an ITAddress pointer.

// Create a consultation call for the conference.
ITBasicCallControl *pConsultCall;
HRESULT hr = pAddress->CreateCall(
        bstrAddressToCall,
        dwAddressType,
        &pConsultCall
        );
// If ( hr != S_OK ) process the error here. 

// Move the consultation call into your conference.
// Note: If a CallHub object does not already exist, TAPI will create it.
hr = pBasicCall->Conference(
               pConsultCall,
               VARIANT_TRUE
               );
// If ( hr != S_OK ) process the error here. 

// Finish the creation of the conference.
hr = pConsultCall->Finish(FM_ASCONFERENCE);
// If ( hr != S_OK ) process the error here. 

// Assuming the Finish method succeeds, the consultation call (pConsultCall)
// may transition to the CS_DISCONNECTED state or may remain connected, 
// depending on the service provider.
//
// Get the ITCallHub interface pointer.
ITCallHub *pCallHub;
hr = pCallInfo->get_CallHub( pCallHub );
// If ( hr != S_OK ) process the error here. 

// You can use the ITCallHub interface to obtain additional information on
// the conference. Specific capabilities depend on the TSP/MSP being used.
```

## Related topics

<dl> <dt>

[**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo)
</dt> <dt>

[**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol)
</dt> <dt>

[**ITCallHub**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallhub)
</dt> </dl>

 

 



