---
title: /protocol switch
description: The /protocol switch specifies which wire protocol is supported by the generated stub.
ms.assetid: b565b30c-72e5-442b-9588-324b9041524b
keywords:
- /protocol switch MIDL
topic_type:
- apiref
api_name:
- /protocol
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /protocol switch

The **/protocol** switch specifies which wire protocol is supported by the generated stub.

``` syntax
midl /protocol (dce | ndr64 | all)
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="dce"></span><span id="DCE"></span>

<span id="dce"></span><span id="DCE"></span>****dce****


</dt> <dd>

The generated stub supports DCE protocol only.

</dd> <dt>

<span id="ndr64"></span><span id="NDR64"></span>

<span id="ndr64"></span><span id="NDR64"></span>****ndr64****


</dt> <dd>

The generated stub supports Microsoft NDR64 protocol only.

</dd> <dt>

<span id="all"></span><span id="ALL"></span>

<span id="all"></span><span id="ALL"></span>****all****


</dt> <dd>

The generated stub supports all available protocols for a given environment.

</dd> </dl> </dd> </dl>

## Remarks

RPC marshals and unmarshals data according to a strict wire protocol, also called transfer syntax, that defines data wire representation such as the order in which data members are marshaled, the alignment of data on the wire, additional information included with the data, among others. Microsoft RPC is compatible with OSF DCE's NDR (network data representation) protocol. In the 64-bit release of Windows XP, Microsoft introduces an experimental protocol NDR64 that is optimized for transferring 64-bit data. NDR64 is not backward compatible with the DCE protocol.

The **dce** protocol is compatible with OSF DCE's NDR transfer syntax. This protocol is optimized for transferring 32-bit data.

The **ndr64** protocol is currently supported only when used in conjunction with the [**/win64**](-win64.md) switch. If a ndr64 only client tries to connect to a dce-only server, or vice versa, the call is rejected with RPC\_S\_UNSUPPORTED\_TRANS\_SYN.

The **all** option creates a stub that may use any available protocol. For 32-bit stubs, the only protocol currently available is DCE. For 64-bit stubs, created using the [**/win64**](-win64.md) switch, both DCE and NDR64 are available.

## Examples

**midl /protocol all /win64 filename.idl**

## See also

<dl> <dt>

[**/&lt;system&gt;**](-system-.md)
</dt> </dl>

 

 




