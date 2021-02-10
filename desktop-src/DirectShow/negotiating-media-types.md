---
description: Negotiating Media Types
ms.assetid: 9872128c-4e3d-4ac8-afc4-b3dc516a0925
title: Negotiating Media Types
ms.topic: article
ms.date: 05/31/2018
---

# Negotiating Media Types

When the Filter Graph Manager calls the [**IPin::Connect**](/windows/desktop/api/Strmif/nf-strmif-ipin-connect) method, it has several options for specifying a media type:

-   **Complete type:** If the media type is fully specified, the pins attempt to connect with that type. If they cannot, the connection attempt fails.
-   **Partial media type:** A media type is *partial* if the major type, subtype, or format type is GUID\_NULL. The value GUID\_NULL acts as a "wildcard," indicating that any value is acceptable. The pins negotiate a type that is consistent with the partial type.
-   **No media type:** If the Filter Graph Manager passes a **NULL** pointer, the pins can agree to any media type that is acceptable to both pins.

If the pins do connect, the connection always has a complete media type. The purpose of the media type given by the Filter Graph Manager is to limit the possible connection types.

During the negotiation process, the output pin proposes a media type by calling the input pin's [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) method. The input pin can accept or reject the proposed type. This process repeats until either the input pin accepts a type, or the output pin runs out of types and the connection fails.

How an output pin selects media types to propose depends on the implementation. In the DirectShow base classes, the output pin calls [**IPin::EnumMediaTypes**](/windows/desktop/api/Strmif/nf-strmif-ipin-enummediatypes) on the input pin. This method returns an enumerator that enumerates the input pin's preferred media types. Failing that, the output pin enumerates its own preferred types.

**Working with Media Types**

In any function that receives an **AM\_MEDIA\_TYPE** parameter, always validate the values of **cbFormat** and **formattype** before dereferencing the **pbFormat** member. The following code is incorrect:


```C++
if (pmt->formattype == FORMAT_VideoInfo)
{
    VIDEOINFOHEADER *pVIH = (VIDEOINFOHEADER*)pmt->pbFormat;
    // Wrong!
}
```



The following code is correct:


```C++
if ((pmt->formattype == FORMAT_VideoInfo) && 
    (pmt->cbFormat > sizeof(VIDEOINFOHEADER) &&
    (pbFormat != NULL))
{
    VIDEOINFOHEADER *pVIH = (VIDEOINFOHEADER*)pmt->pbFormat;
    // Now you can dereference pVIH.
}
```



 

 



