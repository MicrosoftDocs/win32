---
Description: The address type identifies the format required for an address. For example, if the type is LINEADDRESSTYPE\_PHONENUMBER, the address used to dial on the session must be a phone number.
ms.assetid: bea48bde-927a-400a-9a7e-a77e30ba35eb
title: Address Type for a Session
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Address Type for a Session

The [**address type**](lineaddresstype--constants.md) identifies the format required for an address. For example, if the type is LINEADDRESSTYPE\_PHONENUMBER, the address used to dial on the session must be a phone number.

A given device and service provider supports one or more address types. See the [address types for a device](address-type-ovr.md) for information on how to poll a device for the address formats it supports.

**TAPI 2.x:** See [**lineGetCallInfo**](https://msdn.microsoft.com/en-us/library/ms735720(v=VS.85).aspx), **dwAddressType** member of [**LINECALLINFO**](https://msdn.microsoft.com/en-us/library/ms735527(v=VS.85).aspx).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong), called with the **CIL\_CALLERIDADDRESSTYPE**, **CIL\_CALLEDIDADDRESSTYPE**, or **CIL\_CONNECTEDIDADDRESSTYPE** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long).

 

 



