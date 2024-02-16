---
UID: NN:appxdatasource.IAppxStreamingDataSource
title: IAppxStreamingDataSource
description: Provides access to a data source. With this interface, you can create request jobs, and request OOS ranges.
ms.topic: reference
tech.root: appxpkg
ms.date: 02/08/2024
targetos: Windows
prerelease: false
req.assembly: 
req.construct-type: iface
req.ddi-compliance: 
req.header: 
req.idl: 
req.include-header: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - AppxStreamingDataSourcePS.dll
api_name:
 - IAppxStreamingDataSource
f1_keywords:
 - IAppxStreamingDataSource
 - appxdatasource/IAppxStreamingDataSource
dev_langs:
 - c++
helpviewer_keywords:
 - IAppxStreamingDataSource
---

# IAppxStreamingDataSource interface

Provides access to a data source. With this interface, you can create request jobs, and request OOS ranges.

## Inheritance

The **IAppxStreamingDataSource** interface derives from the **IUnknown** interface.

## Methods

The **IAppxStreamingDataSource** interface has these methods.

| &nbsp; |
| ---- |
| [IAppxStreamingDataSource::CreateRangeRequestJob](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource-createrangerequestjob.md) <br><br> Creates a range request job to which ranges can be added for streaming. |
| [IAppxStreamingDataSource::GetAttributes](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource-getattributes.md) <br><br> Returns attributes information specific to the data source. |
| [IAppxStreamingDataSource::GetRangeData](../appxdatasource/nf-appxdatasource-iappxstreamingdatasource-getrangedata.md) <br><br> Requests a range of data synchronously, which is handled at the highest priority. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **DLL** | AppxStreamingDataSourcePS.dll |
