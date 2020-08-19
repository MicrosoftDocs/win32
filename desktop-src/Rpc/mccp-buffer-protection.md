---
title: MCCP Buffer Protection
description: Starting with Windows Vista, the RPC Marshalling Engine takes further steps to try to prevent client-side buffer overruns due to returned data. This facility is called Mini Compute Conformance Protection (MCCP).
ms.assetid: 37fe743b-c64e-469d-b8f4-abab9f05c813
ms.topic: article
ms.date: 05/31/2018
---

# MCCP Buffer Protection

Starting with Windows Vista, the RPC Marshalling Engine takes further steps to try to prevent client-side buffer overruns due to returned data. This facility is called Mini Compute Conformance Protection (MCCP).

When the client passes a pointer to an existing buffer to an \[[**out**](/windows/desktop/Midl/out-idl)\] or \[[**in**](/windows/desktop/Midl/in),**out**\] parameter, returned data for that parameter is copied into the existing buffer. If the returned data is larger than the passed buffer, a buffer overrun can occur when RPC copies the returned data into the too-small buffer. See [Top-Level and Embedded Pointers](top-level-and-embedded-pointers.md).

With MCCP, RPC attempts to detect this condition and reject the call if it is detected. For buffers with a correlation value, such as \[[**size\_is**](/windows/desktop/Midl/size-is)\], if the returned data does not fit in the specified buffer size, the call is rejected and RPC\_X\_BAD\_STUB\_DATA exception is raised. For unsized strings, the call is rejected if the existing string size (length until the **null** terminator) is insufficient to hold the returned string, the call is rejected. RPC cannot detect buffer overruns in all conditions, so the developer is advised to continue to take normal precautions against buffer overruns.

If the client does not pass an existing buffer for an \[[**out**](/windows/desktop/Midl/out-idl)\] parameter, but instead passes a dereferenced pointer to **NULL**, RPC will follow normal rules to allocate a new buffer on the client’s behalf. This buffer will be allocated with sufficient space to hold the returned data.

A second protection is that for correlated parameters, RPC will enforce that a non-**null** buffer is passed when the correlation count variable is non-**null**.

``` syntax
HRESULT PassString( [in] DWORD Length, [in, unique, string, size_is( Length )]LPWSTR MyString );
```

If *MyString* is **NULL**, RPC will reject the call unless *Length* is set to 0. Note that RPC will allow *Length* to be 0 while *MyString* is non-**NULL**, and RPC will treat *MyString* as a 0-length buffer allocation.

 

 