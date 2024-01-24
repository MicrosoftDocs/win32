---
description: Some phone sets support the notion of downloading data from or uploading data to the phone device, which allows the phone set to be programmed in a variety of ways.
ms.assetid: 5734107d-8104-4d8a-b3f7-3cc2a48f71ca
title: Data Areas
ms.topic: article
ms.date: 05/31/2018
---

# Data Areas

Some phone sets support the notion of downloading data from or uploading data to the phone device, which allows the phone set to be programmed in a variety of ways. TAPI models these phone sets as having one or more download or upload areas. Each area is identified by a number that ranges from zero to the number of data areas available on the phone minus one. Sizes of each area can vary. The format of the data itself is device-specific.

The TAPI [**phoneSetData**](/windows/desktop/api/Tapi/nf-tapi-phonesetdata) function downloads a buffer of data to a given data area in the phone device, and the [**phoneGetData**](/windows/desktop/api/Tapi/nf-tapi-phonegetdata) function uploads the contents of a given data area in the phone device to a buffer.

When a data area of a phone device is changed, a [**PHONE\_STATE**](phone-state.md) message is sent to the application to notify the application about the state change. Parameters to this message provide an indication of the change.

 

 



