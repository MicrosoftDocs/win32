---
UID: NE:appxdatasource.SignatureStreamFlags
title: SignatureStreamFlags
description: Defines constants that specify options for the GetSignatureFileStream method.
ms.topic: reference
tech.root: appxdatasource
ms.date: 02/08/2024
targetos: Windows
prerelease: false
req.construct-type: enumeration
req.ddi-compliance: 
req.header: appxdatasource.h
req.include-header: 
req.kmdf-ver: 
req.max-support: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - appxdatasource.h
api_name:
 - SignatureStreamFlags
f1_keywords:
 - SignatureStreamFlags
 - appxdatasource/SignatureStreamFlags
dev_langs:
 - c++
helpviewer_keywords:
 - SignatureStreamFlags
---

# SignatureStreamFlags enumeration

Defines constants that specify options for the [GetSignatureFileStream](./nf-appxdatasource-iappxstreamingdatasource4-getsignaturefilestream.md) method.

## Syntax

```cpp
typedef enum __MIDL_IAppxStreamingDataSource4_0003
{
  SignatureStreamFlagsNone = 0,
  SignatureStreamFlagsAddP7xHeader = 0x1,
} SignatureStreamFlags;
```

## Constants

| &nbsp; |
| -- |
| `SignatureStreamFlagsNone`<br> Specifies no options. |
| `SignatureStreamFlagsAddP7xHeader`<br> Add a p7x header (defined in the **P7xEditor** class) to the stream. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | appxdatasource.h |
