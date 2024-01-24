---
description: The SspiSetChannelBindingFlags function is exposed in both kernel and user mode drivers of SspiCli.
ms.assetid: fa15254f-7018-48dd-b55b-a03ef27e835b
title: SspiSetChannelBindingFlags function (Sspi.h)
ms.topic: reference
ms.date: 07/14/2023
req.target-type: Windows
req.header: Sspi.h
targetos: Windows
dev_langs:
 - c++
topic_type:
- APIRef
- kbSyntax
api_name:
- SspiSetChannelBindingFlags
api_type:
- HeaderDef
api_location:
- Sspi.h
---

# SspiSetChannelBindingFlags function

The **SspiSetChannelBindingFlags** function is exposed in both kernel and user mode drivers of SspiCli. This helps the server side to fetch the channel bindings from query attributes and convert it to the **ChannelBindingsEX** buffer format and set the Audit flags before passing it to the **SSPCommon** for validation during the ASC Call. Thus, EPA Audit can be enabled/disabled.

## Syntax

```cpp
SECURITY_STATUS SEC_ENTRY SspiSetChannelBindingFlags(
  Inout_ SecPkgContext_Bindings *pBindings,
  unsigned long                 flags
);
```

## Parameters

*\*pBindings* `[InOut]`

The channel bindings to be set.

*flags* `[in]`

The flags to be set, indicating your desired configuration.

## Return value

Returns **SEC_E_OK** if the function succeeds; otherwise, returns a nonzero error code.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Not supported |
| Minimum supported server | Windows Server 2019<br/>Windows Server 2022<br/>Windows Server 23H2 |
| Header | Sspi.h |

## See also

[Supporting Extended Protection for Authentication (EPA) in a service](epa-support-in-service.md)

[SecPkgContext_Bindings](/windows/win32/api/sspi/ns-sspi-secpkgcontext_bindings)
