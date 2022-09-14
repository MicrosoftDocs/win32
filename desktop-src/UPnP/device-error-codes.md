---
title: Device Error Codes
description: The InvokeAction and QueryStateVariable methods return HRESULT values that might indicate a device error (that is, an error that is received from a UPnP-certified device).
ms.assetid: 4b18a5d4-f6e8-4670-93dd-ecd012940000
ms.topic: article
ms.date: 05/31/2018
---

# Device Error Codes

The [**InvokeAction**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-invokeaction) and [**QueryStateVariable**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-querystatevariable) methods return **HRESULT** values that might indicate a device error (that is, an error that is received from a UPnP-certified device). If an error is received from a device, the method ([**InvokeAction**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-invokeaction) or [**QueryStateVariable**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-querystatevariable)) returns an **HRESULT** value that is based on the device error code, as explained in this topic. Because a conversion is applied to the device error code to produce an **HRESULT** value, you cannot read the device error code directly from the **HRESULT** value.

## Conversion of a Device Error Code to an HRESULT

There are both standard and non-standard device error codes. The standard codes have the same meaning across all UPnP-certified devices and have values that are less than 600. The non-standard codes are vendor-specific and have values ranging from 600 through 899.

Whether or not the device error code is standard determines how the **HRESULT** value is generated:

-   A standard device error code is mapped to an **HRESULT** value.

<!-- -->

-   A non-standard device error code is embedded in the **HRESULT** value by applying a formula.

Both of these procedures can be reversed to determine the device error code from a particular **HRESULT** value.

## Deriving a Device Error Code from an HRESULT Value

If the **HRESULT** value is greater than or equal to **UPNP\_E\_ACTION\_SPECIFIC\_BASE** (0x80040300) and less than or equal to **UPNP\_E\_ACTION\_SPECIFIC\_MAX** (0x8004042B), the device error code is nonstandard — use the formula in the following section to determine the error code. Otherwise, the device error code is standard — use the table in the Mapping for Standard Device Error Codes section, which provides the mapping from the **HRESULT** value to the device error code.

For a text description of the error after a call to [**IUPnPService::InvokeAction**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-invokeaction), set the *pvarRetVal* parameter to an empty array. Upon return, this parameter will contain a text description of the error, if any occurred.

### Formula for Nonstandard Device Error Codes

Use the following formula if **UPNP\_E\_ACTION\_SPECIFIC\_BASE** ≤ **HRESULT** ≤**UPNP\_E\_ACTION\_SPECIFIC\_MAX**.

Device Error Code = (**HRESULT** - **UPNP\_E\_ACTION\_SPECIFIC\_BASE**) + **FAULT\_ACTION\_SPECIFIC\_BASE**

Substituting the actual numeric values, the equation is: Device Error Code = (**HRESULT** - 0x80040300) + 0x0258

### Mapping for Standard Device Error Codes

Use the following mapping if **HRESULT** < **UPNP\_E\_ACTION\_SPECIFIC\_BASE**.



| HRESULT value                    | Device Error Code                | Actual value |
|----------------------------------|----------------------------------|--------------|
| UPNP\_E\_INVALID\_ACTION         | FAULT\_INVALID\_ACTION           | 401          |
| UPNP\_E\_INVALID\_ARGUMENTS      | FAULT\_INVALID\_ARG              | 402          |
| UPNP\_E\_OUT\_OF\_SYNC           | FAULT\_INVALID\_SEQUENCE\_NUMBER | 403          |
| UPNP\_E\_INVALID\_VARIABLE       | FAULT\_INVALID\_VARIABLE         | 404          |
| UPNP\_E\_ACTION\_REQUEST\_FAILED | FAULT\_DEVICE\_INTERNAL\_ERROR   | 501          |



 

## More Information

Device error codes are specified in "UPnP Device Architecture version 1.0". The constants mentioned in this topic are defined in the files Upnp.h and Upnp.idl.

 

 




