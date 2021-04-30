---
description: The following code example demonstrates use of the TAPI object to examine available telephony resources for an address that can handle a specified set of media type requirements. In this example, audio and video are the required media.
ms.assetid: 8be40a87-931d-4cda-9ef7-f9c0489e0b7b
title: Select an Address
ms.topic: article
ms.date: 05/31/2018
ms.custom: project-verbatim
---

# Select an Address

The following code example demonstrates use of the TAPI object to examine available telephony resources for an address that can handle a specified set of media type requirements. In this example, audio and video are the required media.

Before using this code example, you must perform the operations in [Initialize TAPI](initialize-tapi.md).

> [!NOTE]  
> This example doesn't have the error checking and releases appropriate for production code.

```cpp
// Declare the interfaces used to select an address.
IEnumAddress * pIEnumAddress;
ITAddress * pAddress;
ITMediaSupport * pMediaSupport;

// Use the TAPI object to enumerate available addresses.
hr = gpTapi->EnumerateAddresses( &pIEnumAddress );
// If (hr != S_OK) process the error here. 

// Locate an address that can support the media type the application needs.
while ( S_OK == pIEnumAddress->Next(1, &pAddress, NULL) )
{
    // Determine the media support.
    hr = pAddress->QueryInterface(
         IID_ITMediaSupport,
         (void **)&pMediaSupport
         );
    // If (hr != S_OK) process the error here. 

    // In this example, the required media type is already known.
    // The application can also use the address object to
    // enumerate the media supported, then choose from there.
    hr = pMediaSupport->QueryMediaType(
         TAPIMEDIATYPE_AUDIO|TAPIMEDIATYPE_VIDEO,
         &bSupport
         );
    // If (hr != S_OK) process the error here. 

    if (bSupport)
    {
        break;
    }
}
// pAddress is now a usable address.
```

## Related topics

[ITTAPI::EnumerateAddresses](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-enumerateaddresses)

[ITMediaSupport](/windows/desktop/api/tapi3if/nn-tapi3if-itmediasupport)

[TAPIMEDIATYPE\_ Constants](tapimediatype--constants.md)
