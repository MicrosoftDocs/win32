---
title: ITsSbTarget IpAddresses property
description: Retrieves or specifies the external IP addresses of the target.
ms.assetid: 938a753c-d541-4772-b41b-817324488685
ms.tgt_platform: multiple
keywords:
- TargetExternalIpAddresses property Remote Desktop Services
- TargetExternalIpAddresses property Remote Desktop Services , ITsSbTarget interface
- TargetExternalIpAddresses property Remote Desktop Services , ITsSbTarget interface
- IpAddresses property Remote Desktop Services
- IpAddresses property Remote Desktop Services , ITsSbTarget interface
- ITsSbTarget interface Remote Desktop Services , IpAddresses property
- IpAddresses property Remote Desktop Services , ITsSbTargetEx interface
- ITsSbTargetEx interface Remote Desktop Services , IpAddresses property
topic_type:
- apiref
api_name:
- ITsSbTarget.IpAddresses
- ITsSbTarget.get_IpAddresses
- ITsSbTarget.put_IpAddresses
- ITsSbTargetEx.IpAddresses
- ITsSbTargetEx.get_IpAddresses
- ITsSbTargetEx.put_IpAddresses
- TargetExternalIpAddresses
- ITsSbTarget.TargetExternalIpAddresses
- ITsSbTarget get_TargetExternalIpAddresses
- ITsSbTarget put_TargetExternalIpAddresses
api_location:
- Sbtsv.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbTarget::IpAddresses property

Retrieves or specifies the external IP addresses of the target.

This property is read/write.

## Syntax


```C++
HRESULT put_IpAddresses(
  [in, size_is(numAddresses)]   TSSD_ConnectionPoint *sockaddr,
  [in]                          DWORD                numAddresses
);

HRESULT get_IpAddresses(
  [out, size_is(*numAddresses)] TSSD_ConnectionPoint *sockaddr,
  [in, out]                     DWORD                *numAddresses
);
```



## Property value

A pointer to an array of [**TSSD\_ConnectionPoint**](/windows/win32/api/sessdirpublictypes/ns-sessdirpublictypes-tssd_connectionpoint) structures that receive the external IP addresses of the target.

A pointer to a **DWORD** variable that contains the number of external IP addresses in the *sockaddr* parameter. If the number of addresses is unknown, pass *sockaddr* as **NULL**. The method will return the number of [**TSSD\_ConnectionPoint**](/windows/win32/api/sessdirpublictypes/ns-sessdirpublictypes-tssd_connectionpoint) structures necessary to allocate in the array pointed to by the *sockaddr* parameter.

## Remarks

This property was formerly known as **TargetExternalIpAddresses** in Windows Server 2008 R2.

If the number of external IP addresses is unknown, you can call this method with *sockaddr* set to **NULL**. The method will then return, in the *numAddresses* parameter, the number of [**TSSD\_ConnectionPoint**](/windows/win32/api/sessdirpublictypes/ns-sessdirpublictypes-tssd_connectionpoint) structures necessary to receive all the external IP addresses. Allocate the array for *sockaddr* based on this number, and then call the method again, setting *sockaddr* to the newly allocated array and *numAddresses* to the number returned by the first call.

## Requirements




| Requirement | Value |
|--------|-------|
| Minimum supported client<br /> | None supported<br /> | 
| Minimum supported server<br /> | Windows Server 2012<br /> | 
| IDL<br /> | <dl><dt>Sbtsv.idl</dt></dl> | 
| IID<br /> | IID_ITsSbTarget is defined as:<ul><li>16616ECC-272D-411D-B324-126893033856</li><li>e85e10ea-db0b-4752-b456-5fd5840901c0 on Windows Server 2008 R2</li></ul> | 




## See also

<dl> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dt>

[**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget)
</dt> <dt>

[**TSSD\_ConnectionPoint**](/windows/win32/api/sessdirpublictypes/ns-sessdirpublictypes-tssd_connectionpoint)
</dt> </dl>

 

 





